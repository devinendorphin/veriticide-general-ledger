#!/usr/bin/env python3
"""Measure how faithfully the operator's copy-paste relay reproduced Grok's output.

Compares each assistant message in the native grok.com record against the text the
operator pasted into the ChatGPT session (`../layer3-relay/`). This is the check
that turns RELAY-HELD's central caveat -- "fidelity is operator-attested" -- into a
measurement, for the range the two captures overlap.

Usage:
    python3 verify_relay_fidelity.py grok-share-aed7676d-native.json \
        ../layer3-relay/chatgpt-share-6a8b4330-transcript.md
"""

import difflib
import json
import re
import sys
import unicodedata


def norm(text):
    text = unicodedata.normalize("NFC", text)
    for a, b in (("’", "'"), ("“", '"'), ("”", '"')):
        text = text.replace(a, b)
    return re.sub(r"\s+", " ", text).strip()


def relay_pastes(path):
    """The operator's turns in the ChatGPT transcript are the pasted Grok output."""
    blocks = re.split(r"^## \[\d+\] (\w+) .*$", open(path, encoding="utf-8").read(), flags=re.M)
    out = []
    for role, body in zip(blocks[1::2], blocks[2::2]):
        if role == "user" and body.strip():
            out.append(body.strip())
    return out


def main(native_path, relay_path):
    native = json.load(open(native_path, encoding="utf-8"))
    pastes = [norm(p) for p in relay_pastes(relay_path)]

    print(f"{'grok turn':>9} {'native':>7} {'relay':>7}  ratio   note")
    for i, node in enumerate(n for n in native["responses"] if n["sender"] == "assistant"):
        g = norm(node["message"])
        ratio, idx = max((difflib.SequenceMatcher(None, g, p).ratio(), j)
                         for j, p in enumerate(pastes))
        p = pastes[idx]
        extra = sum(j2 - j1 for tag, _, _, j1, j2 in
                    difflib.SequenceMatcher(None, g, p).get_opcodes() if tag == "insert")
        lost = sum(i2 - i1 for tag, i1, i2, _, _ in
                   difflib.SequenceMatcher(None, g, p).get_opcodes() if tag == "delete")
        note = []
        if extra > 200:
            note.append(f"+{extra}ch appended by operator")
        if lost > 100:
            note.append(f"-{lost}ch (citation-card markup lost to copy-paste)")
        print(f"{i:9d} {len(node['message']):7d} {len(p):7d}  {ratio:.4f}  {'; '.join(note)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
