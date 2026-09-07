---
id: "133"
slug: terminology-glossary-enforcement
style: serious
category: translation
difficulty: intermediate
question: "How do you make a translation system use the right terminology every time?"
tags: [terminology, glossary, constrained-decoding, do-not-translate, translation-memory]
---

# Terminology and glossary enforcement

For most translation, "a correct rendering" is a set with many members. For terminology it is a set
with exactly one. A drug name, a legal term of art, a product name, a UI string that must match
the button the user is looking at — these are not preferences. A translation that is fluent,
accurate and uses the wrong term is a defect.

## Why the model will not do this on its own

A translation model produces the *most probable* rendering given its training distribution. Your
glossary encodes a decision your organisation made, often against the more common usage. The model
has never seen it and has no reason to prefer it.

Worse, it will be **inconsistent** — the same term rendered three ways across one document
(question 131) — because each occurrence is generated independently and all three are locally
plausible.

## The enforcement mechanisms, weakest to strongest

```
   SOFT ─────────────────────────────────────────────────────────► HARD

   put the glossary       fine-tune on          constrain          replace the term
   in the prompt          in-domain data        decoding           with a placeholder
        │                      │                    │                    │
   easy, ~70-90%        durable, needs        near-100%,          100%, but you must
   compliance,          data, still           breaks              restore inflection
   silently drops       probabilistic         morphology          yourself
   under load
```

* **Prompt injection of relevant glossary entries.** Retrieve only the terms occurring in this
  segment — dumping a 5,000-entry glossary into every prompt costs tokens and dilutes attention.
  This is the default for LLM translation and it is genuinely good, not perfect.
* **Fine-tuning** on data that already uses your terminology. Durable and invisible at inference,
  but it cannot express a term added yesterday.
* **Lexically constrained decoding.** Force the target string to appear: grid beam search, dynamic
  beam allocation, or vectorised constrained beam search. Guarantees the string. Costs beam width
  (constraints multiply the search space) and produces ungrammatical output when the constraint
  fights the sentence.
* **Placeholder substitution.** Mask the term before translation, restore after. Absolute
  guarantee, and it moves the problem: you now own agreement, inflection and word order around a
  token the model could not see.

## The failure everyone hits: morphology

A glossary entry is a lemma. Sentences need inflected forms.

```
   glossary:  "gasket"  ->  "Dichtung"  (German, feminine)

   forced verbatim:  "... mit der Dichtung ..."     ✓ nominative happens to fit
                     "... Austausch des Dichtung"   ✗ needs "der Dichtung" (genitive)

   the constraint was satisfied. the sentence is wrong.
```

For morphologically rich and agglutinative languages (question 113) this is not an edge case, it is
the normal case. Practical answers: store **inflected variants** in the glossary rather than
lemmas; accept a *family* of surface forms as satisfying the constraint; or use soft enforcement
and check compliance afterwards rather than forcing it during decoding.

## Do-not-translate is a separate list

Product names, code identifiers, file paths, placeholders like `{count}`, units, and names that
happen to be common nouns. These must pass through **unchanged**, and the common failure is a model
helpfully translating a brand name or "translating" a variable name into another variable name.
Tag-and-restore is the right mechanism here; there is no upside to letting the model see them.

## Translation memory still matters

Before generating anything, check whether this segment or a close variant has been translated and
approved before. Exact matches are free and guaranteed consistent. Fuzzy matches (high-similarity
previous segments) can be put in the prompt as examples, which raises terminology compliance
without any decoding machinery. This is standard in localisation pipelines and frequently absent
from ML-team-built ones.

## Measuring it

**Term accuracy**: of the glossary terms present in the source, what fraction appear correctly in
the output. Report it separately from COMET — a system can gain a COMET point and lose five points
of term accuracy, and the aggregate metric will call that an improvement.

Also measure **consistency rate** within a document, and keep a targeted test set of segments
containing glossary terms in awkward grammatical positions.

## What an interviewer digs into next

* Why does constrained decoding break morphologically rich languages?
* When would you choose placeholders over constrained decoding?
* Why retrieve glossary entries rather than include the whole glossary?
* Why must term accuracy be reported separately from a quality metric?
