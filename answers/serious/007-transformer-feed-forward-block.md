---
id: "007"
slug: transformer-feed-forward-block
style: serious
category: transformers
difficulty: intermediate
question: "What does the feed-forward (MLP) block in a transformer actually do?"
tags: [ffn, mlp, key-value-memory, swiglu, parameters]
---

# The feed-forward block

Every transformer layer alternates **attention** (mix information *between* tokens) with a
**position-wise feed-forward network** (transform each token independently). The FFN is applied
to every position with the same weights and no interaction between positions:

$$\text{FFN}(x) = W_2\,\sigma(W_1 x + b_1) + b_2, \qquad d_{ff} \approx 4 d_{model}$$

```
   d_model = 4096                    d_ff = 16384                    d_model = 4096
        │                                 │                                │
        ▼                                 ▼                                ▼
   ┌─────────┐    W_1 (up-project)   ┌──────────────────┐   W_2 (down)  ┌─────────┐
   │  token  │ ─────────────────────►│ ████████████████ │──────────────►│  token  │
   │  vector │                       │  σ(·) non-linear │               │ updated │
   └─────────┘                       └──────────────────┘               └─────────┘
        ▲                                                                    │
        └──────────────── residual add ──────────────────────────────────────┘

   Applied INDEPENDENTLY to every position — no token talks to another here.
```

## Where the parameters live

For a standard block: attention has `4·d²` parameters (Q, K, V, O), the FFN has `2·d·d_ff = 8·d²`
with the classic 4× expansion. **Two thirds of a transformer's parameters are in the FFN**, and
in gated variants it is closer to that still. If you are asked "where does an LLM store what it
knows", this is the honest answer.

## What it computes

The most useful interpretation is
[Geva et al. (2021)](https://arxiv.org/abs/2012.14913): the FFN is a **key-value memory**. Rows
of `W_1` act as keys — each fires on a particular input pattern; the corresponding columns of
`W_2` are values — each writes a particular update into the residual stream. The activation
picks which memories fire. Empirically the keys correspond to interpretable patterns (a
specific phrase, a topic, a syntactic frame) and the values shift the output distribution
toward the tokens associated with them.

This division of labour is the clean story of the architecture:

| | Attention | FFN |
| --- | --- | --- |
| Moves information | between positions | within a position |
| Depends on | other tokens | this token only |
| Roughly stores | routing / relations | facts / features |
| Parameters | ~1/3 | ~2/3 |
| FLOPs at long context | grows as `n²` | grows as `n` |

Editing work like [ROME](https://arxiv.org/abs/2202.05262) exploits it directly: to change a
model's belief about a fact, you edit a specific mid-layer FFN, not attention.

## Gated variants

Modern models use **SwiGLU** ([Shazeer, 2020](https://arxiv.org/abs/2002.05202)):

$$\text{FFN}_{\text{SwiGLU}}(x) = W_2\big(\text{Swish}(W_1 x) \odot (W_3 x)\big)$$

Three matrices instead of two, so `d_ff` is usually cut to `8/3 · d_model` to keep the
parameter count matched. The gate lets the network multiplicatively suppress or pass features
rather than only thresholding them, and it consistently wins by a small margin at equal
parameters. Llama, PaLM, Mistral and Qwen all use it.

## Why the 4× expansion

Empirical. Too narrow and the layer is a bottleneck with too few "memory slots"; much wider and
you would rather spend the parameters on depth. The ratio has been remarkably stable since
2017, and **Mixture-of-Experts** is essentially the observation that you can make `d_ff`
enormous if you only activate a slice of it per token.

## What an interviewer digs into next

* Why is the FFN position-wise? What would change if it mixed positions?
* Why do gated FFNs shrink `d_ff` to `8/3 d`?
* If most parameters are in the FFN, why does MoE replace the FFN and not attention?
* At 128k context, which dominates FLOPs — attention or FFN? (Work it out.)
