---
layout: post
title:  Designing LLM tutors to check for student understanding
date:   2023-11-01
tags: research education llm
excerpt: What can Doug Lemov teach us about designing LLM tutors?
---

In Doug Lemov's book ["Teach Like a Champion"](https://teachlikeachampion.org/) he proposes 62 teaching techniques. [Here's a quick reference](https://teachlikeachampion.org/wp-content/uploads/Teach-Like-a-Champion-2.0-Placemat-with-the-Nanango-Nine.pdf).
Many of the techniques focus on checking for student understanding, a critical skill for teachers and tutors.

Computer scientists like myself have recently been interested in using large language models (LLMs) like ChatGPT to automate part or all of the tutoring process.
(I recently published [a workshop paper at the NeurIPS conference](https://arxiv.org/abs/2310.03184) focused on using LLMs for math-related Q&A, another important component of the tutoring process.)

While LLMs do seem like they have potential for improving tutoring systems, [designs fail when they don't account for user needs](https://www.nngroup.com/articles/top-10-application-design-mistakes/).
Since I don't have a background in education, I've been learning from educators and students about their needs during my work with the [Learning Engineering Virtual Institute](https://learning-engineering-virtual-institute.org).

An underrated way to learn about user needs in a new field is to read published practice guides like Lemov's book.
I think Lemov's techniques have implications for the design of LLM tutors, so in this post I'll describe 9 techniques and how those techniques are relevant for designing LLM tutors. 
(Note that many of these lessons apply just as well to [intelligent tutoring sysystems that don't use LLMs](https://dl.acm.org/doi/10.5555/1435351.1435353) as to those that do!)
All of these design thoughts are very preliminary: please share your own thoughts and experiences designing interactive tutoring systems!

## How can we use Lemov's techniques to improve the design of LLM tutors?

### Technique 1: Replace self-report
#### “Replace functionally rhetorical questions with more objective forms of impromptu assessment.”

Basically, replace “Does that make sense?” or “Does everyone understand?” or “Got it?” with targeted questions.
Goal here is quick, targeted questions.
Questions should be “straightforward and designed to yield short answers that [reveal] student understanding (or the lack of it) quickly.”

**Relevance to LLM tutors:** Ask _specific_ questions to check for understanding. Require more than a binary “I understand, proceed” input from students moving through a lesson or practice problem explanation. LLM-generated text can be integrated alongside structured assessment questions.

### Technique 2: Retrieval practice
#### “Ask a quick series of carefully chosen, open-ended questions directed at a strategic sample of the class and executed in a short time period.”

“The process of causing students to recall information they’ve learned after a strategic delay.”
This is basically spaced repetition stuff.

**Relevance to LLM tutors:** If engaging over a long period of time, return to previous concepts. Memory augmentation techniques, like those used in the [Generative Agents](https://arxiv.org/abs/2304.03442) paper, may be particularly useful here.

### Technique 3: Standardize the format
#### “Streamline observations by designing materials and space so that you’re looking in the same consistent place every time for the data you need.”

“Designing materials and space so that you’re looking predictably for the data you need.”
My uncharitable summary: make it easy to see when students are making mistakes through better process and worksheet design.

**Relevance to LLM tutors**: Design for collecting structured info from students; don't rely exclusively on fallible LLMs for extracting student intent. Further, design prompts to make use of all information available, whether that’s previous answers, lesson context, clicks, [keystrokes](https://www.jowr.org/index.php/jowr/article/view/592), or student attention info from a webcam.

### Technique 4: Active observation
#### “Be intentional about how you scan your classroom. Decide specifically what you’re looking for and remain disciplined about it in the face of distractions.”

My uncharitable summary: write down your observations when you are looking at student work.
In the book, active observation is summarized as “deciding intentionally what to look for and maintaining discipline in looking for what you have prioritized.”

**Relevance to LLM tutors:** Inject at least some highly-structured evaluation questions. This will force you to decide what information you want to collect, and you should also make sure you actually collect that information from students. Choose metrics that are applicable to the specific tutoring application and create summaries that focus on those metrics so that you can track your progress and identify students that would benefit from individual educator attention.

### Technique 5: Show Me
#### “Flip the classroom dynamic in which the teacher gleans data from a passive group of students. Have students actively show evidence of their understanding.”

“Students actively present the teacher with visual evidence of their understanding.”
Includes presenting answers on mini-whiteboards, holding up fingers, etc. 
In fact, Lemov splits these more generally into “slates” and “hand signals”.
A good “Show Me” should: “ask students (1) present objective data, (2) usually in unison, and (3) in a format that the teacher can assess at a glance.”

**Relevance to LLM tutors:** Ask objective questions that can be definitively evaluated by the system. (i.e. questions with one correct answer.) Supplement free-text responses with constrained (modal) responses.

### Technique 6: Affirmative Checking
#### “Insert specific points into your lesson when students must get confirmation that their work is correct, productive, or sufficiently rigorous before moving on to the next stage.”

“The strategic use of checkpoints where students must get confirmation that their work is correct or on target, and that they are ready to move on to the next stage—a new paragraph, a second draft, a harder set of problems, the last step in a lab.”
My uncharitable summary: this is basically the [mastery-based learning](https://www.modernclassrooms.org/blog/what-is-mastery-based-learning) principle.

Lemov emphasises one point: students should _choose_ when they’re ready for the teacher to evaluate their work. “This empowers students to assess their own work first.”

**Relevance to LLM tutors:** Use checkpoints before moving on to more advanced material. e.g. make sure the student can answer a specific practice problem correctly before moving them on to a problem set. Tie LLM interactions tightly to assessment questions.

### Technique 7: Culture of Error
#### “Create an environment where your students feel safe making and discussing mistakes, so you can spend less time hunting for errors and more time fixing them.”

The basic observation: students are trying to “elude discovery” of their errors; need to create a culture where they are comfortable sharing mistakes! Normalize struggle.
Suggested phrases: 
 - “I’m glad I saw that mistake. It teaches us something we have to fix before we’ve mastered this.”  
 - “I like that your first instinct was to use X, but in this situation, we have to use Y.” 
 - “[The context of the problem] makes it very challenging to follow, but X is true and not Y. Let’s take a look at how we know that.” 
 - “What I am asking you to do is difficult. Even teachers struggle with it. But I know we’ll get it, so let’s take a look at what went wrong here…”

“The first [phrase] flips student expectation; the teacher is glad to have seen the mistake. The second gives credit to the student's understanding of the mathematical principles—but makes it clear that she's come up with the right answer for a different setting. The third and fourth acknowledge that the task is not the sort of thing you try just once and get right. They normalize struggle.”

Lemov suggests discussing possible options without revealing the answer. e.g. if there are multiple possible answers, talk through one of the wrong answers first without revealing if it is right or wrong: keep the focus on the reasoning. “Delay revealing whether an answer is right or wrong until after you’ve discussed it.”

**Relevance to LLM tutors:** Give supportive responses to wrong answers, using the specific examples to normalize not succeeding on the first try before providing reasoning. When providing explanations, describe multiple reasoning pathways. Consider explicitly describing [misconceptions](https://github.com/creature-ai/math-misconceptions) that may have led to student mistakes and creating hint sequences break a problem in to steps.
([CRADLE](https://figshare.com/articles/online_resource/CRADLE_Suggests_Assessment_and_genAI/22494178/1) has made similar recommendations.)
<!-- My question: how feasible is it to give supportive explanations? This is basically the hint/explanation generation problem, with an added need to justify the mistake. The example phrases imply a few different strategies that could be used in prompting: flip expectation about whether it’s good to make mistakes, acknowledge that the students’ approach is reasonable (in a different context/problem), and indicating that the task is not one you should succeed on first-try.  -->

### Technique 8: Show Call
#### “Choosing a student’s work and sharing it, visually, with the class so they are not just talking about it but studying it in a durable sustained way.”

“What’s the quickest and most productive way to respond to an error in the midst of teaching, in other words? Often it’s to study the error itself.”
As a technique, Show Call seems very tied to the group learning environment.
“Show Call works because there is learning power in looking: we build students’ perception ability.”  “Show Call can also work by asking students to use comparative judgment—it can place two examples close together and ask students to discern the differences.”

**Relevance to LLM tutors:** Consider adding features that visualize a student's group learning environment, for example by demonstrating other students’ previous work. How LLMs might best support input from multiple students working together is an interesting open research problem.

### Technique 9: Own and Track
#### “Have students correct or revise their own work, fostering an environment of accountability for the correct answer.”

Briefly: have students write down the “right” answer.
 - (1) Make sure students know what the right answer was. 
 - (2) Get “meta” about wrong answers. “Have students take notes on why wrong answers were wrong.”
 - (3) Get “meta” about the right answers, too. “Have students make notes on why correct answers were correct.”

After analyzing an error, know what was correct and _why_.


**Relevance to LLM tutors:** Ask students for answers that include explanations for why alternative answers are wrong.

## Summary

A common theme across many of the teaching techniques is making assessment accessible to the tutor. 
In the context of a tutoring system, that means collecting structured information on how students are doing.
LLMs can complement structured assessment procedures with flexibility, personalized responses, and a more human-like interface.
I would hope that some of these design opportunities could be used to extend the capabilities of math tutoring systems such as [OATutor](https://dl.acm.org/doi/abs/10.1145/3544548.3581574) by using LLMs to provide personalized hints, conversational assessments, and [conceptual Q&A](https://arxiv.org/abs/2310.03184).

_Interested in learning more about learning engineering? Check out the [Learning Engineering Commons](https://learningengineering.com/)._