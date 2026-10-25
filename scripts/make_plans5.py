exec(open('/home/claude/p2/scripts/build4.py').read())
FEAT="Heat, Massage\n& Relief ♨️😮‍💨"
CTA='Comment "PAD"\nfor the link ⬇️💕'
# lights switch on 1.875s into sB2; cut in 0.45s before it so the switch is the drop, hold 0.75s after so it never looks like a still
LIGHTS=('sB2.mp4',1.425,1.2)
C2B=[{'x':62,'y':11,'w':50,'h':19}]
END=[('sB.mp4',0.6,1.3),('c4N.mp4',2.0,1.5,0.8),('c2N.mp4',1.2,1.8,1.0,C2B),('endfixL.mp4',1.9,3.0,1.0)]
END_V1=[('sB.mp4',0.6,1.3),('c10.mp4',1.0,1.8),('c2N.mp4',1.2,1.8,1.0,C2B),('endfixL.mp4',1.9,3.0,1.0)]
END_B=[('sB.mp4',0.6,1.3),('c2N.mp4',1.2,1.8,1.0,C2B),('c4N.mp4',2.0,1.5,0.8),('endfixL.mp4',1.9,3.0,1.0)]
def caps(hook, second=None, hook_len=2.0):
    c=[(hook,0,hook_len if second else 'drop')]
    if second: c.append((second,hook_len,'drop'))
    return c
def std_caps(scenes): # FEAT from drop to the selfie, CTA on the selfie
    end_start=sum(round(x[2]*30)/30 for x in scenes[:-1])
    return [(FEAT,'drop',end_start),(CTA,end_start,None)]
TVB=[{'x':55,'y':6,'w':62,'h':18},{'x':47,'y':22.3,'w':66,'h':6}]
v1=[('hSN.mp4',1.4,2.3,1.0),('sC.mp4',0.0,1.5),('sD.mp4',0.2,1.2),LIGHTS]+END_V1
build('lg5_v1_need',v1,caps("If you have period cramps,\nyou NEED this 😱🩸")+std_caps(v1),3,0.45)
v2=[('n1burnL.mp4',2.0,2.0,1.0),('sA.mp4',0.3,1.2),('sC.mp4',0.0,1.5),LIGHTS]+END_B
build('lg5_v2_vs',v2,caps("A heating pad that burns you..\nVS.. 🤮","A pad that actually calms\nyour cramps 🥹💕")+std_caps(v2),3,0.45)
v3=[('n2snatchL.mp4',3.2,1.8,1.0),('sC.mp4',0.0,1.5),('sE.mp4',0.5,1.1),LIGHTS]+END
build('lg5_v3_donot',v3,caps("Do NOT show this to a girl\nwith Endometriosis 😭🩸")+std_caps(v3),3,0.45)
v4=[('n3bathL.mp4',0.8,2.05,1.0),('sA.mp4',0.3,1.2),('sC.mp4',0.0,1.5),LIGHTS]+END_B
build('lg5_v4_day2',v4,caps("POV: it's day 2 and you\nfinally found THIS 😮‍💨🩸")+std_caps(v4),3,0.45)
v5=[('n4bfL.mp4',2.1,2.4,1.0,TVB),('sC.mp4',0.0,1.5),('sD.mp4',0.2,1.2),LIGHTS]+END
build('lg5_v5_bf',v5,caps("My bf tried a period\ncramp simulator… then\nbought me THIS 😭")+std_caps(v5),3,0.45)
# 3-2-1 as quick jump cuts (she says three / two / one), reveal on the drop
v6=[('c5N.mp4',0.9,0.85,1.0),('c5N.mp4',2.5,0.85,1.0),('c5N.mp4',4.2,0.75,1.0),('c6N.mp4',1.2,1.8,1.0),('sB.mp4',0.6,1.3),('sC.mp4',0.0,1.5),('c2N.mp4',1.2,1.8,1.0,C2B),('endfixL.mp4',1.9,3.0,1.0)]
build('lg5_v6_gift',v6,[("What every endo girl wants\nfor Christmas 🎁🩸",0,'drop')]+std_caps(v6),3,0.0,hook_scenes=3)
