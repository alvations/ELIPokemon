---
id: "179"
slug: controlled-language-authoring
style: serious
category: translation
difficulty: intermediate
question: "How does changing how the source is written improve translation?"
tags: [controlled-language, source-authoring, ambiguity, simplified-technical-english, upstream]
---

# Fixing the source instead of the translator

Every other technique in this dataset improves the translation. This one improves **the thing being
translated**, and it is consistently the highest-leverage intervention available — and the one
almost nobody has authority to make.

## Why the source is usually the problem

Most translation errors originate in the source. Ambiguity that an English reader resolves
effortlessly must be **resolved by the translator**, and if the translator guesses wrong the error is
downstream of a decision the author never knew they were making.

```
   "Check the cable connecting the sensor to the display unit that is damaged."
                                                    ▲
      which is damaged — the display unit, or the cable? English lets you
      leave this open. Most target languages force a choice via agreement,
      relative-clause structure or word order. The translator must decide.

   author's fix:  "If the cable is damaged, check the cable connecting the
                   sensor to the display unit."
```

One rewrite, and every downstream language is now correct, permanently, in every future version of
the document.

## What controlled language actually specifies

Formalised versions — ASD Simplified Technical English being the best-known, developed for
aerospace maintenance documentation — typically constrain:

* **One meaning per word**, from an approved lexicon. "Follow" means "come after", never "obey".
* **One part of speech per word.** No "test the test".
* **Sentence length limits** (often 20-25 words for instructions).
* **Active voice, imperative mood** for procedures.
* **No omitted relative pronouns**, no dangling participles, no stacked noun phrases ("front brake
  assembly retaining bolt torque specification").
* **Consistent terminology**, enforced against the same glossary the translators use
  (question 133).

The measured effects are real: fewer translation errors, higher TM leverage (question 161) because
consistent sentences match previous ones, lower post-editing effort (question 149), and — often
overlooked — **better comprehension for readers of the source who are not native speakers**, who
are frequently the majority.

## Where it applies and where it does not

Controlled language suits **procedural and technical content**: instructions, safety warnings,
maintenance, UI strings, support articles. It is actively harmful for marketing, narrative and
anything where voice is the product (question 149's transcreation point).

## The organisational reality

This is why it does not happen. The cost falls on the authoring team; the benefit accrues to
localisation, which is usually a different department with a different budget. Adopting it requires
someone senior enough to move cost from one column to another, plus author training, plus a checker
integrated into the authoring tool — because a style rule that is not mechanically enforced decays
within two releases.

**The pragmatic version**, if you cannot get the mandate: run an automated source-quality check
before translation and flag ambiguous, overlong or inconsistent segments back to the author for the
worst 5%. Most of the benefit, a fraction of the political cost.

## What an interviewer digs into next

* Why is fixing the source higher-leverage than fixing the translator?
* Give an ambiguity English tolerates that most target languages cannot.
* Why does controlled language improve TM leverage specifically?
* Why does it usually fail organisationally rather than technically?
