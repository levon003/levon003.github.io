#!/usr/bin/env python3
"""Scrape Bluesky likes and extract URLs, writing to _data/bsky_likes.yml."""

import argparse
import datetime
import logging
import os
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

import requests
import yaml
from atproto import Client
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

logger = logging.getLogger(__name__)

BSKY_INTERNAL_HOSTS = {"bsky.app", "staging.bsky.app", "go.bsky.app"}
# GIF/image CDN hosts that appear as link cards but are media, not articles
MEDIA_CDN_HOSTS = {
    "media.tenor.com", "c.tenor.com",
    "static.klipy.com",
    "media.giphy.com", "i.giphy.com",
    "pbs.twimg.com", "video.twimg.com",
    "link.mail.beehiiv.com",  # newsletter click-tracking URLs, not the article itself
}
REPO_ROOT = Path(__file__).parent.parent.parent
DEFAULT_OUTPUT = REPO_ROOT / "_data" / "bsky_likes.yml"

# Link shorteners we expand to their canonical destination so Citoid can enrich the
# real article (and same-target likes can dedupe). Best-effort: a failed resolve just
# leaves the shortener URL in place.
SHORTENER_HOSTS = frozenset([
    "bit.ly", "buff.ly", "tinyurl.com", "t.co", "ow.ly", "trib.al",
    "dlvr.it", "lnkd.in", "rb.gy", "cfl.re", "shar.es", "tiny.cc",
])
_BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

# Query params that are tracking noise, not part of the resource identity
_TRACKING_PARAMS = frozenset([
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "utm_id", "fbclid", "gclid", "msclkid", "twclid", "_ga", "ref",
    "triedRedirect", "r",
])


def normalize_url(url: str) -> str:
    """Lowercase scheme+host and strip common tracking query params."""
    try:
        parsed = urlparse(url)
        qs = {k: v for k, v in parse_qs(parsed.query, keep_blank_values=True).items()
              if k not in _TRACKING_PARAMS}
        clean_query = urlencode(qs, doseq=True)
        return urlunparse(parsed._replace(
            scheme=parsed.scheme.lower(),
            netloc=parsed.netloc.lower(),
            query=clean_query,
        ))
    except Exception:
        return url


def is_skip_link(url: str, card_title: str | None = None, card_description: str | None = None) -> bool:
    """Return True if this URL/card should be excluded."""
    try:
        netloc = urlparse(url).netloc.lower()
        if netloc in BSKY_INTERNAL_HOSTS:
            return True
        if netloc in MEDIA_CDN_HOSTS:
            return True
    except Exception:
        pass
    # Image cards have "ALT: ..." alt-text as their title/description
    if card_title and card_title.startswith("ALT:"):
        return True
    if card_description and card_description.startswith("ALT:"):
        return True
    return False


def is_shortener(url: str) -> bool:
    try:
        return urlparse(url).netloc.lower() in SHORTENER_HOSTS
    except Exception:
        return False


def resolve_shortener(url: str, session: requests.Session, cache: dict[str, str]) -> str:
    """Follow a shortener to its canonical URL (best-effort, cached).

    Returns the normalized destination URL, or the original URL unchanged on any
    failure or if the redirect never leaves a shortener domain.
    """
    if url in cache:
        return cache[url]
    resolved = url
    try:
        resp = session.get(url, timeout=10, allow_redirects=True, stream=True)
        resp.close()
        final = resp.url
        if final and urlparse(final).netloc.lower() not in SHORTENER_HOSTS:
            resolved = normalize_url(final)
    except Exception as e:
        logger.debug(f"Shortener resolve failed for {url}: {e}")
    cache[url] = resolved
    return resolved


def resolve_shortener_links(links: list[dict], session: requests.Session,
                            cache: dict[str, str]) -> int:
    """Rewrite shortener URLs in a link list to their canonical form in place,
    clearing now-stale enrichment and dropping any resulting duplicates.

    Returns the number of links rewritten.
    """
    changed = 0
    seen: set[str] = set()
    deduped: list[dict] = []
    for link in links:
        url = link["url"]
        if is_shortener(url):
            resolved = resolve_shortener(url, session, cache)
            if resolved != url:
                link["url"] = resolved
                link["citoid"] = None  # old metadata (if any) was for the shortener
                link.pop("dead", None)
                link.pop("archive_url", None)
                changed += 1
                logger.info(f"Resolved shortener {url} -> {resolved}")
        if link["url"] in seen:
            continue
        seen.add(link["url"])
        deduped.append(link)
    links[:] = deduped
    return changed


