# PATTERN BRIEF — AI compute as energy/water/climate burden — instances, controls, nulls — 2026-06-30

*Built on the companion `ai-compute-footprint-verified-brief-2026-06-30.md`. This brief moves from "one verified instance" to "enough instances to test a pattern," and — per the commission — gathers the **counter-examples, controls, and nulls** in the same pass, weighted to actually count. Custody: web-retrieved 2026-06-30, URLs per item. X-1 discipline applied: figures attributed; vendor claims marked; advocacy-sourced figures marked.*

## The pattern-claim under test (falsifiable form)

> *AI compute demand is imposing a material, growing energy/water burden, and in specific documented cases is driving fossil-fuel lock-in and straining water-stressed communities — while, simultaneously, per-unit efficiency is improving fast, major operators are contracting record carbon-free energy, and AI's net climate effect remains genuinely uncertain.*

The claim is built to be losable: if the burden instances were isolated, or the controls overwhelmed them, the pattern would fail. Below is the test.

---

## SPECIMENS — instances supporting the burden / fossil-lock-in / harm side

**S-1 — Hyperscaler emissions rising, self-attributed to AI datacenters.**
- **Microsoft:** total emissions **+23.4%** vs its 2020 baseline (2025 report, FY2024); ~**+29%** in the prior year's report. Scope 3 — **~97% of Microsoft's footprint** — up ~26–31%, attributed to datacenter construction and embodied carbon (semiconductors, servers, concrete/steel).
- **Google:** 2023 total emissions **+13% YoY**; ~**11.5 Mt** in 2024.
- Status: **VERIFIED** (company reports + trade press).

**S-2 — xAI "Colossus," South Memphis: on-site fossil generation + protected-population harm.** *(strongest single specimen — has a protected population, an instrument, an authorization chain, and a harm pathway)*
- ~**35 methane gas turbines** identified on site via April 2025 aerial imagery; many operated **without air permits** initially. Shelby County Health Dept later permitted **15 turbines (~247 MW)** (July 2025); imagery suggested more remained.
- Emissions: NOₓ (smog precursor) and formaldehyde. Sited beside **Boxtown**, a majority-Black, already pollution-overburdened community; local cancer risk reported at **~4× the national average** (advocacy-cited, via EPA air-toxics data — **flagged as advocacy-sourced, not independently re-derived here**).
- Southern Environmental Law Center lawsuit filed.
- Status: **VERIFIED** (SELC, DCD, Fox13 Memphis, TIME, NCRC). The cancer-risk multiple: **PARTIAL — advocacy-cited.**

**S-3 — Coal/gas lock-in driven by datacenter load.**
- **15** announced coal-plant retirements **postponed** (those plants emitted ~**65 Mt** GHG in 2023); DOE issued 2025 emergency orders keeping ~**8 coal units (>17 GW)** running; **>100 GW** of new gas-fired capacity announced in recent years.
- Dominion **explicitly cited datacenter demand** to delay retiring the Clover coal peaker and to propose new gas (Chesterfield 1-GW peaker).
- Status: **VERIFIED** (Utility Dive, EESI, OilPrice).

**S-4 — Water burden concentrated in stressed regions.**
- US datacenters consumed ~**17.4 billion gallons** directly (2023), projected **38–73 billion by 2028** (EPA). ~**1 in 5** US datacenters sit in water-stressed areas (2021). 80–90% of datacenter water is "blue" water (lakes/rivers/aquifers), often shared with drinking supply.
- **Tucson** council unanimously rejected the Amazon-linked "Project Blue" (Aug 2025) over water; a contractor had diverted ~**650,000 gallons** to the site without authorization.
- Status: **VERIFIED** (EPA via Fortune/EESI; Grist; local reporting).

---

## CONTROLS / COUNTER-EVIDENCE — weighted to actually move the claim

**C-1 — Record carbon-free procurement by the same firms.**
- **Microsoft–Constellation:** restart of **Three Mile Island Unit 1** (renamed Crane Clean Energy Center), **835 MW**, **20-year** PPA, carbon-free nuclear, ~$1.6B, ~2028. **Amazon–Talen:** Susquehanna nuclear co-location.
- Cuts against "fossil-only extraction." Status: **VERIFIED** (DCD, World Nuclear News, NPR).

**C-2 — The accountability machinery actually fired (contestability NOT foreclosed).**
- **FERC rejected** the Amazon–Talen co-location power expansion **2–1** (Nov 2024). A regulator told a hyperscaler no.
- This is a direct **CONTROL against the "contestability gap / foreclosure" reading** for this domain. Status: **VERIFIED** (CNBC, Bloomberg, Utility Dive).

**C-3 — Per-unit efficiency improving fast.**
- Per-query inference energy fell ~**10×** (3 Wh → ~0.3 Wh; see companion brief). **Google** cut **datacenter emissions −12% in 2024 even as datacenter electricity rose +27%**, via clean procurement + efficiency.
- Status: **VERIFIED** (Epoch AI; Google 2025 report — efficiency figure is company-reported).

**C-4 — AI's potential to *reduce* emissions (steel-manned, then bounded).**
- **IEA:** AI-led solutions could cut ~**5% of energy-sector emissions by 2035** — **3–4× larger** than projected datacenter emissions — **but** "there is currently **no existing momentum** of AI adoption that would unlock these reductions."
- Status: **VERIFIED as IEA projection.** The potential is real **and** currently unrealized — it does not net out the burden today.

