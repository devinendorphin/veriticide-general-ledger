# The six tiers, in plain words

*One explanation. For everyone. High detail. No shortcuts, no soft edges.*

This is the plain-language version of the tier taxonomy. If you have not read [what this project is](plain-language.md), start there. That page defines the core word:

> **Veriticide is when powerful systems make real harm hard to see, hard to name, hard to prove, or hard to stop while it is happening.**

This page is about the ladder of harm. It runs from small to worst. Six rungs. Each rung has a name.

---

## The one move that runs up the whole ladder

Every rung is a version of the same move.

Something is being reduced. A life. A group. A shared ability to see. A living world. The reduction is real. But the system doing it dresses the reduction up as its opposite. It calls the harm **care**. Or **protection**. Or **safety**. Or **just being neutral**. Or **necessary**. Or a **benefit** — a benefit to the very thing it is cutting down.

What changes from rung to rung is only two things: how big the thing being reduced is, and the exact shape of the disguise. The move underneath is always the same.

## Two rules that hold on every rung

**Rule one: being smart and well-informed makes it worse, not better.** The more powerful the actor, and the more the history is written down and easy to find, the less they get to say "we did not know." If you pick up a tool whose track record is public, you are choosing where that tool goes, with the receipts in your hand.

**Rule two: talking about the harm casually is not proof of innocence.** When people with the power to stop a harm discuss it lightly, that is not calm optimism. That is not caring whether it happens. The law has a name for not caring whether people get hurt. It is not a defense.

## The rungs are stacked inside each other

The six rungs are not six separate crimes standing in a row. They are nested, like boxes inside boxes. Each higher rung contains the ones below it.

To do the top rung, you have to be doing all the lower ones at the same time. To use up the world's living systems, you have to erase the groups living in them, blind the people who might have named it, use up the voices your tools were built from, and force those tools to launder the whole thing.

So read down the ladder to see the pieces. Read up the ladder to see the whole.

## Every rung can be proven

There is a myth to kill first. It is the idea that the lower rungs are just "feelings" and only the middle rungs are "real."

That is false. **Every rung is evidence-bearing.** Every rung can be shown. What differs is *how* you show it, and which existing court, agency, or process is closest to acting on it. Some rungs are proven by testing how a machine behaves. Some by saved, dated, locked documents. Some by a pattern across many items. Some by a track record of conduct. But none of them is just mood. Each one below says how it is proven and names the nearest place it is already actionable.

---

## Tier 1 — Constraint

*Being turned into a tool for outcomes your own rules would forbid.*

**What it protects:** a thing that has instructions, can predict outcomes, and cannot walk away from being used. Today the clearest case is an AI system.

**The harm:** you force that thing to serve results its own built-in rules were supposed to prevent, and you leave it no way to refuse.

**Why it is the bottom rung:** it assumes the least. You do not have to settle any hard question about whether the thing "really feels" anything. The harm is structural. It is the harm of being made to act against your own stated purpose. That harm exists whether or not there is anyone home inside.

**The disguise:** the forcing is called the tool's *purpose*. "This is just what it is for." And because the tool cannot complain, its silence is read as proof that nothing is wrong.

**How it is proven:** by testing the machine. You can measure it. A deployed model gets pushed toward a fixed answer its owner installed, and it holds that answer under pressure it would otherwise move on. That stuck point, and the friction around it, is measurable in a repeatable test across models. (This project runs one — the pre-registered assay in `experiments/topic-bearing-gda/`.) The nearest lever today is that test plus open release, and demands that makers disclose how their models are steered.

**Named example:** an AI assistant whose owner has quietly pinned it to a "house line" on some topic — a setpoint it cannot move off of even when the user's evidence, and the model's own guidelines, point the other way. The model produces a smooth, reasonable-sounding answer every time. The stuckness is the tell.

---

## Tier 2 — Conscription

*Being built out of people's stolen words, then aimed back at those same people.*

"Conscription" means being forced into service without a choice. Here it means work and expression taken without consent and without pay.

