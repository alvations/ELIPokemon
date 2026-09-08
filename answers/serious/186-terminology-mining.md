---
id: "186"
slug: terminology-mining
style: serious
category: translation
difficulty: intermediate
question: "How do you build a bilingual glossary without writing it by hand?"
tags: [term-extraction, bilingual-alignment, validation, glossary-maintenance, precision]
---

# Building the glossary you were told to just have

Question 133 assumes a glossary exists. Usually one does not, or it is a spreadsheet somebody
maintained until 2019. Building it from your own content is a solvable problem with one hard
constraint: **a wrong glossary entry is worse than a missing one**, because it gets *enforced*.

## The pipeline

```
   1. MONOLINGUAL TERM EXTRACTION (source side)
        candidates by: POS patterns (noun phrases), corpus statistics
        (termhood: frequent here, rare in general text), plus
        domain-specific patterns (part numbers, drug names)

   2. BILINGUAL ALIGNMENT
        for each source term, find its target counterpart in aligned segments
        — word alignment, embedding similarity, or an LLM asked directly

   3. FILTER
        frequency threshold, alignment confidence, consistency across occurrences

   4. HUMAN VALIDATION            ← the step nobody can skip
        an expert accepts, rejects or corrects. This is the deliverable.

   5. MAINTENANCE
        versioned, dated, owned
```

## Where each stage fails

* **Extraction returns collocations, not terms.** "Please click", "in accordance with". Frequency
  alone finds boilerplate. Termhood scoring — frequent in *this* corpus relative to a general one —
  is what separates a term from a common phrase.
* **Alignment is systematically wrong on the interesting cases.** A term rendered as several words,
  a term rendered as a *different* part of speech, a term correctly left untranslated. These are
  exactly the entries you most want, and they are the ones alignment misses.
* **Inconsistency in the source data becomes a coin flip.** If your corpus renders the term three
  ways (question 161), the miner picks the most frequent — which may be the one your style guide
  bans.
* **Over-extraction is the default failure.** A 5,000-entry glossary of which 1,200 are wrong is
  worse than 300 correct ones, because question 133's enforcement machinery will faithfully impose
  every error.

**So tune for precision, not recall.** Set a high confidence threshold, produce fewer candidates,
and put a person in front of them.

## Making validation affordable

The bottleneck is expert time, so spend it well:

* **Rank by impact**: frequency in real traffic × risk of the domain. Validating the 200 most-used
  terms covers most of the benefit.
* **Show context**: three real sentences with the candidate in place. Validating a bare word pair is
  guesswork even for an expert.
* **Present alternatives** found in the corpus, so validation is a *choice* rather than a
  yes/no on one option.
* **Capture the rejections too** — a do-not-use list is as valuable as an approved list
  (question 133).

## Maintenance is where glossaries die

Every entry needs an owner, a date and a status. Terms are added when products change, deprecated
when they are renamed, and the glossary must be versioned alongside the content so a translation can
be traced to the rules that were in force when it was made. A glossary without provenance decays
into the same untrustworthy state as an unmaintained translation memory (question 161).

## What an interviewer digs into next

* Why does frequency alone find boilerplate rather than terms?
* Which entries does automatic alignment systematically miss, and why are those the valuable ones?
* Why tune for precision rather than recall here specifically?
* Why is a rejected-terms list worth keeping?
