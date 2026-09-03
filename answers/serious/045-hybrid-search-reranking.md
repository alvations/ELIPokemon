---
id: "045"
slug: hybrid-search-reranking
style: serious
category: rag
difficulty: intermediate
question: "What is hybrid search and why add a reranker?"
tags: [hybrid-search, bm25, rrf, reranking, cross-encoder]
---

# Hybrid search and reranking

Dense and sparse retrieval fail in **complementary** ways, which is the entire argument for
combining them.

| | Sparse (BM25) | Dense (embeddings) |
| --- | --- | --- |
| Matches | exact terms, weighted by rarity | meaning |
| `"error TM-4471"` | ✅ finds it exactly | ❌ ~ any error code |
| `"how do I stop paying?"` → *"cancel subscription"* | ❌ no shared terms | ✅ finds it |
| Rare proper nouns, IDs, codes | ✅ | ❌ |
| Negation, paraphrase | ❌ | ⚠️ partially |
| New domain, no training | ✅ works immediately | ❌ needs a suitable model |
| Interpretable | ✅ you can see the matched terms | ❌ opaque |

BM25 scores by term frequency, inverse document frequency, and length normalisation — a rare term
that appears often in a short document scores highly. It has no notion of meaning, and it is
extremely hard to beat on exact-match queries.

## Fusing the two

**Reciprocal Rank Fusion** is the standard, and its virtue is that it uses only *ranks*, so you
never have to reconcile two incompatible score scales:

$$\text{RRF}(d) = \sum_{r \in \text{retrievers}} \frac{1}{k + \text{rank}_r(d)}, \qquad k \approx 60$$

```
   BM25 ranking          Dense ranking         RRF (k=60)
   ─────────────         ─────────────         ──────────
   1. doc_A              1. doc_C              doc_A: 1/61 + 1/63 = .0323
   2. doc_B              2. doc_D              doc_C: 1/64 + 1/61 = .0320
   3. doc_E              3. doc_A              doc_B: 1/62 + 1/65 = .0315
   4. doc_C              4. doc_B              ...
                                               ▲
                    documents ranked well by EITHER survive;
                    ranked well by BOTH rise to the top
```

The alternative — normalising and weighting raw scores — is tunable but fragile, because BM25 scores
are unbounded and cosine similarities are not.

## Why add a reranker

The retriever and the reranker do genuinely different jobs.

```
  BI-ENCODER (retrieval)              CROSS-ENCODER (reranking)
  ────────────────────────            ─────────────────────────
  encode query and doc SEPARATELY     encode query and doc TOGETHER
  compare with one dot product        full attention across both

   [query] → ●                         ┌──────────────────────────┐
                 } cosine              │ [CLS] query [SEP] doc    │
   [doc]   → ●                         │   ↕ ↕ ↕ attention ↕ ↕ ↕  │
                                       └──────────┬───────────────┘
  docs pre-computed offline ✅                     ▼
  ~1 ms for 10M docs                          score 0–1
  ❌ query never "sees" the doc          ❌ must run per (query, doc) pair
                                        ❌ ~50 ms × 50 docs
                                        ✅ far more accurate
```

The bi-encoder must compress a document into a single vector **before knowing the query** — that
compression is lossy in a query-dependent way. The cross-encoder sees both at once and can attend
from query terms to document terms. It is much more accurate and far too slow to run over a corpus.

Hence the standard two-stage cascade: **retrieve 50–200 candidates cheaply, rerank them expensively,
keep 3–10.** Retrieval optimises recall; reranking optimises precision. Reranking typically buys
10–20 points of NDCG for ~50 ms, which is the best accuracy-per-millisecond available in a RAG
pipeline.

## Practical notes

* Recall at the retrieval stage is a **hard ceiling** — a reranker cannot recover a document that
  was never retrieved. Retrieve generously.
* Late-interaction models (ColBERT) sit between the two: per-token embeddings with a MaxSim
  operator, giving much of the cross-encoder's accuracy at closer to bi-encoder speed, at the cost
  of a far larger index.
* Rerankers are also the natural place to apply business logic: recency, authority, per-tenant
  boosts.
* Measure the stages separately. "RAG is bad" is usually recall@50 being bad, and you cannot see
  that if you only measure end-to-end answer quality.

## What an interviewer digs into next

* Why does RRF use ranks rather than scores?
* Why can't you just use a cross-encoder for retrieval?
* Where does ColBERT sit on the accuracy/cost curve, and what does it cost in storage?
* How would you diagnose whether a RAG failure is retrieval or generation?
