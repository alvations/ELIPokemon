---
id: "094"
slug: multimodal-models
style: serious
category: multimodal
difficulty: intermediate
question: "How do vision-language models fuse modalities?"
tags: [multimodal, vlm, vision-encoder, projector, cross-attention, llava]
---

# Vision-language models

The problem: an LLM consumes token embeddings; an image is a grid of pixels. Fusion is the question
of **where and how the visual signal enters the language model.**

## The three architectures

```
 ┌─ EARLY FUSION / PROJECTION (LLaVA, Qwen-VL, most open VLMs) ────────┐
 │  image ─► [ViT] ─► patch embeddings ─► [MLP projector] ─► "tokens"  │
 │                                                    │                 │
 │  text  ─► [tokenizer] ─► token embeddings ────────┼──► [ LLM ]      │
 │                                                                      │
 │  Visual features are projected INTO the LLM's embedding space and    │
 │  concatenated with text tokens. The LLM is unmodified.               │
 │  ✅ simple, cheap to train, reuses everything                         │
 │  ❌ images consume context (576–2000+ tokens each)                    │
 ├─ CROSS-ATTENTION (Flamingo, Llama 3.2 Vision) ──────────────────────┤
 │  Insert new cross-attention layers into the frozen LLM that attend   │
 │  to visual features. Text tokens query the image.                    │
 │  ✅ image costs no context; LLM weights preserved exactly             │
 │  ❌ new parameters, architectural surgery, more complex               │
 ├─ NATIVE MULTIMODAL (Chameleon, Gemini-class) ──────────────────────┤
 │  Train from scratch on interleaved image and text tokens with a      │
 │  shared vocabulary (images discretised by a VQ tokenizer).           │
 │  ✅ deepest integration; can GENERATE images too                      │
 │  ❌ enormously expensive; cannot reuse a text-only checkpoint         │
 └──────────────────────────────────────────────────────────────────────┘
```

## The projection recipe in detail

The dominant open-source approach, because it is cheap and works:

1. **Vision encoder** — a pretrained ViT, usually CLIP's or SigLIP's, precisely because
   CLIP training already aligned its features with language (question 092). Output: `N` patch
   embeddings (576 for 24×24 patches at 336px).
2. **Projector** — an MLP mapping vision dimensions to LLM embedding dimensions. LLaVA showed a
   two-layer MLP is enough; more elaborate resamplers (Q-Former, Perceiver) compress the token count
   but add complexity and have largely lost on the quality/simplicity tradeoff.
3. **Training, in two stages** —
   * *Alignment:* freeze the vision encoder and the LLM, train only the projector on image-caption
     pairs. Cheap; teaches the projector to speak the LLM's language.
   * *Instruction tuning:* unfreeze the LLM (and sometimes the encoder), train on multimodal
     instruction data.

The remarkable part is how little this costs: LLaVA reached strong results with ~600k image-text
pairs and a day of training, by reusing a strong vision encoder and a strong LLM and learning only
the bridge.

## The hard problems

* **Resolution.** A ViT at 336px cannot read a document. Solutions: tiling (split into crops and
  encode each, as LLaVA-NeXT does), native dynamic resolution (Qwen2-VL), or higher-resolution
  encoders. Each multiplies token count.
* **Token budget.** At 576+ tokens per image, a few images dominate the context. Token reduction
  (pooling, perceiver resampling) trades detail for room.
* **Spatial reasoning** remains weak — counting, relative positions, precise localisation.
* **Modality imbalance.** Models often ignore the image when the text alone suggests a plausible
  answer, producing confident text-only hallucinations.
* **Video** multiplies everything by frame count; frame selection and temporal pooling are the active
  problems.

## Beyond vision

Audio (Whisper-style encoders projected in), 3D, and any-to-any models follow the same recipe:
**encode the modality, project into the LLM's embedding space, train the bridge.** The LLM has become
a general-purpose reasoning engine over anything you can embed — which is the conceptual point worth
making.

## What an interviewer digs into next

* Why use a CLIP encoder rather than a plain ImageNet ViT?
* What does cross-attention buy over projection, and what does it cost?
* Why does resolution matter so much, and what does tiling cost?
* Why do VLMs sometimes ignore the image entirely?
