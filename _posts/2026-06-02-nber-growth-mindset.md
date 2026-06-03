---
layout: post
title:  "Research paper: Efficacy of Social Belonging and Growth Mindset interventions among college students"
tags: [research, education, psychology, "growth mindset", short]
excerpt: "May 2026 NBER working paper finds null results for nudge-style mindset interventions."
---

A new NBER working paper finds null results for [social belonging](https://en.wikipedia.org/wiki/Belongingness) and [growth mindset](https://en.wikipedia.org/wiki/Mindset#Fixed_and_growth_mindsets) interventions for first-year college students.
The paper is ["The (Lack of) Efficacy of Social Belonging and Growth Mindset Interventions Among College Students"](https://www.nber.org/papers/w35230) by Abid Alam, Philip Oreopoulos, and Uros Petronijevic. Here's the abstract:

>Using four large-scale experiments across two major Canadian universities, we experimentally evaluate the effects of growth mindset and social belonging interventions on student outcomes. In a sample of nearly 12,000 students, we find no immediate or dynamic effects on student grades and no effect on persistence through university. We further combine survey and administrative data with machine learning methods to explore treatment effect heterogeneity, finding no evidence of meaningful variation in treatment effects across student subgroups. Despite the recent promise of these light-touch interventions, our findings indicate further research is required to identify the contexts in which their benefits generalize.
 
Both types of interventions involved an invitation to complete an online survey and an online module. Students were incentivized to participate "by assigning a small participation grade of 1-2% of the total course grade for completion." The interventions were delivered from 2015 to 2019 at two Canadian universities: the University of Toronto and York University. All together, ~12,000 students enrolled in first-year economics classes were invited to complete the survey.

To my mind, this is a classic [nudge](https://en.wikipedia.org/wiki/Nudge_theory) intervention; a small lift for participants, so the best we can hope for is small effect sizes.

### What was in the online modules?

The social belonging intervention:

>Students randomly assigned to the belonging intervention read short descriptive stories from a diverse body of upper-year students. These stories were designed to convey the message that worries about belonging are common during academic transition and, with time, they should expect these feelings to dissipate as they meet others like themselves, become more familiar with their surroundings, and settle into a routine. The stories also illustrated that there are others like them who faced and overcame similar struggles. The students were then asked to write a short script on how this message resonated with their own experiences to date, and were told that these responses might be used to help future cohorts.

The growth mindset intervention:

>Students who were randomly assigned to the intervention first read information about the brain and how it learns new information. The content emphasized that by exerting effort through practicing and learning, the brain can be developed and abilities can be improved. In addition, the messages emphasized that working on strategies along with exerting effort can be beneficial. This was followed by scripts that conveyed personal experiences and responses from upper-year students who received the same information. After going through the articles and responses, students were asked to reflect on the information presented to them and were again informed that these responses may be used to help future incoming students.

Again, this is a small nudge: 30-60 minutes of eductional readings and written reflection.

### What effect did this have on students?

The authors used information about students' grades and enrollment status to track students during their subsequent years in college.

First of all, the big outcome: did the interventions affect 5-year student graduation rates? No, the pooled treatment effect across both interventions was very close to zero and swamped by a large standard error.

Well, maybe that's not so surprising. What about for shorter-term academic outcomes? Did the interventions improve student grades in the semester they received the intervention? Also no. The intervention *slightly* improved final course grade (by 0.1 percentage points... out of 100!), but the effect is again indistinguishable from zero.

They do a lot of additional sub-group analyses, but the overall punchline is clear: this intervention did not have a detectable effect on students' academic performance.

### What can we learn from this study?

I've previously helped [build growth mindset interventions](https://arxiv.org/abs/2407.04915) for students onboarding to a math practice tool, so I was really interested by this result. "Mindset" interventions failing to replicate is nothing new, but this is a particularly large and high-quality study.

One point the authors make: a follow-up survey for students who received the growth mindset intervention did indicate increased growth mindset attitudes. So taking the module does change students minds... but those changes are either too small or not relevant to academic performance in the university context where the intervention was delivered.

If I wanted to keep investigating mindset interventions, I would probably attempt to measure to what degree the beliefs these interventions are designed to change are present in my target population. The authors write:

>Another possible explanation for our results is that the targeted psychological constraints are not sufficiently present or binding in our setting. These interventions are designed to address specific barriers—such as fixed beliefs about intelligence or uncertainty about belonging—and may not be effective unless such barriers exist and constrain performance. When these constraints are weak or absent the scope for improvement is limited ([McPartlan et al., "Testing Basic Assumptions Reveals When (Not) to Expect Mindset and Belonging Interventions to Succeed"](https://eric.ed.gov/?id=EJ1280132)).

I wish that the initial survey had asked students about their existing mindset. That would let you explicitly measure the impact of the intervention in the most favorable possible case: does the intervention help students who *start* with a fixed mindset? In other words, do students *with fixed mindsets* who *subsequently increase their growth mindset attitudes* do better academically? If so, there might be something to salvage here. If not... then we may be mistaken about the relevance of a fixed mindset for many academic outcomes we care about.
