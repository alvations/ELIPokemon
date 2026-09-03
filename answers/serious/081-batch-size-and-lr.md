---
id: "081"
slug: batch-size-and-lr
style: serious
category: optimization
difficulty: intermediate
question: "How are batch size and learning rate related, and what is gradient accumulation?"
tags: [batch-size, learning-rate-scaling, gradient-accumulation, critical-batch-size]
---

# Batch size and learning rate

Gradient noise scales as `1/√B`. A larger batch gives a more accurate gradient estimate, so you can
safely take a larger step. That is the whole relationship, and the two standard scaling rules follow
from it.

**Linear scaling** ([Goyal et al., 2017](https://arxiv.org/abs/1706.02677)): if you multiply batch
size by `k`, multiply the learning rate by `k`. The reasoning: `k` steps of size `η` on `k` small
batches ≈ one step of size `kη` on the combined batch, provided the gradient does not change much
across those steps. Validated up to batch 8192 on ImageNet, with warmup — without which the rule
fails immediately at initialisation.

**Square-root scaling**: `η ∝ √k`. Follows from keeping the *noise scale* constant rather than the
expected update, and is generally the better fit for adaptive optimizers like Adam and at very large
batch sizes.

```
   ideal LR │              ___----‾‾‾‾  linear scaling holds
            │         __--
            │      _--                  ▲
            │   _--                     │ beyond the critical batch size,
            │ _-                        │ neither rule holds and returns
            │-                          │ diminish sharply
            └──────────────┬──────────────────────► batch size
                    critical batch size
```

## The critical batch size

Beyond a certain batch size, doubling the batch **stops halving the number of steps needed**
([McCandlish et al., 2018](https://arxiv.org/abs/1812.06162)). Below it you are noise-limited and
bigger batches buy real speedup; above it the gradient is already accurate and you are wasting
compute. The critical batch size grows as training progresses and as the task gets harder, which is
why very large runs ramp batch size over training.

The practical implication: **there is a point past which more parallel hardware does not train faster,
only cheaper per sample.**

## Gradient accumulation

Simulates a large batch on limited memory by summing gradients over several micro-batches before
stepping:

```python
optimizer.zero_grad()
for i, micro in enumerate(batch.chunks(k)):
    loss = model(micro).loss / k        # ← divide, or the effective LR is k× too high
    loss.backward()                     # gradients accumulate
optimizer.step()
```

Mathematically equivalent to a single large batch, at `k`× the wall-clock time and constant memory.
Gotchas worth naming:

* **Forgetting the `/k`** is the classic bug — you get the mean-gradient scale wrong and effectively
  train at `k`× the intended learning rate.
* **BatchNorm is not equivalent**, because its statistics are computed per micro-batch. LayerNorm is
  unaffected — another reason transformers are easier here.
* **Distributed training**: disable gradient synchronisation on all but the final micro-step
  (`no_sync`), or you pay `k`× the communication for nothing.

## Practical guidance

* **Effective batch = micro-batch × accumulation steps × data-parallel world size.** Tune the
  *effective* batch; the split between the three is a memory and throughput decision.
* Small batches regularise (noise helps generalisation), so the largest batch that fits is not
  automatically the best choice for final quality.
* When you change batch size, **change the learning rate**. Reporting that "big batches hurt accuracy"
  without re-tuning the learning rate is a very common invalid comparison.

## What an interviewer digs into next

* Derive the linear scaling rule and say where it breaks.
* Why does Adam prefer square-root scaling?
* What is the critical batch size and why does it grow during training?
* Why does gradient accumulation not reproduce BatchNorm exactly?
