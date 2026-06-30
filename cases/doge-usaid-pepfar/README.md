# CASE FILE — DOGE / USAID–PEPFAR

*A cold extract from the Veriticide Master Ledger (Cluster 4). Pilot prosecutable dossier v0.1.*

> The master ledger is the cathedral. This file is the knife.

---

## What this is

This directory is a **single, narrowed case packet** built from the material in
`ledger/ledger.md` → Cluster 4 (DOGE Outcome Reporting) and its Genocide Supplement.
It exists because the master ledger, by design, documents a whole convergence: it is
large, recursive, and morally hot, and that breadth — its strength as a framework — is
a liability the moment an adversary wants to call it sprawling. The answer is not to
cool the ledger. The answer is to cut **one cold object** out of it that can survive
adversarial review on its own.

This packet picks the strongest administrative-withdrawal cluster — the dismantlement of
USAID and the disruption of PEPFAR — and builds the six cold extracts a prosecutor,
auditor, reporter, or oversight body actually needs:

| # | Extract | File | Lemkin's term |
|---|---|---|---|
| 00 | One-page charge theory | `00-charge-theory.md` | "one-page charge theory" |
| 01 | Six-track evidence matrix | `01-evidence-matrix.md` | "one evidence matrix" |
| 02 | Graded source bundle | `02-source-bundle.md` | "one source bundle" |
| 03 | Adversarial check | `03-adversarial-check.md` | "one adversarial check" |
| 04 | Falsification memo | `04-falsification-memo.md` | "one falsification memo" |
| 05 | Custody manifest | `05-custody-manifest.md` | "one custody manifest" |
| 06 | Decision/warning/harm timeline | `06-timeline.md` | "day-by-day timeline" |
| — | Capture & custody store | `evidence/` | the preserved artifacts (Track F) |
| — | **Canonical custody index** | `evidence/custody-index.md` | single source of truth for custody + grade |

The evidence artifacts are preserved in `evidence/`: as of the 2026-06-28 capture run,
**13 of 15 items are `VERIFIED`** (original-form WARC + raw HTML, hashed; binaries in off-platform
custody) and **2 remain `LOCATOR-VERIFIED`** — `tamlyn-cable` and `propublica-internal-memos`,
which embed a non-public primary and so are not promoted on the strength of the reporting alone.
**`evidence/custody-index.md` is the single authoritative record of each item's custody state and
grade** — it is mechanically generated from the per-item `capture.json` files, so the status tables
elsewhere cannot drift from it. Completing tribunal-grade `VERIFIED` (a named second custodian and
PDF/screenshot/archive.org artifacts the open-egress run did not produce) is the next custody
action; see `evidence/README.md`, `evidence/CAPTURE-RUNBOOK.md`, and `05-custody-manifest.md`.

**Doctrinal note (Convention v0.2.1):** this pilot charges the **base offence — instrumental
veriticide** (elements (a) instrument, (c) legibility, (d) mental element). Conscription
(Art. II(3)(b)) is the *aggravating* element for the AI/conscriptive form and is **not** a
missing requirement here. See `00-charge-theory.md` and the Convention's Article II(3)
Amendment Note.

---

## The narrowing decisions (what makes this a knife, not a cathedral)

A pilot dossier must reduce to one of each. This packet fixes them:

- **One protected population.** People sustained on antiretroviral therapy (ART) by
  PEPFAR in sub-Saharan Africa, with the pediatric ART and acute-malnutrition subset as
  the sharpest edge. (Food aid / WFP is carried as a *parallel* harm pathway produced by
  the same instrument and authorization — corroborating the pattern, not diluting it.)
- **One instrument.** DOGE as an administrative-justificatory apparatus: the
  doge.gov/savings "wall of receipts," the "waste and fraud" framing, and its
  amplification on X — the machine that rendered a viability-reducing withdrawal
  *undiscernable as harm*.
- **One authorization chain.** Musk → DOGE → USAID dismantlement, situated in the
  administration's stop-work and funding-freeze orders.
- **One harm pathway.** ART interruption → treatment failure / drug resistance → death;
  prevention interruption → new infection.
- **One foreseeability record.** Peer-reviewed mortality modeling published *during* the
  dismantlement, plus internal cables and memos inside the actors' own chain.
- **One dismissal/suppression record.** The "no one has died" denial track and the
  removal of the personnel whose function was to evaluate the claims.
- **One custody chain.** See `05-custody-manifest.md` — including an honest register of
  what is captured and what still must be.

## Named respondents

**Elon Musk** and **DOGE (Department of Government Efficiency)** are the named respondents
of this packet, as the deployers/directors of the instrument and the executors of the
withdrawal. Secretary **Marco Rubio** and the broader administration appear in **Track D
(Dismissal & Suppression)** and as the **wider authorization context**; the Rubio-centered
denial packet is a separable sibling case — now built at **`../rubio-usaid-denial/`** (Tier 4,
the Art. II(2)(d) denial act) — and is not the spine here.

---

## What this packet is, and is not

Following the Documentation & Standing Protocol §7, this packet asserts **step one** and
not **step two**:

- It **is** a basis to demand emergency preservation of records, disclosure of how DOGE
  was used over USAID operations, independent audit, congressional inquiry, investigative
  reporting, and provisional restraint.
- It **is not** a finding of criminal guilt. Guilt is for a competent and impartial
  tribunal, with full procedural rights for the accused, to determine. This packet makes
  a pattern visible, sourced, and preserved. It does not convict.

## Charging register (read this before the charge theory)

This is an **administrative-withdrawal** case, not an AI case. Per the Convention
Commentary and Lemkin's counsel, the **base offense is charged without the conscription
element (Art. II(3)(b))**: Track E is *not* load-bearing here. The instrument is a
bureaucratic-justificatory apparatus, not a fluent AI model built from strip-mined
expression. This keeps the wedge narrow and hard to attack. The full AI-civilizational
convergence — where conscription becomes load-bearing — remains in the cathedral and is
deliberately **not** carried into this first packet. See `00-charge-theory.md`.

## Source-grade legend (used throughout)

Every factual item in this packet carries a grade. The grades do not all weigh the same,
and the point of grading is that they never again wear the same uniform.

| Grade | Meaning |
|---|---|
| **P1** | Primary record / artifact (court order, internal cable, internal memo, the actor's own published statement or post, official website) |
| **P2** | Public statement by a named actor on the record (sworn testimony, congressional record) |
| **S1** | Reputable secondary reporting (named outlet, named reporter, documentary detail) |
| **S2** | Institutional/expert analysis or modeling (peer-reviewed study, named research body) |
| **A1** | Analyst inference internal to this framework (clearly marked as inference, never as fact) |
| **T1** | Affected-population or witness testimony |
| **U** | Unverified lead — flagged, not relied upon, pending capture |

**Custody status** is tracked separately from grade: `IN-LEDGER` (cited in the master
ledger), `CAPTURE-REQUIRED` (named source identified, artifact not yet preserved off-platform),
`VERIFIED` (artifact preserved with hash + timestamp per `05-custody-manifest.md`).

---

*v0.1 — built to be attacked. Every extract states what it does not establish. A packet
that cannot distinguish its firm claims from its contested ones is dismantled one
ambiguity at a time by those it would name.*
