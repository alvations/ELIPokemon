---
id: "107"
slug: code-switching
style: serious
category: multilingual
difficulty: intermediate
question: "What breaks when text switches language mid-sentence?"
tags: [code-switching, lid, hinglish, lince, gluecos]
---

# Code-switching

Code-switching is using two or more languages inside one conversation, and often inside one
sentence: *"main office pahunch gaya, so let's start the meeting."* It is not error, slang or
degraded language — it is the ordinary register of hundreds of millions of bilingual speakers,
and it is governed by grammar. The **matrix language** supplies the sentence frame; the
**embedded language** supplies inserted material; the switch points are constrained, not random.

Almost every part of a standard NLP pipeline assumes one language per document.

## Where it breaks

```
  1. CRAWL & FILTER   ──►  sentence-level LID labels the line "hi" (55% confident)
                           and the quality filter deletes it as "mixed junk"
                           ► code-switched text is missing from pretraining

  2. TOKENIZE         ──►  the Hindi run is fragmented (it is a minority of the
                           tokenizer's corpus), the English run is not
                           ► ragged, uneven segmentation inside one sentence

  3. MODEL            ──►  the language signal flips mid-sequence; models trained
                           on monolingual documents have rarely seen this

  4. GENERATE         ──►  the model answers entirely in one language, or drifts
                           into the matrix language and never switches back

  5. EVALUATE         ──►  no monolingual benchmark contains a single example
```

Step 1 is the most damaging and the least visible.
[Kreutzer et al. (2022)](https://arxiv.org/abs/2103.12028) documented how corpus filtering
pipelines systematically mislabel and discard exactly this kind of text, so the data shortage
is partly self-inflicted.

## What the research actually measures

* **LinCE** ([Aguilar et al., 2020](https://arxiv.org/abs/2005.04322)) — a benchmark bundling LID,
  POS, NER and sentiment over several code-switched pairs.
* **GLUECoS** ([Khanuja et al., 2020](https://arxiv.org/abs/2004.12376)) — Hindi-English tasks
  including natural language inference; the finding was that multilingual pretraining alone does
  not solve code-switching, and fine-tuning on switched data helps substantially.
* **Synthetic generation** from monolingual data using linguistic switch-point constraints
  (equivalence constraint theory) is the standard data-augmentation trick, and works better than
  random word substitution because random substitutions produce switch points speakers never use.

## Practical guidance

* **Do LID at token level, not document level**, if you must do it at all — and prefer keeping
  ambiguous text to discarding it.
* **Expect romanisation.** Most code-switched text in the wild is written entirely in Latin
  script regardless of the languages involved (question 109), which makes it doubly invisible to
  a native-script model.
* **Test the return path.** A model that answers a Hinglish question in fluent Hindi has failed;
  matching the user's register is part of the task, and it is not what monolingual fine-tuning
  optimises for.
* **Speech is worse.** Code-switched ASR has to switch acoustic and lexical expectations
  mid-utterance, and most ASR systems take a language code as a fixed input parameter.

## What an interviewer digs into next

* Why does sentence-level LID filtering hurt code-switched data specifically?
* Why is constraint-based synthetic code-switching better than random word swaps?
* How would you evaluate whether a model responds in the *right* mixture?
* What changes for speech recognition rather than text?
