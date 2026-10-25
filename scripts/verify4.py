import sys,json,subprocess,numpy as np,librosa,os
p=sys.argv[1]; plan=json.load(open(f'plans/{p}.json')); v=f'out/{p}.mp4'; fps=30
cuts=[0]
for s in plan['scenes']: cuts.append(cuts[-1]+round(s['duration']*fps))
ct=[c/fps for c in cuts]; m=plan['music']; drop=m['popAt']
# lights / reveal: red jump near drop
d=subprocess.run(['ffmpeg','-v','quiet','-ss',str(max(0,drop-0.5)),'-t','1.0','-i',v,'-vf','scale=54:96','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
f=np.frombuffer(d,np.uint8).reshape(-1,96,54,3).astype(float); r=(f[...,0]-f[...,1]).clip(0).mean((1,2)); j=np.argmax(np.diff(r))
subprocess.run(['ffmpeg','-v','quiet','-y','-i',v,'-ac','1','-ar','22050','/tmp/claude-0/v.wav'])
y,sr=librosa.load('/tmp/claude-0/v.wav',sr=22050); o=librosa.onset.onset_strength(y=y,sr=sr,hop_length=256); t=librosa.times_like(o,sr=sr,hop_length=256)
mm=(t>drop-0.3)&(t<drop+0.3)
h=1600; yy=librosa.resample(y,orig_sr=sr,target_sr=16000); rms=[np.sqrt((yy[i:i+h]**2).mean()) for i in range(0,len(yy)-h,h)]
print(f'{p}: {len(plan["scenes"])} clips, {ct[-1]:.1f}s | clip lengths {[round(b-a,2) for a,b in zip(ct,ct[1:])]}')
print(f'   drop planned {drop:.3f}s, audio slam {t[np.argmax(o*mm)]:.3f}s, light/reveal jump {max(0,drop-0.5)+(j+1)/fps:.3f}s')
print(f'   loudness first 3s (dBFS rms): {20*np.log10(np.mean(rms[:30])):.1f}, rest: {20*np.log10(np.mean(rms[30:])):.1f}')
ts=[(a+b)/2 for a,b in zip(ct,ct[1:])]
tmp='/tmp/claude-0/sh'; os.makedirs(tmp,exist_ok=True)
for i,tt in enumerate(ts): subprocess.run(['ffmpeg','-v','quiet','-y','-ss',str(tt),'-i',v,'-frames:v','1','-vf','scale=240:-1,drawtext=text=%.1f:x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black'%tt,f'{tmp}/{i:02d}.png'])
subprocess.run(['ffmpeg','-v','quiet','-y','-i',f'{tmp}/%02d.png','-vf',f'tile=8x1:color=black',f'/home/claude/p2/v3/fin_{p}.jpg']); subprocess.run('rm '+tmp+'/*',shell=True)
