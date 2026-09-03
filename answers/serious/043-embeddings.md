---
id: "043"
slug: embeddings
style: serious
category: rag
difficulty: core
question: "What are embeddings and how are embedding models trained?"
tags: [embeddings, contrastive, infonce, matryoshka, cosine-similarity]
---

# Embeddings

An embedding maps text to a dense vector such that **semantic similarity becomes geometric
proximity**. "How do I reset my password?" and "I forgot my login credentials" share no content
words, but a good embedding places them close together — which is exactly what keyword search
cannot do.

## How they are trained

Modern text embedding models are trained **contrastively**. Given an anchor query `q`, a positive
passage `p⁺` that answers it, and negatives `p⁻`, minimise InfoNCE:

$$\mathcal{L} = -\log\frac{\exp(\text{sim}(q,p^+)/\tau)}
{\exp(\text{sim}(q,p^+)/\tau) + \sum_i \exp(\text{sim}(q,p_i^-)/\tau)}$$

```
                    embedding space
        ┌────────────────────────────────────────┐
        │                                        │
        │     q ●                                │   pull together ↔
        │       ╲  ← pull                        │   push apart
        │        ● p⁺                            │
        │                                        │
        │                    ● p⁻   ● p⁻         │
        │        push →     ╱      ╱             │
        │              ────╯──────╯              │
        └────────────────────────────────────────┘

   in-batch negatives: every OTHER example's positive in the batch
   serves as a negative — free, which is why batch size matters so much
```

Three practical facts that fall out of this:

* **Large batches matter enormously.** More in-batch negatives means a harder, more informative
  contrastive task. This is why embedding training uses gradient caching and very large batches.
* **Hard negatives are the main quality lever.** Random negatives are trivially separable and teach
  little. Passages that are topically similar but do not answer the query are what force fine
  distinctions. Mining them (usually with an earlier retriever) is most of the work.
* **The temperature `τ`** controls how sharply the model separates; small `τ` emphasises the
  hardest negatives.

Typical pipelines: pretrain a bidirectional encoder → weakly-supervised contrastive training on
hundreds of millions of scraped pairs (title/body, question/answer, citation pairs) → supervised
fine-tuning on curated data with mined hard negatives → optionally instruction-tuning so one model
serves multiple task types via prefixes.

## Details that matter in practice

**Pooling.** Mean pooling over token embeddings, or the `[CLS]` token, or last-token pooling for
decoder-based embedders. Mean pooling is the robust default.

**Asymmetry.** Retrieval is asymmetric: a short query and a long passage are different kinds of
text. Many models require **task prefixes** (`"query: "` / `"passage: "`). Forgetting them is a
top-three cause of silently bad retrieval.

**Normalisation.** Vectors are usually L2-normalised, making cosine similarity equal to a dot
product and to a monotone function of Euclidean distance — so the three metrics coincide. If you do
not normalise, they do not, and your index metric matters.

**Matryoshka embeddings.** Trained so that prefixes of the vector are themselves valid embeddings.
A 1536-d vector can be truncated to 256-d for a fast first-pass search, then re-scored at full
dimension. Big storage and speed savings for a small quality cost.

**Dimensionality.** 384–1536 is the usual range. Bigger is not reliably better and costs storage
and search time linearly.

## Known limits

* **Not interpretable** — you cannot inspect why two things are close.
* **Poor at exact matching** — product codes, rare identifiers, negation. `"not covered by
  warranty"` and `"covered by warranty"` are embarrassingly close. This is the main argument for
  **hybrid search** with BM25.
* **Domain-sensitive** — a general model on legal or medical text underperforms badly.
* **Fixed context** — most embedding models truncate at 512 tokens, silently.
* **Version-locked** — changing the embedding model requires re-indexing the entire corpus, and
  vectors from two models are not comparable.

## What an interviewer digs into next

* Why do in-batch negatives make batch size so important?
* Why are hard negatives necessary, and how would you mine them?
* Why do embeddings handle negation so badly?
* What breaks if you use the wrong task prefix?