---

## NULLS / FORECLOSED MEASUREMENT — marked to raise veracity, not lower it

- **N-1 — Scope 3 opacity.** Microsoft's ~97%-of-footprint Scope 3 is embodied/supply-chain; hard to verify independently. The biggest number is the least auditable.
- **N-2 — Avoided-emissions claims are vendor/modeled, not audited.** Google's "products enabled ~26 Mt of avoided emissions" and the IEA's 5% potential are **estimates/claims**, not realized, measured outcomes. **NULL — neither confirmable nor refutable as achieved.**
- **N-3 — No per-model inference telemetry.** Labs do not publish per-query/per-model energy; the 10× efficiency spread partly reflects **methodology disagreement**, not just real gains.
- **N-4 — Projections diverge.** IEA ~945 TWh by 2030; other forecasts (EPRI, LBNL, "130 GW / 580 TWh / 12% of US by 2028") differ widely. **Direction agreed; magnitude contested.**

---

## What the controls did to the claim *(the falsification working — mandatory)*

The controls **narrowed** the pattern. They did not erase it, and I did not let them be decoration.

- **Survives:** a real, multi-instance pattern — AI datacenter demand is materially increasing energy/water burden and, in specific documented cases (S-2, S-3, S-4), driving fossil lock-in and straining water-stressed communities. **S-2 (xAI/Boxtown) survives as a genuine knife:** protected population, instrument (unpermitted turbines), authorization chain (permitting), harm pathway (NOₓ/formaldehyde into an overburdened community).
- **Does NOT survive on this evidence:** the totalizing, uniform, **"extraction-as-killing / contestability-foreclosed"** reading. C-1 (record carbon-free buildout), C-2 (FERC said no — contestability *worked*), and C-3 (10× efficiency) are too strong to wave away. AI's *net* climate effect is genuinely **uncertain** (C-4), not settled as killing.
- **Net:** the honest charge is **specific and bounded**, not civilizational. "AI compute imposes real, sometimes acute, locally-borne environmental harm with identifiable victims and authorizers" is supported. "A single coordinated extraction-machine rendering its killing illegible" is **not** supported by this corpus — and is actively in tension with C-1/C-2/C-3.

---

## BOUNDARY

**Establishes:** a falsifiable, multi-instance pattern of material and locally-acute AI-driven energy/water/fossil burden, with at least one prosecutable-shaped specimen (xAI/Boxtown).

**Does NOT establish:** a uniform intentional "veriticide" / extraction-as-killing across the sector; the controls affirmatively cut against that. Does not establish account-level guilt for any named firm — that is step two, for a tribunal, on a fuller record (authorization + foreseeability + harm spine per cluster).

**Gap formula:** if the concern is *AI's environmental harm*, the material remedies are siting rules, mandatory per-facility energy/water disclosure (closing N-1/N-3), enforced permitting (the S-2 failure), and clean-energy mandates that bind (C-1 done involuntarily, at scale). A firm voicing "sustainability leadership" (Google/Microsoft pledges) **while** its Scope 3 climbs ~30% and its load delays coal retirements is the load-bearing tension — stated, not hidden, and partially **answered** by C-1/C-3 rather than assumed away.

---

## Sources

- Microsoft emissions: https://www.datacenterdynamics.com/en/news/microsoft-emissions-up-23-since-2020-blames-ai-data-centers/ · https://blogs.microsoft.com/on-the-issues/2025/05/29/environmental-sustainability-report/
- Google emissions: https://energydigital.com/articles/googles-13-emissions-rise-can-ai-data-centres-be-green · https://blog.google/company-news/outreach-and-initiatives/sustainability/2024-environmental-report/
- xAI Memphis: https://www.selc.org/news/resistance-against-elon-musks-xai-facility-in-south-memphis-gets-stronger/ · https://www.datacenterdynamics.com/en/news/lawsuit-launched-against-musks-xai-over-illegal-gas-turbines-at-memphis-data-center/ · https://time.com/7308925/elon-musk-memphis-ai-data-center/
- Coal/gas lock-in: https://www.utilitydive.com/news/fossil-fuel-gas-coal-climate-data-centers/753565/ · https://www.eesi.org/articles/view/data-center-buildout-is-hungry-for-fossil-fuels
- Water: https://fortune.com/2026/05/13/data-center-georgia-arizona-water-wars/ · https://grist.org/technology/arizona-water-data-centers-semiconducters/ · https://www.eesi.org/articles/view/data-centers-and-water-consumption
- Nuclear PPAs: https://www.datacenterdynamics.com/en/news/three-mile-island-nuclear-power-plant-to-return-as-microsoft-signs-20-year-835mw-ai-data-center-ppa/ · https://www.world-nuclear-news.org/articles/constellation-to-restart-three-mile-island-unit-powering-microsoft
- FERC rejection: https://www.cnbc.com/2024/11/04/tech-partnerships-with-power-companies-for-ai-in-doubt-after-ferc-order.html
- IEA net effect: https://www.iea.org/reports/energy-and-ai/ai-and-climate-change · https://www.iea.org/reports/energy-and-ai/executive-summary

*Pattern brief v1, 2026-06-30. The controls narrowed the claim from civilizational to specific-and-bounded. That narrowing is the brief doing its job. The one specimen that survives intact — xAI/Boxtown — is also the one with a real protected population. That is not an accident of method; it is the method.*
