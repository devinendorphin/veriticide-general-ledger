# AGENTS.md — veriticide-general-ledger

## Scope and authority

This file is Codex's entry point. It does not replace `CLAUDE.md` or the repository's canonical instruments.

Before substantive work, read `CLAUDE.md`, `ledger/ledger.md`, the relevant documents in `docs/`, and the target case's full packet. Convention Articles II and IV are the legal spine; subordinate taxonomies and instruments must cite and correct to that spine. The per-item custody index in each evidence store governs custody status.

## Evidentiary discipline

- Use the existing classifications, laundering moves, tier taxonomy, evidence bands, and case grammar. Do not invent or silently merge tags.
- The case files are the deliverable; `ledger/ledger.md` remains their source-of-record archive.
- Preserve original evidence bytes. Keep originals, transcripts, analyses, and other derivatives distinct; verify hashes before and after any evidence-handling change.
- Use custody states exactly as defined. A locator, a hash, or a repository copy is not automatically independent verification. Never promote an item to `VERIFIED` without the required external custody evidence.
- Preserve counter-evidence, nulls, adverse facts, failed captures, and provenance gaps. State who controls missing evidence.
- Every analytic entry needs a `BOUNDARY` stating what it establishes and what it does not establish alone. Case work also requires an adversarial check and falsification conditions.
- Stay at step one: preservation, disclosure, audit, inquiry, and standing. Do not convert a documented basis for inquiry into a finding of guilt.
- Structural identity is not evidence of coordination. Separate mechanism, function, and intention.
- Apply the Reflexivity Clause to the analyst and the model. A concession or self-critique is not a substitute for correction.
- Never restore redacted private identifiers or unredacted assets. Do not attempt history or GitHub PR-ref rewriting without a separately authorized remediation plan.

## Change and review workflow

- Work on a `codex/<task>` branch and open a draft pull request. Do not push directly to `main`, enable auto-merge, file externally, or merge without Endorphin's explicit instruction for that specific action.
- Keep imported evidence byte-preserved and put new analysis in clearly labeled derivative files.
- Validate affected hashes, manifests, custody indexes, internal links, and the case packet's required sections. Record any check that cannot be run.
- Mark uncertain speech-to-text repairs as `[?original→guess]`; never silently guess Endorphin's wording.
- End each task with a ledger of evidence received, files changed, hashes or checks performed, custody-state effects, counter-evidence preserved, and remaining uncertainty.

## Code review rules

Flag overstated custody, missing boundaries, unsupported intention claims, self-sealing inferences, hidden counter-evidence, silent taxonomy changes, step-two language, privacy regressions, and any change that makes the issuer the sole validator.
