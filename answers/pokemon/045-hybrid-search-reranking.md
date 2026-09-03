---
id: "045"
slug: hybrid-search-reranking
style: pokemon
category: rag
difficulty: intermediate
question: "What is hybrid search and why add a reranker?"
tags: [hybrid-search, bm25, rrf, reranking, cross-encoder]
---

# Two scouts and a coach who reads properly

You've got two ways to find things in your scouting reports, and each is embarrassingly bad at
exactly what the other is good at.

## 🔤 The Literalist

Searches for **the exact words you typed.** Nothing else.

* ✅ *"Find report TM-4471."* → **Found it.** Instantly. Perfectly.
* ❌ *"How do I stop paying for the Gym?"* → nothing. Your reports say *"cancel membership."*
  Different words. The Literalist sees no match.

Brilliant with codes, IDs, rare proper nouns, anything exact. Completely helpless with paraphrase.

## 🗺️ The Cartographer

Searches by **meaning**, using the map.

* ✅ *"How do I stop paying?"* → finds *"cancel membership"*, because they mean the same thing.
* ❌ *"Find report TM-4471."* → returns TM-4470, TM-4472, TM-4469. To the map, all error codes live
  in the same neighbourhood.

Brilliant with meaning. Genuinely bad at exactness.

## Use both. Obviously. 🤝

```
   🔤 Literalist says:      🗺️ Cartographer says:      🏆 Combined:
   1. report_A              1. report_C                report_A ← both liked it
   2. report_B              2. report_D                report_C ← both liked it
   3. report_E              3. report_A                report_B
   4. report_C              4. report_B                report_E
```

The clever bit is **how** you combine them. You do *not* try to average their scores — the
Literalist scores things out of some unbounded number, the Cartographer scores out of one. Those
numbers mean nothing to each other.

Instead you use **only the rankings**. *"You were 3rd on one list and 1st on the other."* Anything
both scouts like rises to the top. Anything one scout loves still makes the cut. No score
reconciliation needed, nothing to tune.

## Now the coach 📋

Both scouts share a limitation, and it's a deep one.

Your scouts filed every report **before they knew what you'd ask.** They had to summarise each one
down to something searchable, guessing at what might matter later. That guess is lossy, and it's
lossy in a way that depends on the question they didn't have yet.

So bring in a **coach who reads the question and the report side by side.**

```
   🔍 THE SCOUTS                       📋 THE COACH
   ─────────────                       ───────────
   Filed everything in advance,        Reads your question and ONE
   before knowing your question.       report, together, properly.

   ⚡ Can search 10 million            🐌 Takes real time per report.
      reports instantly.               ✅ Far more accurate.
   ❌ Working from a summary           ❌ Could never do this for
      written by someone who              10 million reports.
      didn't know the question.
```

The coach cannot search your archive — they'd be reading for a month. But they can carefully read
**fifty** reports.

## So: scouts find fifty, coach picks five 🎯

```
   10,000,000 reports
          │
          ▼  🔍 both scouts, fast and rough
       50 candidates
          │
          ▼  📋 coach reads each one properly against the question
        5 best
          │
          ▼
       🧠 hand to the Trainer
```

Fast and broad, then slow and careful. The scouts optimise for **not missing anything**; the coach
optimises for **picking right**. Different jobs, and trying to do both at once is why single-stage
systems disappoint.

The coach typically improves results enormously for about fifty milliseconds of work — the best
return on time anywhere in the pipeline.

## Two things to remember 📌

**🚨 The scouts set a hard ceiling.** If the right report isn't in the fifty, the coach will never
see it. No amount of careful reading recovers something that was never fetched. **Fetch
generously** — fifty, a hundred, more if you can afford it.

**🔬 Measure the stages separately.** When someone says "our lookup system doesn't work," it's
almost always the scouts failing to fetch the right report — and you cannot see that if the only
thing you measure is whether the final answer was good. Check: *was the right report even in the
fifty?* That one number tells you which half to fix.
