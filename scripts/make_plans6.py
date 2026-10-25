exec(open('/home/claude/p2/scripts/build4.py').read())
FEAT="Heat, Massage\n& Relief ♨️😮‍💨"
CTA='Comment "PAD"\nfor the link ⬇️💕'
LIGHTS=('sB2.mp4',1.425,1.2)
C2B=[{'x':62,'y':11,'w':50,'h':19}]
C1B=[{'x':86,'y':11,'w':16,'h':4},{'x':86,'y':25.5,'w':16,'h':4}]
C3B=[{'x':8,'y':25,'w':38,'h':7}]
END=('endfixL.mp4',1.9,3.0,1.0)
def std_caps(scenes):
    end_start=sum(round(x[2]*30)/30 for x in scenes[:-1])
    return [(FEAT,'drop',end_start),(CTA,end_start,None)]
# 1 Mom Christmas gift
m=[('c7N.mp4',2.6,2.3,1.0),('sC.mp4',0.0,1.5),('sD.mp4',0.2,1.2),LIGHTS,('sB.mp4',0.6,1.3),('c8.mp4',0.5,1.8),('c4N.mp4',2.0,1.5,0.8),END]
build('lg6_a_mom',m,[("Gave my mom the period pad\nshe never had 😭🎄",0,'drop')]+std_caps(m),3,0.45)
# 2 Mom's idea vs mine (fail hook)
v=[('c3.mp4',3.0,2.0,1.0,C3B),('sA.mp4',0.3,1.2),('sC.mp4',0.0,1.5),LIGHTS,('sB.mp4',0.6,1.3),('c4N.mp4',2.0,1.5,0.8),('c10.mp4',1.0,1.8),END]
build('lg6_b_momidea',v,[("My mom's idea for cramps 🤮\nVS..",0,2.0),("My idea 🤩",2.0,'drop')]+std_caps(v),3,0.45)
# 3 Pain first: same girl, pain then relief
p=[('c1B.mp4',1.5,2.2,1.0,C1B),('sA.mp4',0.3,1.2),('sC.mp4',0.0,1.5),LIGHTS,('sB.mp4',0.6,1.3),('c2N.mp4',1.2,1.8,1.0,C2B),('c4N.mp4',2.0,1.5,0.8),END]
build('lg6_c_painfirst',p,[("Day 2 cramps\nhit DIFFERENT 😭🩸",0,'drop')]+std_caps(p),3,0.45)
# 4 Trial reel of video 1 with new hook text
t=[('hSN.mp4',1.4,2.3,1.0),('sC.mp4',0.0,1.5),('sD.mp4',0.2,1.2),LIGHTS,('sB.mp4',0.6,1.3),('c10.mp4',1.0,1.8),('c2N.mp4',1.2,1.8,1.0,C2B),END]
build('lg6_d_trial_endo',t,[("Endometriosis girls,\nyou NEED this 😱🩸",0,'drop')]+std_caps(t),3,0.45)
