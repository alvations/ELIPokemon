---
id: "128"
slug: visual-grounding-spatial-reasoning
style: serious
category: multimodal
difficulty: intermediate
question: "How do models point at things in an image, and why is spatial reasoning hard?"
tags: [grounding, bounding-boxes, referring-expressions, set-of-mark, iou, gui-agents]
---

# Visual grounding and spatial reasoning

Saying *what* is in an image is one capability. Saying *where* — pointing at it precisely enough
that a downstream system can act — is a different one, and it is the capability that turns a
describer into something useful: an agent that can click, a document reader that can cite, a
detector you can audit.

## How a language model emits a location

There is no special head. Coordinates are **serialised as text tokens**:

```
   "the red cup left of the laptop"
        ▼
   <box>412 233 508 390</box>          coordinates normalised to a fixed grid (commonly 0-999)
        │    │    │    │                and emitted as ordinary number tokens
        x0   y0   x1   y1

   variants:  points  <point>460 310</point>       (cheaper, enough for clicking)
              polygons / masks as token sequences  (segmentation, far more tokens)
```

Three practical consequences of doing it this way:

* **Resolution is quantisation.** A 0-999 grid on a 4K image means each bin is several pixels.
  Fine for "click this button", too coarse for fine segmentation.
* **The model must learn digit-by-digit numeric structure.** Tokenizers that split numbers
  inconsistently (question 003) measurably hurt box accuracy — the same digit-splitting problem
  that hurts arithmetic.
* **Aspect ratio and tiling interact.** If the image was tiled (question 121), the model must map
  back to whole-image coordinates. Off-by-one tiling bugs show up as systematically shifted boxes,
  which is a very recognisable failure once you have seen it.

## Why spatial relations are genuinely hard

Object identity survives being flattened into a sequence. Geometry does not.

* **Patch order is 1D.** Unless 2D position information is explicit and well-trained
  (question 118), "above" and "below" are weakly encoded.
* **Contrastive pretraining never required it.** CLIP-style objectives treat captions
  approximately as bags of words (question 120), so "the cat on the mat" and "the mat on the cat"
  were never distinguished. A VLM built on such an encoder inherits the gap.
* **Relations are relational.** "Left of" depends on two objects *and* a frame of reference —
  the viewer's left or the subject's left? Training data is inconsistent about this, so models
  are too.
* **Counting fails for the same reason.** Beyond about four, models estimate rather than count,
  because nothing in the pretraining objective ever rewarded enumeration.

## Techniques that work

**Set-of-mark prompting.** Run a segmentation model first, overlay numbered marks on each region,
and ask the VLM to answer with a number instead of coordinates.

```
   raw image ─► segment ─► overlay ①②③④ ─► "which one is the submit button?" ─► "③"
```

This converts a hard continuous regression into an easy multiple choice, and it is a large,
reliable win — particularly for GUI agents, where a mis-click is not a graded error but a wrong
action taken in the world.

**Train on grounded data.** RefCOCO-style referring expressions, detection datasets reformatted as
text, and synthetic renders with exact ground truth. Grounding is learned, not emergent.

**Ask for boxes as evidence.** Requiring a box alongside every claimed object suppresses
hallucination (question 122) and makes answers auditable.

## Evaluation

* **IoU** (intersection over union) with **Acc@0.5** as the headline: a box counts if it overlaps
  ground truth by half. Report the threshold; Acc@0.5 and Acc@0.75 tell different stories.
* **Referring-expression accuracy** on distractor-rich scenes — the test is only meaningful when
  several similar objects are present, otherwise "find the cup" is solved by "find the only cup".
* **Relational probes with swapped arguments.** Ask "is A left of B?" and "is B left of A?" on the
  same image. A model that answers yes to both has no spatial model at all, and aggregate accuracy
  will not reveal it.
* **For agents, measure task success, not box IoU.** A box that is 0.6 IoU but centred on the
  button clicks correctly; a box at 0.8 IoU straddling two buttons does not.

## What an interviewer digs into next

* Why does set-of-mark prompting help so much?
* How does tokenisation of numbers affect box accuracy?
* Why do contrastively-pretrained encoders struggle with "left of"?
* Why is IoU the wrong metric for a GUI agent?
