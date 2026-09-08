---
id: "180"
slug: mt-infrastructure-and-cost
style: serious
category: translation
difficulty: intermediate
question: "How do you run translation at scale without the bill running away?"
tags: [caching, batching, routing, cost, latency, throughput, deployment]
---

# Running translation as a service

A translation product's economics are decided by a handful of infrastructure choices, most of which
have nothing to do with model quality.

## The cost ladder, cheapest first

```
   1. CACHE          exact-match cache on (source, language pair, config)  ──► free
   2. TM             approved human translation (question 161)             ──► free
   3. SMALL NMT      dedicated model (question 135)                        ──► ~1x
   4. FINE-TUNED LLM mid-size, task-specific                               ──► ~10x
   5. FRONTIER LLM   document context, hard cases                          ──► ~50-100x
   6. HUMAN          post-edit or from scratch (question 149)              ──► ~1000x

   the entire discipline is: serve each segment from the CHEAPEST rung that is good enough,
   and use QE (question 132) to decide which rung that is.
```

Most production traffic is repetitive. In UI strings, support content and product catalogues, exact
cache hit rates of 40-80% are ordinary — and a cache hit costs nothing and is perfectly consistent,
which is a quality win as well as a cost win. **Teams routinely deploy a frontier model before
measuring their cache hit rate**, which is the wrong order.

## Cache design details that matter

* **Key on everything that changes the output**: source text, language pair, model version, glossary
  version, formality setting, domain tag. Missing one of these serves a stale translation under a
  new configuration, and it is very hard to debug because it looks correct.
* **Invalidate on glossary and model change.** A terminology update must not be masked by the cache.
* **Normalise before hashing** (question 115) so trivially different strings hit the same entry —
  but do not normalise so hard that meaningfully different strings collide.
* **Cache negative results too**: segments the QE gate rejected, so you do not repeatedly pay to
  produce something you will reject again.

## Throughput and latency

* **Batch aggressively for offline work.** Document translation is not interactive; batch APIs and
  overnight windows are dramatically cheaper.
* **Separate the interactive path.** Chat translation (question 178) has a latency budget; document
  translation has a deadline. Do not run them through the same queue.
* **Bucket by length.** Mixed-length batches waste padding; sorted batches improve throughput
  substantially.
* **Stream for long documents** so the user sees progress rather than a spinner.

## Routing is where the savings are

Send each segment to the cheapest rung that clears the bar:

* short, repetitive, low-risk → cache or small model;
* long, context-dependent, brand-visible → LLM with document context;
* QE-flagged or regulated content → human (question 132).

Measure the **distribution** of routing decisions, not just the average cost. A router sending 5% to
the frontier model and 95% to a small one has a very different cost profile from one splitting
50/50, and the average quality can be identical.

## What to monitor

Cost per segment and per language pair; cache hit rate; the routing distribution; QE score
distribution over time (a shift means your input distribution changed); p50 and p99 latency
separately; and error rates by class (question 136's off-target and repetition checks running
continuously, not only at evaluation time).

## What an interviewer digs into next

* Why measure cache hit rate before choosing a model?
* What belongs in a cache key, and what breaks if you omit one field?
* Why report the routing distribution rather than average cost?
* Why separate the interactive and batch paths?
