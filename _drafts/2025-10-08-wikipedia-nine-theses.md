---
layout: post
title:  "Designing for better visibility on Wikipedia: A reaction to Sanger's Nine Theses"
tags: [wikipedia, governance, online communities, design, research, short]
excerpt: "Proposals for Wikipedia."
---

Controversial Wikipedia co-founder Larry Sanger recently published the [Nine Theses](https://en.wikipedia.org/wiki/User:Larry_Sanger/Nine_Theses) on an essay on Wikipedia but also in [_The Free Press_](https://www.thefp.com/p/i-founded-wikipedia-heres-how-to-fix-it).
(See coverage in [_The Signpost_](https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost/2025-10-02/News_and_notes) and [_Politico_](https://www.politico.com/newsletters/digital-future-daily/2025/10/02/the-speech-wars-come-for-wikipedia-00591844).)

The "theses" are changes Sanger wants made to governance on Wikipedia. They are:

>1. End decision-making by 'consensus.'
>2. Enable competing articles.
>3. Abolish source blacklists.
>4. Revive the original neutrality policy.
>5. Repeal 'Ignore all rules.'
>6. Reveal who Wikipedia’s leaders are.
>7. Let the public rate articles.
>8. End indefinite blocking.
>9. Adopt a legislative process.

Each proposal has a huge essay associated with it.

He also lists a few other proposals that have much less elaboration: 

- Prohibit editing without an account ("IP editing")
- Add term limits and yearly performance reviews for Administrators
- Start a repository of memorial articles (written or approved by a person's next of kin)
- Lower the standards required for a subject to have a Wikipedia article
- Some form of age-based "adult content" warning for Wikipedia articles
- Do partnerships with independent organizations for oversight
- "Replace or augment the edit counter with work assessments."
- Allow off-site coordination and canvasing (["meatpuppetry"](https://en.wikipedia.org/wiki/Wikipedia:Sockpuppetry#Meatpuppetry))

I've been a regular Wikipedia editor since 2021, so I wanted to respond to some of these proposals.

## 1. End decision-making by 'consensus.'

[Consensus]() is one of the most interesting aspects of Wikipedia's bureaucracy.
In my opinion, it's a key ingredient in the secret sauce that makes Wikipedia work.
The basic idea of consensus is that when one person objects to content of a Wikipedia article, they can change it. If others object to that change, they should have a discussion about it, coming to a "consensus" view about what should be done.
(This is called the ["Bold -> Revert -> Discuss"]() cycle.)

It's commonly said that Wikipedia ["works in practice, but not in theory"](), and consensus-driven decision making is a perennial target of criticism because the incentives seem poorly aligned to make asynchronous discussions an effective way to make decisions that are accetable to everyone.

Sanger echoes this complaint:

>[Early Wikipedia governance] never made proper allowances for the harsh reality that there would be truly intractable disagreements, even among people who say they agree with the framework of neutrality—some people simply refuse to let others have their say _at all_, or not in any fair way.

Sanger provides no specific examples of perverse outcomes that arise from current consensus processes; he gestures instead at a general opposition to including a plurality of viewpoints in Wikipedia articles.

Instead, I'll provide an example: the [WP:MEDRS](https://en.wikipedia.org/wiki/WP:MEDRS) policy.
Wikipedia's policies requires that all information in Wikipedia articles should be [verifiable](https://en.wikipedia.org/wiki/WP:V) in [reliable](https://en.wikipedia.org/wiki/WP:RELIABLE) published sources.
Functionally, that restricts the inclusion of material not included in reliable sources.

That means a viewpoint included in a Wikipedia article isn't just some person's opinion... it's some person's opinion that some _other_ person published.
Wikipedia relies heavily on the existence of other people's publishing processes to determine what deserves attention in an article or even which topics deserve an article at all.  
As you can imagine, that puts a lot of pressure on the definition of "reliable" when looking at a published source.

[WP:MEDRS](https://en.wikipedia.org/wiki/WP:MEDRS) is a policy that defines a stricter definition of "reliable" for biomedical information.
Most biomedical claims on Wikipedia need to be sourced to a systematic review paper published in "reputable medical journals", a medical journal, or a position statement "from reputable national or international expert bodies".

The intent of WP:MEDRS is probably obvious: to avoid including potentially false or harmful biomedical information.
The existence of this policy leads to the exclusion of viewpoints on medical-adjacent topics that would otherwise be included.

As an example, take the article on [apple cider vinegar](https://en.wikipedia.org/wiki/Apple_cider_vinegar).
Like other vinegars, apple cider vinegar has an [interesting history](https://thewholeu.uw.edu/2015/07/07/beyond-the-hype-apple-cider-vinegar-as-an-alternative-therapy/) as an alternative home therapy for everything from heart health to weight loss.
However, the way that WP:MEDRS is used in practice prevents the inclusion of this history in the Wikipedia article. As of October 2025, Wikipedia contains the following two sentences on apple cider vinegar as a home remedy, in a section titled "Health effects":

>Evidence for apple cider vinegar having any health effect is poor, such as for weight loss, glycemic control or skin infections. Its use is not recommended for any therapy in medical guidelines of major public health organizations or regulatory agencies.

This provides almost no information about how or why people use apple cider vinegar, and reads as weirdly defensive and non-neutral!

![Bowl of apple cider vinegar.](/images/apple_cider_vinegar.jpg){:style="display:block; margin-left: auto; margin-right: auto;"}
*Apple cider vinegar. Source: Veganbaking.net, [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0), via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Apple_Cider_Vinegar_(4108653248).jpg)*

WP:MEDRS is a good example of good intentions creating "non-neutral" outcomes 
You may personally agree with this policy; clearly, the editors who created it have good intentions. (See ["Why MEDRS?"](https://en.wikipedia.org/wiki/Wikipedia:Why_MEDRS) – a ridiculously condescending essay – for more background.)
But I predict it's exactly the kind of thing that Sanger objects to.

It is easy to continue generating examples of consensus processes going awry.
The problem is "simple": it's not at all obvious how to do better!

## 2. Enable competing articles.

This is a straight-foward solution to the apple cider vinger problem,
Unfortunately, it comes with a host of complications.
Without going into detail here, I'll just say I think this idea is unworkable and based on some very likely false premises (such as that allowing competing articles would increase the number of willing Wikiepdia editors by at least a factor of ten).

I do think this idea is at least interesting.
There's a research idea here: get an LLM to dynamically re-write articles for particular readers.

An example of a Wikipedia article that Sanger objects to is the article on [Yahweh]().
A Christian or Jewish "reader view" might start with the contemporary Christian view before providing context on the XX diety that is the focus of the current article.

Clearly, there are versions of this that are horrible ideas; but small shifts in presentation may make Wikipedia articles much more useful for some readers.

Good touchpoint: this WMF proposal (notably hated by the community) https://en.wikipedia.org/wiki/Wikipedia:Village_pump_(technical)/Archive_221#Simple_summaries:_editor_survey_and_2-week_mobile_study

## 3. Abolish source blacklists.

Wikipedia's [Perennial sources](https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources/Perennial_sources) list.

>This is a non-exhaustive list of sources whose reliability and use on Wikipedia are frequently discussed. This list summarizes prior consensus and consolidates links to the most in-depth and recent discussions from the [reliable sources noticeboard](https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources/Noticeboard) and elsewhere on Wikipedia.


[Spam blacklist](https://en.wikipedia.org/wiki/Wikipedia:Spam_blacklist)
[_Manning Publications_](https://en.wikipedia.org/wiki/Manning_Publications) – a fairly well-known publisher of software engineering books – is on the spam blacklist. 
Some enterprising promoter seemingly used [multiple accounts](https://en.wikipedia.org/w/index.php?title=Wikipedia_talk:WikiProject_Spam&oldid=499832796#Long_term_book_seller_spam) to promote ''Manning'' back in 2012, and they've been banned ever since (after a [declined request for unlisting](https://en.wikipedia.org/wiki/MediaWiki_talk:Spam-blacklist/archives/April_2015#manning.com) in 2014).

## 4. Revive the original neutrality policy.

I have little to say about Sanger's complaints here, since they seem primarily to be based on a misunderstanding 

>Critique this claim: You say you want to avoid giving “equal validity” or “false balance” to competing views. Such jargon was introduced by ideological journalists in the late 1990s, in order to openly reject traditional ideas of journalistic objectivity or neutrality.

## 5. Repeal 'Ignore all rules.'


## 6. Reveal who Wikipedia’s leaders are.
## 7. Let the public rate articles.
## 8. End indefinite blocking.
## 9. Adopt a legislative process.

Now, turning to the less formal proposals:

## Replace the Edit Counter with Work Assessments

>The edit counter has helped create an insider class that does not deserve the degree of power it wields in the system. Some of the most qualified people in the world have little time to edit Wikipedia, and so they will naturally not make many edits. But their opinion about their field of expertise ought to be worth more than that of a teenager with 50,000 edits. If not replaced, then maybe the edit counter could be augmented by independent work assessments (_i.e._, performance evaluations) by open source LLMs and other automated tools. It would be best to move away from the simplistic metric of edit counts and towards a more nuanced evaluation of contributions based on content quality and impact. This would reflect a true measure of a contributor’s value to the project, if that is regarded as important. The use of automated tools for this task would help keep it free of corruption and cronyism. 

Isaac Johnson at the Wikimedia Foundation has been developing some research on [edit types](https://meta.wikimedia.org/wiki/Research:Wikipedia_Edit_Types).

[taxonomy](https://meta.wikimedia.org/wiki/Research:Wikipedia_Edit_Types/Python_package#Edit_Types_Taxonomy)

[`mwedittypes`](https://gitlab.wikimedia.org/repos/research/edit-types)