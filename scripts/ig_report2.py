# IG report for any account via Facebook-login page token. Usage: ig_report2.py IG_ID PAGE_TOKEN
import sys,json,urllib.request
IG,T=sys.argv[1],sys.argv[2]; G='https://graph.facebook.com/v21.0'
u=f'{G}/{IG}/media?fields=id,timestamp,permalink,insights.metric(views,reach,likes,comments,shares,saved,ig_reels_avg_watch_time,reels_skip_rate)&limit=100&access_token={T}'
rows=[]
while u:
    d=json.load(urllib.request.urlopen(u,timeout=60))
    for m in d['data']:
        v={x['name']:x['values'][0]['value'] for x in m.get('insights',{}).get('data',[])}
        rows.append((m['timestamp'][:16],m['permalink'].rstrip('/').split('/')[-1],v))
    u=d.get('paging',{}).get('next')
for ts,c,v in sorted(rows):
    print(f"{ts} {c:12} {v.get('views',0):>5} {v.get('reach',0):>5} lk{v.get('likes',0):>2} cm{v.get('comments',0):>2} sh{v.get('shares',0):>2} sv{v.get('saved',0):>2} {round(v.get('ig_reels_avg_watch_time',0)/1000,1):>5}s skip{v.get('reels_skip_rate',0):>5}")
