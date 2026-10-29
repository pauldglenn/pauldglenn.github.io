#!/usr/bin/env python3
"""Build a review queue from public MLB search pages and Close Call Sports feeds.
Metadata only: does not download video, infer final rulings, or publish candidates.
Run: python scripts/discover-check-swings.py --output docs/check-swing-catalog
"""
import argparse, collections, concurrent.futures, datetime, html, json, re, subprocess, time
from pathlib import Path
from urllib.parse import urlencode

QUERIES=['check swing','checked swing','check-swing','swing appeal','held up','check swing ejected']
def fetch(url):
    for attempt in range(3):
        result=subprocess.run(['curl','-fsSL','--max-time','45',url],capture_output=True,text=True)
        if result.returncode==0:return result.stdout
        if attempt<2:time.sleep(1+attempt)
    raise RuntimeError('Fetch failed: '+url)
def clean(value):
    return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]*>',' ',value))).strip()
def mlb_page(query,page):
    url='https://www.mlb.com/search?'+urlencode({'q':query,'filter':'video','page':page})
    raw=fetch(url);match=re.search(r'<script id="initial-data" type="application/json">(.*?)</script>',raw,re.S)
    if not match:raise ValueError('MLB search format changed: '+url)
    props=json.loads(json.loads(match.group(1))['initState'])['appState']['searchProps']
    return props['resultsState']['rawResults'][0]
def ccs_page(page):
    url='https://www.closecallsports.com/feeds/posts/default?'+urlencode({'alt':'json','max-results':150,'start-index':1+150*(page-1),'q':'"check swing"'})
    return json.loads(fetch(url)).get('feed',{}).get('entry',[])
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--ccs-pages',type=int,default=7);args=ap.parse_args();args.output.mkdir(parents=True,exist_ok=True)
    videos={};reports={};searches=[];errors=[]
    for query in QUERIES:
        try:
            first=mlb_page(query,1);pages=min(first['nbPages'],20);searches.append({'query':query,'reported_hits':first['nbHits'],'pages_scanned':pages,'count_is_exhaustive':first.get('exhaustiveNbHits',False)})
            results=[first]
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:results+=list(pool.map(lambda page:mlb_page(query,page),range(2,pages+1)))
            for result in results:
                for hit in result['hits']:
                    if hit.get('contentType')!='video':continue
                    url=hit['url'];row=videos.setdefault(url,{'source':url,'title':hit['title'],'description':hit.get('description',''),'published':datetime.datetime.fromtimestamp(hit['contentDate']/1000,datetime.timezone.utc).date().isoformat(),'duration':hit.get('duration'),'players':hit.get('playerName',[]),'queries':[],'review_status':'unreviewed','angle':None,'strike':None,'start':None,'end':None,'ruling_source':None})
                    if query not in row['queries']:row['queries'].append(query)
            print('MLB',query,first['nbHits'],'reported;',len(videos),'unique accumulated',flush=True)
        except Exception as error:errors.append(str(error))
    for page in range(1,args.ccs_pages+1):
        try:
            entries=ccs_page(page)
            if not entries:break
            for entry in entries:
                raw=entry.get('content',{}).get('$t','');text=clean(raw)
                if not re.search(r'check(?:ed)?[ -]swing',text,re.I):continue
                url=next((link['href'] for link in entry.get('link',[]) if link.get('rel')=='alternate'),None)
                if not url:continue
                links=list(dict.fromkeys(html.unescape(link) for link in re.findall(r'(?:href|src)=["\']([^"\']+)',raw)))
                relevant=[link for link in links if any(host in link for host in ['mlb.com/video/','mlb.com/gameday/','youtube.com/','youtu.be/','baseballsavant.mlb.com/'])]
                reports[url]={'source':url,'title':entry['title']['$t'],'published':entry['published']['$t'][:10],'excerpt':text[:650],'priority':'high' if re.search(r'check(?:ed)?[ -]swing',text[:500],re.I) else 'low','video_or_game_links':relevant,'review_status':'unreviewed','strike':None,'base':None}
            print('CCS page',page,len(entries),'entries;',len(reports),'unique matching reports',flush=True)
        except Exception as error:errors.append(str(error));break
    counts=collections.Counter(u for row in reports.values() for u in set(row['video_or_game_links']))
    for row in reports.values():row['video_or_game_links']=[u for u in row['video_or_game_links'] if counts[u]<5]
    video_rows=sorted(videos.values(),key=lambda row:row['published'],reverse=True);report_rows=sorted(reports.values(),key=lambda row:row['published'],reverse=True)
    summary={'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mlb_video_candidates':len(video_rows),'ccs_matching_reports':len(report_rows),'ccs_high_priority_reports':sum(x['priority']=='high' for x in report_rows),'ccs_reports_with_video_or_game_links':sum(bool(x['video_or_game_links']) for x in report_rows),'searches':searches,'errors':errors,'warning':'Candidates are not approved game clips. Review footage, side angle, time window, swing ruling, and redistribution permissions separately. Search counts are not a census of check swings.'}
    for name,data in [('review-priority.json',[x for x in report_rows if x['priority']=='high']),('mlb-candidates.json',video_rows),('ruling-candidates.json',report_rows),('discovery-summary.json',summary)]:
        (args.output/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(summary,indent=2),flush=True)
if __name__=='__main__':main()
