import os,sys,time,json,urllib.request,urllib.parse
G='https://graph.facebook.com/v21.0'
PT=os.environ['META_PAGE_TOKEN']; PAGE=os.environ['FB_PAGE_ID']; IG=os.environ['IG_ID']
CAP='Comment “PAD” for the link 💕'
def req(url,data=None,headers=None,method=None):
    if data is not None: data=urllib.parse.urlencode(data).encode()
    r=urllib.request.Request(url,data=data,headers=headers or {},method=method)
    try:
        with urllib.request.urlopen(r,timeout=120) as f: return json.load(f)
    except urllib.error.HTTPError as e: return {'error':e.read().decode()[:400]}
def ig(url):
    c=req(f'{G}/{IG}/media',{'media_type':'REELS','video_url':url,'caption':CAP,'share_to_feed':'true','access_token':PT})
    if 'id' not in c: return 'IG create fail '+str(c)
    for _ in range(60):
        s=req(f"{G}/{c['id']}?fields=status_code,status&access_token={PT}")
        if s.get('status_code')=='FINISHED': break
        if s.get('status_code')=='ERROR': return 'IG processing error '+str(s)
        time.sleep(5)
    p=req(f'{G}/{IG}/media_publish',{'creation_id':c['id'],'access_token':PT})
    return 'IG ok '+str(p.get('id',p))
def fb(url):
    s=req(f'{G}/{PAGE}/video_reels',{'upload_phase':'start','access_token':PT})
    if 'video_id' not in s: return 'FB start fail '+str(s)
    v=s['video_id']
    b=open(url,'rb').read()
    r=urllib.request.Request(f'https://rupload.facebook.com/video-upload/v21.0/{v}',data=b,headers={'Authorization':'OAuth '+PT,'offset':'0','file_size':str(len(b))},method='POST')
    try:
        with urllib.request.urlopen(r,timeout=300) as fh: u=json.load(fh)
    except urllib.error.HTTPError as e: u={'error':e.read().decode()[:400]}
    if not u.get('success'): return 'FB upload fail '+str(u)
    f=req(f'{G}/{PAGE}/video_reels',{'upload_phase':'finish','video_id':v,'video_state':'PUBLISHED','description':CAP,'access_token':PT})
    return 'FB ok '+v if f.get('success') else 'FB finish fail '+str(f)
mode,url=sys.argv[1],sys.argv[2].replace('dl=0','dl=1')
print(ig(url) if mode=='ig' else fb(url))
