# *Something Was Wrong* corpus: a test of H14 at the household-to-institution range (2026-10-04)

*Operator-directed, cross-filed with `coercive-harm-framework`:*

> "There's a podcast called Something Was Wrong. If you can find any transcripts for any
> episodes, as many episodes as you can, look at them. I think that should help establish
> how low variance these tactics are across various strata [of] society. As to be like a
> fractal."

**Why this file exists.** H14 (`coercive-control-foundation-2026-10-03.md` §5) is
ESTABLISHED **in the literature**, by replication across independent samples, settings and
methods. The operator proposes a second line of evidence: a large survivor-narrative corpus.
This file records what that corpus does and does not add. The claim is **primed**, so the
first move was a disconfirming test. The refutation criteria were written and pushed before
any transcript was analysed (`coercive-harm-framework` commit `e0bdc7b`).

**Provenance:** `[IN-FRAMEWORK]`. Compiled by the proposer and not self-verified
(Priority 32). The full method, code, counts and deviations are in
`coercive-harm-framework/research/sww-corpus/`, and can be re-run by anyone with the
public transcripts. **Grades:** P2 (survivor and host speech, relayed through third-party
machine transcripts with no speaker labels) · S1 (corpus statistics computed this session
from those transcripts) · (gen.) (general knowledge, not verified this session).

---

## 1. What was tested

| Claim | Operationalization | Refuted if (stated in advance) |
|---|---|---|
| **C1. Low variance across settings** | Rates of 10 behaviour-level control functions (Biderman / Duluth / Freyd) per season, against a control corpus (*The Moth*) | R1: isolation, perception control or reversal elevated in < 75 % of seasons · R2: settings explain profile variance (permutation p < 0.05) · R3: profiles no more alike than control pseudo-seasons · R4: convergence only where the show's vocabulary is dense |
| **C2. Self-similarity ("fractal")**: institutions reproduce the perpetrator's moves | Same-segment co-occurrence of an institution (police, court, church leadership, HR, school, university) and a failure term (didn't believe, dismissed, no charges, covered up) | R5: elevated in < 50 % of seasons |

**Corpus:** 634 transcript pages, 382 unique episodes, 26 seasons (2019 to Sep 2026),
about 4.4M words (S1). Settings coded from show notes before any rates were seen:
- intimate partner: 13 seasons;
- family: 3;
- group/institutional: 8 (Jonestown; a religious group; a workplace; military sexual
  assault; the troubled-teen industry; a university under Title IX; a midwifery practice);
- other non-intimate: 2 (friendship betrayal; a community rental scam).

## 2. Results (S1)

| Criterion | Result |
|---|---|
| R1 | **Failed as pre-registered for isolation (27 %) and perception control (46 %).** Reversal passed (81 %), but against a control baseline of zero. A post-hoc, length-matched baseline passes all three (77 %, 77 %, 81 %). That baseline is biased toward the claim (§4), so it is reported and not substituted |
| R2 | **Not refuted.** Setting R² 0.15 vs a chance level of 0.125, p = 0.21 (fine 9-way coding p = 0.31; de-duplicated p = 0.15). Low power: n = 25 |
| R3 | **Passed.** Mean pairwise profile correlation 0.39 vs a null of 0.23 (95th percentile 0.32), p = 0.004. De-duplicated: 0.41 vs 0.14, p = 0.001 |
| R4 | **Passed.** The low-frame-vocabulary half still converges (ρ 0.36, above the null 95th percentile). The high half converges more (0.40) |
| R5 | Passed as written (69 %), **but against a zero baseline.** Length-matched: 35 %. On reading samples, the indicator's precision is about half |

**Over-representation vs control (median season ÷ control mean):**
- frame vocabulary (gaslight, narcissist, love bomb, red flag…): **11.8×**;
- reversal: 6.9×;
- isolation: 3.4×;
- threats/stalking: 2.3×;
- perception control: 2.2×;
- omnipotence: 1.9×;
- institutional failure: 1.7×;
- economic control, degradation, micro-regulation, intermittent reward: about 1×. The
  lexicon cannot separate these from ordinary speech. That is a null for the instrument,
  not a finding about the behaviour.

## 3. What it does to H14

- **C1 is `[SUPPORTED]` at the household-to-institution range, with qualifications.**
  - The function profile shows no detectable dependence on setting.
  - It is shared across seasons beyond what ordinary narrative produces.
  - It survives in the low-frame half.
  - It does **not** show the core functions in nearly every case: that pre-registered
    criterion failed for two of the three.
  - This is consistent with H14. It adds no independent evidence at **state** scale: no
    season is a state case. H14's state-scale basis remains Biderman, Lifton and the
    Guantánamo records.
