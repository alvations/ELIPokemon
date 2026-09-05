---
id: "105"
slug: shared-multilingual-vocabulary
style: serious
category: multilingual
difficulty: intermediate
question: "How do you build a subword vocabulary shared across many languages?"
tags: [sentencepiece, vocabulary, byte-fallback, unigram-lm, character-coverage]
---

# Building a shared multilingual vocabulary

One vocabulary has to cover every script you intend to serve, leave enough merges per language
that words do not shatter into characters, and stay small enough that the embedding and output
matrices do not eat the parameter budget. Those three pull against each other, and the whole
design is choosing where to lose.

## The mechanics

[SentencePiece](https://arxiv.org/abs/1808.06226) (Kudo & Richardson, 2018) is the standard
implementation because it operates on raw Unicode with no language-specific pre-tokenisation —
essential when some of your languages have no whitespace word boundaries (question 114). Two
knobs matter most:

* **Algorithm.** BPE merges greedily by frequency; **unigram LM**
  ([Kudo, 2018](https://arxiv.org/abs/1804.10959)) prunes a large candidate set by likelihood.
  Unigram tends to produce more morphologically plausible pieces and is the usual multilingual
  choice; [Bostrom & Durrett (2020)](https://arxiv.org/abs/2004.03720) found it also trains
  better downstream models.
* **Character coverage.** Set to 1.0 every character in the corpus gets an entry, which for CJK
  means thousands of slots. Set to 0.9995 and the rare tail falls back to bytes. **Byte fallback
  is the safety net that stops unseen characters becoming `<unk>`** — and it is expensive, at up
  to four tokens per character.

```
   VOCAB BUDGET, 250k slots
   ┌───────────────────────────────────────────────────────────────┐
   │ ▓▓▓ byte + alphabet floor    ~ 5k   non-negotiable            │
   │ ▓▓▓▓▓▓▓▓▓ CJK characters     ~ 25k  before a single word merge│
   │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ merges  ~220k  divided among languages   │
   └───────────────────────────────────────────────────────────────┘
      the fight is entirely over that last band
```

## Sampling for the tokenizer is its own decision

Train the tokenizer on the natural corpus distribution and low-resource languages get almost no
merges; their words fragment and their fertility explodes (question 102). Standard practice is
to train the tokenizer on a **flatter** distribution than the model — a lower temperature
exponent — because vocabulary slots are cheap insurance compared with the downstream cost of
over-segmentation. [Zheng et al. (2021)](https://arxiv.org/abs/2109.07306) go further and
allocate capacity per language explicitly, choosing per-language vocabulary sizes to equalise a
cost function rather than letting frequency decide.

## Sharing: the benefit and the fight

Shared pieces across related languages are genuinely useful — a common morpheme learned from
Spanish is reused for Portuguese, and shared representations are part of why cross-lingual
transfer works. But the vocabulary is also a **zero-sum resource**: every merge granted to
Finnish compounds is a merge not granted to Thai. Adding a language never comes free.

Two escape hatches:

* **Vocabulary expansion after the fact** — add new pieces for a target language and continue
  pretraining, initialising new embeddings from the average of their old sub-pieces. Cheap and
  effective, and the standard way to adapt an existing model to a new language.
* **Give up on merges entirely** — byte or character models (question 112), which trade sequence
  length for perfect script neutrality.

## Diagnostics worth running before you commit

* **Fertility** (tokens per word) per language, on a native-text sample, not a translated one.
* **Proportion of tokens produced by byte fallback**, per script.
* **Unseen-character rate** on held-out text — a script with no coverage will be invisible in
  aggregate loss.

## What an interviewer digs into next

* Why train the tokenizer on a different distribution than the model?
* What does character coverage of 0.9995 actually discard, and who does it hurt?
* How would you add a new language to an existing model's vocabulary?
* What is the parameter cost of a 250k vocabulary at 1B parameters, and does it change the answer?
