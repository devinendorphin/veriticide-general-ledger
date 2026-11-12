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
