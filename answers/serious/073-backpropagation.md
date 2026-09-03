---
id: "073"
slug: backpropagation
style: serious
category: deep-learning
difficulty: core
question: "What is backpropagation?"
tags: [backprop, chain-rule, autodiff, computational-graph, reverse-mode]
---

# Backpropagation

Backprop is **reverse-mode automatic differentiation** applied to a neural network: an efficient
algorithm for computing the gradient of a scalar loss with respect to every parameter, in a single
backward pass costing roughly the same as one forward pass.

## The mechanism

Forward, cache what you need; backward, apply the chain rule, reusing shared subexpressions.

```
   FORWARD                                     BACKWARD
   ───────                                     ────────
   x ──[W₁]──► z₁ ──[σ]──► a₁ ──[W₂]──► z₂ ──► L
        │            │           │        │
     cache x      cache z₁    cache a₁    │
                                          ▼
   ∂L/∂W₁ ◄── ∂L/∂z₁ ◄── ∂L/∂a₁ ◄── ∂L/∂z₂ ◄── ∂L/∂L = 1
      ▲           ▲           ▲          ▲
      │           │           │          │
   uses x    ×σ'(z₁)      uses W₂    uses a₁

   Each node needs only: the incoming gradient, and its cached forward values.
```

For a chain `L = f_n(f_{n-1}(…f_1(x)))`:

$$\frac{\partial L}{\partial \theta_i}
= \frac{\partial L}{\partial f_n}\frac{\partial f_n}{\partial f_{n-1}}\cdots
\frac{\partial f_{i+1}}{\partial f_i}\frac{\partial f_i}{\partial \theta_i}$$

## Why reverse mode

Forward-mode AD computes the derivative of *everything* with respect to *one input*; reverse mode
computes the derivative of *one output* with respect to *everything*. Neural networks have millions
of parameters and one scalar loss, so reverse mode is the right choice by a factor of millions.

Concretely, forward mode would need one pass per parameter — `O(P)` passes. Reverse mode needs one,
because it propagates from the single scalar output backwards. The naïve alternative, finite
differences, needs `P+1` forward passes and is numerically unstable. This asymmetry is the entire
reason deep learning is computationally feasible.

## Costs

* **Time:** the backward pass is ~2× the forward pass (each node computes gradients with respect to
  both its inputs and its parameters). Total training step ≈ 3× a forward pass — the origin of the
  `C ≈ 6ND` rule in scaling laws (2 FLOPs per parameter forward, 4 backward).
* **Memory:** you must **cache activations** from the forward pass to use in the backward pass. This
  usually dominates training memory, scaling with batch size × sequence length × depth — and it is
  exactly what gradient checkpointing trades away (question 078).

## What goes wrong

* **Vanishing/exploding gradients** — the product of many Jacobians shrinks or grows exponentially
  with depth (question 074).
* **In-place operations** that overwrite a cached value needed for the backward pass. PyTorch raises
  an error; some frameworks silently produce wrong gradients.
* **Detached graphs** — calling `.detach()`, `.item()`, or `numpy()` breaks the chain, so gradients
  silently stop flowing. Usually shows up as a parameter that never changes.
* **Non-differentiable operations** — `argmax`, sampling, hard thresholds. Handled with surrogates:
  the straight-through estimator, Gumbel-softmax, or policy gradients (which exist precisely because
  sampling has no useful gradient).

## Framing for an interview

The concise statement: *"Backprop is the chain rule with memoisation, run in reverse so that one
backward pass gives gradients for all parameters. It is efficient because networks map many
parameters to one scalar, which is exactly the shape reverse-mode AD is optimal for."*

## What an interviewer digs into next

* Why reverse mode rather than forward mode?
* Why is the backward pass roughly twice the forward pass?
* What must be cached, and what is the memory implication?
* How do you get gradients through a sampling step?
