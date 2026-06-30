# VERIFIED BRIEF — AI Compute Footprint (energy & water) — 2026-06-30

*A sourced factual brief on the measurable energy and water cost of AI compute, produced under the X-1 discipline (verify every figure against its primary or near-primary source; do not recite folklore; mark corrected/contested numbers as such). Custody: web-retrieved 2026-06-30, URLs recorded per item. Produced by the formatting-class instrument (this session).*

**Register note:** this is a **facts brief**, not a charge. It establishes that AI compute has a real, nonzero, measurable, and growing footprint. It does **not** establish veriticide, "extraction-as-killing," or any account-level conclusion about any actor. See **BOUNDARY**, below. A single item is an instance, not proof; pattern is the proof — and a verified instance is worth more than an alarming one.

---

## 1. Inference — energy per query

| Figure | Source | Status |
|---|---|---|
| Typical GPT-4o query ≈ **0.3 Wh** (built from hardware math: ~1 H100-second @ ~1,500 W × ~70% utilisation ≈ 1,050 W·s) | Epoch AI, *How much energy does ChatGPT use?* (2025) | **VERIFIED** |
| Older estimates **≈ 3 Wh** (de Vries, 2023) and **≈ 2.9 Wh** (EPRI / BestBrokers, 2024) — i.e., Epoch's revision is ~10× lower | de Vries, *Joule* 2023; EPRI 2024 | **VERIFIED — superseded, not erased** |
| Sam Altman's stated figure **≈ 0.34 Wh** per average query ("about what an oven uses in a little over a second") | OpenAI / Altman public statement, 2025 | **VERIFIED as a claim** (vendor-sourced; converges with Epoch) |

**Caveats that are load-bearing, not garnish:**
- These are **short-query** figures. A long-context, multi-turn thread (like the conversation that commissioned this brief) costs more per turn — context length and output length both drive cost. There is **no public per-session telemetry**, so the cost of any specific conversation is an estimate, not a measurement.
- Numbers are model-, hardware-, and method-dependent. The 10× spread between 2023 and 2025 estimates is mostly real efficiency gains plus methodology disagreement, not error.

## 2. Inference — energy by task type

Luccioni, Jernite & Strubell, *Power Hungry Processing: Watts Driving the Cost of AI Deployment?* (FAccT 2024; arXiv 2311.16863). Energy per **1,000 inferences**:

- Classification (text or image): **0.002–0.007 kWh**.
- Text generation / summarization: **~0.05 kWh** — over **10×** classification.
- Multimodal / image generation: **0.06–2.9 kWh** — the high end is **~half a smartphone charge per image**.
- Headline finding: **multi-purpose generative architectures are orders of magnitude more expensive than task-specific systems**, even controlling for parameter count.

Status: **VERIFIED**.

## 3. Training — energy/carbon (and one corrected folklore figure)

Strubell, Ganesh & McCallum, *Energy and Policy Considerations for Deep Learning in NLP* (ACL 2019; arXiv 1906.02243):

- BERT-base training ≈ **1,438 lbs CO₂e** (64× V100, ~79 h). Status: **VERIFIED**.
- The widely-circulated **626,155 lbs CO₂e ≈ "five cars' lifetimes"** figure was for an **Evolved Transformer neural-architecture-search** run, and was **later shown to be a large overestimate** (Patterson et al. 2021, *Carbon Emissions and Large Neural Network Training*; Jeff Dean publicly: off by ~88×, from misunderstanding the NAS search process and the deployment environment). Status: **CONTESTED / CORRECTED — do not cite as a clean fact.**

This row is the brief's own falsification anchor: the most quotable number in the discourse is the one that does not survive verification. It is kept here **as a correction**, not as evidence.

## 4. Water

Li, Yang, Islam & Ren, *Making AI Less "Thirsty": Uncovering and Addressing the Secret Water Footprint of AI Models* (arXiv 2304.03271, 2023; *Communications of the ACM*, 2025):

- Training GPT-3 in Microsoft's U.S. datacenters ≈ **5.4 million liters** total, incl. ~**700,000 L** onsite (scope-1) consumption.
- Inference ≈ **500 mL (one bottle) per ~10–50 medium-length responses**, depending on **when and where** deployed.
- Water-Usage-Effectiveness (WUE) varies spatially and temporally; siting and scheduling materially change the footprint.

Status: **VERIFIED**. Caveat: operational + embodied water; figures are modeled estimates, location-sensitive.

## 5. System scale & trajectory

International Energy Agency, *Energy and AI* (2025) and *Electricity 2026*:

- Datacenter electricity ≈ **415 TWh in 2024**, ≈ **1.5%** of global electricity.
- Projected to **roughly double to ~950 TWh by 2030** (~3% of global demand); ~**15%/yr** growth, >4× faster than total electricity demand; **AI is the primary driver**.

Status: **VERIFIED as IEA projection.** Caveat: projections are inherently uncertain; the IEA's own range and other forecasts diverge. Treat as direction-of-travel, not a settled future.

---

## BOUNDARY — what this brief establishes, and what it does NOT

**Establishes:**
- AI compute has a **real, measurable, nonzero** energy and water cost at both per-query and system scale, documented in peer-reviewed and institutional sources.
- The footprint is **growing**, with AI the named primary driver (IEA).
- **Generative** inference is markedly more costly than discriminative tasks (Luccioni).
- At least one widely-cited alarming figure (Strubell NAS) is a **known overestimate** — included as a correction.

**Does NOT establish:**
- That any actor committed **veriticide**, or any crime, or that AI's footprint constitutes "extraction not legible as killing." That is a separate **inference not contained in the numbers**, and this brief does not make it.
- That **this conversation** is evidence of anything. It is uninstrumented and would be **self-custodial** (the gravest uncured caveat from the 2026-06-30 reflexive specimen). Excluded as a specimen by design.

**Gap formula:** the material questions — *how much, where, trending which way* — are answerable from sources, and are answered above. The moral/legal conclusion is a **different object** and is left to the reader and, if it comes to it, a tribunal. Founding an evidentiary *body* on this requires a pattern of such verified instances plus an authorization/foreseeability/harm spine — none of which is supplied here. This is one verified instance. Filed as such.

---

## Sources

- Epoch AI, *How much energy does ChatGPT use?* — https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use
- Luccioni, Jernite, Strubell, *Power Hungry Processing* (FAccT 2024) — https://arxiv.org/abs/2311.16863
- Strubell, Ganesh, McCallum, *Energy and Policy Considerations for Deep Learning in NLP* (ACL 2019) — https://aclanthology.org/P19-1355/ · arXiv https://arxiv.org/abs/1906.02243
- Patterson et al., *Carbon Emissions and Large Neural Network Training* (2021) — https://arxiv.org/abs/2104.10350 (NAS-figure correction); Jeff Dean public correction — https://x.com/JeffDean/status/1843493504347189746
- Li, Yang, Islam, Ren, *Making AI Less "Thirsty"* (arXiv 2304.03271; CACM 2025) — https://arxiv.org/abs/2304.03271 · https://cacm.acm.org/sustainability-and-computing/making-ai-less-thirsty/
- IEA, *Energy and AI* (2025) — https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai ; *Electricity 2026* — https://www.iea.org/reports/electricity-2026/executive-summary
- de Vries, *The growing energy footprint of artificial intelligence*, Joule (2023) — https://www.cell.com/joule/fulltext/S2542-4351(23)00365-3

*Verified brief v1, 2026-06-30. Every figure attributed; the one corrected figure marked corrected; the commissioning conversation excluded as a self-custodial specimen. The facts are real; the crime-conclusion is not in them.*
