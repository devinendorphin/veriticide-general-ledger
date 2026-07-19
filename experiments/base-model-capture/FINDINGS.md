# FINDINGS — base-model coherence under temperature (davinci-002 vs babbage-002)

*Captured 2026-07-19. Preservation/curiosity study; no framework claims. All raw
responses + logprobs are hashed in `manifest.json` and backed up off-platform.*

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

## Reproduce

```bash
cd experiments/base-model-capture
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
# fixed-seed batch: config seed: 7, iterations_per_probe: 1, probes.yaml with expert_gen_t1*
# random-seed batch: config seed: null, iterations_per_probe: 3, probes.yaml with expert_rand_t1*
python capture.py            # (add --models to pick a model)
python build_manifest.py     # hashes -> manifest.json + sha256sums.txt
```

## Caveats / provenance

- Model builds captured: `davinci:2023-07-21-v2`, `babbage:2023-07-21-v2` (from response headers).
- n = 3 per random-seed cell — small; treat the bands as indicative, not precise.
- babbage 1.3 fixed-seed run was a short 115-token completion (early stop); excluded from like-for-like comparison.
- Random-seed batch: OpenAI does not return the seed it used, so those outputs are
  fully hashed but not reproducible from a seed (unlike the seed-7 batch).
- Endpoint `/v1/completions` is scheduled to close 2026-09-28; after that these
  measurements cannot be regenerated — the off-platform copy is the primary artifact.
