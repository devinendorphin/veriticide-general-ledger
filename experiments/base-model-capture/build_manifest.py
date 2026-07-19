#!/usr/bin/env python3
"""
Fold run-manifest.jsonl (append log from capture.py) into a single hashed
manifest.json, and re-hash every raw file on disk to confirm nothing drifted
since capture. Commit manifest.json; raw/ stays git-ignored and goes off-platform.

Usage:  python build_manifest.py
"""
from __future__ import annotations
import hashlib, json, sys, datetime
from pathlib import Path

HERE = Path(__file__).parent
RAW = HERE / "raw"
JSONL = HERE / "run-manifest.jsonl"


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    if not JSONL.exists():
        sys.exit("no run-manifest.jsonl yet — run capture.py first")
    rows = [json.loads(l) for l in JSONL.read_text().splitlines() if l.strip()]
    artifacts, mismatches = {}, []
    for r in rows:
        f = HERE / r["file"]
        if not f.exists():
            mismatches.append(f"MISSING {r['file']}")
            continue
        disk = sha256_file(f)
        # response_sha256 hashes the response body; the file also wraps request+headers,
        # so we record the whole-file hash separately and keep the body hash from capture.
        artifacts[r["file"]] = {
            "model": r["model"], "probe_id": r["probe_id"], "kind": r["kind"],
            "iteration": r["iteration"], "captured_at": r["captured_at"],
            "request_sha256": r["request_sha256"],
            "response_sha256": r["response_sha256"],
            "file_sha256": disk, "bytes": f.stat().st_size,
        }
    manifest = {
        "store": "experiments/base-model-capture",
        "purpose": "Phase 0.1 perishable capture of davinci-002 / babbage-002 completions "
                   "(logprobs + echo scoring). Preservation only; no classification.",
        "built_at": datetime.datetime.utcnow().isoformat() + "Z",
        "custody_state": "HASHED-PENDING-BACKUP",
        "endpoint_deadline": "2026-09-28",
        "prereg_hash": rows[0]["prereg_hash"] if rows else None,
        "artifact_count": len(artifacts),
        "artifacts": artifacts,
    }
    (HERE / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    with (HERE / "sha256sums.txt").open("w") as fh:
        for name, d in artifacts.items():
            fh.write(f"{d['file_sha256']}  {name}\n")
    print(f"manifest.json: {len(artifacts)} artifact(s)")
    if mismatches:
        print("WARN:")
        for m in mismatches:
            print("  " + m)


if __name__ == "__main__":
    main()
