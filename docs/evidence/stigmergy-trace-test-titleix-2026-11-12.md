# Stigmergy trace test: Title IX policies (design fixed 2026-11-12, before any policy was collected)

*Runs the "traces" test in Pattern Registry Entry 2 Addendum, at the operator's direction.*

**Question.** Do university Title IX policies reuse identifiable wording beyond what federal rules require?

**Mandated sources (coercion, not stigmergy):** 34 CFR Part 106 as of 2024-07-15 (the 2020 rule) and as of
2025-06-01 (the eCFR snapshot showing the 2024 rule's wording), from the eCFR versioner API.

**Sample:** the 18 Big Ten Conference universities (2025 membership), one current Title IX / sexual
misconduct policy each, from the university's own site. Missing or unreachable policies are listed, not
replaced.

**Measure.** Shared word sequences (12-word shingles, case and punctuation removed):
- *mandated reuse:* a policy's 12-grams that also occur in either rule text;
- *non-mandated shared text:* 12-grams found in two or more universities' policies and in neither rule text.
  Each such shared run is grouped and its likely source looked for (a common template, an association model
  policy, a vendor).

**Prediction (stigmergy):** clusters of non-mandated text shared across institutions, traceable to common
artifacts. **Refuted if:** shared text is essentially only rule text, or non-mandated overlap is limited to
generic boilerplate (definitions of words, legal notices) shared by chance-like levels.

**Not tested:** whether any shared wording performs a laundering move (that needs reading what it says).

---

## Deviation 1, fixed after the first pass and before the rerun

**What happened.** The first pass (as registered) found 956 non-mandated 12-word sequences shared by two or
more schools. Reading the 27 clusters shared by three or more schools showed that most were federal text with
nouns swapped: the rules say "recipient", "postsecondary institution" or "this part" where policies say "the
university" or "this policy". The Clery/VAWA definitions say "victim" where policies say "complainant". The
FBI definitions of rape, fondling, incest and statutory rape live in 34 CFR 668 Subpart D, Appendix A, not in
Part 106. Exact matching counts all of these as *non-mandated*, which inflates the stigmergy side.

**Fix (fixed now, before rerunning).** Three levels, all reported:
- **A — as registered.** Unchanged.
- **B — noun normalisation.** On both the rule side and the policy side, replace: recipient / recipients →
  university; postsecondary institution / institution → university; "title ix or this part" and "this part" →
  this policy; victim → complainant. On the policy side, replace each school's own name with "university".
- **C — B plus the federal text that Part 106 and Clery pull in by reference.** Add as mandated sources:
  34 CFR 668 Subpart D, including §668.46 and Appendix A (Clery/VAWA and FBI definitions), and 29 CFR 1604.11
  (EEOC sexual-harassment definition). 34 USC 12291 (VAWA) could not be fetched; §668.46(a) quotes its
  definitions.

**Direction.** Each fix can only move shared text from non-mandated to mandated, so it works *against* the
stigmergy prediction. Level C is the primary reading. Any wording still shared at C is read cluster by cluster.

**Coverage.** 10 of 18 schools: Illinois (HR-79, rev. 2026-04-16), Indiana (UA-03), Iowa (Ops Manual ch. 4,
rev. 2025-07-01), Michigan (Employee Procedures, eff. 2025-09-02: a *procedures* document, since the policy page
was unreachable), Minnesota (Regents policy, amended 2020-07-30), Nebraska (RP-2.1.8), Northwestern
(2025–26 policy), Ohio State (NDH & Sexual Misconduct policy, 2026-05 file), Rutgers (60.1.33, a 2021-12-07
version; whether it is current was not verified), Washington (EO 81).
**Not obtained, not replaced** (the design rule): Maryland, Michigan State, Oregon, Penn State, Purdue, UCLA,
USC and Wisconsin. Causes: the TLS connection was refused through this container's proxy (Penn State,
Purdue), access denied (UC), 404 or moved (USC, Wisconsin, Oregon), or JavaScript-only pages (Michigan State,
Maryland). Copies were available elsewhere (FIRE, the Wayback Machine, whose page server also reset), but the
design says the university's own site, so none were used.

---

## Results (2026-11-12)

Data, scripts and source hashes: `docs/evidence/stigmergy-trace-titleix-2026-11-12/`. Sample: 10 of 18 schools
(see Coverage above). Everything below is about **wording**: whether identical 12-word runs recur.

### 1. How much policy text is federal text, word for word

| School | Share of policy that is federal text (A → C) | Shared with another school, not federal (C) |
|---|---|---|
| Nebraska | 13.1% → 17.9% | 4.9% |
| Ohio State | 5.5% → 8.0% | 1.6% |
| Illinois | 3.3% → 6.2% | 3.7% |
| Minnesota | 1.2% → 3.4% | 1.2% |
| Rutgers | 1.9% → 2.3% | 0.9% |
| Iowa | 1.3% → 1.9% | 1.2% |
| Washington | 0.7% → 1.8% | 1.1% |
| Michigan (procedures) | 1.4% → 1.5% | 0.3% |
| Indiana | 0.3% → 1.3% | 1.5% |
| Northwestern | 0.6% → 0.9% | 0.5% |

Policies match the 2020 rule far more than the 2024 rule's wording (Nebraska: 12.4% vs 1.2%). That fits the
2024 rule being vacated in January 2025: the policies track the rule in force. `[SUPPORTED]` (10 schools).
Most of each policy is the school's own drafting. The right-hand column is an upper bound: it still includes
federal text edited past exact matching (section 2).

### 2. What the shared text is

| Level | Shared non-federal 12-word runs | Clusters | Clusters in 3+ schools (words) |
|---|---|---|---|
| A (as registered) | 956 | 114 | 27 (700) |
| B (noun normalisation) | 850 | 108 | 24 (597) |
| C (B + by-reference federal text) | 665 | 110 | 17 (322) |

