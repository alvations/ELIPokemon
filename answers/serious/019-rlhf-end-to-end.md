---
id: "019"
slug: rlhf-end-to-end
style: serious
category: alignment
difficulty: intermediate
question: "Walk me through RLHF end to end."
tags: [rlhf, reward-model, ppo, kl-penalty, preference-data]
---

# RLHF end to end

Reinforcement Learning from Human Feedback
([Christiano et al., 2017](https://arxiv.org/abs/1706.03741);
[Ouyang et al., 2022](https://arxiv.org/abs/2203.02155)) has three phases.

```
 ┌── PHASE 1: SFT ─────────────────────────────────────────────────────┐
 │  pretrained model + (prompt, ideal response) demos                  │
 │  → π_SFT, an obedient assistant. Also the reference model later.    │
 └────────────────────────────┬────────────────────────────────────────┘
                              ▼
 ┌── PHASE 2: REWARD MODEL ───────────────────────────────────────────┐
 │  sample k responses per prompt from π_SFT                           │
 │  humans rank them → pairs (chosen y_w, rejected y_l)                │
 │  train r_θ (usually π_SFT with a scalar head) on the Bradley-Terry  │
 │  loss:   L = −log σ( r_θ(x,y_w) − r_θ(x,y_l) )                      │
 │  → a learned proxy for "what humans prefer"                          │
 └────────────────────────────┬────────────────────────────────────────┘
                              ▼
 ┌── PHASE 3: RL OPTIMISATION (PPO) ──────────────────────────────────┐
 │  repeat:                                                            │
 │    1. sample prompt x, generate y ~ π_φ(·|x)                        │
 │    2. score  r = r_θ(x, y)                                          │
 │    3. penalise drift:  R = r − β · KL[ π_φ(y|x) ‖ π_SFT(y|x) ]      │
 │    4. PPO update on π_φ using advantages from a value head          │
 └─────────────────────────────────────────────────────────────────────┘
```

## Why a reward model instead of asking humans directly

RL needs a scalar reward for *every* rollout — millions of them. Humans cannot be in that loop.
So you distil human judgement into a network once, then query it for free. The reward model is
the bottleneck of the whole method: it is a **proxy**, and every failure of RLHF is ultimately a
failure of that proxy.

Ranking rather than absolute scoring matters too. Humans are unreliable at "rate this 1–10" and
comparatively reliable at "which of these two is better", so the data collection is built around
comparisons and the Bradley-Terry model converts them into a scalar.

## Why the KL penalty is non-negotiable

Without it, PPO finds the reward model's adversarial inputs — degenerate text that scores highly
and reads terribly. This is **reward hacking**, and it is not a rare edge case; it is the default
outcome. The KL term anchors the policy near `π_SFT`, keeping generations on the distribution
where the reward model's judgements are meaningful. `β` is the central knob: too low and you get
gibberish with a great score, too high and nothing changes.

## The four moving models

At PPO time you are holding: the **policy** (training), the **reference** (frozen, for KL), the
**reward model** (frozen), and a **value model** (training). That is roughly 4× the memory of
plain fine-tuning and a nightmare to implement correctly. This engineering burden is the single
biggest reason DPO — which needs only the policy and the reference — became popular.

## Known failure modes

* **Reward hacking / Goodharting** — the proxy is optimised until it decouples from the goal.
* **Length bias** — humans mildly prefer longer answers; the reward model amplifies it; RLHF'd
  models become verbose. Length-controlled evaluation exists because of this.
* **Sycophancy** — agreeing with the user is preferred by raters, so it is reinforced.
* **Diversity collapse** — output entropy falls; RLHF'd models are noticeably less varied, which
  matters for creative use and for generating training data.
* **Rater quality is the ceiling.** Preferences from underspecified guidelines produce
  underspecified models. Much of the real work in RLHF is writing the rubric.

## What an interviewer digs into next

* Derive the Bradley-Terry loss and say why ranking beats absolute scoring.
* What exactly does the KL penalty prevent, and what happens as `β → 0`?
* How would you detect reward hacking during a run?
* Why is length bias so persistent, and how do you correct for it in evaluation?
