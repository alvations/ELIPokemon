---
id: "033"
slug: speculative-decoding
style: serious
category: inference
difficulty: advanced
question: "What is speculative decoding and why is it lossless?"
tags: [speculative-decoding, draft-model, medusa, eagle, rejection-sampling]
---

# Speculative decoding

Decoding is memory-bandwidth bound: producing one token requires streaming every weight through
the memory system, and the GPU's arithmetic units sit mostly idle. Verifying *ten* tokens costs
almost exactly the same as verifying one, because it is the same weight-streaming pass with a
slightly larger batch dimension.

Speculative decoding ([Leviathan et al., 2022](https://arxiv.org/abs/2211.17192);
[Chen et al., 2023](https://arxiv.org/abs/2302.01318)) exploits that: let a cheap **draft model**
guess several tokens ahead, then have the **target model** check them all in a single forward pass.

```
   step 1: DRAFT (small model, γ = 4 tokens, cheap and sequential)

      "The capital of France is" →  " Paris" " ," " a" " city"

   step 2: VERIFY (target model, ONE forward pass over all 4 positions)

      position:      1        2        3        4        5(bonus)
      draft said:  Paris      ,        a      city       —
      target p:    0.92     0.75     0.11     0.60      ...
                    ✅       ✅       ❌ reject → resample from
                                          the corrected distribution

   accepted: " Paris ,"  + 1 resampled token   → 3 tokens for the price of 1
```

## Why it is exactly lossless

This is the part interviewers want. Acceptance uses **modified rejection sampling**. For a draft
token `x` with draft probability `q(x)` and target probability `p(x)`:

* accept with probability `min(1, p(x)/q(x))`;
* if rejected, sample from the residual distribution `norm(max(0, p(x) − q(x)))`.

The theorem: the resulting token is distributed **exactly** according to `p`. The output
distribution is identical to running the target model alone — not approximately, identically. Any
draft model works, including a terrible one; a bad drafter only lowers the acceptance rate and
therefore the speedup. It can never change what the target model would have said. (With greedy
decoding the rule degenerates to "accept iff the draft token is the target's argmax".)

## Expected speedup

With draft length `γ` and per-token acceptance rate `α`, the expected number of accepted tokens
per verification is

$$\mathbb{E}[\text{tokens}] = \frac{1 - \alpha^{\gamma+1}}{1 - \alpha}$$

At `α = 0.8, γ = 4` that is ~3.4 tokens per target pass. Net wall-clock speedups of 2–3× are
typical. The tradeoff on `γ`: longer drafts mean more wasted draft compute when an early token is
rejected, since everything after a rejection is discarded.

## The variants

* **Draft model** — a small model from the same family (e.g. a 1B drafting for a 70B). Needs the
  same tokenizer, and a second model to host.
* **Self-speculative** — skip layers of the target model to form the draft. No extra weights.
* **Medusa** — add several parallel prediction heads on the target model that guess tokens `t+1`,
  `t+2`, ... simultaneously; verify a tree of candidates. No separate model.
* **EAGLE** — draft in *feature* space rather than token space using the target's own hidden
  states, giving much higher acceptance rates; currently among the strongest approaches.
* **Prompt lookup / n-gram** — for tasks with heavy input copying (summarisation, code editing,
  RAG), draft by simply copying from the prompt. Zero model, surprisingly effective.

## When it does not help

* **High batch sizes.** Speculation spends spare compute, and at large batch you are already
  compute-bound with none to spare. It is a *latency* optimisation for low-concurrency serving,
  and can reduce total throughput.
* **Low acceptance rates.** Poorly matched drafters, high temperature, or highly unpredictable
  content give `α` too low to pay for the draft compute.

## What an interviewer digs into next

* Prove that modified rejection sampling preserves the target distribution.
* Why does a *worse* draft model cost speed but never quality?
* Why doesn't speculative decoding help at batch size 256?
* How would you choose `γ` adaptively during generation?
