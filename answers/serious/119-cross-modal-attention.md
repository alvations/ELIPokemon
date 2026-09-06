---
id: "119"
slug: cross-modal-attention
style: serious
category: multimodal
difficulty: intermediate
question: "How does cross-attention let text attend to image features?"
tags: [cross-attention, gating, grounding, attention-sinks, registers]
---

# Cross-attention between modalities

Self-attention has queries, keys and values all coming from the same sequence.
**Cross-attention** breaks that symmetry: the queries come from one stream, the keys and values
from another. In a VLM, text asks the questions and the image supplies the answers.

```
   text hidden states          image patch features
        h_1 .. h_n                  v_1 .. v_m
            │                            │
            ▼                     ┌──────┴──────┐
        W_Q · h  = Q              W_K·v = K   W_V·v = V
            │                     └──────┬──────┘
            └──────────► softmax(Q Kᵀ / √d) V ─────► context vector per text position
                              │
                              └─ an n x m map: for each WORD, how much of each PATCH it used

   cost: O(n·m) — linear in each, not quadratic in the sum
```

The shape is the point. Self-attention over concatenated text and image is O((n+m)²).
Cross-attention is O(n·m), and critically **the text sequence never grows**, so KV cache,
context budget and generation cost are unchanged no matter how many image tokens you have. That
is why cross-attention wins for video and long interleaved documents.

## Gating: how you add layers without breaking the model

Insert randomly-initialised cross-attention into a trained LLM and the first forward pass injects
noise into every residual stream, destroying the language model before it learns anything.

The fix is a **gate initialised to zero** — Flamingo uses `tanh(α)` with `α = 0`:

```
   h ← h + tanh(α) · CrossAttn(h, v)        α initialised to 0

   at step 0:  tanh(0) = 0  ►  the layer is a no-op, model behaves exactly as before
   as α grows: the model chooses, per layer, how much vision to let in
```

This is the same trick as LoRA's zero-initialised B matrix and ResNet's zero-init residual
scaling: **start as an identity function, learn your way out.** You can also read the learned
α values afterwards to see which layers actually use vision — usually the middle ones.

## Attention maps are grounding, and they are not free evidence

The n x m map tells you which patches each generated word attended to, which makes it tempting as
an explanation ("the model said 'cat' because it looked here"). Treat that carefully:

* Attention weight is not attribution. High attention on a patch does not mean the patch caused
  the output; gradient-based attribution and attention frequently disagree.
* **Attention sinks.** Transformers dump probability mass onto a few positions that carry little
  information, simply because softmax must sum to one and sometimes the right answer is "attend
  to nothing". In ViTs this shows up as high-norm artifact tokens in blank background patches;
  adding dedicated **register tokens** gives that mass somewhere harmless to go and visibly
  cleans up attention maps.
* Averaging over heads and layers destroys the signal. Individual heads specialise; the mean of
  a specialist and a sink is mush.

## Practical failure modes

* **The gate never opens.** If the visual features are poorly aligned, the cheapest thing the
  model can do is keep α near zero and answer from language priors. Check α; a model that is
  "ignoring the image" often literally is.
* **Resolution/feature mismatch.** Cross-attending to features from a frozen encoder trained on
  a different distribution gives keys that do not separate.
* **Too few queries.** Resampler designs (32-64 learned queries) bound cost but bottleneck
  detail. If your task is counting or OCR, the bottleneck is where accuracy goes.
* **No 2D structure in keys.** Without 2D position information in the patch features, the model
  can attend to *what* but not reliably to *where*.

## What an interviewer digs into next

* Why is cross-attention O(n·m) an advantage over concatenation, given both see the same data?
* What breaks if the gate is not zero-initialised?
* Why are attention maps unreliable as explanations?
* When does a fixed-query resampler cost you accuracy?
