---
id: "003"
slug: multi-head-attention
style: serious
category: transformers
difficulty: core
question: "What is multi-head attention and why use more than one head?"
tags: [attention, multi-head, subspaces, induction-heads]
---

# Multi-head attention

A single attention head produces exactly one probability distribution per token. That means it
can express exactly **one** notion of "relevant" at a time. Multi-head attention runs `h`
independent attention operations in parallel over different learned subspaces, then
concatenates their outputs and mixes them with a final projection `W_O`.

$$\text{MHA}(x) = \left[\text{head}_1; \dots; \text{head}_h\right] W_O, \quad
\text{head}_i = \text{Attention}(xW_Q^i,\, xW_K^i,\, xW_V^i)$$

The crucial detail: heads **split** the model width rather than multiplying it. With
`d_model = 4096` and `h = 32`, each head works in `d_head = 128` dimensions. FLOPs are roughly
the same as one big head — you are buying *diversity*, not capacity.

```
                    x  (d_model = 4096)
                    │
   ┌────────────┬───┴────────┬─────────────┬─────────────┐
   ▼            ▼            ▼             ▼             ▼
 head 1       head 2       head 3   ...  head 32
 d=128        d=128        d=128         d=128
   │            │            │             │
 softmax      softmax      softmax       softmax        ← 32 *different* attention maps
   │            │            │             │
   ▼            ▼            ▼             ▼
 [128]  ++   [128]  ++    [128]  ++  ...  [128]   = concat → 4096
                              │
                              ▼  W_O  (4096 × 4096)
                        output (d_model)

   "The animal didn't cross the street because it was too tired"
    head 4  ─── "it" ──► animal          (coreference)
    head 11 ─── "it" ──► was             (next token / syntax)
    head 23 ─── "it" ──► [BOS]           (attention sink / no-op)
```

## Why the heads differ

Nothing explicitly forces specialisation — it emerges because the heads have different random
initialisations and the loss rewards covering different relations. Interpretability work has
catalogued recurring types:

* **Positional heads** — attend to the previous token, or `i−2`. Cheap syntax.
* **Syntactic heads** — direct object of a verb, determiner of a noun
  ([Clark et al., 2019](https://arxiv.org/abs/1906.04341)).
* **Induction heads** — the famous one: find an earlier occurrence of the current token and
  copy what followed it. [Olsson et al. (2022)](https://arxiv.org/abs/2209.11895) tie their
  formation to the phase change where in-context learning appears.
* **Attention sinks** — heads that dump probability mass on `[BOS]` when they have nothing to
  say, because softmax forces the row to sum to 1
  ([Xiao et al., 2023](https://arxiv.org/abs/2309.17453)).

## How many heads?

More heads means more relations tracked but a smaller `d_head`, and once `d_head` gets too
small each head's `QKᵀ` becomes low-rank and expressive power drops.
[Michel et al. (2019)](https://arxiv.org/abs/1905.10650) showed many trained heads can be
pruned at test time with little loss — evidence that heads are redundant, not that they were
useless during training. Typical practice keeps `d_head` at 64–128 and lets `h` scale with
`d_model`.

## The modern wrinkle: heads are not free at inference

At generation time you cache `K` and `V` for every head, every layer, every past token. Cache
size scales linearly with `h`, and decoding is memory-bandwidth bound. That pressure produced
**MQA** (all query heads share one K/V head) and **GQA** (query heads share K/V in groups),
which keep the query-side diversity that matters for quality while collapsing the K/V side
that dominates memory.

## What an interviewer digs into next

* Why concatenate and project rather than average the heads?
* What is the rank constraint on a head's attention matrix, and why does tiny `d_head` hurt?
* If many heads can be pruned post-hoc, why train with them at all?
* How does GQA change the quality/memory tradeoff, and where is the knee?
