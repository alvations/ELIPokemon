---
id: "104"
slug: language-sampling-pretraining
style: serious
category: multilingual
difficulty: intermediate
question: "How do you sample languages when pretraining on an imbalanced multilingual corpus?"
tags: [sampling, temperature, unimax, data-mixture, pretraining]
---

# Sampling an imbalanced multilingual corpus

Web corpora are brutally skewed: English is often 40-50% of a filtered crawl, the top ten
languages are most of the rest, and the tail languages have a few million tokens each. Train on
the natural distribution and the tail is never seen; train uniformly and you replay a tiny
corpus hundreds of times. Sampling policy is how you choose your place between those failures.

## Temperature sampling, the standard answer

Given empirical language proportions `q_l`, sample language `l` with probability

$$p_l = \frac{q_l^{\alpha}}{\sum_{l'} q_{l'}^{\alpha}}$$

`α = 1` is the natural distribution; `α = 0` is uniform. mBERT used an exponential smoothing
equivalent to `α ≈ 0.7`; XLM and XLM-R settled near **`α = 0.3`**, and that value has stuck as
the default for want of a better idea.

```
  natural (α=1)            α = 0.3                   uniform (α=0)
  ┌──────────────────┐     ┌──────────────────┐      ┌──────────────────┐
  │ en ████████████  │     │ en █████         │      │ en ██            │
  │ fr ██            │     │ fr ███           │      │ fr ██            │
  │ sw ▏             │     │ sw ██            │      │ sw ██            │
  │ my ▏             │     │ my ██            │      │ my ██            │
  └──────────────────┘     └──────────────────┘      └──────────────────┘
   tail never learned       compromise               tail seen 400× —
                                                     memorised, not learned
```

## Why the single knob is wrong

`α` conflates two different questions: *how much should this language be represented?* and
*how many times may this corpus be repeated?* A language with 2M tokens and a language with
200M tokens can land on the same `p_l` and have wildly different epoch counts.

[UniMax](https://arxiv.org/abs/2304.09151) (Chung et al., 2023) fixes exactly this: sample as
close to uniform as possible **subject to an explicit cap on the number of epochs** over any one
language's corpus. Languages run out of unrepeated data and drop out of the budget, which is
redistributed to those that still have fresh text. It beat tuned temperature sampling on the
mT5 setup, and it exposes the parameter that actually matters — repetition — instead of hiding
it behind an exponent.

Repetition is the real risk. [Muennighoff et al. (2023)](https://arxiv.org/abs/2305.16264) found
up to about four epochs of repeated data is nearly as good as fresh data, and returns collapse
after that. A tail language repeated 40 times is not being learned; it is being memorised, and
it inflates its own evaluation scores through contamination.

## The other knobs in the same decision

* **Vocabulary sampling** is a *separate* temperature. The tokenizer is usually trained with a
  flatter distribution than the model, because vocabulary coverage of a script is cheap
  insurance (question 105).
* **Quality filtering interacts badly with balance.** Aggressive filters delete more of the tail,
  because filters are calibrated on high-resource text. Filter first, then sample, then check the
  tail survived.
* **Upsampling multiplies the noise too.** If a low-resource corpus is 30% mislabelled or
  machine-translated junk (question 133), upsampling it 40× makes the junk a first-class
  citizen.

## What an interviewer digs into next

* What exactly does `α = 0.3` do to a language with 0.1% of the corpus?
* Why is an epoch cap a better parameter than a temperature?
* How does data quality filtering interact with your sampling policy?
* How would you know, after training, that your sampling was wrong?
