---
id: "017"
slug: teacher-forcing-exposure-bias
style: serious
category: training
difficulty: intermediate
question: "What are teacher forcing and exposure bias?"
tags: [teacher-forcing, exposure-bias, scheduled-sampling, error-compounding]
---

# Teacher forcing and exposure bias

**Teacher forcing** is how autoregressive models are trained: at every position, condition on
the *ground-truth* prefix rather than on the model's own previous predictions.

$$\mathcal{L} = -\sum_t \log P(x_t \mid x_{<t}^{\text{true}})$$

It exists because it makes training parallel. All positions can be computed in one forward pass
with a causal mask, because every position's input is already known. Without it you would have to
generate token by token during training, and transformers would lose their entire speed
advantage.

## The mismatch

```
  TRAINING (teacher forcing)              INFERENCE (free running)
  ──────────────────────────              ────────────────────────
  input:  The cat sat on the              input:  The cat sat on the
  target:              ▲                  model:                  mat
                       mat                                         │
  next input: ...on the mat  ← TRUTH      next input: ...on the mat ← ITS OWN
                                                                     OUTPUT
  Every step starts from a perfect        One mistake, and every later step
  prefix. The model never sees its        conditions on a prefix the model
  own mistakes during training.           has never been trained on.
```

**Exposure bias** is that gap: the model is only ever *exposed* to ground-truth prefixes, so at
generation time it operates off-distribution, and errors compound. Once it emits a slightly odd
token, the resulting context is unlike anything in training, making the next token more likely to
be odd too.

Visible symptoms: degeneration into repetition loops, drift in long generations, and the way a
single hallucinated fact gets elaborated on confidently for paragraphs — the model is now
faithfully continuing a fictional premise it wrote itself.

## The fixes, and why they mostly lost

* **Scheduled sampling** ([Bengio et al., 2015](https://arxiv.org/abs/1506.03099)) — randomly feed
  the model's own predictions during training, ramping up over time. Helps a little; breaks the
  parallelism that makes transformer training fast, and the estimator is biased.
* **Professor forcing**, sequence-level GAN-style objectives — mostly abandoned; unstable.
* **Minimum risk training / RL on sequence-level rewards** — the model generates, then is scored
  on whole sequences. This is the one that *did* survive, in the form of RLHF: the model samples
  its own continuations and is trained on them, which by construction closes the exposure gap.
* **Sampling discipline at inference** — repetition penalties, nucleus sampling, and
  min-p exist partly to keep generation inside the distribution.

## The modern framing

Exposure bias was a much bigger deal for small seq2seq models than it is for modern LLMs, for two
reasons. First, scale: a model that is right far more often simply enters bad states less. Second,
**RLHF and reasoning-model RL train on self-generated rollouts**, which is exposure-bias
correction whether or not anyone calls it that. This is worth saying explicitly in an interview —
it connects a classic seq2seq problem to why RL post-training helps beyond preference alignment.

## What an interviewer digs into next

* Why does teacher forcing make training parallelisable, precisely?
* Why is scheduled sampling a biased estimator?
* How does RLHF address exposure bias as a side effect?
* Is exposure bias or the ranking/calibration of the output distribution more responsible for
  repetition loops?
