---
id: "117"
slug: vision-language-architectures
style: serious
category: multimodal
difficulty: core
question: "How do vision-language models connect an image encoder to a language model?"
tags: [vlm, projector, cross-attention, clip, llava, flamingo]
---

# Wiring an image encoder to a language model

Almost every vision-language model (VLM) is three parts: a **vision encoder** that turns pixels
into feature vectors, a **language model** that does the reasoning and generation, and a
**connector** that makes the second one able to read the first. The interesting engineering is
entirely in the connector and in what you freeze.

## The two dominant connector designs

**Projection into the token stream (LLaVA-style).** Run the image through the encoder, get a grid
of patch features, push them through a small MLP that maps them into the LLM's embedding
dimension, and splice them into the prompt as if they were text tokens.

**Cross-attention (Flamingo-style).** Leave the text stream alone. Insert new cross-attention
layers into the LLM that attend from text hidden states to image features, gated so the model
starts as the original text model and learns to open the gate.

```
  PROJECTION                              CROSS-ATTENTION
  ──────────                              ───────────────
  image ─► ViT ─► [p1..p576]              image ─► ViT ─► [p1..p576]
                    │                                        │
                    ▼  MLP                                   │ (keys/values)
             [e1..e576]                                      ▼
                    │                        text ─► ┌───────────────┐
   "what is this?" ─┼─► LLM ─► answer              ─►│ gated x-attn  │─► LLM ─► answer
                    ▲                                └───────────────┘
       one flat sequence, LLM untouched          extra params, text seq length unchanged

  cost: 576 extra positions in context        cost: new layers, but O(1) context growth
```

Projection wins on simplicity — no architecture surgery, and the LLM's whole context mechanism
works on image tokens for free. It loses on context: a 576-token image at high resolution
becomes thousands of tokens, and you pay for them at every layer. Cross-attention keeps the text
sequence short and scales better to many images (video, interleaved documents), at the cost of
new parameters and a model you can no longer treat as a stock LLM.

A third option, the **resampler** (Perceiver/Q-Former), sits between them: a fixed set of learned
queries cross-attends to the patch grid and emits a fixed small number of tokens — 32 or 64
regardless of resolution. It bounds the cost, and it throws away detail, which is exactly the
trade you are choosing.

## What to freeze, and in what order

The standard recipe is two stages:

1. **Alignment.** Freeze the vision encoder *and* the LLM. Train only the connector, on
   image–caption pairs. Cheap, and it teaches the projector to speak the LLM's embedding
   language without disturbing either tower.
2. **Instruction tuning.** Unfreeze the LLM (and sometimes the last vision blocks). Train on
   multimodal instruction data. This is where the model learns to *follow* visual instructions
   rather than just caption.

Unfreezing the vision encoder early is the classic mistake: the gradient signal from a language
loss is a poor teacher for a visual representation, and you degrade a strong encoder to fix a
weak projector.

## The failure modes worth naming

* **Modality collapse.** If the connector is weak or the visual tokens are uninformative, the LLM
  falls back on language priors and answers from what is usually true rather than what is in the
  image. This is the root of most object hallucination (question 122).
* **Resolution mismatch.** The encoder was trained at 224px; your document is 2000px. Downsampling
  destroys the text you were asked to read (question 121).
* **Catastrophic forgetting of text ability.** Unfreeze the LLM and train only on multimodal data
  and text-only benchmarks fall. Mix text-only data back in.
* **Position confusion.** Splicing patch embeddings into a 1D sequence discards 2D structure
  unless you add 2D position information; models get spatial relations wrong ("left of") in ways
  they do not get object identity wrong.

## What an interviewer digs into next

* Why freeze the vision encoder in stage one?
* Projection versus cross-attention — when would you actually pick the second?
* How does the connector choice interact with context length and inference cost?
* How would you keep text-only capability from regressing?
