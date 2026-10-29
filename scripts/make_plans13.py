exec(open('/home/claude/p2/scripts/make_plans10.py').read().split("s=[R,PUT,LIGHTS,RELIEF,TUCK,END]")[0])
GYM=('m1gymN.mp4',0.8,2.0,1.0); STORE=('m2storeN.mp4',1.0,2.0,1.0); FLOOR=('m3floorN.mp4',2.8,2.0,1.0); DATE=('m4dateN.mp4',0.0,2.0,1.0); STAIRS=('m5stairsN.mp4',2.8,2.0,1.0); BACK=('m6backN.mp4',2.0,2.0,1.0)
V=[('lg13_01_gym',[GYM,PUT,LIGHTS,RELIEF,TUCK,END],"When cramps hit in the\nmiddle of a workout 😭",None),
('lg13_02_store',[STORE,BTN,LIGHTS,LAUGH,RELIEF,END],"Cramps hitting in the\nmiddle of the store.. 😭🩸",None),
('lg13_03_floor',[FLOOR,HAND,LIGHTS,TUCK,LAUGH,END],"If you've ever slept on the\nbathroom floor from cramps",None),
('lg13_04_date',[DATE,PUT,LIGHTS,HUG,RELIEF,END],"When your period ruins\ndate night 😭🩸",None),
('lg13_05_stairs',[STAIRS,BTN,LIGHTS,RELIEF,TUCK,END],"Day 2 cramps when you\ncan't make it upstairs 😭",None),
('lg13_06_back_burn',[BACK,PUT,LIGHTS,LAUGH,RELIEF,END],"My hot water bottle\ndid THIS to my back 🤮😭","So I switched to this 🥹💕"),
('lg13_07_tag_gym',[GYM,HAND,LIGHTS,LAUGH,TUCK,END],"Tag your gym girl who\ngets the worst cramps 😭",None),
('lg13_08_date_bf',[DATE,BTN,LIGHTS,TUCK,HUG,END],"Boyfriends, if she does\nthis on date night 😭",None),
('lg13_09_send_floor',[FLOOR,PUT,LIGHTS,RELIEF,LAUGH,END],"Send this to your girl\non the bathroom floor 😭",None),
('lg13_10_everywhere',[STORE,HAND,LIGHTS,RELIEF,TUCK,END],"Send this to the girl who\nhas cramps EVERYWHERE 😭",None)]
for n,s,h,sec in V:
    if sec: mk(n,s,caps(s,h,sec,hook_len=2.0),drop_scene=2)
    else: mk(n,s,caps(s,h),drop_scene=2)
