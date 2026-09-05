---
id: "108"
slug: language-identification
style: serious
category: multilingual
difficulty: core
question: "How does language identification work, and where does it fail?"
tags: [lid, fasttext, corpus-quality, precision, glotlid]
---

# Language identification

LID is text classification over character n-grams. The classic systems — `langid.py`, CLD2/CLD3,
fastText's `lid.176` — embed character n-grams and run a linear or shallow classifier, which is
fast enough to label a whole crawl. Recent releases push coverage far wider: NLLB's LID and
[GlotLID](https://arxiv.org/abs/2310.16248) cover 200 and 1600+ labels respectively.

It looks solved because accuracy on clean, long, monolingual, high-resource text is above 99%.
Every one of those four adjectives is doing work.

## Where it fails

```
  ┌─ SHORT TEXT ──────────────────────────────────────────────────┐
  │ "ok"  "haha"  "Barcelona 2-1"  — a query or a chat line has   │
  │ almost no n-gram evidence. Accuracy falls off a cliff below   │
  │ ~20 characters, and most user text is below 20 characters.    │
  ├─ CLOSELY RELATED LANGUAGES ───────────────────────────────────┤
  │ Bosnian / Croatian / Serbian-in-Latin. Indonesian / Malay.    │
  │ Hindi / Marathi. Danish / Norwegian Bokmål. Sometimes there   │
  │ is genuinely no signal in a given sentence.                   │
  ├─ ROMANISED AND CODE-SWITCHED TEXT ────────────────────────────┤
  │ Romanised Hindi looks like nothing the classifier knows;      │
  │ mixed-language sentences have no single right answer at all.  │
  ├─ CLASS IMBALANCE ─────────────────────────────────────────────┤
  │ 0.1% of English leaking into a low-resource bucket that has   │
  │ 0.001% true volume can be MOST of that bucket's content.      │
  └───────────────────────────────────────────────────────────────┘
```

The last one is the failure that matters most for corpus building, and it is a precision/recall
argument. [Kreutzer et al. (2022)](https://arxiv.org/abs/2103.12028), auditing major multilingual
corpora by hand, found several low-resource subsets where under half the sentences were in the
labelled language — filled with English, machine-translated boilerplate, pornographic spam, or
Bible verses. Downstream, models trained on that data inherit it, and evaluation cannot see it
because the evaluators do not speak the language either.

## Design guidance

* **Two stages: script, then language.** Script detection is near-perfect and eliminates most of
  the label space cheaply. It also forces you to name the language/script pair properly
  (question 106).
* **Optimise for precision, not accuracy, when you are building a corpus.** Discarding good
  sentences is recoverable; poisoning a low-resource corpus is not.
* **Use thresholds and abstain.** A confidence floor plus an `und` (undetermined) bucket is
  worth more than forcing every line into a label.
* **Report macro-F1 per language on native text.** Aggregate accuracy is dominated by English
  and will look excellent while the tail is broken.
* **Do not filter code-switched text away** (question 107) — keep the ambiguous, tag it as such.
* **Audit by hand.** Sample 100 lines per language and have a speaker look. There is no
  substitute, and it is how every one of these problems was actually found.

## What an interviewer digs into next

* Why does precision matter more than recall when building a pretraining corpus?
* Why is a two-stage script-then-language design better than one flat classifier?
* How would you evaluate LID for a language with no clean test set?
* What do you do with a sentence that genuinely has no single language?
