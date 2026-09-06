---
id: "130"
slug: low-resource-translation
style: serious
category: translation
difficulty: advanced
question: "How do you translate a language with almost no parallel data?"
tags: [low-resource, back-translation, transfer, pivot, bitext-mining, flores]
---

# Translating a language with almost no parallel data

Most of the world's languages have a few thousand parallel sentences at best, and many have a Bible
translation and nothing else. Every technique below is a way of manufacturing supervision you do
not have.

## 1. Transfer from a related language

The highest-leverage move. Train on a high-resource relative and adapt: Spanish to Galician,
Hindi to Bhojpuri, Indonesian to Malay, Turkish to Azerbaijani. Shared vocabulary, shared
morphology and shared word order mean the model starts far from random.

This is why multilingual models beat bilingual ones in the low-resource regime even though they
are worse in the high-resource one (question 103). **Script matters as much as family**
(question 106): a related language written in a different script transfers much less, and
transliterating into a shared script (question 109) can recover a surprising amount.

## 2. Back-translation

The workhorse. You almost always have **monolingual** text in the low-resource language, even when
you have no parallel data.

```
   have:  a weak X→Y system, and a lot of monolingual Y text

   step 1   monolingual Y  ──[ Y→X system ]──►  synthetic X
   step 2   train X→Y on   ( synthetic X , REAL Y )
                              ▲                ▲
                     noisy INPUT side    clean TARGET side  ← this is why it works
   step 3   the improved X→Y system now makes better synthetic data. iterate.
```

The asymmetry is the whole trick: errors land on the *source* side, where the model is only
learning to be robust, while the target side — what it learns to produce — is genuine human text.
Forward-translation (translating your source monolingual data) puts machine text on the target
side and teaches the model to imitate its own mistakes; it is much weaker and needs careful
filtering.

Practical notes: sample rather than beam-decode the synthetic source (more diverse, works better),
tag synthetic data so the model can distinguish it, and keep the real-to-synthetic ratio roughly
balanced rather than drowning real data.

## 3. Mine parallel data that already exists

Enormous amounts of bitext are sitting in comparable corpora — Wikipedia, news sites, government
publications, religious texts. **Bitext mining** embeds sentences from both sides with a
multilingual sentence encoder (LASER, LaBSE, SONAR) and takes nearest neighbours above a margin
threshold. This is how CCMatrix, WikiMatrix and NLLB's data were built.

Two cautions: the mined pairs are only as good as the encoder's alignment for that language, which
is worst exactly where you need it most; and mined data is noisy, so filter by margin score,
length ratio and language identification (question 108).

## 4. Pivot

Translate X → English → Y when X-Y has no data but both pair with English. Cheap and always
available; it compounds errors, loses information English does not encode (honorifics, evidentiality,
gender agreement), and doubles latency. Direct multilingual models beat pivoting when there is any
direct data at all, which is why NLLB and similar systems emphasise non-English-centric pairs.

## 5. Everything else

* **Adapters / LoRA per language** (questions 110, 025) — add capacity for the new language without
  disturbing the rest.
* **Vocabulary extension** — the base tokenizer may shred the language into bytes (questions 102,
  112). Extending the vocabulary and initialising new embeddings sensibly is often a bigger win
  than any modelling change.
* **Lexicon and grammar injection.** For genuinely tiny data, a dictionary and a grammar sketch in
  the prompt of a strong LLM can outperform a trained system — the "MTOB" style result.

## Evaluating when you cannot evaluate

This is the hardest part and it gets skipped. FLORES-200 gives you a test set for many languages,
but it is a single domain (Wikipedia-style prose), it is in web crawls, and a good FLORES score
does not mean the system is usable for the community's actual needs.

**Involve speakers.** A system that scores well and produces text no fluent speaker would write is
common, and no automatic metric will tell you. Budget for human evaluation from the start, and ask
what the community actually wants translated — it is often not news articles.

## What an interviewer digs into next

* Why does back-translation put the noise on the source side?
* When does transferring from a related language fail?
* What are the failure modes of mined bitext, and where are they worst?
* Why is a good FLORES score weak evidence of usability?
