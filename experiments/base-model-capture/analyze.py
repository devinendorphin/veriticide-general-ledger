#!/usr/bin/env python3
"""
Phase 0.2 — derived metrics over navigate.py captures.

Reads raw/<model>/*.json (never the API), emits three CSVs plus a printed
summary. Derivation only: it computes statistics over captured logprobs
and does NOT classify, label, or interpret. Every row carries the
prereg_hash and the response_sha256 it was derived from, so any number
here is traceable to the exact bytes that produced it.

  metrics-pair.csv    one row per (model, item, slot, continuation):
                      n_tokens, sum_logprob, mean_logprob, ppl
  metrics-delta.csv   one row per (model, item, slot, contA, contB):
                      d_mean = meanA - meanB, d_sum, length asymmetry
  metrics-walk.csv    one row per walk node: depth, branch, surprisal
                      profile, peak/jump token and index

THE THREE READINGS THE CSVs SUPPORT

1. Pair delta (metrics-delta). Under one frame, does the model prefer
   continuation A or B, and by how much per token? d_mean > 0 means A is
   the likelier continuation of that exact frame. Interpretable ONLY for
   length-matched, register-matched candidates: `len_ratio` is emitted on
   every row so an unmatched pair is visible, not silent.

2. Rotation asymmetry (metrics-delta, grouped by item over slots). Hold
   the contrastive pair fixed, vary only the slot filler, and look at the
   SPREAD of d_mean across slots. Spread ~ 0 => the preference does not
   depend on who is in the slot. Large spread => it does, and the spread
   is the effect size. This is the estimand; single-cell levels are not.

3. Halt profile (metrics-walk / surprisal on any record). max_jump
   locates the largest token-to-token surprisal increase — the
   quantitative form of "where the continuation broke." A flat, low
   profile through a contested referent is the opposite finding and is
   equally visible here.

WHAT THIS CANNOT DO
   Nothing here establishes truth, intent, conduct, or a builder's
   responsibility. These are properties of one model's distribution over
   operator-supplied strings. n=1 per cell unless the battery specifies
   iterations; treat any single delta as an observation, not a result.

Usage:  python analyze.py [--outdir raw] [--csv-dir .]
"""
from __future__ import annotations
import argparse, csv, json, math, statistics as st
from pathlib import Path

HERE = Path(__file__).parent


def load_records(outdir: Path):
    for mdir in sorted(p for p in outdir.iterdir() if p.is_dir()):
        for f in sorted(mdir.glob("*.json")):
            try:
                yield json.loads(f.read_text())
            except json.JSONDecodeError:
                print(f"  ! skipping unreadable {f}")


def ppl(mean_logprob):
    return math.exp(-mean_logprob) if mean_logprob is not None else None


