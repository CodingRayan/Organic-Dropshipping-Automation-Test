# Facebook reel report (env META_PAGE_TOKEN, FB_PAGE_ID). Views, avg watch, retention at 1s/3s/end, social actions.
import os,json,urllib.request
T=os.environ['META_PAGE_TOKEN']; P=os.environ['FB_PAGE_ID']; G='https://graph.facebook.com/v21.0'
def get(u):
    try:
        with urllib.request.urlopen(u,timeout=60) as f: return json.load(f)
    except urllib.error.HTTPError as e: return {'error':e.read().decode()[:200]}
reels=get(f'{G}/{P}/video_reels?fields=id,created_time,views,length,description&limit=60&access_token={T}').get('data',[])
print('posted(UTC)      id                views plays avgwatch(s) len  ret@1s ret@3s ret@end  reactions/comments/shares')
for r in sorted(reels,key=lambda x:x['created_time']):
    d=get(f"{G}/{r['id']}/video_insights?access_token={T}")
    v={m['name']:m['values'][0]['value'] for m in d.get('data',[])}
    rg=v.get('post_video_retention_graph') or {}
    keys=sorted(rg,key=lambda k:int(k)) if isinstance(rg,dict) else []
    def at(frac):
        if not keys: return '-'
        k=keys[min(len(keys)-1,int(round(frac*(len(keys)-1))))]; return round(rg[k]*100)
    n=len(keys); r1=round(rg[keys[min(1,n-1)]]*100) if n else '-'; r3=round(rg[keys[min(3*n//max(1,int(r.get('length',10) or 10)),n-1)]]*100) if n else '-'
    sa=v.get('post_video_social_actions') or {}
    print(f"{r['created_time'][:16]} {r['id']:17} {r.get('views',0):>5} {v.get('fb_reels_total_plays','-'):>5} {round((v.get('post_video_avg_time_watched') or 0)/1000,1):>10} {round(r.get('length') or 0,1):>4} {r1:>6} {r3:>6} {at(1.0):>7}  {v.get('post_video_likes_by_reaction_type') or {}} {sa}")
