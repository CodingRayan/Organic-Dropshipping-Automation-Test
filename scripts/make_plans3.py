exec(open('/home/claude/p2/scripts/build_plan.py').read())
FEAT="Heat, red light & massage ♨️😮‍💨"
CTA='Comment "PAD"\nfor the link ⬇️💕'
# drop at beat 13: lights switch on 1 beat into sB2 (switch happens 1.875s into that clip)
tail=[('sB2.mp4',1.25,4,None),('sF.mp4',2.1,5,0.6)]
def caps(hook, extra=None, split=4):
    c=[(hook,0,13 if not extra else split)]
    if extra: c.append((extra,split,13))
    return c+[(FEAT,13,16),(CTA,16,None)]
build('lg3_v1_need',[('hSL.mp4',1.2,4,1.0),('sA.mp4',0.2,3,None),('sC.mp4',0.0,3,None),('sD.mp4',0.2,2,None)]+tail,
      caps("If you have period cramps,\nyou NEED this 😱🩸"),13)
build('lg3_v2_vs',[('hBL.mp4',0.8,4,1.0),('sA.mp4',0.2,3,None),('sC.mp4',0.0,3,None),('sD.mp4',0.2,2,None)]+tail,
      caps("A heating pad that burns you..\nVS.. 🤮","A pad that actually calms\nyour cramps 🥹💕"),13)
build('lg3_v3_donot',[('sA.mp4',0.0,4,None),('sC.mp4',0.0,3,None),('sE.mp4',0.5,3,None),('sD.mp4',0.2,2,None)]+tail,
      caps("Do NOT show this to a girl\nwith Endometriosis 😭🩸"),13)
build('lg3_v4_day2',[('c1L.mp4',1.2,4,1.0,[{'x':86,'y':11,'w':16,'h':4},{'x':86,'y':25.5,'w':16,'h':4}]),('sA.mp4',0.2,3,None),('sC.mp4',0.0,3,None),('sD.mp4',0.2,2,None)]+tail,
      caps("POV: it's day 2 and you\nfinally found THIS 😮‍💨🩸"),13)
build('lg3_v5_bf',[('c9L.mp4',1.4,4,1.0,[{'x':72,'y':24.2,'w':30,'h':3.2}]),('sC.mp4',0.0,3,None),('sE.mp4',0.5,3,None),('sD.mp4',0.2,2,None)]+tail,
      caps("My bf tried a period\ncramp simulator… then\nbought me THIS 😭"),13)
build('lg3_v6_gift',[('c5L.mp4',0.0,8,1.0),('c6L.mp4',1.0,4,1.0),('sB.mp4',0.6,3,None),('sF.mp4',2.1,5,0.6)],
      [("What every endo girl wants\nfor Christmas 🎁🩸",0,8),(FEAT,8,15),(CTA,15,None)],8)
