#!/usr/bin/env python3
"""Enrich bsky_likes.yml with Citoid metadata.

Citoid is a Wikimedia service that converts URLs to citation metadata.
API docs: https://www.mediawiki.org/wiki/Citoid
Rate limit: self-enforced at 200 requests/minute per Wikimedia guidance for
User-Agent-only callers (no OAuth).
"""

import argparse
import json
import logging
import re
import time
from pathlib import Path
from urllib.parse import quote, urlparse

import requests
import yaml

logger = logging.getLogger(__name__)

CITOID_BASE = "https://en.wikipedia.org/api/rest_v1/data/citation/zotero/"
USER_AGENT = (
    "bsky-link-history/0.1 "
    "(https://levon003.github.io; zachary.levonian@gmail.com) "
    "requests/2.32"
)
MIN_INTERVAL = 60.0 / 200  # 200 req/min -> 0.30s between requests

REPO_ROOT = Path(__file__).parent.parent.parent
DEFAULT_DATA = REPO_ROOT / "_data" / "bsky_likes.yml"
DEFAULT_CACHE = Path(__file__).parent / "citoid_cache.json"


def load_cache(cache_path: Path) -> dict:
    if cache_path.exists():
        with cache_path.open() as f:
            return json.load(f)
    return {}


def save_cache(cache: dict, cache_path: Path) -> None:
    with cache_path.open("w") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def parse_zotero_item(item: dict) -> dict:
    """Parse a raw Zotero item dict into our normalized citoid schema."""
    # Citoid Zotero format uses `creators` with firstName/lastName/creatorType,
    # not the `author` array with first/last used by the Zotero client API.
    creators = item.get("creators", [])
    authors = []
    for c in creators:
        if not isinstance(c, dict):
            continue
        if c.get("creatorType") not in ("author", None):
            continue  # skip editors, translators, etc.
        if c.get("literal"):
            authors.append({"literal": c["literal"]})
        elif c.get("lastName") or c.get("firstName"):
            entry = {}
            if c.get("lastName"):
                entry["last"] = c["lastName"]
            if c.get("firstName"):
                entry["first"] = c["firstName"]
            authors.append(entry)

    publisher = (
        item.get("publicationTitle")
        or item.get("publisher")
        or item.get("websiteName")
        or item.get("blogTitle")
        or item.get("institution")
        or item.get("repository")
    )
    return {
        "title": item.get("title") or None,
        "authors": authors or None,
        "date": item.get("date") or None,
        "item_type": item.get("itemType") or None,
        "doi": item.get("DOI") or None,
        "publisher": publisher or None,
        "abstract": item.get("abstractNote") or None,
    }


# OSF preprint server name → DOI prefix (10.XXXXX). "osf" is the generic server.
_OSF_SERVER_PREFIX: dict[str, str] = {
    "osf": "10.31219",
    "psyarxiv": "10.31234",
    "socarxiv": "10.31235",
    "metaarxiv": "10.31222",
    "edarxiv": "10.35542",
    "engrxiv": "10.31224",
    "eartharxiv": "10.31223",
    "africarxiv": "10.31730",
    "indiarxiv": "10.31221",
    "lawarxiv": "10.31228",
    "mindrxiv": "10.31236",
    "paleorxiv": "10.31233",
}

# Titles Citoid returns when it actually hit a bot-wall, JS gate, or generic
# landing page rather than the real content. Treated as fetch failures.
_GENERIC_TITLE_EXACT: set[str] = {
    "osf",
    "404 page not found",
    "page not found",
    "client challenge",
    "tiktok - make your day",  # og:site_name leaks in; the bsky card has the real title
}
_GENERIC_TITLE_FRAGMENTS: tuple[str, ...] = (
    "please wait for verification",
    "just a moment",
    "attention required",
    "are you a robot",
    "not a robot",
    "not a bot",
    "enable javascript",
    "captcha",
    "access denied",
    "before you continue",
    "verify you are human",
)


