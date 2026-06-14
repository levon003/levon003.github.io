# /// script
# requires-python = ">=3.10"
# dependencies = ["pdfplumber", "pypdfium2", "pillow"]
# ///
"""Extract Tacoma's preapproved street-tree lists from the city PDFs into trees.json.

The four "preapproved" PDFs share a tabular layout. Text columns (genus, species,
common name, cultivars, the numeric size columns) come straight out of the text
layer. Three columns are pictorial and are read off a rendered raster instead:

  * West Coast Native  -> a checkmark glyph (U+F061) in the text layer
  * Special Characteristics -> colored icons: brown tree = deciduous,
    green conifer = evergreen, pink tree = ornamental, black pole = overhead-
    utility-friendly. Detected by sampling pixel colors in the cell.

The fruit list uses a reduced 9-column layout with no native/characteristics
columns; every entry is treated as a deciduous, food-producing tree.

Run with:  uv run extract_trees.py
"""
import bisect
import collections
import json
import re
from pathlib import Path

import pdfplumber
import pypdfium2 as pdfium

HERE = Path(__file__).parent
RENDER_SCALE = 4.0  # raster scale for icon color sampling

# Per-size-class source PDFs (everything but fruit shares the 12-column layout).
SOURCES = [
    ("small", "preapproved_small_2025.pdf"),
    ("medium", "preapproved_medium_2025.pdf"),
    ("large", "preapproved_large_2025.pdf"),
    ("fruit", "preapproved_fruit_2025.pdf"),
]

CHECK = ""  # symbol-font checkmark used in the Native column


def column_bounds(page):
    """Vertical column boundaries, from the tall cell rectangles."""
    xs = set()
    for r in page.rects:
        if r["bottom"] - r["top"] > 50:
            xs.add(round(r["x0"]))
            xs.add(round(r["x1"]))
    # collapse boundaries within 3px of each other
    out = []
    for x in sorted(xs):
        if not out or x - out[-1] > 3:
            out.append(x)
    return out


def row_separators(page):
    """Horizontal row-separator y positions (full-width thin rects)."""
    ys = set()
    for r in page.rects:
        if r["x1"] - r["x0"] > 400 and r["bottom"] - r["top"] < 3:
            ys.add(round(r["top"]))
    return sorted(ys)


def cells_for_band(page, y0, y1, bounds):
    """Collect text per column for the chars inside one row band."""
    cols = collections.defaultdict(list)  # ci -> list of (top, x0, text)
    for c in page.chars:
        if y0 + 1 <= c["top"] <= y1 - 1:
            ci = bisect.bisect_right(bounds, c["x0"]) - 1
            if 0 <= ci < len(bounds) - 1:
                cols[ci].append((round(c["top"]), c["x0"], c["text"]))
    out = {}
    for ci, items in cols.items():
        items.sort()
        out[ci] = "".join(t for _, _, t in items)
    return out


def num(s):
    m = re.search(r"-?\d+(?:\.\d+)?", s or "")
    return float(m.group()) if m else None


def parse_dim(s):
    """Parse a dimension cell. Fruit trees give ranges ("6 to 12"); return
    (sort_value, label) where sort_value is the high end and label is the range
    string for display (None for a plain single value)."""
    nums = [float(n) for n in re.findall(r"\d+(?:\.\d+)?", s or "")]
    if not nums:
        return None, None
    if len(nums) >= 2 and "to" in (s or ""):
        fmt = lambda v: str(int(v)) if v == int(v) else str(v)
        return max(nums), fmt(nums[0]) + "–" + fmt(nums[1])
    return nums[0], None


def classify_icons(px, y0, y1, x0, x1, scale):
    """Count icon-colored pixels in a special-characteristics cell."""
    cnt = {"green": 0, "pink": 0, "brown": 0}
    for yy in range(int((y0 + 2) * scale), int((y1 - 2) * scale)):
        for xx in range(int(x0 * scale), int(x1 * scale)):
            r, g, b = px[xx, yy]
            if r > 230 and g > 230 and b > 230:
                continue
            if g > 110 and g > r + 15 and g > b + 15:
                cnt["green"] += 1
            elif r > 180 and b > 120 and r > g + 10 and abs(r - b) < 90 and g < r - 20:
                cnt["pink"] += 1
            elif r > 110 and r >= g >= b and r - b > 25 and g > 60:
                cnt["brown"] += 1
    return cnt