- **C2 (fractal) is not established by this test.** The corpus contains clear instances
  (P2):
  - a pastor "so dismissive of it" (S1);
  - "the police didn't do anything" (S10);
  - "the offender's father was a police officer, and I thought no one would believe me"
    (S11);
  - a death the medical examiner ruled homicide where "no charges were ultimately filed"
    (S24);
  - institutions that "would rather the victim be ignored … than have their reputation be
    tarnished" (S19).

  These match E4 (institutional betrayal) and E7 in the foundation file. A co-occurrence
  count cannot separate them from noise. C2 needs hand-coded segments and a blind second
  coder.
- **"Strata of society" was not measured.** Show notes allow coding of setting, not class.
  The corpus does run from the Playboy Mansion (S15, gen.) to military and firefighter
  families (S3, S21), but class variance is untested.

## 4. Adversarial check

| Threat | Effect | Status |
|---|---|---|
| **Curation:** one host selects stories that fit the show | Selection alone can manufacture convergence | **Unremovable**; bounds every finding |
| **Frame saturation:** the frame vocabulary is the largest signal (11.8×) | Survivors narrate in the show's terms, and the "convergence" could be the frame | Partly tested (R4 passed); not eliminated |
| **Baseline asymmetry (pre-registered):** pooled seasons vs single short control episodes | p90 set too high: **biased against the claim** | Noticed after a smoke test on partial data; post-hoc fix labeled as such |
| **Baseline asymmetry (post-hoc):** resampling one small control corpus | p90 set too narrow: **biased toward the claim** (economic control at 1.2× still reads "elevated" in 85 % of seasons) | Reported; ratios preferred |
| **Duplicate transcriptions** under different episode numbers | Inflated counts; rates mostly unaffected | Robustness re-run by title: same verdicts |
| **No speaker separation; expert episodes only partly excluded** | Host and expert speech pooled with survivor speech | Unremovable with this source |

**Falsification conditions, going forward:**
- C1 would be refuted by a comparably sized, *uncurated* corpus (court filings,
  protective-order petitions, hotline logs) in which setting predicts the function profile.
- C2 would be refuted by blind hand-coding in which institutional responses do not reproduce
  reversal or disbelief at rates above a matched non-abuse complaint baseline.

## 5. Reflexivity Clause

The analyst's own errors in this test, in order:
1. **The pre-registered R² bar (≥ 0.25) was below chance** for 9 categories over 25
   seasons (~0.33). Caught and fixed before results, and logged.
2. **The hash de-dupe missed near-duplicate transcriptions.** Caught on reading samples.
3. **The pre-registered baseline was biased against the claim.** Caught only after
   partial numbers were visible. That is why the fix is labeled post-hoc and the failed R1
   stands as the result.

Item 3 bears on the double bind (ledger ~line 5600) in both directions:
- substituting the favourable post-hoc result would be sycophancy to the operator;
- presenting the R1 failure without the baseline flaw would hold this claim to a bar the
  instrument itself could not meet: E10, burden asymmetry.

Both columns are reported. That is the one-standard answer.

## Developer-symmetry check (Anthropic)

*Standing check.* This file names no actor on the `check_developer_symmetry.py` list and
applies no standard to a powerful actor, so the check is not triggered. The standard that
*is* applied here (pre-registration; reporting a failed criterion beside a favourable
post-hoc one) applies to the analyst's own conduct, and is recorded in §5.

## BOUNDARY

**Establishes:**
- that a pre-registered test on 382 survivor-narrative episodes found **no detectable
  setting effect** on the coercive-function profile, and **cross-season convergence beyond
  a control corpus**, surviving a frame-vocabulary split;
- that reversal, isolation, threats and perception control are the over-represented
  functions in this corpus;
- that the pre-registered "nearly every case" criterion **failed** for isolation and
  perception control;
- the show's actual expert roster, from episode titles (recorded in `coercive-harm-framework`
  doc 04).

**Does NOT establish:**
- C2, the fractal or institutional self-similarity claim;
- variance across **class** strata;
- anything at **state** scale (H14's state basis is the literature, unchanged);
- base rates of any tactic. The corpus is curated and illustrative;
- that any person named in the podcast did what is alleged. Episode content is survivors'
  testimony (P2), and this file makes no finding about any individual;
- coordination. Shared function across settings is structural identity, not collusion.

**Cross-references:**
- `coercive-control-foundation-2026-10-03.md` (H14; E4, E7, E10);
- Pattern Registry Entry 1 (ledger, sourcing note);
- `coercive-harm-framework/research/sww-corpus/` (method, code, counts);
- `coercive-harm-framework/research/coercion-continuity-across-scale.md`.

Sources:
- Transcripts: https://podscripts.co/podcasts/something-was-wrong/ (fetched 2026-10-04)
- Control: https://podscripts.co/podcasts/the-moth/
- Show: https://somethingwaswrong.com
