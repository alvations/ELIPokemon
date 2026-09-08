---
id: "168"
slug: multimodal-embeddings
style: serious
category: multimodal
difficulty: intermediate
question: "How do you build a single embedding space for images and text?"
tags: [embeddings, modality-gap, hard-negatives, instruction-embeddings, ann, hybrid-search]
---

# One embedding space, two modalities

Question 120 built such a space with a contrastive objective. This is about using one — and about
the property that surprises everyone who inspects theirs for the first time.

## The modality gap

Train image and text encoders contrastively and you expect the two modalities to interleave. They
do not. **Image embeddings and text embeddings occupy two separate, nearly disjoint cones**, with a
consistent offset between them, even after training to convergence.

```
   what people assume                 what is actually there

      ·img ·txt ·img                     ·img·img·img·img
    ·txt  ·img  ·txt                            (gap)
      ·img ·txt ·img                     ·txt·txt·txt·txt

   cosine similarity WITHIN a modality:  high, wide range
   cosine similarity ACROSS modalities:  lower, narrow range — a different scale entirely
```

Consequences that bite in production:

* **You cannot use one similarity threshold for both.** A cross-modal score of 0.3 may be an
  excellent match while a within-modality 0.3 is unrelated. Calibrate per modality pair.
* **Mixed-modality nearest-neighbour search returns one modality.** Query with text over an index of
  images *and* captions and the captions win every time, purely because they are nearer in the
  space. Search per modality and merge with per-modality normalised scores.
* **Averaging an image and text embedding** to make a "combined query" mostly does not work, for the
  same reason.

The gap arises from initialisation and is preserved by the contrastive loss (which only needs the
*correct* pair to be nearer than the incorrect ones — not for the modalities to mix). It can be
reduced deliberately, and most deployed encoders do not.

## Making a good multimodal retriever

* **Hard negatives are the whole game.** In-batch negatives (question 120) get you started; mining
  hard negatives — near-duplicate images, captions differing in one attribute — is what produces a
  retriever that can tell a red mug from a blue one. Without them the model learns coarse topic
  similarity and nothing finer.
* **Instruction-conditioned embeddings.** Newer multimodal embedders take a task instruction
  ("retrieve the figure that supports this claim") alongside the query, producing different
  embeddings for different intents over the same content. A meaningful improvement over one fixed
  notion of similarity.
* **Hybrid retrieval.** Dense multimodal vectors plus lexical search plus metadata filters. Dense
  retrieval is bad at exact identifiers — a part number, a filename, a person's name — and lexical
  search is excellent at them. Combine with reciprocal rank fusion rather than choosing.
* **Re-ranking.** Retrieve broadly with embeddings, then re-rank the top 50 with a cross-encoder or
  a VLM that looks at query and candidate jointly. This is where accuracy actually comes from; the
  embedding stage only has to achieve good recall.

## Practical notes

Vector dimensionality drives index cost linearly and multimodal indexes are large — Matryoshka-style
truncatable embeddings let you store short vectors and re-rank with long ones. Normalise before
indexing if your index assumes cosine. And re-embed the whole corpus on model upgrade: embeddings
from two model versions are not comparable, and mixing them silently degrades everything.

## What an interviewer digs into next

* What is the modality gap, and what does it break in a retrieval system?
* Why do hard negatives matter more than more data here?
* Why is dense retrieval bad at part numbers, and what do you pair it with?
* Why must the whole corpus be re-embedded on a model upgrade?
