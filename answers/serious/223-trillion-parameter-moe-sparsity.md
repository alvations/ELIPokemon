---
id: "223"
slug: trillion-parameter-moe-sparsity
style: serious
category: open-weights
difficulty: advanced
question: "A lab ships a 1T-parameter MoE activating 32B, then a 2.8T one activating 104B. What is sparsity a knob for?"
tags: [mixture-of-experts, sparsity, scaling-laws, attention, open-weights]
---

# Sparsity is a ratio with its own scaling law, and it was tuned on purpose

Question 207 makes the first cut: active parameters buy FLOPs, total parameters cost memory. That
is correct and it is not the interesting part of a trillion-parameter checkpoint. The interesting
part is that **the ratio between them is a hyperparameter the lab chose, against a scaling law it
measured**, and the number it chose keeps going up.

Moonshot's Kimi line is the clearest worked example because the lab published the curve. Kimi K2
(July 2025) is 1.04T total with 32.6B activated: 384 routed experts, 8 selected per token, and 1
shared expert. Kimi K3 (July 2026) is 2.8T total with 104B activated: 896 routed experts, 16
selected, 2 shared. Both sets of figures come from the technical reports and the model-summary
tables in Moonshot's own GitHub repositories, which were reachable from this environment; the
Hugging Face model cards were not.

## The sparsity scaling law

The K2 report defines **sparsity as total routed experts divided by activated routed experts** —
384/8 = 48 for K2, 896/16 = 56 for K3. Note this is not the same number as the "active fraction"
you compute from the headline parameter counts (3.1% for K2, 3.7% for K3), because attention and
the shared experts sit outside the ratio. Interviews conflate the two constantly.

The reported finding: at **fixed activated parameters — therefore fixed FLOPs per token —**
increasing the total number of experts consistently lowers training and validation loss. Reaching
a validation loss of 1.5, sparsity 48 needed 1.69x, 1.39x and 1.15x fewer FLOPs than sparsity 8,
16 and 32 respectively. The lab stopped at 48 for K2 not because the curve stopped improving but
because, in its own words, the gain "comes with increased infrastructure complexity".

```
   fixed FLOPs per token.  vary only the pool the router picks from.

   sparsity  =  total routed experts / active routed experts

     8   ████████████████████████████████████   loss ▲     FLOPs to reach 1.5:  1.69x
    16   ██████████████████████████████         loss │                          1.39x
    32   ██████████████████████████             loss │                          1.15x
    48   ████████████████████████               loss │   ◄── Kimi K2   (384/8)   1.00x
    56   ██████████████████████                 loss ▼   ◄── Kimi K3   (896/16)

                                    ▲                          ▲
                                    │                          │
                    the curve keeps going down        the STOPPING POINT is an
                    as you add experts                infrastructure decision,
                                                      not a modelling one
```

Sparsity is therefore a knob for **buying loss with memory and interconnect instead of with
compute**. That is a very different trade from "make the model bigger", and it is why a
trillion-parameter open checkpoint is not simply a scaled-up 70B.

## Granularity, not just count

K2's architecture is explicitly compared to DeepSeek-V3 in its report: same 61 layers, same 8
active experts, but 384 total experts against 256, and an MoE expert hidden dimension of 2048.
More, *smaller* experts at the same active count is finer granularity — the router gets a more
precise answer to pick from, at the same per-token cost. K3 pushes this further with a latent-MoE
design that runs routed experts in a compact latent space (width 3584) so that widening the pool
to 896 does not make every routing decision move a full-width activation across the fabric.

## The other half of the ledger: attention

The part most candidates miss. K2 **halved** its attention heads relative to DeepSeek-V3, 128 to
64, and the report gives the reason in numbers: at a 128k sequence length, going from 64 to 128
heads raises inference FLOPs by **83%**, while buying only a 0.5–1.2% validation-loss improvement.
For an agentic model that lives at long context, that is a bad trade, and it was declined. The
attention-to-MoE ratio is where a long-context serving profile is actually decided.

## What changes at the trillion mark

The arithmetic below is mine, from the published parameter counts and public card specs — it is
not a vendor figure.

```
   Kimi K2   1.04T params  x 1 byte (FP8)              ~1.04 TB of weights
   Kimi K3   2.8T params   x 0.5 byte (MXFP4 experts)  ~1.4 TB + higher-precision
                                                        attention/router/shared ~ >1.5 TB

   H200 = 141 GB HBM        8 x H200 = 1,128 GB   ── K2 fits in ONE node at FP8
                           16 x H200 = 2,256 GB   ── K3 needs TWO

   ┌──────── node 0 ────────┐        ┌──────── node 1 ────────┐
   │  experts 0..447        │◄──────►│  experts 448..895      │
   └────────────────────────┘  RoCE  └────────────────────────┘
                                ▲
                                └ every token's routing decision that crosses
                                  here is an all-to-all over the NETWORK, not
                                  over NVLink. This is the line that matters.
```

Crossing from one node to two is the discontinuity. Inside a node, expert parallelism rides
NVLink; across nodes it rides the fabric, and a single hot expert becomes a straggler that every
other rank waits on. Moonshot open-sourced a dedicated expert-parallelism library (MoonEP,
described as achieving balanced expert execution via dynamic redundant experts) for exactly this
reason — the existence of that repository is itself evidence of where the difficulty moved.
K3 also ships MXFP4 weights with MXFP8 activations produced by **quantisation-aware training from
the SFT stage onward**, not post-training quantisation, which is the lab conceding that at this
size the deployment precision has to be a training-time decision.

## What an interviewer is listening for

That you treat sparsity as a measured design variable with a published curve, not a marketing
figure; that you can state the attention-versus-MoE trade in the same breath; and that you know
the node boundary is the real cliff, not the parameter count. The strongest answers add that
"activated parameters" and "sparsity" are two different ratios and say which one the paper meant.

## Where this stands, September 2026

The K2 and K3 figures above are from the labs' technical reports and GitHub model-summary tables,
read directly. The hardware arithmetic is mine and assumes weights only — add KV or recurrent
state, activations and fragmentation before provisioning. Sparsity will keep climbing; the
*reasoning* — fixed FLOPs, bigger pool, lower loss, higher infrastructure cost — is architectural
and will outlive both checkpoints. Re-check the model-summary table in the repository, not
coverage, when a new version lands.
