---
id: "140"
slug: multimodal-retrieval
style: serious
category: multimodal
difficulty: intermediate
question: "How do you build retrieval over documents that contain images and tables?"
tags: [multimodal-rag, colpali, late-interaction, captioning, chunking, citation]
---

# Retrieval when the corpus is not text

Standard RAG (question 044) assumes the knowledge lives in text you can embed. Real corpora do not
cooperate: slide decks, scanned reports, engineering drawings, invoices, papers where the result is
in a figure and the caption says "see Figure 3".

## Three architectures

**1. Caption everything, then do text retrieval.**

```
   page ─► VLM caption/description ─► text chunk ─► text embedding ─► normal RAG
```

Simple, reuses your entire existing stack, and **lossy at the point of no return**. Whatever the
captioner failed to mention is unretrievable forever. A chart's exact values, a small annotation, a
signature — gone if the caption did not include them. Works acceptably when documents are mostly
text with occasional illustrative figures.

**2. Joint embedding space.** Embed images and text into one space with a CLIP-style model
(question 120) and search both with one query. Elegant, and it inherits CLIP's weaknesses exactly:
bag-of-words text handling, poor fine detail, weak on text-in-image. Fine for photo libraries, poor
for documents.

**3. Retrieve over page images directly (ColPali-style late interaction).** Skip OCR and captioning
entirely. Encode each page as a grid of patch embeddings; encode the query as token embeddings;
score with MaxSim — for each query token, the best-matching patch, summed.

```
   query tokens      q₁ q₂ q₃
                      │  │  │
   page patches   ┌───┴──┴──┴───┐
                  │ ▓ ▒ ░ ▓ ▒ ░ │   score = Σ_i max_j sim(qᵢ, pⱼ)
                  │ ░ ▓ ▓ ▒ ░ ▓ │
                  └─────────────┘   each query token finds its own evidence
```

This preserves layout, figures and text without an extraction pipeline, and it **grounds
naturally** — the winning patches are where the answer is, which gives you a highlightable citation
for free. The cost is storage and compute: hundreds of vectors per page instead of one, which is
why pooling and binary quantisation matter in practice.

## Chunking is the underrated decision

Text chunking has known answers. Multimodal chunking does not, and it determines your ceiling.

* **Keep a figure with its caption and the paragraph that references it.** Splitting them destroys
  both — the figure loses its meaning, the text loses its evidence.
* **Never split a table across chunks.** A header row without its data, or data without its header,
  is worse than useless because it retrieves and misleads.
* **The page is often the right unit** for image-native retrieval, because it is the unit the
  document was designed in.
* **Preserve the reading order and hierarchy** (question 123) so a retrieved chunk carries its
  section context.

## Generation over retrieved images

Retrieval is half the system. The generator then needs the retrieved *pages* — at high enough
resolution to read them (question 121), which is expensive, so retrieve fewer and better. Ask for
**region-level citations**, not just page numbers; an answer that points at the cell it came from
is auditable, and one that points at a page is a hope.

## Evaluation

* **Retrieval and generation, measured separately.** ViDoRe-style benchmarks measure retrieval over
  document images directly. If end-to-end accuracy is poor you must know which half failed.
* **Test the modality-specific queries**: questions answerable only from a chart, only from a table,
  only from a photograph. A mixed benchmark averages these away, and a text-captioning pipeline will
  look fine on it while being unable to answer any of them.
* **Citation accuracy** — does the cited region actually contain the answer?
* **Cost per query**, honestly. Image-native retrieval is materially more expensive at index and
  query time, and that trade is the actual decision.

## What an interviewer digs into next

* What exactly does captioning-then-text-retrieval lose, and when is that acceptable?
* How does late interaction give you grounding for free?
* Why is splitting a table across chunks worse than dropping it?
* How would you decide between the three architectures for a given corpus?
