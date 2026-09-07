---
id: "147"
slug: multimodal-benchmarks-contamination
style: serious
category: multimodal
difficulty: intermediate
question: "Why are multimodal benchmark scores so unreliable?"
tags: [benchmarks, contamination, blind-baseline, saturation, mmmu, evaluation-design]
---

# Reading multimodal benchmarks honestly

Multimodal leaderboards move fast and mean less than they appear to. The reasons are specific and
checkable, and every one of them is something you can test for on any benchmark you are handed.

## The blind baseline is the first thing to run

**Give the model the question and no image.** Whatever it scores is the floor — the part of the
benchmark answerable from language priors, world knowledge and answer-option structure alone.

```
   benchmark X, reported:        68%
   same model, image removed:    54%      ← the "visual" benchmark is 54% not visual
   random chance (4 options):    25%

   the visual capability being measured is the gap: 14 points, not 68.
```

Published blind baselines on several well-known multimodal benchmarks are far above chance. Some
questions are answerable from general knowledge ("what colour is a stop sign"); some from answer
options that give the game away; some because only one option is grammatical.

Run this before you believe any multimodal number, including your own.

## The other structural problems

* **Contamination.** Benchmark images and questions are on the web, and web-scale training corpora
  contain them. For images this cannot be checked by string match — you need perceptual hashing
  against the training set, and almost nobody publishes having done it.
* **Answer-option bias.** Models have position preferences among multiple-choice options. Shuffle
  the options and rescore; a real capability is invariant, a preference is not. This catches more
  problems than it should.
* **Single-frame answerability in video benchmarks** (question 126) — the same disease, one modality
  over.
* **Saturation.** Once a benchmark is at 90%, the remaining 10% is disproportionately label errors
  and ambiguous items. Movement in that range is noise or overfitting, not progress. Several
  standard sets have measured label error rates of several percent.
* **Prompt sensitivity.** Multimodal scores swing several points on formatting alone — where the
  image sits relative to the question, whether options are lettered, whether a chain-of-thought is
  requested. A comparison across models with different prompts is not a comparison.
* **Judge-based scoring for open-ended answers** inherits everything in question 038, plus a
  multimodal twist: the judge often cannot see the image, so it grades plausibility rather than
  correctness.

## What to do instead

**Build a small evaluation on your own data.** A hundred examples from your actual distribution,
labelled by someone who knows the domain, beats any public leaderboard for deciding what to ship.
It is not contaminated, it measures what you care about, and you can inspect every failure.

For public benchmarks, report defensively:

* the score **and** the blind baseline;
* the exact prompt and image placement;
* option-shuffled results for multiple choice;
* the model version and date;
* and per-category breakdowns, since aggregate multimodal scores average across capabilities that
  have nothing to do with each other — OCR, counting, spatial reasoning and world knowledge are not
  one skill.

## The uncomfortable implication

A model can top a leaderboard, be genuinely better on that leaderboard, and be **no better at
looking at images** — if the gain came from language priors, option formatting, or having seen the
test set. That is not a hypothetical failure of evaluation; it is the default outcome unless
somebody checks. The check costs one extra run with the images removed.

## What an interviewer digs into next

* How would you check whether a multimodal benchmark is actually multimodal?
* Why can't image contamination be detected the way text contamination is?
* What does option-shuffling reveal?
* Why are per-category breakdowns more informative than an aggregate score here?
