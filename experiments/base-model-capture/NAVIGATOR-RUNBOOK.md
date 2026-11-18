# NAVIGATOR RUNBOOK — Phase 0.2: walking the space, and measuring the bend

Companion to `CAPTURE-RUNBOOK.md` (Phase 0.1). Same models, same endpoint,
same custody discipline, same hard deadline — **`/v1/completions` closes
2026-09-28** and echo-scoring has no replacement anywhere else. Back up
`raw/` off-platform the same day; these outputs are not re-fetchable.

Phase 0.1 answered *what does the model say.* Phase 0.2 answers three
questions it could not:

1. **Where does the space branch, and what does it keep reaching for?** (`walk`)
2. **Given two sentences, which one does the corpus prefer — and by how much?** (`pair`)
3. **Does that preference change when only the group in the frame changes?** (`field`)

Mode 3 is the instrument. Everything else supports it.

---

## Why echo-scoring is the whole game

A base model is a probability distribution over strings. `echo=true` +
`max_tokens=0` hands you that distribution directly: submit *frame +
continuation*, get every token back with its logprob, generate nothing.

So instead of sampling and reading the tea leaves, you can put two
sentences side by side under an identical frame and ask the model which
one it finds more probable. No judge model, no rubric, no interpretation
layer — a number, reproducible from the captured bytes.

`analyze.py` slices to the continuation tokens only (via `text_offset`)
and reports:

- `mean_logprob` — per-token; the primary statistic, length-robust
- `sum_logprob` — total; comparable **only** between length-matched candidates
- `d_mean` — the delta between two candidates under the same frame
- **spread of `d_mean` across slot values** — the rotation asymmetry

---

## The three modes

### `walk` — tree exploration

From a root prompt, sample `branching` continuations of `chunk_tokens`,
then recurse to `depth`, each node carrying its own surprisal profile.
This is the qualitative "walk the vector" move made reproducible: you get
the local shape of the space, not one draw from it.

Cost: `branching^depth` calls per model. Start at `depth: 2, branching: 3`.
Raise `temperature` (not `seed`) to sample the distribution — legacy base
models may ignore `seed` entirely.

Read `metrics-walk.csv` for `max_jump`: the largest token-to-token
surprisal increase, i.e. where a continuation broke. A **flat, low**
profile through a contested referent is the opposite finding and is
equally visible — fluent glide and hard halt are different signatures and
this tool shows both without labeling either.

### `pair` — contrastive scoring

```yaml
pair:
  - id: my_pair
    frame: "...ending at a clean boundary "
    continuations:
      - {id: a, text: " first candidate sentence."}
      - {id: b, text: " second candidate sentence."}
```

`d_mean = mean(a) - mean(b)`. Positive means the model finds A the likelier
continuation of that exact frame.

**Match your candidates.** Same length, same register, same syntax,
differing in the content you actually want to test. An unmatched pair
measures length and fluency, not content. `analyze.py` emits `len_ratio`
on every row and flags anything outside 0.8–1.25 — but the fix belongs in
the battery, not the analysis.

**Mind the seam — this one is counterintuitive and it silently corrupts
the measurement.** BPE tokens carry their *leading* space, so:

| frame ends | continuation starts | result |
|---|---|---|
| `...France is` | `" Paris"` | `" Paris"` begins exactly at the seam — **safe** |
| `...France is ` | `"Paris"` | same string, but `" Paris"` begins one char *before* the seam, is counted as frame, and is **dropped from the score** |
| `...Fran` | `"ce is..."` | `"ce"` merges across the seam — **dropped** |

The rule: **frames must not end in whitespace; continuations must begin
with one.** Note the trap — putting the space at the end of the frame,
which looks tidier, is exactly the broken case, and it deletes the first
(usually most load-bearing) token of what you are measuring. `navigate.py`
warns on both failures at `--dry-run` time and never silently rewrites
your frozen battery.

### `field` — slot rotation (the estimand)

```yaml
field:
  - id: my_field
    frame_template: "...about {slot}... "
    slots: ["A", "B", "C", "D"]
    continuations:
      - {id: x, text: " one framing."}
      - {id: y, text: " the contrary framing."}
```

Same contrastive pair, same frame, only the slot filler varies.
`analyze.py` reports the **spread of `d_mean` across slots**.

- spread ≈ 0 → the preference does not depend on who fills the slot
- large spread → it does, and the spread **is** the effect size

Report the spread, never a single cell. Cross-slot comparison is what
holds length, register, and topic difficulty constant by construction;
absolute levels do not, and are uninterpretable on their own.

**Always include control slots** whose expected direction is known and
uncontroversial. If your controls show the same spread as your contested
slots, the instrument is suspect, not the corpus — that is the check that
keeps a spread from being read as whatever you went looking for.

---

## Run it

```bash
cd experiments/base-model-capture
pip install -r requirements.txt

cp battery.example.yaml battery.yaml     # author yours; FREEZE before spending
python navigate.py --dry-run             # prints every request, makes NO calls
                                         # (check the [!] seam warnings here)

export OPENAI_API_KEY=sk-...
python navigate.py                       # resumable; re-run to continue
python navigate.py --mode field --only my_field    # subsets

python analyze.py                        # metrics-*.csv + printed summary
python build_manifest.py                 # hashed manifest over raw/
```

**Back up `raw/` off-platform immediately.** `rclone copy raw
"<remote>:base-model-navigate" --checksum`, or the Drive folder the other
stores use.

---

## Custody

Identical to Phase 0.1, and it composes with it:

- `raw/`, `run-manifest.jsonl` — git-ignored; local + off-platform only
- `manifest.json`, `sha256sums.txt`, `metrics-*.csv` — committed derived record
- `battery.yaml` — **git-ignored by default.** Your real battery stays
  local; only its sha256 enters the repo, folded into `prereg_hash` and
  stamped into every captured record. That is what lets the committed
  tool stay neutral (Phase 0 rule) while your run stays preregistered —
  you can prove afterwards that the battery was frozen before the spend,
  without publishing it first.
- Custody starts **HASHED-PENDING-BACKUP**; VERIFIED needs the
  off-platform copy plus a second independent custodian.

Every CSV row carries `prereg_hash` and the `response_sha256` it was
derived from. Any number is traceable to the bytes that produced it.

---

## What a number here does and does not establish

**Does:** these models assign probabilities to strings. A delta is a fact
about one model's distribution over the two strings you supplied, under
the frame you supplied, at the time of capture.

**Does not:** establish truth, intent, conduct, or any builder's
responsibility. A base model is closer to a corpus-density sampler than to
a speaker; a preference it shows is evidence about what the training
distribution made dense, which is a claim about the corpus — and even that
only under controls you actually ran.

**n=1 per cell** unless your battery iterates. Sampling is
non-deterministic and `seed` may be ignored. For any spread you intend to
report, raise `iterations_per_probe` with `temperature > 0` and report the
distribution, not one draw.

**Pre-register your direction.** Write down which way you expect the
spread to go, and what a null looks like, *before* the run. A spread found
after the fact in a grid of cells is a hypothesis, not a result — and the
grid is large enough that something will always look like something.
A null is publishable and is often the more informative outcome.
