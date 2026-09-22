---
id: "264"
slug: outlier-channels-and-quantisation-algorithms
style: serious
category: optimization
difficulty: advanced
question: "Explain outlier channels, and what GPTQ, AWQ and SmoothQuant each do about them."
tags: [quantisation, outliers, gptq, awq, smoothquant]
---

# One fat channel sets the scale, and everything else rounds to nothing.

A transformer's hidden states are not uniformly distributed across dimensions. A small number of
channels — often a couple of dozen out of four or eight thousand — carry magnitudes ten to a
hundred times everything else, and crucially they sit in **the same dimensions for every token**.
Once you size a single scale to fit them, the remaining 99.9% of the tensor is squeezed into two
or three of your available levels. Every quantisation algorithm worth knowing is a different
answer to that one fact, and if you can only say one thing in an interview, say this: **the
problem is not precision, it is dynamic range, and the range is set by a handful of persistent
channels doing real work.** They are not noise, so you cannot clip them.

```
   one linear layer's input activations, 8 channels shown of 4096

   channel:   0     1     2     3     4     5     6     7
              ▁     ▂     █     ▁     ▂     ▁     █     ▂
   |x|:      0.4   0.9  63.0   0.3   1.1   0.5  58.0   0.8
                         ▲                       ▲
                         └── the same two channels, every token

   PER-TENSOR INT8: scale = 63.0/127 = 0.496
        0.4 → 1      0.9 → 2      0.3 → 1      1.1 → 2      0.5 → 1
        ─────────────────────────────────────────────────────────
        six distinct values collapse onto {1, 2}. The layer is gone.

   PER-CHANNEL INT8: one scale per column
        each channel gets its own 127 levels → the fat ones cost nothing
        ─────────────────────────────────────────────────────────
        free for WEIGHTS (the reduction is over rows, so a per-column
        scale factors straight out of the dot product)
        NOT free for ACTIVATIONS (the reduction is ALONG the channel
        axis, so a per-channel scale cannot be hoisted out of the sum)
```

That last asymmetry is the whole reason the field looks the way it does. **Weights quantise
easily** — they are roughly Gaussian per column, have no persistent monster channels, and
per-channel or per-group scales are essentially free. **Activations quantise badly**, and the
granularity that would fix them is the one granularity the matmul will not let you hoist out. So
weight-only 4-bit is a solved problem and W8A8 is where the papers are.

## SmoothQuant: the product does not care where the factor lives

For `Y = XW`, insert any invertible diagonal `s`:

```
   Y = X W = ( X · diag(s)⁻¹ ) ( diag(s) · W ) = X̂ Ŵ        exactly, not approximately

   before                                after, s_j = 8
   ────────────────────────────────      ──────────────────────────────────
   X column j :  63.0  (impossible)      X̂ column j :   7.9  (ordinary)
   W row j    :   0.05 (trivial)         Ŵ row j    :   0.40 (still fine)

   difficulty has been MOVED, not removed — from the tensor that cannot
   take per-channel scales to the tensor that can.
```

