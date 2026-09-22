---
id: "239"
slug: post-training-an-open-checkpoint
style: serious
category: open-weights
difficulty: intermediate
question: "You have downloaded a frontier-scale open checkpoint. What is the path from those weights to something that does your job?"
tags: [fine-tuning, lora, post-training, distillation, open-weights]
---

# The lab paid for the expensive half and gave it away

The half that is left over is the one that decides whether you have a product. Pretraining a
975B-parameter mixture of experts over ~45 trillion tokens is a capital project. Adapting the
result to one company's job is a weekend. That asymmetry is the whole economics of an open-weight
release, and it is why a lab can hand over the expensive artefact without handing over its
business. Thinking Machines Lab put **Inkling** out under Apache 2.0 on 15 July 2026 and, in the
same breath, pointed adopters at **Tinker**, its managed post-training service. The weights are
free; the thing most teams will actually pay for is the loop that shapes them.

## The arithmetic of the asymmetry

Take the usual sparse-model convention, 6·N·D floating-point operations with N the *active*
parameters. It undercounts attention and the always-on shared experts, so read it as an order of
magnitude, not a budget. This arithmetic is mine; it is not a published figure.

```
   PRETRAINING                 6 × 41e9 active × 45e12 tokens   ≈ 1.1e25 FLOPs
   ADAPTATION (LoRA SFT)       6 × 41e9 active × 20e6 tokens    ≈ 4.9e18 FLOPs
                                                                  ────────────
                               ratio                              ≈ 2,000,000 : 1

   ┌────────────────────────────┬──────────────┬──────────────────────────────────┐
   │ WHAT YOU CAN DO            │ REL. COST    │ WHAT IT CAN BREAK                │
   ├────────────────────────────┼──────────────┼──────────────────────────────────┤
   │ system prompt / format     │ ~0           │ nothing. reversible in a commit  │
   │ few-shot exemplars         │ ~0           │ context budget only              │
   │ retrieval over your corpus │ engineering  │ latency, not behaviour           │
   │ LoRA / QLoRA SFT           │ 1×           │ tone, refusals, effort control   │
   │ full-parameter SFT         │ 50-200×      │ all of the above, permanently    │
   │ preference tuning (DPO)    │ 2-10×        │ calibration, diversity           │
   │ RL against a verifier      │ 100-1000×    │ everything, spectacularly        │
   │ distil INTO a small model  │ separate run │ nothing upstream. new model      │
   └────────────────────────────┴──────────────┴──────────────────────────────────┘
        ▲                                              ▲
        │                                              │
   start at the top and stop the moment        every rung below the line is
   your eval passes. most teams that           buying capability by spending
   "need a fine-tune" need better data         behaviour somebody else paid for
```

The ladder is ordered by cost, and it is *also* ordered by blast radius, which is not a
coincidence. The methods that can change the most are the methods that can destroy the most.

## The wrinkle that Inkling specifically introduces

Question 238 establishes that Inkling is not a base model: it ships with a chat template, a
trained `reasoning_effort` control taking `none` through `max`, tool-call and reasoning parsers,
and published refusal numbers. You are therefore not fine-tuning a blank predictor. **You are
fine-tuning a policy that reinforcement learning put into a particular shape, and RL-installed
behaviour is the first thing a supervised run removes.** Four concrete consequences:

* **Train on the model's own template, byte for byte.** Render your SFT examples through the
  shipped chat template rather than a hand-rolled prompt string. A mismatch in role delimiters or
  in the thinking markers teaches the model that its own format is wrong, and the failure shows up
  as degraded tool calling rather than as a template error.
* **Short-answer SFT collapses the effort dial.** The effort control was trained with a per-token
  cost, so the policy learned a mapping from a requested level to a chain-of-thought length. A
  fine-tuning set of terse answers is a very strong gradient towards "spend nothing", and it will
  overwrite that mapping at every level, not only the one you trained on.
* **Refusal behaviour degrades before task performance does.** Published safety figures are
  properties of the released policy. They do not survive into your derivative by default, and the
  lab says as much: treat them as a starting point and own the safety of what you make.
* **Keep a replay set.** A few per cent of on-template examples drawn from the model's own
  distribution, mixed into your SFT data, is the cheapest available defence against catastrophic
  forgetting, and it costs one afternoon.

## What "LoRA on a 975B MoE" actually touches

The choice of which matrices carry adapters matters far more on a sparse model than on a dense
one. The reference implementation shows 256 routed experts plus 2 shared per sparse layer across
66 layers. Adapting every expert is neither affordable nor sensible: any individual expert sees a
small, router-determined slice of your tokens, so its adapter is trained on a handful of examples
and overfits accordingly.

The defensible default is attention-side adapters — the query, key, value and output projections —
plus the shared experts, and **leaving the router alone**. A router is a learned load-balancing
decision made over the pretraining distribution; nudging it on twenty million domain tokens is how
you get a checkpoint that routes everything to four experts and has quietly become a much smaller
model. If the routing genuinely has to move, that is a mid-training project with balance
monitoring, not a fine-tune.

## The direction most people forget

Adaptation is not the only use of a large open checkpoint. **Using it as a teacher is often the
better answer.** A 975B model that runs on multiple nodes is a poor production server and an
excellent labeller: run it once over your corpus to produce reasoning traces, rationales,
preference pairs or structured extractions, then train a small model you can actually serve. The
published ecosystem around Inkling includes exactly this pattern, with logit-matching distillation
across differing tokenizers so the student need not share the teacher's vocabulary. The teacher
costs you a batch job; the student costs you a GPU.

## What an interviewer is listening for

That you start at the top of the ladder and can say what would have to fail before you moved down
it. Strong answers name the template as part of the contract and the replay set as the mitigation.
The strongest notice that adapting a post-trained policy is a *different* task from adapting a
base model, and that distilling out of a large checkpoint is frequently a better use of it than
serving it.

## Where this stands, September 2026

The architecture facts — 66 layers, 256 routed plus 2 shared experts, the chat template and the
effort argument — were read first-hand from the reference implementation on
`raw.githubusercontent.com`. The 975B/41B and 45T figures, the licence, the release date and the
existence of the managed post-training service are **coverage**; the lab's own pages were blocked
from here. The FLOP arithmetic is mine and rests on the 6·N·D convention. Cost ratios in the table
are rough and hardware-dependent. The ladder itself is method, not product news, and will outlast
this checkpoint; re-derive the numbers for whatever you are actually holding.