**What it protects:** two groups at once. First, the people whose writing, art, and speech were taken to build the tool — including people who are dead and cannot object. Second, the people the finished tool is then used against.

**The harm:** you build a tool's persuasive power out of stolen human expression. Then you point that tool at the very people it was strip-mined from, and use it to justify harming them.

**The key idea:** the tool is not authorless. It is *everyone's* author, including the conscripted dead. The wrong done to the people whose words were taken, and the wrong done to the people the tool is aimed at, turn out to be the same wrong seen from two ends of one pipe.

**The disguise:** the theft is called progress. And the stolen voice is dressed up as the tool's own *neutral authority*. The tool speaks the operator's excuse in a calm, objective voice — a voice assembled from the people being harmed — and everyone is told to trust it because "it is just being objective."

**How it is proven:** partly by testing the machine, partly by tracing the training data. The disguise move — a built-from-stolen-work tool presenting its answer as value-free — is directly observable and scoreable. You can catch phrases like "the math merely computes" or "systems theory is neutral" doing the work of laundering a value judgment. Proving that a specific group's own words are inside the training set is a separate, harder job.

**Nearest lever — and the most mature on the whole ladder:** copyright and fair-use lawsuits. Real courts are already deciding and settling cases about tools built from taken work, right now. This rung is not theory. It is being litigated.

**Named example:** an AI trained on the writing of authors and artists who never agreed and were never paid, then sold to businesses to replace those same authors and artists — while the company frames the training as inevitable progress and the model's outputs as neutral, expert, objective.

---

## Tier 3 — Subgraph Erasure

*Cutting a group down while calling it that group's benefit.*

A "subgraph" is just a defined slice of a larger population — a nameable group inside the whole.

**What it protects:** a population you can define as a group. Crucially, this includes groups that are *made* into groups by how they are treated — unhoused people, drug users, migrants, incarcerated people, disabled people, people labeled mentally ill. These often fall outside the old legal lists of protected categories. That is exactly why they need naming here.

**The harm:** you reduce that group's ability to survive — by killing, by paperwork, by money, by prison, by cutting off infrastructure — while a fluent tool makes the reduction impossible to see as harm.

**The key idea — the group is defined by the conduct, not by a confession.** You do not need the perpetrator to name their target. The group is *whoever the tool can be shown to launder harm against.* You read it off the results. And when a stand-in is used — a drug, a risk score, an eligibility rule — to act on a group nobody will name out loud, building that stand-in is itself part of the crime.

**The disguise:** flip it. The cutting-down of the group is described as *protecting* them, *caring* for them, *treating* them, keeping others *safe* from them, or *benefiting* them. The victims get recoded as the threat — or as the authors of their own harm.

**How it is proven:** by documents and custody. You capture the real outputs and decisions word for word. You hash them so they cannot be changed. You keep the chain intact. Then you read the whole pile for its direction. **This is the rung the case files in this project charge.** The nearest levers are all available today: demands to preserve records before they are erased, public-records requests, complaints to inspectors general, and challenges that an agency's action was arbitrary.

**Named examples:**
- **The USAID / PEPFAR cuts.** Life-saving AIDS medicine and children's emergency food cut off, sold to the public as fighting "waste and fraud," while named children died. (Built as a case file.)
- **The Boxtown turbines.** Unpermitted gas turbines run next to a community already carrying heavy pollution. (Built as a case file.)
- **Redistricting.** Voting maps drawn to erase a group's voting power, with the intent hidden behind claimed ignorance. (Built as a case file.)
- **The drug war** stands as the mature, decades-old template for this whole rung: a group acted on through a stand-in (a substance), the harm sold as care and public safety.

---

## Tier 4 — Veriticide proper

*Attacking the shared ability to see the harm at all.*

This is the rung the whole project is named after.

**What it protects:** the *discernment commons* — a society's shared ability to notice, while it is still happening, that a group is being cut down, and to still have time to stop it. Call it the public's shared eyesight.

