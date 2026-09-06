---
id: "131"
slug: document-level-translation
style: serious
category: translation
difficulty: intermediate
question: "Why is sentence-level translation not enough?"
tags: [document-level, discourse, pronouns, formality, consistency, contrapro]
---

# Document-level translation

Sentence-by-sentence translation is the default because training data is sentence-aligned and
metrics are sentence-based. It is also structurally incapable of getting several things right,
because the information needed is **in a different sentence**.

## What needs context, concretely

```
   "The committee published its report. It was criticised immediately."
                                          └─► "it" = the committee? or the report?

   German needs a gendered pronoun: der Ausschuss (masc.) vs der Bericht (masc.) — ambiguous
   French needs: le comité (masc.) vs le rapport (masc.)
   ... and for many noun pairs the genders differ, so the translator MUST choose, and
       a sentence-level system chooses by prior, not by evidence.
```

The recurring cases:

* **Pronoun and gender agreement.** English "it", "they", "you" underspecify what most target
  languages must mark. Also: a speaker's own gender, which many languages mark on verbs and
  adjectives, and which is never in the sentence being translated.
* **Formality / register.** T-V distinction (tu/vous, du/Sie), Japanese and Korean politeness
  levels. Chosen once for a document, not per sentence — a translation that switches between
  formal and informal mid-document is jarring and sometimes offensive.
* **Lexical consistency.** A term translated three different ways across one document. Fine per
  sentence, unacceptable in a manual or contract.
* **Discourse connectives.** "However", "then", "meanwhile" depend on what preceded.
* **Ellipsis.** Languages that drop subjects (Japanese, Chinese, Spanish, Korean) require the
  translator to recover a subject that is only available from earlier context.
* **Named entity and number consistency**, including units and date formats across a document.

## Approaches

| Approach | How | Trade-off |
| --- | --- | --- |
| **Concatenation (k-to-k / k-to-1)** | prepend previous n sentences as context, translate the last | simple, effective, quadratic-ish cost, context dilution |
| **Full-document with an LLM** | translate the whole document in one call | best consistency; length limits, drift, harder to align output |
| **Two-pass** | sentence-level draft, then a document-level consistency edit | practical, keeps alignment, catches terminology |
| **Cache / memory of decisions** | record chosen term and register, enforce on later sentences | deterministic, integrates with translation memory |

Modern LLM translation gets much of this for free simply by having the document in context, which
is the single biggest practical advantage LLMs have over classical NMT for real documents. The
trade is alignment: an LLM given a whole document may merge or split sentences, which breaks
downstream tooling that expects a 1:1 mapping.

## Why you cannot see the improvement in your metrics

This is the crux, and it is why document-level MT was ignored for so long. Corpus BLEU or COMET
over a test set is dominated by sentences where context does not matter. A system that fixes
**every** pronoun in the test set might move the aggregate by a fraction of a point — well inside
noise — while being obviously better to any reader.

The fix is **contrastive test sets**. ContraPro, and its relatives for formality and lexical
choice, present the model with a correct translation and a minimally-different wrong one (the
pronoun swapped), and measure whether it assigns higher probability to the correct one. Accuracy
on that set is a direct, sensitive measure of exactly the capability you added, and it does not
drown in the average.

Also worth measuring: **term consistency rate** (how often a term is translated identically within
a document) and **register consistency** (does formality flip mid-document).

## Practical notes

* Sentence-align carefully. Bad alignment poisons context windows with unrelated text.
* Give the model document metadata when you have it — domain, audience, formality — rather than
  making it infer register from the first sentence.
* Watch for **drift** in long-document LLM translation: quality and terminology adherence often
  degrade past a few thousand tokens.
* Keep a glossary and enforce it (question 133); context alone does not guarantee consistency.

## What an interviewer digs into next

* Give three concrete phenomena that sentence-level MT cannot resolve in principle.
* Why do corpus-level metrics fail to show document-level gains?
* How does a contrastive test set work, and what does it not measure?
* What breaks when an LLM merges sentences during document translation?