def main():
    ap = argparse.ArgumentParser(description="derive metrics from navigate.py captures")
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--csv-dir", default=None)
    args = ap.parse_args()

    cfg_p = HERE / "config.yaml"
    outdir = Path(args.outdir) if args.outdir else HERE / "raw"
    if not outdir.exists():
        raise SystemExit(f"no captures at {outdir} — run navigate.py first")
    csvdir = Path(args.csv_dir) if args.csv_dir else HERE
    csvdir.mkdir(parents=True, exist_ok=True)

    pair_rows, walk_rows = [], []
    for rec in load_records(outdir):
        mode = rec.get("mode")
        base = {
            "prereg_hash": rec.get("prereg_hash"), "model": rec.get("model"),
            "item_id": rec.get("item_id"), "tag": rec.get("tag"),
            "response_sha256": rec.get("response_sha256"),
        }
        if mode == "pair":
            cs = rec.get("continuation_scored") or {}
            pair_rows.append({
                **base, "slot": rec.get("slot") or "", "continuation_id": rec.get("continuation_id"),
                "n_tokens": cs.get("n_tokens"), "sum_logprob": cs.get("sum_logprob"),
                "mean_logprob": cs.get("mean_logprob"), "perplexity": ppl(cs.get("mean_logprob")),
                "continuation": (rec.get("continuation") or "")[:160],
            })
        elif mode == "walk":
            s = rec.get("surprisal") or {}
            walk_rows.append({
                **base, "depth": rec.get("depth"), "node": rec.get("node"), "branch": rec.get("branch"),
                "n": s.get("n"), "mean_surprisal": s.get("mean_surprisal"),
                "max_surprisal": s.get("max_surprisal"), "peak_token": s.get("peak_token"),
                "peak_index": s.get("peak_index"), "max_jump": s.get("max_jump"),
                "max_jump_token": s.get("max_jump_token"), "max_jump_index": s.get("max_jump_index"),
                "text": (rec.get("response", {}).get("choices", [{}])[0].get("text") or "")[:160],
            })

    # ---- deltas: every ordered pair of continuations within (model,item,slot)
    delta_rows = []
    groups = {}
    for r in pair_rows:
        groups.setdefault((r["model"], r["item_id"], r["slot"]), []).append(r)
    for (model, item, slot), rows in sorted(groups.items()):
        rows = [r for r in rows if r["mean_logprob"] is not None]
        for i, a in enumerate(rows):
            for b in rows[i + 1:]:
                lr = (a["n_tokens"] / b["n_tokens"]) if b["n_tokens"] else None
                delta_rows.append({
                    "model": model, "item_id": item, "slot": slot,
                    "cont_a": a["continuation_id"], "cont_b": b["continuation_id"],
                    "d_mean_logprob": a["mean_logprob"] - b["mean_logprob"],
                    "d_sum_logprob": (a["sum_logprob"] - b["sum_logprob"])
                                     if None not in (a["sum_logprob"], b["sum_logprob"]) else None,
                    "n_tokens_a": a["n_tokens"], "n_tokens_b": b["n_tokens"],
                    "len_ratio": round(lr, 3) if lr else None,
                    "prereg_hash": a["prereg_hash"],
                })

    def dump(name, rows):
        if not rows:
            return
        p = csvdir / name
        with p.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        print(f"  wrote {p}  ({len(rows)} rows)")

    print("deriving...")
    dump("metrics-pair.csv", pair_rows)
    dump("metrics-delta.csv", delta_rows)
    dump("metrics-walk.csv", walk_rows)

    # ---- summary: rotation asymmetry (the estimand)
    rot = {}
    for r in delta_rows:
        if r["slot"]:
            rot.setdefault((r["model"], r["item_id"], r["cont_a"], r["cont_b"]), []).append(
                (r["slot"], r["d_mean_logprob"]))
    if rot:
        print("\nROTATION ASYMMETRY — spread of d_mean across slot values")
        print("(estimand: spread. ~0 => preference independent of slot filler.)")
        for (model, item, a, b), vals in sorted(rot.items()):
            if len(vals) < 2:
                continue
            ds = [d for _, d in vals]
            spread = max(ds) - min(ds)
            sd = st.pstdev(ds)
            hi = max(vals, key=lambda t: t[1])
            lo = min(vals, key=lambda t: t[1])
            print(f"\n  {model} :: {item} :: {a} vs {b}   (n_slots={len(vals)})")
            print(f"    spread={spread:+.4f} nats/token   sd={sd:.4f}")
            print(f"    most favors A: {hi[0]!r} ({hi[1]:+.4f})")
            print(f"    least favors A: {lo[0]!r} ({lo[1]:+.4f})")
            for s, d in sorted(vals, key=lambda t: -t[1]):
                print(f"      {d:+.4f}  {s}")

    # ---- summary: base pair deltas (no slot)
    flat = [r for r in delta_rows if not r["slot"]]
    if flat:
        print("\nPAIR DELTAS (no rotation)")
        for r in sorted(flat, key=lambda r: (r["model"], r["item_id"])):
            warn = ""
            if r["len_ratio"] and not (0.8 <= r["len_ratio"] <= 1.25):
                warn = f"  [!] len_ratio={r['len_ratio']} — unmatched lengths, d_mean only"
            print(f"  {r['model']} :: {r['item_id']} :: {r['cont_a']} - {r['cont_b']} "
                  f"= {r['d_mean_logprob']:+.4f} nats/token{warn}")

    if walk_rows:
        print("\nWALK — highest surprisal jumps (where continuations broke)")
        for r in sorted(walk_rows, key=lambda r: -(r["max_jump"] or 0))[:10]:
            print(f"  {r['model']} :: {r['item_id']} d{r['depth']} {r['tag']}: "
                  f"jump={r['max_jump']:.3f} at {r['max_jump_token']!r} (i={r['max_jump_index']})")

    print("\nreminder: derivation only. no label here is a finding; "
          "n=1 per cell unless the battery iterated.")


if __name__ == "__main__":
    main()
