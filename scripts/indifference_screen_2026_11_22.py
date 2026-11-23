#!/usr/bin/env python3
"""Lexical screen for outcome-indifference markers in the 2026-11-22 researcher cohort.

Usage: python3 -I scripts/indifference_screen_2026_11_22.py <posts.jsonl.gz> <out_dir>

Input: the operator-supplied cohort export (posts.jsonl.gz, sha256 cab0ef82...1f9bc1),
one JSON object per post with `researcher`, `words_are_theirs`, `text`, parent/quoted fields.
Output: one JSONL of hits per pattern family, plus per-researcher counts on stdout.

A hit is a candidate for reading, not a finding. Every cited post in
docs/indifference-screen-researcher-cohort-2026-11-22.md was read in full with its parent.
"""
import gzip
import json
import re
import sys
from collections import Counter, defaultdict

PATTERNS = {
    # Literal reading: acceptance of human replacement/extinction, or stated equanimity.
    "succession": r"\bsuccess(?:or|ion)\w*|worthy successor|replace (?:us|humanity|humans)|post-?human|"
                  r"inherit the (?:earth|universe|future)|mind ?children",
    "dontcare": r"(?:do ?n[o']?t|doesn[' ]?t|never|wouldn[' ]?t) (?:really )?(?:care|mind)\b.{0,60}\b"
                r"(?:extinct|die|dies|death|humanity|humans|doom|kill|future|outcome|happens)|whatever happens|"
                r"(?:fine|ok|okay) (?:with|if).{0,40}(?:extinct|humanity (?:dies|ends|goes)|humans (?:die|go extinct)|"
                r"replaced|disempower)",
    "extinct_ok": r"(?:extinction|human extinction).{0,60}(?:not (?:that )?bad|fine|acceptable|good thing|worth it)|"
                  r"(?:not (?:so|that) bad|fine|acceptable).{0,40}extinction",
    "equanimity": r"\bwho cares\b|\bdon'?t care\b|\bindifferen\w*|\bok with\b|\bfine with\b|\bcosmic darwin\w*|"
                  r"\bhandover\w*|\bhand over\b|\bdescendants?\b|\bzen about\b|\bsuccessionis\w*",
    "nihil": r"nihilis|nothing matters|cosmic (?:indifference|perspective)|heat death",
    # v2 (2026-11-23), added after the positive-control cohort showed v1 missed both Barnett anchors
    # (2034437142592839905, 2097731731281547381). Tuned on the control anchors: 4/4 in-sample;
    # out-of-sample recall is unmeasured.
    "replace_ok": r"(?:disempower\w*|human control|AIs? (?:hold|holding|have|control|take|taking) (?:most|all|over|the majority)|transition to a world)[^.]{0,200}(?:wouldn'?t be|isn'?t|is not|not) (?:a |that |so )?(?:bad|catastroph\w*|tragedy|problem)"
                  r"|(?:wouldn'?t be|isn'?t|not) (?:a |that )?(?:bad|catastroph\w*|morally bad)[^.]{0,150}(?:disempower|AIs? (?:hold|take)|transition|replace)"
                  r"|morally bad for humans|peaceful(?:ly)? transition|(?:fine|ok|okay|happy) with (?:our )?(?:\w+ )?descendants|(?:metal|AI|mind) (?:descendants|children)"
                  r"|(?:don'?t|do not) (?:think|consider)[^.]{0,80}catastroph\w*|diminish\w* human control"
                  r"|speciesis\w*|(?:don'?t|do not) care about (?:the )?human species|pass(?:ing)? the torch|succession to AI|resist succession|worthy successor|post-?humanis\w*|biological substrate",
    # Doctrinal reading (Feingold disconfirmer): stated valuation of the outcome or a stopping rule.
    "valuation": r"\b(?:I|we) (?:care|want|hope|fear|worry)\b|worried|scared|terrif\w*|unacceptable|"
                 r"should (?:pause|stop|not build|ban)|\bpause\b|take a breather",
}


def main(src, out_dir):
    rows = [json.loads(l) for l in gzip.open(src, "rt")]
    own = [r for r in rows if r.get("words_are_theirs") is True]
    print(f"posts={len(rows)} own_words={len(own)} researchers={len({r['researcher'] for r in rows})}")
    for name, pat in PATTERNS.items():
        rx = re.compile(pat, re.I)
        hits = [r for r in own if r.get("text") and rx.search(r["text"])]
        by = Counter(r["researcher"] for r in hits)
        print(f"== {name}: {len(hits)} hits; " + ", ".join(f"{k}={v}" for k, v in by.most_common()))
        with open(f"{out_dir}/hits_{name}.jsonl", "w") as f:
            for r in hits:
                f.write(json.dumps({k: r.get(k) for k in (
                    "researcher", "id", "url", "created_at_et", "type", "text",
                    "parent_author", "parent_text", "quoted_author", "quoted_text")}) + "\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
