---
id: "078"
slug: gradient-checkpointing
style: serious
category: systems
difficulty: intermediate
question: "What is gradient checkpointing and what does it trade away?"
tags: [gradient-checkpointing, activation-recomputation, memory, training]
---

# Gradient checkpointing

Backprop needs the forward activations to compute gradients (question 073), so the default is to
cache all of them. For a transformer, activation memory scales as
`O(batch × seq_len × d_model × layers)` and typically **dominates training memory** — often exceeding
the weights and optimizer state combined at long sequence lengths.

Gradient checkpointing (activation recomputation) stores only a subset — the **checkpoints** — and
recomputes the rest during the backward pass.

```
   WITHOUT CHECKPOINTING
   L1 ──► L2 ──► L3 ──► L4 ──► L5 ──► L6 ──► L7 ──► L8 ──► loss
   ▓      ▓      ▓      ▓      ▓      ▓      ▓      ▓        ▓ = stored
   store all 8 activations.  Memory O(L).  Backward is immediate.

   WITH CHECKPOINTING (every √L ≈ 3 layers)
   L1 ──► L2 ──► L3 ──► L4 ──► L5 ──► L6 ──► L7 ──► L8 ──► loss
   ▓      ·      ·      ▓      ·      ·      ▓      ·
   store 3.  Backward at L5: re-run L4→L5 from the L4 checkpoint,
   then compute the gradient. Memory O(√L). One extra forward pass.
```

## The tradeoff, quantified

| | Memory | Compute |
| --- | --- | --- |
| Store everything | `O(L)` | 1 forward + 1 backward |
| Checkpoint every `√L` | `O(√L)` | ~1.33× the total step |
| Checkpoint every layer | `O(1)` per layer | ~1.5× |

The canonical result ([Chen et al., 2016](https://arxiv.org/abs/1604.06174)) is that checkpointing
every `√L` layers gives `O(√L)` memory for one extra forward pass — a very favourable trade, since
the backward pass is roughly twice the forward, so an extra forward adds ~33% to the step rather than
100%.

## Why you use it

Not to save money — to make a run **possible**. Concretely it lets you:

* Train a model that otherwise does not fit at all.
* **Increase batch size**, which often recovers much of the lost throughput because larger batches
  use the GPU better. This is the point people miss: the naïve view is "30% slower", but the achievable
  batch size usually grows more than 30%, so end-to-end throughput can *improve*.
* Train at longer sequence lengths, where activation memory grows fastest.

## Practical notes

* **Selective checkpointing** is better than all-or-nothing: recompute cheap ops (activations,
  normalisation, dropout) and keep expensive ones (attention output, matmul results). Modern
  frameworks support policies that decide per-op, capturing most of the memory saving for much less
  recompute.
* **Interaction with FlashAttention** — FlashAttention already recomputes the attention matrix in its
  backward pass (question 010), so the attention part is checkpointed by construction.
* **Determinism.** Recomputation must reproduce the forward pass exactly, so RNG state for dropout
  must be saved and restored. Frameworks handle this; custom checkpointed functions with randomness
  are a classic source of subtle bugs.
* **It composes with everything else** — ZeRO/FSDP shards parameters and optimizer state, while
  checkpointing attacks activations. They address different terms, so they are complementary, and
  large runs use both.
* **Inference does not need it**, since there is no backward pass and no activations to keep.

## What an interviewer digs into next

* Why is the compute overhead ~33% rather than 100%?
* Why can checkpointing sometimes *increase* throughput?
* Why does dropout need special handling under checkpointing?
* Which memory term does checkpointing address, and which does FSDP address?
