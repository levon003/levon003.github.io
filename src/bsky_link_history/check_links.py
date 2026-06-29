#!/usr/bin/env python3
"""Liveness-check unresolved links in bsky_likes.yml and attach Internet Archive
fallbacks for genuinely dead ones.

Citoid returning a 404/blocked status does NOT mean a link is dead — paywalls and
bot-walls (FT, Bloomberg, ScienceDirect, Reddit, ...) 404 the Citoid scraper while
serving humans fine. So we only consider links that Citoid couldn't turn into real
metadata, then do an actual HTTP check from a browser-like client:

  - 2xx/3xx, or 401/403/429 (gated but present)  -> live, leave untouched
  - 404/410, DNS failure, SSL error, conn refused -> dead
  - 5xx / timeout                                 -> unknown, treated as live (transient)

For each dead link we query the Wayback availability API and, if a snapshot exists,
record `archive_url` (the closest capture). Dead links get `dead: true`; previously-dead
links that have come back to life have those fields removed.

Results are cached in liveness_cache.json so reruns are incremental.
"""

import argparse
import json
import logging
import time
from pathlib import Path
from urllib.parse import urlparse

import requests
import yaml

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).parent.parent.parent
DEFAULT_DATA = REPO_ROOT / "_data" / "bsky_likes.yml"
DEFAULT_CACHE = Path(__file__).parent / "liveness_cache.json"

WAYBACK_AVAILABLE = "https://archive.org/wayback/available"

# A real browser UA — many of these hosts block obvious bots, and we want to know
# whether a *human* can reach the page, not whether a scraper can.
BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

# Hosts where a "dead" verdict is meaningless or unarchivable: app deeplinks,
# auth-gated handles, form/chat endpoints. We skip liveness checks for these.
_SKIP_HOSTS = (
    "go.bsky.app",
    "forms.gle",
    "share.google",
    "images.app.goo.gl",
)
_SKIP_SUFFIXES = (".bsky.social",)

REQUEST_TIMEOUT = 12
MIN_INTERVAL = 0.2  # be polite; these are spread across many hosts


def load_cache(path: Path) -> dict:
    if path.exists():
        with path.open() as f:
            return json.load(f)
    return {}


def save_cache(cache: dict, path: Path) -> None:
    with path.open("w") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def is_resolved(link: dict) -> bool:
    """True if Citoid produced real metadata for this link (so it's live by definition)."""
    c = link.get("citoid")
    if not c:
        return False
    # Real results have a title and no failure status; failures carry only citoid_status.
    return c.get("citoid_status") in (None, "ok") and bool(c.get("title"))


def should_skip(url: str) -> bool:
    try:
        host = urlparse(url).netloc.lower()
    except Exception:
        return True
    if any(h in host for h in _SKIP_HOSTS):
        return True
    return any(host.endswith(s) for s in _SKIP_SUFFIXES)


def check_liveness(url: str, session: requests.Session) -> dict:
    """Return {'state': live|dead|unknown, 'status_code': int|None, 'reason': str}."""
    try:
        resp = session.get(
            url, timeout=REQUEST_TIMEOUT, allow_redirects=True, stream=True
        )
        resp.close()
        code = resp.status_code
    except requests.exceptions.SSLError:
        return {"state": "dead", "status_code": None, "reason": "ssl_error"}
    except requests.exceptions.ConnectionError:
        return {"state": "dead", "status_code": None, "reason": "connection_error"}
    except requests.exceptions.Timeout:
        return {"state": "unknown", "status_code": None, "reason": "timeout"}
    except requests.exceptions.RequestException as e:
        return {"state": "unknown", "status_code": None, "reason": str(e)[:80]}

    if code in (404, 410):
        return {"state": "dead", "status_code": code, "reason": "http_gone"}
    if 500 <= code < 600:
        return {"state": "unknown", "status_code": code, "reason": "server_error"}
    # 2xx, 3xx, and gated-but-present (401/403/429) all count as live.
    return {"state": "live", "status_code": code, "reason": "reachable"}


def lookup_wayback(url: str, session: requests.Session) -> str | None:
    """Return the closest Wayback snapshot URL (https), or None if not archived.

    The availability API is flaky under load, so retry a few times. A genuine
    "not archived" answer is a successful response with an empty snapshots object;
    that returns None without retrying further.
    """
    for attempt in range(3):
        try:
            resp = session.get(
                WAYBACK_AVAILABLE, params={"url": url}, timeout=REQUEST_TIMEOUT
            )
            resp.raise_for_status()
            data = resp.json()
        except (requests.RequestException, ValueError):
            time.sleep(1.0 * (attempt + 1))  # transient; back off and retry
            continue
        snap = (data.get("archived_snapshots") or {}).get("closest") or {}
        if not snap.get("available"):
            return None  # definitive: no snapshot exists
        snap_url = snap.get("url")
        if snap_url and snap_url.startswith("http://"):
            snap_url = "https://" + snap_url[len("http://"):]
        return snap_url or None
    return None  # exhausted retries


