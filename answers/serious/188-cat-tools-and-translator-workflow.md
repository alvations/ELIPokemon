---
id: "188"
slug: cat-tools-and-translator-workflow
style: serious
category: translation
difficulty: intermediate
question: "What does a professional translator's working environment look like, and why should an ML engineer care?"
tags: [cat-tools, xliff, segmentation, qa-checks, workflow, integration]
---

# The software your model's output lands in

ML teams build translation systems and hand them to translators through an API. Translators do not
work in an API. They work in a **CAT tool** — a computer-aided translation environment — and
understanding it changes what you build.

## The screen

```
   ┌──────────────────────────┬──────────────────────────┐
   │ SOURCE segment           │ TARGET segment (editable)│
   ├──────────────────────────┼──────────────────────────┤
   │ Click Save to store...   │ [ translator types here ]│
   └──────────────────────────┴──────────────────────────┘
   ┌───────────────────────────────────────────────────────┐
   │ TM matches:   98%  "Click Save to store your settings"│  ← question 161
   │ MT suggestion:     "Klicken Sie auf Speichern, um..." │  ← your model
   │ Glossary:     Save → Speichern (approved)             │  ← question 133
   │ Concordance:  12 previous uses of "store"             │
   │ QA warnings:  ⚠ placeholder {count} missing           │  ← question 156
   └───────────────────────────────────────────────────────┘
```

Everything is **segment-by-segment**, and every resource is on screen simultaneously. Your MT output
is **one suggestion among several**, competing with an approved TM match that is free and
guaranteed consistent.

## What this implies for what you build

* **Your output must be a candidate, not an answer.** It will be edited. Optimise for
  *editability* — a translation that is 90% right and easy to fix beats one that is 95% right and
  must be rewritten to fix. This is not what your metric measures (question 149).
* **Segment-level API, with document context available.** The tool works in segments; your model
  wants the document (question 131). Accept a segment plus its surrounding segments, and return
  aligned to the segment. Returning merged or split output breaks the tool.
* **Return metadata, not just text.** Confidence (question 132), which glossary terms you applied,
  whether you used a TM match. The tool can display it; the translator uses it to decide how hard
  to look.
* **Respect the tags.** The tool passes inline formatting as tags; return them intact and balanced
  (question 156). This single requirement causes more integration failures than model quality ever
  will.
* **Support the standard formats.** XLIFF for the bilingual file, TMX for memories, TBX for
  termbases. Inventing a JSON schema means nobody can use your system inside their existing process.

## The QA checks the tool already runs

Automatic checks fire before delivery: missing or altered placeholders, tag mismatches, numbers that
differ between source and target, terminology violations against the termbase, untranslated
segments, inconsistent translations of identical sources, length limit breaches, double spaces.

These are the **mechanical integrity checks** of questions 156 and 133 — and the industry has run
them as a blocking gate for two decades. An ML pipeline that does not run them is not being
innovative; it is missing a standard control.

## Why engineers should care

The translator's edits are your highest-quality training signal (question 149), the TM is your best
retrieval corpus (question 161), and the termbase is your glossary (question 133). All three already
exist inside the tool. A team that integrates with the workflow gets them; a team that bypasses it
rebuilds all three, worse, and wonders why adoption is poor.

## What an interviewer digs into next

* Why is editability a different objective from accuracy?
* What breaks when a model merges or splits segments?
* Why are XLIFF/TMX/TBX worth supporting rather than a custom schema?
* Which three assets does integrating with a CAT tool give you for free?
