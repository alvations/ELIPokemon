---
id: "101"
slug: cross-lingual-transfer
style: serious
category: multilingual
difficulty: core
question: "What is cross-lingual transfer, and why does fine-tuning in one language help another?"
tags: [cross-lingual, zero-shot, xlm-r, transfer, xtreme]
---

# Cross-lingual transfer

Fine-tune a multilingual encoder on English question answering, evaluate it on Swahili, and it
works — not as well as English, but far above chance, having seen zero Swahili labels. That is
**zero-shot cross-lingual transfer**. The task knowledge and the language knowledge live in
different places: pretraining on many languages builds a partly shared representation, and task
fine-tuning teaches a decision rule on top of it that is largely language-agnostic.

## Why it happens

The early explanation was shared subword vocabulary — "anchor" tokens like numerals, names and
loanwords that appear identically in both languages.
[Pires et al. (2019)](https://arxiv.org/abs/1906.01502) tested that and found transfer survives
even between languages with **no script overlap**, so
lexical anchors are not the mechanism. [Artetxe et al. (2020)](https://arxiv.org/abs/1910.11856)
went further: freeze a trained English model, learn only new embeddings for the target language,
and transfer still works. The task-solving machinery in the upper layers is genuinely shared;
the language-specific part is mostly at the bottom.

```
        ┌──────────────────────────────────────────────────────┐
        │  TASK HEAD          trained on English labels only   │
        ├──────────────────────────────────────────────────────┤
        │  UPPER LAYERS       abstract, largely language-neutral│  ← transfers
        │  MIDDLE LAYERS      syntax, roles, alignment         │  ← transfers, noisily
        │  LOWER LAYERS       script, morphology, subwords     │  ← language-specific
        ├──────────────────────────────────────────────────────┤
        │  EMBEDDINGS         shared multilingual vocabulary   │
        └──────────────────────────────────────────────────────┘
             English in ──────► same pipe ──────► Swahili in
```

## What predicts how well it transfers

* **Typological distance** — word order, morphology, script. Transfer from English to German
  beats English to Japanese by a wide margin.
* **Pretraining data volume for the target language.** The single strongest predictor.
* **Task type.** Sentence classification transfers well; token-level tasks (parsing, NER) and
  generation transfer far worse, because they depend on the language-specific lower layers.

[XTREME](https://arxiv.org/abs/2003.11080) (Hu et al., 2020) is the standard measurement, and its
headline finding is a large and persistent English-to-rest gap on every task.

## The three recipes

| Recipe | What you do | Cost | Typical quality |
| --- | --- | --- | --- |
| Zero-shot | Fine-tune on English, run on target | free | baseline |
| Translate-train | MT the training set, fine-tune on that | one MT pass | usually better |
| Translate-test | MT the input at inference time | MT per request | good, slow, lossy |

Translate-train usually wins in practice and is under-used, because the noise MT introduces into
training labels costs less than the domain shift zero-shot suffers. Translate-test inherits every
MT error at serving time and doubles latency.

## Caveats worth stating

* Transfer gets **worse as you add languages** to the pretraining mix at fixed capacity
  (question 103).
* A few hundred target-language examples usually beat any zero-shot recipe — few-shot is a real
  option, not a consolation prize.
* Reported zero-shot numbers are often on **translated** test sets, which are easier than native
  ones (question 188). The gap in the wild is bigger than the gap on paper.

## What an interviewer digs into next

* If shared vocabulary is not the mechanism, what is?
* Why do token-level tasks transfer worse than sentence-level ones?
* When would you pay for translate-train over zero-shot, and how would you decide?
* How does the source language choice affect transfer — is English always the best pivot?