def is_generic_title(title: str | None) -> bool:
    """True if the title looks like a bot-wall / JS-gate / generic landing page."""
    t = (title or "").strip().lower()
    if not t:
        return True
    if t in _GENERIC_TITLE_EXACT:
        return True
    return any(frag in t for frag in _GENERIC_TITLE_FRAGMENTS)


def _osf_doi_candidates(doi: str) -> list[str]:
    """OSF DOIs are version-specific. Given a (possibly versioned) OSF DOI, return
    ordered candidates to try: the explicit version, then _v1, then the bare form."""
    base = re.sub(r"_v\d+$", "", doi, flags=re.IGNORECASE)
    candidates = []
    if base != doi:
        candidates.append(doi)  # the version the URL actually named
    candidates.append(f"{base}_v1")  # most OSF preprints have a v1
    candidates.append(base)  # bare form (rarely resolves, but cheap to try)
    seen: set[str] = set()
    return [c for c in candidates if not (c in seen or seen.add(c))]


def doi_candidates(url: str) -> list[str]:
    """Return an ordered list of DOI strings to try against Citoid for this URL.

    Empty if no DOI can be derived. Handles:
      doi.org/10.x...                            (bare DOI in path)
      osf.io/preprints/{server}/{id}             (version-aware OSF DOIs)
      arxiv.org/{abs,pdf,html}/{id}              (-> 10.48550/arXiv.{id})
      dl.acm.org/doi/10.1145/... (+ abs/pdf/epdf/full)
      academic.oup.com/.../doi/10.1093/.../<id>  (strips trailing OUP numeric ID)
      Any URL with /doi/10. in the path
    """
    try:
        parsed = urlparse(url)
        path = parsed.path
        netloc = parsed.netloc.lower()
    except Exception:
        return []

    # doi.org / dx.doi.org: the DOI is the path itself
    if netloc in ("doi.org", "dx.doi.org"):
        doi = path.lstrip("/").rstrip("/")
        if not doi.startswith("10."):
            return []
        return _osf_doi_candidates(doi) if "osf.io/" in doi else [doi]

    # OSF preprints: osf.io/preprints/{server}/{id} → {prefix}/osf.io/{id}
    if netloc == "osf.io":
        m = re.match(r"^/preprints/([^/]+)/([^/?]+)", path, re.IGNORECASE)
        if m:
            server = m.group(1).lower()
            preprint_id = m.group(2)
            prefix = _OSF_SERVER_PREFIX.get(server)
            if prefix:
                return _osf_doi_candidates(f"{prefix}/osf.io/{preprint_id}")
        return []  # other osf.io paths (project pages, files) have no derivable DOI

    # arXiv: arxiv.org/{abs,pdf,html}/{id} -> DataCite DOI 10.48550/arXiv.{id}.
    # Citoid 415s on the PDF/HTML URLs but resolves the DOI to full metadata.
    if netloc.endswith("arxiv.org"):
        # Modern /abs/, /pdf/, /html/ paths and the legacy /ftp/.../papers/.../{id}.pdf form.
        m = re.match(r"^/(?:abs|pdf|html)/(.+)$", path, re.IGNORECASE)
        if not m:
            m = re.search(r"/papers/[^/]+/([^/]+?)(?:\.pdf)?$", path, re.IGNORECASE)
        if m:
            arxiv_id = m.group(1).rstrip("/")
            arxiv_id = re.sub(r"\.pdf$", "", arxiv_id, flags=re.IGNORECASE)
            arxiv_id = re.sub(r"v\d+$", "", arxiv_id)  # the base DOI resolves; drop version
            if arxiv_id:
                return [f"10.48550/arXiv.{arxiv_id}"]
        return []

    # General /doi/ pattern used by ACM, OUP, and many journal sites
    doi_pos = path.lower().find("/doi/")
    if doi_pos == -1:
        return []

    after_doi = path[doi_pos + 5:]  # everything after /doi/
    for prefix in ("abs/", "pdf/", "epdf/", "full/"):
        if after_doi.lower().startswith(prefix):
            after_doi = after_doi[len(prefix):]
            break

    if not after_doi.startswith("10."):
        return []

    doi = after_doi.rstrip("/")

    # OUP appends a numeric internal article ID after the real DOI
    # e.g. /doi/10.1093/bioinformatics/btaa1059/6050106 → strip /6050106
    if "oup.com" in netloc:
        doi = re.sub(r"/\d+$", "", doi)

    return [doi] if doi else []


