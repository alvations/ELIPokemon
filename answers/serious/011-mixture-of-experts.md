---
id: "011"
slug: mixture-of-experts
style: serious
category: architecture
difficulty: advanced
question: "What is a Mixture-of-Experts model and what are its tradeoffs?"
tags: [moe, sparse, routing, load-balancing, switch-transformer]
---

# Mixture-of-Experts

A dense transformer runs every parameter for every token. MoE breaks that coupling: replace the
FFN in (some) layers with `N` parallel expert FFNs plus a small **router** that sends each token
to only the top-`k` experts. Total parameters grow with `N`; FLOPs per token grow with `k`.

```
                        token x
                          │
                    ┌─────▼─────┐
                    │  router   │  softmax over N experts
                    │  W_g · x  │
                    └─────┬─────┘
          scores: [E1 .02][E2 .61][E3 .07][E4 .28][E5 .01] … [E64 .00]
                          │  top-2
              ┌───────────┴────────────┐
              ▼                        ▼
        ┌──────────┐            ┌──────────┐        E1, E3, E5 … E64
        │ Expert 2 │            │ Expert 4 │        stay ASLEEP
        │  (FFN)   │            │  (FFN)   │        (params exist, no FLOPs)
        └────┬─────┘            └────┬─────┘
             │ ×0.61/0.89            │ ×0.28/0.89
             └──────────┬────────────┘
                        ▼
                    output = weighted sum
```

The economics: a model with 64 experts and top-2 routing has ~32× the FFN parameters of the
dense equivalent but roughly 2× the FFN FLOPs. Since knowledge capacity tracks parameters and
cost tracks FLOPs, MoE buys capacity far more cheaply than depth or width.
[Switch Transformer](https://arxiv.org/abs/2101.03961) reported ~7× pretraining speedups at
matched quality; Mixtral 8×7B has 47B total parameters but ~13B active.

## Load balancing is the hard part

The router is trained jointly, and left alone it collapses — a few experts get picked, get
better, get picked more. So you add an **auxiliary load-balancing loss** penalising the
correlation between the fraction of tokens routed to an expert and the router's mean probability
for it. In practice you also need:

* **Capacity factor** — a cap on tokens per expert per batch. Overflow tokens are *dropped*
  (they skip the FFN and pass through the residual), which is a real quality cost.
* **Noisy / stochastic routing** — encourages exploration early.
* **Router z-loss** — keeps router logits small for numerical stability.
* Newer models (DeepSeek-V3) use **auxiliary-loss-free** balancing via per-expert bias terms
  adjusted online, avoiding the gradient interference the aux loss introduces.

## The tradeoffs, stated honestly

| Axis | MoE vs dense |
| --- | --- |
| Quality per FLOP | ✅ much better |
| Quality per parameter | ❌ worse — parameters are used sparsely |
| Memory (VRAM) | ❌ all experts must be resident, even if idle |
| Training stability | ❌ router collapse, dropped tokens, sensitive to hyperparameters |
| Inference at batch=1 | ⚠️ latency good, but memory bandwidth per useful FLOP is poor |
| Inference at high batch | ✅ excellent throughput; needs expert-parallel sharding |
| Fine-tuning | ❌ known to overfit more readily than dense equivalents |

The memory point is the one people underestimate: you host a 47B model to serve 13B of compute.
MoE is a *compute* optimisation, not a *memory* one — which is exactly why it suits large-scale
serving and suits a laptop badly.

## What an interviewer digs into next

* Why route per token rather than per sequence?
* What does an expert actually specialise in? (Often less semantic than people expect —
  frequently token- or syntax-level.)
* What is a dropped token, and how does the capacity factor trade quality for memory?
* Why does MoE need expert parallelism, and what does that do to the interconnect?
