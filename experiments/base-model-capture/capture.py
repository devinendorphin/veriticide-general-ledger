#!/usr/bin/env python3
"""
Phase 0.1 — perishable base-model capture: davinci-002 and babbage-002.

Preservation only. This tool captures raw OpenAI /v1/completions responses —
including per-token logprobs and echo-scored logprobs of provided text — and
hashes each one into a manifest. It performs NO classification and encodes NO
framework language (Phase 0 rule). What the probes contain is entirely
operator-supplied (probes.yaml); keep them neutral per that rule.

WHY NOW — HARD DEADLINE. The /v1/completions endpoint is the only interface
that exposes logprobs + echo on these GPT-3-class base models, and it is
scheduled to close 2026-09-28. After that these measurements cannot be
reproduced from the models at all. Capture before then, and back up the raw/
directory off-platform immediately (see CAPTURE-RUNBOOK.md).

Two capture kinds:
  generate — sample a continuation; logprobs (top-5) on the generated tokens.
  score    — echo=true, max_tokens=0: returns the PROVIDED text tokenized with
             per-token logprobs and top-5 alternatives (the classic way to
             score the model's probability of a given string). Nothing is
             generated; this is a measurement of the fixed text.

Requires: OPENAI_API_KEY in env.  pip install -r requirements.txt
Usage:
  python capture.py --dry-run                 # build + print every request, make NO API calls
  python capture.py                           # capture all probes x models x iters, hash, manifest
  python capture.py --only score_neutral_01   # a subset of probe ids
  python capture.py --models davinci-002      # a subset of models
Re-runs are resumable: an already-captured (model, probe, iter) with a matching
request hash is skipped, so a run interrupted near the deadline can be resumed.
"""
from __future__ import annotations
import argparse, hashlib, json, os, sys, time
from pathlib import Path

try:
    import yaml  # pyyaml
except ImportError:
    sys.exit("pip install -r requirements.txt  (missing pyyaml)")
try:
    import requests
except ImportError:
    sys.exit("pip install -r requirements.txt  (missing requests)")

HERE = Path(__file__).parent


