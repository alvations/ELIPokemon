---
id: "046"
slug: cross-encoder-vs-bi-encoder
style: pokemon
category: rag
difficulty: intermediate
question: "What is the difference between a bi-encoder and a cross-encoder?"
tags: [bi-encoder, cross-encoder, colbert, late-interaction, retrieval]
---

# The filing clerk and the coach

Both judge whether a scouting report answers your question. The difference is **when they look at
the question.**

## 🗂️ The filing clerk — files first, asks later

Reads every report **months in advance** and writes each one a single index card — *"Ferrothorn:
Grass/Steel, defensive"* — then files them.

When your question arrives, they compare your question to the cards. Ten million cards in about a
millisecond.

The catch is baked into the job. They wrote those cards **without knowing what you'd ask.** A report
covering five different Pokémon gets one card that vaguely gestures at all five — and matches every
question about any of them, weakly.

## 📋 The coach — reads them together

Puts your question and one report side by side and reads both, properly.

They can spot things no index card could ever capture: that the report *mentions* Gyarados but
doesn't actually say anything about countering it. That it says "**not** weak to Electric." That it
answers a subtly different question than the one you asked.

Enormously more accurate. And useless for searching, because ten million reports at a minute each is
a career.

```
  🗂️ FILING CLERK                    📋 THE COACH
  ──────────────                      ───────────
  question ●     ● card               ┌──────────────────────┐
            ╲   ╱                     │  question + report,  │
             ╲ ╱   one glance         │  read TOGETHER,      │
              ✕                       │  every line          │
                                      └──────────┬───────────┘
  ⚡ 10 million in 1ms                            ▼
  ❌ card written before                       verdict
     the question existed              🐌 one at a time
                                       ✅ genuinely reads it
```

📌 The clerk's weakness **is** their strength. Filing in advance is the only reason searching is
possible at all — and the price of filing in advance is not knowing the question.

## 🃏 The middle option: a card per line

There's a third approach that splits the difference nicely.

Instead of one index card per report, write **one card per line** of the report. Still filed in
advance — still searchable.

Now when your question comes in, each *word* of your question goes hunting for its best matching
*line*:

```
   your question:  [how] [counter] [Gyarados]
                      ╲      │            │
                       ╲     │ best match │ best match
   report lines:  [to][beat][the][Water][ace][use][Electric]
                            ▲                    ▲
   Each part of your question finds its best match anywhere
   in the report — independently.
```

Much of the coach's insight, still fast enough to search. The price is **storage**: a card per line
instead of per report is ten to a hundred times more filing cabinets.

## How they work together 🎯

```
   10,000,000 reports
          │  🗂️ clerk — instant, rough
          ▼
       100 candidates
          │  📋 coach — reads each one properly
          ▼
       10 best
          │  🧠 Trainer — writes the answer
          ▼
       your answer
```

The principle: **spend more effort per item as the pile gets smaller.** A millisecond each across
ten million, fifty milliseconds each across a hundred, a full second on the last ten. Each stage
earns the next stage's expense.

## Training them 🏋️

**The clerk** learns from near-misses — reports that look relevant but aren't. Obvious mismatches
teach nothing.

**The coach** learns the same way, with a crucial detail: train them on **the exact hundred reports
the clerk will actually hand them.** Not a random sample. The coach's whole job is to sort the
clerk's shortlist, so that's the pile they should practise on.

Train the coach on easy piles and they'll be excellent at a job nobody will ever ask them to do.
