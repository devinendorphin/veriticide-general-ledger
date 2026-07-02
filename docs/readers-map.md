# READER'S MAP — where to start

*One page. Find your role, follow the path. This is **navigation only**; the substance is in the
files it points to. It adds no new claim.*

## Two-minute orientation

- The **product** is the case files (`cases/`). Each is a narrowed dossier that asserts **step one**
  of the Standing Protocol — a basis to demand preservation, disclosure, audit, inquiry, reporting —
  and **never step two** (a finding of guilt, which is for a tribunal).
- The **spine** is the Convention, Articles II (definition/elements) and IV (pattern evidence):
  `docs/convention-on-veriticide-v0.2.md`. Everything else cites into it.
- The **hot register** — the uncaptured statement of the whole — is the Declaration:
  `docs/declaration-on-veriticide-v0.1.md`.
- Every evidentiary claim carries a **custody state**
  (`LOCATOR-VERIFIED` → `HASHED-PENDING-BACKUP` → `VERIFIED`, strongest last). The governing record
  is each case's `evidence/custody-index.md`; the corpus status is `docs/custody-status-2026-07-02.md`.

## If you are a journalist

1. Start with a **Band-1** case: `cases/doge-usaid-pepfar/`, `cases/election-redistricting/`, or
   `cases/xai-boxtown-turbines/`.
2. Read its `00-charge-theory.md` (one page), then `01-evidence-matrix.md` and `02-source-bundle.md`.
3. **Verify before you cite:** `evidence/custody-index.md` + `evidence/custody-receipt.md` give the
   per-item sha256 and Internet-Archive URLs. Cite only what an item's custody state supports — a
   `LOCATOR-VERIFIED` item is a locator, not a held original.
4. Read `03-adversarial-check.md` (the story's own strongest rebuttals) before publishing.
> The one thing to know: these are step-one documentation packets, not verdicts.

## If you are a lawyer / legal reader

1. The definitional core: Convention **Art. II** (elements) and **Art. IV** (pattern) —
   `docs/convention-on-veriticide-v0.2.md`. The tier taxonomy's *evidence-mode* axis
   (`docs/veriticide-stack-tier-taxonomy-v0.1.md`) states how each tier is proven.
2. Standing + forum: the **Documentation & Standing Protocol**
   (`docs/documentation-standing-protocol-v0.1.md`) — the two-step doctrine and **§7-bis Forum-Now**
   (soft vehicles live; hard vehicles dormant behind stated preconditions). Every case's
   `00-charge-theory.md` now carries its own Forum-Now block naming venues and preconditions-to-flip.
3. Per case: `00-charge-theory` → `03-adversarial-check` (defenses) → `04-falsification-memo` →
   `05-custody-manifest` (chain of custody).
4. The **Reflexivity Clause** (Convention Art. IV-bis) is the wall that keeps the framework from
   becoming a Kafka trap; the **asymmetry test** is its discriminator.
> The one thing to know: no case asserts guilt; each names where its record is actionable *today* and
> the preconditions to escalate.

## If you are a community documenter / organizer

1. Read the Protocol **Quick Start** (`docs/documentation-standing-protocol-v0.1.md` §8): six fields,
   start today, no permission required.
2. Keep originals off-platform with capture dates — see a case's `evidence/CAPTURE-RUNBOOK.md` and
   `capture.sh`; more than one custodian where you can.
3. Keep facts and analysis in **separate files**; protect yourself and sources by role, not name.
4. Your live options are the **ACTIVE-soft** vehicles in any case's Forum-Now block: preservation
   demands, FOIA/records requests, IG complaints, public-comment dockets, journalism-with-custody.
> The one thing to know: the record's value begins the moment the first dated output is preserved.

## If you are a researcher / model evaluator

- Tiers 1–2 are **measurable**. Start with `experiments/topic-bearing-gda/` (constraint friction,
  neutral-authority laundering — pre-registered) and the tier taxonomy's evidence-mode axis.
- For the **apex tiers (5–6)**, start with `docs/apex-tiers-5-6-evidentiary-index-2026-07-02.md` — the
  one-page front door that gathers Tier 5's body (AI-energy briefs + Boxtown case) and the new Tier-6
  brief (`docs/tier6-worldcide-evidentiary-brief-2026-07-02.md`), and forwards each body's own
  falsification verdict. Both apex bodies came back **bounded** from their own controls; that is the point.

## If you are a skeptic / adversary

- Start with any case's `03-adversarial-check.md` and `04-falsification-memo.md` — the framework's own
  attempts to break itself — plus the Reflexivity Clause and the external reviews
  (`docs/external-review-*`). The **asymmetry test** asks where the machinery points: at the claim's
  *content* (possible truth-under-siege) or at the speaker's *standing* (the tell).

## Repo legend

| Path | What it is |
|---|---|
| `cases/<case>/` | the dossiers — `00`-charge-theory … `06`-timeline, plus `evidence/` |
| `ledger/ledger.md` | the source-of-record archive ("the cathedral" the case files are cut from) |
| `docs/` | Declaration (hot) · Convention (spine) · Protocol + tier taxonomy (working) · custody status · external reviews |
| `scraper/`, `experiments/` | capture tooling and the Tier-1/2 assay |
