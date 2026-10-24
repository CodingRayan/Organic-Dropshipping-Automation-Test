# MerryWall automated video pipeline

Claude plans the video, Higgsfield makes the clips, this Remotion template edits them, Dropbox hosts the file, Metricool publishes it.

## Flow (Claude runs this)
1. `npm install`
2. Download each approved Higgsfield clip: `scripts/fetch_clip.sh <url> <name>.mp4`
3. Write the edit plan to `plans/current.json` (scenes, trims, zoom, captions, sound effects, music). See `plans/example_cat.json`.
4. Render: `npm run render` (1080x1920, 30fps, about 1 minute per 4 seconds of video).
5. Check the render frame by frame and show it to the user. Nothing goes out without the user saying "post".
6. Upload: `python3 -I scripts/dropbox_upload.py out/video.mp4 /merrywall/<date>_<name>.mp4` (prints a public link).
7. Schedule with the Metricool connector (brand MerryWall, blogId 7555040): Instagram REEL or TRIAL_REEL + Facebook REEL, autoPublish true, isAiGenerated left false.

## Assets
- `public/audio/song.mp3`: Mariah Carey, All I Want For Christmas Is You. Beat drop at 50.30s (silence 49.5 to 50.1s, then the band kicks in). In plans use "music": {"file": "song.mp3", "dropAt": 50.3, "popAt": <second of the light pop in the video>}.
- `public/audio/` song files (user supplies)
- `public/audio/hate.mp3`: Ariana Grande, hate that i made you love me (product #2, LunaGlow). Drop at 30.9s: "music": {"file": "hate.mp3", "dropAt": 30.9, "popAt": <reveal second>, "volume": 0.35, "dropVolume": 0.6}.
- No sound effects: the user does not want them. Leave `sfx` out of plans.

## Plan options added for product #2 (see plans/lg_v1..v6)
- Scene `volume`: plays the clip's own audio (Kling sound-on talking/reactions). Omit to keep the clip muted.
- Music `dropVolume`: song volume after `popAt` (`volume` is used before it), so the song sits under the voices.
- Caption `style: "cta"`: lower-middle line, used for 'Comment "PAD" for the link ⬇️💕' in the last 2s.
- Caption `top`: pixel offset for the hook line (default 540) to keep text off faces.
- Scene `blurs`: [{x,y,w,h}] percent boxes with soft edges, for garbled AI text on TVs. Check the subject never moves into a box.
- Font is TikTok Sans (@fontsource/tiktok-sans). postinstall also copies emoji files without the -fe0f suffix so emojis like ⬇️ resolve.
- `public/clips/` downloaded clips (not committed)

## Secrets
Never commit tokens. Dropbox needs DBX_APP_KEY, DBX_APP_SECRET, DBX_REFRESH_TOKEN as env vars, provided by the user in each new session.

## Settings and rules
- Metricool is on the FREE plan: only 20 published posts per month. Count before scheduling and tell the user when close; extra videos get posted by hand.
- Music is added by Claude in Remotion from the user's song file; never attach Metricool/Instagram audio.
- Text: big, bold, white with black outline, upper middle. Big centered numbers for 3-2-1.
- Show the dark wall 0.5 to 1s before the light pop; beat drop on the pop.
- Max 400 Higgsfield credits per product test. Show frames before spending on video.
- Kling: no second-by-second timings in prompts; keep the wall static.
