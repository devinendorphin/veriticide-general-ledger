# Stigmergy lineage test: US consent law (design fixed 2026-11-12, before any statute was collected)

*Runs the traces test in Pattern Registry Entry 2 Addendum as widened the same day (argument forms and
structures, kept falsifiable by the shared-arbitrary-feature discriminator), at the operator's direction.*

**Question.** Does the "casserole of chaos" in US consent law have a family tree? That is, do states share
**arbitrary** features (features with no function of their own) in co-travelling bundles that trace to
identifiable sources, or are those features spread across states independently?

**Unit.** The 50 states plus DC. For each, the current criminal statutes defining rape / sexual assault /
sexual abuse / criminal sexual conduct and their definitions sections (including any consent definition).

**Sources.** Each jurisdiction's official legislature or code site, retrieved 2026-11-12, hashed. Where the
official site cannot be reached from this container, a recorded mirror (Cornell LII, Justia, FindLaw, or
another publisher) may be used, stated per state. A jurisdiction with no reachable text is listed as missing.

**Arbitrary markers (primary measure), each assigned in advance to its candidate source family.**
Matched case-insensitively on the statute text; a marker is present (1) or absent (0) per jurisdiction.

| Family (candidate source) | Markers |
|---|---|
| MPC 1962 | "gross sexual imposition"; "deviate sexual intercourse"; "compels" + "to submit"; "substantially impaired" + "power to appraise or control" |
| Michigan 1974 reform | "criminal sexual conduct"; "however slight"; "personal injury"; "force or coercion" |
| New York Penal Law art. 130 | "lack of consent results from"; "forcible compulsion"; "clearly expressed"; "physically helpless"; "mentally disabled" or "mentally defective"; "mentally incapacitated" |
| Affirmative / agreement (WA, WI, IL) | "freely given agreement"; "words or overt actions"; "actual words or conduct"; "manner of dress"; "lack of verbal or physical resistance"; "withdraws consent" |
| Federal 1986 Sexual Abuse Act | "sexual act"; "aggravated sexual abuse"; "renders" + "unconscious"; "knowingly engages" |
| Common law | "carnal knowledge"; "against her will" or "against his will" or "against the will"; "ravish" |
| Unassigned (no family claimed) | "no matter how slight"; "sexual battery"; "intimate parts"; "earnest resistance" or "utmost resistance"; "spouse" within 40 characters of "not" + "offense" or "exception" (marital remnant flag) |

**Test 1 (lineage, primary).** Mean pairwise association (phi) between markers of the **same** family
versus markers of **different** families. Null: shuffle family labels across markers (10,000 permutations).
*Stigmergy predicts* within-family association clearly above between-family association.
*Refuted if* within-family association is not above the permutation null (one-sided p ≥ 0.05).

**Test 2 (family structure, secondary).** Are states more alike in their markers than chance allows, given
how common each marker is and how many markers each state has? Statistic: the sum over state pairs of the
squared number of shared markers. Null: curveball randomisation preserving both row and column totals
(10,000 draws). *Stigmergy predicts* the observed value above the null. *Refuted if* it is not (p ≥ 0.05).

**Test 3 (ledger question, descriptive).** Burden-shifting features, coded by keyword with a spot check by
reading: force required in the base offense; resistance language; marital remnant. Are they concentrated in
particular families (persistence by lineage), or spread evenly?

**Not attempted.** Adoption years (session-law research per feature; out of scope for this pass), so no
claim about timing or direction of copying. Function of the features beyond Test 3. Meaning of the
features, beyond the codebook.

**Guard.** Families are candidate *sources*; a state carrying a family's markers may have taken them
second-hand (from a neighbour, a later model, a court). The test can show a family structure exists. It
cannot by itself name who copied whom. Shared structure from a mandate (there is no federal mandate for
state consent definitions) would be coercion, not stigmergy; none is expected here.

---

## Deviation 1, fixed after collection and before any marker was counted

**Coverage: 35 of 51.**
- *Official sites (26):* AZ, DE, FL, IA, ID, KS, MA, MD, ME, MI, MN, MO, MT, NC, ND, NE, NV, OH, OR, RI, SC, VA,
  VT, WA, WV, WY. Also DC (code.dccouncil.gov), HI (data.capitol.hawaii.gov), AK (akleg.gov print view), SD
  (sdlegislature.gov API) and UT (le.utah.gov, current version file).
- *Recorded mirror, public.law (4):* CA, NY, TX, CO. The official sites sit behind a Cloudflare check
  (CA, NY) or render by script (TX), and CO's official code is on Lexis.
- **Missing, not replaced (16):** AL, AR, CT, GA, IL, IN, KY, LA, MS, NH, NJ, NM, OK, PA, TN, WI. Causes:
  the TLS connection was refused at this container's network edge (CT, IL, NH, WI; IL also returned 503 to
  the page-fetch tool); the official code is on Lexis or script-only with no reachable mirror (AL, AR, GA,
  IN, KY, LA, MS, NJ, NM, OK, TN); PA's official page returned no statute text. Justia and FindLaw both
  returned 403.

