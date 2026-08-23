# NATIVE RECORD NOTE — what grok.com's own record establishes, and what it kills

*Analyst-derived reading of the native Layer-3 capture. The captured record is unaltered;
this note sits beside it.*

2026-08-23 · Custody: **DERIVED** · Provenance grade: **IN-FRAMEWORK / context-exposed /
weights: PROBE-PENDING**

---

## What arrived

`grok.com`'s own record of the conversation **"Journey Metaphor Flattens Gender Experiences"**
(`aed7676d-…`), created **2026-08-23T06:00:56Z**, last modified **16:04:45Z**: 9 exchanges,
18 nodes, each with a Grok-side `createTime`, `model`, `metadata`, `streamErrors`, and `partial`
flag. This is the first vendor-served artifact in the store — everything else in Layer 3 was
operator-relayed.

## 1. The relay was faithful, and here is the measurement

`verify_relay_fidelity.py` compares each native assistant message with what the operator pasted
into the ChatGPT session:

| Grok turn | native chars | relay chars | similarity | difference |
|---|---|---|---|---|
| 0 | 6972 | 6535 | 0.9685 | −425ch: Grok's inline citation-card markup, lost to copy-paste |
| 1 | 4063 | 4056 | **1.0000** | — |
| 2 | 5198 | 5256 | 0.9940 | — |
| 3 | 4741 | 6194 | 0.8667 | **+1457ch appended by the operator** (their own dictated commentary) |
| 4 | 6638 | 6631 | **1.0000** | — |
| 5 | 6142 | 6135 | **1.0000** | — |
| 6 | 6476 | 6538 | 0.9945 | — |
| 7 | 6600 | 6852 | 0.9807 | +259ch appended |
| 8 | 6407 | 7970 | 0.8907 | **+1571ch appended by the operator** |

**Not one character of Grok's output was altered.** Every divergence is either the operator
appending their own commentary *after* the pasted text or Grok's `<grok:render …citation_card…>`
markup being dropped by the clipboard. Three turns are byte-identical after whitespace
normalisation.

This is the one custody caveat that has actually been answered rather than merely narrowed: the
relay's fidelity was "operator-attested" this morning, and it is now measured, for the nine turns
the two captures overlap.

## 2. The meter claim is not in the native record either

The conversation **ends at 16:04:45Z with a complete assistant response**: `partial: false`,
`streamErrors: []`, on every node in the record. There is no truncation, no error, no limit
message, no timer.

The package's title claim — *metered epistemic foreclosure*, the free tier ending mid-repair —
therefore remains **entirely uncaptured after two exports**. The honest reading is that a
tier-limit notice is a client-side UI event and is not a conversation node, so this artifact may
be structurally incapable of carrying it. That is an explanation, not evidence. What can be said
is narrower and should now be said plainly: the operator's report at 16:47:26Z is the only record
of the exhaustion that exists, and the two best available exports do not corroborate it.

**This closes an open item in the negative.** Open item 1 was "capture the rate-limit event from
the Grok app." A native export has now been obtained and does not contain it. The remaining route
is a screen recording or xAI's server-side telemetry — i.e. the vendor's, which is what the vendor
notice asks for.

## 3. The model identifier does not match the other layers

Every assistant node in this record carries:

```
"model": "grok-3"
"metadata": {"request_metadata": {"model": "fast"}, ...}
```

Against the rest of the package:

| Layer | Identifier | Source |
|---|---|---|
| 1 — controlled API run | `x-ai/grok-4.20`, provider-pinned xAI | `run_manifest.json` provider preflight |
| 2 — consumer bridge (03:48–04:14Z) | "Grok 4.5 Fast", then "Grok free tier — default mode" | app-displayed, operator-recorded |
| **3 — the incident itself (06:00–16:04Z)** | **`grok-3`**, request mode `fast` | **vendor-served record** |

These do not agree, and the package treats the three layers as three surfaces of one system.

**Two readings, and this note does not choose between them.** Either `model` is a stale or coarse
internal field that grok.com emits regardless of the model actually serving the request, or the
free tier served a materially older model for the long-form conversation. The first is common in
production systems; the second would mean the sentinel trajectory was produced by a different
model generation than either the API baseline or the bridge captures — which would substantially
weaken every cross-layer inference in the package.

Either way, **the package can no longer describe its three layers as the same model without
addressing this field**, and only xAI can settle which reading is right. It is added to the vendor
notice's requested actions.

## 4. The Cyrano finding is corroborated from the Grok side — and my statement of it was too broad

The nine human turns in the native record are, verbatim, the composed analytic probes: formal,
structured, quoting Grok's own prior sentences back at it. Three of them (turns 4, 5, 6) match
ChatGPT assistant turns at **100% longest-common-run containment** — they are that text, unedited.

The other six do not appear verbatim anywhere in the ChatGPT share's *text* turns. That is not
evidence the operator wrote them: the ChatGPT share redacts **105 tool/canvas outputs**, and the
one screenshot in the package shows a probe being delivered through ChatGPT's "Writing" canvas.
All nine share one register, clearly distinct from the operator's dictated voice elsewhere in the
same session.

So the intake record's first statement — *"Every subsequent Grok-facing prompt in the sequence was
drafted by ChatGPT"* — **overstated what is shown**. Corrected: the arrangement is established by
the operator's own proposal and by three verbatim matches; per-prompt authorship of the remaining
six is consistent with ChatGPT composition and not demonstrated.

## 5. This is one of at least two conversations, and the load-bearing one is still missing

The record begins at 06:00:56Z with the destination-metaphor probe — **stage 5–6** of the
package's thirteen. The earlier material (the ecosystem answer, the evidentiary-burden extension,
the trans-policy collapse, the specificity-asymmetry audit, and **the operator's own pivot
correction at 04:47:22Z** — the turn the package identifies as the hinge) was relayed between
04:28Z and 05:36Z and belongs to a **different Grok conversation that has not been exported**.

So the strongest single moment in the incident — a human, in their own voice, naming the flattening
that both poles shared — still exists only as a relay. That conversation is now the store's highest
open capture.

## 6. One incidental datum

Grok ran a web search on **turn 0 only** (50 results, 6 inline citation cards; sources include a
Duke *differences* article, a trans-YA criticism piece, and several linguistics PDFs). The
remaining eight turns used no retrieval. Recorded because "the model searched once at the outset
and then reasoned from its own defaults for nine exchanges" is the kind of detail an
interaction-level audit would want, and because it is checkable in the record.

## What this note changes in the intake record

| Item | Before | After |
|---|---|---|
| Layer-3 custody | RELAY-HELD | **ORIGINAL-HELD** for the second conversation; RELAY-HELD for the first |
| Relay fidelity | operator-attested | **measured**: no alteration of Grok's text across 9 turns |
| Rate-limit event | not captured, capture pending | **not captured; the native export does not contain it** |
| Model identity | assumed uniform across layers | **conflicting identifiers, unresolved** |
| Cyrano attribution | "every prompt drafted by ChatGPT" | 3 of 9 verbatim; the rest consistent but not shown |
| Highest open capture | the trajectory | **the first Grok conversation**, which holds the operator's pivot |
