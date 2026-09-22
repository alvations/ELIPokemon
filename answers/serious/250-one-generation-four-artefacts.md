---
id: "250"
slug: one-generation-four-artefacts
style: serious
category: open-weights
difficulty: advanced
question: "Qwen 3.8 ships a 27B dense, a Flash-Next, a 2.4T-A95B and a hosted Max. What does that line-up tell you?"
tags: [qwen, open-weights, post-training, packaging, multimodal]
---

# Four artefacts in fifteen days, and three of the four facts are not in the benchmark table

The line-up itself is the finding. Qwen 3.8 is not one model with size options; it is **four
artefacts with four different reasons to exist**, and reading them side by side tells you
something each model card on its own does not:

```
   artefact                    date         open?   total / active   input       thinking
   ─────────────────────────   ──────────   ─────   ──────────────   ─────────   ──────────
   Qwen3.8-2.4T-A95B           2026-08-12   yes*    2.4 T / 95 B     text only   always on
   Qwen3.8-27B                 2026-08-14   yes     27 B  / 27 B     + vision    switchable
   Qwen3.8-Flash-Next          2026-08-26   yes*    ~180 B / 6 B     + vision    switchable
   qwen3.8-max                 2026-08··    no      = the 2.4T       + vision    switchable
   ─────────────────────────   ──────────   ─────   ──────────────   ─────────   ──────────
   * conditional licence, not Apache — question 222. Dates for the three
     open artefacts are from the lab's own dated lists, read directly.
```

Three readings follow, and only the first one is ever in a chart.

## 1. The 27B is the same architecture as the last one, and it is worth 14 index points more

Qwen3.8-27B and Qwen3.6-27B are reported to declare the **same architecture class, the same 64
layers, the same 5,120 hidden size, the same 262,144-token context and the same 248,320-token
vocabulary**. Independently, Artificial Analysis scores them at roughly **38 and 52** on its
Intelligence Index. Same shape, same parameter count, four months apart, fourteen points.

That is corroborated first-hand from an unexpected direction: **vLLM's model registry contains no
Qwen 3.6 or Qwen 3.8 class at all.** The entire 3.5-to-3.8 line resolves through one module:

```
   "Qwen3_5ForCausalLM"                 → qwen3_5      (text only)
   "Qwen3_5MoeForCausalLM"              → qwen3_5      (text only)
   "Qwen3_5ForConditionalGeneration"    → qwen3_5      (+ vision tower)
   "Qwen3_5MoeForConditionalGeneration" → qwen3_5      (+ vision tower)
   ──────────────────────────────────────────────────────────────────
   nothing named Qwen3_6* or Qwen3_8*.  A serving framework has to
   carry a class for every architecture it supports; it carries none.
```

**What that result does license.** At fixed architecture and fixed parameter count, data and
post-training moved a broad third-party aggregate by 14 points in four months. As natural
experiments in public go, that is about as clean as it gets: the usual confound — "they also made
it bigger" — is absent, and the index is not the vendor's.

**What it does not license, and this is the half interviews are actually testing.**

- *Not* "architecture does not matter." It measures the marginal return of **holding a good
  architecture fixed**, not the contribution of choosing it. The hybrid stack was already there.
- *Not* a transfer to your task. A composite index is a weighted average over benchmarks a third
  party chose. Issue #238 on the lab's own tracker reports Qwen3.8-27B **worse** than Qwen3.6-27B
  on Tamil medical generation — 13–27% acceptance against 93% — and argues it is in the trained
  weights rather than in quantisation. A 14-point aggregate gain and a specific regression are
  compatible.
- *Not* contamination-free. Post-training is precisely the stage at which eval-shaped data enters.
  A large aggregate move with no architectural change should **raise** the contamination question.
- *Not* effort-neutral. The index entry is labelled `(xhigh)` — the default reasoning level. If
  your production setting is `low`, the 52 is not what you bought (question 220).
- *Not* proven identical. "Same layers, same hidden size" comes from config fields, not from a
  diff of tokenizer, rope settings and full-attention placement. Identical-looking configs can
  still differ where it counts.

## 2. Flash-Next is the only architecturally new thing in the generation

By the lab's own description it *"serves as an early preview of the architecture used in Qwen4"*,
with four named changes — Gated DeltaNet plus **Qwen Sparse Attention**, a four-branch **Gated
Residual**, an **N-gram Embedding** table that can be offloaded to host memory, and the **Muon**
optimizer (question 224). The shape is unusual on purpose: **125B main model, 51B of N-gram
embeddings, 6B active per token**, which coverage reports as roughly 180B of weights on disk.

So the generation contains one research artefact and three products, and the version number does
not distinguish them. Deploying Flash-Next because it says 3.8 is deploying a preview.

## 3. Max and the 2.4T-A95B are the same model, and the open one cannot see

This is the strangest fact in the family and the most instructive. The open card states plainly
that **multimodal inputs are not supported**; the hosted `qwen3.8-max` accepts text, image and
video. The capability is absent from the artefact you can download and present in the artefact you
can rent — and the two are reported to be the same model.

The mechanism is mundane and checkable. In vLLM's `qwen3_5.py`, the multimodal class is literally
a composition:

```
   Qwen3_5MoeForConditionalGeneration
   ├── self.visual         = Qwen3_VisionTransformer(config.vision_config, ...)
   └── self.language_model = Qwen3_5MoeForCausalLM(...)
                                     ▲
                                     └── this, alone, is what the open
                                         2.4T checkpoint loads as

   ship the visual.* tensors + a vision_config  →  ...ForConditionalGeneration
   ship neither                                 →  ...ForCausalLM
```

**The vision was not trained out. It was not shipped.** One subtree of weights and one string in
`config.json` separate the two artefacts. Four consequences follow directly:

1. **You cannot fine-tune it back.** You do not have the encoder or its projection. This is not a
   capability you can recover with data.
2. **It is a product decision, so it can move in both directions** — restored in a later open
   drop, or withdrawn from the endpoint — without anything about "the model" changing.
3. **Published numbers may be from the other box.** Any Qwen 3.8 result involving an image was
   measured on the artefact with the encoder. Ask which artefact before you copy a figure.
4. **Your acceptance test must name an artefact, not a family** (question 219). "We evaluated Qwen
   3.8" is not a sentence with a truth value here.

## What an interviewer is listening for

That you read a line-up as a set of decisions rather than a size ladder. Then that you can state
what the identical-architecture result proves *and* enumerate what it does not — the strongest
answers volunteer the contamination question and the effort confound before being asked. Finally,
that you treat a capability removed by packaging as different in kind from one the model never
had, because the remedies are different: one is a procurement conversation, the other is a
research problem.

## Where this stands, September 2026

The three open release dates, the Flash-Next architecture description and its 125B / 51B / 6B
split, and the absence of any Qwen 3.6 or 3.8 model class are read directly — the first two from
the Qwen team's own GitHub READMEs, the third from vLLM's `registry.py` and `qwen3_5.py` on
`main`, where the vision-tower composition above is also read first-hand. **Coverage, not
primary:** the two 27B config comparisons, the 38-and-52 Intelligence Index scores (independent of
the vendor, but relayed), the ~180B on-disk total, the Flash-Next licence name, and every
capability difference between `qwen3.8-max` and the open 2.4T including the quoted "multimodal
inputs are not supported" line — `huggingface.co`, `qwen.ai` and `alibabacloud.com` are all
blocked from this environment, and the model cards are the authority. Issue #238 is a user report
on the lab's tracker, read directly, and is one team's measurement, not a benchmark. The
four-artefact line-up will be stale by the next generation; the habit of asking *which artefact*
will not.
