---
id: "022"
slug: ppo-for-llms
style: serious
category: alignment
difficulty: advanced
question: "Explain PPO in the context of language model alignment."
tags: [ppo, policy-gradient, advantage, clipping, gae]
---

# PPO for language models

Proximal Policy Optimization ([Schulman et al., 2017](https://arxiv.org/abs/1707.06347)) is a
policy-gradient method whose defining feature is that it takes **several gradient steps per batch
of rollouts without letting the policy move too far**. That matters for LLMs because generating
rollouts is by far the expensive part.

## Mapping the RL vocabulary onto text

| RL concept | LLM instantiation |
| --- | --- |
| State `s_t` | prompt + tokens generated so far |
| Action `a_t` | the next token |
| Policy `π_φ(a\|s)` | the language model's next-token distribution |
| Episode | one complete response |
| Reward | reward-model score at the **final** token only |
| Discount `γ` | usually 1 (short episodes, terminal reward) |

The reward is **sparse and terminal**: one scalar for a 500-token response. Credit assignment
across those tokens is the whole difficulty.

## The objective

$$L^{\text{CLIP}}(\phi) = \mathbb{E}_t\left[\min\left(\rho_t A_t,\;
\text{clip}(\rho_t, 1-\epsilon, 1+\epsilon)A_t\right)\right],
\qquad \rho_t = \frac{\pi_\phi(a_t|s_t)}{\pi_{\phi_{\text{old}}}(a_t|s_t)}$$

```
   effect of the clip on the surrogate objective

   A_t > 0 (this token was better than expected)
        │        ┌──────────  clipped: no more reward for
   obj  │      ╱ │            pushing ρ beyond 1+ε
        │    ╱   │
        │  ╱     │
        └──┼─────┼──────────────► ρ
          1-ε   1+ε

   A_t < 0 (worse than expected)  → mirrored: no unbounded push below 1-ε
```

Without clipping, a single batch could push some token's probability to 1.0 based on one noisy
advantage estimate. Clipping caps the incentive to move any individual token's likelihood far
from where it started, which is what makes multiple epochs per rollout batch safe.

## Advantages: GAE and the value head

`A_t = Q(s_t,a_t) − V(s_t)` — how much better this token was than the baseline expectation.
`V` is a learned **value head** (another head on a transformer, often sharing the reward model's
initialisation), and advantages are computed with **GAE**, exponentially averaging `n`-step
returns with parameter `λ` to trade bias against variance.

Subtracting a baseline does not change the gradient's expectation but massively reduces its
variance — which is the only reason policy gradients work on 500-token sequences at all.

## The full per-token reward

$$R_t = \underbrace{r_\theta(x,y)\cdot\mathbb{1}[t = T]}_{\text{terminal RM score}}
\;-\;\beta\,\underbrace{\log\frac{\pi_\phi(a_t|s_t)}{\pi_{\text{ref}}(a_t|s_t)}}_{\text{per-token KL}}$$

The KL term is applied *per token*, not once at the end, which gives dense shaping and keeps the
policy anchored to the SFT reference everywhere in the sequence.

## Why it is hard in practice

* **Four models resident** — policy, reference, reward, value.
* **Rollout generation dominates wall-clock** — you are running inference inside a training loop.
* **Hyperparameter sensitivity** — `β` (KL), `ε` (clip), `λ` (GAE), rollout batch size, epochs per
  batch, value-loss coefficient. Small changes flip runs between "no learning" and "collapse".
* **The value head is hard to fit.** Predicting the eventual reward-model score from a partial
  generation is genuinely difficult, and a bad value function means high-variance advantages.

That last problem motivated **GRPO**, which deletes the value model entirely and estimates the
baseline by sampling a group of responses to the same prompt and using their mean reward. Same
variance-reduction idea, no critic to fit.

## What an interviewer digs into next

* Why clip the ratio rather than use a hard KL constraint (TRPO)?
* Why does subtracting a baseline reduce variance without biasing the gradient?
* Where should the KL penalty be applied and why per-token?
* What does GRPO remove, and what does it lose by removing it?
