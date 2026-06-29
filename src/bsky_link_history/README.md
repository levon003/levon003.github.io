# bsky-link-history

Scrapes my Bluesky likes, extracts the external links, enriches them with citation
metadata, flags dead ones, and writes `_data/bsky_likes.yml` — which Jekyll renders at
`/bsky-links/`.

## Setup

Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

Create a `.env` with a Bluesky **app password** (Settings → Privacy and Security → App
Passwords — *not* your account password):

```
BSKY_HANDLE=your-handle.bsky.social
BSKY_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx
```

## Pipeline

Three scripts run in order; each reads and rewrites `_data/bsky_likes.yml`. GitHub Actions
runs all three daily (`.github/workflows/scrape-bsky-likes.yml`), persisting the JSON caches
between runs so each pass is incremental.

```bash
uv run python scrape_likes.py    # 1. fetch likes, extract links
uv run python enrich.py          # 2. add Citoid citation metadata
uv run python check_links.py     # 3. flag dead links, attach Wayback fallbacks
uv run python summarize.py       # 4. write _data/bsky_links_summary.yml (counts, top domains + accounts)
```

### 1. `scrape_likes.py`

Fetches likes via `app.bsky.feed.getActorLikes` and extracts links from each post's link
card, inline facets, and quoted post.

When a liked post has **no link of its own**, the thread is fetched and links are pulled
**only from posts by the thread's original (root) author** (ancestors + self-replies). Links
posted by other accounts are ignored — if you liked one of those, it shows up as its own
entry.

Liked posts from the same thread are merged into one entry. Link-shortener URLs
(`bit.ly`, `buff.ly`, `tinyurl.com`, `t.co`, …) are expanded to their canonical
destination so Citoid can enrich the real article — best-effort, so a failed resolve just
leaves the shortener in place.

```bash
uv run python scrape_likes.py                       # incremental (stops at first known post)
uv run python scrape_likes.py --full-refresh        # re-fetch all likes (still skips known URIs)
uv run python scrape_likes.py --backfill-threads    # populate thread_root_uri + re-merge
uv run python scrape_likes.py --resolve-shorteners  # expand shorteners in existing entries
```

### 2. `enrich.py`

Fetches citation metadata from [Wikimedia's Citoid API](https://www.mediawiki.org/wiki/Citoid)
for each unique URL, cached to `citoid_cache.json`. Self-limited to 200 req/min.

```bash
uv run python enrich.py                  # enrich un-enriched links
uv run python enrich.py --retry-errors   # re-fetch cached errors
uv run python enrich.py --retry-generic  # re-fetch bot-wall / landing-page results
uv run python enrich.py --reparse        # re-parse cached raw responses, no API calls
```

- **DOI extraction.** For URLs that embed a DOI (ACM, OUP, OSF preprints, arXiv, `doi.org`,
  any `/doi/10.` path), the bare DOI is sent to Citoid instead of the publisher URL — cleaner
  metadata, dodges publisher bot-blocking, and recovers PDFs Citoid otherwise 415s on
  (e.g. `arxiv.org/pdf/{id}` → `10.48550/arXiv.{id}`). OSF DOIs are version-specific, so
  `_v1` and the bare form are tried as fallbacks.
- **Generic / bot-wall detection.** Citoid sometimes returns HTTP 200 with a junk title (an
  `"OSF"` landing page, a Cloudflare `"Client Challenge"`, etc.). These are detected and
  recorded as `citoid_status: blocked` rather than stored as real metadata.

### 3. `check_links.py`

Liveness-checks links Citoid *couldn't* resolve and marks the genuinely dead ones, caching to
`liveness_cache.json`. A Citoid failure ≠ a dead link: paywalls and bot-walls refuse the
scraper while serving humans fine, so this does a real browser-like HTTP GET:

- 2xx/3xx, or 401/403/429 (gated but present) → **live**
- 404/410, DNS/SSL/connection failure → **dead**
- 5xx / timeout → **unknown**, treated as live (transient)

Dead links get `dead: true` and, when a snapshot exists, an `archive_url` from the Wayback
availability API; a link that comes back to life has both cleared. App deeplinks, bare
`*.bsky.social` handles, and form/chat links are skipped.

```bash
uv run python check_links.py                   # check unresolved links not yet cached
uv run python check_links.py --recheck         # re-check everything
uv run python check_links.py --refresh-archives # just re-query Wayback for dead links missing an archive
```

### 4. `summarize.py`

Writes `_data/bsky_links_summary.yml` — `entries_with_links`, `total_links`,
`unique_domains`, `total_likes`, and the `--top` (default 10) most-frequent link **domains**
and most-liked **accounts** — which the page header renders as an intro line plus two lists.
No caches or network; just reads the YAML.

- Domains are grouped by **registrable domain** (eTLD+1, via `tldextract`'s bundled
  public-suffix snapshot), so `open.substack.com` and `samkriss.substack.com` both count as
  `substack.com`. (The per-link display in the page still shows the full host, which is more
  specific.)
- Accounts are counted over the link-bearing likes that actually appear on the page (not
  every like in the dataset), keyed by author DID so a handle change doesn't split the count.

## Output format

```yaml
- post_uri: at://did:plc:.../app.bsky.feed.post/...
  thread_root_uri: at://did:plc:.../app.bsky.feed.post/...
  all_post_uris: [at://...]          # all liked posts in this thread
  liked_at: '2025-01-15T20:34:12Z'
  author_handle: someone.bsky.social
  author_did: did:plc:...
  links:
    - url: https://example.com/paper
      source: card                   # card | facet | quoted* | thread
      card_title: Some Paper Title
      card_description: ...
      citoid:                        # present once enriched
        title: Some Paper Title
        authors: [{first: Jane, last: Smith}]
        date: '2024'
        doi: 10.1234/example
        publisher: Journal of Examples
```

- Failed Citoid lookups store only a status: `citoid: {citoid_status: http_error | blocked |
  empty}`. The renderer falls back to `card_title` / the bare URL.
- Dead links carry `dead: true` and (when archived) `archive_url`.

## Reference

| Need | Endpoint | Auth |
|---|---|---|
| Start session | `com.atproto.server.createSession` | sends creds |
| Your likes | `app.bsky.feed.getActorLikes` | yes (self only) |
| Thread around a post | `app.bsky.feed.getPostThread` | no |
| Batch hydrate posts | `app.bsky.feed.getPosts` (max 25) | no |

Permalink: `at://{did}/app.bsky.feed.post/{rkey}` → `https://bsky.app/profile/{did}/post/{rkey}`

**Notes.** The caches are gitignored and regenerable; the YAML is rewritten atomically after
each fetch, so an interrupted run loses at most one request. Remaining permanent Citoid errors
are mostly PDFs (415) and 404s, which won't resolve on retry.
