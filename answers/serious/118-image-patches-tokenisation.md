---
id: "118"
slug: image-patches-tokenisation
style: serious
category: multimodal
difficulty: core
question: "How is an image turned into tokens a transformer can read?"
tags: [vit, patches, position-embeddings, patch-size, pooling]
---

# Turning an image into a token sequence

A transformer consumes a sequence of vectors. An image is a grid of pixels. The Vision
Transformer's answer is deliberately blunt: **cut the image into fixed square patches, flatten
each one, project it, and call the result a token.**

## The mechanics

For a 224x224 image with 16x16 patches:

```
   224 x 224 x 3 pixels
        │
        ├─ cut into a 14 x 14 grid of 16x16 patches ──► 196 patches
        │
        ├─ flatten each patch:  16*16*3 = 768 raw numbers
        │
        ├─ linear projection ──► 768-dim embedding      (this is the "patch embedding")
        │
        └─ add a POSITION embedding, one per grid cell
                    │
                    ▼
        [ pos+p(0,0) ][ pos+p(0,1) ] ... [ pos+p(13,13) ]   ─►  196 tokens ─► transformer
```

Note what the projection actually is: a learned linear map applied to every patch identically.
It is implemented as a strided convolution — kernel 16, stride 16 — which is the same operation
written more efficiently. There is no hierarchy, no pooling pyramid, no hand-designed feature
extractor. That is the point of the architecture.

## Why position embeddings are not optional here

Self-attention is permutation-invariant. Without position information the model sees an unordered
bag of 196 squares and cannot distinguish a face from the same face with the eyes and mouth
swapped. Text gets away with 1D positions; images need the **2D grid structure**, either through
learned per-cell embeddings, factorised row+column embeddings, or 2D RoPE (question 002).

This matters at inference: change the input resolution and the grid changes shape, so the
position embeddings must be **interpolated** to the new grid. Doing this badly is a common
source of silent accuracy loss when someone fine-tunes at a resolution the encoder was not
pretrained at.

## The patch-size trade-off

| Patch size | Tokens at 224px | Detail retained | Compute |
| --- | --- | --- | --- |
| 32x32 | 49 | coarse | cheap |
| 16x16 | 196 | standard | baseline |
| 14x14 | 256 | finer | ~1.3x |
| 8x8 | 784 | fine | ~16x attention cost |

Attention is quadratic in token count, so halving the patch size roughly **sixteen-times** the
attention cost. Everything below the patch size is invisible: a 16px patch at 224px on a
document scan is far coarser than a character, which is why document VLMs either raise
resolution, tile the image, or use a dedicated OCR path (questions 121, 123).

## Getting a single vector out

Downstream you often want one embedding, not 196. Two conventions:

* **`[CLS]` token** — prepend a learned token, use its final state. Inherited from BERT.
* **Global average pooling** over patch tokens. Slightly better in several careful comparisons
  and has no special-token asymmetry.

For a VLM you usually want **neither** — you keep all the patch tokens, because the language
model needs to attend to specific regions, not to a summary.

## Alternatives worth knowing

* **Discrete tokenisation (VQ-VAE / VQ-GAN).** Quantise patches against a learned codebook so an
  image becomes a sequence of integer codes, exactly like text. Enables autoregressive image
  *generation* with a standard LM. Costs reconstruction fidelity at the quantisation step.
* **Hierarchical encoders (Swin, ConvNeXt).** Reintroduce a pyramid and local windows. Better
  for dense prediction (segmentation, detection) where fine spatial detail must survive.
* **Patch n' Pack / NaViT.** Pack variable-resolution images into one sequence with masking, so
  you stop distorting aspect ratios by force-resizing everything to a square.

## What an interviewer digs into next

* Why is a patch embedding equivalent to a strided convolution?
* What breaks if you change input resolution at inference?
* How does patch size trade against attention cost, quantitatively?
* When would you use a discrete image tokenizer instead of continuous patches?
