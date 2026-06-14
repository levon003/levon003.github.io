---
layout: post
title:  "Tacoma's pre-approved street trees"
tags: [tacoma, trees, data, short]
excerpt: "The City of Tacoma, Washington's preapproved street-tree list in one table."
---

If you want to plant a tree in the Right-of-Way [planting strip](https://en.wikipedia.org/wiki/Road_verge) between
the sidewalk and the street in Tacoma, Washington, you need to get a planting permit. See ["Trees in the Right-of-Way"](https://tacoma.gov/government/departments/environmental-services/urban-forestry/trees-in-the-right-of-way/) on the City of Tacoma website.

The city maintains lists of *pre-approved* species you can choose from that serve as recommendations and that will make review easier.
Unfortunately, those lists live in a few random PDFs.
I wanted to get an easier sense of what these options are, so I had Claude Opus 4.8 build the table below, which is searchable and sortable.
This table is based on the 2025 revision of the pre-approved tree lists, so it may be out-of-date if you're looking at this in 2027 or later.

You can also download the extracted and structured data as JSON [here](/files/tacoma_trees/trees.json).

## Pre-approved trees

{% include tacoma-trees.html %}

## Notes

- **Data is from January 2025.** The data were extracted from the PDFs on the City of Tacoma's website, last revised January 30, 2025.
- **Data tweaks.** The data has a few quirks — a misspelled species, an evergreen icon on a tree you'd call deciduous, etc. I worked with Claude to fix these; see the full list of corrections below.
- **Definitions.** *Growth rate* and *Canopy factor* are defined as follows (see [13.01.060.C](https://ecode360.com/48470096)):
  >A method of calculating tree size by taking into account the tree’s mature height, mature crown spread and growth rate. The Canopy Factor is calculated using the following formula: (mature height in feet) x (mature crown spread in feet) x (growth rate number) x 0.01 = Canopy Factor. The growth rate number is 1 for slow growing trees, 2 for moderately growing trees, and 3 for fast growing trees.
  >
  > •Large Trees = Canopy Factor greater than 70,
  >
  > •Medium Trees = Canopy Factor from 40 to 70,
  >
  > •Small Trees = Canopy Factor less than 40.
- **Prohibited trees.** There's also a separate list of not recommended and prohibited trees, which is not included here. At the time of writing, you can find that list [here](https://tacoma.gov/wp-content/uploads/2025/09/Appendix-7D-Prohibited-Tree-List_2025_Update.pdf).

<details markdown="0">
<summary>Full list of tweaks Claude and I made to the city's data</summary>
<p>Data corrections:</p>
<ul>
<li><strong>Misspelled scientific names:</strong> <em>Chamaecyparis obstusa</em> → <em>obtusa</em>; <em>Gingko biloba</em> → <em>Ginkgo biloba</em>; <em>Eucalyptus gunni</em> → <em>gunnii</em>; <em>Cladastris kentukea</em> → <em>Cladrastis kentukea</em>; <em>Tillia tomentosa</em> → <em>Tilia tomentosa</em>; <em>Ulmus parviflora</em> → <em>parvifolia</em>; <em>Ulmus caprinifolia × parvifloia</em> → <em>carpinifolia × parvifolia</em>; <em>Cornus kousa × nuttalii</em> → <em>nuttallii</em>.</li>
<li><strong>Naming and taxonomy:</strong> <em>Crataegus crus-galli var. inermis</em> is corrected to <em>Crataegus crus-galli</em> 'Inermis' — the thornless cockspur hawthorn, where "inermis" is a cultivar rather than a botanical variety; and <em>Cupressus bakeri</em> is updated to its currently accepted name, <em>Hesperocyparis bakeri</em>.</li>
<li><strong>Reclassified as evergreen:</strong> Four broadleaf evergreens were marked with a deciduous icon in the source: <em>Eucalyptus neglecta</em> (omeo gum), <em>Eucalyptus parvula</em> (small-leaved gum), <em>Quercus ilex</em> (holm oak), and <em>Quercus myrsinifolia</em> (bamboo-leaf oak).</li>
<li><strong>Untangled columns:</strong> The two <em>Syringa pekinensis</em> rows had the cultivar code (<em>'Morton'</em>, <em>DTR 124'</em>) sitting in the common-name slot and the trade name in the cultivars slot; I swapped them back. A footnote asterisk was stripped from three large trees (Douglas-fir, coastal redwood, ponderosa pine).</li>
<li><strong>Fruit tree canopy factor:</strong> The fruit list gives sizes as ranges (e.g. "6–12"); the canopy factor for these is computed from the formula above using the upper end of the range. In addition, the fruit sheet doesn't carry the utility-friendly flag, but I believe all of the dwarf fruit trees are allowed under power lines — so I've marked them as such, with the exception of the fig (<em>Ficus carica</em>) which I'm not sure about.</li>
</ul>
</details>

If you spot any additional errors, please do let me know!
