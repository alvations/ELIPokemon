---
id: "242"
slug: multimodal-pretraining-mixture
style: serious
category: open-weights
difficulty: advanced
question: "A model is pretrained on 45 trillion tokens spanning text, images, audio and video. What does that mixture buy, what does it cost, and how would you evaluate it?"
tags: [multimodal, pretraining, data-mixture, evaluation, open-weights]
---

# "45 trillion tokens" is a sum over four incommensurable units

Inkling is reported as pretrained on roughly 45 trillion tokens of text, images, audio and video.
That is a composition claim, and composition — not the total — is what decides what the model can
do. Three things follow, and the third is the one candidates skip: **a modality in the pretraining
mixture is not a capability until something measured it.**

## A token is not a token

The reference implementation that shipped into `transformers` on release day is readable from
`raw.githubusercontent.com`, and it makes the unit problem concrete. These are primary:

```
   WHAT ONE "TOKEN" IS, INSIDE A 45-TRILLION-TOKEN TOTAL

   TEXT    a BPE piece over a 201,024-entry vocabulary       ── measured, crowded field
             │
   IMAGE   a 40x40 patch; a hierarchical MLP folds a block   ── measured, thin field
           of neighbouring patches into the channel dim
             │
   AUDIO   a 100 ms chunk → 80 mel bins → each value put     ── measured, NO COMPARISON
           into one of 256 discrete bins → embedding table      (competitor columns empty)
             │
   VIDEO   the image path plus a temporal patch size of 2    ── NOT MEASURED AT ALL
             │                                                  in the mixture, not in
             ▼                                                  the card
        ┌──────────────────────────────────────────────┐
        │  ONE decoder stack. 66 layers, width 6,144.  │
        │  256 routed experts, top-6, 2 shared.        │
        │  Thin towers: an MLP for pixels, a lookup    │
        │  for mel bins. No per-modality encoder for   │
        │  the hard work to hide inside.               │
        └──────────────────────────────────────────────┘
```

Adding those four counts together produces a number, not a quantity. A word, a 1,600-pixel block
and a tenth of a second of speech carry wildly different amounts of what the model is trying to
learn, and the **fractions** — how much of the 45T was each — are what you would actually want.
They were not published. When a headline gives you a total across modalities, the first correct
response is "in what proportion", and the second is "so the total tells me almost nothing".

## What the mixture buys

The towers are deliberately thin: a small hierarchical MLP for image patches and an embedding
table over discretised mel values, with no separate pretrained encoder per modality. That is a
design bet, and it is the interesting one. **The cross-modal work is pushed into the shared
decoder rather than handled by alignment between frozen encoders.**

What that buys, concretely, is interleaving without a seam. A chart and a question about it are
the same sequence; a recording and a question about it are the same sequence. There is no
speech-recognition model to version separately, no captioner whose vocabulary disagrees with the
language model's, and no place for an error to be introduced between two components that were
trained apart. It also means audio, images and text can appear in any order in one context, which
is what makes a document plus a spoken correction a single problem rather than a pipeline.

## What it costs

* **The modality tax is paid in text.** At fixed compute, every image and audio token is a text
  token you did not train on. This is the trade, it is unavoidable, and it is why a multimodal
  model at a given scale is usually behind a text-only model of the same scale on text. Nothing in
  a headline token count exposes it.
* **Router capacity gets spent on modality identity.** Question 229 covers routing and collapse;
  the multimodal case adds a failure mode, which is experts that specialise by *modality* rather
  than by content. That looks like healthy specialisation and behaves like a smaller model per
  modality, and it is only visible if you log routing distributions per input type.
* **Sequence budget is not modality-neutral.** A 1M-token window is a million of whichever unit
  you are spending, and images and audio buy far less meaning per unit than text does. Question
  226 is the serving-side version of this; the pretraining-side version is that long-context
  ability measured on text does not transfer to long-context ability measured on video.
* **Evaluation debt.** Four modalities means per-modality suites, cross-modal suites, and an
  interference measurement — and the second two barely exist.

## The gap the release is honest about, and what to do with it

The published write-ups state that video frames go through the image path with an added temporal
dimension, that this is expected to help *downstream fine-tuning*, and that out-of-the-box video
performance **was not evaluated**. One of the four things in the headline mixture therefore has no
number attached to it anywhere.

Take that seriously in both directions. It is a costly disclosure of exactly the kind question 241
argues you should weight — nobody outside could have established it, and it forecloses a marketing
line. And it is the clean example of the rule at the top: video is in the mixture and is not a
claimed capability, and treating "pretrained on video" as "does video" is the error the sentence
exists to prevent.

## How you would actually evaluate it

1. **Per modality, knowing the fields differ in maturity.** Vision has crowded suites — MMMU-Pro,
   CharXiv — where a score sits among competitors and means something relative. Audio does not.
   Reported audio rows carry empty cells for most competitors, which means you have a number with
   **nothing beside it**. A number without a column is not a ranking, and it is precisely the
   situation where question 208's second axis — your eval, your data — is the only thing left.
2. **Cross-modal, because that is what the architecture claims.** Single-modality suites cannot
   test the thing the thin towers were chosen for. Build tasks where the answer lives in the join:
   a chart plus a spoken question, a form plus an audio amendment, a slide plus its narration
   disagreeing with it.
3. **Interference, honestly: you cannot measure it.** Pricing the modality tax requires a
   text-only twin trained on the same compute, and it does not exist. A smaller sibling on the
   same recipe controls for scale, not for mixture. Say so rather than estimating it.
4. **Watch the behavioural tell.** Reported traces show the model converting non-text input to
   text first — transcribe or OCR, then characterise, then answer. If that is the dominant
   strategy, the predicted failures are inputs whose content does not survive transcription: tone,
   timing, overlapping speakers, layout that carries meaning, motion. Test *those*, because they
   are where a transcribe-first model is weakest and where the benchmark suites are thinnest.

## What an interviewer is listening for

That you refuse to treat a cross-modal token total as a single quantity, and ask for fractions.
Strong answers name the modality tax and say who pays it. The strongest separate "in the mixture"
from "measured", spot the modality with no number, and observe that an empty competitor column
changes what a benchmark score can even mean.

## Where this stands, September 2026

The patch size, the temporal patch size, the 80 mel bins quantised into 256, the vocabulary size
and the decoder shape were read first-hand from the reference implementation on
`raw.githubusercontent.com` and are primary. The 45T figure, the modality list, the statement that
video was not evaluated, and the benchmark grid are **coverage** — the lab's pages and the model
card were blocked from here. Mixture fractions have not been published by anyone and may never be.
Suites move fast; the reasoning — sum incommensurable units at your peril, price the tax, and
never promote a training modality to a capability — does not.
