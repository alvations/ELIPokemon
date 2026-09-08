---
id: "177"
slug: multilingual-rag
style: serious
category: translation
difficulty: advanced
question: "How do you build retrieval-augmented generation across languages?"
tags: [multilingual-rag, cross-lingual-retrieval, query-translation, citation, language-control]
---

# RAG when the query and the documents are in different languages

Standard RAG (question 044) assumes one language. Real corpora are multilingual: a support knowledge
base in English, a policy document in German, a regulation in Japanese, and a user asking in
Portuguese. Every stage of the pipeline needs a language decision, and getting one wrong produces a
confident answer from the wrong document.

## Four architectures

```
   1. TRANSLATE THE QUERY      query ─► MT ─► retrieve in doc language ─► answer
      + reuses monolingual retrieval    − MT errors become retrieval errors,
                                          and you must know which language to translate INTO

   2. TRANSLATE THE CORPUS     docs ─► MT ─► index in one language
      + one index, simple               − expensive, stale, and errors are baked in permanently

   3. CROSS-LINGUAL EMBEDDINGS query and docs in one shared space (question 168)
      + no MT anywhere, elegant         − quality varies wildly by language pair

   4. MULTI-QUERY FAN-OUT      translate the query into each corpus language, retrieve
                               in each, merge
      + best recall                     − N times the cost, and merging scores across
                                          languages is not straightforward
```

In practice 3 with 4 as a fallback works well: retrieve cross-lingually, and fan out when the
cross-lingual retriever's confidence is low or the corpus language is one it handles poorly.

## The problems that only appear in the multilingual case

* **Score comparability across languages.** Retrieval scores from different language pairs are not
  on the same scale (question 168's calibration issue). Merging raw scores systematically favours
  whichever pair the encoder handles best — usually English. Normalise per language before merging.
* **Language control on output.** The user asked in Portuguese; the evidence is German; the model
  may answer in either, or in English, or drift mid-answer (question 136). State the output language
  explicitly and **verify it with LID** before returning.
* **Citation across languages.** If you cite a German passage in a Portuguese answer, the user
  cannot check it. Show the original *and* a translation of the cited span, marked as machine
  translated. An uncheckable citation is decoration.
* **Terminology consistency** between the retrieved documents and the generated answer
  (question 133) — the answer should use the target language's established term, not a fresh
  rendering of the source's.
* **Conflicting sources across locales.** The English and German versions of a policy may genuinely
  differ, because they were localised for different jurisdictions (question 150). This is not a
  retrieval bug to be resolved — it is information, and the right behaviour is to surface both with
  their locales.

## Evaluation

* **Retrieval recall per language pair**, never pooled. The aggregate is dominated by whichever
  language has the most queries.
* **Answer language accuracy** — the fraction of answers in the requested language. This should be
  ~100% and frequently is not.
* **Faithfulness to a source in another language**, which needs a bilingual evaluator or a
  translated reference; an LLM judge is weakest for exactly the low-resource pairs where you most
  need it (question 132).
* **The English-query control.** Ask the same question in English and in the target language and
  compare. A large gap tells you the pipeline is English-centric, which is the default outcome.

## What an interviewer digs into next

* Why does merging raw retrieval scores across languages favour English?
* Why is a citation in a language the user cannot read worse than no citation?
* When are conflicting cross-locale documents information rather than a bug?
* What does the English-query control reveal?
