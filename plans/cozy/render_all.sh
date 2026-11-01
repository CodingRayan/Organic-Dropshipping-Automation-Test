#!/bin/bash
cd /home/claude/organic-dropshipping-automation-test
B=$(ls -d /opt/pw-browsers/chromium_headless_shell-1243/*/)chrome-headless-shell
render(){ npx remotion render src/index.ts Ad out/$1.mp4 --props=plans/cozy/$1.json --browser-executable=$B --log=error > out/$1.log 2>&1 && echo "done $1" || echo "FAIL $1"; }
export -f render; export B
ls plans/cozy/*.json | xargs -n1 basename | sed 's/.json//' | xargs -P 1 -I{} bash -c 'render {}'
echo ALL_DONE
