---
id: "224"
slug: muon-optimizer-and-training-stability
style: serious
category: open-weights
difficulty: advanced
question: "A lab trains its trillion-parameter models with Muon instead of AdamW. What should a practitioner take from that?"
tags: [optimizers, muon, training-stability, pretraining, attention]
---

# The optimizer stopped being settled, and the efficiency came with a new failure mode

AdamW has been the default for long enough that most engineers treat it as part of the furniture.
Moonshot's Kimi line does not. Kimi K2 — 1.04T parameters, 32.6B activated — was pre-trained on
15.5 trillion tokens with **MuonClip**, and Kimi K3 uses a per-head refinement of the same idea.
The report claims **zero loss spikes across the entire K2 run**. That is a strong claim and it is
worth understanding what it cost to make it true.

The lineage: Muon is Keller Jordan's 2024 optimizer for hidden layers. Moonshot's own *Muon is
Scalable for LLM Training* (arXiv 2502.16982, the "Moonlight" paper) is what took it to scale.
Both are cited in the K3 reference list, which I read directly; arXiv itself was blocked from this
environment, so the arXiv identifier is from that bibliography rather than from the paper page.

## What Muon does differently

Adam keeps per-coordinate second-moment estimates and scales each weight's step by its own
history. Muon instead treats a weight matrix as a matrix: it takes the momentum matrix and
**orthogonalises it with a Newton–Schulz iteration** before applying it, so the update has a
roughly flat spectrum rather than being dominated by a few directions.

Moonlight identified the two things needed to make that work at scale: **adding weight decay**,
and **matching the per-parameter update RMS** so matrix and non-matrix parameters move at
comparable scale. In the K2 algorithm listing this is the factor `sqrt(max(n, m)) * 0.2`, applied
explicitly to "match Adam RMS".

**The headline result: roughly 2x computational efficiency against a tuned AdamW baseline under
compute-optimal training — about 52% of the FLOPs for the same validation performance.** That is
a scaling-law claim from one lab's controlled experiments, and how good the AdamW baseline was is
load-bearing. Treat it as direction, not as a number you can bank.

## The failure mode the efficiency bought

Scaling Muon up surfaced a specific pathology: **exploding attention logits**, which the report
says occurs more frequently with Muon than with AdamW. In a mid-scale run (9B activated, 53B
total) max attention logits passed **1000**, which is where loss spikes and divergence live.

The two obvious fixes were both unavailable. Logit soft-capping clips the logits, but the
query-key dot products can still grow arbitrarily before the cap applies — the symptom is
treated, the weight growth is not. QK-Norm is **not applicable to multi-head latent attention at
all**, because MLA does not fully materialise its key matrices at inference. The architecture and
the optimizer were coupled, and the coupling removed the standard answer.

## QK-Clip

```
   per training step t:

   ┌─ 1. Muon step ───────────────────────────────────────────────┐
   │   M_t  = mu * M_{t-1} + G_t                 momentum         │
   │   O_t  = NewtonSchulz(M_t) * sqrt(max(n,m)) * 0.2            │
   │   W_t  = W_{t-1} - eta * (O_t + lambda * W_{t-1})            │
   └──────────────────────────────────────────────────────────────┘
   ┌─ 2. QK-Clip, PER HEAD ───────────────────────────────────────┐
   │   S_max(h) = max logit for head h, already computed in fwd   │
   │   if S_max(h) > tau:                                         │
   │        gamma = tau / S_max(h)                                │
   │        W_qc(h) *= sqrt(gamma)                                │
   │        W_kc(h) *= sqrt(gamma)                                │
   │        W_qr(h) *= gamma        (shared rotary k_R untouched) │
   └──────────────────────────────────────────────────────────────┘

   K2 used tau = 100.

   max logit
   1200 ┤        ╭─────  vanilla Muon, 53B MoE: past 1000 by step 15k
        │       ╱
    100 ┤──────────────╮
        │              ╰──────────────────  K2 with MuonClip: pinned at
      0 ┤                                   100, then decays after ~30%
        └────────────────────────────────►  of steps and never returns
```

Three details make this a good piece of engineering rather than a hack:

1. **It is applied per head, not per layer.** Only a small subset of heads explode; clipping the
   whole layer would over-regularise the healthy ones.
2. **It does not change the current step's forward or backward pass.** The max logit is used only
   as a signal for how hard to shrink the weights afterwards.
3. **It self-deactivates.** In K2, 12.7% of heads triggered the clip at least once during the
   first 70,000 steps; after that, every head had brought its max logit below the threshold and
   the clip stopped firing entirely, with no change to tau.

K3 keeps the clip and refines the optimizer itself into **Per-Head Muon**: instead of running
Newton–Schulz on the whole Q, K and V projection, it partitions the momentum along the head
dimension and orthogonalises each head's block separately, so heads with large momentum no longer
dominate a shared update direction. It also reports that this is slightly *cheaper*, because
Newton–Schulz on tall thin blocks costs less than on the full matrix.

## What a practitioner should actually take from this

* **The optimizer is a live variable again.** It was not, for most of a decade. If a frontier lab
  is willing to re-derive it, the "AdamW and move on" reflex deserves a second look.
* **Efficiency gains arrive attached to new pathologies.** Adopting an optimizer means adopting
  its failure modes, and it was one nobody was monitoring for. Log your max
  attention logit. It is cheap and it is a leading indicator.
* **Optimizer choice and architecture choice are coupled.** MLA is why QK-Norm was off the table.
  You cannot pick these two independently and expect the standard mitigations to be available.
* **Distributed implementation is the real work.** Newton–Schulz needs the full parameter matrix
  while a sharded optimizer deliberately does not have it; Moonlight ships a ZeRO-1-style
  distributed Muon and K3 describes a P2P-based orthogonalisation for the same reason.
* **Do not extrapolate a pretraining result to a fine-tune.** A 2x token-efficiency claim measured
  under compute-optimal pretraining says nothing about your LoRA run.

## What an interviewer is listening for

That you can state what Muon does in one sentence — orthogonalise the momentum matrix — and then
immediately name the cost, rather than treating the efficiency number as free. The strongest
answers volunteer that QK-Clip is per-head and self-deactivating, because that is the detail that
separates having read the report from having read a summary of it.

## Where this stands, September 2026

Figures above are from the Kimi K2 and Kimi K3 technical reports, read directly as PDFs from the
labs' GitHub repositories. Whether Muon displaces AdamW generally is unsettled; what is settled is
that one lab ran a trillion-parameter, 15.5T-token pretraining on it without a loss spike and
published the algorithm. Re-check whether the 2x figure survives independent replication with a
well-tuned AdamW baseline — that is the claim most likely to move.
