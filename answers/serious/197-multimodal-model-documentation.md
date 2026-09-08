---
id: "197"
slug: multimodal-model-documentation
style: serious
category: multimodal
difficulty: intermediate
question: "What should a multimodal model's documentation actually say?"
tags: [model-cards, datasheets, disclosure, intended-use, limitations, provenance]
---

# Documenting a multimodal model

A model card is not marketing and it is not a legal shield. It is the document that lets somebody
else decide whether your model is safe to use for **their** problem — a decision they cannot make
from a leaderboard number.

```
   WHAT THE LEADERBOARD SAYS          WHAT THE READER NEEDS TO DECIDE
   ─────────────────────────          ───────────────────────────────
   MMMU: 64.3                         at what resolution? (q121)
   DocVQA: 91.7                       how many visual tokens, at what cost? (q165)
   "supports 30 languages"            in the VISION path too? which scripts? (q123)
   "safety aligned"                   in the image channel? (q139) in which
                                      languages? (q193)
   "trained on web data"              synthetic captions? (q146) what did the
                                      aesthetic filter remove? (q190)

   the left column is comparable. Only the right column is ACTIONABLE.
```

## What is specific to multimodal

Text model cards are established. Multimodal adds fields that are routinely missing and routinely
matter:

* **Input resolution and tiling behaviour.** The single most consequential undisclosed parameter
  (question 121). A benchmark run at 1344px and a default of 336px are different models to a user.
* **Visual token budget and its cost implications** (question 165), because it determines whether
  the model is affordable at the user's volume.
* **Which modalities are actually supported, and to what depth.** "Supports video" may mean
  eight sampled frames (question 126). Say which.
* **Language coverage of the *vision* path.** OCR and text-in-image performance varies enormously by
  script and is almost never documented (questions 106, 123).
* **Whether the vision path was safety-trained** (question 139), and in which languages
  (question 193).
* **Training data provenance**: what the vision tower was pretrained on, whether captions were
  synthetic (question 146), and what filtering was applied — including what the aesthetic filter
  removed (question 190).

## The sections that carry the weight

**Intended use, and out-of-scope use.** The second is more useful than the first and is usually
vaguer. "Not validated for medical imaging, biometric identification, or documents in
non-Latin scripts" tells a reader something. "Should not be used for harmful purposes" tells them
nothing.

**Evaluation, with the blind baseline.** Report benchmark numbers alongside the text-only baseline
(question 147). Without it a reader cannot tell how much of your score is vision.

**Known failure modes, specifically.** Counting beyond four, spatial relations, small text below a
stated size, negation, multi-image reasoning. Every one of these is a documented general weakness
(questions 122, 128, 137); a card that does not mention them is either untested or not saying.

**Disaggregated performance.** By language, by script, by image type, by demographic group where
people are depicted (question 184). An aggregate is not a disclosure.

**Versioning.** Model version, date, and what changed. Downstream users in regulated contexts
(question 187) cannot pin what you do not version.

## The honesty test

The test for a good card is simple: **does it tell a reader something that would make them not use
the model?** A card containing no such statement has not been written for the reader.

That includes the uncomfortable version — "this model has not been evaluated in the languages most
of your users speak", "the vision safety training covers English only", "our aesthetic filter
removed most documents from the training set". These statements cost something to write and they
are the entire value of the document.

## What an interviewer digs into next

* Why is resolution the most consequential undisclosed multimodal parameter?
* Why is the out-of-scope section more useful than the intended-use section?
* Why must a benchmark number be reported with its blind baseline?
* What is the test for whether a model card was written for the reader?
