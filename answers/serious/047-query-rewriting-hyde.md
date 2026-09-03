---
id: "047"
slug: query-rewriting-hyde
style: serious
category: rag
difficulty: advanced
question: "What are query rewriting and HyDE, and when do they help?"
tags: [hyde, query-expansion, multi-query, step-back, rag]
---

# Query transformation

Retrieval fails when the query and the answer are written differently. Query transformation attacks
that gap on the **query side**, before search happens.

## The problem

```
   user asks:  "why is my thing broken"
   corpus has: "Error 4471 occurs when the authentication token expires
                after 24 hours of inactivity."

   Shared vocabulary: none.  Dense retrieval: weak. BM25: nothing.
```

Real queries are short, underspecified, conversational, full of pronouns referring to earlier turns,
and written in the user's vocabulary rather than the corpus's.

## The techniques

**1. Multi-query expansion.** Generate `n` paraphrases, retrieve for each, fuse with RRF.

```
   "how do I cancel?"
        ├─► "steps to cancel a subscription"
        ├─► "terminate my membership"
        └─► "stop recurring billing"
                    │
                    ▼  retrieve each, fuse ranks
```

Simple, robust, and the highest-value transformation for most systems. It directly increases recall
by covering more phrasings.

**2. HyDE — Hypothetical Document Embeddings**
([Gao et al., 2022](https://arxiv.org/abs/2212.10496)). Ask the LLM to *hallucinate an answer*, then
embed **that** and search with it.

```
   query:   "why is my thing broken"
              │  LLM writes a plausible answer (probably factually wrong)
              ▼
   hypothetical: "This error typically occurs when the authentication
                  token expires. Sessions time out after a period of
                  inactivity and must be re-established."
              │  embed THIS, discard the text
              ▼
   search ──► retrieves the real doc, which looks like this text
```

The insight is that it fixes an **asymmetry**: queries and documents live in different regions of
embedding space (short/interrogative vs long/declarative). HyDE moves the search vector into
*document* space, where the neighbours are actual documents. The hypothetical answer being factually
wrong does not matter — you only need it to be *stylistically and topically* right.

**3. Step-back prompting.** Ask a more general question first, retrieve for both.
*"Which school did Estella Leopold attend in Aug 1954?"* → *"What is Estella Leopold's education
history?"* Retrieving broader context and then reasoning within it beats retrieving on an
over-specific query that matches nothing.

**4. Query decomposition.** Split multi-hop questions into sub-questions, retrieve for each, and
compose. *"Which of our customers uses the library with the CVE?"* → *"which library had the CVE?"*
then *"which customers use library X?"* Single-shot retrieval cannot answer chained questions; this
is the standard fix.

**5. Contextual rewriting.** In multi-turn chat, resolve pronouns and ellipsis against history
before retrieving. *"What about the second one?"* is un-retrievable; rewriting it to *"What are the
side effects of the second medication, metformin?"* is trivially retrievable. **This is mandatory
for any conversational RAG system** and is the single most commonly missing piece.

## When they help — and when they don't

| Helps when | Doesn't help when |
| --- | --- |
| Queries are short and vague | Queries are already well-specified |
| Vocabulary mismatch between users and corpus | Users and corpus share vocabulary |
| Multi-turn conversation | Single-shot, self-contained queries |
| Multi-hop questions | Simple lookups |
| The corpus is technical, the users are not | Exact-match queries (IDs, codes) — expansion *hurts* |

Every transformation costs an LLM call: 200–500 ms of latency and real money, on the critical path
before retrieval even starts. Multi-query also multiplies retrieval cost by `n`.

The honest ordering: **fix chunking, add a reranker, add hybrid search — then consider query
transformation.** Query rewriting is a genuine win on the hard queries and an easy way to add
latency to a system whose actual problem was elsewhere. And always measure: on an already-good
retriever, HyDE sometimes *reduces* accuracy by pulling the query toward a plausible-but-wrong
region.

## What an interviewer digs into next

* Why does HyDE work despite generating factually wrong text?
* Which of these would you implement first for a conversational assistant?
* Why does query expansion hurt exact-match queries?
* How would you decide, per query, whether to apply a transformation?
