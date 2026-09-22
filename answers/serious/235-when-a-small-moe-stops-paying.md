---
id: "235"
slug: when-a-small-moe-stops-paying
style: serious
category: open-weights
difficulty: advanced
question: "A 26B model that activates 4B per token should be cheap to run. On one consumer card it often is not. What went wrong?"
tags: [mixture-of-experts, gemma, consumer-gpu, quantisation, serving]
---

# Nothing went wrong. Sparsity buys FLOPs, and a 16 GB card does not ration FLOPs

Gemma 4's `26B-A4B` holds 128 experts per layer and fires 8 of them per token. The FLOP saving is
real and large. The memory bill is also real, also large, and arrives whether or not you collect
the saving — and on a single consumer card memory is the constraint that binds first. The label
tells you what it computes. It does not tell you what it occupies, and the second number is the
one that decides whether you get the first.

## What is actually in the checkpoint

Read from `Gemma4_26B_A4B` in `gemma/gm/nn/gemma4/_gemma4.py`
([`google-deepmind/gemma`](https://github.com/google-deepmind/gemma)): 30 layers, `embed_dim`
2816, 128 experts of hidden width 704, `top_k_experts=8`, plus a **dense shared MLP** of hidden
width 2112 that runs on every token in every layer, plus 16 attention heads over 8 KV heads.

```
   one layer of Gemma 4 26B-A4B

     router 2816 × 128            0.36 M     runs always
     shared dense MLP 3×2816×2112 17.8 M     runs always
     attention (local layer)      37.0 M     runs always
     128 experts × 3×2816×704    761.3 M     8 of them run   ← 8 × 5.95 M = 47.6 M
                                 ───────
     resident per layer          816.5 M     active per layer  102.8 M

   × 30 layers, + 262,144 × 2816 embedding

     TOTAL RESIDENT   25.2 B          ACTIVE PER TOKEN   3.82 B
     experts alone    22.8 B  = 90.5% of the model, 6.3% of it used per token

   ┌─ the same checkpoint, on the two axes that matter ────────────────────┐
   │                            reads per token      must be resident     │
   │  Gemma 4 26B-A4B  @ int4        ~1.9 GB             ~12.6 GB         │
   │  a dense 12B      @ int4        ~6.0 GB              ~6.0 GB         │
   │                                                                      │
   │  on a 16 GB card:   MoE leaves ~3.4 GB for KV, activations and the   │
   │                     vision tower.  The dense 12B leaves ~10 GB.      │
   │                     KV alone at 131,072 tokens is 1.55 GB.           │
   └──────────────────────────────────────────────────────────────────────┘
```

Ninety percent of the parameters are experts, and a given token touches one expert in sixteen.
That is the design working exactly as intended — and it is also why the residency number is six
times the active number rather than twenty percent above it.

## The four things that eat the saving on one card

**1. Decode is bandwidth-bound, and the MoE genuinely does read less — right up until it doesn't
fit.** At batch one you are not FLOP-limited, you are limited by how many bytes you can drag out
of memory per token. Reading 3.82B of parameters instead of 12B is a real win. But the instant the
checkpoint exceeds VRAM, the experts are the thing that gets pushed out — they are 90% of the
bytes — and now every token pulls its eight chosen experts across PCIe instead of out of HBM. The
axis you were winning on becomes the axis you lose on, discontinuously.

**2. The gather is not free, and its cost is implementation-defined.** A public bug report against
`ik_llama.cpp` (issue #1765) benchmarks this exact checkpoint at Q4\_K with experts on CPU, on a
Ryzen 9 7945HX with an RTX 5070 Ti: prompt processing 2,181 tok/s against upstream `llama.cpp`'s
577, and token generation **6.86 tok/s against 30.10**. Same model, same quantisation, same
machine — a 4.4× swing in generation from the expert-offload path alone, and the issue was closed
`wontfix`. When a 4× performance difference is a property of which build you compiled, you are not
measuring the architecture.

**3. Eight small GEMMs are worse than one big one.** Per token per layer the MoE path runs eight
matmuls of shape (1 × 2816) × (2816 × 704) at scattered addresses, thirty times over: 240 gathers
and 240 tiny GEMMs per token. A dense MLP of comparable active width runs one contiguous matmul.
The FLOP counts are similar; the achieved utilisation is not, because arithmetic intensity at
M = 1 is already terrible and fragmenting it makes it worse.

**4. Batch is what redeems all of this, and a single user has none.** At batch 256 the tokens
scatter across enough of the 128 experts that every expert has work, the gathers amortise, and the
sparse model delivers what it promised. One person typing at one GPU is the pathological case.

## The comparison that flatters and the comparison that binds

Coverage of this checkpoint on consumer cards mostly pits it against Gemma 4's **dense 31B** and
reports it several times faster. That is true and it is the wrong comparison: the 31B does not fit
on the card either. The comparison that decides your deployment is against the largest dense
checkpoint that fits *with room left over*, because the room left over is your context window,
your vision tower and your batch size. Against that model, a small MoE is asking you to spend
roughly 2× the memory to run roughly a third of the compute, and to accept a 4× kernel lottery
while you are at it. The bet is that the 25.2B of stored capacity shows up as quality. Sometimes
it does. Measure it on your traffic, not on a leaderboard.

## Where a small MoE is right

Shared serving with real concurrency; a card or a box where the weights fit comfortably and the
spare memory is not needed for anything else; workloads with wide topic variety, where total
parameters are the thing that pays. None of those describe a laptop. This is the same shape as the
dense-versus-sparse argument in question 218, run at a tenth of the scale — and at a tenth of the
scale the memory term dominates far more completely, because the denominator is one consumer card
rather than a rack.

## What an interviewer is listening for

That you say "active parameters are a compute claim and total parameters are a memory claim" and
then ask which one the target machine rations. Then that you can name the discontinuity: sparsity
degrades gracefully in FLOPs and catastrophically in residency, so the interesting question is not
how fast it is but how close to the edge of memory it sits. The strongest answers ask what batch
size the deployment actually sees before offering an opinion at all.

## Where this stands, September 2026

The architecture numbers — 30 layers, 128 experts, expert hidden 704, top-8, the shared dense MLP
at 2112, `embed_dim` 2816 — were read first-hand from `google-deepmind/gemma` and are **primary**.
The 25.2B total and 3.82B active are my own arithmetic over that config; they land on the
published "26B total, 3.8B activated" figures, which is the check that the arithmetic is right.
The `ik_llama.cpp` throughput numbers were read first-hand from the public issue thread and are a
**primary reading of one user's benchmark** — one machine, one build, not a controlled study. The
consumer-card comparisons against the dense checkpoints are **coverage**; `huggingface.co` and
`ai.google.dev` are blocked from this environment. Quantisation formats and kernel quality move
monthly and item 2 above will date fastest. The residency-versus-compute distinction will not.
