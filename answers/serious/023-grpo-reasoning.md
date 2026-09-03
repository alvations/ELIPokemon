---
id: "023"
slug: grpo-reasoning
style: serious
category: alignment
difficulty: advanced
question: "What is GRPO and why is it used for training reasoning models?"
tags: [grpo, rlvr, deepseek-r1, verifiable-rewards, group-baseline]
---

# GRPO and RL with verifiable rewards

**Group Relative Policy Optimization** (introduced in
[DeepSeekMath](https://arxiv.org/abs/2402.03300), made famous by
[DeepSeek-R1](https://arxiv.org/abs/2501.12948)) is PPO with the value model deleted.

PPO needs a baseline to compute advantages, and it learns one with a value head — a network
trained to predict the eventual reward from a partial generation. That is a hard regression
problem, and a poorly fit value function produces high-variance advantages and unstable runs.

GRPO's observation: if you are going to sample anyway, sample **`G` responses to the same
prompt** and use the group's own statistics as the baseline.

$$A_i = \frac{r_i - \text{mean}(r_1,\dots,r_G)}{\text{std}(r_1,\dots,r_G)}$$

```
   PPO                                    GRPO
   ───                                    ────
   prompt ──► 1 response                  prompt ──┬─► response 1 → r=1  ┐
                 │                                 ├─► response 2 → r=0  │
                 ▼                                 ├─► response 3 → r=1  │ group
          ┌─────────────┐                          ├─► response 4 → r=0  │
          │ VALUE MODEL │ predicts baseline        ├─► response 5 → r=1  │
          │  (trained)  │                          ├─► response 6 → r=0  │
          └─────────────┘                          ├─► response 7 → r=0  │
                 │                                 └─► response 8 → r=1  ┘
                 ▼                                            │
          A = r − V(s)                              mean = 0.5, std = 0.53
                                                              ▼
                                            A_i = (r_i − 0.5)/0.53
                                            correct → +0.94, wrong → −0.94
   4 models in memory                       3 models in memory
   value function can be wrong               baseline is measured, not predicted
```

Every token in response `i` receives the same advantage `A_i`, the clipped surrogate objective is
otherwise identical to PPO, and the KL penalty is usually applied directly in the loss rather than
folded into the reward.

## Why this suits reasoning

GRPO is normally paired with **RLVR** — RL from *verifiable* rewards. For a maths problem, run the
answer through a checker. For code, run the unit tests. The reward is `1` or `0`, computed by a
program, and:

* it **cannot be Goodharted** the way a learned reward model can — there is no proxy to exploit,
  only the actual task;
* it needs **no human labels** at all, so you can generate as much signal as you have problems;
* binary rewards make the group baseline especially natural — the mean is just the pass rate, and
  the advantage is "did you do better than your own average attempt".

This combination is what produced the long chain-of-thought behaviour in R1-style models. Nobody
supervised the reasoning traces. The model was rewarded only for final correctness, and *longer
deliberation emerged* because it raised the pass rate — response length grew from hundreds to
thousands of tokens over training, with self-correction ("wait, let me reconsider") appearing
spontaneously.

## Requirements and limits

* **Prompts must be verifiable.** Maths, code, formal logic, structured extraction. Open-ended
  writing has no checker, so RLVR does not apply.
* **The group must have variance.** If all `G` samples are wrong (or all right), the advantages are
  all zero and the prompt teaches nothing. Curriculum difficulty matters: you want problems the
  model solves *sometimes*.
* **Compute cost shifts to sampling.** `G = 8..64` generations per prompt is a lot of inference.
* **Reward hacking still exists**, just in a different place: models find checker bugs, exploit
  test harnesses, or produce answers in formats that trivially match the grader.
* **Bias caveats.** The standard-deviation normalisation over-weights prompts where the model is
  nearly deterministic; variants (Dr. GRPO, and length-normalisation fixes) address a length bias
  in the token-level averaging.

## What an interviewer digs into next

* Why does removing the value model reduce variance rather than increase it?
* What happens to a prompt where all `G` samples get the same reward?
* Why can't you use RLVR for creative writing, and what do you use instead?
* Where does reward hacking show up when the reward is a unit test?
