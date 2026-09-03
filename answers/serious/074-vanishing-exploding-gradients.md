---
id: "074"
slug: vanishing-exploding-gradients
style: serious
category: deep-learning
difficulty: core
question: "What are vanishing and exploding gradients, and how are they fixed?"
tags: [vanishing-gradients, exploding-gradients, clipping, initialisation, lstm]
---

# Vanishing and exploding gradients

Backprop multiplies Jacobians through the network. Through `L` layers the gradient is a product of
`L` terms, and products of many numbers behave badly:

$$\frac{\partial L}{\partial \theta_1} = \frac{\partial L}{\partial h_L}
\prod_{l=2}^{L}\frac{\partial h_l}{\partial h_{l-1}} \cdot \frac{\partial h_1}{\partial \theta_1}$$

```
   if each factor ≈ 0.8, over 50 layers:  0.8⁵⁰ ≈ 1.4e-5   → VANISHES
   if each factor ≈ 1.2, over 50 layers:  1.2⁵⁰ ≈ 9,100    → EXPLODES
   only ≈ 1.0 survives, and that is a knife edge
```

**Vanishing:** early layers receive essentially no signal and stop learning. The network trains only
its last few layers. Insidious, because loss still decreases — just far less than it should.

**Exploding:** gradients become huge, a single step throws the weights far away, and the loss becomes
NaN. Obvious, and therefore much easier to fix.

## The historical cause: saturating activations

Sigmoid's derivative peaks at 0.25 and approaches 0 in both tails. Stack ten sigmoid layers and the
best case is `0.25¹⁰ ≈ 1e-6`. Tanh is better (peak 1.0) but still saturates. This is why deep
networks were considered untrainable before roughly 2010, and why the fixes below were transformative
rather than incremental.

## The fixes

**1. Non-saturating activations.** ReLU has derivative exactly 1 for positive inputs, so it does not
shrink the gradient at all. This was the single largest contributor to making deep networks trainable.
(Its own failure mode is dying units — a unit stuck at negative input has zero gradient forever —
addressed by LeakyReLU and GELU.)

**2. Residual connections.** `∂y/∂x = I + ∂F/∂x`. The identity term guarantees a path with gain 1 to
every layer regardless of what the blocks do (question 006). This is the structural fix and the
reason 100+ layer networks train.

**3. Normalisation.** BatchNorm/LayerNorm keep activations in a well-conditioned range, so Jacobians
stay near unit scale rather than drifting.

**4. Careful initialisation.** **Xavier/Glorot** (`Var(W) = 1/n_in` — for tanh) and **He/Kaiming**
(`Var(W) = 2/n_in` — for ReLU, the 2 compensating for half the outputs being zeroed) set the initial
scale so signal variance is preserved layer to layer. Wrong initialisation causes vanishing or
exploding *at step 0*, before training does anything.

**5. Gradient clipping** — the standard fix for exploding gradients, by global norm:

```python
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
```

Scale the whole gradient down if its norm exceeds a threshold. Preserving the *direction* while
capping the *magnitude* is why norm-clipping is preferred to value-clipping. Essentially every LLM
training run uses it.

**6. Gated architectures** — LSTM/GRU solve this for recurrence: the cell state has an additive path
(the "constant error carousel") that avoids repeated multiplication. Transformers sidestep the
problem differently, by removing depth-in-time entirely.

## Diagnosing

Log gradient norms **per layer**. Vanishing appears as norms decaying by orders of magnitude toward
the input; exploding as spikes preceding a NaN. This one piece of instrumentation identifies the
problem immediately and is routinely missing from training scripts.

## What an interviewer digs into next

* Why does He initialisation use `2/n_in` and Xavier `1/n_in`?
* Why does the residual connection guarantee gradient flow?
* Why clip by norm rather than by value?
* Why do transformers not suffer the RNN version of this problem?