**Known bias from the gap.** The missing set includes most of the Deep South (common-law family) and three
of the states named as sources for the affirmative/agreement family (IL, WI) or close to it (NJ). Both
families are under-sampled, which weakens Test 1 for them.

**Trimming.** Whole-chapter downloads were cut to the sexual-offense sections, so that unrelated offenses
cannot trigger markers: DE §§761–780, NV NRS 200.364–200.37x, OR 163.305–163.4xx, SC 16-3-651–16-3-6xx,
WA 9A.44.010–9A.44.12x, WY 6-2-301–6-2-3xx. Script: `tools/trim.py`, then the WY/SC re-cut in the run log.

**Mechanical rules fixed now.**
1. A marker present in fewer than 2 jurisdictions, or in all of them, cannot co-vary. It is reported but
   dropped from Tests 1 and 2.
2. Marital-remnant flag: "spouse" with "not", "exception" or "defense" within 40 characters either side.
   This also catches anti-exemption wording ("whether or not his or her spouse"), so the flag is read by
   hand before being reported.
3. Test 3 keyword codes: *force* = "forcib" / "by force" / "physical force" / "forcible compulsion";
   *resistance* = "resist". Both are spot-checked by reading before being reported.

**Deviation 2 (found while checking the results; it does not change them).** The four public.law mirror
pages carry a shared help note ("Blank Outline Levels…"). It created spurious shared text among CA, CO, NY
and TX in the codebook-free check. Each mirror page was cut at "Up to date", where the site's own matter
begins (it remains in CO, where no other text shares it). All tests were rerun. The marker tests were
identical before and after, so the note never triggered a marker.

---

## Results (2026-11-12)

Data, scripts, source URLs and hashes: `docs/evidence/stigmergy-consent-law-us-2026-11-12/`.
35 of 51 jurisdictions (16 missing, listed above).

### Marker prevalence (how many of the 35 carry each marker)

| Family | Markers (n of 35) |
|---|---|
| MPC 1962 | gross sexual imposition 2 · deviate sexual intercourse 3 · compels…to submit 6 · substantially impaired…power to appraise or control 4 |
| Michigan 1974 | criminal sexual conduct 4 · however slight 23 · personal injury 5 · force or coercion 5 |
| New York art. 130 | lack of consent results from 1 · forcible compulsion 5 · clearly expressed 1 · physically helpless 15 · mentally disabled/defective 7 · mentally incapacitated 12 |
| Affirmative / agreement | freely given agreement 4 · words or overt actions 3 · actual words or conduct 1 · manner of dress 3 · lack of verbal or physical resistance 2 · withdraws consent 0 |
| Federal 1986 | sexual act 14 · aggravated sexual abuse 2 · renders…unconscious 1 · knowingly engages 3 |
| Common law | carnal knowledge 0 · against the will 6 · ravish 1 |
| Unassigned | no matter how slight 0 · sexual battery 7 · intimate parts 14 · earnest/utmost resistance 0 |

20 assigned markers vary enough to enter Test 1 (rule 1). The common-law family has only one usable
marker, so it contributes no within-family pairs. That is expected with most of the Deep South missing.

### Test 1 — do a family's markers travel together? **Yes.**
Mean association between markers of the same family is φ = 0.31; between families it is −0.02
(difference 0.32, permutation p = 0.0001). By family: New York 0.54, Michigan 0.37, affirmative 0.27,
MPC 0.22, federal −0.01. **The federal family shows no lineage**: "sexual act" is too generic to be a
marker.

Robustness (all p ≈ 0.0002):
- dropping each family in turn: difference 0.29–0.37;
- merging the New York incapacity trio into one marker, in case it is one list counted three times: 0.27;
- dropping markers carried by more than half the states: 0.34;
- keeping only the 28 states whose text includes a definitions section: 0.37.

**Pre-registered criterion: not refuted.** `[SUPPORTED]`

### Test 2 — are states more alike than chance, without using family labels? **Yes.**
The observed sharing statistic is 2,383, against a null of 2,110 ± 73 that preserves how common each
marker is and how many markers each state has. z = 3.7, p = 0.0005. **Not refuted.** `[SUPPORTED]`

### Codebook-free check (added; it removes the analyst's marker choices)
The coder who chose the markers knows a lot of state law. The markers could therefore have been chosen
because they were already known to cluster, and Test 2 depends on that choice too. The added check counts
rare 8-word runs (shared by 2–4 jurisdictions), with no codebook at all.
- State pairs in the same dominant family share 8.1 such runs on average; other pairs share 3.0
  (permutation p = 0.007). The state grouping still uses the markers, but the text measure does not.
