exec(open('/home/claude/p2/scripts/build_plan.py').read())
FEAT="Heat, red light & massage ♨️😮‍💨"
CTA='Comment "PAD"\nfor the link ⬇️💕'
tail=[('sB2.mp4',1.25,3,None),('sB.mp4',0.6,2,None),('sF.mp4',2.1,4,0.6)]
def caps(hook, extra=None):
    c=[(hook,0,10 if not extra else 3)]
    if extra: c.append((extra,3,10))
    return c+[(FEAT,10,14),(CTA,14,None)]
build('lg2_v1_need',[('hS.mp4',1.3,4,1.0),('sC.mp4',0.1,2,None),('sE.mp4',0.9,1,None),('sD.mp4',0.2,2,None)]+tail,
      caps("If you have period cramps,\nyou NEED this 😱🩸"),10)
build('lg2_v2_vs',[('hB.mp4',1.3,3,1.0),('sA.mp4',0.3,1,None),('sC.mp4',0.1,2,None),('sE.mp4',0.9,1,None),('sD.mp4',0.2,2,None)]+tail,
      caps("A heating pad that burns you..\nVS.. 🤮","A pad that actually calms\nyour cramps 🥹💕"),10)
build('lg2_v3_donot',[('sA.mp4',0.0,3,None),('sC.mp4',0.1,2,None),('sE.mp4',0.9,2,None),('sD.mp4',0.2,2,None)]+tail,
      caps("Do NOT show this to a girl\nwith Endometriosis 😭🩸"),10)
build('lg2_v4_day2',[('c1.mp4',1.7,3,1.0,[{'x':86,'y':11,'w':16,'h':4},{'x':86,'y':25.5,'w':16,'h':4}]),('sA.mp4',0.3,1,None),('sC.mp4',0.1,2,None),('sE.mp4',0.9,1,None),('sD.mp4',0.2,2,None)]+tail,
      caps("POV: it's day 2 and you\nfinally found THIS 😮‍💨🩸"),10)
build('lg2_v5_bf',[('c9.mp4',1.4,4,1.0,[{'x':72,'y':24.2,'w':30,'h':3.2}]),('sC.mp4',0.1,2,None),('sE.mp4',0.9,1,None),('sD.mp4',0.2,2,None)]+tail,
      caps("My bf tried a period\ncramp simulator… then\nbought me THIS 😭"),10)
build('lg2_v6_321',[('c5.mp4',0.0,8,1.0),('c6.mp4',1.0,3,1.0),('sB.mp4',0.6,2,None),('sC.mp4',0.1,2,None),('sF.mp4',2.1,4,0.6)],
      [("3… 2… 1… what every endo\ngirl wants for Christmas 🎁🩸",0,8),(FEAT,8,15),(CTA,15,None)],8)
