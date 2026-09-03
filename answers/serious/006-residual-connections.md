---
id: "006"
slug: residual-connections
style: serious
category: deep-learning
difficulty: core
question: "Why do residual (skip) connections matter in deep networks?"
tags: [resnet, residual, gradient-flow, identity]
---

# Residual connections

A residual block computes `y = x + F(x)` instead of `y = F(x)`. The layer learns a *correction*
to its input rather than a replacement for it. [He et al. (2015)](https://arxiv.org/abs/1512.03385)
introduced this to fix a specific embarrassment: plain 56-layer CNNs had **higher training
error** than 20-layer ones. Not overfitting — they could not even fit. Deep plain networks
struggle to learn the identity function, so adding layers made things strictly worse.

## The gradient argument

$$\frac{\partial y}{\partial x} = I + \frac{\partial F}{\partial x}$$

Through `L` stacked blocks the Jacobian is a product of `(I + J_l)` terms. Expanding it gives a
sum of paths, one of which is pure identity. So even if every `J_l` is tiny, the gradient still
has a route to the bottom with **gain 1**.

```
  PLAIN NET                              RESIDUAL NET
  gradient must survive every layer      gradient has an express lane

   loss                                    loss
    │ ×0.7                                  │
   [L5]                                    [L5]───┐
    │ ×0.6                                  │     │ identity
   [L4]                                    [L4]───┤ (gain = 1)
    │ ×0.8                                  │     │
   [L3]                                    [L3]───┤
    │ ×0.5                                  │     │
   [L2]                                    [L2]───┤
    │ ×0.7                                  │     │
   [L1]   arrives at ×0.12                 [L1]───┘  arrives at ×1 + corrections
```

## The other framing: iterative refinement

In a transformer the residual stream is better read as a **communication bus**. Each block
reads from it, computes something, and *adds* its result back. Nothing is overwritten;
information written by layer 2 is still available at layer 40 unless some layer actively
subtracts it. This is the mental model that underpins most mechanistic interpretability work
([Elhage et al., 2021](https://transformer-circuits.pub/2021/framework/index.html)):
attention heads and MLPs are readers and writers on a shared stream.

It also explains why depth is forgiving. A block that has nothing useful to contribute can
learn `F(x) ≈ 0` and become a no-op, so extra depth costs compute but not accuracy. In a plain
network, a useless layer still mangles the signal.

## Consequences worth knowing

* **Ensembling behaviour.** [Veit et al. (2016)](https://arxiv.org/abs/1605.06431) showed
  residual nets behave like an ensemble of exponentially many shallow paths; dropping
  individual blocks at test time degrades them gracefully, which is not true of plain nets.
* **Variance growth.** Each block adds to the stream, so its variance grows roughly linearly
  with depth. Very deep models scale the residual branch (e.g. by `1/√(2L)`) at init to
  compensate.
* **Interaction with normalisation.** Where the norm sits relative to the `+` is the whole
  pre-norm/post-norm question — and pre-norm wins precisely because it keeps the residual path
  clean.
* **Requirement: matching shapes.** When dimensions change you need a projection on the skip
  (`1×1` conv, or a linear layer), which is a slight break in the identity guarantee.

## What an interviewer digs into next

* Why did the *training* error go up for deeper plain nets, and why does that rule out
  overfitting as the explanation?
* Why is the residual stream's growing variance a problem, and what fixes it?
* In a transformer, what is written to the residual stream by an attention block vs an MLP?
* Are residual connections still needed if you have good normalisation and initialisation?
