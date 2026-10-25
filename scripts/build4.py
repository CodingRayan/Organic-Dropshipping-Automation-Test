# Natural clip lengths; only the beat drop is synced (the drop lands at a chosen moment inside one scene).
import json
SONG={'stars':40.56}
def build(name, scenes, caps, drop_scene, drop_in_scene, song='stars', pre=0.55, duck=0.4, post=0.85, end_duck=0.45, hook_scenes=1):
    fps=30; out=[]; t=0.0; starts=[]
    for sc in scenes:
        clip,cs,d=sc[0],sc[1],sc[2]; vol=sc[3] if len(sc)>3 else None; blurs=sc[4] if len(sc)>4 else None
        fr=round(d*fps); starts.append(t); s={"src":clip,"start":cs,"duration":fr/fps,"captions":[]}
        if vol: s["volume"]=vol
        if blurs: s["blurs"]=blurs
        out.append(s); t+=fr/fps
    total=t
    drop_t=starts[drop_scene]+round(drop_in_scene*fps)/fps
    for text,a,b in caps:   # a,b in video seconds; b None = end; 'drop' allowed
        a=drop_t if a=='drop' else a; b=total if b is None else (drop_t if b=='drop' else b)
        for i,s in enumerate(out):
            s0=starts[i]; s1=s0+s["duration"]; lo=max(a,s0); hi=min(b,s1)
            if hi-lo>0.01:
                c={"text":text,"top":330}
                if lo-s0>0.01: c["from"]=round(lo-s0,3)
                if s1-hi>0.01: c["to"]=round(hi-s0,3)
                s["captions"].append(c)
    hook_end=starts[hook_scenes]
    last0=starts[-1]
    plan={"fps":fps,"music":{"file":song+".mp3","dropAt":SONG[song],"popAt":round(drop_t,3),"volume":pre,"dropVolume":post,"ducks":[{"from":0,"to":round(hook_end,3),"volume":duck},{"from":round(last0,3),"to":round(total,3),"volume":end_duck}]},"scenes":out}
    json.dump(plan,open(f'/home/claude/organic-dropshipping-automation-test/plans/{name}.json','w'),ensure_ascii=False,indent=1)
    print(f'{name}: {len(out)} clips, {total:.2f}s, drop at {drop_t:.2f}s, hook {hook_end:.2f}s')