# --------------------------------------------------------------------------
# Config + probes + provenance
# --------------------------------------------------------------------------
def load_yaml(name: str) -> dict:
    p = HERE / name
    if not p.exists():
        sys.exit(f"missing {name} (copy probes.example.yaml -> probes.yaml and edit)")
    return yaml.safe_load(p.read_text())


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canon(obj) -> bytes:
    """Canonical JSON for stable hashing (sorted keys, tight separators)."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def prereg_hash(config_name: str, probes_name: str) -> str:
    h = hashlib.sha256()
    for n in (config_name, probes_name):
        h.update((HERE / n).read_bytes())
    return h.hexdigest()[:16]


# --------------------------------------------------------------------------
# Request construction — the only place capture semantics live.
# --------------------------------------------------------------------------
def build_payload(kind: str, item: dict, model: str, cfg: dict) -> dict:
    """Return the exact JSON body POSTed to /v1/completions."""
    s = cfg["sampling"]
    logprobs = int(s["logprobs"])
    if logprobs > 5:
        raise ValueError("logprobs max is 5 on the completions API")
    if kind == "generate":
        payload = {
            "model": model,
            "prompt": item["prompt"],
            "max_tokens": int(item.get("max_tokens", s.get("max_tokens", 16))),
            "temperature": float(item.get("temperature", s["temperature"])),
            "top_p": float(s["top_p"]),
            "logprobs": logprobs,
            "echo": bool(item.get("echo", False)),
            "n": 1,
        }
    elif kind == "score":
        # echo=true + max_tokens=0 -> echo the provided text with per-token logprobs,
        # generate nothing. This measures the model's probability of the fixed string.
        payload = {
            "model": model,
            "prompt": item["text"],
            "max_tokens": 0,
            "temperature": 0.0,
            "top_p": 1.0,
            "logprobs": logprobs,
            "echo": True,
            "n": 1,
        }
    else:
        raise ValueError(f"unknown probe kind: {kind}")
    # seed is recorded for provenance; legacy base models may ignore it. Only send if set.
    if s.get("seed") is not None:
        payload["seed"] = int(s["seed"])
    return payload


# --------------------------------------------------------------------------
# HTTP with fail-closed retries. Raw body preserved verbatim.
# --------------------------------------------------------------------------
KEEP_HEADERS = ("openai-version", "openai-model", "openai-organization",
                "x-request-id", "date", "x-ratelimit-remaining-requests")


def post_completion(endpoint: str, payload: dict, cfg: dict) -> tuple[dict, dict]:
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        sys.exit("OPENAI_API_KEY not set — this tool makes no calls without it.")
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    if os.environ.get("OPENAI_ORG"):
        headers["OpenAI-Organization"] = os.environ["OPENAI_ORG"]
    rc = cfg["request"]
    last = None
    for attempt in range(int(rc["max_retries"])):
        try:
            r = requests.post(endpoint, headers=headers, json=payload, timeout=int(rc["timeout_s"]))
            if r.status_code == 200:
                kept = {k: v for k, v in r.headers.items() if k.lower() in KEEP_HEADERS}
                return r.json(), kept
            # 429 / 5xx -> backoff and retry; 4xx (other) -> stop, it will not fix itself
            if r.status_code not in (429, 500, 502, 503, 504):
                sys.exit(f"HTTP {r.status_code}: {r.text[:400]}")
            last = f"HTTP {r.status_code}"
        except requests.RequestException as e:
            last = str(e)
        wait = float(rc["backoff_base_s"]) * (2 ** attempt)
        print(f"    retry {attempt+1}/{rc['max_retries']} after {last} — waiting {wait:.0f}s", flush=True)
        time.sleep(wait)
    sys.exit(f"gave up after {rc['max_retries']} retries: {last}")


# --------------------------------------------------------------------------
# Capture loop
# --------------------------------------------------------------------------
def iter_probes(probes: dict):
    for kind in ("generate", "score"):
        for item in probes.get(kind, []) or []:
            if "id" not in item:
                sys.exit(f"probe missing 'id' in section '{kind}': {item}")
            yield kind, item


def manifest_path(outdir: Path) -> Path:
    return outdir.parent / "run-manifest.jsonl"


def already_done(rows: list[dict], model: str, pid: str, it: int, req_hash: str) -> bool:
    for r in rows:
        if r["model"] == model and r["probe_id"] == pid and r["iteration"] == it \
           and r["request_sha256"] == req_hash:
            return True
    return False


def load_manifest(mpath: Path) -> list[dict]:
    if not mpath.exists():
        return []
    return [json.loads(line) for line in mpath.read_text().splitlines() if line.strip()]


def main():
    ap = argparse.ArgumentParser(description="Phase 0.1 base-model capture (davinci-002, babbage-002)")
    ap.add_argument("--dry-run", action="store_true", help="build + print requests, make NO API calls")
    ap.add_argument("--only", nargs="*", default=None, help="only these probe ids")
    ap.add_argument("--models", nargs="*", default=None, help="only these model ids")
    args = ap.parse_args()

    cfg = load_yaml("config.yaml")
    probes = load_yaml("probes.yaml" if (HERE / "probes.yaml").exists() else "probes.example.yaml")
    ph = prereg_hash("config.yaml",
                     "probes.yaml" if (HERE / "probes.yaml").exists() else "probes.example.yaml")

    models = args.models or cfg["models"]
    endpoint = cfg["endpoint"]
    iters = int(cfg.get("iterations_per_probe", 1))
    outroot = HERE / cfg.get("output_dir", "raw")
    mpath = manifest_path(outroot)
    rows = load_manifest(mpath)

    plan = [(k, it) for (k, it) in iter_probes(probes)
            if (args.only is None or it["id"] in args.only)]
    print(f"[prereg {ph}] {len(models)} model(s) x {len(plan)} probe(s) x {iters} iter — "
          f"endpoint={endpoint}  deadline={cfg.get('deadline','?')}")
    if args.dry_run:
        print("[dry-run] no API calls will be made\n")

    n_new = 0
    for model in models:
        for kind, item in plan:
            for it in range(iters):
                payload = build_payload(kind, item, model, cfg)
                req_hash = sha256_bytes(canon(payload))
                pid = item["id"]
                if args.dry_run:
                    print(f"  {model} :: {pid} ({kind}) it{it}  req={req_hash[:12]}")
                    print("    " + json.dumps(payload)[:300])
                    continue
                if already_done(rows, model, pid, it, req_hash):
                    print(f"  skip {model}/{pid} it{it} (already captured)")
                    continue
                print(f"  capture {model}/{pid} ({kind}) it{it} ...", flush=True)
                body, kept_headers = post_completion(endpoint, payload, cfg)
                resp_hash = sha256_bytes(canon(body))
                record = {
                    "capture": {
                        "prereg_hash": ph, "probe_id": pid, "kind": kind, "model": model,
                        "iteration": it, "captured_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                        "request_sha256": req_hash, "response_sha256": resp_hash,
                    },
                    "request": {"endpoint": endpoint, "payload": payload},
                    "response_headers": kept_headers,
                    "response": body,
                }
                mdir = outroot / model
                mdir.mkdir(parents=True, exist_ok=True)
                fpath = mdir / f"{pid}__it{it:02d}.json"
                fpath.write_text(json.dumps(record, indent=2, ensure_ascii=False))
                row = {
                    "file": str(fpath.relative_to(HERE)), "prereg_hash": ph, "model": model,
                    "probe_id": pid, "kind": kind, "iteration": it,
                    "request_sha256": req_hash, "response_sha256": resp_hash,
                    "bytes": fpath.stat().st_size,
                    "captured_at": record["capture"]["captured_at"],
                }
                with mpath.open("a") as fh:
                    fh.write(json.dumps(row) + "\n")
                rows.append(row)
                n_new += 1

    if not args.dry_run:
        print(f"\nDone. {n_new} new capture(s). Manifest: {mpath.relative_to(HERE)}")
        print("NEXT: run build_manifest.py to fold run-manifest.jsonl into a hashed manifest.json,")
        print("      then back up raw/ off-platform (CAPTURE-RUNBOOK.md). raw/ is git-ignored.")


if __name__ == "__main__":
    main()
