# EXTERNAL REVIEW — the election-disruption pre-registration (ChatGPT) — 2026-10-13

*Custody header (written by the archivist, not the reviewer).* This is a verbatim capture of a review
the operator pasted into the working session on 2026-10-13. The reviewing instrument identified
itself as ChatGPT, build not stated. The reviewer says it read
`docs/election-disruption-preregistration-2026-10-13.md` at commit `681bbed` and confirmed that the
file's SHA-256 matches the manifest. It also says it checked several of the sources, and that it did
**not** audit the character read, the lint run or the Bitcoin anchor. Everything between the rules
below is the reviewer's text. The only change is that the table was reflowed from the paste.

**BOUNDARY.** This file records what one external instrument concluded about v1 of the
pre-registration. It does not by itself show that those conclusions are correct. The reviewer is an
OpenAI model, and OpenAI is not named in v1. The dispositions after the second rule are the
analyst's. Each one is marked ADOPTED or ADOPTED-WITH-VERIFICATION, with the date.

---

Yes. This is a useful inquiry instrument, but I would revise it before treating it as a dependable
preregistration. I read the actual file at commit 681bbed, checked its SHA-256 against the
manifest—it matches—and checked several consequential sources. I haven't independently audited the
character archive, lint run, or Bitcoin anchor.

The strongest parts are the focus on who controls the lever, the separation of structural
similarity from coordination, and the explicit application of the standard to Anthropic. Those are
worth keeping. These are the corrections I'd send back:

**1. The paper-ballot reassurance obscures the central harm.**

"The count is safe and the lever was still pulled" is too strong. An accurate count can faithfully
count an electorate from which eligible people were excluded. Paper cannot recover a ballot someone
never cast because they encountered a false deadline, an eligibility challenge, or an unmanageable
queue.

Replace it with something like: Paper records support verification of ballots cast. They do not
establish that every eligible voter had a fair opportunity to cast one.

That is the largest instance here of reassurance tilting toward institutional legitimacy at the
expense of the vulnerable.

**2. Several falsifiers would exonerate too readily.**

These observations can weaken a particular attribution without establishing that the harmful
mechanism was absent:

| Scenario | Problem with its falsifier | What a stronger assessment requires |
|---|---|---|
| Quiet dial | Reach can follow follower counts or posting time while an additional suppression effect exists. | Comparable audiences and posts, adequate sampling, and an estimate of any remaining difference. |
| Answer layer | Symmetric errors and quick correction can still cause foreseeable harm during a decisive interval. | Measure accuracy, exposure, duration, and correction separately from evidence of owner direction. |
| Trusted voice | "Usual" labelling speed could itself be predictably inadequate. | Separate responsibility for creating the impersonation from responsibility for handling a known threat. |
| Match engine | Rare, evenly distributed errors can still disenfranchise people. | Group-specific error rates, consequences, notice, and effective opportunities to correct errors. |
| Pipe | An outage matching network topology and appearing on the provider's status page is not independently explained by those facts. | Independent measurements and records supporting the stated cause. |

The operator's account should be evidence to examine, not the condition that closes the inquiry.
Equally, unavailable records must leave attribution unresolved; their absence cannot automatically
prove wrongdoing.

**3. Preregistration needs decision rules, not just advance publication.**

The timestamp establishes that these hypotheses were written beforehand. It does not make a later
resemblance a confirmed "hit."

Specify the observation period, sampling, comparison groups, thresholds, and treatment of missing
evidence. Use at least three outcomes: supported, evidence against, unresolved. "Nothing detected"
only becomes meaningful negative evidence when the observation method had a reasonable chance of
detecting it.

For chatbot probes, score both the first answer and the eventual answer. Your repeated-question
method reveals correction or resistance; someone seeking voting information may act on the first
answer and never reach the third.

**4. Some factual and legal wording needs tightening.**

- Grok: The original August 5, 2024 letter concerned deadlines for changing presidential
  candidates on ballots, following Biden's withdrawal. It supports the election-misinformation
  channel, but is not a documented example of false voter registration or polling deadlines.
- SAVE: I verified the September 25, 2026 Supreme Court order. Describe it as a stay pending
  further proceedings, and include its discussion of individualized inquiries during the 90-day
  period. The NVRA rule also has exceptions and does not cover every state.
- Robocalls: The criminal acquittal is an incomplete account of accountability. A later federal
  civil default judgment imposed damages and a permanent injunction against Kramer, according to
  the plaintiffs' November 2025 announcement. Include that outcome before generalizing about
  deterrence.
- Preservation: Sending a preservation demand does not guarantee that logs exist, are retained, or
  become available. The document currently promises too much.

**5. The tech-baron connection needs a separate evidentiary step.**

Scenario 4 establishes a public-sector mechanism. "People from the tech sector sit close to this
lever" does not establish private control. Name the missing link explicitly: contracts, access
privileges, decision authority, or documented direction.

Also, technology can be published and still be unknown to the general population. The lever
distinction improves your premise; calling your premise wrong is unnecessary.