def extract_links_from_post(post) -> list[dict]:
    """Extract all links from a PostView, returning list of link dicts."""
    links = []
    seen_urls: set[str] = set()

    def add_link(url, source, card_title=None, card_description=None):
        if not url or is_skip_link(url, card_title, card_description):
            return
        normed = normalize_url(url)
        if normed in seen_urls:
            return
        seen_urls.add(normed)
        links.append({
            "url": normed,
            "source": source,
            "card_title": card_title,
            "card_description": card_description,
            "citoid": None,
        })

    embed = getattr(post, "embed", None)
    if embed is not None:
        _extract_from_embed(embed, add_link, source_prefix="")

    record = getattr(post, "record", None)
    if record is not None:
        for facet in (getattr(record, "facets", None) or []):
            for feature in (getattr(facet, "features", None) or []):
                uri = getattr(feature, "uri", None)
                if uri:
                    add_link(uri, "facet")

    return links


def _extract_from_embed(embed, add_link, source_prefix=""):
    # External link card
    if hasattr(embed, "external"):
        ext = embed.external
        uri = getattr(ext, "uri", None)
        if uri:
            source = f"{source_prefix}card" if source_prefix else "card"
            add_link(uri, source,
                     card_title=getattr(ext, "title", None),
                     card_description=getattr(ext, "description", None))

    # Quoted post (record without media, or record with media)
    if hasattr(embed, "record"):
        _extract_from_record_view(embed.record, add_link, source_prefix="quoted_")
        # If there's also media (recordWithMedia), recurse into it too
        if hasattr(embed, "media"):
            _extract_from_embed(embed.media, add_link, source_prefix=source_prefix)


def _extract_from_record_view(record_view, add_link, source_prefix="quoted_"):
    # The embedded record view wraps the actual post; unwrap one level if needed
    inner = getattr(record_view, "record", record_view)

    embed = getattr(inner, "embed", None)
    if embed is not None:
        _extract_from_embed(embed, add_link, source_prefix=source_prefix)

    # Facets in the quoted post's record text
    value = getattr(inner, "value", None) or getattr(inner, "record", None)
    if value is not None:
        for facet in (getattr(value, "facets", None) or []):
            for feature in (getattr(facet, "features", None) or []):
                uri = getattr(feature, "uri", None)
                if uri:
                    add_link(uri, f"{source_prefix}facet")


def _post_author_did(post) -> str | None:
    author = getattr(post, "author", None)
    return getattr(author, "did", None) if author else None


def fetch_thread_links(client: Client, post_uri: str, root_author_did: str,
                       existing_urls: set[str]) -> list[dict]:
    """Return thread links shared by the thread's root author only.

    Links posted by *other* accounts in the thread (replies, the parent of a reply I
    liked, etc.) are ignored — if I liked one of those posts it's captured as its own
    like entry and rendered on its own. Only the original author's contributions to
    their thread (ancestors and self-replies) are folded into this entry.
    """
    try:
        response = client.app.bsky.feed.get_post_thread(
            params={"uri": post_uri, "depth": 6, "parentHeight": 10}
        )
    except Exception as e:
        logger.warning(f"Failed to fetch thread for {post_uri}: {e}")
        return []

    thread = response.thread
    thread_links = []
    seen = set(existing_urls)

    def add_thread_link(url, source, card_title=None, card_description=None):
        if not url or is_skip_link(url, card_title, card_description):
            return
        normed = normalize_url(url)
        if normed in seen:
            return
        seen.add(normed)
        thread_links.append({
            "url": normed,
            "source": source,
            "card_title": card_title,
            "card_description": card_description,
            "citoid": None,
        })

    def consider(post):
        """Collect links from a post only if it was authored by the thread root author."""
        if post is None or _post_author_did(post) != root_author_did:
            return
        for link in extract_links_from_post(post):
            # A link sitting in a post quoted by the thread is "quoted", not the thread
            # author's own; preserve that distinction for the renderer.
            source = "quoted" if "quoted" in (link.get("source") or "") else "thread"
            add_thread_link(link["url"], source,
                            link.get("card_title"), link.get("card_description"))

    # Walk the parent chain up to the root.
    node = getattr(thread, "parent", None)
    while node is not None:
        consider(getattr(node, "post", None))
        node = getattr(node, "parent", None)

    # Walk down into replies (the root author's self-replies; others are filtered out).
    def walk_replies(node, depth):
        for reply in (getattr(node, "replies", None) or []):
            consider(getattr(reply, "post", None))
            if depth > 0:
                walk_replies(reply, depth - 1)

    walk_replies(thread, 5)

    return thread_links


