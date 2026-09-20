---
id: "229"
slug: fine-grained-expert-routing
style: serious
category: open-weights
difficulty: advanced
question: "How does fine-grained MoE routing actually work, and what does router collapse look like while it is happening?"
tags: [mixture-of-experts, routing, load-balancing, deepseek, training]
---

# The router is a linear layer and a top-k. Everything hard is downstream of that.

Question [011](011-mixture-of-experts.md) covers what a mixture of experts is and
[207](207-sparse-moe-serving.md) covers what it costs to serve one. This is the routing itself:
how finely the experts are sliced, what stays always-on, how you stop the router collapsing onto
a handful of favourites, and what that collapse looks like while it is happening rather than
afterwards.

## The step, in shapes

DeepSeek-V3's published configuration is the one to reason from, because the file is in the lab's
own repository and the numbers reconcile against the headline:

```
   dim 7168 · 61 layers (first 3 dense) · moe_inter_dim 2048 · inter_dim 18432
   256 routed experts + 1 shared · top-8 · sigmoid gate · route_scale 2.5
   8 expert groups, a token may touch at most 4

   token h  ──► gate: h · W_g  ──► 256 sigmoid scores
                                        │
                        + per-expert bias b_i   (selection only)
                                        │
                                    top-8 ──► normalise the *unbiased* scores of
                                              the chosen 8 → gating weights g_i
                                        │
        ┌───────────────────────────────┴──────────────────────────┐
        ▼                                                          ▼
   shared expert (always)                          8 of 256 routed experts
   3 · 7168 · 2048 = 44,040,192 params             8 × 44,040,192 params
                                                          │
                        out = h + shared(h) + Σ g_i · E_i(h)
```

That is FLOP-neutral **by construction**, and it is the cleanest way to see what "fine-grained"
means. `9 × 2048 = 18432` — the width of the dense FFN in the same model. An MoE layer here fires
exactly one dense layer's worth of feed-forward arithmetic. What changed is not how much compute
runs; it is that the 18,432 columns are now chosen from a menu of 256 × 2,048 instead of being
one fixed block.

The whole model reconciles:

```
   per expert          3 · 7168 · 2048                  =     44,040,192
   257 experts × 58 MoE layers                          =        656.5 B
   + 3 dense FFN layers + 61 attention layers + embeds  =        670.9 B  (published: 671 B)

   9 active experts × 58 layers                         =         23.0 B
   + dense + attention + one embedding table            =         36.5 B  (published: 37 B)
```

If your reading of a config does not land on the announced parameter count, you have misread the
config. This one does, to within rounding.

## Why many small experts beat few large ones

At fixed active FLOPs, slicing each expert's FFN width by `m` and activating `m` times as many
buys you **combinations**:

```
   8 coarse experts, top-2     C(8,2)     =                    28 routings
   64 experts, top-8           C(64,8)    =         4,426,165,368      (DeepSeekMoE's own figure)
   256 experts, top-8          C(256,8)   =   409,663,695,276,000
```

