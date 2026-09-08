---
id: "172"
slug: named-entity-translation
style: serious
category: translation
difficulty: intermediate
question: "How should a translation system handle names?"
tags: [named-entities, transliteration, entity-linking, exonyms, consistency, back-transliteration]
---

# Names

"Do not translate names" is wrong, and so is "translate names". The correct behaviour depends on
the kind of name, the language pair, and the convention in the target locale — and getting it wrong
produces errors that readers notice instantly.

## Four different behaviours, one grammatical category

| Kind | Behaviour | Example of the failure |
| --- | --- | --- |
| **Person names** | usually transliterate, never translate | "Mr. Baker" rendered as the occupation |
| **Place names with established exonyms** | use the target's own name | leaving "München" in an English text, or worse, inventing a new form |
| **Organisations** | depends: official name if one exists, else transliterate, sometimes gloss | translating a company name into a description |
| **Products, brands, code** | leave alone (question 133) | a product name helpfully rendered |

The hardest part is that these are decided by **convention in the target language**, not by rule.
Some countries' capitals have exonyms in one language and not another; some organisations have an
official name in five languages and not a sixth.

## Transliteration is not deterministic

```
   Latin → Cyrillic → Latin      "Smith" → "Смит" → "Smit"

   round-tripping loses information: the mapping is many-to-one in one
   direction, so BACK-transliteration cannot recover the original spelling
```

Consequences:

* **Never re-transliterate a name that already exists in the target script.** Look it up. A person
  whose name is already written in Cyrillic should not be transliterated from an English rendering
  of it.
* **Back-transliteration needs a knowledge base**, not an algorithm. Given "Смит", the right answer
  depends on who this person is.
* **Multiple valid systems exist** (question 109) — scholarly, journalistic, national standards —
  and mixing them within one document looks like carelessness.

## Entity linking is the real solution

The robust design does not translate the name at all. It **identifies** it, then looks up the
target-language form:

```
   source text ─► NER ─► entity linking (Wikidata, an internal KB, a client glossary)
                                │
                          ┌─────┴─────┐
                     found            not found
                        │                 │
              use the KB's target    transliterate, flag for review,
              form. Consistent,      and ADD it to the KB so the next
              correct, auditable     occurrence is consistent
```

This is question 133's glossary mechanism specialised to names, and it is why serious localisation
systems maintain an entity list alongside a terminology list. It also gives you **consistency for
free**: the same person is named identically across a 400-page document, which no amount of
per-segment cleverness achieves.

## The failures worth testing for

* **Inconsistency within a document** — the highest-frequency complaint, and cheap to measure.
* **Over-translation**: names with transparent meaning ("White", "Green", "Baker") getting rendered
  as words. Test with a set of these deliberately.
* **Gender agreement on names** in languages that inflect them (Slavic surnames), which needs
  information the text may not contain (question 142).
* **Honorific handling** — titles that must be added, removed or reordered by convention
  (question 141).
* **Segment boundaries splitting a name** — poor segmentation (question 156) rendering half a name
  in each half.

## What an interviewer digs into next

* Why is "never translate names" wrong?
* Why can't back-transliteration be done algorithmically?
* How does entity linking give you consistency that per-segment translation cannot?
* Which names would you put in a deliberate test set, and why?