def post_uri_to_url(uri: str) -> str:
    # at://did:plc:.../app.bsky.feed.post/rkey -> https://bsky.app/profile/{did}/post/{rkey}
    parts = uri.split("/")
    did = parts[2]
    rkey = parts[-1]
    return f"https://bsky.app/profile/{did}/post/{rkey}"


def get_thread_root_uri(post) -> str:
    """Return the AT URI of the thread root (post.uri if the post is itself the root)."""
    record = getattr(post, "record", None)
    reply = getattr(record, "reply", None) if record else None
    if reply is not None:
        root = getattr(reply, "root", None)
        if root is not None:
            root_uri = getattr(root, "uri", None)
            if root_uri:
                return root_uri
    return post.uri


def _merge_links(target: list[dict], source: list[dict]) -> list[dict]:
    """Merge source links into target, deduplicating by URL (prefer enriched entries)."""
    by_url: dict[str, dict] = {lnk["url"]: lnk for lnk in target}
    for link in source:
        url = link["url"]
        if url not in by_url:
            by_url[url] = link
        elif link.get("citoid") is not None and by_url[url].get("citoid") is None:
            by_url[url] = link  # prefer the enriched version
    return list(by_url.values())


def merge_thread_entries(likes: list[dict]) -> list[dict]:
    """Collapse liked posts from the same thread into single entries.

    Entries without thread_root_uri are emitted as-is. Order is preserved
    (each thread's position is set by its first appearance).
    """
    merged: list[dict] = []
    root_to_idx: dict[str, int] = {}

    for like in likes:
        root = like.get("thread_root_uri")

        if root is None or root not in root_to_idx:
            entry = dict(like)
            all_uris = list(dict.fromkeys([entry["post_uri"]] + (entry.get("all_post_uris") or [])))
            entry["all_post_uris"] = all_uris
            if root is not None:
                root_to_idx[root] = len(merged)
            merged.append(entry)
        else:
            entry = merged[root_to_idx[root]]
            # Union of all liked URIs
            existing_uris = entry.get("all_post_uris") or [entry["post_uri"]]
            for uri in (like.get("all_post_uris") or [like["post_uri"]]):
                if uri not in existing_uris:
                    existing_uris.append(uri)
            entry["all_post_uris"] = existing_uris
            # Use the most recent liked_at across all posts in the thread
            if (like.get("liked_at") or "") > (entry.get("liked_at") or ""):
                entry["liked_at"] = like["liked_at"]
            entry["links"] = _merge_links(entry.get("links") or [], like.get("links") or [])

    return merged


