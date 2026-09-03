---
id: "038"
slug: llm-as-a-judge
style: serious
category: evaluation
difficulty: intermediate
question: "What is LLM-as-a-judge and what biases does it have?"
tags: [llm-as-judge, position-bias, verbosity-bias, self-preference, mt-bench]
---

# LLM-as-a-judge

Use a strong model to grade outputs instead of humans. It is 100–1000× cheaper, returns in seconds,
is perfectly consistent, and — for open-ended generation where no reference answer exists — is
often the only scalable option. [MT-Bench / Chatbot Arena](https://arxiv.org/abs/2306.05685)
reported ~80% agreement between GPT-4 judgements and human preferences, which is roughly the
agreement rate *between humans*.

That framing is the important one: the ceiling is not perfection, it is human-level agreement, and
the judge is already close to it.

## The two protocols

**Pairwise** — "which response is better, A or B?" More reliable, because relative judgements are
easier than absolute ones. Costs `O(n²)` for a full ranking, usually reduced by Elo-style sampling.

**Pointwise** — "score this 1–10 against this rubric." Cheaper and gives absolute numbers, but
scores drift, cluster (everything gets a 7 or 8), and are not comparable across runs.

## The documented biases

**1. Position bias.** The same pair, presented in the opposite order, gets a different winner
disturbingly often. *Fix:* evaluate both orders and average; count disagreement as a tie. This is
not optional.

**2. Verbosity bias.** Longer answers win, controlling for quality. *Fix:* length-controlled
scoring (as AlpacaEval 2.0 does), or explicit rubric instructions penalising padding.

**3. Self-preference bias.** Models rate their own outputs higher
([Panickssery et al., 2024](https://arxiv.org/abs/2404.13076)), plausibly because they assign them
higher likelihood. *Fix:* never let a model be the sole judge of its own family; use a panel of
judges from different families.

**4. Style over substance.** Confident tone, markdown headers, and bullet points score higher
regardless of correctness. Judges are markedly weaker at detecting subtle factual errors than at
assessing presentation.

**5. Sycophancy / anchoring.** Judges can be swayed by an assertion in the prompt about which
answer is expected to be better.

**6. Poor calibration on hard content.** A judge cannot reliably grade reasoning it cannot itself
perform. If your task is harder than the judge, the scores are noise dressed as numbers.

## Making judges reliable

```
   ┌───────────────────────────────────────────────────────────┐
   │ ✅ Pairwise, both orderings, average                       │
   │ ✅ A concrete rubric with named criteria, not "which is    │
   │    better?"                                                │
   │ ✅ Reasoning BEFORE the verdict (judgement quality drops   │
   │    sharply if the verdict comes first)                     │
   │ ✅ A reference answer when one exists — this is the single │
   │    biggest accuracy improvement available                  │
   │ ✅ Few-shot examples of correctly-graded pairs             │
   │ ✅ Allow explicit ties; forcing a winner manufactures noise│
   │ ✅ Validate against ~100 human labels and report agreement │
   └───────────────────────────────────────────────────────────┘
```

That last point is the discipline that separates a usable judge from a comforting one. **A judge is
a model, so it needs its own eval.** Measure agreement with human labels on a held-out set, report
it, and re-measure whenever you change the prompt.

## When not to use one

* When a **verifiable** check exists — unit tests, a schema validator, exact match. Always prefer a
  deterministic checker; it cannot be flattered.
* For **safety-critical** decisions without human review in the loop.
* When the task exceeds the judge's competence.
* As the **optimisation target** for training, without care: optimising against a judge Goodharts
  it exactly as it Goodharts a reward model. (This is the same failure as reward hacking, and it is
  why judge-scored leaderboards drift toward verbose, well-formatted, confident answers.)

## What an interviewer digs into next

* How would you measure and correct position bias?
* Why does requiring reasoning before the verdict improve judgements?
* How would you validate a judge, and what agreement rate is good enough?
* What happens if you train on judge scores?
