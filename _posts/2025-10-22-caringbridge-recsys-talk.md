---
layout: post
title:  "CSCW best paper: \"Peer Recommendation Interventions for Health-related Social Support\""
tags: [research, caringbridge, hci, cscw, recsys, "peer support", health]
excerpt: "Using recommendations to help people find peer support online. Adaptation of a talk at CSCW 2025."
---

_This post is an adaptation of my CSCW 2025 presentation, which is available [on YouTube](https://youtu.be/Mq-BPlyFlmk). A shorter summary was previously published [here]({% post_url 2025-02-25-caringbridge-recsys-paper %})._

Back in 2021, I did a study looking at the feasibility of peer recommendation interventions for health-related social support.
The [published paper](https://arxiv.org/abs/2209.04973) just won a [Best Paper award](https://medium.com/acm-cscw/announcing-the-best-of-cscw-2025-a95517e67ba3) at CSCW 2025.

[Social support](https://en.wikipedia.org/wiki/Social_support) is a key determinant of mental and physical health.
We also know that support is particularly important during health journeys. 
But, a lot of the social support that people undergoing a health journey might benefit from is unavailable in their existing support networks.
In particular, people benefit from support specifically from others with similar but potentially uncommon experiences.

Unfortunately, actually finding and connecting with these people – with _peers_ – is logistically hard. 
For example, it’s one of the reasons hospitals organize condition-specific support groups.
Fortunately, the internet exists!

![Finding peers is hard. Online health communities offer the ability to find a community of peers.](/images/cbrecsys/s1.png){:style="display:block; margin-left: auto; margin-right: auto;"}
*Finding support during health journeys is not easy. [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*

Online communities organized around health (creatively called [online health communities](https://en.wikipedia.org/wiki/Online_health_communities)) offer the promise of a space where people can seek and receive support.
But even in online health communities we have a _discovery_ problem.

Imagine a highly-motivated support seeker:

 - I have some kind of support need in mind.
 - I’m interested in connecting with peers.
 - …now I need to wade through thousands of forum threads.
 
Not great.

There are a lot of design opportunities here, but a suggestion that comes up again and again is _recommendation_.

Read a [Computer-Supported Cooperative Work](https://en.wikipedia.org/wiki/Computer-supported_cooperative_work) paper looking at an online health community, one of the design implications will probably involve improving peer recommendation systems. (I [wrote a paper](https://arxiv.org/abs/2007.16172) like that too.)
But empirical research on systems designed for connecting peers in online health communities is remarkably rare.

My challenge to the community is to treat recommendation as a serious intervention into people’s social networks.
That means we need to design the intervention with particular health benefits in mind.

In this case, we’re designing our intervention to increase two behaviors that are plausibly associated with health benefits:
 1. Reading about the experiences of peers
 2. Interacting with peers

In general, we don’t know that recommendation will actually increase these behaviors, nor do we know that increasing these behaviors is actually linked with health benefits.
This is a classic “causal gap”: we have some associational evidence that manipulation could help, but no strong causal evidence.

![Recommendation can increase: reading about peer experiences, interacting with peers. Behaviors are associated with benefits.](/images/cbrecsys/s2.png){:style="display:block; margin-left: auto; margin-right: auto;"}
*Two behaviors that we hope are associated with health benefits. [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*



The associational evidence _is_ quite good.
For example, we ran our study on CaringBridge.org, a health blogging platform.
On CaringBridge, receiving interactions from peer blog authors was associated with an additional 6 blog posts and an additional 3 months of activity on the site.

![Recommendation can increase number of blog posts and months on platform, based on 200,000 CaringBridge blogs with at least one interaction.](/images/cbrecsys/s3.png){:style="display:block; margin-left: auto; margin-right: auto;"}
*Associational evidence shows a relationship between peer interactions and online behaviors. [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*

That’s a huge effect size… _if_ there’s a strong causal relationship between peer interaction and engagement.

What we want is to evaluate [efficacy](https://en.wikipedia.org/wiki/Efficacy#Medicine).
Will the recommendation intervention actually increase desired behaviors?
The conventional next step is to run a randomized controlled trial (RCT).
But running an RCT is hard and expensive! 
There are too many open questions about the intervention, and too many [degrees of researcher freedom](https://en.wikipedia.org/wiki/Researcher_degrees_of_freedom) to collect high-quality evidence.
Instead, let’s run a _feasibility study_ first.

<!--![Feasibility studies involve collecting evidence in multiple areas. In this case: demand, practicality, acceptability, and implementation.](/images/cbrecsys/s4.png){:style="display:block; margin-left: auto; margin-right: auto;"}
*Adapted from [Bowen et al. 2009](https://pubmed.ncbi.nlm.nih.gov/19362699/). [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*-->

This concept comes mostly from the health sciences (see [Bowen et al. 2009](https://pubmed.ncbi.nlm.nih.gov/19362699/)) and is greatly underused in human–computer interaction research.
We will try to collect some data about efficacy, but our focus is on all the preliminaries: 

1. The _demand_ for the intervention
2. The _acceptability_ of the intervention to participants
3. How _practical_ and adaptable the intervention is
4. Specific challenges in _implementation_

Our goal is to triangulate overall feasibility by collecting evidence in each of these areas. 

## System design

By embracing the feasibility study mindset, we want to be practical.
Email notifications are common on CaringBridge.
So, we copied the design of existing author notifications into a new “blog recommendation email” with five links.

![Email notifications are common CaringBridge.](/images/cbrecsys/s5.png){:style="display:block; margin-left: auto; margin-right: auto;"}
*[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*


To generate recommendations, we trained a deep learning recommendation model from historical interaction data we already had.
The goal of a feasibility study is to surface useful insights, so we also did a bunch of experiments about what data it’s useful to have if you’re trying to do this… see the [paper appendices](https://arxiv.org/abs/2209.04973) for details.

## Field study

![Flowchart showing the progression of the field study.](/images/cbrecsys/s6.png){:style="display:block; margin-left: auto; margin-right: auto;"}
*Field study flowchart and timeline. [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*


We threw up a recruitment banner and got CaringBridge authors to take a survey. 
We got 79 people to sign up for 12 weeks of emails.
Then we collected data for 3 months after the study so we could estimate efficacy over a slightly longer term.

<div class="aside" markdown="1">

**Sidebar: Recruitment survey** <br>
We got a bunch of interesting data in the recruitment survey. The table below shows the percentage of the ~100 respondents who checked various _motivations_ for connecting with peers and various _characteristics_ that make a peer connection valuable.

| Motivations for peer connection     | % checked | Desired peer characteristics  | % checked |
| ----------------------------------- | --------- | ----------------------------- | --------- |
| Learn from others                   | 80%       | Similar diagnosis or symptoms | 84%       |
| Communicate with peers              | 46%       | Similar treatment             | 54%       |
| Receive experienced support         | 44%       | High-quality writing          | 51%       |
| Mentor newer authors                | 29%       | Same caregiver relationship   | 32%       |
| Not interested, but maybe in the future | 6%        | Lives near me                 | 25%       |
| Never interested                    | 2%        | Similar cultural background   | 14%       |
| Not interested, but maybe in the past   | 0%        |                               |           |
| Something else                      | 9%        | Something else                | 8%        |

</div>


Here are our results, condensed to one image: 

![No evidence of negative impact on retention or engagement. 2 “bad” recommendations. “Even with all I’m going through I’ve come to care about these people whose blogs I am following. …. So I’m really really grateful you guys have done this." 589 return visits, 680 likes, 268 comments, 24 follows.](/images/cbrecsys/s7.png){:style="display:block; margin-left: auto; margin-right: auto;"}
*Summary of results. [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*

No apparent harms, either qualitatively or in terms of retention and engagement.
One participant objected to 2 recommendations, otherwise people mostly didn’t give us feedback on the recommendations.
We also heard some really nice feedback from participants.

Recommendations didn’t seem to hurt, and they caused hundreds of new likes and comments.
Now, we have the confidence to do a full-blown RCT.

During this study, we learned a bunch of fiddly, practical things that I hope will be really helpful for other people designing peer recommendation systems.
If you’re interested in peer recommendation or peer matching at all, [check out the paper](http://arxiv.org/abs/2209.04973) for more details.

Here's the full paper citation:

>Zachary Levonian, Matthew Zent, Ngan Nguyen, Matthew McNamara, Loren Terveen, and Svetlana Yarosh. 2025. Peer Recommendation Interventions for Health-related Social Support: a Feasibility Assessment. _Proc. ACM Hum.-Comput. Interact._ 9, 2, Article CSCW146 (April 2025), 59 pages. <https://doi.org/10.1145/3711044>

A preprint is available on arXiv: <http://arxiv.org/abs/2209.04973>
