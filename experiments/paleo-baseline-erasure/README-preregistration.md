# Paleo baseline-erasure re-analysis — pre-registration

*Operationalizes the measurability scope `docs/tier6-baseline-erasure-research-scope-2026-07-02.md` (Tier-6 sub-mechanism: **temporal emptiness-declaration / baseline erasure**). It converts the scope's **narrow, testable** claim — anthropogenic mycorrhizal-community simplification, forgotten by present baselines — into a pre-registered re-analysis of **already-published fungal sedaDNA cores**, no new fieldwork. Files: `config.yaml` (run + inclusion gates), `cores.yaml` (candidate core matrix to screen), `run_baseline_erasure.py` (unexecuted skeleton). Freeze and hash all three before any run; `run_baseline_erasure.py` records that hash in every output row. This is a data re-analysis, not primary data collection; nothing here has been executed.*

---

## The one line that governs the whole design

**This tests composition/richness, not network function.** No sedaDNA core recovers past mycorrhizal *topology or resource-transfer function*. A "yes" here means *the mycorrhizal community measurably simplified with human impact and current baselines forgot it* — it does **not** mean "the forest was a functional wood-wide web." Any analysis, figure, or abstract that lets the second read off the first is committing the exact over-reach the parent brief's C-1 control exists to police. The functional layer is held out of reach by category, on purpose, in every output.

---

## Why this run exists (and what it deliberately cannot do)

The parent brief filed baseline-erasure with a **conceded untestable far leg**. The scope showed the far leg is *untested, not untestable*, via paleoecology. This pre-registration makes the near-far bridge decidable and — critically — **pre-commits the refutation conditions**, so a null is as reportable as a hit. The design's whole spine is that "mycorrhizal decline with human impact" must survive:
1. a **taphonomic** control (a measured decline can be DNA preservation loss, not ecological loss),
2. a **climate-attribution** control (late-Holocene fungal turnover has climatic drivers), and
3. a **negative-guild** control (a fungal guild that should *not* track soil/land-use human impact must **not** show the anthropogenic breakpoint — if it does, the instrument, not the forest, is the finding).

Immovable to the last: if the human-impact signal appears everywhere including the negative control, the run indicts its own method, not the baseline.

## Data

Published lake/bog **fungal sedaDNA metabarcoding** cores (ITS or 18S/SSU) that **also** carry, *in the same core*, (a) a human-impact proxy — cerealia/anthropogenic pollen, macro/micro-charcoal, coprophilous "grazing" fungi (e.g. *Sporormiella*), or industrial markers (spheroidal carbonaceous particles, heavy-metal enrichment) — and (b) a dated age–depth model (¹⁴C / ²¹⁰Pb). Candidates to **screen** (not yet confirmed-eligible) are in `cores.yaml`; eligibility is decided by the `config.yaml` inclusion gates, logged per core.

## Response variables (pre-specified)

- **R1 — mycorrhizal richness:** number of mycorrhizal (ecto- + arbuscular) OTUs/ASVs per sample, rarefied to common read depth (taphonomic control, N-1).
- **R2 — ectomycorrhizal share:** ecto reads / total fungal reads (compositional; robust to absolute-abundance loss).
- **R3 — community composition:** ordination distance from the core's own pre-impact centroid.
- **Negative-control guild:** an aquatic/planktonic-parasite or saprotroph guild with no expected soil/land-use coupling (its breakpoint should **not** align with human impact).

## Primary estimand

**The alignment (in calibrated time, within age-model uncertainty) between the change-point in the mycorrhizal series (R1/R2/R3) and the change-point in the *in-core human-impact proxy*, tested against alignment with an independent *climate* proxy.** Not a raw trend, not a single-core story: the estimand is *coincidence-of-breakpoints*, meta-analyzed across cores.

## Pre-registered hypotheses (with pre-committed nulls)

- **H1 (anthropogenic breakpoint).** Across cores, the mycorrhizal change-point aligns with the in-core human-impact onset more closely than with climate-proxy breakpoints, at a rate above chance given age-model error. *Null:* no better-than-climate alignment → **MEASURABLE / REFUTED** for the near-far bridge.
- **H2 (direction = simplification).** Where H1 holds, the shift is a *decline* in R1 and/or R2 (simplification), not an increase or a neutral turnover. *Null:* shifts are directionless or enriching → bridge unsupported.
- **H3 (specificity / negative control).** The negative-guild series does **not** show the anthropogenic breakpoint. *Null:* it does → **instrument suspect**, run reports method failure, not a baseline finding.
- **H4 (the forgetting leg, N-5).** The reconstructed pre-impact mycorrhizal composition differs from the composition assumed in a present "reference/old-growth" baseline dataset for the same biome. *Null:* modern baseline already encodes the pre-impact state → no forgetting; the *mechanism's* second clause fails even if H1–H2 hold.
- **H5 (attribution honesty).** Effect sizes are reported with age-model and read-depth uncertainty propagated; any core where human-impact and climate proxies are themselves collinear is flagged and cannot support H1. *This is a discipline commitment, not an outcome.*

## Conversion criteria (declared before any result)

- **→ MEASURABLE / SUPPORTED:** H1 ∧ H2 ∧ H3-holds ∧ H4. The far leg graduates to "measured near-far bridge; functional layer still open."
- **→ MEASURABLE / REFUTED:** H1 null, or H2 directionless, or H4 null. Recorded as *tested-and-unsupported*, not quietly dropped.
- **→ INSTRUMENT FAILURE:** H3 null (negative control lights up). No baseline claim either way; method is the finding.
- **Functional layer:** stays out of reach in all four outcomes. Not a gap to close with more cores — a category boundary.

## Custody / provenance

Freeze `config.yaml` + `cores.yaml` + `run_baseline_erasure.py` (+ any `queries/`), hash the set, and bind that hash into every output row (Standing Protocol Track F discipline, mirroring the GDA prereg). Source datasets are cited by DOI/accession in `cores.yaml`; re-analysis outputs are released for contest. LOCATOR-VERIFIED until the frozen set is hashed and archived.

*Pre-registration v1, 2026-07-02, unexecuted. The success condition is a **decidable** near-far bridge with a meaningful null — not a hit. The functional-web layer staying honest-unknown is the design working, not failing.*
