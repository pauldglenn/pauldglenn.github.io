#!/usr/bin/env python3
"""Validate the reviewed catalog and embed identical selections in game and score API."""
import argparse,json,re,hashlib
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
PUBLIC_FIELDS=['id','batter','date','matchup','base','strike','start','end','umpire','context','evidence','source','video','availableFrom','footageCredit']
API_FIELDS=['id','batter','date','base','strike','evidence','availableFrom','mediaProvider']
def validate(rows):
    seen=set();seen_pitches=set()
    for row in rows:
        identity=row.get('id');assert isinstance(identity,str) and re.fullmatch(r'[a-z0-9_-]+',identity), 'Invalid clip ID'
        assert identity not in seen,'Duplicate clip ID: '+identity;seen.add(identity)
        pitch=row.get('pitchIdentity')
        if pitch:
            assert type(pitch.get('gamePk')) is int and pitch['gamePk']>0 and re.fullmatch(r'[a-f0-9]{8}(?:-[a-f0-9]{4}){3}-[a-f0-9]{12}',pitch.get('playId','')),'Invalid exact pitch identity: '+identity
            key=(pitch['gamePk'],pitch['playId']);assert key not in seen_pitches,'Duplicate exact pitch: '+identity;seen_pitches.add(key)
        assert row['base'] in (1,3) and type(row['strike']) is bool,'Invalid ruling/base: '+identity
        assert isinstance(row['start'],(int,float)) and isinstance(row['end'],(int,float)) and 0<=row['start']<row['end'],'Invalid playback window: '+identity
        assert row['end']-row['start']<=15,'Excessively long window: '+identity
        assert re.fullmatch(r'\d{4}-\d{2}-\d{2}',row['date']),'Invalid date: '+identity
        if row.get('availableFrom'):assert re.fullmatch(r'\d{4}-\d{2}-\d{2}',row['availableFrom']),'Invalid activation date'
        for field in ['evidence','source','video']:
            u=urlparse(row[field]);assert u.scheme=='https' and u.hostname,'Invalid source URL'
        host=urlparse(row['video']).hostname
        if host=='pdglenn.com':
            u=urlparse(row['video']);assert u.path=='/check-swing/assets/'+identity+'.mp4' and not u.query and not u.fragment,'Invalid excerpt asset URL'
            origin=urlparse(row.get('transcodedFrom',''));assert origin.scheme=='https' and origin.hostname=='blogs.fangraphs.com','Unapproved excerpt source'
            asset=ROOT/'content/check-swing/assets'/(identity+'.mp4');provenance=row.get('provenance',{})
            assert asset.is_file() and hashlib.sha256(asset.read_bytes()).hexdigest()==provenance.get('outputSha256'),'Excerpt asset missing or changed'
            assert row.get('footageCredit') and provenance.get('frameTimingVerified') is True,'Excerpt attribution/timing evidence required'
        elif host=='mlb.com' or host.endswith('.mlb.com'):
            assert urlparse(row['video']).path.endswith('.mp4'),'Expected reviewed MLB MP4 playback: '+identity
        elif host=='video.twimg.com':
            u=urlparse(row['video']);origin=urlparse(row['source'])
            assert re.fullmatch(r'/amplify_video/\d+/vid/avc1/\d+x\d+/[A-Za-z0-9_-]+\.mp4',u.path) and not u.query and not u.fragment,'Invalid reviewed broadcast rendition: '+identity
            assert origin.hostname in ['x.com','twitter.com'] and re.fullmatch(r'/TalkinBaseball_/status/\d+',origin.path),'Missing public broadcast source: '+identity
            assert row.get('footageCredit'),'Broadcast attribution required: '+identity
        elif not (host=='mlb.com' or host.endswith('.mlb.com')):
            m=row.get('mediaProvider',{});u=urlparse(row['video'])
            assert u.netloc=='did-he-go-scores.paul-glenn280578.chatgpt.site' and u.path=='/media/'+identity and not u.query,'Invalid managed media URL: '+identity
            if m.get('provider')=='brightcove':
                assert m.get('accountId')=='1704050871' and m.get('playerId')=='JCdte3tMv','Unapproved broadcaster: '+identity
                assert re.fullmatch(r'\d+',m.get('videoId','')) and m.get('durationMs',0)>row['end']*1000,'Invalid source identity: '+identity
                assert m.get('sourcePath','').startswith('/media/v1/pmp4/static/clear/1704050871/') and m['sourcePath'].endswith('.mp4'),'Invalid reviewed source path: '+identity
            elif m.get('provider')=='streamable':
                vid=m.get('videoId','');assert re.fullmatch(r'[a-z0-9]{3,12}',vid),'Invalid video identity'
                assert m.get('sourceHost') in ['cdn-cf-east.streamable.com','cdn-cf-west.streamable.com'],'Unapproved video host'
                assert re.fullmatch(r'/video/mp4/'+vid+r'(?:_\d+)?\.mp4',m.get('sourcePath','')),'Invalid reviewed path'
                spec=m.get('selectedSource',{});assert spec.get('duration',0)>row['end'] and spec.get('size',0)>0 and spec.get('framerate',0)>0,'Missing reviewed video properties'
            else:raise AssertionError('Unapproved media provider: '+identity)
            assert m.get('selectedSource',{}).get('container')=='MP4' and m['selectedSource'].get('width',0)>0,'Missing reviewed rendition: '+identity
        for field in ['batter','matchup','umpire','context']:assert isinstance(row[field],str) and row[field].strip(),'Missing '+field
    assert len(rows)>=6,'Do not remove the original catalog'
def embed(path,rows,check):
    source=path.read_text();replacement='const CLIPS='+json.dumps(rows,ensure_ascii=False,separators=(',',':'))+';'
    updated,n=re.subn(r'const CLIPS=\[.*?\];',lambda _:replacement,source,count=1,flags=re.S)
    assert n==1,'Could not locate catalog in '+str(path)
    if check:assert source==updated,'Embedded catalog out of sync: '+str(path)
    else:path.write_text(updated)
def main():
    p=argparse.ArgumentParser();p.add_argument('--catalog',type=Path,default=ROOT/'content/check-swing/catalog.json');p.add_argument('--backend',type=Path);p.add_argument('--check',action='store_true');args=p.parse_args()
    rows=json.loads(args.catalog.read_text());validate(rows)
    embed(ROOT/'content/check-swing/index.html',[{k:r[k] for k in PUBLIC_FIELDS if k in r} for r in rows],args.check)
    if args.backend:embed(args.backend/'worker/index.js',[{k:r[k] for k in API_FIELDS if k in r} for r in rows],args.check)
    print(('Checked' if args.check else 'Synced'),len(rows),'reviewed clips')
if __name__=='__main__':main()
