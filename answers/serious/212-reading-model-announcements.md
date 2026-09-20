---
id: "212"
slug: reading-model-announcements
style: serious
category: frontier
difficulty: core
question: "A new model is announced with striking numbers and you cannot test it yet. How do you read the claim?"
tags: [evidence, benchmarks, rumour, primary-sources, procurement]
---

# Sort the claim before you argue with it

Every announcement mixes four kinds of statement, and almost all bad reasoning about models comes
from treating them as one kind.

```
  ┌─────────────────────┬──────────────────────────────────────────────┐
  │ 1. CHECKABLE NOW    │ Price. Context window. Max output. Licence.  │
  │    (minutes)        │ Exact API model ID. Regions. Availability.   │
  │                     │ Read it off the docs. Never argue about it.  │
  ├─────────────────────┼──────────────────────────────────────────────┤
  │ 2. CHECKABLE WITH   │ "80.6% on SWE-bench Verified." Meaningful    │
  │    WORK             │ only with harness version, prompt, scaffold, │
  │                     │ attempt budget. Reproducible in principle;   │
  │                     │ almost never reproduced in practice.         │
  ├─────────────────────┼──────────────────────────────────────────────┤
  │ 3. ONLY CHECKABLE   │ "Best at reasoning." "40–200× faster."       │
  │    ON YOUR TRAFFIC  │ A range spanning an order of magnitude is a  │
  │                     │ statement about the range of tasks chosen.   │
  ├─────────────────────┼──────────────────────────────────────────────┤
  │ 4. NOT CHECKABLE    │ Unreleased models. Codenames. "Sources say." │
  │    AT ALL           │ Useful for planning. Worthless as evidence.  │
  └─────────────────────┴──────────────────────────────────────────────┘
```

## Source hierarchy, in the order you should reach

1. **The docs, the model card and the system card.** Prices, IDs, limits, licences, evaluation
   methodology and stated limitations. Boring and authoritative.
2. **The technical report or paper.** Where the method is, when there is one.
3. **The vendor's launch post.** True, selected. Read for what it does *not* claim.
4. **Reputable reporting.** Useful for context and for things vendors omit.
5. **Aggregator blogs.** A large fraction of "GPT-X vs Gemini-Y" pages are assembled from each
   other. A number that exists only in tier five does not exist.
6. **Rumour.** Plan with it. Never cite it.

## The specific traps

* **Tier collapse.** "GPT-5.6 costs $5" — which of Sol, Terra and Luna? They differ by more than
  an order of magnitude and share a context window (question 205).
* **Name collisions.** Two organisations shipped an "Astra" in 2026; "Solar" and "Sol" are
  unrelated products (question 210).
* **A saturated benchmark reported as a win.** 100% means the ruler broke (question 211).
* **Comparisons against the wrong tier or an old snapshot.** Check what the competitor column is.
* **Orders-of-magnitude ranges.** "40–200×" tells you the task set was heterogeneous; your task is
  somewhere in it, and nothing in the claim says where.
* **Cost per call instead of cost per completed task.** A cheap model that needs three attempts
  and a verifier is not cheap.

## The discipline that actually works

**Write the eval before you read the announcement.** Twenty to fifty examples from your own
traffic, with a scoring function you trust, costs an afternoon and converts every future launch
from an argument into a measurement. Pin the model ID, log the served model, record the settings
(question 210). Then the only question a launch raises is when you get around to running it.

## What an interviewer is listening for

That you ask what kind of claim it is before asking whether it is true, and that you know which
facts are free to verify. The strongest answers say "I'd run our eval" and can describe the eval
— not as a gesture, but with the number of examples, the metric and the cost.

## Where this stands, September 2026

This arc of the dataset is itself a worked example. The brief that produced it named a "lunar"
model that does not exist — there is a **Luna** tier — used "Astra" as though it were one
product when two organisations ship one, and put Upstage's **Solar** next to OpenAI's **Sol** as
though they were related. Every one of those is an ordinary, easy mistake made from second-hand
material. Everything in questions 201–212 is a September 2026 snapshot, assembled from public
sources rather than from first-hand testing, and it will date faster than anything else here.
Treat it as tier three at best, and go and read the primary sources.
