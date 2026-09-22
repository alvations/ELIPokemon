---
id: "268"
slug: roofline-decode-and-prefill
style: serious
category: optimization
difficulty: advanced
question: "Decode is memory-bandwidth-bound and prefill is compute-bound. Do the roofline arithmetic, and say what follows for kernel work."
tags: [roofline, bandwidth, prefill, decode, kernels]
---

# Two phases, the same weights, and a factor of seven thousand between them.

Prefill and decode run the identical layers over the identical parameters. They differ in one
ratio — **FLOPs performed per byte moved** — and that ratio decides which half of the GPU you are
allowed to use. Prefill sits far above the machine's ridge point and is limited by tensor cores.
Decode sits far below it and is limited by HBM. Every optimisation in this arc is either a bytes
optimisation or a FLOPs optimisation, and applying one to the wrong phase buys nothing.

```
                                     ridge point = peak FLOP/s ÷ peak bytes/s
   attainable
   FLOP/s  ▲
           │                    ┌──────────────────────── compute roof  989 TF/s
   989 TF  ┤          ┌─────────┘                         (H100 SXM, BF16, dense)
           │         ╱│
           │       ╱  │
           │     ╱    │  ridge = 989e12 ÷ 3.35e12 = 295 FLOP/byte
           │   ╱      │
           │ ╱  slope = 3.35 TB/s                    ● prefill 8192   8,650
           ╱          │                              │
           └──────────┼───────────────────────────────────────────────────────▶
        ● decode B=1  │                                      arithmetic intensity
            1.13      295                                    (FLOP per byte)
```

Hardware figures: H100 SXM 80 GB, 989 TFLOP/s dense BF16, 3.35 TB/s HBM3, 132 SMs. These are
NVIDIA's published specs; I could not reach `nvidia.com` from this environment, so they are taken
from [stas00/ml-engineering's accelerator
chapter](https://github.com/stas00/ml-engineering/blob/master/compute/accelerator/README.md),
which I did read directly, and which also reports a **measured** best-case BF16 matmul of
**794.5 TFLOP/s** — 80.3% of spec. Use the measured number and the ridge point drops to 237.

## The configuration

Llama-3.3-70B on 8×H100, TP=8: 80 layers, hidden 8192, 64 query heads, 8 KV heads, head_dim 128,
intermediate 28672, vocab 128256. That is 70.55B parameters, so **141.1 GB** of BF16 weights, and
`2 · 8 · 128 · 2 · 80 = 327,680` bytes = **320 KiB of KV per token** (the formula is
[228](228-attention-variants-and-kv-arithmetic.md)). Aggregate: 26.8 TB/s, 7,912 TFLOP/s.

## The arithmetic

```
   PREFILL, one 8192-token request
     bytes   weights read once                            141.1 GB
             KV written  8192 × 320 KiB                     2.7 GB
                                                        ───────────
                                                          143.8 GB
     FLOPs   dense  2 · 70.55e9 · 8192                   1155.9 TFLOP
             attn   80 · 2 · (2 · 64 · 128 · 8192²) / 2    88.0 TFLOP
                                                        ─────────────
                                                         1243.9 TFLOP
     intensity  1243.9e12 / 143.8e9  =  8,650 FLOP/byte     29× ABOVE ridge
     time       1243.9 / 6356 (measured roof)  =  196 ms    COMPUTE-BOUND

   DECODE, batch 1, 8192 of context
     bytes   weights read once                            141.1 GB
             KV read     8192 × 320 KiB                     2.7 GB
                                                        ───────────
                                                          143.7 GB
     FLOPs   dense  2 · 70.55e9 · 1                        0.141 TFLOP
             attn   80 · 2 · 2 · 64 · 128 · 8192           0.021 TFLOP
                                                        ─────────────
                                                          0.163 TFLOP
     intensity  0.163e12 / 143.7e9  =  1.13 FLOP/byte      261× BELOW ridge
     time       143.7 / 26800  =  5.36 ms → 186 tok/s      BANDWIDTH-BOUND
```

**Those two rows move the same bytes — 143.8 GB against 143.7 GB — and differ in work by 7,650×.**
That single comparison is the whole argument. Prefill runs the tensor cores at 80% of what silicon
can do; decode at batch 1 runs them at 0.38% and spends 5.36 ms doing nothing but reading weights
it will read again in 5.36 ms' time.

## Batching moves you right along the axis, but not as far as you think

The obvious fix is more sequences per step: the weights are read once for the whole batch, so
intensity should climb with `B`. It does — and then it stops.

```
   decode, batch 128, 8192 context
     bytes   141.1 GB weights  +  128 × 2.68 GB KV = 343.6 GB   =  484.7 GB
     FLOPs   128 × 0.163 TFLOP                                  =   20.8 TFLOP
     intensity  42.9 FLOP/byte        still 6.9× BELOW the ridge
     time       18.09 ms → 7,076 tok/s

   128× the batch bought 38× the throughput and cost 3.4× the per-token latency.
```

Take the limit. Each extra sequence adds 0.163 TFLOP of work and 2.68 GB of KV reads, so the
intensity **asymptotes** at `0.163e12 / 2.68e9 = 60.6 FLOP/byte` — and 60.6 < 295.

> At 8K context, this model's decode phase cannot become compute-bound at **any** batch size.
> The weights amortise; the KV cache does not.

Shorten the context and the picture changes, because the fixed 141.1 GB of weights is then spread
over much less KV traffic. At 512 tokens of context the per-token ratio is 849 FLOP/byte and
batch 448 does reach the ridge. So the honest statement is not "decode is memory-bound" but
**"decode is memory-bound at any context length you actually serve"**.

## What follows for kernels

1. **Decode kernels are bytes engineering.** Fewer KV bytes
   ([228](228-attention-variants-and-kv-arithmetic.md)), fewer weight bytes (FP8, FP4), fewer
   round trips through HBM. A decode kernel that halves its
   FLOPs and moves the same bytes is exactly as fast as before.
2. **Prefill kernels are tile engineering.** Tensor-core utilisation, tile shapes, warp
   specialisation, avoiding the quadratic term. Compressing the KV cache does nothing for prefill,
   because prefill's cost is set by the query head count, which no KV variant changes.
3. **The two want opposite batches**, which is why a scheduler that mixes them exists at all
   ([270](270-serving-stack-around-the-kernel.md)).
4. **Fusion is a bytes optimisation**, which is why it pays off so enormously on elementwise
   training code ([271](271-training-kernels-and-fusion.md)) and so little on a GEMM.
5. **A speedup with no stated phase is unreadable.** "2× faster attention" measured on prefill and
   quoted at a decode-heavy shop is not a lie and not a result
   ([272](272-reading-a-kernel-benchmark.md)).

## Where this stands, September 2026

The ridge point is the part that outlives every library here. It has drifted **upward** for a
decade — A100 312/2.0 = 156, H100 989/3.35 = 295, B200 2250/8.0 ≈ 281 for BF16, and far higher for
the low-precision modes, because arithmetic has scaled faster than HBM. Every generation makes the
memory-bound region wider, so the fraction of LLM serving that is bandwidth-bound goes up, not
down. The specific numbers above are a 70B dense model on Hopper in September 2026 and will be
stale within a year; the method — count the bytes, count the FLOPs, divide, compare to
peak÷bandwidth — will not be.

## What an interviewer digs into next

* Why does batching not rescue decode at long context? (The KV term.)
* Which of GQA, FP8 weights and FlashAttention help prefill, and which only help decode?
* Your decode kernel got 2× fewer FLOPs and no faster. What happened?
