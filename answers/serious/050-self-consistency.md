---
id: "050"
slug: self-consistency
style: serious
category: prompting
difficulty: intermediate
question: "What is self-consistency decoding?"
tags: [self-consistency, majority-vote, sampling, test-time-compute, verifier]
---

# Self-consistency

Sample `k` independent chains of thought at non-zero temperature, extract the final answer from
each, and take the **majority vote** ([Wang et al., 2022](https://arxiv.org/abs/2203.11171)).

```
   question ──┬─► chain 1: ... ──► 42   ┐
              ├─► chain 2: ... ──► 42   │
              ├─► chain 3: ... ──► 17   ├─► tally: 42×4, 17×1, 8×1
              ├─► chain 4: ... ──► 42   │
              ├─► chain 5: ... ──►  8   │   → answer: 42
              └─► chain 6: ... ──► 42   ┘
```

Reported gains at the time: +17 points on GSM8K, +12 on AQuA. It remains one of the most reliable
prompting-level interventions.

## Why it works

**There are many valid reasoning paths to a correct answer, and errors are idiosyncratic.** Correct
reasoning converges on the same answer from different directions; mistakes are diverse and scatter.
So the correct answer accumulates votes while wrong answers split them.

This is precisely the ensembling argument, applied at inference time to a single model rather than
across models. It also connects to a broader principle: **marginalise over the reasoning path rather
than maximising over it.** The question is *"what answer is most likely?"*, not *"what is the most
likely single chain?"* — and greedy decoding answers the wrong one of those.

Temperature matters as a result: `T = 0` makes all `k` samples identical and the method degenerates
to plain CoT. You need genuine diversity, typically `T ≈ 0.7`.

## Scaling

Accuracy rises with `k` and saturates — most of the benefit arrives by `k ≈ 5–10`, with diminishing
returns to 40. Cost is linear in `k`, so this is a straightforward accuracy-for-compute trade and one
of the earliest clear demonstrations of **test-time compute scaling**.

## Limits

* **Requires an extractable, comparable final answer.** Majority voting needs answers you can
  compare for equality — numbers, multiple choice, short spans. It does not apply to essays or code
  (though you can vote on *test outcomes* for code).
* **Confidently wrong models stay wrong.** If a systematic misconception drives 5 of 6 chains to the
  same wrong answer, voting confirms it. Self-consistency corrects *random* error, not *bias*.
* **`k`× cost and latency**, though the samples parallelise.
* **Diversity can collapse** on heavily RLHF'd models, which have low output entropy — reducing the
  method's effectiveness on exactly the models people deploy.

## The family it belongs to

Self-consistency is the simplest member of a general pattern: **generate many candidates, then
select**.

| Method | Selection mechanism |
| --- | --- |
| Self-consistency | majority vote |
| Best-of-n | reward model or LLM judge |
| Verifier-guided | a trained verifier scores each chain |
| Weighted self-consistency | vote weighted by chain likelihood or verifier score |
| Tree-of-thought | search over partial chains with backtracking |
| Reasoning models | RL-trained to do the search *within* one chain |

The trend line is clear: this family established that inference-time compute buys accuracy, and
reasoning models are the result of training that behaviour in rather than orchestrating it from
outside. Self-consistency remains valuable because it needs no extra models, no training, and about
ten lines of code.

## What an interviewer digs into next

* Why does self-consistency fail on systematic errors?
* What temperature would you use, and why is `T=0` useless here?
* How would you apply this to code generation?
* When is best-of-n with a reward model better than majority voting?
