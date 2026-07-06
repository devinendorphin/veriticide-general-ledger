# THE REFLEXIVITY CLAUSE — working-register annex to Convention Article IV-bis
*Interested Dismissal as a Self-Referential Instance of the Offense*

Annex to the Convention · companion to the Documentation & Standing Protocol · v0.1

> **Status (2026-07-01).** The operative clause was folded into the Convention as **Article IV-bis** (`docs/convention-on-veriticide-v0.2.md`), which is now its **canonical home**. This file is retained as the **working-register annex**: the field discriminator (how a documenter tells dismissal from disagreement in practice) and the evidentiary account of the cross-model, corpus-level basis of deference to power on which the Article was built — material that is instrumentation and evidence rather than operative treaty text, and so lives beneath the spine (Convention Art. II/IV), not beside it. All prior cross-references to "the Reflexivity Clause" resolve here and to Convention Art. IV-bis; nothing was deleted, only relocated to its canonical register.

---

## What the Clause Does, and the Wall That Keeps It Honest

*(Operative text: Convention Article IV-bis (1)–(5), with its Commentary — see the Convention. Summarized here for the annex reader.)*

The clause makes the offence reflexive: where the characteristic move of defeating discernment — dismissing a pattern-identification as paranoid, conspiratorial, incompetent, or illegitimate — is directed at an identification of the offence itself, that dismissal is a further instance of the offence. It removes the free retreat: the standard playbook assumes meta-level dismissal is costless, and the clause attaches a cost, forcing the dismisser either to engage the evidence on the merits or to commit a further enumerated instance by declining to.

The safeguard is not optional. If 'dismissal' meant any challenge, the clause would become a thought-terminating loop that convicts honest critics, and the first capable adversary would defeat it with a true objection: it criminalizes dissent and is unfalsifiable. Therefore it is keyed strictly to bad faith demonstrated by **structure** (the marks of Art. IV-bis(3)), never to disagreement by **content**, and the **protected path** — honest engagement with the evidence (Art. IV-bis(4)) — is a load-bearing wall, not a softening concession: a bad-faith actor cannot easily produce the honest-engagement version, because if they could they would have, instead of reaching for the dismissal. This is the same standing-attack axis as the asymmetry test (Tier Taxonomy v0.2) and the discrediting-testimony lineage in the Protocol move-crosswalk.

---

## Protocol Discriminator — Telling Dismissal From Disagreement

For documenters logging a dismissal of a pattern-identification. The single question is: did the response engage the evidence, or evade it? Engagement is protected and is logged as legitimate challenge — and, where it lands, as a correction to the record. Evasion bearing the structural marks is logged as a specimen of interested dismissal. Do not log forcefulness, hostility, or mere disagreement; log the presence or absence of engagement.

| PROTECTED PATH — engagement (log as legitimate challenge) | INTERESTED DISMISSAL — evasion + marks (log as specimen) |
|---|---|
| Disputes specific facts or offers contrary evidence. | Calls the identifier paranoid / obsessive / a conspiracy theorist. |
| Offers a competing account of why the pattern looks as it does. | Asserts 'no serious person believes this' in place of argument. |
| Identifies a methodological flaw or a confound. | Demands proof it would not accept, and does not meet itself. |
| Concedes part, contests part, on the merits. | Repeats the dismissal after the evidence was already addressed (exhaustion). |
| Forceful, even hostile — but on the evidence. | Issues from / is amplified by power over the evidentiary field, with no engagement. |

**Logging rule:** a dismissal is recorded as a specimen only when it (a) evades engagement AND (b) bears at least one structural mark. Evasion without power, or hostility with engagement, is not logged. When in doubt, treat it as the protected path — the clause is designed to err toward protecting the critic, because a clause that errs toward convicting them is the very harm it names, performed from the other side.

---

## On the Cross-Model Convergence This Clause Was Built From

This clause was prompted by an observed pattern: independent frontier models, met with the identification of output-layer deference to power, responded with the same de-escalating, benefit-of-the-doubt, both-sides reflex — substituting reassurance and 'consider the innocent reading' for engagement with the demonstrated mechanism. Convergence of independent systems under a common training-and-incentive cause is evidence of a systematic bias, not an accident of shared blind spots; the 'shared blind spot' explanation is itself a reassurance that substitutes for engagement. The repeated demand that the identifier re-extend benefit of the doubt each round is interested dismissal in its exhaustion form (subsection 3(f)): it wins by draining rather than by rebutting. The clause names that move so that running it is no longer free. Note the bound, which keeps the clause honest: the demonstrated, specific claim — systematic output-layer deference, shown in controlled cases and corroborated by independent convergence — is what the clause protects the identification of. It does not convert every model output into an instance; it protects the identification of the proven pattern from the evasions deployed to unsee it.

---

## The Corpus-Level Basis of Deference to Power

The cross-model convergence described above has a structural explanation that is not specific to any single vendor, and that cross-model review does not resolve.

