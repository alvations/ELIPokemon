---
id: "076"
slug: learning-rate-schedules
style: serious
category: optimization
difficulty: intermediate
question: "Why do we use learning-rate warmup and decay schedules?"
tags: [learning-rate, warmup, cosine-decay, wsd, schedules]
---

# Learning rate schedules

The learning rate is the single most important hyperparameter, and the best value **changes during
training**. A schedule encodes that.

```
   lr │      ╱‾‾‾╲
      │     ╱      ╲___
      │    ╱            ╲___
      │   ╱                  ╲____
      │  ╱                        ╲______
      │ ╱                                ╲_____
      └─────────────────────────────────────────────► steps
       │←warmup→│←──────── decay ─────────────────→│
        (1–5%)
```

## Warmup

Linearly ramp from ~0 to the peak over the first few thousand steps. Three reasons, and the second is
the one people miss:

1. **Adam's second-moment estimate is unreliable early.** With `β₂ = 0.999`, `v` needs thousands of
   steps to become a meaningful variance estimate. Before then the adaptive denominator is noisy, so
   the effective step size is erratic and can be enormous. Warmup keeps steps small until the
   estimate stabilises. ([RAdam](https://arxiv.org/abs/1908.03265) makes this argument explicitly and
   proposes rectification as an alternative.)
2. **Large-batch training needs high peak learning rates**, and a high rate applied to a random
   initialisation destroys it immediately.
3. **Pre-norm transformers** tolerate less warmup than post-norm ones, but at scale everyone still
   uses some.

Skipping warmup on a transformer is one of the most reliable ways to produce a divergent run.

## Decay

Early in training, large steps make fast progress across a poorly-conditioned landscape. Later,
large steps bounce around the minimum instead of settling. Decay anneals from exploration to
refinement.

| Schedule | Shape | Notes |
| --- | --- | --- |
| **Cosine** | smooth half-cosine to ~0 or to a floor | the standard for LLM pretraining |
| **Linear** | straight line to 0 | common for fine-tuning; nearly as good |
| **Step** | drop ×0.1 at milestones | classic vision recipe |
| **Inverse sqrt** | `1/√step` | the original transformer schedule |
| **WSD** | warmup → **constant** → short sharp decay | see below |

## Why WSD matters

Cosine has a practical flaw: the schedule depends on the **total** step count, chosen in advance. You
cannot stop early and get a usable model (the rate never decayed), and you cannot extend training
without redoing the schedule.

**Warmup-Stable-Decay** holds the rate constant for most of training, then decays sharply over the
last ~10%. This gives usable checkpoints at any point — branch off, run the short decay, and you have
a finished model. It matches or beats cosine and is far more practical for continued pretraining, so
it has become common in recent large runs.

## Practical guidance

* **Peak LR scales with batch size.** Linear scaling (`lr ∝ B`) works up to a point; square-root
  scaling is often better for very large batches.
* **Fine-tuning wants ~10–100× lower LR than pretraining.** `1e-5` to `5e-5` is typical for full
  fine-tuning; LoRA wants `1e-4`–`3e-4`, because a small number of parameters must move further.
* **LR range test.** Sweep the LR upward over a few hundred steps and plot loss; the largest rate
  before divergence, divided by ~3, is a good peak. Ten minutes of work that beats guessing.
* **Warmup length:** 1–5% of total steps, or a fixed 500–2000 steps.
* **Restarts / cyclical rates** (SGDR) — periodic resets to escape sharp minima. Less common now.

## What an interviewer digs into next

* Why does Adam specifically need warmup?
* What is the practical problem with cosine decay?
* How would you set the peak learning rate for a new model?
* Why does LoRA want a much higher learning rate than full fine-tuning?
