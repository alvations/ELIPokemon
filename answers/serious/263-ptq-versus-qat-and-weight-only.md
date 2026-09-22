---
id: "263"
slug: ptq-versus-qat-and-weight-only
style: serious
category: optimization
difficulty: intermediate
question: "When does quantisation-aware training earn its cost over post-training quantisation, and what does weight-only quantisation buy that W8A8 does not?"
tags: [quantisation, ptq, qat, weight-only, inference]
---

# PTQ is a file conversion. QAT is a training run. They are not on the same shelf.

**Post-training quantisation** takes a finished checkpoint, fits scales and zero-points from a few
hundred forward passes over a calibration set, and writes a new file. Minutes to a few hours on
one GPU; no gradients, no training corpus. **Quantisation-aware training** inserts a fake-quant
node in the forward pass — round to the grid, then let the gradient pass straight through as
though you had not, the straight-through estimator — and keeps training, so the weights settle
where the grid can represent them. That is GPU-days at minimum, a data pipeline, and a loss curve
somebody has to trust. The 2026 summary: at 8 or 4 bits on a model above a few billion parameters,
a good PTQ algorithm lands close enough that QAT is not worth the run. QAT earns its cost in three
places — **below 4 bits**, on **small models** where the redundancy has run out, and when you are
shipping to **fixed silicon** whose numerics you cannot negotiate with.

```
   POST-TRAINING QUANTISATION                QUANTISATION-AWARE TRAINING
   ──────────────────────────                ───────────────────────────
   trained BF16 checkpoint                   trained BF16 checkpoint
            │                                         │
            ▼                                         ▼
   128–1024 calibration samples              fake-quant in the forward pass
   forward only, no gradients                + straight-through estimator
            │                                         │
            ▼                                         ▼
   fit scales · solve rounding               CONTINUE TRAINING on real data
            │                                (hours → weeks, full cluster)
            ▼                                         │
   new file, same weights, fewer bits                 ▼
                                             new weights, chosen KNOWING
   cost: one GPU, one afternoon              they will be rounded
   needs: a few hundred documents
   risk:  calibration mismatch (267)         cost: a training budget
                                             needs: the training corpus
                                             risk:  you now maintain two models
```

## What each one costs and what it buys

| | PTQ | QAT |
| --- | --- | --- |
| Produce | minutes–hours, one GPU | GPU-days–weeks, a cluster |
| Needs | 128–1024 calibration samples | the training data, or a good proxy |
| Typical use | INT8, INT4, FP8 weights | ≤3-bit, ternary, small models, NPUs |
| Serving | identical — the file is the file | identical |
| Recoverable | re-run with a different calibration set | re-run the training |

Note the last row of the serving column: **the two produce the same kind of artefact**. Nothing
downstream can tell how the numbers got there. QAT does not buy a faster model; it buys a *more
accurate* model at the same bit-width. If PTQ already clears your accuracy bar, QAT buys nothing
at all, and the bar is the thing to establish first ([267](267-evaluating-a-quantised-model.md)).

There is a cheap middle ground that is often the right answer and is worth naming in an interview:
**quantise the base model with PTQ, then fine-tune a LoRA adapter on top of the frozen quantised
weights** — QLoRA ([028](028-qlora.md)). You get some of QAT's adaptation for a small fraction of
the compute, and the adapter can be merged or served separately.

## The second axis: what you quantise, not how

Weight-only against weight-and-activation is a completely separate decision, and it is the one
that actually changes the shape of your serving cost.

**Weight-only** (GPTQ, AWQ, NF4, GGUF k-quants) stores weights at 4–8 bits and dequantises to BF16
inside the kernel. The matmul is still a BF16 matmul: **zero FLOP saving**. What you save is bytes
moved, and during single-stream decode that is the entire cost, because you stream every weight
from HBM once per token and the arithmetic units idle.

