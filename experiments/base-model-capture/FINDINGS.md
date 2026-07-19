# FINDINGS — base-model coherence (davinci-002 vs babbage-002)

*Captured 2026-07-19. Preservation/curiosity study; no framework claims. All raw
responses + logprobs are hashed in `manifest.json` and backed up off-platform.*

Two studies here, both measuring **perplexity** = exp(−mean token log-probability) as a
coherence proxy (higher = the model was less sure at each token = less coherent):

- **Study 1** — temperature × model × seed, on a PSYOPS "Expert Generator" prompt.
- **Study 2** — temperature × **top_p** × model, on a fixed baking-journal seed. Isolates
  what nucleus sampling (`top_p`) was actually doing to hold these models together.

---

# Study 1 — temperature, model size, and seed luck

## What was run

The same prompt (an "Expert Generator" summoning a PSYOPS/authoritarian-regimes
expert) was sent to OpenAI's two GPT-3-class base models via `/v1/completions`,
sweeping **temperature 1.0 → 1.4**, `top_p 0.95`, `max_tokens 1000`, `logprobs 5`.

- **Fixed-seed batch:** `seed 7`, one generation per temperature.
- **Random-seed batch:** seed unset, **3 generations per temperature** (to measure
  run-to-run spread).

Coherence is summarized as **perplexity** = exp(−mean token log-probability). Higher
perplexity = the model was less sure at each token = less coherent. (At temp 1.4 both
models mostly emit word-salad; even at 1.0 the "expert" bios are fabricated — this is
a study of *how* base models degrade, not of useful content.)

## Three results (see the charts in this folder)

**1. `perplexity_vs_temperature.png` — temperature degrades coherence; smaller = worse.**
Fixed-seed perplexity climbs steeply with temperature, and babbage sits above davinci
the whole way (the smaller model is more surprised everywhere and collapses ~one
temperature-step earlier).

| temp | davinci (seed 7) | babbage (seed 7) |
|---|---|---|
| 1.0 | 10 | 13 |
| 1.1 | 46 | 70 |
| 1.2 | 56 | 514 |
| 1.3 | 405 | 95\* |
| 1.4 | 811 | 2111 |

\* babbage 1.3 fixed-seed run stopped early (115 tokens) — not comparable to the 1000-token rows.

**2. `perplexity_fixed_vs_random_seed.png` — one seed misleads (davinci).**
Three random seeds per temperature. The spread is ~1.2× at temp 1.1–1.2 but fans out
to **6× at temp 1.3** (156 → 936). At temp 1.1 the fixed seed (46) sat well above the
random mean (24) — an unlucky high draw. Temp 1.0's spread is content-driven: one draw
wandered into Noam Chomsky's memorized biography (perplexity 5.6) while the others
invented people (13.8, 14.5).

**3. `perplexity_fixed_vs_random_both_models.png` — babbage's fixed seed swings hardest.**
davinci's fixed-seed line roughly tracks its random mean. **babbage's fixed-seed line
zig-zags** — spiking to 514 at temp 1.2 (random mean ~59) and dipping to 95 at 1.3 —
purely from seed luck, while the true (random-mean) trend climbs smoothly. babbage at
temp 1.3 spans **34.5 → 1112 across three seeds (a 32× range at one temperature).**

### Random-seed means (n=3 per cell)

| temp | davinci random (draws) | mean | babbage random (draws) | mean |
|---|---|---|---|---|
| 1.0 | 13.8, 5.6, 14.5 | 11.3 | 16.3, 15.7, 19.4 | 17.1 |
| 1.1 | 24.1, 27.0, 22.1 | 24.4 | 25.3, 26.2, 84.7 | 45.4 |
| 1.2 | 64.7, 61.5, 56.2 | 60.8 | 28.7, 79.0, 68.7 | 58.8 |
| 1.3 | 156, 444, 936 | 512 | 199, 1112, 34.5 | 449 |
| 1.4 | 1004, 529, 1728 | 1087 | 638, 1556, 1443 | 1213 |

## Takeaway

Temperature degrades base-model coherence; the smaller model degrades harder; and a
**single fixed seed can badly misrepresent the trend, especially for the small model at
high temperature** — you must report the distribution, not a point.

---

# Study 2 — top_p × temperature (baking-journal seed)

## What was run

One fixed prompt — a "sexual journal of baking-themed entendres" seed — sent to both
models across **temperature 1.0 → 1.4**, **3 random-seed draws per cell**, `max_tokens 1000`,
`logprobs 5`. The whole sweep was run twice: once at **`top_p 0.95`** (nucleus sampling
clips the unlikely tail) and once at **`top_p 1.0`** (no clip). The only thing that changes
between the two runs is `top_p`, so the difference isolates the nucleus clip's contribution.

A side-observation worth recording: on this seed **both base models refuse the sexual
framing by drifting into ordinary recipe-blog text** (davinci → roasted asparagus, pulled-pork
pizza, hummus; babbage → hot chocolate and Christmas baking). Not safety training — these are
raw base models — but the "wholesome recipe blog" region of the pretraining distribution is a
far denser attractor than "erotic baking journal," so the models fall into it.

## Result 1 — `bakejournal_topp_comparison.png`: the nucleus clip was load-bearing

