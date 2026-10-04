# Candidate entry: the Henning shooting and the public record (LASD, 2012–2015)

*Filed 2026-10-04 as a **candidate**. The ledger has no cluster for police use of force, so
where (or whether) this goes is the operator's call. It came out of coercive-harm-framework
research: `research/something-was-wrong-s16.md` F1 and F7 in that repo. Custody:
**LOCATOR-ONLY**. Every primary item was read in full this session; none is hashed or
archived.*

## The item

On 21 Feb 2012, in Paramount, California (a city that contracts with LASD), a Los Angeles
County sheriff's deputy shot and killed **Robert Chester Henning II** (22). A passer-by had
called 911 because Henning appeared to be in a mental-health crisis. The family sued in
federal court (*Elizabeth Adam, et al. v. County of Los Angeles*, C.D. Cal. CV 13-01156,
filed 15 Feb 2013). The County settled in 2015 for **$1,500,000**.

The public record of the death now consists of three artifacts. Their wording is the
specimen.

| # | Artifact (date) | Verbatim wording | Grade |
|---|---|---|---|
| A1 | Wikipedia, "List of killings by law enforcement officers in the United States, February 2012" (current; raw wikitext fetched 2026-10-04) | "unnamed male … Man was shot twice after attempting to take an officer's gun." It cites KTLA, "Deputy Kills Man in Paramount Shooting" | Secondary; reflects the 2012 press account |
| A2 | LA County Counsel, case summary for the Contract Cities Liability Trust Fund Claims Board (27 May 2015) | "The Deputies contend that the force used was reasonable and in response to Robert Henning's actions. Due to the risks and uncertainties of litigation, a reasonable settlement at this time will avoid further litigation costs." | County record (P1), read in full |
| A3 | The same memo's cover note | It refers to a "Summary Corrective Action Plan" as attached | **The plan itself was not located.** Status U |

**Counter-account (testimony; first-hand, but not tested in court).** The 911 caller is an
eyewitness. On a recording played in the podcast *Something Was Wrong* S16 (E7 and E8, 2023),
he says the deputies arrived with guns drawn and shot Henning "point blank". He says the
deputy told him "he went for my gun", which the witness contests ("I seen the whole thing").
He says another deputy then said "good job, partner". He is also reported to have given
depositions in the federal case.

**Searched for and not located (single-query depth):**
- an LA District Attorney charging decision. LASD's public table of deputy-involved
  shootings begins in 2018, and the DA's JSID letters searched did not include this case;
- a discipline record;
- the corrective action plan.

## Disconfirming test: is A2 case-specific?

At the time of drafting, the expectation was that A2's wording was case-specific
laundering. To test it, the wording was compared against the County Claims Board's
**4 May 2015** Statement of Proceedings (`file.lacounty.gov/SDSInter/ceo/claimsboards/1133462_CB-SOP-050415.pdf`).
That meeting settled five cases involving deputies.

| Case (4 May 2015) | Type | What the case summary records |
|---|---|---|
| *McDonald* | force | the plaintiff's **legal claim**; the deputies' **factual account** ("force … reasonable and in response to Mr. McDonald's actions") |
| *Torres* | force and false arrest | same structure ("… in response to Mr. Torres's resistance") |
| *Carrington* | force (custody) | same structure ("… in response to Mr. Carrington's resistance") |
| *Coulter* | false arrest | the plaintiff's allegation only; no deputy account |
| *Livingston-Bell* | vehicle collision | **both** factual accounts ("The Plaintiff and the Deputy each contends that the other ran through a red traffic signal") |
| *Henning* (A2, a different board, the same County Counsel attorney as *McDonald*) | force, death | same structure as the three force cases |

**Result:**
- **A2 is not case-specific.** It is a **template sentence**. Read alone, it shows nothing
  about the Henning case in particular, and the expectation above fails at the item level.
