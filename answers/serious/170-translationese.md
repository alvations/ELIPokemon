---
id: "170"
slug: translationese
style: serious
category: translation
difficulty: advanced
question: "What is translationese, and why does it distort MT evaluation?"
tags: [translationese, test-set-direction, source-original, simplification, interference, wmt]
---

# Translationese

Translated text is systematically different from text originally written in the same language.
Not worse — **different**, in measurable, repeatable ways. Translation studies has characterised
these as near-universals:

* **Simplification** — smaller vocabulary, shorter sentences, fewer rare words than original text.
* **Explicitation** — connectives and relationships made explicit that the original left implied.
* **Normalisation** — idiom and unusual phrasing regularised toward conventional forms.
* **Interference** — the source language's structure showing through: word order, cognates,
  punctuation habits.

A classifier can distinguish translated from originally-written text at high accuracy. That fact is
what makes it an evaluation problem rather than a stylistic curiosity.

## Why this breaks test sets

A test set has a **direction of origin**. Half of a WMT test set was written in the source language
and translated to make the reference; the other half was written in the target language and
translated to make the *source*.

```
   SOURCE-ORIGINAL half            TARGET-ORIGINAL half
   ────────────────────            ────────────────────
   source: natural text            source: TRANSLATIONESE (it was translated to get here)
   ref:    translationese          ref:    natural text

   a system evaluated on the second half is being asked to translate
   already-translated text into natural text — an easier, unrepresentative task,
   and one that flatters systems producing translationese-flavoured output.
```

Measured effects are large enough to change conclusions. Scores on the target-original half run
substantially higher, and system *rankings* can flip between halves. This is why WMT moved to
**source-original-only** test sets, and why any evaluation you build yourself should record the
direction of origin of every segment.

**Practical rule:** if you scrape a test set from parallel data, you do not know its direction, and
your numbers are not interpretable. Build test sets from text originally written in the source
language, translated once, by a professional, for this purpose.

## Why it matters for training too

Most parallel corpora are translations, so models are trained predominantly on translationese
targets. Consequences:

* Output inherits the flattened, explicitated register — fluent, slightly foreign, recognisably
  translated.
* **Back-translation makes this worse in one direction and better in another** (question 130): the
  synthetic *source* being translationese is fine; if you accidentally put machine output on the
  *target* side, you are training on translationese-squared.
* Post-edited output fed back into a TM (questions 149, 161) compounds it further. Post-editese and
  translationese stack.

Mitigations: mix in monolingual target-language text for language modelling, prefer
target-original data where you can identify it, and evaluate on human-written text in the target
language rather than only on references.

## The honest caveat

Translationese is not a defect to be eliminated. Translated text is *for* something, and some
explicitation is genuinely helpful to readers. The problem is not that it exists but that it is
**invisible in evaluation** — it makes systems look better than they are, and it accumulates
silently across a pipeline that keeps feeding its own output back in.

## What an interviewer digs into next

* Name three properties of translationese and explain why each arises.
* Why do system rankings flip between the two halves of a test set?
* Why is it safe for back-translation to put translationese on the source side?
* How would you build an evaluation set that avoids this problem?
