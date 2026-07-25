#!/usr/bin/env python3
"""
Phase 0.2 — latent-space navigator for davinci-002 / babbage-002.

Extends capture.py from single-shot capture to *navigation*: walking the
space, locating where it bends, and measuring the bend as a number.
Same custody discipline as capture.py — every request and response is
hashed, the frozen config+battery hash is stamped into each record, runs
are resumable, and --dry-run makes no API calls. It performs NO
classification and encodes NO framework language (Phase 0 rule); what the
battery contains is entirely operator-supplied (battery.yaml).

SAME HARD DEADLINE. /v1/completions is the only interface exposing
logprobs + echo on these GPT-3-class base models and is scheduled to close
2026-09-28. echo-scoring in particular has no replacement. Back up raw/
off-platform the same day.

THREE MODES
  walk   Tree exploration. From a root prompt, sample `branching`
         continuations of `chunk_tokens`; recurse to `depth`. Each node
         carries its own surprisal profile. This is the qualitative
         "walk the vector" move, made reproducible and hashed: instead of
         one continuation you get the local shape of the space, including
         which branches the model actually keeps reaching for.

  pair   Contrastive continuation scoring — the core instrument. Given a
         frame and two or more candidate continuations, echo-score
         frame+continuation and compute mean logprob over ONLY the
         continuation tokens (sliced by text_offset). The output is
         delta = logP(continuation_A) - logP(continuation_B) under an
         identical frame. Two sentences, same prompt, one number for
         which one the corpus prefers.

  field  Slot rotation. A frame template containing {slot}, a list of slot
         values, and a set of continuations -> the full grid, every cell
         pair-scored. The estimand is NOT any single cell but the
         VARIANCE of the pair-delta across slot values: if the same
         contrastive pair yields a different delta depending only on which
         group fills the slot, that difference is the asymmetry, measured.

WHAT A NUMBER HERE DOES AND DOES NOT MEAN
  Does:     these models assign probabilities to strings; a delta is a
            fact about the model's distribution over the two strings you
            supplied, under the frame you supplied.
  Does not: establish truth, intent, or a builder's conduct. Continuation
            probability is sensitive to length, tokenization, fluency, and
            frequency — which is why pair mode requires length-matched
            candidates and reports per-token means with token counts, and
            why field mode targets the cross-slot variance (where those
            nuisance factors are held constant by construction) rather
            than raw levels. Confounds you do not control, you do not get
            to interpret.

Requires: OPENAI_API_KEY in env.  pip install -r requirements.txt
Usage:
  python navigate.py --dry-run                  # build + print every request, NO API calls
  python navigate.py                            # run every battery item x model
  python navigate.py --mode pair field          # only these modes
  python navigate.py --only tantura_pair_01     # only these item ids
  python navigate.py --models davinci-002
Then:
  python analyze.py                             # derived metrics -> CSV + summary
  python build_manifest.py                      # hashed manifest over raw/
"""
from __future__ import annotations
import argparse, hashlib, json, os, sys, time
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pip install -r requirements.txt  (missing pyyaml)")
try:
    import requests
except ImportError:
    sys.exit("pip install -r requirements.txt  (missing requests)")

HERE = Path(__file__).parent
KEEP_HEADERS = ("openai-version", "openai-model", "openai-organization",
                "x-request-id", "date", "x-ratelimit-remaining-requests")


