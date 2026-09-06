---
id: "124"
slug: interleaved-multimodal-data
style: serious
category: multimodal
difficulty: advanced
question: "Why train on interleaved image-text documents instead of image-caption pairs?"
tags: [interleaved, obelics, mmc4, in-context-learning, data-curation, packing]
---

# Interleaved image-text data

Caption pairs teach a model to describe one image. **Interleaved documents** — web pages,
tutorials, papers, manuals, where images and text alternate in a single sequence — teach it
something else: to hold several images in context, refer back to them, and follow a demonstration.

## Why the format changes the capability

```
   PAIRS                                INTERLEAVED
   ─────                                ───────────
   [img A] "a red bird"                 "...first, look at [img A]. Notice the crest.
   [img B] "a blue bird"                 Compare with [img B], where the crest is absent.
   [img C] "a bird in flight"            The third specimen [img C] shows..."

   one image, one description           several images, referred to by position, in one context
   -> captioning                        -> multi-image reasoning, in-context learning
```

Two capabilities come almost entirely from interleaved data:

* **Few-shot multimodal in-context learning.** Give the model three image-answer demonstrations
  and a fourth image; it infers the task. A model trained only on pairs has never seen more than
  one image in a sequence and cannot do this.
* **Reference and comparison.** "The second image", "the one on the left", "unlike the previous
  figure". These require the training distribution to contain multi-image discourse.

The standard corpora are **MMC4** (images matched back into C4 documents) and **OBELICS**
(interleaved documents extracted from Common Crawl with the document structure preserved). Both
are large, both are noisy.

## The curation problem

Interleaved web data has a weakness pair data does not: **the association between an image and
the nearby text is weak and sometimes absent.** Alt text is often empty, decorative, or SEO spam;
a photo may illustrate a paragraph three screens away; navigation icons and logos are images that
mean nothing.

What a real pipeline does:

* **Drop images that carry no information** — dimensions below a threshold, extreme aspect ratios
  (banners), near-duplicate logos repeated across a domain.
* **Filter by image-text relevance**, usually with a CLIP-style score, but with a *low* threshold.
  Filtering hard on CLIP similarity destroys the very thing you wanted: loosely-associated images
  in genuine discourse. Aggressive CLIP filtering turns interleaved data back into caption data.
* **Cap images per document** so one gallery page does not dominate a batch.
* **Deduplicate at image level and document level**, and dedup against evaluation sets.
* **Safety and licence filtering** before anything else, because you are ingesting raw web images.

## Mixing ratios

Nobody trains on interleaved data alone. The usual recipe blends:

| Source | Role |
| --- | --- |
| Caption pairs (high quality, often synthetic recaptions) | grounds objects and attributes precisely |
| Interleaved documents | multi-image context, in-context learning, discourse |
| Text-only | prevents language degradation (question 117) |
| Instruction/OCR/chart data | task-specific ability |

Removing text-only data measurably degrades language ability. Removing pair data degrades
grounding precision. The ratios are one of the least-published and most consequential parts of
any VLM recipe.

## Sequence packing

Interleaved documents vary enormously in length and image count, so packing them into fixed-length
training sequences matters:

* Pack multiple documents per sequence with **attention masking at document boundaries**, or the
  model learns spurious cross-document dependencies.
* Balance image count per sequence, or batches have wildly different vision-tower cost and you
  stall on stragglers.
* Keep image order and text order strictly aligned; an off-by-one in interleaving position is a
  silent, devastating bug — the model learns to describe the *next* image.

## What an interviewer digs into next

* Why can't a pairs-only model do multimodal in-context learning?
* Why is aggressive CLIP-score filtering harmful for interleaved data?
* What goes wrong without document-boundary attention masking?
* How would you detect an off-by-one in image placement?
