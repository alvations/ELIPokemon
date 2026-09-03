---
id: "034"
slug: sampling-temperature-top-p
style: serious
category: inference
difficulty: core
question: "Explain temperature, top-k, and top-p (nucleus) sampling."
tags: [sampling, temperature, top-p, nucleus, min-p, decoding]
---

# Decoding: temperature, top-k, top-p

At every step the model produces logits over the vocabulary. Decoding is the policy for turning
that distribution into one token. It changes output quality enormously and costs nothing to tune —
which is why it is a favourite interview topic.

## Temperature

$$P(x_i) = \frac{\exp(z_i/T)}{\sum_j \exp(z_j/T)}$$

```
   logits: [3.0, 2.0, 1.0, 0.5]

   T = 0.5  →  [0.84, 0.11, 0.02, 0.01]   sharper — confident, repetitive
   T = 1.0  →  [0.64, 0.23, 0.09, 0.05]   the model's actual beliefs
   T = 2.0  →  [0.42, 0.26, 0.16, 0.12]   flatter — creative, incoherent
   T → 0    →  [1, 0, 0, 0]               greedy / argmax
```

Temperature rescales logits *before* softmax. Crucially it **never changes the ranking**, only the
gaps. `T > 1` flattens, `T < 1` sharpens, `T = 0` is greedy.

## Top-k

Keep the `k` highest-probability tokens, renormalise, sample. Simple, but `k` is fixed while the
distribution's shape is not:

* After *"The capital of France is"* the distribution is a spike. `k = 50` admits 49 junk tokens.
* After *"She opened the door and saw a"* it is genuinely broad. `k = 50` truncates good options.

## Top-p (nucleus)

[Holtzman et al. (2019)](https://arxiv.org/abs/1904.09751): keep the smallest set of tokens whose
cumulative probability exceeds `p`.

```
   sorted probabilities, p = 0.9

   token:     Paris  the   a    Lyon  Nice  ...  (50k more)
   prob:      0.72  0.11  0.05  0.03  0.02       ~0
   cumsum:    0.72  0.83  0.88  0.91 ────────── cut here
                                  ▲
   nucleus = 4 tokens.  In a flat context the same p might keep 400.
```

The nucleus **adapts to the distribution's entropy**, which is exactly what fixed `k` cannot do.
This is why top-p is the standard default.

The paper's motivating observation is worth quoting: maximisation-based decoding (greedy, beam)
produces degenerate repetitive text, because *high-probability* text is not *human-like* text —
humans routinely choose mildly surprising words, and always taking the safest option produces
loops.

## min-p and the newer variants

**min-p** keeps tokens with `P(x) ≥ min_p × P(max)` — a threshold relative to the top token rather
than a cumulative mass. It handles the confident case better (when the top token has 0.9, almost
nothing else survives) while staying permissive when the model is genuinely uncertain. Also in use:
**typical sampling** (keep tokens whose surprisal is near the distribution's entropy),
**η/ε-sampling**, and **repetition/frequency/presence penalties** which subtract from logits of
already-used tokens.

## Choosing settings

| Task | Suggested |
| --- | --- |
| Code, extraction, structured output | `T = 0` (greedy) or `T ≈ 0.1` |
| Factual Q&A, classification | `T ≈ 0.2–0.5`, `top_p 0.9` |
| General chat | `T ≈ 0.7`, `top_p 0.9–0.95` |
| Creative writing, brainstorming | `T ≈ 0.9–1.2`, `top_p 0.95` |
| Generating diverse synthetic data | `T ≈ 1.0+`, high `top_p` |
| Self-consistency / majority voting | `T ≈ 0.7` — you *need* diversity |

Two things worth saying explicitly. First, **stacking temperature and top-p is order-dependent**
and most implementations apply temperature first, then truncate. Second, **`T = 0` is not
deterministic in practice** on GPU: batching and reduction order make floating-point results vary
slightly between runs, which can flip near-ties. Do not promise reproducibility on that basis.

## What an interviewer digs into next

* Why does top-p adapt to uncertainty where top-k cannot?
* Why does maximisation-based decoding produce repetition loops?
* When would you deliberately raise temperature?
* Why isn't greedy decoding bit-for-bit reproducible on a GPU?
