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

s=[('hSN.mp4',1.7,2.0,1.0),PUT,LIGHTS,GLOW,TUCK,END]
mk('lg7_01_endo_need',s,caps(s,"If you have Endometriosis,\nyou NEED this..😱🩸"),drop_scene=2)
s=[('n3bathL.mp4',0.8,2.05,1.0),PUT,LIGHTS,GLOW,RELIEF,END]
mk('lg7_02_second_day',s,caps(s,"POV: it's second day\nwith Endometriosis 😣🥺"),drop_scene=2)
s=[('n1burnL.mp4',2.0,2.0,1.0),BTN,LIGHTS,GLOW,LAUGH,END]
mk('lg7_03_hurts_vs',s,caps(s,"A heating pad that hurts you..\nVS..","One that actually calms\nyour cramps 🥹💕",hook_len=2.0),drop_scene=2)
s=[('c6N.mp4',1.2,2.0,1.0),PUT,LIGHTS,GLOW,HUG,END]
mk('lg7_04_tag_xmas',s,caps(s,"Tag someone who needs\nthis for Christmas 🎁"),drop_scene=2)
s=[('sB2.mp4',1.4,2.0),PUT,BTN,LAUGH,RELIEF,END]
mk('lg7_05_lights_first',s,caps(s,"This is what endo girls\nare using now 😱",hook_len=2.0),drop_scene=0,drop_in=0.475,feat_from=2.0)
s=[('n2snatchL.mp4',3.2,1.8,1.0),PUT,LIGHTS,GLOW,RELIEF,END]
mk('lg7_06_bestie',s,caps(s,"My bestie when she saw this 😭"),drop_scene=2)
s=[('c7N.mp4',2.6,2.3,1.0),PUT,LIGHTS,GLOW,HUG,END]
mk('lg7_07_mom_needed',s,caps(s,"POV: you got your mom the\ngift she actually needed 😭🎄"),drop_scene=2)
s=[('n4bfL.mp4',2.1,2.4,1.0,TVB),BTN,LIGHTS,GLOW,TUCK,END]
mk('lg7_08_bf_gets_it',s,caps(s,"POV: your bf finally gets it 😭"),drop_scene=2)
s=[('c5N.mp4',0.9,0.85,1.0),('c5N.mp4',2.5,0.85,1.0),('c5N.mp4',4.2,0.75,1.0),('c6N.mp4',1.2,1.6,1.0),GLOW,PUT,RELIEF,END]
mk('lg7_09_only_gift',s,[("The only Christmas gift\nshe'll actually use 🎁🩸",0,'drop')],drop_scene=3,drop_in=0.0,hook_scenes=3)
s=[('c4N.mp4',0.0,2.0,1.0),PUT,LIGHTS,GLOW,RELIEF,END]
mk('lg7_10_three_days',s,caps(s,"Me after 3 days of cramps\nfinally finding this 😭"),drop_scene=2)
