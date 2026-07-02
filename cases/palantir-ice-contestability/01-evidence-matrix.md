# 01 — EVIDENCE MATRIX

*Component → move/element → item → source grade → status. Grades: **P1** = party/primary (federal
award record, congressional letter, court filing, company statement); **S1** = quality journalism;
**ADV** = advocacy (party-primary for its own claims, advocacy for characterization). Status: VERIFIED
(multi-source) · PARTIAL (single/contested) · OPEN.*

| # | Item | Establishes | Source grade | Status |
|---|---|---|---|---|
| 1 | `contract` | **P1 (USASpending API/JSON):** PIID **70CTD022FR0000170**, recipient **Palantir**, awarding **DHS/ICE**, "Investigative Case Management (ICM) O&M Support Services and Custom Enhancements," **total obligation $150,703,824.61**, POP 2022-09-26→2026-05-04 (potential 2027-09-26), Delivery Order. **ImmigrationOS** ($30M, Apr 2025) = reported enhancement under this vehicle; +$30M (Sep 2025) "voluntary return" (S1) | **P1** (JSON) | **VERIFIED** |
| 2 | `instrument-scope` | ImmigrationOS **fuses IRS tax, SSA, DMV, passport/visa, license-plate-reader** data; 3 functions (identify/apprehend prioritized removals; track self-deportations "near real-time"; deportation logistics); FALCON/ICM since 2013 | S1 (AIC, State of Surveillance, Axios) | **VERIFIED** (capabilities as reported) |
| 3 | `oversight` | Congressional demands for answers — **Menendez** letter; **Goldman/Wyden/Velázquez** letter — re: ICE use of Palantir tech for mass surveillance | **P1** (congressional letters) | **VERIFIED** |
| 4 | `contestability` | **ELITE** emits probabilistic "where a removable person likely lives" scores used to direct apprehension; an ICE agent ("J.B.") testified to its use; reporting notes the scores are **not well suited to satisfy the constitutional (warrant) standard** they're used for | S1 (Biometric Update, NPR) + court testimony | **VERIFIED** (warrant-standard point) |
| 4a | `contestability` (quote) | Reported agent line that the app "could say 100 percent, and it's wrong" | S1 (single outlet) | **PARTIAL** — not reconfirmed; do not lean on it |
| 5 | `harm` | ICE detained/removed **~2,840 U.S. citizens (2007–2015)**; databases "incomplete and full of errors," used to target "especially Latinos"; a **U.S. citizen wrongfully arrested/jailed by ICE is suing** (ACLU SoCal) | ADV + S1 + **P1** (court filing) | **VERIFIED** (pattern + named suit) |
| 6 | `counter-register` / `palantir-defense` | Palantir's defense (now **first-party, verbatim**): "we — as contractors ... should not be in a position to set policy on behalf of the US Government," and are "not an oversight authority entrusted with scrutinizing ... executive branch actors"; "long shared EFF's commitment to privacy, civil liberties"; tech "mitigating risks while enabling targeted outcomes" | **P1** (Palantir blog) + ADV (ACLU) | `palantir-defense` **LOCATOR-VERIFIED** (Medium uncapturable; verbatim quotes hashed in transcript); `counter-register` **VERIFIED** |
| N-1 | `medicaid-feed` | Report that an ICE-used Palantir tool **feeds on Medicaid data** | ADV/S1 (EFF) | **PARTIAL** — reported; not independently confirmed |
| N-2 | `per-case-error` | Per-case false-positive/error rate of the targeting outputs | — | **OPEN** — undisclosed; a step-one demand |

**Load-bearing conjunction (1 + 2 + 4):** a real, contracted, fused-data targeting instrument whose
**liberty-depriving outputs are uncontestable** and used beyond what they can bear. Remove the
contestability failure (item 4) and it's a normal IT contract; remove the instrument (1/2) and there's
nothing to charge. The conjunction is what `04` tests.
