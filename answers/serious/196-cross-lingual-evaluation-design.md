---
id: "196"
slug: cross-lingual-evaluation-design
style: serious
category: translation
difficulty: advanced
question: "How do you design an evaluation that is fair across languages?"
tags: [benchmark-design, translated-benchmarks, cultural-validity, native-authoring, reporting]
---

# Building an evaluation that is fair across languages

The default approach — take an English benchmark, translate it, report per-language scores — is
cheap, ubiquitous, and produces numbers that mean less than they appear to. Three separate problems
compound.

## 1. Translated items carry the source's assumptions

```
   an English item:  "How many quarters make $1.75?"

   translated into a language whose currency has no quarters:
        the arithmetic survives; the SITUATION does not.
        The item now tests whether the model knows about US coins.

   an item about legal procedure, school grades, family terms, address formats,
   or measurement conventions has a DIFFERENT CORRECT ANSWER elsewhere (q150)
```

You are no longer measuring the capability. You are measuring familiarity with the source culture,
which correlates with pretraining data in exactly the way that makes the result look like a
capability gap.

## 2. The items are translationese

A translated test set is, by construction, question 170's problem: simpler, more explicit, more
regular than text originally written in that language. Models handle it **better** than real text,
so translated benchmarks tend to **overstate** performance in absolute terms while distorting
comparisons.

## 3. Difficulty does not survive translation

An item calibrated as hard in English may be trivial in a language that marks the distinction
grammatically, or impossible in one that does not. Item difficulty is a property of the
language-item pair, not of the item.

## What a fair design looks like

* **Locally authored items**, written by speakers, about locally relevant content, with locally
  determined correct answers. Expensive, and the only thing that actually measures the capability in
  that language.
* **Both, reported separately.** Translated items give you comparability across languages; native
  items give you validity within one. **The gap between them is itself the finding** —
  it separates "worse at the task" from "unfamiliar with the culture" (question 195).
* **Native speakers validating every item**, including the translated ones, with authority to
  reject items that do not transfer.
* **Report per language, never pooled** (question 185), with sample sizes — small per-language
  samples produce confidence intervals wide enough to swallow most reported differences, and
  those intervals are almost never shown.
* **Document the provenance of every item**: originally authored in which language, translated by
  whom, validated by whom. Without this a reader cannot tell what your number means.

## The uncomfortable economics

Locally authored evaluation costs real money per language, which is why almost nobody does it, which
is why the field's picture of multilingual capability rests largely on translated English
benchmarks. That is worth stating plainly when you report results — including your own.

And when a language has no adequate evaluation, the honest report is **"we cannot currently
measure this"**, not a number from a translated set presented without qualification. Question 185's
tiering argument applies to your evaluation as much as to your model.

## What an interviewer digs into next

* Give an item type whose correct answer changes across locales.
* Why do translated benchmarks overstate absolute performance?
* What does the gap between translated and native items tell you?
* When is "we cannot measure this" the right thing to report?