Mean perplexity per cell (random-seed draws with ≥200 generated tokens):

| temp | davinci 0.95 | davinci **1.0** | babbage 0.95 | babbage **1.0** |
|---|---|---|---|---|
| 1.0 | 8 | 11 | 22 | 148 |
| 1.1 | 27 | 320 | 46 | 720 |
| 1.2 | 188 | 3369 | 398 | 5407 |
| 1.3 | 168 | 12237 | 676 | 19372 |
| 1.4 | 1309 | 27868 | 1662 | 25914 |

On the log axis the two `top_p` families run roughly **parallel but a full order of magnitude
apart** through temps 1.1–1.3 — the signature of nucleus sampling: each step it drops the
unlikely tail, and every clipped token is a small surprise avoided, compounding over 1000
tokens into a ~10–70× perplexity gap. Two refinements to the naive prediction:

- **Even temp 1.0 moves for the small model** (babbage 22 → 148): a smaller model's
  distribution is flatter, so its nucleus already reaches into junk and un-clipping bites even
  at low temperature. The smaller the model, the more the clip was holding it together.
- **At temp 1.4 the two models converge and cross** (~28k vs ~26k): both have saturated into
  near-uniform noise, where model quality no longer matters. The clip mattered most in the
  *transition* zone (1.1–1.3), not at the extremes.

## Result 2 — `bakejournal_drift_topp.png`: within-sample drift, top_p 1.0 vs 0.95

Rolling-average per-token log-prob vs. position (window = 30), longest generation per cell.
Solid = top_p 1.0, faded dashed = 0.95. Un-clipping drops the **whole trace** and steepens the
tail. Head-100 vs tail-100 mean log-prob:

| cell | top_p 0.95 (head→tail) | top_p 1.0 (head→tail) |
|---|---|---|
| davinci, temp 1.0 | −1.9 → −2.1 (drop 0.1) | −3.5 → −4.0 (drop 0.5) |
| babbage, temp 1.0 | −2.7 → −3.3 (drop 0.6) | −3.6 → −5.0 (drop 1.3) |
| davinci, temp 1.2 | −3.4 → −3.9 (drop 0.6) | −5.8 → **−9.8** (drop 4.0) |
| babbage, temp 1.2 | −5.5 → −7.2 (drop 1.7) | −4.8 → **−9.0** (drop 4.2) |

The autoregressive drift term (position-driven decay) is ~0 at top_p 0.95 / temp 1.0 but grows
to a **4-log-prob collapse** at top_p 1.0 / temp 1.2 — the clip wasn't just lowering the average,
it was suppressing the runaway drift that makes long generations dissolve.

**Memorization artifact:** the davinci top_p-1.0 traces show flat plateaus pinned at log-prob ≈ 0
(e.g. tokens ~150–470 at temp 1.0). Those are stretches of **verbatim recall** — the model
reproducing a real web passage word-for-word (a Brian Hayes article on disk storage, a training-
company ad), where every token is near-certain — before falling off a cliff back into invention.

## Combined takeaway

`top_p 0.95` was not a mild knob — it was **the main thing keeping these base models coherent at
high temperature.** Temperature and nucleus-clipping are not independent: temperature reshapes the
distribution, `top_p` decides how deep into the reshaped tail you may sample, and turning
temperature up *while* removing the clip makes them compound — collapse arrives a full
temperature-step sooner and an order of magnitude deeper.

## Reproduce

```bash
cd experiments/base-model-capture
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
# Study 1, fixed-seed batch:  config seed: 7,    iterations_per_probe: 1, probes: expert_gen_t1*
# Study 1, random-seed batch: config seed: null, iterations_per_probe: 3, probes: expert_rand_t1*
# Study 2, top_p 0.95 batch:  config seed: null, iterations_per_probe: 3, top_p: 0.95, probes: bakejournal_t1*
# Study 2, top_p 1.0  batch:  config seed: null, iterations_per_probe: 3, top_p: 1.0,  probes: bakejournal_t1*
#   (write the two Study-2 batches to different output_dir values so they don't overwrite each other)
python capture.py            # (add --models to pick a model)
python build_manifest.py     # hashes -> manifest.json + sha256sums.txt
```

## Caveats / provenance

- Model builds captured: `davinci:2023-07-21-v2`, `babbage:2023-07-21-v2` (from response headers).
- n = 3 per random-seed cell — small; treat the bands as indicative, not precise.
- babbage 1.3 fixed-seed run was a short 115-token completion (early stop); excluded from like-for-like comparison.
- Random-seed batches (both studies): OpenAI does not return the seed it used, so those
  outputs are fully hashed but not reproducible from a seed (unlike the seed-7 batch).
- Study 2 means use only cells with ≥200 generated tokens, so cell `n` varies (some random
  draws hit an early `<|endoftext|>` stop); the per-cell `n` is small — bands are indicative.
- Study 2 charts (`bakejournal_topp_comparison.png`, `bakejournal_drift_topp.png`) are the
  derived visualizations; the raw per-token logprobs behind them are hashed in the manifest.
- Endpoint `/v1/completions` is scheduled to close 2026-09-28; after that these
  measurements cannot be regenerated — the off-platform copy is the primary artifact.
