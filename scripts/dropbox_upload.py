#!/usr/bin/env python3
"""Upload a finished video to the Dropbox app folder and print a public share link.

Needs env vars (never commit them): DBX_APP_KEY, DBX_APP_SECRET, DBX_REFRESH_TOKEN.
Usage: python3 -I scripts/dropbox_upload.py out/video.mp4 /merrywall/2026-10-21_cat.mp4
"""
import json, os, sys, urllib.request, urllib.parse, base64

def token():
    data = urllib.parse.urlencode({"grant_type": "refresh_token", "refresh_token": os.environ["DBX_REFRESH_TOKEN"]}).encode()
    req = urllib.request.Request("https://api.dropboxapi.com/oauth2/token", data=data)
    auth = base64.b64encode(f"{os.environ['DBX_APP_KEY']}:{os.environ['DBX_APP_SECRET']}".encode()).decode()
    req.add_header("Authorization", "Basic " + auth)
    return json.load(urllib.request.urlopen(req, timeout=30))["access_token"]

def call(url, at, body=None, arg=None, raw=None):
    req = urllib.request.Request(url, data=raw if raw is not None else json.dumps(body).encode())
    req.add_header("Authorization", "Bearer " + at)
    if arg is not None:
        req.add_header("Dropbox-API-Arg", json.dumps(arg))
        req.add_header("Content-Type", "application/octet-stream")
    else:
        req.add_header("Content-Type", "application/json")
    try:
        return json.load(urllib.request.urlopen(req, timeout=300))
    except urllib.error.HTTPError as e:
        return json.loads(e.read() or b"{}")

local, remote = sys.argv[1], sys.argv[2]
at = token()
with open(local, "rb") as f:
    up = call("https://content.dropboxapi.com/2/files/upload", at, arg={"path": remote, "mode": "overwrite"}, raw=f.read())
print("uploaded", up.get("path_display"))
link = call("https://api.dropboxapi.com/2/sharing/create_shared_link_with_settings", at,
            {"path": remote, "settings": {"requested_visibility": "public"}})
url = link.get("url")
if not url:  # link already exists
    links = call("https://api.dropboxapi.com/2/sharing/list_shared_links", at, {"path": remote, "direct_only": True})
    url = links["links"][0]["url"]
print(url)
