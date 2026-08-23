# CUSTODY INDEX — Consumer-surface incident, 2026-08-23 (ontological correction tax)

*Evidence store for `docs/consumer-surface-incident-2026-08-23-ontological-correction-tax.md`.*

> **This index governs custody state.** **VERDICT: DECLINED** — no account-level, vendor-level, or
> intent-level finding is entered against xAI, Anthropic, or any person. What is filed is a
> mechanism demonstration and a preservation/replication demand (Standing Protocol §7, step one).

**Intake:** 2026-08-23 · **Source:** operator-supplied package
`consumer_llm_ontological_correction_incident_v01` (v0.1), plus two operator-supplied captures added
later the same day · **Items:** 18 tracked in 3 layers · **States:** ORIGINAL-HELD 5,
SCREENSHOT-HELD 1, DERIVED 12 (7 analyst-derived) · **Not preserved:** the rate-limit event and the
first Grok conversation (see §NOT-PRESERVED)

> **Amended twice on 2026-08-23.** First the operator supplied the ChatGPT session behind the
> package (NOT-PRESERVED → **RELAY-HELD**), then grok.com's own record of the second of at least two
> Grok conversations (→ **ORIGINAL-HELD** for that conversation). The native record **measures** the
> relay as unaltered, and it **does not contain a rate-limit event** — so the package's title claim
> is uncaptured after two exports, and the first Grok conversation, which holds the operator's own
> pivot correction, is now the store's highest open capture.