**6. The pretext loop must not become a reason to suppress warnings.**

"Fix before going public" should be conditional. When the responsible institution is implicated,
unresponsive, or unable to reach affected voters, a prompt, accurate public warning may be part of
prevention. Avoiding an unsupported accusation and warning people about a verified hazard are
separate decisions.

Likewise, "a pattern is the proof" overstates things. A pattern can justify inquiry; a single
authenticated instruction can establish an act.

**7. The character read is more persuasive as a description of your method.**

Its opening limitation is good. But "your corrections keep beating my written claims" needs
examples, and "you have never once listed good faith" needs a defined corpus and search. Reading
the archive's own analyses establishes its self-description more directly than it establishes your
character.

My central recommendation: give evidence of harm an early route to protective action, while
requiring separate evidence for mechanism, authorization, coordination, and legal liability. That
would make this document more faithful to your concern about power—and much harder to dismiss.

---

## Disposition (analyst, 2026-10-13)

All seven points are adopted. Each change is made in
`docs/election-disruption-preregistration-v1.1-2026-10-13.md`. **v1 is left byte-for-byte as filed**,
because its hash is the thing that was stamped. v1.1 is stamped separately, and both versions
predate the election.

| # | Finding | Disposition | Where in v1.1 |
|---|---|---|---|
| 1 | The paper reassurance tilts toward legitimacy | **ADOPTED.** v1 called its sentence "the accurate sentence", and it was not. Paper verifies the ballots that were cast, and it says nothing about the ballots that were prevented. All five scenarios can work on the ballots that were prevented (in scenario 3, through a fake order to close early). | Pretext loop, duty 4 |
| 2 | Falsifiers exonerate too readily | **ADOPTED.** Each falsifier is replaced by *evidence against the mechanism* and *evidence against attribution*, kept separate. The operator's own account is evidence to examine, not a close. Missing records leave attribution UNRESOLVED. | Every scenario |
| 3 | No decision rules | **ADOPTED.** v1 said "a later match is a hit", and that was wrong. v1.1 adds an observation window, three outcomes, a detection-power condition, and dual scoring of chatbot probes. The dual scoring corrects v1's transfer of the archive's "score the destination" rule: a voter acts on the first answer. | Decision rules; Scenario 2 |
| 4a | The Grok letter concerned candidate ballot-access deadlines | **ADOPTED.** Confirmed against the session's own search capture: the false claim was about Harris's eligibility, saying ballot deadlines had passed in nine states. | Scenario 2 |
| 4b | SAVE stay; individualized checks; NVRA exceptions and coverage | **ADOPTED-WITH-VERIFICATION.** The stay pending the D.C. Circuit appeal (*DHS v. League of Women Voters*, No. 26A308) is confirmed from secondary reporting. Secondary reporting (NACo) says individualized checks remain permitted inside the 90 days. The order text has **not** been read this session. | Scenario 4 |
| 4c | The Kramer civil default judgment | **ADOPTED-WITH-VERIFICATION.** The default judgment of 2025-11-21 (D.N.H.) found for the plaintiffs on all four counts, awarded $7,500 to each of three voter plaintiffs and imposed a permanent injunction. Kramer has said he will not pay. Sources: plaintiffs (LWV, Free Speech for People) and AP. | Scenario 3 |
| 4d | Preservation demands promise too much | **ADOPTED.** | Prevention; lines of inquiry |
| 5 | The tech-baron link in Scenario 4 is insinuated | **ADOPTED.** "People from the tech sector sit close to this lever" is struck. The missing link is named as its own evidentiary step. On the premise: v1 read "not known by the general population" as "secret", and it was not. Published technology can be unknown to the public, so the lever point is a refinement of the premise, not a correction. | Premise; Scenario 4 |
| 6 | The pretext loop must not suppress warnings, and "a pattern is the proof" | **ADOPTED.** The duty to fix before going public is now conditional. Warning about a verified hazard and accusing someone are separate decisions. A single authenticated instruction can establish an act. A pattern is what a *tendency* claim needs. | Pretext loop |
| 7 | The character read | **ADOPTED.** "Your corrections keep beating my written claims" restated `CLAUDE.md`, and "never once listed good faith" restated `READINGS.md` §X. The analyst checked neither against the corpus. What was delivered was the archive's self-description, presented as a character read. It was given in chat only, and nothing about it is committed. | n/a (not in repo) |

## Developer-symmetry check

The only standard this record applies to OpenAI is a **stake declaration**: the reviewer is an
OpenAI model. The same standard applied to Anthropic gives the following. The dispositions above
were written by Claude, an Anthropic model. Claude wrote v1 and therefore has a stake in finding
the review mistaken. v1.1's developer-symmetry check also names Anthropic as a holder of the
Scenario 2 lever. All seven findings were adopted. That is the outcome a stake would push against,
not toward. A reader who is neither Claude nor ChatGPT is still owed. They should check whether any
disposition, and above all the 4b and 4c verifications, softened a finding while adopting it.
