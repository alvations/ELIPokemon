---
id: "189"
slug: multimodal-data-flywheel
style: serious
category: multimodal
difficulty: advanced
question: "How do you build a data flywheel for a multimodal product?"
tags: [data-flywheel, feedback-loops, active-learning, labelling, drift, privacy]
---

# Turning usage into training data

Every serious multimodal system improves through a loop: real inputs arrive, failures are
identified, they become training data, the model improves, and it attracts more usage. Building that
loop deliberately is usually higher-leverage than any modelling change — and it is where the
compounding advantage lives.

## The loop, and where each stage breaks

```
   real user inputs
        │
        ├─► [1] CAPTURE       ─ consent, retention, PII (question 174)
        │
        ├─► [2] FIND FAILURES ─ this is the hard stage
        │
        ├─► [3] LABEL         ─ expensive; prioritise ruthlessly
        │
        ├─► [4] TRAIN         ─ and hold the mixture (question 148)
        │
        └─► [5] MEASURE ──────┘ on a frozen set the loop cannot touch
```

**Stage 2 is where flywheels die.** You cannot label everything, and random sampling finds mostly
easy successes. What actually surfaces failures:

* **Implicit signals.** The user rephrased the question, zoomed in, retried, abandoned, or corrected
  the output. These are free and abundant, and most teams do not instrument them.
* **Explicit feedback**, which is sparse and biased toward the angry.
* **Model uncertainty**, which is weak on its own (question 122's confident hallucinations) but
  useful combined with the above.
* **Disagreement between two models**, or between a model and a specialist tool (question 176) — one
  of the strongest cheap signals available.
* **Distribution outliers**: inputs unlike anything in training. Cheap to compute with embeddings
  and it finds the genuinely new.

## The trap: the loop optimises for what it can see

A flywheel fed by user retries improves the cases users retry. It is blind to:

* users who **gave up** rather than retried — the worst failures leave the weakest signal;
* use cases you do not have users for **yet**;
* populations under-represented in your traffic, whose failures are proportionally invisible
  (question 184).

So deliberately sample **outside** the feedback signal: a random slice, labelled regardless of
whether anyone complained. It feels wasteful and it is the only thing that finds unknown unknowns.

## The evaluation set must be outside the loop

If your test set is drawn from the same pipeline that produces your training data, it drifts with
it, and you will measure improvement forever while the product does not improve. **Freeze a set,
version it, and label it independently.** Refresh it deliberately and infrequently, and when you do,
report both old and new numbers for a release so the discontinuity is visible.

## Privacy is a design constraint on the loop

User images and audio are the most sensitive data most products handle. Consent for training use
must be explicit and separable from consent to use the product; retention should be bounded; faces
and text should be redacted at capture where the task allows; and deletion must propagate to
training sets, which is an engineering problem people discover far too late. Build the deletion path
before you build the capture path.

## What an interviewer digs into next

* Why does random sampling fail to find failures?
* Which failures leave the weakest signal, and what do you do about it?
* Why must the evaluation set sit outside the flywheel?
* Why build the deletion path first?