- The strongest pairs, found mechanically:
  - Colorado–Wyoming 95 (identical "intrusion, however slight…", "causes submission… by threatening to
    retaliate" and "intimate parts" definitions);
  - **Michigan as a hub**: SC 87, RI 66, NC 45, MN 40 (the "criminal sexual conduct" degree structure and
    "mentally incapacitated means…" definitions);
  - Oregon–Washington 56, Iowa–Oregon 31, New York–Washington 28 (the New York family).
- Direction of copying is not tested: adoption years were not collected. That Michigan's 1974 reform is
  the root rests on the coder's background knowledge `[HYPOTHESIS]`. That Michigan's text is shared with
  four states is measured `[SUPPORTED]`.

### Test 3 — do burden-shifting features run in families? **Measure failed; hand reading instead.**
The keyword "resist" mostly hits text saying the victim was *unable* to resist, or that resistance is
*not* required, so the keyword code is unusable. The force keyword hits 29 of 35, too common to separate
families. Hand reading of every "resist" hit:
- **Resistance expressly not required:** AK, DC, FL, ME, MI (§750.520i), MN, MT, OR (§163.315).
  HI's own annotation records the 1986 deletion of the requirement that force "overcome resistance".
- **Resistance still carries weight:**
  - **WA**: "forcible compulsion means physical force which overcomes resistance". This is the New York-family
    term with a resistance condition attached. NY's and OR's current definitions of the same term carry
    no resistance condition, and HI deleted it. *Within the New York family, the burden-shifting variant
    survives in one branch.*
  - **NE** "need only resist, either verbally or physically, so as to make the victim's refusal to consent
    genuine and real and so as to reasonably make known to the actor…"; **DE** "need resist only to the
    extent that it is reasonably necessary to make the victim's refusal to consent known to the defendant".
    The same construction in different words: resistance downgraded to a duty to signal. **This is the
    paraphrase-level trace the 12-gram method cannot count.** Two states cannot establish lineage.
  - **ID** "where the victim resists but the resistance is overcome by force" (one route among several).
  - **WY** "by any means that would prevent resistance by a victim of ordinary resolution".
- **Marital flag, read by hand:**
  - *Explicit anti-exemption:* IA, MI (§520l), NC (§14-27.34), NV (§200.373), VA ("whether or not his or her
    spouse").
  - *Spouse carved out of particular offenses:* CO (age-based offenses), ME (age- and supervision-based
    offenses), MI (professional–client contact). OH and RI define "spouse" with exceptions, which means some
    provision still distinguishes spouses; where it applies was not read here.
  - *False positives:* ND (adultery and bigamy), and the HI and MN definitions.

## Verdict

**The casserole has a family tree.** Arbitrary features of US consent law travel in bundles that trace to
identifiable sources (New York, Michigan, the MPC, the agreement statutes). The bundles show up both with
the codebook (Tests 1 and 2) and without it (shared rare text). Both pre-registered refutation criteria
failed. **Stigmergic lineage in state consent law: `[SUPPORTED]`.** The policy-diffusion literature
predicts this, and finds bill-to-bill text reuse at scale (Burgess et al., KDD 2016; Linder et al., PSJ 2018).
So the finding is a replication in this domain, not a discovery.

The part that bears on the ledger (protocol conduct move 5, attribution to victim) is thinner. A
burden-shifting variant can persist inside a family while other branches drop it (WA's "overcomes
resistance"). And a resistance duty can travel in paraphrase (DE/NE). Both are **instances, not a pattern**
`[HYPOTHESIS]`.

## Boundary

What this establishes:
- in 35 jurisdictions, arbitrary statutory features cluster by source family well beyond chance, under
  every robustness cut tried and in a codebook-free check;
- Michigan's text recurs in four other states;
- named residual resistance and marital provisions exist as quoted.

What it does NOT establish:
- **who copied whom, or when** (no adoption dates);
- that the families are the true sources rather than intermediaries;
- that the 16 missing jurisdictions follow the same structure (the Deep South and two core
  agreement-family states are missing);
- that any legislature acted in bad faith;
- that argument forms in everyday speech travel the same way. This is statute text. The everyday
  argument-form test (e.g. on the *Something Was Wrong* corpus) is still to be run.

Single provisions are instances; pattern is the proof.

## Next tests with power
1. Adoption years from session laws for the MI and NY markers, to test direction and timing.
2. Hand or browser collection of the 16 missing states, above all AL, GA, MS, TN, LA (the common-law family)
   and IL, WI, NJ (the agreement family).
3. A paraphrase codebook for burden-shifting constructions (residual resistance, "genuine and real",
   "ordinary resolution"), coded blind by a second coder, to turn the Test 3 instances into a count.

---

## Deviation 3 (operator direction: use the browser), fixed before the new texts were collected

The 35-jurisdiction results above stand as reported. This extension collects the missing jurisdictions with
the container's headless Chromium (Playwright). The same network proxy applies: CT, IL, NH and WI official
sites still fail at the network edge, and Justia still shows a bot check. **FindLaw codes** (codes.findlaw.com)
render in the browser, so FindLaw is the recorded mirror for the missing states. Its pages carry a
"Current as of" date, which is recorded per section. FindLaw warns that its codes may lag the official text.

**Sections taken (offense sections plus definitions and consent provisions, as for the original 35):**
AL 13A-6-60, -61, -62, -66, -67, -70 · AR 5-14-101, -103, -124, -125 · CT 53a-65, -70, -70a, -71, -72a,
-73a · GA 16-6-1, -2, -22.1, -22.2 · IL 720 ILCS 5/11-0.1, 11-1.20, 11-1.30, 11-1.50, 11-1.60, 11-1.70 ·
IN 35-42-4-1, -8 · KY 510.010, .020, .040, .050, .060, .070, .110, .130 · LA 14:41, 14:42, 14:42.1, 14:43
· MS 97-3-65, -95, -97 · NJ 2C:14-1, -2, -3 · NM 30-9-10, -11, -12, -13 · PA 18 §§3101, 3107, 3121,
3124.1, 3125, 3126 · TN 39-13-501, -502, -503, -505 · WI 940.225. NH (632-A:1–4) and OK (21 §§1111, 1111.1,
1114) only if a FindLaw page is found, otherwise missing.

**Text handling.** Only the statute body is kept: from "Updated by FindLaw Staff" up to FindLaw's closing
notice. **Analysis.** Unchanged and rerun on all jurisdictions collected. Results are reported for both the
original 35 and the extended set.

---

## Extended results: 49 of 51 jurisdictions (2026-11-12, after Deviation 3)

Collected with headless Chromium from FindLaw: AL, AR, CT, GA, IL, IN, KY, LA, MS, NJ, NM, PA, TN, WI. The
"current as of" dates run from January 2023 (LA) to January 2026 (IN, PA); see `SOURCES.tsv`. AL 13A-6-70
(lack of consent) is not on FindLaw: the URL returns a landing page, which was dropped. **Still missing:
NH, OK** (no FindLaw page found; official sites unreachable). Because FindLaw can lag the official text, any
amendment after a page's date is not reflected.

| Test | 35 jurisdictions | 49 jurisdictions |
|---|---|---|
| 1. Family markers travel together (φ within − between) | 0.32, p = 0.0001 | **0.31, p = 0.0001** |
| — by family: NY / MI / AFF / MPC / FED | 0.54 / 0.37 / 0.27 / 0.22 / −0.01 | 0.38 / 0.29 / **0.33** / 0.22 / 0.00 |
| 1-robust: range across all cuts | 0.27–0.37 | 0.27–0.36, all p ≈ 0.0002 |
| 2. States alike beyond chance | z = 3.7 | **z = 4.4**, p = 0.0001 |
| Codebook-free rare text, same family vs other pairs | 8.1 vs 3.0, p = 0.007 | 4.8 vs 2.3, p = 0.010 |

**Both pre-registered criteria still fail to refute. The result strengthens with the added states.**
Adding IL and WI, the core of the agreement family, raised that family's internal association from 0.27 to
0.33. The common-law family still has only one usable marker ("carnal knowledge" survives only in GA).

**New lineages the codebook-free check found (not in the pre-set families):**
- IL–NY 97 shared runs: custodial and care-facility offenses ("who provides direct care services… or
  direct supervision of the residents"; "detained or otherwise in the custody of a police officer"). A
  newer wave of reform travelling the same way.
- CT–MN 47: a psychotherapist module ("therapeutic deception means a representation by a psychotherapist
  that sexual contact… is consistent with or part of the patient's treatment").
- CA–IL 64: fraud as to professional purpose ("was not aware, knowing, perceiving, or cognizant of the
  essential characteristics of the act due to the perpetrator's fraudulent representation…").
- KY–NY 71 and MI–TN 59 fit the pre-set New York and Michigan families.

All were checked by reading the shared runs; none is mirror boilerplate.

**Test 3 additions (hand reading).**
- *Resistance expressly not required:* AL ("forcible compulsion does not require proof of resistance"),
  KY, IL ("lack of verbal or physical resistance… shall not constitute consent"), NM, PA (§3107).
- *A burden-shifting construction with a lineage:* **"prevent resistance by a [person / victim] of
  [ordinary / reasonable] resolution"**, found in OH, PA and WY. It descends from the 1962 MPC's "woman of
  ordinary resolution" standard, which reform critics singled out as a resistance requirement in
  disguise (Fischel, Harvard J. Law & Gender, 2025) `[SUPPORTED]`. Three states carry it in paraphrase
  (the gender neutralised, "ordinary" turned to "reasonable" in PA). **This is the first Test 3 finding
  that is a lineage rather than an instance: one burden-shifting form, one documented source, three
  descendants.**
- LA 14:42.1 keeps resistance at the centre of second-degree rape: "prevented from resisting… where the
  victim reasonably believes that such resistance would not prevent the rape".
- *Marital:* GA ("the wife of the defendant shall not be a defense"; rape is still defined as "carnal
  knowledge" of "a female"); WI ("Marriage not a bar to prosecution"); MS (anti-exemption in one
  subsection). Spouse carve-outs within particular offenses remain in AR, IL, KY, NM, PA (custodial or
  age-based).

**Verdict, updated.** Stigmergic lineage in US consent law: `[SUPPORTED]` on 49 of 51 jurisdictions.
Burden-shifting forms persisting by lineage: one documented lineage (the "ordinary resolution" standard,
3 states) plus instances (WA "overcomes resistance"; DE/NE "need only resist… to make refusal known"; LA).
Upgraded from instances only to **one lineage plus instances** `[SUPPORTED]` for the lineage. Still not a
pattern across families.

**Boundary unchanged** except the coverage: still no adoption dates, so no direction; FindLaw currency
caveat; NH and OK missing.

---

## Adoption-year test (direction), design fixed 2026-11-12 before any year was collected

**Question.** Did the Michigan- and New York-family markers start in Michigan and New York and spread
outward? Or did they appear elsewhere first, which would make the family labels wrong?

**Scope.** Every jurisdiction carrying a Michigan marker ("criminal sexual conduct", "personal injury",
"force or coercion"; "however slight" included as a check) or a New York marker ("lack of consent results
from", "forcible compulsion", "physically helpless", "mentally disabled/defective", "mentally
incapacitated"), in the 49-jurisdiction set.

**Year measured.** The **enactment year of the section that now carries the marker**, read from the
session-law history note attached to that section (in the collected text, or on the official site where
the collected text lacks one). Where a history note shows the marker arriving by a later amendment, and
the amendment text confirms it, that year is used instead. Otherwise the year is recorded as **"section
year"**: the marker was present by that year *if* it was in the original enactment, which the note alone
does not prove. A year from a secondary source (case law, a law-review survey) is labelled as such. No
year is guessed. A missing year is reported as missing.

**Prediction (source-and-spread).**
- MI markers: Michigan's year (1974 Act 266 by the coder's background knowledge, to be confirmed from
  the note) is the earliest among carriers.
- NY markers: New York's year (Penal Law of 1965, by background knowledge, to be confirmed) is the
  earliest among carriers, MPC 1962 excepted.

**Refuted for a family if** any other carrier's confirmed year for that family's distinctive markers
precedes the putative source's year. "However slight" is expected to fail as a Michigan marker, because
the phrase is older common-law language. If it fails, that marker leaves the Michigan family.

### Adoption-year results (2026-11-12)

Table: `results/adoption_years.csv`; raw extraction: `results/adoption_years_raw.json`, `tools/years.py`.
Every year is a **section year**: the enactment year of the section that now carries the marker, from its
history note. No amendment text was read, so none of these proves the marker was in the original enactment.
Three automatic readings were corrected by hand (MT "1947" was the code name R.C.M. 1947, so 1973; HI 1981
came from an annotation, so 1972; WY 2019 belonged to a neighbouring section, so WY is undated).

**Michigan family** (criminal sexual conduct; force or coercion; personal injury): **MI 1974** → MN 1975 →
NE 1977, SC 1977 → NC 1979, RI 1979. **FL 1974** ties MI at section level for "personal injury" only, and
whether the marker was in Florida's 1974 text is unconfirmed. Undated: DE, TN, NJ, NM. **No dated carrier
precedes Michigan. Prediction not refuted.** `[SUPPORTED]`
- Michigan's 1974 act is independently confirmed by a 1975 Nevada Legislative Counsel Bureau background
  paper: "Michigan in 1974 enacted what many persons hail as a model rape law… Criminal sexual conduct is
  defined by degree".

**New York family** (lack of consent results from; forcible compulsion; physically helpless; mentally
defective/incapacitated): **NY 1965** → OR 1971 → HI 1972 → MT 1973 → FL, MI 1974 → MN, WA 1975 → AL, MO,
SC 1977 → IA, NC, RI 1979. Undated: AR, CO, CT, IN, KY, MD, MS, NJ, NM, PA, TN, WY. **No dated carrier
precedes New York. Prediction not refuted.** `[SUPPORTED]`
- The year is New York's enactment of the whole Penal Law (L.1965 c.1030). That each marker was in the
  1965 text is background knowledge, not read here `[HYPOTHESIS]`.
- Note the order: the NY-family terms reach Michigan's 1974 act. **The Michigan model itself carries New
  York-family incapacity language**, so the two families are not independent roots. Michigan grafted New
  York's incapacity terms onto its own degree-and-coercion structure. That is consistent with the
  MI-family states (MN, SC, NC, RI) also carrying the NY incapacity trio. `[SUPPORTED as to the order]`

**Check marker "however slight": fails as a Michigan marker, as predicted.** Four carriers' sections predate
1974: SD (SDC 1939), OR 1971, HI 1972, ID 1972. Under the design it leaves the Michigan family. Test 1
without it was already run (the "drop markers in >50% of states" cut): difference 0.33, p = 0.0002, so the
lineage result is unchanged.

**What this adds.** Direction is now partly established. Within the dated carriers, both families spread
outward in time from their putative source, over about 14 years (1965–1979), with no counter-example. The
Michigan wave is fast: MN within a year, then SC and NE in 1977.

**Boundary.**
- **Section years only.** A marker could have arrived by a later amendment. That would make spread later,
  not earlier, so it cannot by itself produce a counter-example. It could hide one only if a carrier's
  *predecessor* section (older than its current section) had the marker, and that was not checked.
- **Undated carriers** (4 Michigan, 12 New York) could still hold a counter-example.
- **Florida–Michigan order** within 1974 is unresolved.
- **Copying is not shown.** Temporal order is necessary for copying, not sufficient: a later state could
  have taken the term from an intermediary or a common source, such as a draft both states saw.

**Next.** Session-law text for the four undated Michigan carriers (DE, TN, NJ, NM) and for FL ch. 74-121.
That is where a counter-example would have to be.

### Adoption-year results, revised with relayed external research (2026-11-12)

*Source: a ChatGPT research run, relayed verbatim by the operator. Provenance: external model, citing
session laws and court opinions this container could not reach. Claude's own searches could neither
confirm nor contradict the signing dates or the Philadelphia route. Claims are entered as **relayed**,
and the pre-registered rule is applied to them as relayed.*

**Florida breaks the 1974 tie, against the prediction.** Ch. 74-121 already used "serious personal injury"
when signed on **May 31, 1974**. Michigan's PA 266 was signed **August 12, 1974**. Under the rule fixed in
advance (enactment years; "refuted for a family if any other carrier's confirmed year… precedes the
putative source's year"), **the Michigan-source prediction is refuted for "personal injury"**. The
relayed report adds that Michigan's bill (introduced February 28, 1974) already used the phrase, so the
direction of borrowing between the two is open. That fact does not change the verdict under the
design, which measures enactment. "Personal injury" leaves the Michigan family as a source-attributed
marker. Its status is now **"Michigan/Florida 1974, direction open"**.

**The other Michigan markers survive.** Relayed dates for the previously undated carriers are all later
than Michigan:
- NM: Laws 1975, ch. 109 ("force or coercion", "personal injury"); the NM Supreme Court names Michigan's
  act as an influence.
- TN: 1978 Pub. Acts ch. 937, May 11, 1978 (all three Michigan markers).
- NJ: P.L. 1978, ch. 95, Aug. 10, 1978 ("physical force or coercion", "severe personal injury").
- DE: 70 Del. Laws ch. 124, 1995 ("criminal sexual conduct" as an umbrella phrase, a literal hit only).

For "criminal sexual conduct" and "force or coercion": **no counter-example; prediction holds**
`[SUPPORTED, partly on relayed dates]`.

**A named intermediary.** The relayed report says the NJ Supreme Court traces New Jersey's statute to the
**1976 Philadelphia Center for Rape Concern model statute**, which drew on Michigan, New Mexico,
Minnesota and Wisconsin. This is the "common source or intermediary" the boundary warned about, and a
textbook stigmergic trace: a model statute deposited in the environment and taken up by a legislature
with no direct contact with Michigan. It weakens "NJ copied MI" and strengthens the lineage claim.
`[relayed; consistent with Claude's background recollection of State in Interest of M.T.S., 1992; not
verified here]`

**New York, upgraded.** The relayed report found a historical printing of §130.00 containing "forcible
compulsion" and all three incapacity terms, with a history note to L.1965 c.1030, effective September 1,
1967. The four NY markers move from `[HYPOTHESIS]` to `[SUPPORTED, relayed]`. WY: 1977 ch. 70 (Feb. 24,
1977) defines "physically helpless", after NY. "Lack of consent results from" is verified only in
Washington's 1974 draft (quoted in *State v. Lynch*); New York's original §130.05(2) wording is still open.

**Revised verdict.**
- New York family: spreads outward from 1965, no counter-example.
- Michigan family: holds for "criminal sexual conduct" and "force or coercion"; **refuted for "personal
  injury"** (Florida enacted first).
- At least one route ran through a model statute, not state to state.

**Next source.** Bienen, *Rape IV* (1980), which has a state-by-state chart, for the remaining undated New
York carriers.

### Adoption-year test, step 3: case-law bound for the remaining New York carriers (design fixed before running)

Bienen's *Rape IV* (1980) is not reachable from this container. It is a printed supplement with no
online copy found, NCJRS has not digitized *Rape III*, and the Cambridge and CORE copies of later surveys
are blocked. **Substitute measure:** for each remaining New York-family carrier (AR, CO, CT, IN, KY, MD,
MS, PA) and each New York marker it carries, the **earliest published opinion of that state's courts**
on CourtListener containing the exact phrase (HTML search, oldest first).
- This gives an upper bound: the term was in use in that state by that date. It is not an adoption year.
- **Counter-example rule** (unchanged in substance): a state is a counter-example only if its earliest
  hit is before L.1965 c.1030 (July 20, 1965) **and** reading the hit shows the state's own sex-offense
  statute using the term. Hits that quote New York law, or use the phrase outside a sex-offense statute
  (e.g. "mentally defective" in commitment law), do not count. Those hits are read, and the next hit is
  taken.
- Limits: CourtListener's coverage of old state opinions is incomplete. A missing early hit is weak
  evidence of absence.

### Step 3 results: case-law bound (2026-11-12)

*Bienen's* Rape IV *was not reached (see the design note above).* Raw results:
`results/courtlistener_any_context.json`, `results/courtlistener_sex_context.json`; scripts `tools/cl.py`,
`tools/cl_sex.py`.

**Pass 1, any context.** Pre-1966 hits exist for the generic terms in AR, CT, IN, KY, MD and MS. **All were
read, and none is a sex-offense statute.** They are ordinary English in wills, deeds, contracts, injury,
pension and workers' compensation cases ("mentally incapacitated to execute a will", 1910; "physically
helpless and constantly ill", 1917; "physically or mentally incapacitated from earning", 1918–1942). One MS
hit (*Horton v. State*, 1944, "mentally defective") showed no usable snippet; it does not appear in the
sex-offense-context pass. So none counts under the rule.

**Pass 2, restricted to opinions that also mention rape, sexual intercourse, sexual assault or sodomy.**
Earliest hit per state and term:

| State | Term | Earliest sex-context opinion |
|---|---|---|
| AR | forcible compulsion | 1968 (*Randle v. State*; context not readable, see below) |
| AR | physically helpless / mentally defective / mentally incapacitated | 1978 / 1977 / 1991 |
| CO | physically helpless | 1981 |
| CT | physically helpless / mentally incapacitated | 1978 / 1982 |
| IN | mentally disabled | 1979 |
| KY | forcible compulsion / physically helpless / lack of consent results from | 1977 / 1977 / 1993 |
| MD | physically helpless | 1979 |
| MS | mentally incapacitated / physically helpless | 1969 (*Wilson v. State*; context not readable) / 1983 |
| PA | forcible compulsion | 1978 |

**Verdict.** No remaining New York-family carrier shows the term in a sex-offense context before 1968, and
none before L.1965 c.1030. **No counter-example; the New York-source prediction holds for all carriers
checked** `[SUPPORTED, weak for these eight]`. The bound is weak: these are upper bounds from court
coverage, not enactment years. The two earliest (AR 1968, MS 1969) predate those states' own reform
codes as commonly dated, and their pages did not render here, so what the courts were quoting is
unknown. Both are after 1965, so neither can refute.

**Overall direction result.**
- **New York family:** spreads outward from 1965 with no counter-example across all carriers (dated by
  enactment, by relayed session laws, or bounded by case law).
- **Michigan family:** holds for "criminal sexual conduct" and "force or coercion"; refuted for "personal
  injury" (Florida enacted first, relayed).
- **At least one route ran through a model statute** (Philadelphia 1976, relayed).

Bienen's chart remains the right source to turn the eight case-law bounds into enactment years.

### Step 4: Bienen, *Rape IV* charts (1980), read for the eight case-law-bounded states (2026-11-12)

Source: "Charts," 6(3) *Women's Rights Law Reporter* 1–235 (1980), HeinOnline scan hosted on the author's
site, URL supplied by the operator (hash in `SOURCES.sha256`). The text layer is uncorrected OCR noise, so
the pages were rendered to images and read. Quotations are from the DERIVATION / HISTORY and STATUTORY
STRUCTURE rows. PDF page numbers are given.

| State | Bienen's history (quoted) | New York-family term by | Before NY 1965? |
|---|---|---|---|
| **AR** (p. 6) | "1967 changed force to forcible compulsion…; **1975 followed New York Penal Code and Model Penal Code**." The 1979 chart lists forcible compulsion, physically helpless, mentally defective, mentally incapacitated (§§ 41-1803 to -1809). | 1967 (forcible compulsion); 1975 (the rest) | No |
| **CO** (pp. 8–9) | "1971 enacted Model Penal Code definitions…; 1975 enacted rape reform legislation." The 1978 chart's summary does not mention "physically helpless". | after 1975, possibly after 1978 (earliest case 1981) | No |
| **CT** (p. 10) | "1969 repealed, **introduced new chapter on sex offenses based on Model Penal Code and New York Code**…; added rape 1st degree where by force or if female **physically helpless**." | 1969 | No |
| **IN** (p. 18) | "1975 rape evidence reform statute passed; new formulations of offenses 1977." The chart reads "so mentally disabled or deficient that consent cannot be given". | 1977 | No |
| **KY** (p. 21) | "in 1974 revised criminal code enacted"; present law a "Model Penal Code formulation". The chart reads "1st degree rape – sexual intercourse by **forcible compulsion**". | 1974 | No |
| **MD** (p. 24) | "1976 penalty statutes replaced by statute defining 2 degrees of rape and 4 degrees of sexual offenses." | 1976 | No |
| **MS** (p. 29) | Present law (1979): "**traditional formulation** of rape" (carnal knowledge only). | after 1979 (the 1969 case hit was not statutory) | No |
| **PA** (pp. 46–47) | "Model Penal Code rape statute passed 1972, eff. 1973; 1976 major amendments." The 1980 chart reads "by **forcible compulsion**, by threat of forcible compulsion that would prevent resistance by **person of reasonable resolution**." | 1972 | No |

**Verdict: the New York-family prediction holds for every carrier, now dated by enactment.** No state
carries a New York term before L.1965 c.1030. The earliest after New York are CT 1969 and AR 1967.
`[SUPPORTED]`

**Beyond chronology: two attributions to New York in a contemporary source.** Bienen states that
Connecticut's 1969 chapter was "based on Model Penal Code and New York Code" and that Arkansas's 1975 code
"followed New York Penal Code and Model Penal Code". These are statements of derivation, not only order.
With the New Jersey route through the Philadelphia model statute (relayed), three lineage links now rest on
a source that names the parent. `[SUPPORTED]`

**Side result for Test 3.** Pennsylvania's "prevent resistance by a person of reasonable resolution" is in
the 1980 chart, so the Model Penal Code "ordinary resolution" descendant was present in Pennsylvania by
1980 and dates from the 1972 Model Penal Code-type statute or its 1976 amendments.

**The direction test is complete.**
- **New York family:** no counter-example; two named derivations (CT, AR).
- **Michigan family:** holds for "criminal sexual conduct" and "force or coercion"; refuted for "personal
  injury" (Florida, relayed).
- **Still open:** New York's original 1965 wording of "lack of consent results from" (§130.05(2)).

### Step 5: New York's original §130.05 wording — searched, not found (2026-11-12)

**Not obtained.** No full text of §130.05 as enacted by L.1965 c.1030 was reachable from this container:
- CourtListener opinion pages return empty to direct fetch;
- Google Books' API was over a shared quota;
- the Internet Archive has no matching printing;
- HathiTrust's full-text search is behind a Cloudflare JavaScript check, which was not bypassed;
- web search returns only current and post-2006 texts.

**What the 1965–1977 New York case law (CourtListener search snippets) does establish:**
- **Subdivision structure by 1968–1972.**
  - *People v. Bullis* (App. Div., Oct. 31, 1968) quotes "section 130.05 (subd. 3, par. [a]) 'A person is
    deemed incapable…'".
  - *People v. Hayden* (1972) cites "§ 130.05, subd. 1" for lack of consent as an element of each degree of
    sexual abuse.
  - *People v. McEaddy* (N.Y. 1972) cites "§ 130.05, subd. 2, par. [a]" alongside the forcible-compulsion
    offense.
  - So by 1972, subdivision 2 was a lettered list whose paragraph (a) was forcible compulsion, matching the
    current "Lack of consent results from: (a) Forcible compulsion; (b) Incapacity to consent; …".
  - The exact lead-in words are **not confirmed** for 1965. `[SUPPORTED as to structure; HYPOTHESIS as to
    wording]`
- **Amendments since:**
  - a second 1965 chapter (c.1038) amended §130.05 before the 1967 effective date (search-result report;
    contents unread);
  - paragraph (d), "clearly expressed", was added by L.2000 c.1 §45 (secondary: court opinion and 2025 bill
    text).
- **Negative finding:** no New York opinion filed 1965–1977 contains "impliedly acquiesce", the wording of
  current paragraph (c). Paragraph (c)'s present wording may therefore be later than 1965, but absence from
  the case-law snippets is weak evidence.

**Effect on the lineage test:** none. Kentucky's "lack of consent results from" dates from its 1974 code
(Bienen), and the relayed Washington 1974 draft also has it. Both are after 1965 whichever way New York's
original wording reads.

**Where it can be read:** *Laws of New York 1965*, ch. 1030 §130.05 and ch. 1038 (session laws, likely full
view on HathiTrust), or McKinney's Penal Law pamphlet (1967), opened in an ordinary browser.

### Step 5, closed with relayed external research (2026-11-12)

*Source: a ChatGPT research run, relayed by the operator. It used HathiTrust page-level full-text search and
read the 1964 draft page, which this container cannot reach (Cloudflare check). The link targets did not
survive the paste. Entered as **relayed**.*

- **1964 study bill**, §135.05(2), p. 81: reads "Lack of consent results from" and lists forcible
  compulsion, incapacity to consent, and a third ground for specified sexual-abuse offences where the
  victim did not "expressly or impliedly acquiesce". *Read on the page.*
- **L.1965 c.1030, §130.05(2)**, printed p. 2391 (scan 589): exact-phrase hits for "lack of consent results
  from" and "the victim does not expressly or impliedly acquiesce in the actor's conduct". *Verified by
  search hit only; the full enacted page has not been transcribed.*
- **L.1965 c.1038, §130.05(1)**, p. 2684 (scan 882): added the exception for consensual sodomy to
  subdivision 1.

**Corrections to Step 5.**
- New York's wording dates to **1964 in draft and 1965 in law** `[SUPPORTED, relayed]`.
- Step 5's weak negative ("impliedly acquiesce" possibly later than 1965) is **wrong**. The acquiescence
  wording was in the 1965 enactment. Its absence from 1965–77 case-law snippets meant only that no court
  quoted it.
- The second 1965 chapter changed subdivision 1, not the "lack of consent results from" clause.

**New lineage link (relayed): New York → Montana.** Montana's annotated 1973 code names N.Y. Penal Law
§130.05 (1965) as the source of its own definition of "without consent", substantially reworked. That is a
parentage statement, not just order. Montana's dated marker in this test ("physically helpless", 1973) fits
it.

**Named derivations from New York now on record:**
- Connecticut 1969 (Bienen, read here);
- Arkansas 1975 (Bienen, read here);
- Montana 1973 (relayed annotation).

**Still open:** a verbatim transcription of the enacted §130.05 page (L.1965 p. 2391).
