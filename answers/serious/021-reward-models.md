---
id: "021"
slug: reward-models
style: serious
category: alignment
difficulty: intermediate
question: "What is a reward model and how is it trained and evaluated?"
tags: [reward-model, bradley-terry, goodhart, reward-hacking, rewardbench]
---

# Reward models

A reward model `r_θ(x, y)` maps a (prompt, response) pair to a scalar approximating human
preference. It exists because RL needs a reward for millions of rollouts and humans cannot supply
them.

## Architecture and training

Take the SFT model, replace the language-modelling head with a scalar head reading the final
token's hidden state, and train on pairwise comparisons with the **Bradley-Terry** loss:

$$\mathcal{L} = -\mathbb{E}_{(x,y_w,y_l)}\left[\log \sigma\big(r_\theta(x,y_w) - r_\theta(x,y_l)\big)\right]$$

```
        prompt x + response y
                 │
        ┌────────▼─────────┐
        │  transformer     │  ← initialised from the SFT policy
        │  (frozen-ish or  │
        │   fully trained) │
        └────────┬─────────┘
                 │ hidden state of the LAST token
        ┌────────▼─────────┐
        │  linear → scalar │
        └────────┬─────────┘
                 ▼
             r(x, y) ∈ ℝ

   loss pushes  r(x, y_chosen)  above  r(x, y_rejected)  by a soft margin
```

Only *differences* are meaningful — the loss is invariant to adding a constant per prompt, so the
absolute scale is arbitrary and comparisons across prompts are not meaningful. Initialising from
the policy matters: the reward model needs the same competence to evaluate a response that the
policy needed to produce it.

## Why pairwise

Absolute ratings from humans are noisy, drift over a labelling session, and vary between
annotators. Comparisons are far more stable. Bradley-Terry is the standard way to turn a set of
pairwise outcomes into a latent scalar — the same model used for chess Elo.

Common refinements: `k`-way rankings decomposed into all `C(k,2)` pairs from one prompt (much
cheaper per pair, and pairs from the same prompt cancel prompt-level difficulty); margin terms
when annotators report *how much* better; and ensembles to detect where the reward is uncertain.

## Evaluation

* **Pairwise accuracy** on held-out preferences — the basic metric, typically 65–80%. Note the
  ceiling: human-human agreement is often only ~70–80%, so a "perfect" reward model is not 100%.
* **RewardBench**-style suites, which break accuracy down by category (chat, reasoning, safety)
  and include adversarial pairs where the wrong answer is longer or better formatted.
* **Best-of-n reranking** — sample `n` responses, take the highest-scoring, measure downstream
  quality. This tests the reward model where it is actually used.
* **Over-optimisation curves** ([Gao et al., 2022](https://arxiv.org/abs/2210.10760)) — plot true
  quality against KL from the initial policy. The curve rises, peaks, and *falls*. The peak
  location tells you how much optimisation the reward model can support before Goodharting.

That last one is the most important idea here: **a reward model is only valid near the
distribution it was trained on**, and optimising against it eventually destroys the thing you
wanted.

## Failure modes

* **Length bias** — the most reliably documented one. Longer responses score higher, essentially
  regardless of content.
* **Format bias** — markdown headers, bullet points, and bold text score higher.
* **Sycophancy** — agreement with the user's stated view scores higher.
* **Distribution shift** — the reward model was trained on `π_SFT` samples but is queried on
  `π_φ` samples, which move away from it during training.
* **Reward hacking** — the policy finds high-scoring degenerate text.

Mitigations: reward-model ensembles and uncertainty penalties, periodic retraining on fresh
on-policy samples, explicit length normalisation, and — where possible — replacing the learned
reward with a **verifiable** one (unit tests, a proof checker, an exact-match grader), which
cannot be Goodharted the same way.

## What an interviewer digs into next

* Why is the reward model's absolute scale meaningless?
* Explain the over-optimisation curve and how you would choose where to stop.
* How would you diagnose length bias, and how would you fix it?
* When can you replace a learned reward model with a verifiable reward?
