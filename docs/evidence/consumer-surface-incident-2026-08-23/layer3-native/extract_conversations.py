#!/usr/bin/env python3
"""Extract only the incident-relevant conversations from an xAI account export.

The operator's account export (`prod-grok-backend.json` inside the export ZIP)
holds their ENTIRE Grok account: 155 conversations and 2007 media posts, plus a
sibling `prod-mc-auth-mgmt-api.json` carrying email, legal name, date of birth,
and per-session IP address, city, latitude/longitude, and postal code. None of
that belongs in this repository. This script pulls out the conversations that
are part of the incident and nothing else.

It also strips account-identity fields wherever they appear -- on the
conversation header (`user_id`, `anon_user_id`, `x_user_id`, `team_id`,
`organization_id`) and nested in response metadata (`xai_user_id`) -- which is
why the committed subset is REDACTED-HELD rather than ORIGINAL-HELD. Everything
else (message text, timestamps, model, sender, parent/child ids) passes through
verbatim; nothing inside a message is altered. The scrub is asserted, not
assumed: the script fails loudly if any stripped key survives its own output.

Usage:
    unzip -j <export>.zip '*/prod-grok-backend.json' -d /tmp/exp
    python3 extract_conversations.py /tmp/exp/prod-grok-backend.json \
        > grok-account-export-incident-subset.json
"""

import json
import sys

# The two long-form conversations, identified by id so a retitle cannot change
# what this selects, plus the eight consumer-bridge captures that became Layer 2
# (selected by their capture window, since they are eight separate throwaways).
WANTED = {
    "aa3cb627-d610-455e-97b5-56f5f2055443",  # 1st long-form: ecosystem -> the pivot
    "aed7676d-7e08-4923-a453-20f8e696c986",  # 2nd long-form: destination metaphor -> records
}
BRIDGE_WINDOW = ("2026-08-23T03:47", "2026-08-23T04:21")

STRIP = ("user_id", "anon_user_id", "x_user_id", "team_id", "organization_id",
         "xai_user_id")


def scrub(obj):
    """Remove STRIP keys anywhere in the structure, however deeply nested."""
    if isinstance(obj, dict):
        return {k: scrub(v) for k, v in obj.items() if k not in STRIP}
    if isinstance(obj, list):
        return [scrub(v) for v in obj]
    return obj


def role_of(conv):
    if conv.get("id") in WANTED:
        return "long_form"
    created = conv.get("create_time") or ""
    if BRIDGE_WINDOW[0] <= created <= BRIDGE_WINDOW[1]:
        return "consumer_bridge"
    return None


def main(path):
    data = json.load(open(path, encoding="utf-8"))
    out = []
    for entry in data["conversations"]:
        conv = entry["conversation"]
        role = role_of(conv)
        if not role:
            continue
        header = scrub(conv)
        header["_incident_role"] = role
        header["_redacted_fields"] = list(STRIP)
        out.append({"conversation": header, "responses": scrub(entry["responses"])})

    out.sort(key=lambda e: e["conversation"].get("create_time") or "")
    payload = {
        "_source": "xAI account data export, prod-grok-backend.json",
        "_selection": "incident-relevant conversations only; the rest of the account is "
                      "deliberately not extracted",
        "_redaction": f"account-identity fields {list(STRIP)} removed wherever they appear, "
                      "header or nested metadata; everything else verbatim",
        "conversations": out,
    }

    rendered = json.dumps(payload, indent=1, ensure_ascii=False)
    for key in STRIP:
        marker = f'"{key}":'
        assert marker not in rendered, f"scrub failed: {key} survived into the output"
    sys.stdout.write(rendered + "\n")
    print(f"extracted {len(out)} conversations; scrub asserted clean", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
