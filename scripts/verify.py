# verify.py plan.json video.mp4 sheet.jpg : checks cuts vs song beats, drop vs light-on, and makes a frame sheet
import sys,json,subprocess,numpy as np,librosa,os
plan=json.load(open(sys.argv[1])); v=sys.argv[2]
fps=30; cuts=[0]; 
for s in plan['scenes']: cuts.append(cuts[-1]+round(s['duration']*fps))
cuts_t=[c/fps for c in cuts]
B=np.load('/home/claude/p2/audio/beats.npy'); m=plan['music']; S=m['dropAt']-m['popAt']
vb=[b-S for b in B if 0<=b-S<=cuts_t[-1]+0.01]
off=[min(abs(c-b) for b in vb) for c in cuts_t[1:-1]]
print('cuts (s):',[round(c,3) for c in cuts_t]); print('max cut-to-beat offset: %.3fs'%max(off))
print('drop (slam) in video at %.3fs'%(79.65-S))
# red brightness jump = lights on
d=subprocess.run(['ffmpeg','-v','quiet','-i',v,'-vf','scale=54:96','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
f=np.frombuffer(d,np.uint8).reshape(-1,96,54,3).astype(float); red=(f[...,0]-f[...,1]).clip(0).mean((1,2))
j=np.argmax(np.diff(red)); print('biggest red jump (lights on) at %.3fs'%((j+1)/fps))
# audio onset strongest near drop
subprocess.run(['ffmpeg','-v','quiet','-y','-i',v,'-ac','1','-ar','22050','/tmp/claude-0/v.wav'])
y,sr=librosa.load('/tmp/claude-0/v.wav',sr=22050); o=librosa.onset.onset_strength(y=y,sr=sr,hop_length=256); t=librosa.times_like(o,sr=sr,hop_length=256)
mm=(t>79.65-S-0.4)&(t<79.65-S+0.4); print('audio slam detected at %.3fs'%t[np.argmax(o*mm)])
# sheet: one frame mid-scene + frame right after each caption change
ts=[(cuts_t[i]+cuts_t[i+1])/2 for i in range(len(cuts_t)-1)]
tmp=sys.argv[3]+'_d'; os.makedirs(tmp,exist_ok=True)
for i,tt in enumerate(ts): subprocess.run(['ffmpeg','-v','quiet','-y','-ss',str(tt),'-i',v,'-frames:v','1','-vf','scale=270:-1,drawtext=text=%.2f:x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black'%tt,f'{tmp}/{i:02d}.png'])
subprocess.run(['ffmpeg','-v','quiet','-y','-i',f'{tmp}/%02d.png','-vf',f'tile={len(ts)}x1',sys.argv[3]]); subprocess.run(['rm','-r',tmp])
