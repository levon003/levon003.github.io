---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: home
title: Blog Index
permalink: /blog/
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


## Posts hosted on other sites

<ul>
  <li>
      <a href="https://zwlevonian.medium.com/how-would-you-deal-with-an-ambiguous-problem-data-science-interview-question-891638470572">
          How would you deal with an ambiguous problem?
      </a><br>
      May 2022. Conceptual workflow for scoping Data Science problems.
  </li>
  <li>
      <a href="https://zwlevonian.medium.com/model-vs-modeler-trade-offs-designing-interactive-text-classification-interfaces-cda41c367e89">
          Model vs Modeler: Trade-offs designing interactive text classification interfaces
      </a><br>
      March 2022. Accessible summary of my IUI 2022 paper.
  </li>
  <li>
      <a href="https://nbviewer.org/github/levon003/ml-visualized/blob/master/_notebook/BoWLinRegTweets.ipynb">
          Basics of machine learning with text data: bag-of-words for linear regression
      </a><br>
      October 2021. Twitter data workshop presented to undergraduate HCI researchers.
  </li>
  <li>
      <a href="https://zwlevonian.medium.com/integer-linear-programming-with-pulp-optimizing-a-draftkings-nfl-lineup-5e7524dd42d3">
          Integer Linear Programming with PuLP: Optimizing a DraftKings NFL lineup
      </a><br>
      November 2020. Basic introduction to ILP with Python.
  </li>
  <li>
      <a href="https://zwlevonian.medium.com/https-medium-com-zwlevonian-prototyping-a-handheld-with-the-omega2-fcc0545f06c2"
          style="text-decoration: none">
          Prototyping a handheld with the Omega2: A complete beginner's guide
      </a><br>
      November 2018. Tutorial for making a battery-powered handheld.
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


## Short posts & other writing stuff hosted on other sites

<ul>
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
      Renata Fitzpatrick, Julia Kroll, Zachary Levonian<br>
      <em>WLN: A Journal of Writing Center Scholarship.</em> 2016.
      I was a Lead Writing Consultant at the Carleton College Writing Center,
      and we wrote this journal article about our experience.<br>
  </li>
  <li>
      I created a few biographies on English Wikipedia.<br>
      You can find links and read more about my editing on <a
          href="https://en.wikipedia.org/wiki/User:Suriname0">my user page</a>.
  </li>
  <li>
      <a
          href="https://meta.wikimedia.org/wiki/Research:ORES_Inspect:_A_technology_probe_for_machine_learning_audits_on_enwiki">
          ORES Inspect: A technology probe for machine learning audits on English Wikipedia
      </a>
      I'm working on a side-project to audit the vandalism detection classifiers used on Wikipedia.
  </li>
</ul>