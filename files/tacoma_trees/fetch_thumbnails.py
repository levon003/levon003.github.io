# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "pillow"]
# ///
"""Fetch a small thumbnail for each tree species in trees.json.

Strategy: use the English Wikipedia article's lead/infobox image (already
human-curated to be representative) via the `pageimages` API. For species whose
article has no usable image — or where the curated lead image is poor — a manual
override in OVERRIDES points at a specific Commons file instead.

For every image we record attribution (author + license + source URL), since
Commons images are almost all CC-BY / CC-BY-SA and require credit when rehosted.

Outputs:
  thumbs/<slug>.webp        ~200px WebP thumbnails
  thumbnails.json           { "Genus species": {file, artist, license, license_url, source} }

Run with:  uv run fetch_thumbnails.py
"""
import html
import io
import json
import re
import time
from pathlib import Path

import requests
from PIL import Image

HERE = Path(__file__).parent
THUMBS = HERE / "thumbs"
MAX_DIM = 200          # stored thumbnail max dimension (px)
WEBP_QUALITY = 80

# Manual overrides: "Genus species" -> a Commons File: name (without "File:").
# Used when Wikipedia has no article/image, or its lead image isn't a usable
# plant photo. Populated during QA.
OVERRIDES = {
    "Syringa pekinensis": "Syringa pekinensis 'Morton', Arnold Arboretum - IMG 5969.JPG",
    "Callitropsis nootkatensis": "Cupressus_nootkatensis_1334.JPG",
    "Cydonia oblonga": "Quince_in_Fergana.jpg",
    "Platanus x acerifolia": "Arboles_de_Platanos.jpg",
    "Quercus myrsinifolia": "Cyclobalanopsis_myrsinifolia1.jpg",
    # photos rather than botanical drawings, for the fruit list
    "Prunus persica": "Autumn Red peaches.jpg",
    "Prunus persica var. nucipersica": "Nectarine branch surachit.jpg",
    "Ficus carica": "Ripe fig fruit on tree (Ficus Carica) in Southern France.JPG",
    "Prunus salicina x armeniaca x persica": "Red pluots.JPG",
    # photos rather than botanical illustrations
    "Frangula purshiana": "Rhamnus purshiana -- leaves and fruits.JPG",
    "Cryptomeria japonica": "Cryptomeria japonica. A Ferradura. Santiago de Compostela. Galiza 01.jpg",
    "Aesculus hippocastanum": "Aesculus hippocastanum-1.jpg",
}

# Hybrids / varieties / generics whose exact name isn't an article title: look
# up this Wikipedia article (parent species or genus) for the lead image instead.
TITLE_FALLBACK = {
    "Pinus contorta var. contorta": "Pinus contorta",
    "Cupressus bakerii": "Cupressus bakeri",
    "Syringa pekinensis": "Syringa reticulata subsp. pekinensis",
    "Malus crabapple sp.": "Malus",
    "Cornus kousa x nuttallii": "Cornus kousa",
    "Magnolia acuminata x denudata": "Magnolia acuminata",
    "Magnolia liliiflora ‘Nigra’ × sprengeri ‘Diva’": "Magnolia liliiflora",
    "Catalpa x erubescens": "Catalpa",
    "Ulmus carpinifolia x parvifolia": "Ulmus",
    "Prunus salicina x armeniaca x persica": "Pluot",
}

API = "https://en.wikipedia.org/w/api.php"  # resolves both local and Commons files
COMMONS_API = "https://commons.wikimedia.org/w/api.php"  # for file-page wikitext
S = requests.Session()
S.headers["User-Agent"] = "TacomaTreeTable/1.0 (zach@renphil.org) thumbnail-fetch"


def api(params, retries=4, base=API):
    """GET the MediaWiki API with maxlag + retry/backoff (be a polite client)."""
    params = {**params, "maxlag": 5}
    for attempt in range(retries):
        try:
            r = S.get(base, params=params, timeout=30)
            if r.status_code == 200:
                j = r.json()
                if "error" not in j:
                    return j
        except requests.RequestException:
            pass
        time.sleep(1.5 * (attempt + 1))
    return {}


def get_bytes(url, retries=4):
    for attempt in range(retries):
        try:
            r = S.get(url, timeout=60)
            if r.status_code == 200 and r.content:
                return r.content
        except requests.RequestException:
            pass
        time.sleep(1.5 * (attempt + 1))
    return None


def slug(genus, species):
    return re.sub(r"[^a-z0-9]+", "_", f"{genus} {species}".lower()).strip("_")


def wiki_lead_image(title):
    """Return the Commons file name of the article's lead image, or None."""
    r = api({"action": "query", "format": "json", "redirects": 1,
             "titles": title, "prop": "pageimages", "piprop": "name"})
    pg = next(iter(r.get("query", {}).get("pages", {}).values()), {})
    return pg.get("pageimage")