# Near-black pixels are nearly unique to the utility-pole icon. Counting them
# across the whole special-characteristics cell separates pole-present cells
# (>=391 at scale 4) from pole-absent ones (<=284, the tree-icon outline). The
# pole's position within the cell varies, so we must scan the full width — the
# threshold sits in the gap. (Medium/large lists have no poles at all.)
POLE_THRESHOLD = 340


def pole_dark(px, y0, y1, x0, x1, scale):
    """Near-black pixel count across the special-characteristics cell."""
    dark = 0
    for yy in range(int((y0 + 2) * scale), int((y1 - 2) * scale)):
        for xx in range(int((x0 + 2) * scale), int((x1 - 2) * scale)):
            r, g, b = px[xx, yy]
            if r < 100 and g < 100 and b < 100:
                dark += 1
    return dark


def extract_standard(size_class, path):
    """12-column layout (small / medium / large)."""
    plumb = pdfplumber.open(path)
    doc = pdfium.PdfDocument(str(path))
    rows = []
    for pi, page in enumerate(plumb.pages):
        bounds = column_bounds(page)
        if len(bounds) < 13:
            continue
        seps = row_separators(page)
        img = doc[pi].render(scale=RENDER_SCALE).to_pil().convert("RGB")
        px = img.load()
        # pdfplumber text coords and the pypdfium raster differ by the MediaBox
        # y-origin; add this offset to text y's before sampling the raster.
        y_off = -page.mediabox[1]
        sc_x0, sc_x1 = bounds[11], bounds[12]  # special-characteristics cell
        for i in range(len(seps) - 1):
            y0, y1 = seps[i], seps[i + 1]
            if not (8 < y1 - y0 < 40):
                continue
            cols = cells_for_band(page, y0, y1, bounds)
            height = num(cols.get(4, ""))
            genus = cols.get(0, "").strip()
            if height is None or not genus or not genus[0].isalpha():
                continue
            icons = classify_icons(px, y0 + y_off, y1 + y_off, sc_x0, sc_x1, RENDER_SCALE)
            dark = pole_dark(px, y0 + y_off, y1 + y_off, sc_x0, sc_x1, RENDER_SCALE)
            evergreen = icons["green"] > 300 and icons["green"] >= icons["brown"]
            rows.append({
                "size_class": size_class,
                "genus": genus,
                "species": cols.get(1, "").strip(),
                "common_name": cols.get(2, "").strip(),
                "cultivars": cols.get(3, "").strip(),
                "height_ft": height,
                "width_ft": num(cols.get(5, "")),
                "growth_rate": num(cols.get(6, "")),
                "canopy_factor": num(cols.get(7, "")),
                "min_strip_ft": num(cols.get(8, "")),
                "native": CHECK in cols.get(9, ""),
                "evergreen": evergreen,
                "ornamental": icons["pink"] > 300,
                "utility_friendly": dark > POLE_THRESHOLD,
                "food_producing": False,
            })
    return rows


def extract_fruit(size_class, path):
    """9-column fruit layout: no native / characteristics / canopy columns."""
    plumb = pdfplumber.open(path)
    rows = []
    for page in plumb.pages:
        bounds = column_bounds(page)
        if len(bounds) < 10:
            continue
        seps = row_separators(page)
        for i in range(len(seps) - 1):
            y0, y1 = seps[i], seps[i + 1]
            # No upper bound: fruit rows with long cultivar lists are tall.
            if y1 - y0 <= 8:
                continue
            cols = cells_for_band(page, y0, y1, bounds)
            height, h_label = parse_dim(cols.get(4, ""))
            width, w_label = parse_dim(cols.get(5, ""))
            genus = cols.get(0, "").strip()
            if height is None or not genus or not genus[0].isalpha():
                continue
            rows.append({
                "size_class": size_class,
                "genus": genus,
                "species": cols.get(1, "").strip(),
                "common_name": cols.get(2, "").strip(),
                "cultivars": cols.get(3, "").strip(),
                "height_ft": height,
                "width_ft": width,
                "height_label": h_label,
                "width_label": w_label,
                "growth_rate": num(cols.get(6, "")),
                "canopy_factor": None,
                "min_strip_ft": num(cols.get(7, "")),
                "native": False,
                "evergreen": False,
                "ornamental": False,
                "utility_friendly": False,
                "food_producing": True,
            })
    return rows


