exec(open('/home/claude/p2/scripts/make_plans10.py').read().split("s=[R,PUT,LIGHTS,RELIEF,TUCK,END]")[0])
TEA=('k6teaN.mp4',2.5,1.6,1.0); PILLS=('k7pillsN.mp4',2.3,1.8,1.0)
def rank(name,scenes,labels):
    # labels: list of rating lines for scenes before the lights scene; lights scene index = len(labels)
    st=[];t=0
    for sc in scenes: st.append(t); t+=round(sc[2]*30)/30
    H="Rating period cramp hacks 🩸\n"
    li=len(labels); drop=st[li]+round(0.45*30)/30
    caps=[(H+l,st[i],st[i+1]) for i,l in enumerate(labels)]
    caps+=[(H+"This pad: 🤔",st[li],drop),(H+"This pad: 10/10 🥹💕",drop,st[-1]),(CTA,st[-1],None)]
    build(name,scenes,caps,li,0.45,hook_scenes=1)
rank('lg11_01_rating',[('n1burnL.mp4',1.3,2.0,1.0),TEA,PILLS,LIGHTS,RELIEF,END],["Hot water bottle: 1/10 🤮","Period tea: 3/10 😐","Pain pills: 5/10 😣"])
rank('lg11_02_rating_b',[('k5burnN.mp4',1.6,2.0,1.0),PILLS,TEA,LIGHTS,LAUGH,END],["Plug-in heating pad: 2/10 🤮","Pain pills: 5/10 😣","Period tea: 3/10 😐"])
