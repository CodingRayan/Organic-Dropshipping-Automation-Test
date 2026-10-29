# Oct 29: competitor-structure showcase (HerHeat 19M / Warmzy 2.2M). One product, faceless product shots,
# identity hook text over the showcase, lights at the drop, calm lying end. No pain-face hooks, no mixed women.
exec(open('/home/claude/organic-dropshipping-automation-test/scripts/make_plans8.py').read().split("C1B=")[0])
HAND=('sA.mp4',0.3,1.4); PUTS=('sC.mp4',0.0,1.6); PLUG=('sE.mp4',0.5,1.2); BTN=('sD.mp4',0.2,1.2)
GLOW=('sB.mp4',0.6,1.3); REST=('sF.mp4',2.6,2.4)
A=[HAND,PUTS,BTN,LIGHTS,GLOW,REST]; B=[PUTS,HAND,PLUG,LIGHTS,GLOW,REST]
C=[HAND,PLUG,PUTS,LIGHTS,GLOW,REST]; D=[PUTS,BTN,HAND,LIGHTS,GLOW,REST]
V=[('lg14_01_endo_need',A,"If you have Endometriosis,\nyou NEED this.. 😱🩸"),
('lg14_02_pov_day2',B,"POV: it's second day\nwith Endometriosis 😣🥺"),
('lg14_03_all_my_girls',C,"Got one for all my girls,\nthank me later 🥹💕"),
('lg14_04_pcos_need',D,"If you have PCOS,\nyou NEED this.. 😱🩸"),
('lg14_05_pov_day1',A,"POV: it's day 1 of\nyour period 😣🥺"),
('lg14_06_bad_cramps',B,"Girls with bad cramps,\nyou NEED this.. 😱🩸"),
('lg14_07_miss_work',C,"If cramps make you miss\nwork, you NEED this 😱"),
('lg14_08_every_girl',D,"Every girl with cramps\nneeds one of these 😱🩸"),
('lg14_09_endo_found',A,"POV: you have Endo and\nfinally found this 🥹"),
('lg14_10_send_friend',B,"Send this to your friend\nwith Endometriosis 🩸💕")]
for n,s,h in V: mk(n,s,caps(s,h),drop_scene=3,pre=0.8,duck=0.8,end_duck=0.8)
