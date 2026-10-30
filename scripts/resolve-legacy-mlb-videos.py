#!/usr/bin/env python3
"""Resolve public legacy MLB video IDs into review leads, never approved clips.
Retain every MP4 rendition: alternate bitrates can contain different edits/timings.
Input: JSON array of discovery reports with source and video_or_game_links (or links).
"""
import argparse,concurrent.futures,json,re,subprocess
from pathlib import Path
from urllib.parse import urlparse,parse_qs

def video_ids(links):
    found=set()
    for link in links:
        u=urlparse(link)
        if not u.hostname or not (u.hostname=='mlb.com' or u.hostname.endswith('.mlb.com')):continue
        match=re.search(r'/video/(?:v|c|[^/?#]+-c)(\d+)(?:[/?#]|$)',u.path)
        if match:found.add(match.group(1))
        for value in parse_qs(u.query).get('content_id',[]):
            if value.isdigit():found.add(value)
    return found

def resolve(item):
    identity,reports=item;url=f'https://content.mlb.com/mlb/item/id/v1/{identity}/details/web-v1.json'
    run=subprocess.run(['curl','-fsSL','--max-time','30',url],capture_output=True,text=True)
    result={'videoId':identity,'metadataUrl':url,'reports':reports,'reviewStatus':'unreviewed'}
    if run.returncode:return {**result,'error':'Public metadata fetch failed','curlExitCode':run.returncode}
    try:doc=json.loads(run.stdout)
    except ValueError:return {**result,'error':'Metadata was not JSON'}
    playbacks=[]
    for row in doc.get('playbacks',[]):
        playback=row.get('url','');u=urlparse(playback)
        if u.hostname and (u.hostname=='mlb.com' or u.hostname.endswith('.mlb.com')) and u.path.endswith('.mp4'):
            playbacks.append(row)
    return {**result,'title':doc.get('title'),'description':doc.get('description'),'date':doc.get('date'),'gamePks':[r['value'] for r in doc.get('keywordsAll',[]) if r.get('type')=='game_pk'],'playbacks':playbacks}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--input',required=True,type=Path);parser.add_argument('--output',required=True,type=Path);parser.add_argument('--limit',type=int,default=200);args=parser.parse_args()
    if not 1<=args.limit<=500:parser.error('--limit must be between 1 and 500')
    references={}
    for report in json.loads(args.input.read_text()):
        links=report.get('video_or_game_links',report.get('links',[]))
        for identity in video_ids(links):
            references.setdefault(identity,[]).append(report.get('source',report.get('report')))
    jobs=sorted(references.items())[:args.limit]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(resolve,jobs))
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'uniqueIdsFound':len(references),'resolved':len(results),'withMp4Renditions':sum(bool(r.get('playbacks')) for r in results),'warning':'Unreviewed metadata leads. Verify exact rendition, playable motion, angle, event identity and ruling before publishing.'}))
if __name__=='__main__':main()
