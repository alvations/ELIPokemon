---
id: "159"
slug: referring-segmentation
style: serious
category: multimodal
difficulty: intermediate
question: "How do models select a specific region of an image from a description?"
tags: [segmentation, sam, open-vocabulary, referring-expressions, miou, part-whole]
---

# Referring segmentation: language to pixels

Question 128 covered pointing with a box. A box is a poor description of most things — a box around
a bicycle is mostly not bicycle. **Segmentation** asks for the actual pixels, and adding language
to it asks for *the pixels of the thing I described*, which is a different problem from *the pixels
of every object*.

## Three capabilities, often conflated

| | What you give it | What you get |
| --- | --- | --- |
| **Promptable segmentation** (SAM-style) | a point, box or scribble | the mask of whatever is there — no semantics at all |
| **Open-vocabulary segmentation** | a class name | masks for every instance of that class |
| **Referring segmentation** | a full expression: "the mug behind the laptop" | exactly one mask, resolved by the description |

The third is the hard one, because the expression must be *resolved*, not just matched. "The
second cup from the left" requires counting and ordering; "the one he is holding" requires relating
two entities.

## The standard architecture

```
   image ──► vision encoder ──► dense features ─┐
                                                 ├──► mask decoder ──► mask
   "the mug behind the laptop" ──► text enc ────┘
                                    ▲
        fusion happens BEFORE the mask decoder, so language shapes which
        pixels are selected — not "segment everything, then filter by text"
```

Segment-then-filter is the obvious design and it is worse: it commits to a segmentation before
knowing what was asked, so it cannot honour part-whole distinctions ("the handle", "the tail
flame") that the class-agnostic segmenter never proposed.

A powerful practical pattern is the **hybrid**: run a promptable segmenter to get candidate masks,
overlay numbered marks, and let a VLM choose (set-of-mark, question 128). This converts a hard
dense-prediction problem into multiple choice and it is often better than an end-to-end referring
model, at the cost of two model calls.

## Where it fails

* **Ambiguous expressions.** "The cup" in a scene with three cups. The honest behaviour is to
  return several masks or ask; most systems silently pick one.
* **Part versus whole.** "The wheel" on a bicycle, "the handle" on a mug. Datasets are dominated by
  whole objects, so parts are under-learned.
* **Negation and exclusion.** "The cup that is *not* red" — same failure as question 137's negation
  problem, arriving through the text encoder.
* **Relational expressions** requiring spatial reasoning (question 128).
* **Stuff versus things.** "The grass" has no instances; "the sheep" does. Models trained on
  instance data handle amorphous regions poorly.

## Evaluation

**mIoU** (mean intersection over union) is standard, with **cIoU** (cumulative, computed over the
whole dataset's pixels) reported alongside because they disagree: mIoU weights every image equally,
cIoU weights every pixel, so mIoU is dominated by small objects and cIoU by large ones. Report both
or say which you used.

Beyond that:

* **Test with distractors.** "Find the mug" in a one-mug image measures detection, not referring.
* **Measure the ambiguous cases separately**, and check what the model does with them — a system
  that always picks confidently is worse than one that flags ambiguity, and the aggregate score
  prefers the confident one.
* **Boundary quality** (boundary F-score) separately from region overlap; a mask can have good IoU
  and unusable edges for compositing.

## What an interviewer digs into next

* Why fuse language before the mask decoder rather than filtering afterwards?
* When does set-of-mark beat an end-to-end referring model?
* Why do mIoU and cIoU disagree, and which do you want?
* What should a model do with a genuinely ambiguous referring expression?
