---
id: "116"
slug: multilingual-instruction-tuning
style: serious
category: multilingual
difficulty: intermediate
question: "How do you instruction-tune a model to follow instructions in many languages?"
tags: [instruction-tuning, aya, translated-data, preference-data, multilingual]
---

# Multilingual instruction tuning

A pretrained multilingual model has the *knowledge* of a language and none of the *behaviour*.
Instruction tuning supplies the behaviour, and the practical question is how much data you need
per language and where it comes from.

## The encouraging result

Instruction-following transfers across languages far better than most abilities. Tuning on a
handful of languages produces a model that follows instructions in many more —
[Chen et al. (2024)](https://arxiv.org/abs/2309.08958) found that instruction tuning in two to
four languages captured most of the multilingual benefit, and that monolingual English tuning
alone already produced substantial cross-lingual instruction-following.

The reading: instruction tuning is mostly teaching a *format and a stance*, which is
language-agnostic, on top of language competence the pretraining already provided. That is why
it needs thousands of examples rather than billions.

## Where the data comes from, and what each source costs

```
  ┌────────────────────────┬───────────────────────┬──────────────────────────┐
  │ SOURCE                 │ SCALES TO             │ WHAT IT GETS WRONG       │
  ├────────────────────────┼───────────────────────┼──────────────────────────┤
  │ MT of English data     │ every language, today │ translationese, English  │
  │ (Bactrian-X, tr-Alpaca)│                       │ cultural framing, MT     │
  │                        │                       │ errors baked into labels │
  ├────────────────────────┼───────────────────────┼──────────────────────────┤
  │ Templated NLP datasets │ wherever the datasets │ unnatural instructions,  │
  │ (xP3-style)            │ already exist         │ narrow task distribution │
  ├────────────────────────┼───────────────────────┼──────────────────────────┤
  │ Model-generated        │ cheaply, any language │ inherits the teacher's   │
  │ (self-instruct)        │                       │ weaknesses in that       │
  │                        │                       │ language, and its accent │
  ├────────────────────────┼───────────────────────┼──────────────────────────┤
  │ Human-written, native  │ slowly, expensively   │ nothing — this is the    │
  │ (Aya)                  │                       │ gold standard            │
  └────────────────────────┴───────────────────────┴──────────────────────────┘
```

[Aya](https://arxiv.org/abs/2402.07827) (Üstün et al., 2024) is the reference point for the last
row: a community effort producing human-written instruction data across 65+ languages, plus a
513M-instance collection spanning 114. Its own ablations show human-written native data beating
translated data of the same size, and the gap is largest for languages furthest from English.

## The parts people forget

* **Preference data, not just SFT data.** RLHF/DPO stages are almost always English-heavy, so a
  model can be instruction-tuned in 100 languages and *aligned* in one. That mismatch is where
  multilingual safety gaps come from (question 189).
* **Response-language control is a trained behaviour.** If your data always pairs a
  non-English instruction with an English answer — easy to do accidentally when translating only
  the prompts — you have trained language confusion in (question 117).
* **Cultural framing rides along with translated data.** Translated instructions ask about
  Thanksgiving and imperial units, in Bengali. The instructions are grammatical and the
  situations are foreign.
* **Evaluate per language, not in aggregate**, and on natively-written prompts (question 188).

## What an interviewer digs into next

* Why does instruction-following transfer better than, say, factual recall?
* What exactly is wrong with fine-tuning on machine-translated instruction data?
* How would you check that a model answers in the language it was asked in?
* Where does the alignment stage break the multilingual story?
