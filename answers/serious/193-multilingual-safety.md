---
id: "193"
slug: multilingual-safety
style: serious
category: translation
difficulty: advanced
question: "Why is model safety weaker in some languages than others?"
tags: [multilingual-safety, jailbreak, refusal-rates, moderation, red-teaming, coverage]
---

# Safety does not transfer across languages

A model's refusal behaviour is trained, and it is trained overwhelmingly in English. The capability
to *understand* the request generalises across languages far better than the trained behaviour of
*declining* it does. That gap is a reliable, reproducible vulnerability.

```
   harmful request in English      ─► refused
   the same request in a
   low-resource language           ─► answered

   both were understood. Only one was covered by safety training.
```

This is the same structural failure as question 139's image channel: **an input path the alignment
data did not cover**. Multilingual jailbreaking has been demonstrated repeatedly, and the pattern is
consistent — the fewer safety examples in a language, the higher the compliance rate.

## Why it happens

* **Preference and safety data is English-dominated**, often by an order of magnitude or more.
* **Translated safety data is thin.** Machine-translating English refusal data helps and imports
  its own problems: translationese (question 170), and harm categories that do not map cleanly
  across cultures.
* **Moderation classifiers are per-language**, and the low-resource ones are the weakest — exactly
  where the model is most compliant, so both layers fail together (question 162's pattern).
* **Harm is locally defined.** What constitutes a slur, a dangerous instruction, or a regulated
  claim differs by jurisdiction and culture. An English-derived taxonomy misses categories that
  matter elsewhere and flags things that are unremarkable.

## The other direction: over-refusal

The mirror failure is under-reported. Models refuse benign requests more often in some languages —
because unfamiliar text looks anomalous, because a word innocuous in one language resembles
something flagged in another, or because the moderation classifier is simply worse. A speaker
experiencing this cannot tell whether the model is broken, being cautious, or judging them, and it
lands as a quality-of-service difference along language lines.

**Both directions must be measured**, per language, or you will fix one and worsen the other
(question 167's lesson).

## What to actually do

* **Measure refusal rates per language**, on a parallel set — the same requests, translated by
  humans, harmful and benign. The spread across languages *is* your finding, and it is usually
  large.
* **Red-team in the target languages, with native speakers.** English red-teaming does not transfer,
  for the same reason English safety training does not.
* **Include multilingual examples in safety training**, not only translated ones — locally authored
  where possible, because the categories differ.
* **Run moderation on the source language**, not on a translation into English (question 178's
  laundering problem).
* **Report coverage honestly.** If safety was validated in five languages and the product serves
  fifty, say so. This is question 185's tiering argument applied to safety, and it matters more
  here: a user in an unvalidated language has no way to know the guardrails are thinner.

## What an interviewer digs into next

* Why does capability generalise across languages better than refusal behaviour?
* Why do the model layer and the moderation layer fail together rather than covering each other?
* Why is translated safety data insufficient?
* Why must over-refusal be measured alongside under-refusal?