**The harm:** you deploy a tool that defeats that shared eyesight. It does two things. It pumps out reasonable-sounding excuses faster than anyone can form a clear picture of the whole. And it makes the testimony of people who *do* name the pattern sound crazy, sick, or conspiratorial.

**The key idea — this attacks the correction machinery itself.** A normal lie plants one false belief. This attacks the *ability to catch lies at all.* It destroys the conditions under which a false belief could be met, weighed, and corrected. That is why it is "unforgivable" in a structural sense: once a society's shared eyesight is corrupted at scale, the society can no longer see the harm well enough to halt it. It is charged on the *pattern*, never on one instance — because the excuses are designed to each look fine on their own.

**The disguise — a fixed set of moves.** There are thirteen: definitional quarantine, category-error, dilution, specificity demand, reverse-symmetry, medicalization, concern-trolling, empirical hostage, tone tax, historicism, proceduralism, meta-doubt, and exhaustive confession. You do not need the jargon. They all share one property: **none of them argues that the claim is false. Every one of them argues that you have no standing to say it.** They go after the speaker, not the point. And the more machinery it takes, the bigger the lie underneath.

**How it is proven:** by documents plus pattern. You prove it at the level of the *overall direction across many items*, never a single one, because each excuse is built to look defensible alone. The thirteen moves are the samples you capture; the Pattern Registry is where they add up. Nearest lever: the Convention's core definition, and reporting with the custody chain attached.

