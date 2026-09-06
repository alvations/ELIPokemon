---
id: "120"
slug: contrastive-image-text-pretraining
style: serious
category: multimodal
difficulty: intermediate
question: "How does contrastive image-text pretraining like CLIP actually work?"
tags: [clip, infonce, contrastive, temperature, siglip, zero-shot]
---

# Contrastive image-text pretraining

CLIP-style training has one idea: **two separate encoders, one shared embedding space, and a loss
that says a matched image-text pair should be closer than every mismatched one.** No captioning,
no generation, no per-image labels. Just "which caption goes with which picture".

## The loss

Take a batch of N image-text pairs. Encode both sides, L2-normalise, and compute the N x N matrix
of cosine similarities scaled by a learned temperature. The diagonal is correct; everything else
is a negative.

```
              text 1   text 2   text 3   text 4
   image 1  [  ✓   ]    ·        ·        ·
   image 2     ·     [  ✓   ]    ·        ·        maximise the diagonal
   image 3     ·        ·     [  ✓   ]    ·        minimise everything else
   image 4     ·        ·        ·     [  ✓   ]

   loss = ½·CE(rows, diagonal) + ½·CE(columns, diagonal)      (symmetric InfoNCE)
```

Three details that matter more than the diagram suggests:

* **The negatives are free.** Every other item in the batch is a negative, so a batch of 32k gives
  each example 32k-1 negatives at no extra forward cost. This is why CLIP training is
  batch-size-hungry in a way most training is not — the batch *is* the difficulty of the task.
* **Temperature is learned, and clipped.** It is parameterised as a log and typically clamped
  (CLIP caps it at the equivalent of 100). Left unbounded it runs away, because sharpening the
  distribution is an easy way to reduce loss without learning anything.
* **The loss is symmetric.** Image-to-text and text-to-image. Asymmetric versions retrieve well in
  one direction and poorly in the other.

**SigLIP** replaces the softmax with an independent sigmoid per pair. That removes the global
normalisation over the batch, so the loss no longer needs an all-gather across devices and works
well at much smaller batch sizes — a genuinely useful engineering difference, not just a tweak.

## Why it gives you zero-shot classification

Once both modalities live in one space, classification is retrieval. Embed the class names as
sentences, embed the image, take the nearest.

```
   classes ─► "a photo of a {label}"  ─► text encoder ─► [ c1 c2 ... ck ]
   image   ─────────────────────────────► image encoder ─►    v
   prediction = argmax_i  cos(v, c_i)
```

The prompt template is not cosmetic. Bare labels underperform templated ones by several points,
because captions in the training data are sentences, not nouns — the template moves the text
embedding back into the distribution the encoder actually saw. Ensembling many templates gains
another point or two.

## The known weaknesses

* **Bag-of-words behaviour.** CLIP embeddings are famously weak on *composition*: "a red cube on
  a blue sphere" and "a blue cube on a red sphere" embed almost identically. The contrastive task
  rarely requires word order, so the text tower does not learn it. Benchmarks like Winoground and
  ARO exist to expose this.
* **Counting and spatial relations** are poor for the same reason.
* **Fine-grained distinctions** need the concept to have been in the caption distribution.
  CLIP knows "bird"; it knows far less about which bird.
* **It inherits web-scale bias** directly and with no label-curation step to filter it.
* **Evaluation contamination.** Web-scraped pairs overlap with standard eval sets. If you do not
  dedup against your benchmarks, zero-shot numbers are partly memorisation.

## Where it sits in a modern stack

CLIP-style encoders are usually the **frozen vision tower** of a generative VLM (question 117),
which is why their weaknesses propagate: a VLM built on a bag-of-words image encoder will
struggle with spatial questions no matter how good the language model is.

## What an interviewer digs into next

* Why does batch size matter so much here, and what does SigLIP change?
* Why is the temperature clamped?
* Why do prompt templates help zero-shot accuracy?
* What is the compositionality failure, and how would you test for it?
