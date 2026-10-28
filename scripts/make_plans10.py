exec(open('/home/claude/p2/scripts/build4.py').read())
FEAT="Heat, Massage\n& Relief ♨️😮‍💨"
CTA='Comment "PAD"\nfor the link ⬇️💕'
LIGHTS=('sB2.mp4',1.425,1.2)          # lights switch on 0.45s in = the drop
C2B=[{'x':62,'y':11,'w':50,'h':19}]
TVB=[{'x':55,'y':6,'w':62,'h':18},{'x':47,'y':22.3,'w':66,'h':6}]
END=('endfixL.mp4',2.6,2.35,1.0)     # "okay, this is literally saving my life"
GLOW=('sB.mp4',0.6,1.0)
PUT=('sC.mp4',0.0,1.3)
BTN=('sD.mp4',0.2,1.2)
RELIEF=('c2N.mp4',1.2,1.3,1.0,C2B)
LAUGH=('c4N.mp4',2.0,1.3,0.8)
TUCK=('c10.mp4',1.0,1.3)
HUG=('c8.mp4',0.5,1.3)
def caps(scenes,hook,second=None,hook_len=None,drop_label='drop'):
    end_start=sum(round(x[2]*30)/30 for x in scenes[:-1])
    if second: c=[(hook,0,hook_len),(second,hook_len,drop_label)]
    else: c=[(hook,0,drop_label if hook_len is None else hook_len)]
    return c
def finish(scenes,feat_from='drop'):
    end_start=sum(round(x[2]*30)/30 for x in scenes[:-1])
    return [(FEAT,feat_from,end_start),(CTA,end_start,None)]
def mk(name,scenes,hookcaps,drop_scene=3,drop_in=0.45,feat_from='drop',**kw):
    build(name,scenes,hookcaps+finish(scenes,feat_from),drop_scene,drop_in,**kw)

C1B=[{'x':86,'y':11,'w':16,'h':4},{'x':86,'y':25.5,'w':16,'h':4}]
C3B=[{'x':8,'y':25,'w':38,'h':7}]
HAND=('sA.mp4',0.3,1.2)
PWR=('sE.mp4',0.9,1.2)
R=('k1restN.mp4',2.2,2.2,1.0); CAR=('k2carN.mp4',1.6,2.0,1.0); BED=('k3bedN.mp4',1.6,2.0,1.0); KIT=('k4kitchN.mp4',1.0,2.0,1.0); BRN=('k5burnN.mp4',1.6,2.0,1.0)
s=[R,PUT,LIGHTS,RELIEF,TUCK,END]
mk('lg10_01_work',s,caps(s,"POV: your cramps hit\nin the middle of work 😭🩸"),drop_scene=2)
s=[CAR,BTN,LIGHTS,LAUGH,RELIEF,END]
mk('lg10_02_car',s,caps(s,"When your cramps are so bad\nyou can't even drive 😭"),drop_scene=2)
s=[BED,PUT,LIGHTS,TUCK,LAUGH,END]
mk('lg10_03_3am',s,caps(s,"3am and my cramps\nwon't let me sleep 😣🩸"),drop_scene=2)
s=[KIT,HAND,LIGHTS,RELIEF,HUG,END]
mk('lg10_04_day2',s,caps(s,"Day 2 cramps hit\nDIFFERENT 😭🩸"),drop_scene=2)
s=[BRN,BTN,LIGHTS,RELIEF,LAUGH,END]
mk('lg10_05_burned',s,caps(s,"My heating pad did THIS\nto my stomach.. 🤮😭","So I switched to this 🥹💕",hook_len=2.0),drop_scene=2)
s=[R,HAND,LIGHTS,LAUGH,TUCK,END]
mk('lg10_06_tag_bathroom',s,caps(s,"Tag the girl who hides\nin the bathroom at work 😭"),drop_scene=2)
s=[CAR,PUT,LIGHTS,RELIEF,HUG,END]
mk('lg10_07_cried_car',s,caps(s,"If you've ever cried in\nyour car from cramps.. 🩸"),drop_scene=2)
s=[BED,BTN,LIGHTS,LAUGH,RELIEF,END]
mk('lg10_08_send_sleep',s,caps(s,"Send this to your girl who\ncan't sleep on her period 😭"),drop_scene=2)
s=[KIT,PUT,LIGHTS,TUCK,RELIEF,END]
mk('lg10_09_boyfriends',s,caps(s,"Boyfriends, if she looks\nlike this every month 😭"),drop_scene=2)
s=[BRN,PUT,LIGHTS,LAUGH,TUCK,END]
mk('lg10_10_burn_vs',s,caps(s,"Heating pads that burn you..\nVS.. 🤮","One that actually\ncalms your cramps 🥹💕",hook_len=2.0),drop_scene=2)