def commons_file_info(filename):
    """Return (thumb_url, attribution dict) for a file, or (None, None)."""
    r = api({"action": "query", "format": "json", "titles": "File:" + filename,
             "prop": "imageinfo", "iiprop": "extmetadata|url|mime",
             "iiurlwidth": 400})
    pg = next(iter(r.get("query", {}).get("pages", {}).values()), {})
    info = pg.get("imageinfo", [{}])
    if not info:
        return None, None
    ii = info[0]
    em = ii.get("extmetadata", {})

    def field(key):
        return em.get(key, {}).get("value", "")

    def plain(s):
        s = re.sub(r"<[^>]+>", " ", s or "")
        s = html.unescape(s)
        return re.sub(r"\s+", " ", s).strip()

    artist = plain(field("Artist"))[:120]
    license_name = plain(field("LicenseShortName"))
    # extmetadata is sometimes empty on older "own work" uploads; fall back to
    # parsing the file page wikitext for the author and license template.
    if not artist or not license_name:
        wa, wl = wikitext_attr(filename)
        artist = artist or wa
        license_name = license_name or wl
    # self-licensed / transferred files often have no author field; the original
    # uploader is the licensor in that case.
    if not artist:
        artist = original_uploader(filename)
    attr = {
        "artist": artist or "Unknown",
        "license": license_name or "see source",
        "license_url": field("LicenseUrl"),
        "source": ii.get("descriptionurl", ""),
    }
    return ii.get("thumburl") or ii.get("url"), attr


def original_uploader(filename):
    """Username of the file's original uploader (best-effort author fallback)."""
    r = api({"action": "query", "format": "json", "titles": "File:" + filename,
             "prop": "imageinfo", "iiprop": "user|timestamp", "iilimit": "max"},
            base=COMMONS_API)
    pg = next(iter(r.get("query", {}).get("pages", {}).values()), {})
    revs = pg.get("imageinfo", [])
    if not revs:
        return ""
    return min(revs, key=lambda x: x.get("timestamp", "")).get("user", "")


def wikitext_attr(filename):
    """Parse author + license from a Commons file page's wikitext (fallback)."""
    r = api({"action": "query", "format": "json", "titles": "File:" + filename,
             "prop": "revisions", "rvprop": "content", "rvslots": "main"},
            base=COMMONS_API)
    pg = next(iter(r.get("query", {}).get("pages", {}).values()), {})
    revs = pg.get("revisions")
    if not revs:
        return "", ""
    txt = revs[0].get("slots", {}).get("main", {}).get("*", "")
    low = txt.lower()
    m = re.search(r"cc-by-sa-(\d)\.(\d)", low)
    if m:
        lic = f"CC BY-SA {m.group(1)}.{m.group(2)}"
    elif (m := re.search(r"cc-by-(\d)\.(\d)", low)):
        lic = f"CC BY {m.group(1)}.{m.group(2)}"
    elif "cc-zero" in low or "{{cc0" in low:
        lic = "CC0"
    elif "gfdl" in low:
        lic = "GFDL"
    elif re.search(r"\{\{\s*pd[-} ]|public domain", low):
        lic = "Public domain"
    else:
        lic = ""
    author = ""
    am = re.search(r"\|\s*author\s*=\s*(.*)", txt, re.I)
    if am:
        a = am.group(1).split("\n")[0]
        a = re.sub(r"\[\[User:[^|\]]+\|([^\]]+)\]\]", r"\1", a)
        a = re.sub(r"\[\[(?:User:)?([^\]|]+)(?:\|[^\]]+)?\]\]", r"\1", a)
        a = re.sub(r"\[https?://\S+ ([^\]]+)\]", r"\1", a)
        a = re.sub(r"\{\{[^}]*\}\}|<[^>]+>|https?://\S+", "", a)
        author = re.sub(r"\s+", " ", a).strip(" '\"|")
    return author[:120], lic


def save_thumb(url, dest):
    data = get_bytes(url)
    if not data:
        raise RuntimeError("download failed")
    im = Image.open(io.BytesIO(data)).convert("RGB")
    im.thumbnail((MAX_DIM, MAX_DIM))
    dest.parent.mkdir(exist_ok=True)
    im.save(dest, "WEBP", quality=WEBP_QUALITY, method=6)


def main():
    trees = json.loads((HERE / "trees.json").read_text())
    # unique species, preserving first-seen order
    seen, species = set(), []
    for t in trees:
        key = (t["genus"], t["species"])
        if key not in seen:
            seen.add(key)
            species.append(key)

    # resume: keep already-fetched entries whose file still exists (unless overridden)
    existing = {}
    jf = HERE / "thumbnails.json"
    if jf.exists():
        existing = json.loads(jf.read_text())

    out, missing = {}, []
    for genus, sp in species:
        name = f"{genus} {sp}"
        prev = existing.get(name)
        complete = prev and prev.get("artist") != "Unknown" and prev.get("license") not in ("see source", "")
        if name not in OVERRIDES and complete and (THUMBS / prev["file"]).exists():
            out[name] = prev
            continue
        time.sleep(0.3)
        filename = OVERRIDES.get(name) or wiki_lead_image(TITLE_FALLBACK.get(name, name))
        if not filename:
            missing.append(name)
            print(f"  MISSING  {name}")
            continue
        thumb_url, attr = commons_file_info(filename)
        if not thumb_url:
            missing.append(name)
            print(f"  NO-INFO  {name} ({filename})")
            continue
        sl = slug(genus, sp)
        try:
            save_thumb(thumb_url, THUMBS / f"{sl}.webp")
        except Exception as e:
            missing.append(name)
            print(f"  FAIL     {name}: {e}")
            continue
        attr["file"] = f"{sl}.webp"
        out[name] = attr
        print(f"  ok       {name}  [{attr['license']}]")

    # tidy author strings: drop trailing "(talk)" / "(talk · contribs)" links
    for v in out.values():
        v["artist"] = re.sub(r"\s*\(\s*talk[^)]*\)", "", v["artist"]).strip()

    (HERE / "thumbnails.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(f"\n{len(out)} thumbnails, {len(missing)} missing -> thumbnails.json")
    if missing:
        print("missing:", ", ".join(missing))


if __name__ == "__main__":
    main()
