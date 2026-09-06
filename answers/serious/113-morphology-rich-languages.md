---
id: "113"
slug: morphology-rich-languages
style: serious
category: multilingual
difficulty: intermediate
question: "How does rich morphology challenge subword models?"
tags: [morphology, agglutination, sigmorphon, segmentation, inflection]
---

# Morphologically rich languages

English gets away with a crude story about words because English morphology is thin. Elsewhere
a single orthographic word can encode what English spreads over a clause:

* **Agglutinative** (Turkish, Finnish, Hungarian, Swahili, Quechua): morphemes stack, each with
  one clean meaning. Turkish *evlerinizden* = house-PLURAL-your-from.
* **Fusional** (Russian, Arabic, Greek): one affix bundles several features at once, and stems
  change shape. Arabic is templatic — a consonantal root interleaved with a vowel pattern, so
  related forms do not share a contiguous prefix at all.
* **Polysynthetic** (Inuktitut, Mohawk): a word can be a whole sentence.

## Where this hurts

```
  1. TYPE EXPLOSION
     Finnish nouns inflect into ~2000 forms. Any fixed vocabulary
     covers a vanishing fraction, so nearly every word is split.

  2. SPLITS THAT ARE NOT MORPHEMES
     BPE cuts by frequency, not by meaning:
        evlerinizden  ►  [evler][ini][zden]     frequency-optimal
                      ►  [ev][ler][iniz][den]   what it means
     The model must relearn compositional meaning from arbitrary shards.

  3. SPARSITY
     A rare inflection of a common stem is treated as a rare word.
     The stem's knowledge does not automatically reach it.

  4. GENERATION IS HARDER THAN ANALYSIS
     Reading a wrong-case noun is easy. PRODUCING correct agreement across
     a long sentence needs the model to track features it was never told
     exist. MT into Finnish is much harder than MT out of it.
```

That asymmetry in point 4 is the thing to say in an interview: translation quality is not
symmetric across a language pair, and morphology is a large part of why.

## What helps

* **Larger and better-allocated vocabulary** for those languages specifically (question 105) —
  the cheapest real fix.
* **Morphologically-informed segmentation.** Morfessor and unsupervised morphology induction
  predate BPE and still beat it on some tasks; unigram-LM segmentation is closer to
  morphologically plausible than greedy BPE
  ([Bostrom & Durrett, 2020](https://arxiv.org/abs/2004.03720)).
* **Subword regularisation.** Sampling different segmentations of the same word during training
  ([Kudo, 2018](https://arxiv.org/abs/1804.10959)) makes models robust to which arbitrary shard
  boundary they get, and reliably helps low-resource MT.
* **Character or byte-level access** (question 112), which sidesteps the boundary question.
* **Evaluate with character-level metrics.** chrF (question 139) is standard for
  morphologically rich targets precisely because a word-level metric scores a nearly-correct
  inflection as a total miss.

The [SIGMORPHON](https://sigmorphon.github.io/) shared tasks are the field's benchmark for
inflection and segmentation, and are the right place to look for what current systems can and
cannot do.

## What an interviewer digs into next

* Why is translating *into* a morphologically rich language harder than out of it?
* What is subword regularisation, and why does it help low-resource cases most?
* Why is BLEU a bad metric for Finnish output, and what would you use instead?
* How would you allocate vocabulary between Turkish and Vietnamese in one model?
