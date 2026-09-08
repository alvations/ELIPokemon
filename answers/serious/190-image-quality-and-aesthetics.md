---
id: "190"
slug: image-quality-and-aesthetics
style: serious
category: multimodal
difficulty: intermediate
question: "How do you score image quality and aesthetics, and what goes wrong?"
tags: [aesthetics, iqa, reward-models, filtering, bias, subjectivity]
---

# Scoring how good an image looks

Two different problems wear the same name:

* **Technical quality (IQA)** — blur, noise, compression artefacts, exposure, banding. Reasonably
  objective, and models predict human ratings well.
* **Aesthetic quality** — is this a *good picture*. Subjective, culturally situated, and where all
  the interesting failures live.

Both matter operationally: aesthetic scoring filters training corpora for generative models
(question 137), ranks generation candidates, and orders search results. So the scorer's biases become
the generator's biases, at scale.

## What aesthetic scorers actually learn

Trained on rating datasets (AVA, LAION-Aesthetics and successors), they reliably learn:

```
   HIGH SCORE                          LOW SCORE
   ──────────                          ─────────
   shallow depth of field              flat lighting
   golden-hour warmth                  cluttered background
   high saturation and contrast        anything documentary
   centred, symmetric subject          candid, unposed, ordinary
   post-processed "look"               plain snapshots
```

That is not "beauty". It is **a specific commercial-photography aesthetic**, learned from who
happened to rate the training images. Filtering a corpus by such a scorer is deciding, quietly,
what all future generated images will look like — and it is a large part of why text-to-image
outputs share a recognisable house style.

## The specific problems

* **Score is entangled with content.** These models rate photographs of certain subjects higher
  regardless of execution: landscapes and portraits over documents, diagrams, or people who are not
  young and conventionally attractive. Filtering therefore removes *subject matter*, not just poor
  images.
* **Cultural specificity.** Rating populations are narrow. Composition conventions, colour
  preference and what counts as "clean" vary; a scorer trained on one population imposes it
  globally.
* **Gameability.** As a reward signal, models learn to produce the *markers* of the aesthetic —
  bokeh, warmth, saturation — rather than better images. This is question 021's over-optimisation,
  visible to the eye: the characteristic over-processed look of a heavily aesthetic-tuned generator.
* **Confusion with prompt adherence.** An image can be beautiful and not what was asked for
  (question 137). Score them separately, always.

## Doing it responsibly

* **Use technical quality for filtering; be cautious with aesthetic scores.** Removing blurry,
  tiny, corrupted and duplicate images is safe and valuable. Removing "unaesthetic" images removes
  documentary photography, diagrams, and whole categories of subject.
* **Report what your filter removed**, by category. Look at a sample of rejected images. Teams
  routinely discover their filter was removing charts, or people, or a region's photography.
* **Score aesthetics and adherence separately**, and never combine them into a single number for
  ranking generations.
* **If it is a reward signal, cap its influence** and watch for the over-processed drift
  (question 167's informativeness lesson, in pixels).

## What an interviewer digs into next

* Why is aesthetic filtering a decision about future generations' house style?
* Why does aesthetic score entangle with subject matter?
* What does over-optimising an aesthetic reward look like, visually?
* Why keep technical and aesthetic filtering separate?