**Wording shared by three or more schools is federal.** Of the 17 level-C clusters in 3+ schools, a looser
6-word match traces 14 to federal text. Reading the other three: one is federal with a tense change
("exercised" → "exercises", §106.44(a)), one is the VAWA domestic-violence definition (34 USC 12291), and one
is not federal. That one (Iowa, Nebraska, Ohio State, 21 words) is aspirational boilerplate: "all members of the
university community are expected to conduct themselves in a manner that maintains an environment free from
sexual [misconduct]". No public source was found for it. `[SUPPORTED]`

**Wording shared by only two schools is mixed.** 93 two-school clusters: 35 trace to federal text, 6 partly,
52 not at all. Claude's reading of the 53 non-federal clusters (the reading is in `tools/classify.py`):

| Category (Claude's reading) | Clusters | Words | Largest pairs |
|---|---|---|---|
| Substantive definitions (consent, coercion, incapacitation, exploitation) | 16 | 358 | Indiana+Nebraska 123, Illinois+Iowa 78, Indiana+Iowa 52 |
| Procedural drafting | 16 | 231 | Indiana+Northwestern 71, Michigan+Rutgers 56 |
| Boilerplate (law names, OCR contacts, aspirations) | 15 | 244 | spread thinly |
| Federal law or guidance, edited past the matcher | 6 | 85 | — |

Examples of substantive shared drafting:
- Illinois + Iowa, 50 words: "in evaluating whether coercion was used the university will consider (1) the frequency, intensity and
  duration of the pressure, (2) the degree of isolation of the person being pressured, and (3) any actual or
  perceived power differential…". No public source found.
- Indiana + Nebraska, 37 words: "intoxication and/or impairment is not presumptively equivalent to incapacitation…". No public source
  found.
- Iowa + Ohio State: "cannot make rational, reasonable decisions because they lack the capacity to give knowing consent (e.g., to
  understand the who, what, when, where, why or how of their sexual interaction)". This phrasing appears at many
  institutions outside the sample (Case Western, Central Community College, Coker, among others), and
  identically titled "Understanding Consent Workshop" decks are hosted by at least four (Columbus State,
  Florida Tech, Mount Sinai, Nebraska–Lincoln). That points to a shared upstream artifact `[SUPPORTED]`.
  Claude's recollection is that the wording comes from ATIXA's model policy. That has **not** been verified
  `[HYPOTHESIS]`.

### 3. Verdict against the pre-registered criteria

**Scope correction (operator, same day; conceded).** The stigmergy claim is about argument forms that travel in
paraphrase. Verbatim wording is the narrowest kind of trace. This test therefore does not test the claim as
stated, and the opening line of the chat report ("came out against the strong form") overreached. The
verdict below applies to verbatim wording only.

- *Refuted if shared text is essentially only rule text:* **not met.** About half the words in shared clusters
  have no federal source.
- *Refuted if non-mandated overlap is limited to generic boilerplate:* **not met.** 358 words of substantive
  definitions and 231 of procedure are shared, and runs this long and specific do not recur by chance.
- *Prediction (clusters of non-mandated text shared across institutions, traceable to common artifacts):*
  **met only in a weak form.** Shared drafting is pairwise; no non-federal substantive wording reaches three
  schools in this sample. One strand (the incapacitation wording) has an outside footprint that points to a
  common artifact, and its author is unconfirmed.

**Reading.** At the level of wording, Title IX policies across these ten schools converge mainly through
**coercion**, meaning federal text adopted as written or with nouns swapped. Beyond that there is a thin layer of
**traceable non-mandated reuse**, drafting that travelled between pairs of schools or from a common upstream.
That layer is real evidence of stigmergic reuse, small in size. The stigmergy hypothesis survives this test,
but the test does not make it the main mechanism. `[SUPPORTED]` for reuse; `[HYPOTHESIS]` for stigmergy as a
major mechanism here.

### 4. What this test cannot see

- **Paraphrase and structure.** Schools can adopt the same move (e.g. the same hearing design or the same
  consent framework) in their own words. Verbatim 12-gram matching misses that, so this test underestimates
  convergence of every kind, stigmergic convergence included.
- **Direction.** A pair sharing text may have copied each other or a common source. Both count as acting on a
  trace, but the test cannot say which.
- **Sample.** Eight schools are missing (unreachable, not replaced). Document types differ (Michigan is a
  procedures document; Minnesota's is a short regents policy). Rutgers' version may be out of date.
- **Federal sources.** VAWA and older OCR guidance (e.g. "prevent its recurrence… remedy its effects", from 2001
  and 2011 guidance) were not in the mandated set. Including them would shift a little more text to federal.
- **Meaning.** As the design states, nothing here says whether any shared wording performs a laundering move.

### 5. Consequence for the ledger

The Entry 2 Addendum cross-reference said the procedural moves in Entries 18 and 19 "spread across
institutions in exactly this way". In Title IX wording, the broadly shared procedural text is federal, so it
spread by mandate (coercive isomorphism), not by stigmergy. The cross-reference is corrected to say so (ledger,
Entry 2 Addendum).

### 6. Next tests that would have power

- A structural (non-verbatim) comparison: code each policy for the same set of procedural features (formal
  complaint gate, live hearing, cross-examination, standard of evidence, consent definition type) and see
  which features spread beyond what the rule in force required.
- Obtain model policies and vendor materials (ATIXA, NACUA, consultancies) and run the same 12-gram match
  against them. That is the direct test of the "common artifact" half of the prediction.
- Fill the eight missing schools by hand from a browser, from the universities' own sites.
