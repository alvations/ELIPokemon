---
id: "046"
slug: cross-encoder-vs-bi-encoder
style: serious
category: rag
difficulty: intermediate
question: "What is the difference between a bi-encoder and a cross-encoder?"
tags: [bi-encoder, cross-encoder, colbert, late-interaction, retrieval]
---

# Bi-encoders vs cross-encoders

The difference is **when** the query and the document meet.

```
  BI-ENCODER                             CROSS-ENCODER
  ──────────                             ─────────────
   query          document                query + document, concatenated
     │               │                             │
   ┌─▼──┐         ┌──▼─┐                    ┌──────▼──────┐
   │ enc│         │enc │  ← offline!        │  encoder    │
   └─┬──┘         └──┬─┘                    │  full cross │
     │               │                      │  attention  │
     ▼               ▼                      └──────┬──────┘
    ● ────cosine──── ●                             ▼
                                                score ∈ [0,1]

  documents encoded ONCE, ahead of time    nothing can be precomputed
  query time: one dot product              query time: a full forward pass
  10M docs in ~1 ms                        50 docs in ~50 ms
  ❌ the document vector was computed       ✅ every query token can attend
     without knowing the query                to every document token
```

## The information-theoretic framing

A bi-encoder must compress an entire document into one fixed vector **before the query exists**. It
has to guess which aspects will matter. For a document covering five topics, one vector is an
average of five things and matches all of them weakly.

A cross-encoder never compresses. It sees the pair together and can compute genuinely
query-conditional features — term overlap, negation, whether the document *answers* the question or
merely mentions it. That is why it is consistently 10–20 NDCG points better and why it can never be
used for retrieval: scoring 10M documents at 50 ms each is 140 hours per query.

Note the symmetry: the bi-encoder's weakness *is* its strength. Precomputability is exactly what
makes search possible, and it is bought with query-independence.

## Late interaction: ColBERT

[ColBERT](https://arxiv.org/abs/2004.12832) sits between them. Encode query and document
independently — but keep **per-token** embeddings rather than pooling to one vector. Score with
MaxSim: for each query token, take its maximum similarity to any document token, and sum.

$$s(q,d) = \sum_{i \in q} \max_{j \in d} \; q_i \cdot d_j$$

```
   query tokens:  [how] [cancel] [subscription]
                     ╲      │ max        │ max
   doc tokens: [to][end][your][plan][please][contact]
                        ▲              ▲
   each query token finds its best match anywhere in the document,
   independently — interaction, but only at the very end
```

Document embeddings are still precomputable, so it retains search-ability, and the token-level
interaction recovers much of the cross-encoder's accuracy. The cost is storage: one vector *per
token* rather than per document — 10–100× the index size, mitigated by aggressive quantization
(PLAID, ColBERTv2).

## The cascade

| Stage | Model | Candidates | Latency | Optimises |
| --- | --- | --- | --- | --- |
| 1. Retrieve | bi-encoder + BM25 | 10M → 100 | ~10 ms | recall |
| 2. Rerank | cross-encoder | 100 → 10 | ~50 ms | precision |
| 3. Generate | LLM | 10 → answer | ~1 s | the answer |

Each stage is cheap relative to the next stage's per-item cost, which is the general principle
behind every cascade: spend more per item as the candidate set shrinks.

## Training

Bi-encoders train contrastively with in-batch and hard negatives (the negatives are what teach fine
distinctions). Cross-encoders train as pointwise binary classifiers or with pairwise/listwise ranking
losses on (query, relevant, irrelevant) triples — and they benefit enormously from *hard* negatives
mined by the bi-encoder that will feed them in production, so the reranker is trained on exactly the
distribution it will see.

## What an interviewer digs into next

* Why is precomputability incompatible with query-conditional scoring?
* Explain MaxSim and why ColBERT's index is so much larger.
* How would you train a reranker for your own domain?
* What is the right candidate count for stage 1, and how would you choose it?
