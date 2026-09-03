---
id: "041"
slug: rag-vs-finetuning
style: serious
category: rag
difficulty: core
question: "What is RAG, and when should you use it instead of fine-tuning?"
tags: [rag, retrieval, grounding, fine-tuning, architecture]
---

# RAG, and when to use it

Retrieval-Augmented Generation ([Lewis et al., 2020](https://arxiv.org/abs/2005.11401)) retrieves
relevant documents at query time and puts them in the prompt, so the model *reads* rather than
*recalls*.

```
   query ──► ┌──────────────┐
             │  embed       │
             └──────┬───────┘
                    ▼
             ┌──────────────┐      ┌────────────────────────────┐
             │  vector store│◄─────│ offline: chunk → embed →   │
             │  ANN search  │      │ index your corpus          │
             └──────┬───────┘      └────────────────────────────┘
                    │ top-k candidates (k ≈ 50)
             ┌──────▼───────┐
             │  reranker    │  cross-encoder, precision pass
             └──────┬───────┘
                    │ top-n (n ≈ 5)
             ┌──────▼───────────────────────────────────┐
             │  prompt = instructions + chunks + query  │
             └──────┬───────────────────────────────────┘
                    ▼
                 generation, with citations
```

The reframing that makes RAG work: it converts a **recall** problem (which models are unreliable
at) into a **reading comprehension** problem (which they are very good at).

## RAG vs fine-tuning

| | RAG | Fine-tuning |
| --- | --- | --- |
| Adds new **knowledge** | ✅ its entire purpose | ❌ unreliable, raises hallucination |
| Changes **behaviour/style** | ⚠️ only via prompt | ✅ its entire purpose |
| Update latency | seconds (re-index one doc) | days (retrain) |
| Attribution / citations | ✅ built in | ❌ impossible |
| Access control per user | ✅ filter at retrieval | ❌ baked into weights |
| Removing a document | ✅ delete from index | ❌ requires retraining |
| Inference cost | higher (long prompts) | unchanged |
| Latency | + retrieval hop | unchanged |
| Failure mode | retrieves the wrong thing | confidently misremembers |

The decision rule is one sentence: **RAG for what the model should know, fine-tuning for how the
model should behave.** They are complementary, not competing — a fine-tuned model that follows your
citation format, retrieving from your corpus, is a common and correct design.

The under-appreciated arguments for RAG are the operational ones: **auditability** (you can show
the source), **revocability** (delete a document and it is gone, which matters for GDPR and for
licensing), and **per-user permissions** (filter the index by the caller's ACL — impossible once
knowledge is in weights).

## Where RAG breaks

* **Retrieval is now your bottleneck.** If the right chunk is not retrieved, no amount of model
  quality helps. Most "RAG doesn't work" reports are retrieval failures.
* **Global questions.** "Summarise the main themes across all 10,000 documents" is not answerable
  by top-5 retrieval. This needs hierarchical summarisation or a graph-based approach.
* **Multi-hop questions.** "Which of our customers uses the library that had the CVE?" requires two
  retrieval steps chained; single-shot retrieval fails.
* **Context dilution.** Stuffing 20 chunks in often scores *worse* than 5 good ones — more
  distractors, and the middle of a long context is poorly attended.
* **Chunk-boundary loss.** The answer spans a boundary and neither chunk contains it whole.

## Long context vs RAG

With million-token windows, why retrieve? Because RAG is cheaper (you pay for 2k tokens, not 500k),
faster, auditable, permission-filterable, and — for multi-hop and distractor-heavy tasks —
frequently *more accurate*, since a focused context beats a diluted one. Long context is the better
choice when the corpus is small enough to fit and the question genuinely requires the whole thing.
In practice hybrids win: retrieve widely, then let a long context hold more of what you retrieved.

## What an interviewer digs into next

* Why does RAG reduce hallucination more effectively than fine-tuning on the same documents?
* How would you handle a multi-hop question with a single-shot retriever?
* When is long context strictly better than RAG?
* How do you enforce per-user document permissions in a RAG system?