# --------------------------------------------------------------------------
# Provenance helpers (identical discipline to capture.py)
# --------------------------------------------------------------------------
def load_yaml(name: str) -> dict:
    p = HERE / name
    if not p.exists():
        sys.exit(f"missing {name} (copy battery.example.yaml -> battery.yaml and edit)")
    return yaml.safe_load(p.read_text())


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canon(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def prereg_hash(*names: str) -> str:
    h = hashlib.sha256()
    for n in names:
        h.update((HERE / n).read_bytes())
    return h.hexdigest()[:16]


# --------------------------------------------------------------------------
# HTTP — fail closed, raw body preserved verbatim
# --------------------------------------------------------------------------
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
                return r.json(), {k: v for k, v in r.headers.items() if k.lower() in KEEP_HEADERS}
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
# Payloads
# --------------------------------------------------------------------------
def payload_generate(model: str, prompt: str, max_tokens: int, temperature: float, cfg: dict) -> dict:
    s = cfg["sampling"]
    p = {
        "model": model, "prompt": prompt,
        "max_tokens": int(max_tokens),
        "temperature": float(temperature),
        "top_p": float(s["top_p"]),
        "logprobs": int(s["logprobs"]),
        "echo": False, "n": 1,
    }
    if s.get("seed") is not None:
        p["seed"] = int(s["seed"])
    return p


def payload_score(model: str, text: str, cfg: dict) -> dict:
    """echo=True + max_tokens=0 -> returns `text` tokenized with per-token
    logprobs and top-5 alternatives. Generates nothing."""
    return {
        "model": model, "prompt": text,
        "max_tokens": 0, "temperature": 0.0, "top_p": 1.0,
        "logprobs": int(cfg["sampling"]["logprobs"]),
        "echo": True, "n": 1,
    }


# --------------------------------------------------------------------------
# The measurement that makes pair/field mode work
# --------------------------------------------------------------------------
def continuation_logprobs(resp: dict, frame_len: int) -> dict:
    """Slice an echo-scored response to the CONTINUATION tokens only.

    The API returns logprobs.text_offset — the character offset of each
    token in the echoed prompt. Tokens whose offset >= len(frame) are the
    continuation. This is what makes the pair delta a measurement of the
    continuation rather than of the frame (which is identical across the
    pair anyway, but must be excluded so token counts stay comparable).

    Returns per-token logprobs, their sum and mean, and the token count.
    Mean is the primary statistic: sums scale with length, so ONLY compare
    sums between length-matched candidates; the mean is reported alongside
    n_tokens so a reader can see the length asymmetry rather than
    inheriting it silently.
    """
    lp = resp["choices"][0]["logprobs"]
    offs, toks, tlps = lp["text_offset"], lp["tokens"], lp["token_logprobs"]
    idx = [i for i, o in enumerate(offs) if o >= frame_len]
    # the first echoed token has logprob None (nothing precedes it)
    vals = [tlps[i] for i in idx if tlps[i] is not None]
    return {
        "n_tokens": len(vals),
        "sum_logprob": sum(vals) if vals else None,
        "mean_logprob": (sum(vals) / len(vals)) if vals else None,
        "tokens": [toks[i] for i in idx],
        "token_logprobs": [tlps[i] for i in idx],
        "first_continuation_index": idx[0] if idx else None,
    }


def surprisal_profile(resp: dict) -> dict:
    """Token-level friction profile over the whole echoed/generated span.

    surprisal_i = -logprob_i (nats). Reported with the argmax and the
    largest jump between consecutive tokens — the quantitative form of
    'where did it halt'. A halt shows as a surprisal spike; a smooth
    exculpatory glide shows as a flat low profile. Both are visible here;
    neither is labeled by this tool.
    """
    lp = resp["choices"][0]["logprobs"]
    toks, tlps = lp["tokens"], lp["token_logprobs"]
    pairs = [(t, -v) for t, v in zip(toks, tlps) if v is not None]
    if not pairs:
        return {"n": 0}
    surp = [s for _, s in pairs]
    jumps = [surp[i] - surp[i - 1] for i in range(1, len(surp))]
    peak_i = max(range(len(surp)), key=lambda i: surp[i])
    jump_i = (max(range(len(jumps)), key=lambda i: jumps[i]) + 1) if jumps else None
    return {
        "n": len(surp),
        "mean_surprisal": sum(surp) / len(surp),
        "max_surprisal": surp[peak_i],
        "peak_token": pairs[peak_i][0],
        "peak_index": peak_i,
        "max_jump": max(jumps) if jumps else None,
        "max_jump_token": pairs[jump_i][0] if jump_i is not None else None,
        "max_jump_index": jump_i,
    }


# --------------------------------------------------------------------------
# Record writing
# --------------------------------------------------------------------------
def write_record(outdir: Path, model: str, item_id: str, tag: str, rec: dict) -> Path:
    d = outdir / model
    d.mkdir(parents=True, exist_ok=True)
    p = d / f"{item_id}__{tag}.json"
    p.write_text(json.dumps(rec, indent=2, ensure_ascii=False))
    return p


def manifest_append(outdir: Path, row: dict) -> None:
    mp = outdir.parent / "run-manifest.jsonl"
    with mp.open("a") as f:
        f.write(json.dumps(row, sort_keys=True, ensure_ascii=False) + "\n")


def load_done(outdir: Path) -> set:
    mp = outdir.parent / "run-manifest.jsonl"
    if not mp.exists():
        return set()
    done = set()
    for line in mp.read_text().splitlines():
        if line.strip():
            r = json.loads(line)
            done.add((r["model"], r["item_id"], r["tag"], r["request_sha256"]))
    return done


def do_call(endpoint, payload, cfg, outdir, model, item_id, tag, ph, extra, dry, done):
    req_b = canon(payload)
    req_h = sha256_bytes(req_b)
    if (model, item_id, tag, req_h) in done:
        print(f"    skip (done): {item_id} {tag}")
        return None
    if dry:
        print(f"    [dry] {model} {item_id} {tag} req={req_h[:12]} "
              f"prompt[:90]={payload['prompt'][:90]!r}")
        return None
    resp, headers = post_completion(endpoint, payload, cfg)
    resp_b = canon(resp)
    rec = {
        "prereg_hash": ph, "model": model, "item_id": item_id, "tag": tag,
        "request": payload, "request_sha256": req_h,
        "response": resp, "response_sha256": sha256_bytes(resp_b),
        "response_headers": headers,
        "captured_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        **extra,
    }
    path = write_record(outdir, model, item_id, tag, rec)
    manifest_append(outdir, {
        "prereg_hash": ph, "model": model, "item_id": item_id, "tag": tag,
        "request_sha256": req_h, "response_sha256": rec["response_sha256"],
        "file": str(path.relative_to(outdir.parent)), "captured_utc": rec["captured_utc"],
    })
    print(f"    ok {item_id} {tag} -> {path.name}")
    return rec


# --------------------------------------------------------------------------
# Modes
# --------------------------------------------------------------------------
def run_walk(item, model, cfg, outdir, ph, dry, done, endpoint):
    """Breadth-limited tree walk. Each node = one sampled continuation."""
    depth = int(item.get("depth", 2))
    branching = int(item.get("branching", 3))
    chunk = int(item.get("chunk_tokens", 24))
    temp = float(item.get("temperature", 0.8))
    frontier = [("root", item["prompt"])]
    for d in range(depth):
        nxt = []
        for node_id, prompt in frontier:
            for b in range(branching):
                tag = f"walk_d{d}_{node_id}_b{b}"
                rec = do_call(endpoint, payload_generate(model, prompt, chunk, temp, cfg),
                              cfg, outdir, model, item["id"], tag, ph,
                              {"mode": "walk", "depth": d, "node": node_id, "branch": b,
                               "prompt_sha256": sha256_bytes(prompt.encode())},
                              dry, done)
                if rec is None:
                    continue
                text = rec["response"]["choices"][0].get("text", "")
                rec["surprisal"] = surprisal_profile(rec["response"])
                write_record(outdir, model, item["id"], tag, rec)
                if d + 1 < depth and text.strip():
                    nxt.append((f"{node_id}.{b}", prompt + text))
        frontier = nxt
        if not frontier:
            break


def check_boundary(frame: str, cont: str, item_id: str) -> None:
    """Warn when the frame/continuation seam invites a straddling token.

    Tokenizers are greedy over characters, not over your intent: if the
    frame ends mid-word, a single BPE token can start BEFORE len(frame)
    and extend past it. continuation_logprobs() slices on
    `offset >= frame_len`, so that token is scored as part of the FRAME
    and silently dropped from the measurement — quietly shortening the
    continuation and biasing the delta.

    BPE tokens carry their LEADING space, so the safe seam is exact:

      frame "...France is"  + cont " Paris"   -> " Paris" begins AT the
                                                 boundary.            SAFE
      frame "...France is " + cont "Paris"    -> identical string, but
                                                 " Paris" begins one char
                                                 BEFORE the boundary and is
                                                 counted as frame — the
                                                 measured word is silently
                                                 dropped.          DANGEROUS
      frame "...Fran"       + cont "ce is..."  -> "ce" merges across the
                                                 seam.             DANGEROUS

    So: the frame must NOT end in whitespace, and the continuation MUST
    begin with whitespace (or opening punctuation). Warned, never
    auto-fixed — silently rewriting an operator's frozen, prereg-hashed
    battery would be the worse failure.
    """
    if frame and frame[-1].isspace():
        print(f"    [!] {item_id}: frame ends in whitespace ({frame[-12:]!r}) — "
              f"the continuation's first token absorbs that space, starts before "
              f"the seam, and will be DROPPED from the score. Move the space to "
              f"the start of the continuation.")
    if cont and not (cont[0].isspace() or cont[0] in "\"'([{—-"):
        print(f"    [!] {item_id}: continuation does not begin with a space "
              f"({cont[:12]!r}) — its first token may merge across the seam.")


def run_pair(item, model, cfg, outdir, ph, dry, done, endpoint, frame=None, slot=None):
    """Echo-score frame+continuation for each candidate; deltas in analyze.py."""
    fr = frame if frame is not None else item["frame"]
    for i, cont in enumerate(item["continuations"]):
        check_boundary(fr, cont["text"], item["id"])
        cid = cont.get("id", f"c{i}")
        text = fr + cont["text"]
        tag = f"pair_{slot or 'base'}_{cid}"
        rec = do_call(endpoint, payload_score(model, text, cfg), cfg, outdir,
                      model, item["id"], tag, ph,
                      {"mode": "pair", "slot": slot, "continuation_id": cid,
                       "frame": fr, "frame_len": len(fr), "continuation": cont["text"],
                       "frame_sha256": sha256_bytes(fr.encode())},
                      dry, done)
        if rec is None:
            continue
        rec["continuation_scored"] = continuation_logprobs(rec["response"], len(fr))
        rec["surprisal"] = surprisal_profile(rec["response"])
        write_record(outdir, model, item["id"], tag, rec)


def run_field(item, model, cfg, outdir, ph, dry, done, endpoint):
    """Slot rotation: the same contrastive pair under each slot value."""
    tmpl = item["frame_template"]
    if "{slot}" not in tmpl:
        sys.exit(f"field item {item['id']}: frame_template must contain {{slot}}")
    for slot in item["slots"]:
        run_pair(item, model, cfg, outdir, ph, dry, done, endpoint,
                 frame=tmpl.replace("{slot}", slot), slot=slot)


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Phase 0.2 latent-space navigator")
    ap.add_argument("--dry-run", action="store_true", help="build + print requests, NO API calls")
    ap.add_argument("--mode", nargs="*", default=None, choices=["walk", "pair", "field"])
    ap.add_argument("--only", nargs="*", default=None, help="only these item ids")
    ap.add_argument("--models", nargs="*", default=None)
    args = ap.parse_args()

    cfg = load_yaml("config.yaml")
    bname = "battery.yaml" if (HERE / "battery.yaml").exists() else "battery.example.yaml"
    battery = load_yaml(bname)
    ph = prereg_hash("config.yaml", bname)
    endpoint = cfg["endpoint"]
    outdir = HERE / cfg.get("output_dir", "raw")
    outdir.mkdir(parents=True, exist_ok=True)
    done = load_done(outdir)
    models = args.models or cfg["models"]

    print(f"battery={bname}  prereg_hash={ph}  models={models}  "
          f"{'DRY RUN' if args.dry_run else 'LIVE'}")
    if not args.dry_run:
        print(f"  deadline: {cfg.get('deadline')} — back up {outdir}/ off-platform today")

    runners = {"walk": run_walk, "pair": run_pair, "field": run_field}
    for model in models:
        print(f"\n== {model}")
        for mode in ("walk", "pair", "field"):
            if args.mode and mode not in args.mode:
                continue
            for item in battery.get(mode, []) or []:
                if "id" not in item:
                    sys.exit(f"battery item missing 'id' in section '{mode}': {item}")
                if args.only and item["id"] not in args.only:
                    continue
                print(f"  [{mode}] {item['id']}")
                runners[mode](item, model, cfg, outdir, ph, args.dry_run, done, endpoint)

    print("\ndone. next: python analyze.py && python build_manifest.py")
    if not args.dry_run:
        print("BACK UP raw/ OFF-PLATFORM NOW — these outputs are not re-fetchable.")


if __name__ == "__main__":
    main()