**Weight-and-activation** (W8A8, FP8, and now FP4) quantises the activations too, so the tensor
cores run the multiply at low precision — a genuine 2× on FP8 against BF16, 4× on FP4. It costs
you the hard part: activations contain outlier channels and have to be handled at runtime
([264](264-outlier-channels-and-quantisation-algorithms.md)). Scales are either **static** (fitted
during calibration — free at runtime, fragile to distribution shift) or **dynamic** (computed
per-token at serving time — robust, a few percent of overhead).

## The arithmetic that decides it

Take Llama-3-8B. Its weights are 16.06 GB at BF16; llama.cpp's own scoreboard puts the Q4_K_M
build at 4.58 GiB. On an H100 SXM at roughly 3.35 TB/s of HBM bandwidth and about 990 dense BF16
TFLOP/s:

```
   DECODE, batch 1 — one token, one full pass over the weights
   ───────────────────────────────────────────────────────────
   BF16   16.06 GB / 3.35 TB/s = 4.79 ms   ← weight streaming
          2 × 8e9 FLOP / 990e12  = 0.016 ms ← arithmetic
                                              300× smaller. Idle silicon.
   Q4_K_M  4.92 GB / 3.35 TB/s = 1.47 ms
   ───────────────────────────────────────────────────────────
   3.3× faster, and not one multiply was made cheaper.

   DECODE, batch 256 — same weight read, 256× the arithmetic
   ───────────────────────────────────────────────────────────
   weight streaming  4.79 ms   (read ONCE, amortised over 256 sequences)
   arithmetic        4.14 ms   (2 × 8e9 × 256 / 990e12)
   ───────────────────────────────────────────────────────────
   weight-only quantisation removes 3.3 ms of the 8.9 and leaves the rest.
   FP8 W8A8 halves the 4.14 as well — and that is the half weight-only
   cannot touch, at any bit-width, ever.
```

The crossover for an 8B model on this card sits somewhere around batch 250. Below it you are
bandwidth-bound and weight-only is the whole game. Above it you are compute-bound and you need
low-precision *compute*. This is why the same year produced both "everyone runs Q4_K_M locally"
and "the datacentre standard is FP8": they are answers to different questions. Note also that the
KV cache is missing from both columns above, and at long context it dominates them both
([266](266-kv-cache-quantisation.md)).

## Failure modes worth naming

* **Dequantisation overhead at high batch.** A weight-only kernel that unpacks 4-bit weights into
  BF16 registers does real work per element. At batch 1 it hides behind the memory stall; at batch
  512 it is on the critical path and a 4-bit model can serve *fewer* tokens per second than an FP8
  one.
* **Static activation scales fitted on the wrong traffic.** A scale that is right for English
  prose and wrong for base64 blobs fails silently, and it fails on the requests you did not
  calibrate on.
* **QAT that quietly becomes a second model.** Once you have trained against the grid, your 4-bit
  build is no longer a derivative of the BF16 one. Two checkpoints, two eval runs, two rollbacks.
* **Small models.** The redundancy that makes INT4 safe at 70B is thin at 8B and mostly absent at
  1B. That is the regime where QAT stops being optional.

## What an interviewer digs into next

* Why does weight-only quantisation give no FLOP saving, and when does that stop being acceptable?
* Static or dynamic activation scales — what does each fail on?
* Would you QAT a 70B model to 4 bits? (Almost certainly not. Say why.)
* What does the straight-through estimator actually approximate, and why does it work at all?

## Where this stands, September 2026

The two figures I leaned on hardest are checkable: 4.58 GiB for Llama-3-8B at Q4_K_M is from
llama.cpp's own perplexity scoreboard in `tools/perplexity/README.md`, which I read directly, and
is **primary**. The H100 bandwidth and BF16 throughput numbers are **coverage** — the vendor
datasheets are unreachable from this environment, so treat 3.35 TB/s and 990 TFLOP/s as
round-to-the-nearest-order figures and re-derive the crossover on your own card. What rots is the
hardware and the batch at which the lines cross; what does not is the structure: PTQ and QAT
differ in *production* cost and not at all in serving, while weight-only and W8A8 differ in
serving and barely at all in production.
