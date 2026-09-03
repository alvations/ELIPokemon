---
id: "048"
slug: evaluating-rag
style: serious
category: rag
difficulty: intermediate
question: "How do you evaluate a RAG system?"
tags: [rag-evaluation, recall, faithfulness, ragas, component-eval]
---

# Evaluating RAG

The essential discipline: **evaluate the retriever and the generator separately, then end to end.**
An end-to-end score tells you the system is bad; it does not tell you which half to fix, and teams
routinely spend weeks tuning prompts to fix a retrieval failure.

```
   query ──► [RETRIEVER] ──► chunks ──► [GENERATOR] ──► answer
                  │                          │              │
             recall@k                  faithfulness    correctness
             precision@k               (grounded?)     completeness
             MRR / NDCG                citation        no-answer
                                       accuracy        behaviour
```

## Stage 1: retrieval

Requires a labelled set of (query → relevant chunk ids). Build it by sampling real queries and
having someone annotate, or by generating synthetic queries *from* chunks (cheap, but biased toward
the chunk's own phrasing — so mix in real queries).

* **Recall@k** — was a relevant chunk in the top `k`? **The most important number in the whole
  system**, because it is a hard ceiling: the generator cannot use what was never retrieved.
* **Precision@k** — what fraction of retrieved chunks were relevant. Matters because distractors
  degrade generation.
* **MRR / NDCG@k** — position-aware, which matters given that models attend unevenly across a long
  context.

Measure recall at the retriever's `k` *and* after reranking, so you can see which stage is losing
documents.

## Stage 2: generation, given the context

* **Faithfulness / groundedness** — is every claim supported by the retrieved chunks? Measured by
  decomposing the answer into atomic claims and checking each against the context with an NLI model
  or an LLM judge. This is the RAG-specific metric, and the one that catches the failure where
  retrieval worked and the model ignored it.
* **Answer relevance** — does it address the question asked?
* **Citation accuracy** — do the cited spans actually support the claims? Distinct from
  faithfulness: a model can be faithful and cite the wrong chunk.
* **Context utilisation** — of the retrieved chunks, how many were used? Low utilisation suggests
  `k` is too high.

## Stage 3: end to end

* **Answer correctness** against gold answers, by exact match where possible and LLM judgement
  otherwise.
* **No-answer behaviour** — the most under-tested dimension. Include queries whose answers are *not*
  in the corpus and verify the system says so instead of confabulating. A system that scores 90% on
  answerable questions and 0% on unanswerable ones is dangerous, and you will not notice unless you
  test it.
* **Latency and cost per query**, broken down by stage.

## Frameworks and their caveats

RAGAS, TruLens, ARES and DeepEval implement these metrics, mostly using LLM judges. They are a good
starting scaffold — but the judge inherits every bias from question 038, so validate the automated
scores against a few hundred human labels before trusting them. Report the agreement rate.

## Building the eval set

1. **Sample real queries.** Production logs, support tickets, search logs. Your imagined queries are
   not distributed like real ones.
2. **Include the hard cases deliberately**: multi-hop, unanswerable, ambiguous, queries needing
   recency, adversarial ones.
3. **Annotate relevant chunks, not just answers** — without chunk-level labels you cannot compute
   recall, and you are blind to the most important stage.
4. **Freeze and version it.** Re-annotate when the corpus or chunking changes, since chunk ids move.
5. **Track a per-stage dashboard**, not one number.

## What an interviewer digs into next

* Why is recall@k a ceiling on end-to-end quality?
* How do you measure faithfulness without human annotation?
* How would you test that the system correctly refuses unanswerable questions?
* Retrieval recall is 95% and answers are still wrong. What now?
