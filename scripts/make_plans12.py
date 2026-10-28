exec(open('/home/claude/p2/scripts/make_plans10.py').read().split("s=[R,PUT,LIGHTS,RELIEF,TUCK,END]")[0])
DESK=('k8desk.mp4',0.5,1.8); CAROK=('k9carok.mp4',0.0,1.8)
def story(name,scenes,hook,pay,pay_idx):
    st=[];t=0
    for sc in scenes: st.append(t); t+=round(sc[2]*30)/30
    caps=[(hook,0,'drop'),(FEAT,'drop',st[pay_idx]),(pay,st[pay_idx],st[pay_idx+1])]
    if pay_idx+1<len(scenes)-1: caps.append((FEAT,st[pay_idx+1],st[-1]))
    caps.append((CTA,st[-1],None))
    build(name,scenes,caps,2,0.45)
story('lg12_01_work_story',[R,BTN,LIGHTS,DESK,END],"POV: your cramps hit\nin the middle of work 😭🩸","Now I wear it at my desk 🤫\n(runs on a power bank) 🔋",3)
story('lg12_02_car_story',[CAR,PUT,LIGHTS,CAROK,END],"When your cramps are so bad\nyou can't even drive 😭","Now it lives in my car 🚗💕",3)
story('lg12_03_work_tag',[R,HAND,LIGHTS,DESK,LAUGH,END],"Tag the girl who hides\nin the bathroom at work 😭","Now she can wear it\nat her desk instead 🤫💕",3)
