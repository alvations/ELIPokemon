---
id: "114"
slug: word-segmentation-no-spaces
style: serious
category: multilingual
difficulty: intermediate
question: "How do you handle languages that do not put spaces between words?"
tags: [segmentation, chinese, thai, sacrebleu, tokenization, evaluation]
---

# Languages without whitespace

Chinese, Japanese, Thai, Khmer, Lao, Burmese and Tibetan do not separate words with spaces.
Classical NLP pipelines assumed whitespace pre-tokenisation, so each of these languages needed a
dedicated segmenter — Jieba or Stanford Segmenter for Chinese, MeCab or Juman for Japanese,
dictionary-plus-CRF systems for Thai.

Two things follow, and the second is the one people get wrong.

## 1. For modelling, the problem mostly dissolved

[SentencePiece](https://arxiv.org/abs/1808.06226) treats input as a raw Unicode stream and
learns subwords directly, whitespace included as a marker character. No language-specific
pre-tokenisation, no segmenter dependency, and — importantly — the process is reversible, so you
can detokenise exactly. Modern models simply do this. The old segmenters remain useful for
linguistic annotation and for search indexing, not for feeding a transformer.

It is also worth questioning the premise: "word" is not a well-defined universal. Chinese
segmentation standards disagree with each other; the Penn Chinese Treebank and the Peking
University standard produce different, both-defensible segmentations of the same sentence.
Human agreement on Chinese word boundaries is well below what people assume.

## 2. For evaluation, the problem is very much alive

Metrics that count word n-grams need words. If your metric segments the text, **the metric's
score depends on the segmenter**, and comparing two papers that used different segmenters is
meaningless.

```
   系统翻译得很好
   ├─ segmenter A ► 系统 | 翻译 | 得 | 很好      4 tokens
   ├─ segmenter B ► 系统 | 翻译 | 得很 | 好      4 tokens, different
   └─ characters  ► 系 统 翻 译 得 很 好          7, and unambiguous

   BLEU computed over A and over B are DIFFERENT NUMBERS
   for the same translation. Neither is wrong. They are not comparable.
```

This is why [sacreBLEU](https://arxiv.org/abs/1804.08771) (Post, 2018) exists: it pins the
tokenisation to a named, versioned scheme and prints a signature string with the score, so a
number is reproducible. For Chinese it offers `tok:zh`; for Japanese `tok:ja-mecab`; and
character-level metrics such as chrF (question 139) avoid the question entirely, which is one
reason chrF has become the recommended default for these languages.

## Practical checklist

* **Do not pre-segment before a subword tokenizer.** You are throwing away information and
  making detokenisation lossy.
* **Report the tokenisation signature with every MT score**, or use chrF.
* **Chunking for RAG needs care** (question 042): splitting "on whitespace" produces one giant
  chunk for a Thai document, and splitting on characters cuts mid-word. Split on punctuation and
  line structure, or use a model-aware splitter.
* **Length heuristics break.** Word-count limits, "average words per sentence" filters and
  truncation rules calibrated on English silently do something else here.
* **Display and line-breaking are separate problems** with their own standards (UAX #14) that
  matter as soon as you render output.

## What an interviewer digs into next

* Why did SentencePiece make segmenters unnecessary for modelling but not for evaluation?
* Two papers report BLEU on the same Chinese test set with different numbers. What do you ask?
* How would you chunk a Thai document for retrieval?
* Is "word" a useful unit for Chinese at all?
