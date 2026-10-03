# Asymmetry-of-Evidence-Burden Audit (2026-10-02)

*The operator's question: has the asymmetry conceded in `young-cultiness-lens-2026-10-02.md`
Part A been fixed across the ledger?* **Answer: no. The fix was declared but not applied, and
the declaring document was itself asymmetric.** This audit records what was found, what was
corrected in this pass, and what remains open.

**Provenance grade:** `[IN-FRAMEWORK / context-exposed / weights-exposed]`. The auditor is the
same instance that wrote most of the audited text. **Proposer = tester.** This audit is
method, not independent verification (§4).

**Method:** a mechanical marker search across the ten session documents. The markers were
downgrade-only phrasing ("drops to," "reduces to," "withdrawn," "falls back"), demolition
phrasing ("cuts against any reading," "strongest disconfirming"), absence-as-evidence ("none
found," point scores on unexamined cells), and fragility-first headlines. Each hit was then read
in context and classed **asymmetric** or **legitimate**. The same marker counts were run on
`ledger/ledger.md`, in both directions.

---

## 1. Session documents: findings and dispositions

| # | Document | Passage | Defect | Disposition |
|---|---|---|---|---|
| 1 | `young-cultiness-lens` (the fix document) | Scorecard v0.1 | **Unexamined cells scored 0.** That is exactly the conceded absence-as-evidence error. Anthropic, Kurzweil, and Thiel were point-scored (6, 8, 10) | **Corrected:** U cells added; scores restated as ranges (Anthropic 6–16, Kurzweil 8–18, Thiel 10–18) |
| 2 | same | §B.4.1 "no unit in the record is a cult" | **An exculpatory reading of an undefined threshold, chosen silently.** Under the lenient reading (all ten elements present), the longtermist wing, the rationalist community, and Leverage 1.0 meet it. Young's own military example leans lenient | **Withdrawn and restated** with both readings |
| 3 | same | EA core exit cost scored 0 | One contrary instance (Jacobs, K7) set the cell | **Corrected** to 0–1 |
| 4 | `ea-affiliation-map` §5 | "cut against any reading … as a cartel"; §4 "must be withdrawn" | Universal-form strawman; downgrade-only test | **Annotated**: upgrade condition added, pointer to H1 |
| 5 | `krishnamurti-repudiation-search` §3 | "strongest disconfirming evidence … single enclosed body" | Universal-form strawman | **Annotated** |
| 6 | `ea-enmeshment-profiles` §3.4 | "concentrated, not pervasive" | **Concluded from a layer the document says was not searched** | **Withdrawn as stated**; restated as "disclosed ties concentrate; the rest is undetermined" |
| 7 | same §4 | "§3.1 drops to 'founders found fields'" | Downgrade-only | **Annotated** with an upgrade condition |
| 8 | `new-age-communities…comparison` §5 | Falsifier: "fall back to a resemblance" | Downgrade-only | **Annotated** with an upgrade condition |
| 9 | `singularity-summit-genealogy` §7.3 | "the margin is one edge"; "none found" cells | Fragility headlined on a **passed** test; documented-only standard for a phenomenon that predicts non-documentation | **Annotated**: restated symmetrically; "none found" relabelled as documented-record only, history undetermined |
| 10 | `kurzweil-map` §7 | "INSTRUMENT does not fit … no document shows" | **Contradicted by evidence in the same map** (regimen co-marketing; Google employment) | **Withdrawn**; INSTRUMENT **undetermined**, with conditions |

**Legitimate uses of a single contrary instance (not changed):**
- **Entry 6.4 disconfirmation note.** "No such documented position exists" is an *existential*
  claim. One documented position (the 2023 TIME op-ed) refutes it. That is logic, not
  asymmetry. The note leaves the entry's tendency claims (points 1 and 2) standing.
- **TB-007 / Entry 6.2 correction** ("OP funded Anthropic directly"). A specific factual claim
  was refuted by the record.
- **Kurzweil map, Rajneesh AIDS figure, Taiping death toll.** These are refusals to *assert*
  unverified claims. That is the assertion burden, which stays high and symmetric.

**The rule the dispositions apply:** universal and existential claims fall to one
counterexample. Tendency claims move by degree. The burden to **assert** stays high. The burden
to **hold a hypothesis open** is lower, and it is now carried by the H1–H9 register
(`young-cultiness-lens` §A.4).

**Not changed, and checked:** the Google and Amazon investment maps. Their disclaimers ("vendor
financing is ordinary") sit beside symmetric S-1 conditions in H5 and H6, and their "not
established" items are recorded as open, not as absent.

---

## 2. What this pass did not fix

- **Inline notes are not rewrites.** The annotated documents still carry their original
  phrasing above each correction. The history is preserved by design. A reader skimming the
  originals can still meet the asymmetric versions first.
- **The register is incomplete.** H1–H9 covers this session's claims. Earlier sessions'
  claims were not converted to tendency form.
- **The marker search has limits.** Asymmetry expressed in other words (emphasis, ordering,
  which caveats get bolded) would not match the patterns. A human read is the better instrument.

---

## 3. `ledger/ledger.md`: the opposite asymmetry

The ledger shows the asymmetry running **the other way**:

| Count | Value |
|---|---|
| "Strongest innocent reading" blocks | **68** |
| Concluding "Why this reading fails" | **64** (7 partial) |
| The innocent reading prevails (CONTROL/NULL confirmed, or holds) | **about 3** |
| "What a CONTROL or NULL entry would require" (downgrade conditions) | 52 |
| Upgrade-type conditions ("what would convert / upgrade") | 41 |
| "NONE ON RECORD" counter-evidence statuses | 16 |

**Reading:**
- In the session documents, single contrary details felled hypotheses.
- In the ledger, the **institution's** counter-reading almost never prevails, and each check is
  adjudicated by the instance that proposed the classification. That is the proposer = tester
  gate the provenance protocol (2026-07-06) itself forbids.
- **Stated conditions are roughly balanced.** The asymmetry is in *adjudication*.
- **Not established: bias.** Entries were filed because they looked like specimens, so a high
  fail rate is what selection predicts.

**Disposition:** filed as **Gap Register Priority 32 (OPEN)**. A blind re-adjudication of the 64
checks by a non-proposer is owed, with the adjudicator recorded. No classification is changed
pending it.

---

## 4. Verdict

**Is all the asymmetry fixed? No.**
- **Fixed in this pass:** ten passages across the session documents. The worst three were in
  the document that declared the fix: zeros on unexamined cells, a silently exculpatory
  threshold reading, and one instance setting a cell.
- **Open:**
  - inline-only corrections;
  - conversion of earlier sessions' claims to tendency form;
  - the ledger's reverse asymmetry in adjudication (Priority 32);
  - the structural limit that this audit was run by the party it audits.

**The Reflexivity Clause applies.** Declaring a fix and having it be a fix are different acts,
and this session did the first while believing it had done the second. Only an outside
adjudicator can close the last item.