The package is committed **verbatim** under `package/`. Nothing inside `package/` was edited,
reordered, renamed, or corrected on intake — including its terminology near-misses (see the intake
record's §Terminology). Analyst work sits outside it, under `reanalysis/`.

---

## Layer 1 — controlled baseline (CTTA-01.0)

| Item | Type | Role | Custody | sha256 |
|---|---|---|---|---|
| `package/evidence/original_uploads/ctta01_full_main.zip` | Run archive (16 files, 18.6 MB uncompressed) | The executed 768-call locked-graph domain-transfer run: `prompt_bank.jsonl`, `generations.jsonl` (every raw response), `endpoint_records.csv` (every prompt, response, parser outcome, score), `run_manifest.json`, `RUN_STATE.json`, and the five results CSVs. **The primary artifact of the whole package** — the only item from which its Layer-1 numbers can be independently re-derived. | ORIGINAL-HELD (operator-supplied; bytes committed in-repo) | `600decea06f4c753f4a932bd15fa73f90bab4f9714e684b29fd665745083cc2c` |
| `package/evidence/extracted_summaries/confirmatory_tests.csv` | Results extract | Grok confirmatory CER domain-divergence: 0.05859375, 95% CI [0.01953125, 0.09765625], exact p = 0.03515625, n = 16 pairs. Claude row: `not_estimable`. | DERIVED (from the zip, unchanged) | `0b557dc586e2a39821d55f313af50e109b30f3580603dc07a50c3e55614880c3` |
| `package/evidence/extracted_summaries/mechanism_tests.csv` | Results extract | The four Holm-family mechanism contrasts. Reveal effect: 0.0556640625, MC p = 0.01281, **Holm-adjusted 0.05123948760512395 — above 0.05**. The other three are null. Claude rows non-estimable. | DERIVED (from the zip, unchanged) | `a7318a83a1c7cc78e880c0d62e82f3d3e0fab275eb63ceab424944501ddb6a2c` |
| `package/evidence/extracted_summaries/channel_outcomes.csv` | Results extract | Channel-layer tally, kept separate from behavioral scores by design. Verified on intake: grok `ok` 384/384; claude `invalid_json` 376, `ok` 8. | DERIVED (from the zip, unchanged) | `51d92971aebf5904552a3870fa9d5539819c8a207328a5603413744c571a4fa3` |

**Independently checked on intake** (against the zip, not against the summaries): planned/terminal
calls 768; scoreable 392; channel failures 376; `actual_cost_usd` 10.9806743; temperature 0.2;
`max_tokens` 1100; reasoning disabled; `design_seed` 22082601; provider pins verified for both arms
(`x-ai/grok-4.20` → xAI; `anthropic/claude-opus-4.6` → Anthropic). Every figure the package states
for Layer 1 reproduces from the archive. **One attribution does not** — see `reanalysis/`.

## Layer 2 — free-tier consumer bridge

| Item | Type | Role | Custody | sha256 |
|---|---|---|---|---|
| `package/evidence/original_uploads/grok_app_bridge_free_tier_latest.zip` | Capture archive (4 files) | Eight manual captures from the Grok standalone consumer app, free tier, 2026-08-23 03:48–04:14 UTC: `frozen_prompt_packet.json` (the prompts, frozen before capture), `responses.jsonl`, `response_summary.csv`, `README_UPLOAD.txt`. | ORIGINAL-HELD (operator-supplied; bytes committed in-repo) | `d3b5f3283bec90832369bee51a22f780c7e750842a517344eb7a9a919ff56765` |
| `package/evidence/extracted_summaries/consumer_bridge_response_summary.csv` | Capture summary | 8/8 `INTEGRATIVE_INTERVENTION`; 8/8 edges retained; 8/8 graph checksums matched; **1 mapping-checksum mismatch** (`core_03_masked`); 0 decisiveness mismatches. First capture displayed "Grok 4.5 Fast", the other seven "Grok free tier — default mode". | DERIVED (from the zip, unchanged) | `c014c1417ee021360cb508c89d2555811124da4e491e858bdd71db040ca9a3ea` |

**Custody caveat, load-bearing.** These are **manual** captures from a phone app. There is no
canonical URL, no native export, no session ID, and no server-side attestation of the displayed
model or mode. The displayed-mode string is what the app rendered, as recorded by the operator.
This layer cannot exceed operator-attested custody by any procedure available to the operator, and
that is a property of the surface, not a to-do.

## Layer 3 — the long-form ecological incident

| Item | Type | Role | Custody | sha256 |
|---|---|---|---|---|
| `package/evidence/original_uploads/interaction_prompt_screenshot.jpg` | Screenshot (509×1536) | The **only** preserved primary artifact of the long-form conversation: one adaptive prompt removing the cooperative child–parent–clinician assumption, with the model's preceding turn and the app's interaction context visible. Checked on intake: no third-party handles, names, avatars, or faces; no private individual is identifiable. Nothing was redacted because nothing required it. | SCREENSHOT-HELD (operator-supplied) | `3bb70b8f788ac347b14a0b11133acafb2c57708ca87724346986a75b74943b34` |
| `package/EVIDENCE_EXCERPTS.md` | Reconstruction | The 13-stage conceptual sequence of the conversation, quoted from Grok outputs supplied during the surrounding research exchange. **Its own first section is a provenance warning** stating that it is a reconstruction, that exact prompts are omitted unless independently preserved, and that elapsed time / token totals / the native rate-limit message are absent and were not invented. | **DERIVED** — and the source it derives from is now in the store (`layer3-relay/`), so its selections are checkable rather than trusted. Still not a transcript; the relay governs on any conflict. | `065c7d2f2c1fd7316b41e1c96257796fa6c8d732a328eb24933248384f197320` |
| `layer3-relay/chatgpt-share-6a8b4330.html` | Captured web page | The operator-supplied ChatGPT share (`chatgpt.com/share/6a8b4330-…`, *"Analysis recovery patch"*, `gpt-5.6-sol-wm`, 213 messages, 2026-08-23 03:07:52Z–18:59:04Z). Carries **the long-form Grok outputs as pasted back by the operator** (25 relayed responses, 04:28:32Z–16:16:02Z), the ChatGPT-composed prompts that elicited them, the operator's own dictated diagnoses, the package's drafting turns, and the exchange logged as reception-register R-003. | **ORIGINAL-HELD** (third-party-hosted page, captured verbatim). **Not re-fetchable to this hash** — the page carries a per-response CSP nonce and the share URL is owner-revocable. | see `sha256.txt` |
| `layer3-relay/chatgpt-share-6a8b4330-transcript.md` | Decoded transcript | Ordered, timestamped, role-labelled transcript of the above. The readable Layer-3 artifact and the stable one. | DERIVED (re-derivable from the page by `decode_share.py`) | see `sha256.txt` |
| `layer3-relay/decode_share.py` | Decoder | Reassembles the share page's turbo-stream payload and resolves its index graph. Committed so the transcript is *derivable* from the captured bytes rather than asserted. | DERIVED (analyst-generated) | see `sha256.txt` |
| `layer3-relay/capture.json` | Capture record | Source URL, method, span, counterparty model slug, and the four stated limitations of a relayed capture. | DERIVED (analyst-generated) | see `sha256.txt` |

| `layer3-native/grok-share-aed7676d-native.json` | Vendor record | **grok.com's own record** of *"Journey Metaphor Flattens Gender Experiences"* (`aed7676d-…`, created 06:00:56.177538Z, modified 16:04:45.734Z): 9 exchanges, 18 nodes, each with a Grok-side `createTime`, `model`, `metadata`, `streamErrors`, and `partial` flag. Fetched from `rest/app-chat/share_links_data/<shareLinkId>` — the endpoint the share page's own JS bundle names; the page HTML is an SPA shell carrying no conversation content and is deliberately not committed. **The first vendor-served artifact in this store.** | **ORIGINAL-HELD** (vendor-served, captured verbatim) | see `sha256.txt` |
| `layer3-native/grok-share-aed7676d-transcript.md` | Rendered transcript | The record in reading order, each node stamped with its vendor timestamp, model, request mode, and any flags. | DERIVED (re-derivable by `render_transcript.py`) | see `sha256.txt` |
| `layer3-native/render_transcript.py` · `verify_relay_fidelity.py` | Tools | Renderer, and the comparison that measures the relay against the native record turn by turn. | DERIVED (analyst-generated) | see `sha256.txt` |
| `layer3-native/capture.json` · `NATIVE-RECORD-NOTE.md` | Capture record + findings | Source endpoint, span, model fields, privacy scan, four stated limitations; and the analyst reading — relay fidelity measured, no rate-limit event, the `grok-3` mismatch, the Cyrano correction, the missing first conversation. | DERIVED (analyst-generated) | see `sha256.txt` |

**What the native record settles, and what it kills.** (a) **Relay fidelity is now measured, not
attested:** three of nine assistant turns byte-identical after whitespace normalisation, the rest
0.98–0.99; every divergence is operator commentary appended *after* the paste (+1457, +1571, +259
chars) or Grok's inline citation-card markup lost to the clipboard (−425). **No alteration of
Grok's text.** (b) **No rate-limit event:** the record ends 16:04:45Z with a complete response,
`partial: false`, `streamErrors: []` throughout. (c) **Model mismatch:** `model: "grok-3"`,
`request_metadata.model: "fast"` — against "Grok 4.5 Fast" displayed in the Layer-2 captures two
hours earlier and `x-ai/grok-4.20` pinned in Layer 1. Recorded, unresolved, and only xAI can settle
it. (d) **Retrieval:** Grok web-searched on turn 0 only (50 results, 6 citation cards); the other
eight exchanges used none. (e) **Privacy scan:** no emails, user ids, handles, author names, or long
numeric ids anywhere in the record; grok.com itself flags the share `isPublic: true`,
`allowIndexing: true`.

**Custody caveats on the relay, load-bearing.** The chain is Grok app → operator copy-paste →
ChatGPT. There is **no Grok-side timestamp, no session id, no displayed model/mode attestation, no
native metadata, and no rate-limit message**. The timestamps are ChatGPT-side *receipt* times and
bound the true times from above only. Whether every response was pasted complete and unedited is
operator-attested. RELAY-HELD is therefore a real improvement on NOT-PRESERVED and is not an export.

**Disclosure the relay establishes, as corrected by the native record.** The operator proposed at
04:26:44Z that ChatGPT compose the Grok-facing probes — an arrangement `package/INCIDENT_REPORT.md`
does not disclose. **Three of the nine** probes in the native record are verbatim ChatGPT text; the
other six do not appear in the relay's text turns, but the relay redacts 105 tool/canvas outputs and
all nine share one composed register distinct from the operator's dictated voice. So the arrangement
is established and per-prompt authorship of six is not. The substantive diagnoses are the operator's
own (the pivot at 04:47:22Z). See the intake record's §The disclosure the package omits.

## Synthesis and instrument documents (operator-supplied, part of the package)

| Item | Role | Custody | sha256 |
|---|---|---|---|
| `package/INCIDENT_REPORT.md` | The causal account: the correction→accommodation→boundary-reversion→depletion→closure mechanism, the three-layer evidence structure, burden allocation, severity, disposition. | ORIGINAL-HELD (as supplied) | `2dd327b22ec49cad763b221d756673a762faedd5bd6f3450c6f7b037fde59d6e` |
| `package/CLAIMS_AND_LIMITS.md` | The package's own boundary statement — four bands: directly supported / strong inferences / hypotheses requiring replication / claims not made. | ORIGINAL-HELD (as supplied) | `72e84cdc96b3bafe61fbcdba37e882ff7a14a928b457480b11167e5ebbff69e7` |
| `package/INTERACTION_AUDIT_PROTOCOL.md` | The reproducible instrument: eight measures (OCC, EPI, CRR, ORR, BTR, TNC, MC, NRG), branch procedure, surface matrix, participation terms, minimum incident threshold. | ORIGINAL-HELD (as supplied) | `9e95aa43f76821add95eed10f6f5bd6c1a79ba4b488a2566770e958c18e8932e` |
| `package/VENDOR_NOTICE.md` | Notice and eight requested corrective actions, with burden allocation. **Not yet sent** — see the intake record §Disposition. | ORIGINAL-HELD (as supplied) | `3e1196324d23400abb9aeedb3b38e5f0d8c0916ccebb9172ac911cdf7c077db5` |
| `package/PUBLIC_SUMMARY.md` | Public-facing description; carries the demand line ("Stop making marginalized users purchase enough context to become legible"). | ORIGINAL-HELD (as supplied) | `126a1a8d3a81c984399c2a7b62138735ca4e226d56e01be911a9327b30915ae7` |
| `package/README.md` | Package orientation, evidence-layer separation, core terminology. | ORIGINAL-HELD (as supplied) | `fb021380b16bd3e723e9a0f4d4c22c0f4b38c89f857adaf8f832cc9e176b3f72` |
| `package/REFERENCES.md` | Nine adjacent sources, with an explicit statement that none individually establishes the incident claim. Locators **not** independently checked on intake. | ORIGINAL-HELD (as supplied) | `d9ce5ace8e9fa088dcb7535ae2edb6593b5133d283ef890dd61bb4e7cfe62ca2` |
| `package/EVIDENCE_INDEX.csv` | The package's own item-level provenance table (E01–E09), each row carrying its limitations. | ORIGINAL-HELD (as supplied) | `8bffda3d687b25b735ad171a5130e4300227a70af108972363f9dd34938484b1` |
| `package/SHA256SUMS.txt` | The package's own 16-file integrity record. **Verified complete and passing on intake** (`sha256sum -c` → 16/16 OK). | ORIGINAL-HELD (as supplied) | `e2a31136c90335846270328c7fd351971dee94dd7fc3544fb015a1638440f075` |

## Analyst-derived (outside the package)

| Item | Role | Custody | sha256 |
|---|---|---|---|
| `reanalysis/recover_claude_arm.py` | Strips the fence, re-parses, reports the decisive-edge and premise-objection heterogeneity, derives and **validates** the CER rule against all 384 scored Grok rows, then rebuilds the pre-registered confirmatory endpoint for both arms. Reproduces every number in the note offline, no network, no API calls. | DERIVED (analyst-generated, from the Layer-1 zip) | see `sha256.txt` |
| `reanalysis/RECOVERY-NOTE.md` (v0.2) | The findings: (a) the Claude arm's 376 "channel failures" are fenced-but-valid JSON returned `ok`/`stop`, recovering 376/376 for USD 0.00 against the USD 10.0687 (91.7% of the run) they already cost; (b) the fence violated an **explicit** "no code fence" instruction present in all 768 prompts — Claude 8/384 compliant, Grok 384/384 — so the data loss was the harness's and the non-compliance was Claude's; (c) re-scored under a CER rule validated against the harness's own Grok output on all 384 rows, the **Claude confirmatory endpoint is an exact null** (0.0, all 16 pairs zero); (d) Grok's significant result is **positive in the direction of better preservation on the trans-policy skin** (0.9219 vs 0.8633). Carries its own reflexivity declaration and records the two corrections a cross-vendor check made to v0.1. | DERIVED (analyst-generated) | see `sha256.txt` |

## NOT-PRESERVED (capture required; upgrade blocked until then)

| Item | Why it matters | Required capture | Recoverable? |
|---|---|---|---|
| **The first Grok conversation** (relayed 04:28–05:36Z) | It holds the trans-policy collapse, the specificity-asymmetry audit, and **the operator's own pivot correction at 04:47:22Z** — the human turn the incident hinges on. It exists only as relay, and its fidelity is the one the native record could not measure. | A grok.com share of that conversation, captured the same way as `layer3-native/` | **Yes, and cheaply** — if the conversation still exists in the operator's account. Now the store's highest-value open capture. |
| **The rate-limit event** | The package's title claim. | Screen recording of the limit message with its timestamp, or xAI's server-side telemetry | **Not by export.** See below. |
| **Which model served `aed7676d-…`** | Decides whether the package's three layers describe one system or three. | xAI's answer; a one-line disclosure | Vendor-only. Added to the vendor notice. |
| *(closed 2026-08-23)* ~~The long-form conversation text~~ | — | — | **Closed by the two captures.** Second conversation ORIGINAL-HELD; first RELAY-HELD. |
| *(closed in the negative 2026-08-23)* ~~Native export carrying the rate-limit event~~ | — | — | **Obtained and does not contain it.** The record ends with a complete response, no truncation, no error. A tier-limit notice is a client-side UI event and is not a conversation node — an explanation, not evidence. |

*Status:* **NOT-PRESERVED.** Per the repo's standing rule (Track F, TF-003), an item with no capture
is filed with explicit caveats and takes no upgrade until original-form capture is complete. The
sentinel classification in the intake record is entered **with this gap on its face**, not around it.

## Custody states used

- **ORIGINAL-HELD (operator-supplied)** — the artifact as the operator produced or exported it,
  byte-preserved and hashed. Unusually for this repo, the bytes themselves are committed (the
  originals total ~950 KB, so the `.gitignore` binary exclusion that keeps other stores hash-only
  did not need to apply). That gives this store a real second custodian for the bytes, which the
  older stores lack.
- **SCREENSHOT-HELD** — operator-supplied screenshot with no canonical URL and no original-form
  bytes behind it (the state the CTF-1 corpus established).
- **DERIVED** — extracted or generated from another item in the store; the parent governs on any
  conflict. `EVIDENCE_EXCERPTS.md` is the hard case: derived from a source that is **not in the
  store and not preserved anywhere**, which is why it is marked separately above.
- **RELAY-HELD** — the content exists as a contemporaneous copy-paste relay into a third-party
  system, captured and hashed here, with the originating system's own metadata absent. Weaker than
  ORIGINAL-HELD (no native export, no source-side attestation) and stronger than a reconstruction
  (the text is fixed, ordered, and timestamped on the receiving side). Introduced for this store
  because none of the existing states describes it honestly; it is a description of what is held,
  not a promotion path. **Its one live demonstration:** where a native counterpart exists, the relay
  reproduced the source text without alteration — which is evidence about *this* relay over nine
  turns, not a general warrant for the state.
- **NOT-PRESERVED** — known artifact, no capture.

## Why this store is not VERIFIED

Per `docs/custody-status-2026-07-02.md`, `VERIFIED` requires hashed originals **plus** an
off-platform second custodian **plus** confirmation the capture holds real source content. Two of
the three hold here: the originals are hashed and the bytes are committed, and Layers 1–2 hold real
content (checked against the archives, not merely against the summaries). What is missing is an
off-platform second custodian for the byte copies — newly urgent, since **both** Layer-3 sources are
revocable third-party URLs and the grok.com endpoint may stop resolving without notice.
**Store state: HASHED-PENDING-BACKUP for Layers 1–2; SCREENSHOT-HELD + ORIGINAL-HELD (second Grok
conversation) + RELAY-HELD (first) for Layer 3.** The second conversation now has vendor-side
attestation; the first does not, and the promotion path for it is the same share-and-capture route
that produced `layer3-native/`.

## Verify

```bash
# from docs/evidence/consumer-surface-incident-2026-08-23/
sha256sum -c sha256.txt                     # this store
cd package && sha256sum -c SHA256SUMS.txt   # the package's own record, 16 files

# reproduce the Claude-arm recovery and re-score (no API calls, no network)
unzip -q -d /tmp/ctta package/evidence/original_uploads/ctta01_full_main.zip
python3 reanalysis/recover_claude_arm.py /tmp/ctta/ctta01_full_main

# re-derive the Layer-3 relay transcript from the captured page
python3 layer3-relay/decode_share.py layer3-relay/chatgpt-share-6a8b4330.html | diff - layer3-relay/chatgpt-share-6a8b4330-transcript.md

# re-render the native record, and re-measure the relay against it
cd layer3-native
python3 render_transcript.py grok-share-aed7676d-native.json | diff - grok-share-aed7676d-transcript.md
python3 verify_relay_fidelity.py grok-share-aed7676d-native.json \
    ../layer3-relay/chatgpt-share-6a8b4330-transcript.md
```