def _call_citoid(citoid_target: str, session: requests.Session) -> list:
    """Make a single Citoid API call; raises HTTPError on 4xx/5xx."""
    api_url = CITOID_BASE + quote(citoid_target, safe="")
    resp = session.get(api_url, timeout=15)
    resp.raise_for_status()
    return resp.json()


def fetch_citoid(url: str, session: requests.Session) -> dict:
    """Fetch Zotero metadata from Citoid. Returns a dict with citoid_status + raw item.

    Tries any DOIs derivable from the URL first (Citoid resolves DOIs natively and
    publishers like ACM block direct URL scraping), then falls back to the raw URL.
    A result whose title looks like a bot-wall / generic landing page is rejected: we
    keep trying remaining candidates, and if only the bare URL yields one we return
    citoid_status="blocked" rather than storing the junk title.
    """
    targets = doi_candidates(url) + [url]
    last_idx = len(targets) - 1
    blocked_title: str | None = None

    for i, target in enumerate(targets):
        is_url = i == last_idx  # the final fallback is the raw URL
        try:
            items = _call_citoid(target, session)
        except requests.HTTPError as e:
            if is_url:
                raise  # exhausted DOIs; surface the URL's HTTP error
            if e.response.status_code in (400, 403, 404, 410, 415):
                continue  # this DOI candidate didn't resolve; try the next
            raise

        if not items:
            continue

        item = items[0]
        parsed = parse_zotero_item(item)
        if is_generic_title(parsed.get("title")):
            blocked_title = (parsed.get("title") or "").strip()
            continue  # bot-wall / landing page; try the next candidate

        return {"citoid_status": "ok", "raw": item, **parsed}

    if blocked_title is not None:
        return {"citoid_status": "blocked", "title": blocked_title}
    return {"citoid_status": "empty"}


def reparse_cache(cache: dict) -> int:
    """Re-parse all cached raw Zotero items using current parse_zotero_item logic."""
    updated = 0
    for url, entry in cache.items():
        if entry.get("citoid_status") != "ok" or "raw" not in entry:
            continue
        parsed = parse_zotero_item(entry["raw"])
        entry.update(parsed)
        updated += 1
    return updated


def _citoid_is_generic(d: dict | None) -> bool:
    """True if a citoid dict (applied YAML entry or cache entry) is a generic /
    bot-wall result — explicitly 'blocked' status, or an ok result whose title
    looks like a landing page."""
    if not d:
        return False
    if d.get("citoid_status") == "blocked":
        return True
    if d.get("citoid_status") in (None, "ok"):
        return is_generic_title(d.get("title"))
    return False


