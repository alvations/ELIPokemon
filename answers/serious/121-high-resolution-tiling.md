---
id: "121"
slug: high-resolution-tiling
style: serious
category: multimodal
difficulty: intermediate
question: "How do vision-language models handle high-resolution images?"
tags: [resolution, anyres, tiling, position-interpolation, token-budget, navit]
---

# High resolution in a model trained at 224 pixels

Vision encoders are pretrained at a fixed, small resolution — 224 or 336 pixels square. Real
inputs are not: a phone photo is 4000px, a scanned invoice is 2500px, a screenshot is
1920x1080 and not square at all. Naively resizing to 336x336 destroys exactly the detail you were
asked about.

## Why you cannot just raise the resolution

Three things break at once:

1. **Position embeddings are per-grid-cell.** A 336px input at patch 14 is a 24x24 grid. Feed
   672px and you get 48x48 — embeddings that do not exist. You must **interpolate** them
   (bicubic on the 2D grid), which works surprisingly well but is a distribution shift.
2. **Token count grows quadratically.** 24x24 = 576 tokens; 48x48 = 2304; 96x96 = 9216. In a
   projection-style VLM these all land in the LLM's context.
3. **Attention cost grows quadratically in the token count**, so 4x the pixels is roughly 16x the
   attention compute inside the vision tower.

## The dominant fix: tiling with a global view

"AnyRes" / dynamic tiling, used by LLaVA-NeXT, InternVL, Qwen-VL and others:

```
   original 1344 x 672
        │
        ├─► pick a grid from a fixed menu of aspect ratios ──► 2 x 1 tiles
        │
        ├─► each tile resized to the encoder's NATIVE 336 ──► encode separately
        │        ┌──────────┐ ┌──────────┐
        │        │  tile A  │ │  tile B  │   576 tokens each
        │        └──────────┘ └──────────┘
        │
        └─► ALSO resize the whole image to 336 ──► "thumbnail"
                 ┌──────────┐
                 │  global  │   576 tokens — carries layout and context
                 └──────────┘

   sequence = [thumbnail tokens] + [tile A tokens] + [tile B tokens]     = 1728 tokens
```

The thumbnail is the part people leave out and regret. Tiles alone give you detail with no global
context: the model can read the text in tile B but does not know tile B was the bottom-right
corner of a form. The thumbnail restores the layout.

## Controlling the token budget

At 4 or 9 tiles you are spending 2300-5200 tokens per image, which dominates context and cost.
The standard levers:

* **Pixel shuffle / space-to-depth.** Fold a 2x2 group of patch tokens into one token with 4x the
  channels. Instant 4x reduction, no information discarded at the encoder — the projector absorbs
  it. Qwen2-VL and InternVL both do this.
* **Token merging / pruning.** Drop or merge similar adjacent tokens. Cheap, lossy, and usually
  fine on photographs and dangerous on documents.
* **Resampler with fixed queries.** Bounds cost absolutely, bottlenecks detail absolutely
  (question 119).
* **Cap the tile count** and accept downsampling past some size.

## Aspect ratio is a separate problem

Force-resizing to a square distorts everything non-square, and most real inputs are non-square.
Options: pad to square (wastes tokens on padding), pick from a menu of aspect-ratio grids (the
AnyRes approach), or **NaViT-style patch-n-pack** — keep native resolution and aspect ratio, pack
variable-length sequences together with attention masking. The last is the cleanest and requires
the encoder to have been trained that way.

## Evaluation traps

* Report resolution with every number. "Model A beats model B on DocVQA" is meaningless if A ran
  at 1344px and B at 336px.
* High-resolution gains concentrate almost entirely in **text-in-image and fine-detail** tasks.
  On natural-image VQA they are often nil, so an average over a mixed benchmark suite hides the
  effect.
* Check the interpolation. A silent position-embedding bug degrades everything by a little, which
  is much harder to notice than breaking one thing badly.

## What an interviewer digs into next

* Why is a thumbnail worth 576 tokens alongside the tiles?
* Where exactly does pixel shuffle lose information, if anywhere?
* What breaks when you interpolate position embeddings?
* Why do high-resolution gains not show up on natural-image benchmarks?