def backfill_thread_roots(client: Client, likes: list[dict]) -> list[dict]:
    """Populate thread_root_uri on entries that are missing it via batch getPosts calls."""
    to_fetch = [r["post_uri"] for r in likes if r.get("thread_root_uri") is None]
    if not to_fetch:
        logger.info("All entries already have thread_root_uri")
        return likes

    logger.info(f"Fetching thread roots for {len(to_fetch)} posts in batches of 25...")
    uri_to_root: dict[str, str] = {}

    for i in range(0, len(to_fetch), 25):
        batch = to_fetch[i:i + 25]
        try:
            response = client.app.bsky.feed.get_posts({"uris": batch})
            for post in response.posts:
                uri_to_root[post.uri] = get_thread_root_uri(post)
        except Exception as e:
            logger.warning(f"Batch {i // 25 + 1} failed: {e}")
        if (i // 25 + 1) % 20 == 0:
            logger.info(f"  {min(i + 25, len(to_fetch))}/{len(to_fetch)}")

    updated = 0
    for like in likes:
        if like.get("thread_root_uri") is None:
            uri = like["post_uri"]
            # Deleted/inaccessible posts: treat as their own thread root
            like["thread_root_uri"] = uri_to_root.get(uri, uri)
            updated += 1

    logger.info(f"Set thread_root_uri on {updated}/{len(to_fetch)} entries")
    return likes


def load_existing_likes(output_path: Path) -> tuple[list[dict], set[str]]:
    if not output_path.exists():
        return [], set()
    with output_path.open() as f:
        data = yaml.safe_load(f) or []
    known_uris: set[str] = set()
    for r in data:
        if "post_uri" in r:
            known_uris.add(r["post_uri"])
            known_uris.update(r.get("all_post_uris") or [])
    return data, known_uris


def tid_to_datetime(tid: str) -> str | None:
    """Decode an AT Protocol TID (base32-sortable) to an ISO 8601 UTC string.

    TID upper 53 bits = microseconds since Unix epoch.
    """
    try:
        # AT Proto TID uses a custom base32 alphabet: 234567abcdefghijklmnopqrstuvwxyz
        ALPHABET = "234567abcdefghijklmnopqrstuvwxyz"
        n = 0
        for ch in tid:
            n = n * 32 + ALPHABET.index(ch)
        microseconds = n >> 10  # upper 53 bits
        dt = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc) + datetime.timedelta(microseconds=microseconds)
        return dt.isoformat()
    except Exception:
        return None


def liked_at_from_viewer(post) -> str | None:
    """Extract actual like timestamp from post.viewer.like URI (rkey is a TID)."""
    try:
        viewer = getattr(post, "viewer", None)
        like_uri = getattr(viewer, "like", None)
        if not like_uri:
            return None
        rkey = like_uri.split("/")[-1]
        return tid_to_datetime(rkey)
    except Exception:
        return None


def to_str(val) -> str | None:
    """Coerce a potential datetime to string for YAML serialization."""
    if val is None:
        return None
    return str(val) if not isinstance(val, str) else val


