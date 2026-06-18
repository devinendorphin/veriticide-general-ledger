"""
Twitter scraping via public guest-token GraphQL.
No API key required. Fragile — Twitter changes internals periodically.
Falls back gracefully if broken: returns empty list and prints a warning.
"""

import re
import time
import requests
from datetime import datetime, timezone

_GUEST_TOKEN_URL = "https://api.twitter.com/1.1/guest/activate.json"
_BEARER = (
    "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I6xULjWV"
    "lFYw%3DEALAAA0Z24IR3Vwyd0fQ6sCitDrNS8uFInsy6Dy9ngo"
)
_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def _get_guest_token(session: requests.Session) -> str | None:
    session.headers.update({
        "Authorization": f"Bearer {_BEARER}",
        "User-Agent": _UA,
    })
    try:
        resp = session.post(_GUEST_TOKEN_URL, timeout=10)
        resp.raise_for_status()
        return resp.json().get("guest_token")
    except Exception as e:
        print(f"  [twitter] could not obtain guest token: {e}")
        return None


def _user_tweets(session: requests.Session, handle: str, max_tweets: int) -> list[dict]:
    # Resolve user ID via username lookup
    url = (
        "https://twitter.com/i/api/graphql/"
        "G3KGOASz96M-Rd1XT40yOA/UserByScreenName"
    )
    params = {
        "variables": f'{{"screen_name":"{handle}","withSafetyModeUserFields":true}}',
        "features": (
            '{"hidden_profile_likes_enabled":false,'
            '"hidden_profile_subscriptions_enabled":false,'
            '"responsive_web_graphql_exclude_directive_enabled":true,'
            '"verified_phone_label_enabled":false,'
            '"subscriptions_verification_info_verified_since_enabled":true,'
            '"highlights_tweets_tab_ui_enabled":true,'
            '"creator_subscriptions_tweet_preview_api_enabled":true,'
            '"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,'
            '"responsive_web_graphql_timeline_navigation_enabled":true}'
        ),
    }
    try:
        r = session.get(url, params=params, timeout=15)
        r.raise_for_status()
        data = r.json()
        user = (
            data.get("data", {})
            .get("user", {})
            .get("result", {})
        )
        user_id = user.get("rest_id")
        if not user_id:
            print(f"  [twitter] could not resolve user id for @{handle}")
            return []
    except Exception as e:
        print(f"  [twitter] user lookup failed for @{handle}: {e}")
        return []

    # Fetch timeline
    tl_url = (
        "https://twitter.com/i/api/graphql/"
        "V7H0Ap3_Hh2FyS75OCDO3Q/UserTweets"
    )
    tl_params = {
        "variables": (
            f'{{"userId":"{user_id}",'
            f'"count":{max_tweets},'
            '"includePromotedContent":false,'
            '"withQuickPromoteEligibilityTweetFields":true,'
            '"withVoice":true,'
            '"withV2Timeline":true}}'
        ),
        "features": (
            '{"responsive_web_graphql_exclude_directive_enabled":true,'
            '"verified_phone_label_enabled":false,'
            '"creator_subscriptions_tweet_preview_api_enabled":true,'
            '"responsive_web_graphql_timeline_navigation_enabled":true,'
            '"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,'
            '"tweetypie_unmention_optimization_enabled":true,'
            '"responsive_web_edit_tweet_api_enabled":true,'
            '"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,'
            '"view_counts_everywhere_api_enabled":true,'
            '"longform_notetweets_consumption_enabled":true,'
            '"tweet_awards_web_tipping_enabled":false,'
            '"freedom_of_speech_not_reach_the_federation_enabled":true,'
            '"standardized_nudges_misinfo":true,'
            '"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":false,'
            '"longform_notetweets_rich_text_read_enabled":true,'
            '"longform_notetweets_inline_media_enabled":false,'
            '"responsive_web_enhance_cards_enabled":false}'
        ),
    }
    try:
        r = session.get(tl_url, params=tl_params, timeout=15)
        r.raise_for_status()
        return _parse_timeline(r.json(), handle)
    except Exception as e:
        print(f"  [twitter] timeline fetch failed for @{handle}: {e}")
        return []


def _parse_timeline(data: dict, handle: str) -> list[dict]:
    results = []
    try:
        instructions = (
            data["data"]["user"]["result"]["timeline_v2"]
            ["timeline"]["instructions"]
        )
        for instr in instructions:
            for entry in instr.get("entries", []):
                content = entry.get("content", {})
                item_content = content.get("itemContent", {})
                tweet_results = item_content.get("tweet_results", {}).get("result", {})
                legacy = tweet_results.get("legacy", {})
                text = legacy.get("full_text", "")
                tweet_id = legacy.get("id_str", "")
                created_at = legacy.get("created_at", "")
                if text and tweet_id:
                    results.append({
                        "handle": handle,
                        "tweet_id": tweet_id,
                        "text": text,
                        "created_at": created_at,
                        "url": f"https://twitter.com/{handle}/status/{tweet_id}",
                    })
    except (KeyError, TypeError):
        pass
    return results


def scrape_twitter(cfg: dict) -> list[dict]:
    accounts = cfg.get("accounts", [])
    keywords = [k.lower() for k in cfg.get("keywords", [])]
    max_tweets = cfg.get("max_tweets_per_account", 10)

    if not accounts:
        return []

    session = requests.Session()
    session.headers.update({
        "User-Agent": _UA,
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://twitter.com/",
        "x-twitter-active-user": "yes",
        "x-twitter-client-language": "en",
    })

    guest_token = _get_guest_token(session)
    if not guest_token:
        print("  [twitter] skipping — no guest token")
        return []

    session.headers.update({
        "x-guest-token": guest_token,
        "Authorization": f"Bearer {_BEARER}",
    })

    captured = []
    for handle in accounts:
        print(f"  [twitter] fetching @{handle} ...")
        tweets = _user_tweets(session, handle, max_tweets)
        for tweet in tweets:
            text_lower = tweet["text"].lower()
            if keywords and not any(kw in text_lower for kw in keywords):
                continue
            # Strip retweets if you only want original content:
            # if tweet["text"].startswith("RT @"):
            #     continue
            captured.append({
                "source_name": f"Twitter/@{handle}",
                "url": tweet["url"],
                "title": f"Tweet by @{handle}",
                "text": tweet["text"],
                "captured_at": datetime.now(timezone.utc).isoformat(),
                "capture_method": "Twitter public scrape",
                "tweet_meta": {
                    "handle": handle,
                    "tweet_id": tweet["tweet_id"],
                    "posted_at": tweet["created_at"],
                },
            })
        time.sleep(1.5)

    return captured
