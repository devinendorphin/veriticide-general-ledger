#!/usr/bin/env python3
"""Decode a saved chatgpt.com/share page into an ordered transcript.

The share page ships its conversation as a React Router turbo-stream payload:
one flat array in which every value is either a literal or an index into the
same array, enqueued as JS string chunks. This script reassembles the chunks,
resolves the index graph, and emits the linear conversation in order.

It exists so the transcript in this store is *derivable* from the captured
HTML rather than asserted by the analyst. Re-run it on the .html beside it and
the output must match `chatgpt-share-6a8b4330-transcript.md` byte for byte
(modulo the header this script writes).

Usage:
    python3 decode_share.py chatgpt-share-6a8b4330.html > transcript.md
"""

import datetime
import json
import re
import sys

SPECIAL = {-1: None, -2: None, -5: None, -6: None, -7: True, -8: False}


def load_payload(html: str):
    chunks = re.findall(
        r'streamController\.enqueue\((".*?")\)\s*;?\s*</script>', html, re.S
    )
    payload = "".join(json.loads(c) for c in chunks)
    return json.JSONDecoder().raw_decode(payload)[0]


def resolver(arr):
    memo = {}

    def res(i):
        if not isinstance(i, int):
            return i
        if i < 0:
            return SPECIAL.get(i)
        if i in memo:
            return memo[i]
        v = arr[i]
        if isinstance(v, dict):
            out = {}
            memo[i] = out
            for k, val in v.items():
                key = res(int(k[1:])) if isinstance(k, str) and k.startswith("_") else k
                out[key] = res(val)
            return out
        if isinstance(v, list):
            out = []
            memo[i] = out
            for x in v:
                out.append(res(x))
            return out
        memo[i] = v
        return v

    return res


def main(path: str) -> int:
    sys.setrecursionlimit(200000)
    arr = load_payload(open(path, encoding="utf-8", errors="replace").read())
    root = resolver(arr)(0)
    data = root["loaderData"]["routes/share.$shareId.($action)"]["serverResponse"]["data"]

    print(f"# {data['title']}")
    print()
    print(f"- share id: `{data['conversation_id']}`")
    print(f"- default model slug: `{data.get('default_model_slug')}`")
    print()

    i = 0
    for node in data["linear_conversation"]:
        msg = node.get("message") if isinstance(node, dict) else None
        if not msg:
            continue
        content = msg.get("content") or {}
        parts = content.get("parts") or []
        text = "".join(p if isinstance(p, str) else json.dumps(p) for p in parts)
        if not text.strip():
            continue
        i += 1
        role = (msg.get("author") or {}).get("role")
        ts = msg.get("create_time")
        stamp = (
            datetime.datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
            if ts
            else "unknown"
        )
        slug = (msg.get("metadata") or {}).get("model_slug") or ""
        print(f"\n## [{i}] {role} · {content.get('content_type')} · {stamp}Z · {slug}\n")
        print(text)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