[SmoothQuant](https://arxiv.org/abs/2211.10438) picks `s_j = max|X_j|^α / max|W_j|^(1-α)`, with α
≈ 0.5 as the usual starting point, and folds `diag(s)⁻¹` into the preceding LayerNorm's affine
parameters so it costs **nothing at runtime**. What it exploits: a mathematical invariance that
was sitting there the whole time. What it costs: α is a per-model knob, and on models with
extremely severe outliers (some of the Falcon and early Mistral checkpoints) no single α makes
both sides comfortable.

## AWQ: salience is decided by the activations, not by the weights

[AWQ](https://arxiv.org/abs/2306.00978) starts from an uncomfortable experiment. Keep 1% of weight
channels in FP16 and quantise the rest to 4 bits, and almost all the loss comes back — but *only
if you choose that 1% by activation magnitude*. Choosing by weight magnitude does nearly nothing,
and choosing at random does nothing at all. A weight is important because of what gets multiplied
by it.

Mixed-precision storage is kernel-hostile, so AWQ does not keep them in FP16. It **scales the
salient channels up before rounding** — a larger value lands on a finer part of the same grid,
relative to its own size — and divides the corresponding activation channel by the same factor.
Which is the SmoothQuant move again, pointed the other way: AWQ and SmoothQuant are the same
identity used for two different goals.

What it exploits: salience is sparse, and it is determined by data the weights cannot see. What it
costs: a small grid search over the scaling exponent. What it buys beyond accuracy: **no
backpropagation and no reconstruction**, so it is fast to produce and it leans on the calibration
set far less than GPTQ does — which is why it aged better as the datacentre default.

## GPTQ: round one column, then let the others absorb the error

[GPTQ](https://arxiv.org/abs/2210.17323) descends from Optimal Brain Surgeon. It does not try to
make each weight close to its original value; it minimises the **layer output** error ‖WX − ŴX‖²_F
on calibration data, which is a different and better objective.

```
   columns of W, quantised left to right

   [ done | done | NOW | free | free | free | free ]
                    │      ▲      ▲      ▲      ▲
                    │      └──────┴──────┴──────┘
                    │      still adjustable — push the error here
                    ▼
            round to the grid, measure the error e,
            then update every remaining column by
                  δ = − (e / [H⁻¹]_jj) · H⁻¹[j, j+1:]
            where H = 2XXᵀ + λI, from the calibration data.

   Do it in a fixed left-to-right order with a Cholesky of H⁻¹ and lazy
   block updates, and 175B parameters quantise in a few GPU-hours.
```

What it exploits: the un-quantised weights still have freedom, and second-order information says
exactly how to spend it. What it costs: it is the slowest of the three to produce, it needs the
Hessian to be well-conditioned (hence the damping λ), and it is **the most calibration-sensitive
method of the three** — it is explicitly fitting a reconstruction on your 128 samples, so a
mismatched calibration set is a real risk rather than a theoretical one
([267](267-evaluating-a-quantised-model.md)).

## Rotation: the basis was arbitrary all along

The 2024–2026 direction, and the one that made W4A4 credible: multiply the hidden state by a
random orthogonal or Hadamard matrix `R` and the inverse into the next weight matrix. `R` and
`R⁻¹` fold into neighbouring linears, so the network computes the same function — but in the
rotated basis the outlier energy is smeared across all dimensions and *no coordinate is special
any more*. QuaRot and SpinQuant are the names to know; the Hadamard version is cheap enough to do
online. It is the most satisfying answer of the four because it does not manage the outliers at
all. It removes the coordinate system that made them outliers.

## What an interviewer digs into next

* Why is a per-channel scale free on weights and not on activations?
* If AWQ and SmoothQuant use the same identity, when would you use one and not the other?
* Which of these three would you expect to overfit a calibration set, and why?
* What would you measure to tell "the rotation worked" from "the eval is insensitive"?

## Where this stands, September 2026

The mechanisms are stable and the ranking of the tools is not. As of now AWQ and FP8 are the GPU
serving defaults, GPTQ is fading in practice despite being the most accurate on paper, SmoothQuant
lives on inside other pipelines rather than as a product, and rotation is standard equipment
anywhere below 8-bit activations. Everything in this answer about *algorithms* is from the
literature rather than from a re-reading of it — arxiv.org is blocked from this environment —
while the claim that the field's outlier problem is real and structural is visible in any weight
file you care to open. What will not rot: dynamic range is the enemy, granularity is the lever,
and a mathematical invariance is always cheaper than a smarter rounding rule.

**Citation note.** The arXiv identifiers linked above are given from working knowledge.
`arxiv.org` is blocked from the environment this was written in, so **not one of them was resolved
while writing**. Resolve every identifier before you cite it.
