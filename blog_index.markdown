---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: home
title: Blog Index
permalink: /blog/
list_all_posts: false
---
View my peer-reviewed research and writing on my [homepage](https://levon003.github.io).

This page lists my self-published writings, including both posts hosted elsewhere and {{ site.posts | size }} posts hosted on this blog.

## Posts

<ul class="post-list">
  {%- for post in site.posts -%}
    {%- unless post.tags contains "short" -%}
    <li>
      {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
      <span class="post-meta">{{ post.date | date: date_format }}</span>
      <h3>
        <a class="post-link" href="{{ post.url | relative_url }}">
          {{ post.title | escape }}
        </a>
      </h3>
      {%- if site.show_excerpts -%}
        {{ post.excerpt }}
      {%- endif -%}
    </li>
    {%- endunless -%}
  {%- endfor -%}
</ul>


## Posts on [Medium](https://zwlevonian.medium.com/)

<ul class="post-list">
  <li>
    <span class="post-meta">{{ "2022-05-09" | date: date_format }}</span>
    <h3><a href="https://zwlevonian.medium.com/how-would-you-deal-with-an-ambiguous-problem-data-science-interview-question-891638470572" class="post-link">
        How would you deal with an ambiguous problem?
    </a></h3>
    Conceptual workflow for scoping Data Science problems.
  </li>
  <li>
    <span class="post-meta">{{ "2022-03-09" | date: date_format }}</span>
    <h3><a class="post-link" href="https://zwlevonian.medium.com/model-vs-modeler-trade-offs-designing-interactive-text-classification-interfaces-cda41c367e89">
        Model vs Modeler: Trade-offs designing interactive text classification interfaces
    </a></h3>
    Accessible summary of my IUI 2022 paper.
  </li>
  <li>
    <span class="post-meta">{{ "2021-10-29" | date: date_format }}</span>
    <h3><a class="post-link" href="https://nbviewer.org/github/levon003/ml-visualized/blob/master/_notebook/BoWLinRegTweets.ipynb">
        Basics of machine learning with text data: bag-of-words for linear regression
    </a></h3>
    Twitter data workshop presented to undergraduate HCI researchers.
  </li>
  <li>
    <span class="post-meta">{{ "2020-11-01" | date: date_format }}</span>
    <h3><a class="post-link" href="https://zwlevonian.medium.com/integer-linear-programming-with-pulp-optimizing-a-draftkings-nfl-lineup-5e7524dd42d3">
        Integer Linear Programming with PuLP: Optimizing a DraftKings NFL lineup
    </a></h3>
    Basic introduction to ILP with Python.
  </li>
  <li>
    <span class="post-meta">{{ "2018-11-06" | date: date_format }}</span>
    <h3><a class="post-link" href="https://zwlevonian.medium.com/https-medium-com-zwlevonian-prototyping-a-handheld-with-the-omega2-fcc0545f06c2"
        style="text-decoration: none">
        Prototyping a handheld with the Omega2: A complete beginner's guide
    </a></h3>
    Tutorial for making a battery-powered handheld.
  </li>
</ul>

<!-- ## Posts:

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul> -->

## Short posts

<ul class="post-list">
  {%- for post in site.posts -%}
    {%- if post.tags contains "short" -%}
    <li>
      {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
      <span class="post-meta">{{ post.date | date: date_format }}</span>
      <h3>
        <a class="post-link" href="{{ post.url | relative_url }}">
          {{ post.title | escape }}
        </a>
      </h3>
      {%- if site.show_excerpts -%}
        {{ post.excerpt }}
      {%- endif -%}
    </li>
    {%- endif -%}
  {%- endfor -%}
</ul>


## Other writing stuff

<ul class="post-list">
  <li>
      Conference reading lists for <a
          href="https://zwlevonian.medium.com/my-chi-2022-reading-list-6595d5fa901e">CHI 2022</a> and <a
          href="https://zwlevonian.medium.com/21-cscw-2021-papers-to-read-b7b651f2e0a3">CSCW 2021</a><br>
      Short summaries of recommended human-computer interaction papers.
  </li>
  <li>
      Annotated source lists for <a
          href="https://zwlevonian.medium.com/why-not-use-linear-regression-for-star-ratings-58c0cd0e5dae">using
          linear regression for ordinal variables</a> and <a
          href="https://zwlevonian.medium.com/information-theory-crowdsourced-sources-15c1ec66ab3e">information
          theory</a><br>
      Short lists of useful sources on a particular topic.
  </li>
  <li>
      <a href="https://grouplens.org/blog/are-bots-ravaging-online-encyclopedias/"
          style="text-decoration: none">
          Are Bots Ravaging Online Encyclopedias?
      </a>
      [<a href="https://github.com/levon003/wiki-ores-feedback/tree/master/reu2021">code</a>]<br>
      October 2021. Blog post written by Abby Newcomb and Sokona Mangane about our work together
      during the <a href="https://reu.cs.umn.edu/">UMN REU program</a>. (I was a research mentor.)
  </li>
  <li>
      <a href="https://web.archive.org/web/20230102083258/https://www.wlnjournal.org/archives/v41/41.3-4.pdf"
          id="smt-simple" name="smt-simple" style="font-style: italic; text-decoration: none">
          A Reflection on Reflective Writing Center Work [pdf]</a><br>
      November 2016. Journal article published in <em>WLN: A Journal of Writing Center Scholarship</em>, authored by Renata Fitzpatrick, Julia Kroll, and myself while I was a Lead Writing Consultant at the <a href="https://www.carleton.edu/writing-center/">Carleton College Writing Center</a>.
  </li>
  <li>
      <a
          href="https://meta.wikimedia.org/wiki/Research:ORES_Inspect:_A_technology_probe_for_machine_learning_audits_on_enwiki">
          ORES Inspect: A technology probe for machine learning audits on English Wikipedia
      </a><br>
      2021-Present. I'm working on a side-project to audit the vandalism detection classifiers used on Wikipedia.
  </li>
</ul>