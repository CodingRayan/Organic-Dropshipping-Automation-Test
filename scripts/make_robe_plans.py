import json
# OctoWrap heated robe showcase (Nov 8): competitor cloak showcase copied shot for shot.
# Song: frightful.mp3 (user's file, first sound at 0.45s) played from its start, coming in as the
# countdown ends; it simply stops (short fade) when the video ends.
SHOTS = [  # (file, start, duration, clip volume) -- tight cut, jump cuts inside the long actions like competitor v1/v2
    ("rb_hook.mp4", 0.3, 3.9, 1.0),       # 3-2-1 bounce, drop, reveal (starts on "3", cut just after the reveal)
    ("rb_hood.mp4", 0.9, 1.4, 0.8),       # hood: skips the start, hands grab it and it goes up
    ("rb_feet.mp4", 0.2, 1.0, 0.8),       # first foot into the pocket
    ("rb_feet.mp4", 2.3, 1.0, 0.8),       # second foot into the pocket
    ("rb_feet.mp4", 4.0, 1.3, 0.8),       # robe pulled open
    ("rb_close.mp4", 2.4, 1.0, 0.8),      # robe closed, tying the bow
    ("rb_plug2.mp4", 0.5, 2.1, 1.0),      # plug: gap -> one smooth push -> fully in -> click
    ("rb_remote_sd.mp4", 1.8, 1.9, 1.0),  # remote: 3 clicks, light 3 -> 4 -> 5
    ("rb_couch.mp4", 0.4, 2.2, 0.8),      # couch snuggle
]
SONG_AT = 2.7  # song file starts here; first note at 3.15, right as her "let's see how it turns out" ends and the robe drops
TEXTS = {  # one text per video; a tuple = (text on the hook shot, text after the hook)
    "rb_v1": "I made this for the\ncold-aholics.. 🥶🐙",
    "rb_v2": "\"Send this to someone\nwho'd absolutely wear\nthis with you 😆🤭\"",
    "rb_v3": ("\"My bf: Stop buying\nnonsense.\" 🙄", "Me 🐙:"),
    "rb_v4": "Don't show this to\nan anemic.. 😳❄️",
    "rb_v5": "Do NOT let a girl who's\nalways cold see this.. 🥶🐙",
    "rb_v6": "Send this to someone\nwho's always cold 🥶🐙",
    "rb_v7": "I made this for the girls\nwho are always cold.. 🥶🐙",
    "rb_v8": "\"Send this to someone\nwho'd absolutely wear\nthis with you 🥶🐙\"",
    "rb_v9": "\"Send this to your friend\nwho'd absolutely wear\nthis with you 😆🤭\"",
    "rb_v10": "Don't show this to a girl\nwho's always cold.. 🐙❄️",
    # Day 2 (Nov 9): one-change split tests of the outlier rb_v6 (67K) + one of rb_v7 (T39/T42/T36)
    "d2_1": "Send this to your friend\nwho's always cold 🥶🐙",
    "d2_2": "Send this to your bestie\nwho's always cold 🥶🐙",
    "d2_3": "Send this to your gf\nwho's always cold 🥶🐙",
    "d2_4": "Send this to your mom\nwho's always cold 🥶🐙",
    "d2_5": "Send this to your sister\nwho's always cold 🥶🐙",
    "d2_6": "Send this to someone\nwho's ALWAYS cold 🥶🐙",
    "d2_7": "Send this to someone\nwho's always freezing 🥶🐙",
    "d2_8": "Send this to someone\nwho's always cold 🥶💕",
    "d2_9": "Tag someone who's\nalways cold 🥶🐙",
    "d2_10": "I made this for the girls\nwho are always freezing.. 🥶🐙",
    # Day 3 (Nov 10): last test. One-change splits of the day-2 outlier d2_2 "bestie" (55K) + gifting (T37)
    "d3_1": "Send this to your bestie\nwho's ALWAYS cold 🥶🐙",
    "d3_2": "Send this to your best friend\nwho's always cold 🥶🐙",
    "d3_3": "Tag your bestie who's\nalways cold 🥶🐙",
    "d3_4": "Send this to your bestie\nwho's always cold 🥶🎁",
    "d3_5": "Send this to your roommate\nwho's always cold 🥶🐙",
    "d3_6": "Send this to your mom\nwho's ALWAYS cold 🥶🐙",
    "d3_7": "Send this to your friend\nwho's ALWAYS cold 🥶🐙",
    "d3_8": "Send this to your bf so\nhe gets you this for\nChristmas 🎁🥶",
    "d3_9": "Getting my bestie this for\nChristmas cause she's\nalways cold 🎁🥶",
    "d3_10": "The perfect gift for the girl\nwho's always cold 🎁🐙",
}
def plan(text):
    hook_t, rest_t = text if isinstance(text, tuple) else (text, text)
    scenes = [{"src": f, "start": st, "duration": d, "volume": v,
               "captions": [{"text": hook_t if i == 0 else rest_t, "top": 345, "from": 0, "to": d}]}
              for i, (f, st, d, v) in enumerate(SHOTS)]
    return {"fps": 30, "music": {"file": "frightful.mp3", "at": SONG_AT, "volume": 0.7}, "scenes": scenes}
for name, text in TEXTS.items():
    json.dump(plan(text), open(f"plans/{name}.json", "w"), ensure_ascii=False, indent=1)
    print("wrote", name, sum(s[2] for s in SHOTS))
