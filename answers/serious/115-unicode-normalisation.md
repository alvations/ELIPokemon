---
id: "115"
slug: unicode-normalisation
style: serious
category: multilingual
difficulty: core
question: "Why does Unicode normalisation matter in a multilingual pipeline?"
tags: [unicode, nfc, nfkc, confusables, zwj, casefolding]
---

# Unicode normalisation

Two strings can look identical, print identically, and compare unequal. That is not a bug in
your code; it is Unicode working as specified, and every multilingual pipeline has to decide
what it does about it.

## The four normalisation forms

* **NFD / NFC** — canonical decomposition and composition. `é` is either one codepoint
  (U+00E9) or two (`e` + combining acute, U+0065 U+0301). NFC composes, NFD decomposes. They
  are **lossless and round-trippable**.
* **NFKD / NFKC** — compatibility forms. These also fold characters that are "the same" only
  loosely: `ﬁ` → `fi`, `②` → `2`, full-width `Ａ` → `A`, superscripts to digits. **Lossy and not
  reversible.**

```
   "café"  typed on macOS   ►  c a f e ́       (NFD, 5 codepoints)
   "café"  typed on Windows ►  c a f é        (NFC, 4 codepoints)

   len() differs. == is False. A dict lookup misses. A dedup pass keeps both.
   A tokenizer sees different subwords. A search index has two entries.

   NFC(both) ► identical.        NFKC("ﬁle") ► "file"   ← information gone
```

## The rules I would give a team

* **Normalise to NFC at ingestion**, and store the normalised form. NFC is the web's default
  (the W3C recommends it) and is safe.
* **Use NFKC deliberately, never by default.** It is right for a search index key or a fuzzy
  matcher, wrong for text you will show back to a user or train a generative model on — it
  destroys distinctions the writer intended.
* **Do not strip zero-width characters blindly.** ZWJ (U+200D) and ZWNJ (U+200C) are
  *semantically required* in Devanagari, Persian, Kannada and emoji sequences. The
  strip-invisible-characters rule people copy from an English codebase corrupts those scripts.
* **Casefolding is locale-dependent.** Turkish `I`/`ı` and `İ`/`i` are the standard example:
  naive `lower()` produces the wrong letter, which changes the word. Use case folding, and know
  the locale.
* **Confusables are a security matter, not an aesthetic one.** Cyrillic `а` (U+0430) and Latin
  `a` (U+0061) render the same. This is used for domain spoofing and, in an LLM context, to slip
  strings past filters and pattern matchers (question 059). Unicode's TR39 defines skeleton
  mapping for confusable detection.

## Where it shows up in ML specifically

* **Deduplication** silently under-counts if half your corpus is NFD, so near-duplicate documents
  survive into training.
* **Tokenizer training and inference must use the same normaliser.** SentencePiece bakes a
  normalisation rule into the model file precisely so this cannot drift.
* **Evaluation.** A model output that differs from the reference only in composition scores as
  wrong under exact match. Normalise both sides before scoring, and say that you did.
* **Retrieval.** Query and index must be normalised the same way, or accented-language recall
  quietly collapses.

## What an interviewer digs into next

* When is NFKC the right choice and when is it destructive?
* Why is stripping zero-width characters dangerous?
* How would you dedup a corpus that mixes NFC and NFD?
* What is a homoglyph attack, and where would it bite in an LLM pipeline?
