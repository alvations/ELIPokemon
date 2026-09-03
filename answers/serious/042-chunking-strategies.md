---
id: "042"
slug: chunking-strategies
style: serious
category: rag
difficulty: intermediate
question: "How do you chunk documents for retrieval, and why does it matter so much?"
tags: [chunking, rag, semantic-chunking, late-chunking, context-window]
---

# Chunking

Chunking decides what a "retrievable unit" is. It is the most consequential and least glamorous
decision in a RAG system: an embedding model cannot retrieve information that your chunking split
in half, and a reranker cannot rescue a chunk that never contained the answer.

## The core tension

```
   SMALL CHUNKS (128–256 tokens)         LARGE CHUNKS (1024–2048 tokens)
   ─────────────────────────────         ──────────────────────────────
   ✅ precise embeddings — one topic     ✅ self-contained, context intact
      per vector, so similarity is        ✅ fewer boundary casualties
      meaningful                          ❌ diluted embedding: one vector
   ✅ less irrelevant text in the prompt     averaging many topics, so it
   ❌ context lost — "it increased 40%"      matches everything weakly
      with no idea what "it" is          ❌ wastes context on irrelevant text
   ❌ answers split across boundaries

              ┌──────────────────────────────────────┐
              │  the fix is usually to DECOUPLE:     │
              │  embed small, retrieve large         │
              └──────────────────────────────────────┘
```

## Strategies, from naïve to good

**1. Fixed-size with overlap.** `N` tokens, `N/10` overlap. The baseline. Overlap gives boundary
answers a second chance. Cheap, and roughly 80% as good as anything fancier — start here.

**2. Recursive character splitting.** Split on the largest natural boundary that fits: paragraphs,
then sentences, then words. Respects structure without needing to understand it. The sensible
default, and what most libraries do.

**3. Document-structure-aware.** Split on markdown headers, HTML sections, code functions, PDF
sections. **Prepend the header path to every chunk** (`"Guide > Billing > Refunds: ..."`), which
restores the context a small chunk otherwise loses. This is a large, cheap win and it is
under-used.

**4. Semantic chunking.** Embed sentences, split where consecutive-sentence similarity drops below
a threshold. Intuitively appealing; the empirical evidence that it beats good structure-aware
splitting is weaker than its popularity suggests.

**5. Late chunking.** Embed the *whole document* with a long-context embedding model first, then
pool token embeddings into chunk vectors. Each chunk's vector is therefore computed with full
document context — so "it increased 40%" carries the knowledge of what "it" was. Elegant, and a
genuine improvement where you can afford it.

**6. Contextual retrieval.** Use an LLM to prepend a short generated description situating each
chunk in its document. Expensive to build (one LLM call per chunk, mitigated by prompt caching),
and reported to cut retrieval failures substantially.

## Decoupling what you embed from what you return

The most useful structural pattern, in three variants:

* **Small-to-big** — embed small chunks for precision, return the enclosing parent section for
  context.
* **Sentence-window** — embed single sentences, return the sentence plus `k` neighbours.
* **Multi-vector / hypothetical questions** — index several embeddings per chunk (a summary,
  generated questions it answers, the raw text), all pointing at the same chunk.

## What to do in practice

Start with recursive splitting at ~512 tokens with 10% overlap and header prepending, **then
measure**. Chunk size interacts with the embedding model's training length, the reranker, and the
question type — a chunking strategy that wins on one corpus loses on another, and this is not
predictable from first principles. Build a retrieval eval set (question → known-correct chunk) and
sweep. It is a half-day of work that routinely beats weeks of model tuning.

Also: chunk **cleaned** text. Headers, footers, navigation menus and boilerplate repeated on every
page will otherwise dominate your embeddings and retrieve constantly.

## What an interviewer digs into next

* Why does a large chunk's embedding retrieve worse, mechanically?
* Explain small-to-big retrieval and what problem it solves.
* How would you evaluate a chunking strategy?
* What is late chunking and why does it help with pronoun-heavy text?