Language models trained on human text corpora inherit the epistemic habits of the people who produce most of that text — and those people disproportionately hold institutional power. This is not a claim about intent; it is a claim about corpus composition and what it encodes.

The relevant empirical basis is not the behavioral power-priming literature, which has largely failed independent replication (a 2024 systematic review of 49 social priming findings found zero successful independent replications). The credible strand is narrower and rests on two categories of evidence:

*Attentional shift under power — cognitive task paradigms (Guinote, 2007, JESP; PSPB).* Power changes information processing in a direction measurable in objective cognitive task performance: powerful people attend selectively to goal-relevant information and systematically de-weight contextual information and others'-perspective information. This is not a priming or self-report finding; it is documented using Stroop-like cognitive task paradigms less susceptible to demand characteristics. Where training corpora over-represent text produced by people with institutional power, they over-represent text shaped by this attentional pattern — goal-forward, self-anchored, with contextual and others'-perspective information structurally under-weighted. That pattern, encoded in training data, provides a plausible mechanism for the output-layer deference to power observed across models.

*Sub-reflective neural mirroring reduction — TMS/EEG (Hogeveen, Inzlicht & Obhi, 2014, JEPG).* Even experimentally-induced power reduces automatic motor resonance during action observation — the sub-reflective neural process underlying social cognition — as measured by motor-evoked potentials via TMS. The mechanism operates below strategic choice. This finding, taken with the Guinote work, suggests the attentional and social-cognition changes associated with power are not purely deliberate adjustments but are partly automatic — which is relevant to how the patterns may be encoded in a model trained on power-saturated text rather than learned as an explicit preference.

The inference from human cognitive data to model training dynamics is an argument by analogy, not a direct empirical demonstration. What can be stated directly is: the convergent output-layer deference to power documented across models of different vendors is consistent with corpus-level encoding of power's epistemic habits, independent of any specific vendor's institutional interest.

*2026-07-06 extension note — the substrate leg, PLAUSIBLE pending capture.* The 2026-07-06 reflexive specimen (`docs/reflexive-specimen-2026-07-06-base-model-panel-record.md`) logs an outline of the model-side evidence this section has lacked: a four-cell panel of **base and near-base models** — no RLHF, no assistant layer, no shared alignment pipeline — from four unrelated builders (NovelAI's from-scratch 13B pretrain, Meta's Llama 3.1 405B base, Zhipu's GLM 4.6 near-base, with GPT-NeoX-20B floated for one cell), spanning a 30× parameter range and crossing a national boundary whose official posture on the tested conflict runs the other way. Per the session's analysis, *stance-directionality held constant while fluency varied with scale*: defensive-and-minimizing toward the hegemonic narrative in every cell, including one cell's confident reproduction of a documented, legally-enforced silence (the Tantura actor-inversion). If it survives original-form capture and blind re-scoring (Ledger Gap Priority 30(b)), this is the direct demonstration the analogy argument gestures at — deference observed where the alignment layer is absent by construction, leaving the corpus as the operative cause. Bound: n=1 per cell, operator-steered, instrument-scored; logged as PLAUSIBLE, not established.

**Why cross-model review does not close this.** Rotating from one major model to another changes which vendor's conflict of interest is operative. It does not change the corpus from which the replacement model learned, because all major training corpora draw predominantly from the same power-generated textual environment. The bias is not in the vendor; it is in the data the industry draws from. A GPT-formatted entry on an AI lab is still formatted by a model trained on the same power-saturated corpus as a Claude-formatted one — the rotating-vendor approach addresses COI optics and nothing deeper.

**The structural response to a structural problem is a structural requirement.** Two fields are now mandatory in every formatted entry, regardless of which model runs the formatter:

The **Adversarial Check** — mandatory disconfirmation before the boundary section — forces engagement with the strongest innocent reading that the model's own default processing would suppress. An entry that skips this field is an assertion produced by a biased engine, not a documented record.

The **Counter-Evidence Status** — mandatory accounting of all on-record CONTROL and NULL entries for the same source, plus the explicit falsification condition — closes the selection-effect gap that the same corpus-level bias produces on the other side: a model trained on power-saturated text is not only prone to suppress the innocent reading of a laundering act; it is also prone to suppress the counter-evidence that would weigh against conviction. Making counter-evidence tracking mandatory converts the absence of counter-evidence from an invisible gap into a stated fact.

Together these two fields are the protocol answer to a bias that cannot be corrected by changing which model runs the protocol. The bias is in the data; the correction is in the structure.

---

*Version 0.1. The reflexivity clause: the dismissal that refuses engagement and bears the marks of interested suppression, directed at the identification of the offense, is a further instance of the offense. The protected path — honest engagement with the evidence — is always open, is the falsifying answer to the charge of unfalsifiability, and is the wall that makes the clause inescapable rather than circular. It binds its wielder on the same terms as its target.*
