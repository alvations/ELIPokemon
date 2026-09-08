---
id: "161"
slug: translation-memory-systems
style: serious
category: translation
difficulty: intermediate
question: "What is a translation memory, and how does it fit alongside MT?"
tags: [translation-memory, fuzzy-match, leverage, cat-tools, retrieval, maintenance]
---

# Translation memory

A translation memory is a database of segment pairs that a human has already approved. Before any
model is invoked, you ask it a simple question: **has this, or something close to it, already been
translated and signed off?**

It predates neural MT by decades, it is the backbone of every professional localisation workflow,
and ML teams building translation products routinely rebuild a worse version of it by accident.

## Matching and leverage

```
   incoming segment: "Click Save to store your changes."

   TM lookup ─┬─ 100%  exact match          ─► reuse verbatim. free, consistent, done.
              ├─  95%  "Click Save to store your settings."   ─► edit one word
              ├─  75%  "Press Save to keep your changes."     ─► useful as a hint
              └─ <70%  ─► not worth showing; it anchors the translator wrongly (q149)
```

**Leverage** is the fraction of a job covered by matches, and it is the number the whole commercial
model is built on: exact matches are usually charged at a small fraction of the full rate, high
fuzzies at a discount, and no-matches at full price. That pricing structure is why TM hygiene is a
business concern and not just an engineering one.

Two mechanisms worth distinguishing: **segment matching** (the lookup above) and **concordance
search** (find every previous occurrence of a phrase, anywhere in the memory, to see how it has been
handled). Translators use the second constantly; automated pipelines usually forget it exists.

## TM, MT and LLMs together

They are not competitors. The sensible arrangement:

| Situation | Use |
| --- | --- |
| Exact match | the TM. It is approved, consistent and free |
| High fuzzy (85%+) | the TM entry, presented for editing |
| Low fuzzy | **feed the fuzzy matches to the LLM as examples** (question 134) |
| No match | MT, with glossary (question 133) and QE gating (question 132) |

That third row is the one modern systems get real gains from: a TM is a **domain-specific retrieval
corpus**, and putting the nearest approved translations into the prompt raises terminology
compliance and style consistency more reliably than fine-tuning does, with no training run.

## Maintenance is the whole game

A TM degrades. It accumulates:

* **Stale entries** — terminology that changed, product names that were rebranded, UI strings for
  screens that no longer exist.
* **Contradictions** — the same source segment with three different approved translations, from
  three projects with different style guides. The lookup returns one arbitrarily.
* **Post-editese** (question 149) — as post-edited output flows back in, the memory drifts toward
  machine phrasing, and future retrieval reinforces it.
* **Context-free segments** — a segment approved in a context that no longer applies.

Practical hygiene: version the TM per product and locale, date entries and prefer recent ones, run
periodic duplicate/conflict reports, and **keep provenance** — who approved this, when, in what
project. A memory without provenance cannot be cleaned, only trusted or abandoned.

## What an interviewer digs into next

* Why is a low fuzzy match sometimes worse than no match at all?
* How would you use a TM with an LLM rather than instead of one?
* What causes a TM to contain contradictory entries, and how do you resolve them?
* Why does provenance matter more than volume in a translation memory?