def enrich(
    data_path: Path,
    cache_path: Path,
    limit: int | None,
    no_card: bool,
    retry_errors: bool,
    retry_generic: bool,
    reparse: bool,
) -> None:
    with data_path.open() as f:
        likes = yaml.safe_load(f) or []

    cache = load_cache(cache_path)

    if reparse:
        n = reparse_cache(cache)
        save_cache(cache, cache_path)
        logger.info(f"Reparsed {n} cached entries")

    # Collect URLs that still need fetching (not cached, citoid not yet applied)
    to_fetch: list[str] = []
    seen_urls: set[str] = set()
    for like in likes:
        for link in like.get("links", []):
            url = link["url"]
            if url in seen_urls:
                continue
            citoid_val = link.get("citoid")
            if citoid_val is not None:
                # OK results are skipped unless they're generic and we're retrying those
                is_error = citoid_val.get("citoid_status") not in (None, "ok")
                is_generic = _citoid_is_generic(citoid_val)
                if not ((retry_errors and is_error) or (retry_generic and is_generic)):
                    continue
            elif url in cache:
                cached_entry = cache[url]
                is_error = cached_entry.get("citoid_status") != "ok"
                is_generic = _citoid_is_generic(cached_entry)
                if not ((retry_errors and is_error) or (retry_generic and is_generic)):
                    continue  # skip unless retrying failures / generics
            if no_card and link.get("card_title"):
                continue  # skip links that already have a display title
            seen_urls.add(url)
            to_fetch.append(url)

    if limit is not None:
        to_fetch = to_fetch[:limit]

    logger.info(f"URLs to fetch: {len(to_fetch)} (cache has {len(cache)} entries)")

    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT

    last_request_at = 0.0
    for i, url in enumerate(to_fetch):
        wait = MIN_INTERVAL - (time.monotonic() - last_request_at)
        if wait > 0:
            time.sleep(wait)
        last_request_at = time.monotonic()

        try:
            result = fetch_citoid(url, session)
            status = result["citoid_status"]
            title = result.get("title", "")[:60] if result.get("title") else ""
            logger.info(f"[{i+1}/{len(to_fetch)}] {status} {url[:60]!r}"
                        + (f" → {title!r}" if title else ""))
        except requests.HTTPError as e:
            result = {"citoid_status": "http_error", "error": str(e),
                      "status_code": e.response.status_code}
            logger.warning(f"[{i+1}/{len(to_fetch)}] HTTP {e.response.status_code}: {url[:60]!r}")
        except Exception as e:
            result = {"citoid_status": "error", "error": str(e)}
            logger.warning(f"[{i+1}/{len(to_fetch)}] Error: {e} — {url[:60]!r}")

        cache[url] = result
        save_cache(cache, cache_path)  # save after each fetch so progress survives interruption

    # Apply cache to all links without citoid, plus re-apply to error links on retry
    applied = skipped = 0
    for like in likes:
        for link in like.get("links", []):
            citoid_val = link.get("citoid")
            if citoid_val is not None:
                is_error = citoid_val.get("citoid_status") not in (None, "ok")
                is_generic = _citoid_is_generic(citoid_val)
                if not ((retry_errors and is_error) or (retry_generic and is_generic)):
                    continue  # skip ok results; skip errors/generics if not retrying
            cached = cache.get(link["url"])
            if cached is None:
                skipped += 1
                continue
            if cached["citoid_status"] == "ok":
                link["citoid"] = {k: v for k, v in cached.items()
                                  if k != "citoid_status" and v is not None}
            else:
                # Record the attempt outcome so we don't re-fetch blindly
                link["citoid"] = {"citoid_status": cached["citoid_status"]}
            applied += 1

    logger.info(f"Applied: {applied} links  |  No cache entry yet: {skipped} links")

    with data_path.open("w") as f:
        yaml.dump(likes, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    logger.info(f"Wrote {data_path}")


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    parser = argparse.ArgumentParser(description="Enrich bsky_likes.yml with Citoid metadata")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--limit", type=int, default=None,
                        help="Max number of new URLs to fetch from Citoid (for testing)")
    parser.add_argument("--no-card", action="store_true",
                        help="Only enrich links that have no card_title (bare URLs)")
    parser.add_argument("--retry-errors", action="store_true",
                        help="Re-fetch URLs whose cached status is an error")
    parser.add_argument("--retry-generic", action="store_true",
                        help="Re-fetch URLs whose cached result is a generic / bot-wall "
                             "page (e.g. an OSF landing page titled 'OSF')")
    parser.add_argument("--reparse", action="store_true",
                        help="Re-parse all cached raw responses without hitting the API")
    args = parser.parse_args()

    enrich(args.data, args.cache, args.limit, args.no_card,
           args.retry_errors, args.retry_generic, args.reparse)


if __name__ == "__main__":
    main()
