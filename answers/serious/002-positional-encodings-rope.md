---
id: "002"
slug: positional-encodings-rope
style: serious
category: transformers
difficulty: core
question: "Why do transformers need positional encodings, and how does RoPE work?"
tags: [positional-encoding, rope, alibi, extrapolation]
---

# Positional encodings and RoPE

Self-attention is a **set** operation: it computes a weighted sum over tokens, and sums are
permutation-invariant. Shuffle the input and the attention output is shuffled identically —
the layer literally cannot tell *"dog bites man"* from *"man bites dog"*. Positional encodings
are how order gets injected back in.

## The three families

```
 ┌───────────────────────────────────────────────────────────────────────────┐
 │ ABSOLUTE (sinusoidal / learned)      x_i  ←  x_i + p_i                     │
 │   position added to the embedding once, at the bottom of the stack         │
 │   ✗ learned variants cannot go past trained length at all                  │
 ├───────────────────────────────────────────────────────────────────────────┤
 │ RELATIVE (T5 bias, ALiBi)            score_ij  ←  q_i·k_j + b(i-j)         │
 │   a bias on the attention logits that depends only on distance             │
 │   ✓ extrapolates; ✗ ALiBi's linear decay bakes in a recency prior          │
 ├───────────────────────────────────────────────────────────────────────────┤
 │ ROTARY (RoPE)                        q_i ← R_i q_i ,  k_j ← R_j k_j        │
 │   rotate q and k by an angle proportional to position                      │
 │   ✓ absolute to apply, relative in effect; the modern default              │
 └───────────────────────────────────────────────────────────────────────────┘
```

The original paper used **fixed sinusoids**, `p_{pos,2i} = sin(pos/10000^{2i/d})`, chosen so
that `p_{pos+k}` is a linear function of `p_{pos}` — the model can in principle learn relative
offsets. GPT-2 used **learned** absolute embeddings instead, which work well in-distribution
and fail hard beyond the trained length, because position 4097 has no vector.

## RoPE: rotate, don't add

[RoPE](https://arxiv.org/abs/2104.09864) treats each pair of dimensions of `q` and `k` as a
point in a 2-D plane and rotates it by `mθ`, where `m` is the token's position and `θ` is a
frequency fixed per dimension pair (`θ_i = 10000^{-2i/d}`, the same geometric ladder as the
sinusoids). Nothing is added to the residual stream; only `q` and `k` are rotated, inside
every attention layer.

```
 dimension pair (2i, 2i+1) viewed as a plane:

        position 0            position 3            position 7
            ↑ q                   ↑                     ↑
            │                    ╱                   ╲  │
            │  q             q  ╱                     ╲ │
        ────┼────►        ────┼────►               ────┼╲───►
            │                  ╲                       │ ╲ q
                                                       
        rotate by 0·θ         rotate by 3·θ         rotate by 7·θ
```

The magic is what happens in the dot product. For a 2-D rotation matrix,

$$(R_m q)^\top (R_n k) = q^\top R_{n-m} k$$

The absolute rotations cancel and leave a function of `n − m` alone. So you apply an
**absolute** transform per token — cheap, cacheable, no `n × n` bias matrix — and get a
**relative** attention score for free. Low-frequency dimension pairs rotate slowly and encode
coarse, long-range position; high-frequency pairs rotate fast and encode fine local order.

## Extending context

Because RoPE is a continuous function of position, you can stretch it rather than retrain:

* **Position interpolation** ([Chen et al., 2023](https://arxiv.org/abs/2306.15595)) — divide
  positions by a factor `s`, squeezing 8k positions into the 2k range the model was trained
  on. Cheap and needs only light fine-tuning, but it compresses local resolution.
* **NTK-aware / YaRN scaling** — interpolate the *low* frequencies (long-range) while leaving
  the *high* frequencies (local order) alone, so you do not blur adjacent-token distinctions.
* **Raising the base θ** (10 000 → 500 000 or more) during a long-context training phase, which
  is what most current long-context models actually do.

Naïvely feeding a RoPE model longer sequences than it was trained on degrades sharply: the
rotations reach angles the model has never seen, and attention logits go out of distribution.

## Tradeoffs worth stating

| | Sinusoidal | Learned absolute | ALiBi | RoPE |
| --- | --- | --- | --- | --- |
| Params | 0 | `n_max × d` | 0 | 0 |
| Extrapolates | weakly | no | yes | with scaling |
| Works with KV cache | yes | yes | yes | yes (rotate on write) |
| Long-range recall | ok | ok | biased to recent | good |

## What an interviewer digs into next

* Why does RoPE go on `q` and `k` but never on `V`?
* If RoPE is relative, why does the model still degrade past its training length?
* What breaks if you apply RoPE *before* caching keys vs after?
* When would ALiBi's recency bias be a feature rather than a bug?
