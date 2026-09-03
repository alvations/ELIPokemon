---
id: "040"
slug: hallucination
style: serious
category: reliability
difficulty: core
question: "Why do LLMs hallucinate and how do you reduce it?"
tags: [hallucination, calibration, rag, grounding, abstention]
---

# Hallucination

A model produces fluent, confident, false content. The single most important framing for an
interview: **hallucination is not a bug in the implementation, it is a consequence of the training
objective.**

## Why it happens

**1. The objective rewards plausibility, not truth.** Next-token prediction maximises the
likelihood of text that *looks like* the corpus. There is no term for factual accuracy anywhere in
pretraining. A fluent falsehood and a fluent truth are equally good continuations.

**2. There is no "I don't know" in the data.** Human-written text rarely trails off into
uncertainty; it asserts. The model learns the *form* of confident assertion and applies it
regardless of whether it has the underlying knowledge.

**3. Post-training makes it worse in a specific way.** Preference raters prefer confident, complete
answers over hedged ones. RLHF therefore *rewards* answering over abstaining. And SFT on facts the
base model does not know explicitly teaches confident guessing
([Gekhman et al., 2024](https://arxiv.org/abs/2405.05904)).

**4. Compression.** Model weights are a lossy encoding of the training data. Facts seen once are
stored imprecisely and are reconstructed by interpolation, which produces plausible near-misses —
the right shape of answer with the wrong details.

**5. Exposure bias compounds it.** One invented detail becomes context for everything after it, and
the model then coherently elaborates its own fiction.

```
   TAXONOMY — different causes, different fixes

   ┌────────────────────┬────────────────────────────────────────────┐
   │ Factuality error   │ contradicts the world → RAG, grounding      │
   │ Faithfulness error │ contradicts the given source → decoding,     │
   │                    │   citation enforcement, NLI verification     │
   │ Knowledge gap      │ model never knew → retrieval or abstention   │
   │ Reasoning error    │ knew the facts, derived wrongly → CoT, tools │
   │ Stale knowledge    │ knew, but it changed → retrieval             │
   └────────────────────┴────────────────────────────────────────────┘
```

Diagnosing *which* one you have is most of the work. Teams routinely apply RAG to what is actually
a reasoning error, and are surprised when nothing improves.

## Mitigations, in rough order of effectiveness

1. **Retrieval grounding.** Provide the facts in context. Converts a knowledge problem into a
   reading-comprehension problem, which models are far better at.
2. **Require citations, then verify them.** Post-hoc check that each claim is entailed by a cited
   span (an NLI model works well). Catches the residual faithfulness errors RAG does not.
3. **Make abstention acceptable.** Explicitly prompt and train for "I don't know". This trades
   coverage for precision, and for many applications that is the correct trade — but it must be
   *rewarded*, or preference optimisation will train it away.
4. **Tools for anything computable.** Arithmetic, dates, lookups, unit conversion. Do not ask the
   model to be a calculator.
5. **Self-consistency.** Sample `k` times; disagreement across samples is a strong hallucination
   signal, since fabrications are less stable than knowledge.
6. **Lower temperature** for factual tasks.
7. **Uncertainty from token probabilities.** Low probability on the *entity* tokens specifically is
   informative, more so than average sequence probability.

## What does not work

* Telling the model "do not hallucinate". It does not know when it is.
* Fine-tuning on more facts (see cause 3).
* Asking the model "are you sure?" — it will often flip its answer under social pressure without
  new information, which is sycophancy rather than verification.

## Measuring it

You cannot manage this without measurement: build a domain-specific factuality eval with known
answers, and report **both** hallucination rate and abstention rate. Optimising one alone produces
either a confident liar or a model that refuses everything.

## What an interviewer digs into next

* Why does RLHF increase hallucination?
* How would you distinguish a faithfulness error from a factuality error in production?
* Design a hallucination eval for a medical Q&A product.
* Why is "are you sure?" not a valid verification step?
