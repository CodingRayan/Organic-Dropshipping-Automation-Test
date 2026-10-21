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
- `public/audio/` song files (user supplies)
- No sound effects: the user does not want them. Leave `sfx` out of plans.
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
