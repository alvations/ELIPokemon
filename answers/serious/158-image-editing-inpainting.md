---
id: "158"
slug: image-editing-inpainting
style: serious
category: multimodal
difficulty: intermediate
question: "How does instruction-based image editing work, and why is preservation hard?"
tags: [inpainting, instruct-editing, controlnet, identity-preservation, masks, editing-metrics]
---

# Editing an image instead of generating one

Generation is unconstrained: any plausible image satisfying the prompt will do. **Editing is
constrained on both sides** — the change must happen, and *everything else must stay exactly as it
was*. The second requirement is the hard one, and it is the one benchmarks under-measure.

## Three mechanisms

**1. Mask-based inpainting.** The user supplies a region. The model regenerates inside it,
conditioned on the surroundings and a prompt. Outside the mask, pixels are untouched by
construction — preservation is *guaranteed*, not hoped for.

```
   image + mask ─► diffuse only inside the mask, attending to the outside for context
                   ▲
        outside the mask is copied verbatim. this is the strength AND the limit:
        the model cannot make a change that needs the boundary to move
```

Failure mode: **boundary artefacts** and context mismatch — lighting, grain and perspective that do
not agree across the mask edge. Feathering the mask and generating at the surrounding image's noise
level both help.

**2. Instruction-based editing (InstructPix2Pix and descendants).** No mask. "Make it winter."
The model was trained on (original, instruction, edited) triples — often synthesised by generating
paired images from paired captions. It decides for itself what to change.

Failure mode: **it changes everything**. The instruction was about the sky and the model has also
subtly restyled the faces, shifted the composition and changed the colour grade. This is the
dominant complaint about instruction editing, and it is why preservation must be measured
separately from whether the edit happened.

**3. Structure-conditioned generation (ControlNet-style).** Extract depth, edges, pose or
segmentation from the original and generate a new image conditioned on that structure. Not really
editing — regeneration that preserves layout. Excellent for restyling, useless for "remove the cup
from the table" since the cup is in the structure.

## Identity preservation

The hardest sub-problem: keep *this specific* face, product or character across an edit. Approaches
run from identity-embedding conditioning (IP-Adapter-style) to per-subject fine-tuning (DreamBooth
and LoRA variants). All of them trade **fidelity to the subject** against **editability** — push
identity hard enough and the model stops following the instruction. That curve is the real
engineering surface.

## The consequential part: provenance

Editing tools are how a photograph becomes evidence of something that did not happen. Anything you
build here should attach provenance — C2PA-style signed edit history, or an invisible watermark
(question 165 in the same family of concerns) — and should refuse edits that fabricate identifiable
people in false circumstances. This is not an add-on; retrofitting provenance after launch does not
work, because the untagged outputs are already in circulation.

## Evaluation, done properly

Report **two numbers that trade against each other**, never one:

* **Edit success** — did the requested change happen? (human rating, or a VLM judge asked
  specifically about the requested attribute)
* **Preservation** — how much of the rest survived? Measure on the *unedited region*: masked
  L1/LPIPS against the original, plus identity similarity where a subject is involved.

A model can max either alone. Copy the input: perfect preservation, zero edit success. Regenerate
from scratch: perfect edit success, no preservation. **Any single-number leaderboard here is
measuring one of those two degenerate strategies.**

## What an interviewer digs into next

* Why does mask-based inpainting guarantee preservation, and what can it therefore not do?
* Why do instruction-based editors change things they were not asked to?
* What is the identity-versus-editability trade-off?
* Why must edit success and preservation always be reported together?
