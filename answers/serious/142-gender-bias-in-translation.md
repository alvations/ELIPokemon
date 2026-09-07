---
id: "142"
slug: gender-bias-in-translation
style: serious
category: translation
difficulty: intermediate
question: "Why do translation systems get gender wrong, and what can you do about it?"
tags: [gender-bias, winomt, stereotypes, ambiguity, multiple-translations, fairness]
---

# Gender in machine translation

The same structural problem as formality (question 141) — the source underspecifies something the
target must mark — but with a difference that matters: **the model's guess encodes a stereotype,
and shipping it causes harm.**

## Where the ambiguity comes from

```
   Turkish:  "O bir doktor."        ("o" carries no gender)
   English:  "He is a doctor."   ←  the model chose. nothing in the source did.

   Turkish:  "O bir hemşire."
   English:  "She is a nurse."   ←  it chose again, the other way, for the same reason

   The model is reproducing occupational statistics from its training data
   and presenting them as a translation.
```

Three distinct cases, often conflated:

1. **Genuinely ambiguous** — the source truly does not specify. Any single output is a guess.
2. **Resolvable from context** — the information is in an earlier sentence, and a sentence-level
   system cannot see it (question 131). *"The surgeon finished. She removed her gloves."*
3. **Explicitly specified and overridden anyway** — the source marks feminine, the model outputs
   masculine because the occupation prior is stronger. This is a straightforward error and the most
   damning of the three.

There is also **speaker gender**: many languages inflect adjectives and verbs for the speaker's own
gender, which is never in the sentence being translated and often never in the document either.

## Measurement

**WinoMT** is the standard instrument: sentences with two human referents, one stereotypical and
one anti-stereotypical for the occupation, where coreference resolves the gender unambiguously.
Report:

* **Accuracy overall**;
* **the pro-stereotypical / anti-stereotypical gap** — this is the bias measure, and it is the
  number that matters. High overall accuracy with a large gap means the system is right when the
  stereotype agrees and wrong when it does not;
* **masculine/feminine skew** — what fraction of ambiguous cases go masculine.

As always, **aggregate quality metrics will not show any of this.** A system can fix its entire
gender behaviour and move COMET by nothing.

## What to actually do

* **Give it the context.** Document-level translation resolves case 2 outright, and it is the
  cheapest large win available (question 131).
* **Let the caller specify.** If your product knows the speaker's or subject's gender, pass it. This
  is the same argument as passing register in question 141: do not infer what you already know.
* **Return multiple translations when genuinely ambiguous.** Google Translate does this for short
  queries: show both the feminine and masculine rendering and label them. Honest about the
  ambiguity, and it puts the choice with the person who knows the answer.
* **Gender-aware rewriting.** Produce one translation, then re-inflect it to a requested gender with
  a dedicated model. Decouples the problem and scales to more than two options where the language
  supports it.
* **Fine-tune on balanced data**, or counterfactually augment (swap genders in training pairs). Helps
  the prior; does not fix genuine ambiguity, because nothing can.
* **Support neutral forms where the language has them** — and be careful, because in many languages
  the "neutral" form is the masculine, which is not neutral.

## The thing to be clear-eyed about

Case 1 has **no correct single answer**. A system that always picks masculine is not more accurate
than one that picks randomly; it is more consistently biased. The engineering question is therefore
not "how do we guess better" but **"how do we stop guessing"** — by getting context, asking, or
showing both. Systems that quietly guess and present the guess as *the* translation are making an
editorial decision on behalf of a user who does not know it happened.

## What an interviewer digs into next

* Why is the pro/anti-stereotypical gap a better bias measure than overall accuracy?
* Which of the three cases can document context fix, and which can it not?
* Why is "always masculine" not a defensible default?
* How would you surface ambiguity to a user without making the product unusable?
