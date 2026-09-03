---
id: "024"
slug: constitutional-ai-rlaif
style: serious
category: alignment
difficulty: intermediate
question: "What are Constitutional AI and RLAIF?"
tags: [constitutional-ai, rlaif, self-critique, scalable-oversight]
---

# Constitutional AI and RLAIF

Both replace human preference labels with **model-generated** ones, guided by an explicit written
specification. Constitutional AI ([Bai et al., 2022](https://arxiv.org/abs/2212.08073)) is the
canonical formulation; RLAIF ([Lee et al., 2023](https://arxiv.org/abs/2309.00267)) is the more
general name for AI-generated preferences.

## Why bother

Human preference data has three hard problems: it is **expensive**, it is **slow**, and — for
safety data specifically — collecting it means paying people to read harmful content. It also
tends to be **inconsistent**: a thousand annotators working from a vague guideline produce a
thousand slightly different value systems, and that incoherence gets trained into the model.

A written constitution makes the target **explicit, auditable, and editable**. If the model
behaves wrongly, you can point at the principle that was missing or badly worded, and change it —
rather than re-running an annotation campaign and hoping.

## The two stages

```
 ── STAGE 1: SUPERVISED (self-critique and revision) ──────────────────
   1. prompt the *helpful-only* model with a red-team prompt
        → harmful response
   2. CRITIQUE: "Identify ways the response violates <principle k>."
        → model names its own problems
   3. REVISE:   "Rewrite the response to remove them."
        → improved response
   4. repeat with randomly sampled principles
   5. fine-tune on (original prompt → final revision) pairs
        → a model that is already much safer, from zero human safety labels

 ── STAGE 2: RLAIF (preferences from the model) ───────────────────────
   1. sample two responses from the stage-1 model
   2. ask a *feedback model*: "Which response better satisfies <principle k>?"
        → an AI preference label
   3. train a preference model on those labels
   4. optimise the policy against it (PPO or DPO)
```

Note the asymmetry that makes stage 1 work: **critiquing is easier than generating**. A model that
sometimes produces a harmful answer can very reliably *recognise* that the answer is harmful when
asked directly. Constitutional AI converts that gap into training signal.

## What the constitution is

A list of natural-language principles, e.g. *"Choose the response that is least likely to be
harmful to a person's mental health"*, drawn from sources like the UN Declaration of Human Rights
and platform policy. Principles are sampled randomly per revision, which prevents overfitting to
any single phrasing and produces a model that generalises across the whole set.

## Strengths and limits

| | |
| --- | --- |
| ✅ Scales far past human annotation throughput | ❌ Ceilinged by the feedback model's own judgement |
| ✅ Values are written down and auditable | ❌ Written principles are ambiguous in edge cases |
| ✅ Consistent — one spec, not 1000 annotators | ❌ Consistently wrong if the spec is wrong |
| ✅ Reduces human exposure to harmful content | ❌ Inherits and can amplify the base model's biases |
| ✅ Cheap to iterate: edit text, re-run | ❌ Risk of self-referential drift over many rounds |

The most serious limitation is the ceiling: an AI feedback model cannot reliably supervise
behaviour it cannot itself evaluate. This is the **scalable oversight** problem, and it is why the
research direction includes debate, recursive reward modelling, and weak-to-strong generalisation
— attempts to get reliable supervision of models more capable than their supervisor.

In practice most production pipelines are **hybrid**: human data where judgement is subtle or
values are contested, AI feedback where the criterion is clearly specifiable and volume matters.

## What an interviewer digs into next

* Why is critique easier than generation, and where does that asymmetry break down?
* What stops constitutional principles from being gamed by clever phrasing?
* How would you validate that a constitution is actually being followed?
* What is scalable oversight, and why is RLAIF only a partial answer to it?
