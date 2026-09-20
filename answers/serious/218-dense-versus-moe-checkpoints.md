---
id: "218"
slug: dense-versus-moe-checkpoints
style: serious
category: open-weights
difficulty: advanced
question: "Qwen ships a dense 27B checkpoint and a 35B-A3B mixture-of-experts checkpoint in the same generation. When is the dense one the right answer?"
tags: [qwen, mixture-of-experts, dense-models, quantisation, fine-tuning]
---

# The two numbers are not commensurable, and that is the whole question

Alibaba's Qwen line is the best family to reason about this with, because it ships both shapes
in the same generation, weeks apart, trained on the same data. From the Qwen team's own
repository: on 2026-02-24 they released **Qwen3.5-122B-A10B, Qwen3.5-35B-A3B and Qwen3.5-27B**
together. Qwen3.6 did it again — **35B-A3B on 2026-04-16, the dense 27B on 2026-04-22**. Qwen3.8
did it a third time — **2.4T-A95B on 2026-08-12, the dense 27B on 2026-08-14**.

So you can hold "35B" and "27B" side by side and ask which is bigger. The answer is that the
question is malformed. **`35B-A3B` means 35B of weights and 3B of arithmetic.** The dense 27B
means 27B of weights and 27B of arithmetic. One of those numbers is a memory bill and the other
is a compute bill, and they are paid to different vendors (question 207).

## The arithmetic, laid out

```
   checkpoint              total    active    BF16 weights    4-bit weights   FLOPs/token
   ──────────────────────  ───────  ────────  ──────────────  ──────────────  ───────────
   Qwen3.5-27B  (dense)     27 B     27 B      ~54 GB          ~16 GB          ∝ 27 B
   Qwen3.5-35B-A3B  (MoE)   35 B      3 B      ~70 GB          ~20 GB          ∝  3 B
   Qwen3.5-397B-A17B        397 B    17 B      ~794 GB         ~220 GB         ∝ 17 B
   Qwen3.8-2.4T-A95B        2.4 T    95 B      ~4.8 TB         ~1.3 TB         ∝ 95 B

   ┌─ what actually binds ────────────────────────────────────────────────┐
   │  one 24 GB card    │  both 27B and 35B-A3B fit at 4-bit. Memory is   │
   │                    │  NOT the deciding factor at this scale.         │
   │  one 80 GB card    │  27B fits in BF16. 35B-A3B does not.            │
   │  a rack            │  2.4T-A95B in FP8 is reported at ~2,325 GiB —   │
   │                    │  16 GB300-class GPUs across four trays.         │
   └──────────────────────────────────────────────────────────────────────┘

   Same release. Two days apart. Four orders of magnitude of deployment cost.
```

That last row is the part people miss. Qwen3.8-27B and Qwen3.8-2.4T-A95B came out of the same
announcement in the same week, and one of them runs on a workstation while the other needs a
multi-node rack. "Qwen3.8 is open" is true of both and tells you nothing operational.

## Five reasons to pick the dense checkpoint that are not about memory

**1. Quality per parameter has stopped favouring sparsity at the small end.** Qwen's own
announcement for Qwen3.6-27B claims it beats the ~15× larger Qwen3.5-397B-A17B on every major
coding benchmark — SWE-bench Verified 77.2 vs 76.2, SWE-bench Pro 53.5 vs 50.9, Terminal-Bench
2.0 59.3 vs 52.5, SkillsBench 48.2 vs 30.0. Those are vendor numbers from a release blog I could
not reach directly, so treat them as a claim, not a measurement (question 212). But the direction
is corroborated by the 27B's existence: a lab does not ship a dense flagship-class coder unless
the dense path is winning something.

**2. Fine-tuning a dense model is routine; fine-tuning an MoE is a research project.** LoRA,
QLoRA and full-parameter SFT on a dense 27B are a solved workflow in every training framework.
On an MoE you inherit router collapse, dead experts, auxiliary-loss balancing and gradient noise
from the fact that each expert sees a small, non-stationary slice of your data. If the plan
involves your own data, the dense checkpoint is the one with a support matrix.

**3. Quantisation is uniform on a dense model and is not on a sparse one.** Rarely-activated
experts get the least calibration data, so post-training quantisation degrades them first — and
they are exactly the experts that serve your unusual inputs. A dense 27B at Q4 loses a little
everywhere; a sparse model at Q4 loses a lot in a few places you will not find on an average
benchmark.

**4. Batch-one latency is a flat matmul.** MoE decode speed depends on which experts this token
wants and whether they are resident on this GPU. At batch size one there is no grouping to
exploit, so the FLOP saving does not arrive and the routing overhead does. This is the same
result seen elsewhere in this dataset: a small-active MoE running *slower* than a dense model of
comparable active size on a single consumer card (question 207).

**5. The operational surface is smaller.** No expert parallelism, no all-to-all across the
interconnect, no load-imbalance dashboard, no straggler expert. For a team that does not have a
serving group, that is often the deciding argument on its own.

## When the MoE is right

When the memory is already bought and the traffic is high. At large batch, tokens scatter across
enough experts to keep every GPU busy, and you get the knowledge capacity of a 397B model for the
FLOPs of a 17B one. That is a genuinely excellent trade for a shared inference platform and a
non-trade for a single application on a single box. The other real case is capacity breadth —
multilingual and long-tail knowledge scale with *total* parameters, and Qwen3.5 claims 201
languages, which is a total-parameter-shaped claim.

## What an interviewer is listening for

That you refuse the comparison as stated and split it into a memory question and a compute
question before answering. Then that you name a binding constraint — one card, a fine-tuning
plan, a p99 target — rather than reasoning from benchmark averages. The strongest answers point
out that at 27B the dense-vs-sparse choice is mostly about *operations and tuning*, while at 2.4T
it is entirely about *memory*, and that using one argument at the other scale is the actual
mistake.

## Where this stands, September 2026

The release dates and the total/active splits above come from the Qwen team's own GitHub
repository, read directly. The parameter-to-bytes figures are arithmetic, not quotes. The
Qwen3.6-27B benchmark numbers are the vendor's own, relayed through coverage because
`qwen.ai` and `huggingface.co` are both blocked from this environment — the release blog and the
model card are the authorities and should be read before anyone cites them. Re-check the model
list every quarter; the reasoning about which number is a memory bill will outlast all of it.
