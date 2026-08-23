#!/usr/bin/env python3
"""Render the native grok.com share record into an ordered transcript.

The share page at grok.com/share/<shareLinkId> is an SPA shell: the conversation
is not in its HTML. The record is served by

    GET https://grok.com/rest/app-chat/share_links_data/<shareLinkId>

which returns the conversation object plus every response node with Grok-side
`createTime`, `model`, `metadata`, `streamErrors`, and `partial` flags. That JSON
is the primary artifact; this script only renders it.

Usage:
    python3 render_transcript.py grok-share-aed7676d-native.json > transcript.md
"""

import json
import sys


def main(path: str) -> int:
    data = json.load(open(path, encoding="utf-8"))
    conv = data["conversation"]

    print(f"# {conv['title']}")
    print()
    print(f"- conversationId: `{conv['conversationId']}`")
    print(f"- created: `{conv['createTime']}` · last modified: `{conv['modifyTime']}`")
    print(f"- exchanges: {len(data['responses']) // 2}")
    print()

    for i, node in enumerate(data["responses"]):
        model = node.get("model") or ""
        req = ((node.get("metadata") or {}).get("request_metadata") or {}).get("model", "")
        flags = []
        if node.get("partial"):
            flags.append("PARTIAL")
        if node.get("streamErrors"):
            flags.append(f"streamErrors={node['streamErrors']}")
        if node.get("webSearchResults"):
            flags.append(f"webSearchResults={len(node['webSearchResults'])}")
        tail = (f" · model `{model}`" if model else "") + \
               (f" · request mode `{req}`" if req else "") + \
               ("  **" + ", ".join(flags) + "**" if flags else "")
        print(f"\n## [{i}] {node['sender']} · {node['createTime']}{tail}\n")
        print(node["message"])

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
