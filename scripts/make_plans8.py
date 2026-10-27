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
# burn / VS family (FB winner: hurts vs 308)
s=[('n1burnL.mp4',2.0,2.0,1.0),PUT,LIGHTS,RELIEF,TUCK,END]
mk('lg8_01_burns_vs',s,caps(s,"A heating pad that burns you..\nVS.. 🤮","One that actually calms\nyour cramps 🥹💕",hook_len=2.0),drop_scene=2)
s=[('c3.mp4',3.0,2.0,1.0,C3B),BTN,LIGHTS,LAUGH,HUG,END]
mk('lg8_02_mom_idea_vs',s,caps(s,"My mom's idea for cramps 🤮\nVS..","My idea 🤩",hook_len=2.0),drop_scene=2)
s=[('n1burnL.mp4',1.0,2.0,1.0),PUT,LIGHTS,LAUGH,RELIEF,END]
mk('lg8_03_still_bottle',s,caps(s,"Still using a hot water\nbottle for cramps? 🤮","Try this instead 🥹💕",hook_len=2.0),drop_scene=2)
s=[('n1burnL.mp4',1.3,2.0,1.0),BTN,LIGHTS,TUCK,LAUGH,END]
mk('lg8_04_burn_marks',s,caps(s,"POV: your hot water bottle\nleft burn marks again 😭"),drop_scene=2)
# day 2 pain family (FB: 275, 241)
s=[('n3bathL.mp4',0.8,2.05,1.0),BTN,LIGHTS,RELIEF,LAUGH,END]
mk('lg8_05_day2_nothing',s,caps(s,"POV: it's day 2 and\nnothing is working 😭🩸"),drop_scene=2)
s=[('c1B.mp4',1.5,2.2,1.0,C1B),PUT,LIGHTS,TUCK,LAUGH,END]
mk('lg8_06_day2_couch',s,caps(s,"Day 2 cramps\nhit DIFFERENT 😣🩸"),drop_scene=2)
s=[('n3bathL.mp4',0.8,2.05,1.0),PUT,LIGHTS,LAUGH,TUCK,END]
mk('lg8_07_miss_work',s,caps(s,"When your cramps make you\nmiss work again 😭🩸"),drop_scene=2)
s=[('c1B.mp4',1.5,2.2,1.0,C1B),BTN,LIGHTS,RELIEF,LAUGH,END]
mk('lg8_08_cant_stand',s,caps(s,"Cramps so bad you\ncan't even stand up 😣🩸"),drop_scene=2)
# need / gift
s=[('hSN.mp4',1.7,2.0,1.0),PUT,LIGHTS,LAUGH,TUCK,END]
mk('lg8_09_cramps_need',s,caps(s,"If you have bad cramps,\nyou NEED this..😱🩸"),drop_scene=2)
s=[('c6N.mp4',1.2,2.0,1.0),BTN,LIGHTS,RELIEF,HUG,END]
mk('lg8_10_gift_cramps',s,caps(s,"Every girl with bad cramps\nneeds this for Christmas 🎁🩸"),drop_scene=2)
