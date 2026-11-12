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