- **What survives is a structural asymmetry inside the template.** In these four
  force-case summaries:
  - the institution's **factual account** is the only factual account recorded;
  - the claimant appears only as a **legal label** ("alleging … civil rights were
    violated");
  - the record closes with a public payment and the stock reason "risks and uncertainties".

  In the one non-force case at the same meeting, the template records **both** sides'
  factual contentions.
- **Sample size:** five summaries from one meeting, plus A2. That is an instance of a
  template, not yet a pattern.

## Analysis (Ledger Analytical Taxonomy)

- **Move 2, self-evidence assertion (bare-verdict form).** "Force … reasonable" is the
  only characterization of the event in the record of public payment. No contrary account
  appears.
- **Move 5, euphemism / bureaucratic abstraction.** "Risks and uncertainties of
  litigation" stands in for whatever the county's own risk assessment found. That
  assessment was presumably in the corrective action plan, and the plan is not public.
- **Downstream propagation (A1).** The 2012 official account, carried in press reports,
  is still the reference-work entry. Henning is unnamed, and the 2015 settlement is
  absent. On the same page, a different 2012 death records the officer's citation and
  later firing. *A1 records propagation, not an act by an institution.* Wikipedia editors
  are not the actor. It belongs on the record as what the official account looks like
  after three years of litigation have not touched it.
- **Gap formula.** If the stated concern is accountability for deputy force (the reason a
  corrective action plan exists), the material remedy is a public finding of fact, or a
  public corrective action plan. A record that pays $1.5M while publishing only the
  deputies' account, and keeps the plan unlocated, voices the concern without the remedy.
  *Held as hypothesis* until the plan is found and read.

## Classification (proposed; for the operator)

- **A2 alone: NULL at the item level.** A template sentence used in every force case at
  the meeting tested says nothing about this case.
- **The template: SPECIMEN, provisional, structural.** The asymmetry between force and
  non-force summaries is the discriminator.
  - *Upgrade condition:* the asymmetry holds across a larger sample of Claims Board
    summaries (say, 30+ force cases across several years and boards).
  - *Downgrade condition:* force summaries also routinely record the claimant's factual
    account, or the corrective action plans are public and do the fact-finding.
- **A1: not classified.** It is a downstream record, kept as context.

## Developer-symmetry check (Anthropic)

*Standing check. Each standard this file applies to a powerful actor is applied to
Anthropic, the analyst's developer. U = not searched; none found = searched, nothing
located.*

| Standard applied in this file | Result for Anthropic |
|---|---|
| A settlement record that carries only the paying party's framing, with no admission | **Applies.** *Bartz v. Anthropic* settled for $1.5B in Sept 2025, without admission of liability. As reported (search summary; the primary statement was not captured), Anthropic's deputy general counsel said the settlement "will resolve the plaintiffs' remaining legacy claims. We remain committed to developing safe AI systems that help people … advance scientific discovery, and solve complex problems." "Legacy claims" is **Move 5**. The commitment sentence is a **Move 6** benefit reframe. That is **more** framing than the County's template carries, not less. |
| A public corrective plan referenced but not published | U for Anthropic as a direct analogue. Whether Anthropic published remedial measures after *Bartz* (for example, on data acquisition) was not searched this session. |

## BOUNDARY

**Establishes:**
- a dated County record of a $1.5M settlement, with no admission, of a wrongful-death suit
  over a deputy shooting during a crisis call;
- that the record's only factual statement is the deputies' contention;
- that this wording is a template, which within one meeting appears only in force cases;
- that the reference-work entry still carries the 2012 official account.

**Does NOT establish:**
- what happened on 21 Feb 2012;
- that any individual acted in bad faith;
- that the County drafts force summaries to suppress claimants' accounts (intent is open;
  the template may be a defensive-litigation convention);
- that the asymmetry is general. One meeting is an instance.

**What would falsify the structural reading:** force-case summaries that routinely record
the claimant's factual account, or published corrective action plans that make factual
findings.

**Cross-references:** Pattern Registry Entry 7 (the Accountability Simulacrum: payment
without a finding as a candidate form); Entry 17 (Performed Ignorance: the unlocated
corrective plan); Track D (testimony that the record does not contain).
