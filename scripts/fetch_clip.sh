#!/usr/bin/env bash
# Download a Higgsfield result (or any URL) into public/clips.
# Usage: scripts/fetch_clip.sh <url> <name.mp4>
set -euo pipefail
mkdir -p public/clips
curl -sS -L -m 300 -o "public/clips/$2" "$1"
echo "saved public/clips/$2"
