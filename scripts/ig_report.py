# Instagram reel report via Instagram-login token (env IG_LOGIN_TOKEN). Prints one row per reel.
import os,json,urllib.request,datetime
T=os.environ['IG_LOGIN_TOKEN']; G='https://graph.instagram.com/v21.0'
def get(u):
    try:
        with urllib.request.urlopen(u,timeout=60) as f: return json.load(f)
    except urllib.error.HTTPError as e: return {'error':e.read().decode()[:200]}
media=get(f'{G}/me/media?fields=id,timestamp,permalink,caption&limit=50&access_token={T}').get('data',[])
M='views,reach,likes,comments,shares,saved,ig_reels_avg_watch_time,reels_skip_rate'
rows=[]
for m in media:
    d=get(f"{G}/{m['id']}/insights?metric={M}&access_token={T}")
    v={x['name']:x['values'][0]['value'] for x in d.get('data',[])}
    rows.append((m['timestamp'][:16],m['permalink'].rstrip('/').split('/')[-1],v))
print('posted(UTC)       reel         views reach likes cmts shares saves avgwatch(s) skip%')
for ts,code,v in sorted(rows):
    print(f"{ts}  {code:12} {v.get('views','-'):>5} {v.get('reach','-'):>5} {v.get('likes','-'):>5} {v.get('comments','-'):>4} {v.get('shares','-'):>6} {v.get('saved','-'):>5} {round(v.get('ig_reels_avg_watch_time',0)/1000,1):>10} {v.get('reels_skip_rate','-'):>5}")