That is the argument from [DeepSeekMoE](https://arxiv.org/abs/2401.06066): finer slices let
knowledge decompose more precisely, and the exploded combination count means the *combination*
carries information the individual experts do not have to. The cost is real and mostly
infrastructural — smaller matmuls per expert are less efficient on tensor cores, and the
all-to-all scatters more finely.

**Shared experts** are the other half of that paper. If every expert is narrow, each one ends up
re-learning the same general-purpose transformations, because some fraction of every token's
work is common. Isolating one expert that every token passes through lets the routed 256 stop
duplicating it. In V3 the shared expert is 1/9th of the active FFN compute — a cheap place to put
what everything needs.

## Load balancing, and the loss that is no longer there

Routers are positive-feedback systems. An expert that gets more tokens trains faster, becomes
better, and gets picked more. Left alone that ends in **routing collapse**: a handful of experts
do everything, the rest are dead capacity you are still paying memory for, and under expert
parallelism the GPUs holding the hot experts become stragglers every other rank waits on.

The classic fix is the Switch Transformer auxiliary loss: with `f_i` the fraction of tokens routed
to expert `i` and `P_i` the mean gate probability for it,

```
   L_aux = α · N · Σ_i f_i · P_i          typically α ≈ 0.01
```

minimised when both are uniform. It works, and it is a second objective fighting the first. The
gradient it injects is interference: you are pushing the router away from the choice it wanted,
and past some α that shows up as worse perplexity.

The 2026 default is the alternative from
[Wang et al., 2024](https://arxiv.org/abs/2408.15664), which DeepSeek-V3 shipped:

* keep a per-expert bias `b_i`, added to the score **only** for deciding the top-k;
* compute the gating weight from the **unbiased** score, so nothing the expert contributes is
  scaled by the balancing machinery;
* after each step, nudge `b_i` by `±γ` depending on whether that expert was over- or under-loaded.

No extra gradient reaches the model. The balancing lives entirely in the selection rule. The
paper measures balance with **MaxVio** — the worst expert's load divided by the mean, minus one —
and reports better perplexity *and* better balance than the tuned auxiliary loss.

DeepSeek adds a second, purely infrastructural constraint: the 256 experts sit in 8 groups, and a
token may draw its 8 from at most 4 of them. That caps how many nodes a single token's all-to-all
touches. It is a routing rule that exists for the network fabric, not for quality.

## What collapse looks like while it is happening

The trap is that **the loss curve often looks fine**. Here is what to actually watch:

```
   expert utilisation, layer 30, tokens per expert per step

   healthy                            collapsing
   ┌──────────────────────────┐       ┌──────────────────────────┐
   │▁▂▂▁▂▁▂▂▁▂▂▁▂▁▂▂▁▂▁▂▂▁▂▁▂ │       │█▁▁▁▆▁▁▁▁▁▁▇▁▁▁▁▁▁▁▁▁█▁▁▁ │
   └──────────────────────────┘       └──────────────────────────┘
    MaxVio ≈ 0.1                       MaxVio ≈ 6.0, climbing

   step time  ──► median flat, p99 rising      (one rank is a straggler)
   drop rate  ──► climbing, if capacity is finite
   gate entropy per layer:
        → 0        every token to one expert       collapse
        → log(256) routing is uniform noise        the *other* failure: no specialisation
   loss       ──► unremarkable for thousands of steps
```

Both ends of the entropy range are broken, which is why "the auxiliary loss went to zero" is not
by itself good news — a router that has become a random number generator balances perfectly and
has stopped being a router.

## Where this stands, September 2026

Sparsity keeps climbing and the slices keep getting finer. DeepSeek-V3 is 671B/37B (18×);
Mistral Large 3 is reported at 675B total with 41B active under Apache 2.0; GLM-5.3 at roughly
744B/40B under MIT; Llama 4 Maverick at 400B/17B over 128 experts plus a shared one; and Kimi K3
is reported to activate 16 of 896 experts for ~104B of 2.8T. I read DeepSeek's config file
directly; every other figure here came from coverage, because Hugging Face and arXiv are both
unreachable from this environment — read the model cards before you provision anything. The
mechanism is the durable part: a gate, a top-k, something always-on, and a balancing rule that
must not be allowed to contaminate the gradient. The specific checkpoint that best demonstrates
it will be replaced within months.

## What an interviewer digs into next

* Why is `9 × 2048 = 18432` not a coincidence?
* Why does the bias term touch selection but not the gating weight?
* Your MoE run has flat loss and a rising p99 step time. What do you plot first?

**Citation note.** The arXiv identifiers linked above are given from working knowledge and
checked against search results. `arxiv.org` is blocked from the environment this was written
in, so **not one of the papers was opened while writing**. Resolve every identifier before
you cite it.
