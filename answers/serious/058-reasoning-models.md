---
id: "058"
slug: reasoning-models
style: serious
category: reasoning
difficulty: advanced
question: "How are reasoning models trained, and how do they differ from chat models?"
tags: [reasoning-models, o1, r1, rlvr, thinking-tokens, distillation]
---

# Reasoning models

A reasoning model is one post-trained to **spend tokens deliberating before answering**, with the
deliberation produced as an explicit (often hidden) chain. o1, R1, and their successors.

## How they are trained

The recipe made public by [DeepSeek-R1](https://arxiv.org/abs/2501.12948):

```
  ┌─ base model ────────────────────────────────────────────────────┐
  │                                                                 │
  ├─ (optional) COLD START SFT ────────────────────────────────────┤
  │   a few thousand long, well-formatted reasoning traces          │
  │   purpose: readable output and a stable starting format.        │
  │   R1-Zero skipped this — and produced unreadable, language-      │
  │   mixing reasoning that nonetheless scored well.                 │
  ├─ RL WITH VERIFIABLE REWARDS (the essential step) ───────────────┤
  │   maths, code, logic — problems with checkable answers           │
  │   reward = 1 if the checker passes, 0 otherwise                  │
  │   + a small format reward for using the thinking delimiters      │
  │   algorithm: GRPO (group baseline, no value model)               │
  ├─ REJECTION SAMPLING + SFT ─────────────────────────────────────┤
  │   generate many solutions, keep the correct ones, fine-tune      │
  │   on them; mix in general data to restore breadth                │
  ├─ FINAL RL for helpfulness and safety ──────────────────────────┤
  └─────────────────────────────────────────────────────────────────┘
```

The striking finding: **nobody taught the reasoning.** The reward was only for final correctness. Over
training, response length grew from hundreds to thousands of tokens, and self-verification,
backtracking and re-derivation appeared spontaneously — because they raised the pass rate. The
"aha moment" in the R1 paper is the model writing *"wait, let me reconsider"* unprompted.

## How they differ from chat models

| | Chat model | Reasoning model |
| --- | --- | --- |
| Optimised for | human preference (RLHF) | verifiable correctness (RLVR) |
| Output | answer directly | long internal chain, then answer |
| Tokens per response | 10² | 10³–10⁵ |
| Best at | conversation, writing, breadth | maths, code, logic, planning |
| Prompting | benefits from CoT prompting | CoT prompting is redundant, can interfere |
| Few-shot examples | help | often **hurt** — zero-shot with a clear problem is better |
| Latency | ~1 s | 10–100 s |
| Cost | baseline | 5–50× |

The prompting differences are practical and frequently missed. Reasoning models want the *problem
stated clearly*, not instructions about how to think; adding "think step by step" or few-shot
reasoning examples measurably degrades them, because you are interfering with a procedure they were
trained to run.

## Distillation

R1 also demonstrated that **fine-tuning small dense models on reasoning traces from a large reasoning
model works remarkably well** — a distilled 7B–32B model beating much larger non-reasoning models on
maths. Notably, distillation from a strong reasoner outperformed running RL directly on the small
model: the small model cannot discover the behaviour on its own, but it can imitate it. That is a
significant and slightly counterintuitive result.

## Limits

* **Domain-bound.** RLVR needs verifiable answers. Gains transfer partially to unverifiable domains
  but the training signal does not exist there.
* **Overthinking.** Reasoning models burn thousands of tokens on trivial questions unless the budget
  is controlled.
* **Hidden reasoning.** Providers often hide the chain, so you cannot audit it — and per question 049
  it would not be a faithful audit anyway.
* **Reward hacking against checkers** — exploiting test harnesses rather than solving the problem.
* **Cost and latency** make them wrong for most interactive traffic.

The deployment pattern that follows: **route**. Cheap chat model for most traffic, reasoning model
for the queries that need it, with a classifier deciding.

## What an interviewer digs into next

* Why did long reasoning emerge without being supervised?
* Why do few-shot examples hurt reasoning models?
* Why does distillation beat direct RL for small models?
* How would you decide which queries deserve a reasoning model?
