import json
# OctoWrap heated robe showcase (Nov 8): competitor cloak showcase copied shot for shot.
# Song: frightful.mp3 (user's file, 15.05s, first sound at 0.45s) played start to finish,
# placed so it comes in right before the cut after the hook and ends with the video.
SHOTS = [  # (file, start, duration, clip volume)
    ("rb_hook.mp4", 0.0, 5.0, 1.0),
    ("rb_hood.mp4", 0.4, 2.2, 0.8),
    ("rb_feet.mp4", 0.5, 5.0, 0.8),
    ("rb_close.mp4", 2.5, 1.0, 0.8),
    ("rb_plug.mp4", 1.2, 1.2, 1.0),
    ("rb_remote.mp4", 0.1, 1.7, 1.0),
    ("rb_couch.mp4", 0.4, 3.25, 0.8),
]
SONG_AT = 4.3  # song file starts here; its first sound lands at 4.75, just before the 5.0 cut
TEXTS = {
    "rb_v1": "I made this for the\ncold-aholics.. 🥶🐙",
}
def plan(text):
    scenes = [{"src": f, "start": s, "duration": d, "volume": v,
               "captions": [{"text": text, "top": 345, "from": 0, "to": d}]} for f, s, d, v in SHOTS]
    return {"fps": 30, "music": {"file": "frightful.mp3", "at": SONG_AT, "volume": 0.7}, "scenes": scenes}
for name, text in TEXTS.items():
    json.dump(plan(text), open(f"plans/{name}.json", "w"), ensure_ascii=False, indent=1)
    print("wrote", name, sum(s[2] for s in SHOTS))
