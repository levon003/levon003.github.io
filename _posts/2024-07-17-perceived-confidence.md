---
layout: post
title:  "Research paper: Multimodal, multi-class bias mitigation for predicting speaker confidence"
date:   2024-07-17
tags: research short
excerpt: "Educational Data Mining (EDM) 2024 paper on predicting perceived speaker confidence."
---

Andrew Emerson presented ["Multimodal, Multi-Class Bias Mitigation for Predicting Speaker Confidence"](https://zenodo.org/records/12729896) at [Educational Data Mining (EDM) 2024](https://educationaldatamining.org/edm2024/), an active project at [Educational Testing Service (ETS)](https://www.ets.org/) to predict a speaker's confidence.

It seems clear why ETS might want to predict a speaker's confidence:
 - Build feedback tools that help people understand how confident they come across
 - Build teaching tools that help people improve their projected confidence
 - Build evaluation tools for assessing confidence in educational environments e.g. to assist in grading classroom presentations
 - Build evaluation tools for assessing confidence in occupational environments e.g. to assist in evaluating job candidates' interview performance

Evidently, a mix of reasonable and controversial applications.
What struck me as interesting about this task is the way it does or does not resemble more conventional "digital physiognomy" tasks like emotion detection.

Notably, "confidence" is a construct defined by both self-perception and external perception. 
_Perceived_ confidence - which is what they try to predict in the paper - is the more important characteristic in the context of e.g. job interviews or other high-stakes social situations. 
So automated detectors focused on predicting a person's external perception seem ethical to me in a way that inferring _self_-perception is not.

In the paper, they also make the interesting choice to annotate the videos they collected for perceived gender, age, race, and non-native English speaking. I suspect this is actually more valuable than collecting demographic data from participants (who were Amazon Mechanical Turkers answering a common interview question via webcam) because - again - the relevant factor in a high-stakes social setting is the assumptions made by your assessors.

An ETS psychologist developed a rubric for annotating perceived confidence with six components:

 - Eye gaze
 - Gestures and body movement
 - Posture
 - Vocal variation
 - Facial expression
 - Speaking pace

![Perceived confidence table, with full text from the paper linked above.](/images/perceived_confidence.png){:style="display:block; margin-left: auto; margin-right: auto;"}
*The rubric for perceived confidence: a screenshot of Table 1.*

The multi-modal models they train achieve an F1 score of ~0.6; this is clearly a hard and subjective task. Unfortunately, they used an external contractor for annotation so we don't get per-item [interrater reliability]({% post_url 2024-05-17-disagreement %}).
I think the rubric is interesting, and I'd love to see more work exploring perceptions of confidence in various social settings and cultural contexts.
