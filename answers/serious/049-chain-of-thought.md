---
id: "049"
slug: chain-of-thought
style: serious
category: prompting
difficulty: core
question: "What is chain-of-thought prompting and why does it help?"
tags: [chain-of-thought, reasoning, test-time-compute, faithfulness]
---

# Chain-of-thought

Prompt the model to produce intermediate reasoning before its final answer
([Wei et al., 2022](https://arxiv.org/abs/2201.11903)). Either by few-shot examples that show worked
reasoning, or zero-shot by appending *"Let's think step by step"*
([Kojima et al., 2022](https://arxiv.org/abs/2205.11916)).

The gains on multi-step tasks were large — GSM8K roughly tripling for large models — and the effect
is scale-dependent: below a few billion parameters, CoT often *hurts*, because the model produces
plausible-looking reasoning that is wrong and then commits to it.

## Why it works: the compute argument

This is the explanation that actually holds up.

A transformer performs a **fixed** amount of computation per token: `L` layers, one forward pass, no
loops. A problem requiring more sequential steps than `L` cannot be solved in a single forward pass,
regardless of how large the model is.

Generating tokens changes that. Each generated token is another forward pass, and previously
generated tokens are readable from context. So the model uses the token stream as **external
scratch memory**, converting a hard depth limit into a soft length budget.

```
   WITHOUT CoT                      WITH CoT
   ───────────                      ────────

   "23 × 17 = ?" ──► [L layers] ──► "391"
                     one pass       (guess — the model must do
                                     all steps in fixed depth)

   "23 × 17 = ?" ──► "23 × 10 = 230"  ──► [L layers]
                 ──► "23 × 7 = 161"   ──► [L layers]   each step is a
                 ──► "230 + 161 = 391"──► [L layers]   FULL forward pass
                 ──► "391"                              reading the last

   depth limit  L  →  effective depth  L × (number of tokens)
```

This is formalised in work showing constant-depth transformers are in a limited complexity class,
while transformers with a polynomial-length chain of thought can simulate polynomial-time
computation ([Merrill & Sabharwal, 2023](https://arxiv.org/abs/2310.07923)).

A secondary mechanism: CoT conditions the model on its own intermediate statements, keeping later
tokens in a region of the distribution where the correct answer is more likely. Writing "230" makes
"391" much more probable than it was from the raw question.

## The faithfulness problem

The stated reasoning is **not necessarily the actual reason** for the answer.
[Turpin et al. (2023)](https://arxiv.org/abs/2305.04388) biased models by always making answer (A)
correct in the few-shot examples, then observed models choosing (A) on new questions while
constructing plausible reasoning that never mentioned the pattern. The chain was post-hoc
rationalisation.

The consequence matters for anyone building on this: **a chain of thought is not an explanation you
can audit.** It is a computation aid that happens to be human-readable. Do not use it as a safety
mechanism, and be careful using it as an interpretability tool.

## Practical variants

* **Zero-shot CoT** — "think step by step". Free, works surprisingly well.
* **Few-shot CoT** — demonstrate the reasoning style you want. Better, costs prompt tokens.
* **Self-consistency** — sample `k` chains, majority-vote the answer. Reliable gains, `k`× cost.
* **Least-to-most** — decompose into subproblems, solve in order.
* **Program-of-thought** — emit code and execute it. Strictly better for arithmetic: an actual
  interpreter cannot make an arithmetic slip.
* **Structured scratchpads** — for extraction and classification, an explicit intermediate schema
  beats free-form prose.

## When not to use it

* Simple lookups and classification — it adds latency and can *reduce* accuracy by talking the model
  out of a correct first instinct.
* Latency-sensitive paths.
* When the model has native reasoning (an o1/R1-style model), where CoT prompting is redundant and
  can interfere with the model's own trained procedure.

Note that modern reasoning models have effectively internalised CoT: they were RL-trained to produce
long chains before answering, which is why prompting them to "think step by step" adds little.

## What an interviewer digs into next

* Why does a fixed-depth transformer need CoT for multi-step problems?
* Why does CoT hurt small models?
* What is unfaithful reasoning and why does it matter for safety?
* When would you use program-of-thought instead?
