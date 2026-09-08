---
id: "167"
slug: multimodal-preference-tuning
style: serious
category: multimodal
difficulty: advanced
question: "How do you apply RLHF and DPO to vision-language models?"
tags: [rlhf-v, dpo, reward-model, hallucination, reward-hacking, over-refusal]
---

# Preference tuning with an image in the loop

Everything in questions 019-022 applies, plus one structural difference that changes the whole
design: **the reward model must see the image**.

## Why that matters more than it sounds

A text reward model judges a response against a prompt. A multimodal reward model must judge a
response against a prompt **and an image** — and if it cannot see the image well, it grades
plausibility instead of correctness.

```
   response A: "A golden retriever catching a red frisbee on a beach."
   response B: "A golden retriever catching a blue frisbee on a beach."

   text-only reward model: identical. Both fluent, both plausible, no basis to choose.
   image-blind judging therefore rewards FLUENCY, and hallucination survives untouched
   — which is the exact failure it was deployed to fix (question 122).
```

So the reward model needs a vision tower at least as capable as the policy's. A weak judge with a
strong policy is worse than useless: the policy learns to satisfy the judge's blind spots.

## Where the preference data comes from

* **Hallucination-targeted pairs (RLHF-V style).** Take a model response, have an annotator correct
  it **segment by segment** rather than rewriting it. The corrected and uncorrected versions differ
  minimally and *only* on the hallucination, which gives a far cleaner learning signal than two
  independently written responses that differ in a dozen ways.
* **Synthetic negatives.** Take a correct caption, perturb one object, attribute or count. Cheap,
  scalable, and it teaches exactly the discrimination you want. Risk: the model learns to detect
  perturbation artefacts rather than to look.
* **Rejection sampling.** Generate n responses, score with an image-aware judge or a QE-style
  checker, train on the best. Simple, effective, and the standard starting point.
* **Human preference on real traffic**, which is the highest-value and the slowest.

## The failure modes

* **Reward hacking toward hedging.** Penalise hallucination hard and the model learns that vague
  responses are safest: "there appears to be some kind of animal". Technically unfalsifiable,
  useless. Measure **informativeness** alongside accuracy or you will optimise straight into this.
* **Over-refusal.** Multimodal safety tuning (question 139) pushed too hard produces a model that
  refuses to read any image containing text or any photo containing a person. Both directions must
  be measured; improving one alone reliably wrecks the other.
* **Verbosity and position bias** in the judge, inherited wholesale from question 038.
* **Degradation of text-only ability**, as ever (question 148). Mix text-only preference data in.
* **Over-optimisation** against the reward model (question 021) — the same curve, and it arrives
  sooner here because multimodal reward models are weaker.

## Evaluation

Report, at minimum, all four together:

| Axis | Why |
| --- | --- |
| Hallucination rate (POPE/CHAIR, question 122) | the thing you were fixing |
| Informativeness / helpfulness | catches the hedging hack |
| Refusal rate on benign images | catches over-refusal |
| Text-only benchmarks | catches the usual regression |

Any one of these alone can be improved by a model that is worse overall. That is not a hypothetical
— it is the default outcome of optimising a single number.

## What an interviewer digs into next

* Why must the reward model see the image, concretely?
* Why are segment-level corrections a better signal than rewritten responses?
* What does a model do when hallucination is penalised without an informativeness term?
* Why does over-optimisation arrive sooner in the multimodal setting?
