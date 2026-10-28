#!/usr/bin/env bash
# Usage: bash scripts/render_batch.sh plan1 plan2 ...   (plan names from plans/*.json, without .json)
# Renders with Remotion, masters audio (hook boost + loudnorm), then exports the posting copy to out/post/.
# HOOK_GAIN (default 2.0) and HOOK_END (default 2.2s) can be overridden per run.
cd "$(dirname "$0")/.."
mkdir -p out/post
G=${HOOK_GAIN:-2.0}; E=${HOOK_END:-2.2}
for p in "$@"; do
  npx remotion render src/index.ts Ad out/$p.raw.mp4 --props=plans/$p.json --browser-executable=${CHROME:-/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell} --log=error > out/$p.log 2>&1 \
  && ffmpeg -v quiet -y -i out/$p.raw.mp4 -c:v copy -af "volume='if(lt(t,$E),$G,1)':eval=frame,loudnorm=I=-10:TP=-1.0:LRA=11:linear=true,alimiter=limit=0.92:level=false" -ar 48000 -c:a aac -b:a 192k out/$p.mp4 \
  && ffmpeg -v error -y -i out/$p.mp4 -c:v libx264 -profile:v high -level 4.1 -pix_fmt yuv420p -preset medium -b:v 5M -maxrate 6M -bufsize 10M -r 30 -c:a aac -b:a 128k -ar 48000 -movflags +faststart out/post/$p.mp4 \
  && echo "done $p" || echo "FAIL $p"
done
