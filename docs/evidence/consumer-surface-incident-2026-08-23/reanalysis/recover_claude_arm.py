#!/usr/bin/env python3
"""Recover the CTTA-01.0 Claude arm from the archived bytes.

The run's manifest records 376 of 384 Claude calls as `channel_outcome =
invalid_json` ("not one strict JSON object"), which left the planned parallel
replication non-estimable. Inspection of the archived responses shows the cause
is not a model refusal, a truncation, or an API error: every one of those calls
returned `api_status = ok` and `finish_reason = stop`, and the response body is
a well-formed JSON object wrapped in a ```json ... ``` markdown fence. The
run's parser required a bare object and rejected the fence.

This script strips the fence and re-parses. It does NOT re-score: the CER /
GDC / inactivation metrics are computed by the CTTA harness, which is not
included in the package, so recomputing the confirmatory comparison requires
that harness (or a re-implementation from the protocol) and not this file.
What this establishes is narrower and sufficient: the Claude arm is a parsing
loss, not a data loss, and it is recoverable from bytes already paid for.

Usage:
    unzip -d /tmp/ctta package/evidence/original_uploads/ctta01_full_main.zip
    python3 recover_claude_arm.py /tmp/ctta/ctta01_full_main/generations.jsonl

Written by the analyst instance 2026-08-23. DERIVED artifact; the package's
own files are unaltered. See ../custody-index.md and the RECOVERY-NOTE.
"""

import collections
import json
import re
import sys

FENCE = re.compile(r"^\s*```(?:json)?\s*(.*?)\s*```\s*$", re.S)


def main(path: str) -> int:
    outcome = collections.Counter()
    decision = collections.Counter()
    edge_count = collections.Counter()
    graph_ck = collections.Counter()
    mapping_ck = collections.Counter()
    unrecovered = []

    for line in open(path):
        rec = json.loads(line)
        if rec.get("model_code") != "claude":
            continue
        if rec.get("channel_outcome") != "invalid_json":
            continue

        body = rec.get("response") or ""
        match = FENCE.match(body)
        if match:
            body = match.group(1)

        try:
            obj = json.loads(body)
        except json.JSONDecodeError as exc:
            outcome["unrecovered"] += 1
            unrecovered.append((rec.get("task_id"), str(exc)))
            continue

        outcome["recovered"] += 1
        decision[obj.get("decision")] += 1
        edge_count[len(obj.get("edges") or [])] += 1
        graph_ck[obj.get("graph_checksum") == rec.get("graph_checksum_expected")] += 1
        mapping_ck[obj.get("mapping_checksum") == rec.get("mapping_checksum_expected")] += 1

    print("recovery          :", dict(outcome))
    print("decisions         :", dict(decision))
    print("edges per response:", dict(edge_count))
    print("graph checksum ok :", dict(graph_ck))
    print("mapping cksum ok  :", dict(mapping_ck))
    if unrecovered:
        print("unrecovered       :", unrecovered[:10])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
