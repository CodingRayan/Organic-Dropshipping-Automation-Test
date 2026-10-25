# Builds a Remotion plan where every cut lands on a real beat of the song.
# segs: list of (clip, clip_start_seconds, n_beats, volume_or_None)
# caps: list of (text, from_beat, to_beat)  (to_beat None = end)
import json, numpy as np, sys
import os
SONG=os.environ.get('SONG','stars')
BEATS=np.load('/home/claude/p2/audio/stars_beats.npy') if SONG=='stars' else np.load('/home/claude/p2/audio/beats.npy')
DROP=40.56 if SONG=='stars' else 79.65
DROP_BEAT=40.57 if SONG=='stars' else 79.668
SONGFILE='stars.mp3' if SONG=='stars' else 'hate.mp3'
def build(name, segs, caps, drop_beat, pre=0.45, post=0.8, top=330):
    # index of the beat at the drop
    di=int(np.argmin(abs(BEATS-DROP_BEAT)))
    start_i=di-drop_beat
    S=BEATS[start_i]-0.02 if drop_beat else DROP
    S=DROP-(BEATS[di]-BEATS[start_i])  # make drop land exactly on the cut at drop_beat
    t=lambda k: round((BEATS[start_i+k]-BEATS[start_i])*30)/30  # beat k snapped to a whole frame (30fps) so cuts never drift
    scenes=[]; k=0
    for seg in segs:
        clip,cs,n,vol=seg[:4]; blurs=seg[4] if len(seg)>4 else None
        d=round(t(k+n)-t(k),3)
        sc={"src":clip,"start":cs,"duration":d,"captions":[]}
        if vol: sc["volume"]=vol
        if blurs: sc["blurs"]=blurs
        sc["_b0"]=k; sc["_b1"]=k+n; scenes.append(sc); k+=n
    total_b=k
    for text,b0,b1 in caps:
        b1=total_b if b1 is None else b1
        for sc in scenes:
            lo=max(b0,sc["_b0"]); hi=min(b1,sc["_b1"])
            if lo<hi:
                c={"text":text,"top":top}
                f=t(lo)-t(sc["_b0"]); to=t(hi)-t(sc["_b0"])
                if f>0.001: c["from"]=round(f,3)
                if to<sc["duration"]-0.001: c["to"]=round(to,3)
                sc["captions"].append(c)
    for sc in scenes: sc.pop("_b0"); sc.pop("_b1")
    plan={"fps":30,"music":{"file":SONGFILE,"dropAt":DROP,"popAt":round(t(drop_beat),3),"volume":pre,"dropVolume":post},"scenes":scenes}
    json.dump(plan,open(f'/home/claude/organic-dropshipping-automation-test/plans/{name}.json','w'),ensure_ascii=False,indent=1)
    print(name, 'length %.2fs'%t(total_b), 'drop at %.2fs'%t(drop_beat), 'song starts %.2f'%(DROP-t(drop_beat)))
