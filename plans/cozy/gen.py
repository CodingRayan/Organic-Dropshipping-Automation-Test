import json
FPS=30
def build(scenes, caps, music):
    # caps: list of (text, from, to, top, size) global seconds; split into scenes
    out=[]; t=0
    for (src,start,dur,vol) in scenes:
        s={"src":src,"start":start,"duration":dur}
        if vol: s["volume"]=vol
        cs=[]
        for (txt,a,b,top,size) in caps:
            lo=max(a,t); hi=min(b,t+dur)
            if hi-lo>0.01:
                cs.append({"text":txt,"from":round(lo-t,3),"to":round(hi-t,3),"top":top,"size":size})
        if cs: s["captions"]=cs
        out.append(s); t+=dur
    return {"fps":FPS,"music":music,"scenes":out}, round(t,2)

TOP=330; SZ=58; LT=400; LSZ=62
# Template A: Problem / Vs... / Solution  (All I Want for Christmas, drop at 9.55s, cut at 9.6s)
A_sc=[("cP_problem2.mp4",0.0,3.27,1.0),("c2_install.mp4",0.6,1.56,0),("c3_buckle.mp4",1.26,2.74,0),("c4_blanket.mp4",0.5,2.03,0),
      ("c6_golden_fix.mp4",0.4,1.83,0),("c1_drive.mp4",0.0,1.7,0),("c7_overhead.mp4",0.4,1.6,0)]
A_caps=[("The Problem 🤕🚘",0,3.27,LT,LSZ),("Vs...",3.27,9.6,LT,LSZ),("The Solution 🤤❤️",9.6,99,LT,LSZ)]
B_sc=[("cI_idea2.mp4",0.3,3.37,1.0),("c2_install.mp4",0.4,2.23,0),("c3_buckle.mp4",0.0,4.0,0),
      ("c6_golden_fix.mp4",0.4,1.83,0),("c5_laugh.mp4",0.4,1.7,0),("c7_overhead.mp4",0.4,1.6,0)]
B_caps=[("The Idea 😭",0,3.37,LT,LSZ),("Vs...",3.37,9.6,LT,LSZ),("The Product 😍🎁",9.6,99,LT,LSZ)]
mA={"file":"aiwfc.mp3","start":0,"volume":1.0,"ducks":[{"from":0,"to":3.3,"volume":0.75}]}
# Template C: POV gift (Last Christmas, CTA at 9.0s)
C_sc=[("c1_drive.mp4",0.0,2.0,0),("c2_install.mp4",0.5,1.7,0),("c3_buckle.mp4",1.2,2.8,0),("c4_blanket.mp4",0.5,2.5,0),
      ("c7_overhead.mp4",0.3,1.73,0),("c5_laugh.mp4",0.5,1.87,0),("c6_golden_fix.mp4",0.6,2.7,0)]
C2_sc=[("c6_golden_fix.mp4",0.6,2.0,0),("c2_install.mp4",0.5,1.7,0),("c3_buckle.mp4",1.2,2.8,0),("c4_blanket.mp4",0.5,2.5,0),
      ("c7_overhead.mp4",0.3,1.73,0),("c5_laugh.mp4",0.5,1.87,0),("c1_drive.mp4",0.0,2.0,0)]
mC={"file":"cozy.mp3","start":0,"volume":1.0}
CTA='Comment "COZY" if you\nwant one! ❤️🫣'
hooks=[
 ("c01_perfect_gift",C_sc,'"The perfect gift for a pregnant\nwife doesn\'t exi-" 😭🫶'),
 ("c02_hide",C_sc,'HIDE this from your\npregnant wife... 🤫🤰'),
 ("c03_never_complains",C_sc,'"My pregnant wife NEVER complains\non road trips agai-" 😮‍💨🫶'),
 ("c04_send_mom_to_be",C_sc,'Send this to a mom-to-be with\na holiday drive coming up 🤰🚗'),
 ("c05_tag_thanksgiving",C2_sc,'Tag your husband before the\nThanksgiving drive 🦃🚗'),
 ("c06_pov_found",C2_sc,'POV: you\'re pregnant and he finally\nfound you a car pillow 🥹🤰'),
 ("c07_every_passenger",C2_sc,'Every pregnant passenger needs\nthis before Christmas 🎄🤰'),
 ("c08_8_months",C2_sc,'8 months pregnant on a road trip\nhits different now 😴🫶'),
]
plans={}
p,t=build(A_sc,A_caps,mA); plans["a01_problem_solution"]=(p,t)
p,t=build(B_sc,B_caps,mA); plans["b01_idea_product"]=(p,t)
for name,sc,h in hooks:
    p,t=build(sc,[(h,0,9.0,TOP,SZ),(CTA,9.0,99,TOP,SZ)],mC); plans[name]=(p,t)
for k,(p,t) in plans.items():
    json.dump(p,open(f'plans/cozy/{k}.json','w'),ensure_ascii=False,indent=1); print(k,t)
