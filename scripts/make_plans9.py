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
s=[('n1burnL.mp4',2.0,2.0,1.0),PUT,LIGHTS,RELIEF,TUCK,END]
mk('lg9_01_send_girl_bottle',s,caps(s,"Send this to the girl\nwho still uses this 🤮😭","This works way better 🥹💕",hook_len=2.0),drop_scene=2)
s=[('c3.mp4',3.0,2.0,1.0,C3B),BTN,LIGHTS,LAUGH,HUG,END]
mk('lg9_02_send_mom',s,caps(s,"Send this to your mom 😭\nthis does NOT help 🤮","This actually does 🥹💕",hook_len=2.0),drop_scene=2)
s=[('n3bathL.mp4',0.8,2.05,1.0),PUT,LIGHTS,RELIEF,LAUGH,END]
mk('lg9_03_send_cancels',s,caps(s,"Send this to your girl who\ncancels plans every month 😭"),drop_scene=2)
s=[('c1B.mp4',1.5,2.2,1.0,C1B),BTN,LIGHTS,TUCK,RELIEF,END]
mk('lg9_04_tag_this_bad',s,caps(s,"Tag someone whose cramps\nare THIS bad 😣🩸"),drop_scene=2)
s=[('n3bathL.mp4',0.8,2.05,1.0),HAND,LIGHTS,LAUGH,HUG,END]
mk('lg9_05_bestie_endo',s,caps(s,"If your bestie has endo,\nsend her this 🩸💕"),drop_scene=2)
s=[('n1burnL.mp4',1.0,2.0,1.0),PUT,LIGHTS,LAUGH,TUCK,END]
mk('lg9_06_threw_out',s,caps(s,"POV: you finally threw out\nthe hot water bottle 🤮","for this 🥹💕",hook_len=2.0),drop_scene=2)
s=[('c1B.mp4',1.5,2.2,1.0,C1B),PUT,LIGHTS,RELIEF,TUCK,END]
mk('lg9_07_boyfriends',s,caps(s,"Boyfriends, if she looks\nlike this every month 😭"),drop_scene=2)
s=[('n3bathL.mp4',0.8,2.05,1.0),BTN,LIGHTS,TUCK,LAUGH,END]
mk('lg9_08_day2_be_like',s,caps(s,"Day 2 of my period\nbe like.. 😣🩸"),drop_scene=2)
s=[('n1burnL.mp4',2.0,2.0,1.0),HAND,LIGHTS,RELIEF,LAUGH,END]
mk('lg9_09_burn_vs',s,caps(s,"Heating pads that burn you..\nVS.. 🤮","One that actually\ncalms your cramps 🥹💕",hook_len=2.0),drop_scene=2)
s=[('c1B.mp4',1.5,2.2,1.0,C1B),PUT,LIGHTS,LAUGH,RELIEF,END]
mk('lg9_10_midol',s,caps(s,"When Midol stops working\nby day 2.. 😭🩸"),drop_scene=2)
