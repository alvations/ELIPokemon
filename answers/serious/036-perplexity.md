---
id: "036"
slug: perplexity
style: serious
category: evaluation
difficulty: core
question: "What is perplexity and what are its limits?"
tags: [perplexity, cross-entropy, evaluation, tokenizer, bits-per-byte]
---

# Perplexity

Perplexity is the exponentiated average negative log-likelihood per token:

$$\text{PPL} = \exp\!\left(-\frac{1}{N}\sum_{i=1}^{N}\log P(x_i \mid x_{<i})\right) = \exp(\mathcal{L}_{\text{CE}})$$

It is exactly `e` raised to the cross-entropy loss — the same number the model was trained to
minimise, in a more interpretable unit.

## The interpretation

Perplexity is the **effective branching factor**: the number of equally-likely options the model is
effectively choosing between at each step.

```
   PPL = 1      perfect. Every token predicted with probability 1.
   PPL = 2      as uncertain as a fair coin flip per token.
   PPL = 50     as if picking uniformly among 50 candidates.
   PPL = 50,000 as if picking uniformly from the whole vocabulary — untrained.

   Modern LLMs on general web text: roughly 5–15.
```

If a model assigns probability `1/k` to the correct token every time, its perplexity is `k`. Lower
is better.

## Why it is useful

* It is the **only** metric that is a smooth, dense function of every token, so it detects small
  changes reliably.
* It requires no labels, no reference outputs, and no human judgement.
* It is what **scaling laws** are expressed in, and it predicts remarkably well across orders of
  magnitude.
* It is the right instrument for regression testing: quantization damage, data-mixture changes, or
  a training bug show up in perplexity before they show up anywhere else.

## The limits — the part interviewers care about

**1. Not comparable across tokenizers.** Perplexity is per *token*, and tokenizers differ in how
many tokens they use for the same text. A model with a larger vocabulary gets shorter sequences and
mechanically lower perplexity without being better. To compare across tokenizers, use
**bits-per-byte**: `BPB = (N_tokens / N_bytes) · log₂(PPL)`, normalising to a unit that does not
depend on the tokenizer.

**2. Not comparable across datasets.** Perplexity on Wikipedia and on Reddit are different numbers
measuring different things. Always report the corpus.

**3. Contamination inflates it.** If the eval text was in the training set, perplexity is
meaninglessly low.

**4. It does not measure what you care about.** This is the important one. Perplexity measures
*calibrated prediction of the next token in a corpus*, which is only loosely related to being
helpful, correct, or safe. Specifically:

* **RLHF reliably increases perplexity while improving human preference scores.** The model becomes
  more decisive and less distribution-matching — worse at predicting arbitrary internet text,
  better at being an assistant. If you use perplexity to evaluate a post-trained model you will
  reject exactly the changes you wanted.
* It cannot see factual accuracy: a fluent falsehood and a fluent truth can have identical
  perplexity.
* It cannot see instruction following, reasoning, or long-horizon coherence.
* Marginal perplexity differences do not map to task differences — a 2% perplexity gap says almost
  nothing about downstream benchmark scores.

**5. It is undefined for non-probabilistic outputs.** You cannot compute perplexity of an API that
only returns text.

## The rule of thumb

**Use perplexity during pretraining, stop using it after.** It is a superb training-time
instrument and a bad product metric. Once you have an assistant, you need task benchmarks, human
preference, and application-specific evals.

## What an interviewer digs into next

* Derive perplexity from cross-entropy and explain the branching-factor reading.
* Why does a bigger vocabulary lower perplexity without improving the model?
* Why does RLHF *raise* perplexity, and is that bad?
* What would you use instead to compare two post-trained models?