def refresh_archives(cache: dict, cache_path: Path) -> None:
    """Re-query Wayback for cached dead links that have no archive_url. The
    availability API is flaky, so a missing archive may just be a failed lookup."""
    targets = [u for u, v in cache.items()
               if v.get("state") == "dead" and not v.get("archive_url")]
    logger.info(f"Re-querying Wayback for {len(targets)} dead links without an archive")
    session = requests.Session()
    session.headers["User-Agent"] = BROWSER_UA
    found = 0
    for i, url in enumerate(targets):
        if i:
            time.sleep(1.0)  # space out availability-API calls; it rate-limits bursts
        archive = lookup_wayback(url, session)
        if archive:
            cache[url]["archive_url"] = archive
            found += 1
            logger.info(f"[{i+1}/{len(targets)}] archived: {url[:70]!r}")
        save_cache(cache, cache_path)
    logger.info(f"Newly archived: {found}/{len(targets)}")


def check_links(data_path: Path, cache_path: Path, limit: int | None,
                recheck: bool, refresh_archives_only: bool) -> None:
    with data_path.open() as f:
        likes = yaml.safe_load(f) or []

    cache = load_cache(cache_path)

    if refresh_archives_only:
        refresh_archives(cache, cache_path)
        # fall through to apply so YAML picks up the new archive_urls

    # Collect unique unresolved URLs (none when we're only refreshing archives).
    to_check: list[str] = []
    seen: set[str] = set()
    if not refresh_archives_only:
        for like in likes:
            for link in like.get("links", []):
                url = link["url"]
                if url in seen or is_resolved(link) or should_skip(url):
                    continue
                if url in cache and not recheck:
                    continue
                seen.add(url)
                to_check.append(url)

    if limit is not None:
        to_check = to_check[:limit]

    logger.info(f"Unresolved links to check: {len(to_check)} (cache has {len(cache)})")

    session = requests.Session()
    session.headers["User-Agent"] = BROWSER_UA
    wayback_session = requests.Session()
    wayback_session.headers["User-Agent"] = BROWSER_UA

    last_at = 0.0
    for i, url in enumerate(to_check):
        wait = MIN_INTERVAL - (time.monotonic() - last_at)
        if wait > 0:
            time.sleep(wait)
        last_at = time.monotonic()

        result = check_liveness(url, session)
        if result["state"] == "dead":
            result["archive_url"] = lookup_wayback(url, wayback_session)
            arch = "archived" if result["archive_url"] else "no archive"
            logger.info(f"[{i+1}/{len(to_check)}] DEAD ({result['reason']}, {arch}) {url[:70]!r}")
        else:
            logger.info(f"[{i+1}/{len(to_check)}] {result['state']} "
                        f"({result.get('status_code')}) {url[:70]!r}")
        cache[url] = result
        save_cache(cache, cache_path)

    # Apply cache to YAML: set/clear dead + archive_url on every unresolved link.
    dead = revived = 0
    for like in likes:
        for link in like.get("links", []):
            if is_resolved(link) or should_skip(link["url"]):
                continue
            entry = cache.get(link["url"])
            if entry is None:
                continue
            if entry["state"] == "dead":
                link["dead"] = True
                if entry.get("archive_url"):
                    link["archive_url"] = entry["archive_url"]
                else:
                    link.pop("archive_url", None)
                dead += 1
            else:
                # came back to life (or never dead) — clear any stale markers
                if link.pop("dead", None) is not None:
                    revived += 1
                link.pop("archive_url", None)

    logger.info(f"Marked dead: {dead} links ({revived} previously-dead now live)")

    with data_path.open("w") as f:
        yaml.dump(likes, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    logger.info(f"Wrote {data_path}")


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--limit", type=int, default=None,
                        help="Max number of links to check (for testing)")
    parser.add_argument("--recheck", action="store_true",
                        help="Re-check links even if already in the liveness cache")
    parser.add_argument("--refresh-archives", action="store_true",
                        help="Skip liveness checks; just re-query Wayback for cached dead "
                             "links missing an archive_url (the availability API is flaky)")
    args = parser.parse_args()
    check_links(args.data, args.cache, args.limit, args.recheck, args.refresh_archives)


if __name__ == "__main__":
    main()