# --- Curated corrections to the city's data ---------------------------------
# Misspelled binomials in the source PDFs, keyed by the (genus, species) as
# printed. Values are the corrected (genus, species).
SPELLING = {
    ("Chamaecyparis", "obstusa"): ("Chamaecyparis", "obtusa"),
    ("Gingko", "biloba"): ("Ginkgo", "biloba"),
    ("Eucalyptus", "gunni"): ("Eucalyptus", "gunnii"),
    ("Cladastris", "kentukea"): ("Cladrastis", "kentukea"),
    ("Tillia", "tomentosa"): ("Tilia", "tomentosa"),
    ("Ulmus", "parviflora"): ("Ulmus", "parvifolia"),
    ("Ulmus", "caprinifolia x parvifloia"): ("Ulmus", "carpinifolia x parvifolia"),
    ("Cornus", "kousa x nuttalii"): ("Cornus", "kousa x nuttallii"),
    ("Cupressus", "bakerii"): ("Hesperocyparis", "bakeri"),  # accepted name; was Cupressus bakeri
    # interspecific Prunus cross; the species cell repeats the genus
    ("Prunus", "Prunus salicina x Prunus armeniaca x Prunus persica"):
        ("Prunus", "salicina x armeniaca x persica"),
}

# Broadleaf evergreens the city's icon marks (or we read) as deciduous, but
# which are evergreen in this climate. Keyed by the corrected (genus, species).
EVERGREEN_FIX = {
    ("Eucalyptus", "neglecta"),
    ("Eucalyptus", "parvula"),
    ("Quercus", "ilex"),
    ("Quercus", "myrsinifolia"),
}


def apply_corrections(rows):
    for r in rows:
        key = (r["genus"], r["species"])
        if key in SPELLING:
            r["genus"], r["species"] = SPELLING[key]
        # A few wide "species + cultivar" entries spill the cultivar code into
        # the common-name column; the real common name lands in cultivars.
        if r["genus"] == "Syringa" and r["species"] == "pekinensis":
            r["common_name"], r["cultivars"] = r["cultivars"], r["common_name"]
        # 'inermis' is a thornless cultivar, not a botanical variety
        if r["genus"] == "Crataegus" and r["species"] == "crus-galli var. inermis":
            r["species"], r["cultivars"] = "crus-galli", "Inermis"
        if (r["genus"], r["species"]) in EVERGREEN_FIX:
            r["evergreen"] = True
        # Per personal communication with the city, all the dwarf fruit trees
        # are allowed under power lines (the sheet doesn't say so), except fig.
        if r["food_producing"] and r["genus"] != "Ficus":
            r["utility_friendly"] = True
        # The fruit list omits canopy factor; compute it from the city's formula
        # (TMC 13.01.060.C): height x width x growth-rate number x 0.01.
        if r["canopy_factor"] is None and None not in (
            r["height_ft"], r["width_ft"], r["growth_rate"]
        ):
            r["canopy_factor"] = round(
                r["height_ft"] * r["width_ft"] * r["growth_rate"] * 0.01, 2
            )
    return rows


def main():
    all_rows = []
    for size_class, fname in SOURCES:
        path = HERE / fname
        if size_class == "fruit":
            rows = extract_fruit(size_class, path)
        else:
            rows = extract_standard(size_class, path)
        print(f"{size_class:7s}: {len(rows)} trees")
        all_rows.extend(rows)
    # tidy whitespace and known wrap artifacts in text fields
    FIXES = {"contortacontorta var.": "contorta var. contorta"}
    for r in all_rows:
        for k in ("genus", "species", "common_name", "cultivars"):
            v = re.sub(r"\s+", " ", r[k]).strip()
            v = FIXES.get(v, v)
            v = v.rstrip("*").strip()  # '*' is an undefined source footnote marker
            r[k] = v
    apply_corrections(all_rows)
    out = HERE / "trees.json"
    out.write_text(json.dumps(all_rows, indent=1, ensure_ascii=False))
    print(f"total  : {len(all_rows)} trees -> {out}")


if __name__ == "__main__":
    main()
