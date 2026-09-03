---
id: "001"
slug: attention-mechanisms
style: serious
category: transformers
difficulty: core
question: "Can you explain the concept of attention mechanisms in transformer models?"
tags: [attention, self-attention, transformers, qkv, softmax]
---

# Attention mechanisms in transformer models

Attention lets every token in a sequence look directly at every other token and decide, per
token, how much each one matters right now. Introduced for translation by
[Bahdanau et al. (2014)](https://arxiv.org/abs/1409.0473) and made the whole architecture by
["Attention Is All You Need"](https://arxiv.org/abs/1706.03762), it replaced the recurrent
bottleneck of RNNs and LSTMs — which had to squeeze all history into one hidden state and
process tokens strictly in order — with a single parallel operation whose path length between
any two positions is **one hop**, not *n*.

## The core idea: self-attention

Consider *"The animal didn't cross the street because **it** was too tired."* When the model
processes `it`, self-attention scores `it` against every other token and puts most of its
weight on `animal`. Change the last word to *"too wide"* and the weight shifts to `street` —
without changing a single parameter. That contextual re-routing is the whole trick: a token's
representation is rewritten as a weighted blend of the tokens it decided were relevant.

## Queries, keys and values

Each token embedding `x` is projected by three learned matrices into three vectors. The
standard analogy is a soft dictionary lookup:

| Vector | Learned as | Reads as |
| --- | --- | --- |
| 🔍 **Query** `q = xW_Q` | what this token is looking for | *"I'm a pronoun — where's my referent?"* |
| 🏷️ **Key** `k = xW_K` | what this token advertises | *"I'm a singular animate noun."* |
| 📦 **Value** `v = xW_V` | what this token contributes if selected | the content actually mixed in |

The lookup is *soft*: instead of retrieving one entry, you retrieve a convex combination of
all of them.

## The computation

$$\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$

```
   tokens →   The   animal   didn't   cross  ...   it
              ┌──┐   ┌──┐    ┌──┐    ┌──┐        ┌──┐
    x         │  │   │  │    │  │    │  │        │  │
              └┬─┘   └┬─┘    └┬─┘    └┬─┘        └┬─┘
      ┌────────┴──────┴───────┴───────┴───────────┴────────┐
      │  W_Q            W_K                 W_V            │
      └───┬──────────────┬───────────────────┬─────────────┘
          ▼              ▼                   ▼
         q_it        k_1 … k_n           v_1 … v_n
          │              │                   │
          └───► q·kᵀ ────┘   raw scores      │      "how related?"
                 │
                 ▼  ÷ √d_k                          keeps variance ≈ 1
                 │
                 ▼  softmax                         scores → weights summing to 1
        ┌────────────────────────────────────┐
        │ The .02 │ animal .61 │ street .07 │…│      ← attention distribution for "it"
        └────────────────────────────────────┘
                 │
                 └───► Σ (weight × v) ──────► output for "it"
                        a blend dominated by "animal"
```

1. **Score** — `QKᵀ` gives an `n × n` matrix: how well every query matches every key.
2. **Scale** — divide by `√d_k`. Without it, dot products of `d_k`-dimensional vectors grow
   with `d_k`, softmax saturates, and gradients vanish.
3. **Mask** — in a decoder, set future positions to `-∞` before the softmax so position *i*
   can only see `≤ i`. This is what makes autoregressive generation valid.
4. **Normalise** — softmax over each row turns scores into weights that sum to 1.
5. **Mix** — multiply by `V`. Relevant tokens keep their signal; irrelevant ones are muted.

## Multi-head attention

One attention distribution can only express one notion of relevance. Transformers therefore
run `h` heads in parallel (8–128 in practice), each with its own `W_Q, W_K, W_V` projecting
into a `d_model/h`-dimensional subspace, then concatenate and project the results with `W_O`.
Probing work such as [Clark et al. (2019)](https://arxiv.org/abs/1906.04341) finds heads that
specialise: some track syntactic dependencies, some resolve coreference, some just attend to
the previous token or a delimiter. Total compute is roughly unchanged — the heads split the
width rather than adding to it.

## Why it won

* **Parallelism.** All positions are computed at once, so training saturates GPUs; an RNN
  cannot start step *t* before step *t-1*.
* **Path length.** Any two tokens interact in one layer, so long-range dependencies do not
  have to survive hundreds of recurrent steps.
* **Interpretable-ish structure.** Attention maps are inspectable — though attention weights
  are *not* faithful explanations ([Jain & Wallace, 2019](https://arxiv.org/abs/1902.10186)).

The bill is quadratic: time and memory scale as `O(n²·d)` in sequence length. Everything in
the efficiency literature — FlashAttention, sliding-window and sparse attention, linear
attention, GQA, KV-cache compression — is an attempt to pay less of that bill.

## What an interviewer digs into next

* Why divide by `√d_k` specifically, and what breaks if you don't?
* Where does the causal mask go, and why before the softmax rather than after?
* What is the memory cost of attention at inference, and why is it the KV cache rather than
  the `n × n` matrix that hurts?
* Self-attention vs cross-attention — which one does an encoder-decoder use where?
