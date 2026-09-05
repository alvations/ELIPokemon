---
id: "106"
slug: script-vs-language
style: serious
category: multilingual
difficulty: core
question: "What is the difference between a script and a language, and why does it matter?"
tags: [script, orthography, digraphia, bcp-47, language-tags]
---

# Script is not language

A **language** is a system of speech and grammar; a **script** is a set of marks used to write
one. The mapping between them is many-to-many, and almost every multilingual bug I have seen
starts with code that assumes it is one-to-one.

* **One language, two scripts.** Serbian is written in both Cyrillic and Latin, officially and
  interchangeably. Punjabi is Gurmukhi in India and Shahmukhi (Perso-Arabic) in Pakistan.
  Kazakh is mid-migration from Cyrillic to Latin.
* **One script, many languages.** Latin serves English, Vietnamese, Turkish and Yoruba, whose
  grammars share nothing. Arabic script serves Arabic, Persian, Urdu, Pashto and Uyghur.
* **One language, several scripts at once.** Japanese interleaves kanji, hiragana, katakana and
  Latin in a single sentence, by design, not by accident.
* **Two languages, one script, mutually intelligible speech.** Hindi and Urdu, in Devanagari and
  Perso-Arabic respectively, are close to a single spoken language with two written traditions.

```
                      LANGUAGE  ──────────────  SCRIPT
                      (grammar, lexicon)        (marks on the page)

        Serbian  ─────────┬────────────────────►  Cyrillic
                          └────────────────────►  Latin
        Hindi    ─────────────────────────────►  Devanagari
        Urdu     ─────────────────────────────►  Perso-Arabic
        English  ─────────┐
        Vietnamese ───────┼────────────────────►  Latin
        Turkish  ─────────┘

        A model can be excellent at Hindi and useless at Hindi typed
        in Latin letters. Same language. Different script. Different task.
```

## Why it matters in practice

* **Tokenizers are allocated by script, not by language.** Coverage, byte fallback and fertility
  are all script-level properties (question 102). A language that switches script switches cost
  bracket overnight.
* **Language identification is really script identification plus a guess** (question 108). LID
  models are far more confident about Cyrillic-vs-Latin than about Serbian-vs-Croatian.
* **Transfer follows script more than you would like.** Shared script gives shared subwords, so
  a model transfers more easily within a script even to an unrelated language — one reason
  romanisation is sometimes worth it (question 109).
* **Romanised text is a separate variety.** Romanised Hindi, Arabizi, and pinyin-typed Chinese
  are how enormous numbers of people actually type, and a model trained on native-script data
  handles them badly.

## Tag your data properly

Use BCP-47, which composes ISO 639 language subtags with ISO 15924 script subtags: `sr-Cyrl`,
`sr-Latn`, `zh-Hans`, `zh-Hant`, `pa-Guru`, `pa-Arab`. A dataset labelled `sr` alone has thrown
away the fact you most need at training and eval time. The convention is to omit the script only
when it is the language's unambiguous default (`en`, not `en-Latn`).

Also normalise before you compare (question 115): identical-looking text can differ in codepoints
through Unicode composition, presentation forms and confusable characters.

## What an interviewer digs into next

* If a model scores well on Hindi, what have you learned about its Urdu ability? About romanised
  Hindi?
* Why do LID systems confuse Serbian and Croatian but never Serbian and Japanese?
* When would you romanise your entire corpus, and what would you lose?
* How would you split train and test for a language with two active scripts?