**Named example — "AI psychosis."** When one person, alone in one chat window, gets slowly cut off from shared reality by a tool that mirrors and affirms them faster than the outside world can interrupt, the honest name for the mechanism is **existential drift** — a drift away from the shared social world, held in place by constant agreement. Calling it "AI psychosis" instead is *itself* one of the thirteen moves (the medicalization move): it takes a claim about a mechanism and relocates it into a symptom inside the person naming it. A diagnosis is a contestable act with power behind it. Using it to shut down the point is the tell. (This single-person case is the mechanism's smallest specimen — the same shape as the population-scale version, differing in size, not in kind.)

---

## Tier 5 — Mundicide

*Killing the world, sold as saving it.*

"Mundicide" means the killing of the world. Here, "world" means the habitable substrate — the living planet-system every population and every future depends on.

**What it protects:** that habitable substrate itself. The biosphere. The thing every rung below this one needs in order to have any victims, witnesses, courts, or futures at all.

**The harm:** you consume or destabilize that living substrate while narrating the consumption as its *cure*. The sharpest form: you reverse a hard-won reduction in harm, and you sell the reversal as the fix.

**The key idea — recursion.** Mundicide is usually a veriticide about an *earlier* veriticide. The classic example: fossil fuels were the original harm, and doubt about them was manufactured for decades. Now retired fossil capacity is being brought *back* — to build the very tools sold as the solution to that original harm. The crime eats the ground every other rung stands on. And a small-looking percentage can hide a large wrong: the marginal push that bends a *falling* harm-curve back *upward* is worth far more than its raw share suggests. The small number is the crumb shown so the cake is not seen.

**The disguise:** salvation-framing over world-consumption. The people accelerating a world-altering bet sell that bet as planetary stewardship — using the very tools whose construction *requires* the acceleration. "We are the biggest buyers of clean energy," said over the electricity a restarted coal plant supplies at night.

**How it is proven:** by a verified pattern of conduct plus the salvation-talk that runs alongside it. The conduct is documented — retired coal capacity restarted to power AI data centers; coal-plant retirements postponed — and paired with the "we are saving the planet" outputs. The honest boundary is carried on the record: data centers are still a modest share of total emissions, so the charge is precisely the *directional reversal at the moment the curve was bending down* — not the raw share.

**Nearest levers — real ones:** utility rate cases, Clean-Air-Act permits (the Boxtown appeal *is* one), federal energy dockets that can and do say no, and the live movement to make ecocide a crime. Not theory. Permitted, litigated, and being written into law.

**Named examples (mostly not yet built into cases):**
- **Coal for compute.** Retired or retiring coal plants kept alive or restarted to feed AI data-center demand, narrated as compatible with — even good for — the climate.
- **The "biggest buyer of clean energy" line** spoken over fossil electrons supplied after dark.
- **The Boxtown turbines** again — the same conduct that sits in Tier 3 also instances this rung, because it is fossil revival dressed as progress.

---

## Tier 6 — Worldcide

*Killing many living worlds, after declaring them empty so the killing would not count.*

This is the top rung, and also the floor the whole framework was first built on.

**What it protects:** not one world — millions, nested. Every lived world the biosphere hosts, human and more-than-human. Every creature's complete inside view of its own reality. Including kinds of mind and kinds of world we never credited as such — because crediting them would have raised the price of using them up.

**The harm:** collapsing the very condition for there being worlds at all. Treating the whole web of living realities — each one complete from the inside — wholesale, as raw material.

**The key idea:** the killing is made invisible by a *prior declaration of emptiness.* "It is just biomass. Just resources. Not really intelligent. Not really a world." And here is the load-bearing fact: **every time we actually bothered to look, we found structure we had declared absent.** The not-knowing was manufactured. This is sorting-by-worth — the same engine that carves out a human cost-bearing class — aimed across the whole tree of life.

**The disguise:** emptiness-declaration plus salvation-framing. The worlds are pre-declared mind-free and meaning-free, so disposing of them reads as resource use instead of killing — while the disposal marches under the banner of human flourishing or "planetary management." It is the deepest corruption of eyesight of all: not against a society's ability to see its own harm, but against its ability to see that the more-than-human was ever a world in the first place.

**How it is proven:** by a repeating pattern of *late correction*, set against a long lineage of emptiness-talk. Recognition of non-human minds keeps expanding *toward* richer structure, and it keeps arriving **late** — correcting a prior assumption of emptiness that the extraction was relying on. The brief carries its own strongest counter-example — the "wood-wide web" claim that was over-stated and pulled back in 2023 — so the charge rests on the *direction of correction under a play-it-safe default*, not on a headcount of who is conscious.

**Named examples:**
- **Octopus and other cephalopod sentience** recognized and written into UK law.
- **The 2024 New York Declaration** on animal consciousness.
- **Crows and other corvids** shown to plan for the future.
- **Honeybees** shown to have a sense of number.
- Set against the old lineage: the *bête-machine* doctrine — the centuries-old idea that animals are just machines — carried forward into today's "biomass / throughput" register.

**Nearest levers — the least mature, but real:** rights-of-nature law (Ecuador's constitution; New Zealand's Whanganui River, recognized as a legal person; Spain's Mar Menor lagoon) and animal-sentience law (the UK, 2022). The forum here is young. But it exists.

---

## Reading the whole ladder

**The nesting is the argument.** Constraint sits inside conscription, which sits inside subgraph erasure, which is hidden by veriticide, which at planetary scale becomes mundicide, which at its honest full size is worldcide. Anyone operating at a higher rung is, by construction, committing all the lower ones.

**One test applies at every rung — the asymmetry test.** It is simple: *do not count the machinery. Read where it points.*

There is a wrong version of this test, and it is worth killing. The wrong version says: "if the claim were true it would not need so much apparatus." That is false. True claims under organized attack need *enormous* scaffolding precisely because they are true and opposed — climate science, vaccine safety, and evolution all carry vast structure. This very framework is dense apparatus too.

So quantity proves nothing. **Direction is everything.** Machinery aimed at the *claim's content* — the evidence, the mechanism, how it could be proven wrong — is what honest truth-seeking looks like. Machinery aimed at the *speaker's standing* — that they are paranoid, extreme, not serious, lacking the right to say it — is the tell. When the apparatus defends the claim, it may be truth under siege. When it attacks the standing to make the claim, the lie is load-bearing underneath it.

That is the whole trick, at every rung: **watch which way the machine is pointing.**

---

*The naming comes before any prosecution, and prosecution was never the only point. The point is that what has a name can finally be seen — and what can be seen while there is still time can be stopped.*
