#!/usr/bin/env python3
"""Write _data/bsky_links_summary.yml — aggregate counts for the links page header.

Reads the enriched bsky_likes.yml and emits totals plus the most-frequent link
domains, so the Jekyll layout can show a summary without recomputing it on every build.
"""

import argparse
import logging
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

import tldextract
import yaml

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).parent.parent.parent
DEFAULT_DATA = REPO_ROOT / "_data" / "bsky_likes.yml"
DEFAULT_OUT = REPO_ROOT / "_data" / "bsky_links_summary.yml"

# Use the bundled public-suffix snapshot only (no network) so CI is deterministic.
_extract = tldextract.TLDExtract(suffix_list_urls=())


def registrable_domain(url: str) -> str | None:
    """Return the eTLD+1 (e.g. 'substack.com' for 'open.substack.com'), or the bare
    host if no registrable domain can be derived."""
    try:
        ext = _extract(url)
    except Exception:
        return None
    # `top_domain_under_public_suffix` (tldextract >=5.3) supersedes `registered_domain`.
    reg = getattr(ext, "top_domain_under_public_suffix", None)
    if reg is None:
        reg = ext.registered_domain
    if reg:
        return reg.lower()
    host = urlparse(url).netloc.lower()  # IP / intranet / malformed: fall back to host
    return host or None


def build_summary(data_path: Path, out_path: Path, top_n: int) -> dict:
    likes = yaml.safe_load(data_path.read_text()) or []

    entries_with_links = 0
    total_links = 0
    domains: Counter[str] = Counter()
    accounts: Counter[str] = Counter()  # keyed by author DID (stable across handle changes)
    handle_for_did: dict[str, str] = {}
    for like in likes:
        links = like.get("links") or []
        if not links:
            continue  # only count likes that actually appear in the list (have links)
        entries_with_links += 1

        did = like.get("author_did")
        if did:
            accounts[did] += 1
            if like.get("author_handle"):
                handle_for_did[did] = like["author_handle"]

        for link in links:
            total_links += 1
            d = registrable_domain(link["url"])
            if d:
                domains[d] += 1

    summary = {
        "entries_with_links": entries_with_links,
        "total_links": total_links,
        "unique_domains": len(domains),
        "top_domains": [{"domain": d, "count": n} for d, n in domains.most_common(top_n)],
        "top_accounts": [
            {"handle": handle_for_did.get(did, did), "did": did, "count": n}
            for did, n in accounts.most_common(top_n)
        ],
    }
    out_path.write_text(yaml.dump(summary, allow_unicode=True, sort_keys=False))
    logger.info(
        f"{entries_with_links} entries with links, {total_links} links, "
        f"{len(domains)} domains, {len(accounts)} accounts → {out_path}"
    )
    return summary


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--top", type=int, default=10, help="Number of top domains to emit")
    args = parser.parse_args()
    build_summary(args.data, args.out, args.top)


if __name__ == "__main__":
    main()