def scrape_likes(handle: str, password: str, output_path: Path,
                 full_refresh: bool = False, max_pages: int | None = None):
    client = Client()
    client.login(handle, password)
    logger.info(f"Authenticated as {handle}")

    http_session = requests.Session()
    http_session.headers["User-Agent"] = _BROWSER_UA
    shortener_cache: dict[str, str] = {}

    existing_likes, known_uris = load_existing_likes(output_path)
    logger.info(f"{len(existing_likes)} existing likes, {len(known_uris)} known URIs")

    new_likes = []
    cursor = None
    stop_early = False
    page = 0

    while not stop_early:
        params = {"actor": handle, "limit": 100}
        if cursor:
            params["cursor"] = cursor

        response = client.app.bsky.feed.get_actor_likes(params=params)
        feed = response.feed
        if not feed:
            break

        page += 1
        logger.info(f"Page {page}: {len(feed)} likes")

        for feed_item in feed:
            post = feed_item.post
            post_uri = post.uri

            if not full_refresh and post_uri in known_uris:
                logger.info(f"Reached known post, stopping")
                stop_early = True
                break

            author = post.author
            record = getattr(post, "record", None)
            post_text = (getattr(record, "text", "") or "")[:280] if record else ""
            post_date = to_str(getattr(record, "created_at", None) if record else None) \
                or to_str(getattr(post, "indexed_at", None))

            thread_root_uri = get_thread_root_uri(post)

            links = extract_links_from_post(post)

            if not links:
                # The DID embedded in the root URI is the thread's original author.
                root_author_did = thread_root_uri.split("/")[2]
                thread_links = fetch_thread_links(client, post_uri, root_author_did, set())
                links.extend(thread_links)

            resolve_shortener_links(links, http_session, shortener_cache)

            clean_links = [
                {
                    "url": link["url"],
                    "source": link["source"],
                    "card_title": link.get("card_title"),
                    "card_description": link.get("card_description"),
                    "citoid": None,
                }
                for link in links
            ]

            liked_at = liked_at_from_viewer(post) or to_str(getattr(post, "indexed_at", None))

            new_likes.append({
                "post_uri": post_uri,
                "thread_root_uri": thread_root_uri,
                "post_url": post_uri_to_url(post_uri),
                "post_date": post_date,
                "liked_at": liked_at,
                "author_handle": getattr(author, "handle", ""),
                "author_did": getattr(author, "did", ""),
                "post_text": post_text,
                "links": clean_links,
            })

            logger.debug(f"  {post_uri}: {len(clean_links)} links")

        cursor = getattr(response, "cursor", None)
        if not cursor or (max_pages is not None and page >= max_pages):
            break

    logger.info(f"Scraped {len(new_likes)} new likes")

    # Merge new likes that are from the same thread (e.g. liked multiple posts in a thread)
    new_likes = merge_thread_entries(new_likes)

    # Cross-merge: if a new like belongs to a thread already in existing data, fold it in
    existing_by_root: dict[str, int] = {}
    for i, like in enumerate(existing_likes):
        root = like.get("thread_root_uri")
        if root:
            existing_by_root[root] = i

    standalone_new: list[dict] = []
    for new_like in new_likes:
        root = new_like.get("thread_root_uri")
        if root and root in existing_by_root:
            existing = existing_likes[existing_by_root[root]]
            all_uris = existing.get("all_post_uris") or [existing["post_uri"]]
            for uri in (new_like.get("all_post_uris") or [new_like["post_uri"]]):
                if uri not in all_uris:
                    all_uris.append(uri)
            existing["all_post_uris"] = all_uris
            if (new_like.get("liked_at") or "") > (existing.get("liked_at") or ""):
                existing["liked_at"] = new_like["liked_at"]
            existing["links"] = _merge_links(existing.get("links") or [], new_like.get("links") or [])
        else:
            standalone_new.append(new_like)

    all_likes = standalone_new + existing_likes
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w") as f:
        yaml.dump(all_likes, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    logger.info(f"Wrote {len(all_likes)} total likes to {output_path}")


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    parser = argparse.ArgumentParser(description="Scrape Bluesky likes and extract URLs")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--full-refresh", action="store_true",
                        help="Re-fetch all likes, ignoring existing data")
    parser.add_argument("--max-pages", type=int, default=None,
                        help="Stop after this many pages (for testing)")
    parser.add_argument("--backfill-threads", action="store_true",
                        help="Populate thread_root_uri on existing entries then merge same-thread likes")
    parser.add_argument("--resolve-shorteners", action="store_true",
                        help="Expand shortener URLs in existing entries to their canonical "
                             "form (clears their citoid so enrich.py re-fetches the real URL)")
    args = parser.parse_args()

    # Maintenance pass that doesn't need the Bluesky API (just HTTP redirects).
    if args.resolve_shorteners:
        likes, _ = load_existing_likes(args.output)
        session = requests.Session()
        session.headers["User-Agent"] = _BROWSER_UA
        cache: dict[str, str] = {}
        total = 0
        for like in likes:
            links = like.get("links")
            if links:
                total += resolve_shortener_links(links, session, cache)
        with args.output.open("w") as f:
            yaml.dump(likes, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        logger.info(f"Resolved {total} shortener links across {len(likes)} entries in {args.output}")
        return

    handle = os.environ.get("BSKY_HANDLE")
    password = os.environ.get("BSKY_APP_PASSWORD")
    if not handle or not password:
        print("BSKY_HANDLE and BSKY_APP_PASSWORD must be set", file=sys.stderr)
        sys.exit(1)

    if args.backfill_threads:
        client = Client()
        client.login(handle, password)
        likes, _ = load_existing_likes(args.output)
        likes = backfill_thread_roots(client, likes)
        likes = merge_thread_entries(likes)
        with args.output.open("w") as f:
            yaml.dump(likes, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        logger.info(f"Backfilled and merged → {len(likes)} entries in {args.output}")
        return

    scrape_likes(handle, password, args.output,
                 full_refresh=args.full_refresh, max_pages=args.max_pages)


if __name__ == "__main__":
    main()
