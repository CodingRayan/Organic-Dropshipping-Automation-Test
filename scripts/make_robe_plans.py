import json
# OctoWrap heated robe showcase (Nov 8): competitor cloak showcase copied shot for shot.
# Song: frightful.mp3 (user's file, 15.05s, first sound at 0.45s) played start to finish,
# placed so it comes in right before the cut after the hook and ends with the video.
SHOTS = [  # (file, start, duration, clip volume) -- 10 shots, jump cuts inside the long actions like competitor v1/v2
    ("rb_hook.mp4", 0.3, 3.9, 1.0),     # 3-2-1 bounce, drop, reveal (starts right on "3", cut just after the reveal)
    ("rb_hood.mp4", 0.2, 1.0, 0.8),     # hands on the hood (face on hood visible)
    ("rb_hood.mp4", 1.6, 1.0, 0.8),     # hood goes up
    ("rb_hood.mp4", 2.8, 0.8, 0.8),     # hood on, adjusting (competitor v2 has 3 hood cuts)
    ("rb_feet.mp4", 0.1, 1.3, 0.8),     # first foot into the pocket
    ("rb_feet.mp4", 2.2, 1.3, 0.8),     # second foot into the pocket
    ("rb_feet.mp4", 4.0, 1.65, 0.8),     # robe pulled open
    ("rb_close.mp4", 2.4, 1.4, 0.8),    # robe closed, tying the bow
    ("rb_plug.mp4", 1.2, 1.2, 1.0),     # plug click
    ("rb_remote.mp4", 0.1, 1.6, 1.0),   # remote clicks
    ("rb_remote2.mp4", 3.8, 0.8, 1.0),  # last click, light jumps to max (numbers stay correct in this part)
    ("rb_couch.mp4", 0.4, 1.8, 0.8),   # couch snuggle
]
SONG_AT = 2.7  # song file starts here; first note at 3.15, right as her "let's see how it turns out" ends and the robe drops
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
