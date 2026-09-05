---
id: "110"
slug: language-adapters
style: serious
category: multilingual
difficulty: advanced
question: "What are language adapters, and when do you prefer them to one big multilingual model?"
tags: [adapters, mad-x, modularity, peft, lora]
---

# Language adapters

An adapter is a small bottleneck module inserted into every layer of a frozen backbone
([Houlsby et al., 2019](https://arxiv.org/abs/1902.00751)) — typically under 1% of the model's
parameters. A **language adapter** is one trained with a language-modelling objective on
monolingual text in a target language; a **task adapter** is one trained on labelled task data.
Stack them and you get the design that makes this interesting.

## MAD-X, the canonical recipe

[Pfeiffer et al. (2020)](https://arxiv.org/abs/2005.00052) compose three pieces:

```
                ┌──────────────────────────────────────┐
   input ──────►│ frozen multilingual backbone (XLM-R)  │
                │   ├─ invertible adapter  ← per language, on the embeddings
                │   ├─ language adapter    ← per language, monolingual LM data
                │   └─ task adapter        ← per task, trained on ENGLISH
                └──────────────────────────────────────┘
                                 │
   train:   [ en language adapter ] + [ task adapter ]   on English labels
   serve:   [ sw language adapter ] + [ task adapter ]   on Swahili input
                                 ▲
                    swap ONE component. Nothing is retrained.
```

The trick is the swap. The task adapter never saw Swahili; the language adapter never saw the
task. Composed at inference, they transfer — and crucially you can add a language the backbone
never pretrained on by training a language adapter (plus vocabulary extension) on unlabelled
text alone.

## Why you would want this

* **Adding a language does not touch the others.** No retraining, no catastrophic forgetting
  (question 026), no regression testing of 99 other languages because you added a 100th.
* **It buys back capacity.** The curse of multilinguality (question 103) is interference over
  shared parameters; per-language parameters are the direct answer.
* **Cheap to train and ship.** Megabytes per language, not gigabytes. You can hold hundreds in
  memory and route per request.
* **Composability** — language × task × domain, trained independently and combined, which is the
  broader "modular deep learning" argument
  ([Pfeiffer et al., 2023](https://arxiv.org/abs/2302.11529)).

## Why you would not

* **You lose positive transfer at serving time.** A monolithic model can use Portuguese evidence
  while answering in Galician; a strictly-routed adapter stack cannot, unless you fuse adapters
  (AdapterFusion) or average them — which brings back the interference you were avoiding.
* **Routing is now your problem.** You must know the request's language before you can pick the
  adapter, so LID errors (question 108) become serving errors. Code-switched input has no
  correct routing decision at all.
* **Serving complexity.** Batching requests with different adapters is awkward; the throughput
  story is worse than one dense model unless your stack supports multi-adapter batching.
* **A quality ceiling.** Full fine-tuning usually still wins by a small margin when you have the
  data and can afford to maintain a separate model.

LoRA (question 027) is the same argument with a different parameterisation, and per-language
LoRA on a decoder LLM is the modern instantiation of MAD-X's idea.

## What an interviewer digs into next

* Why does the task adapter transfer if it was only ever trained on English?
* How would you add a language whose script the backbone has never seen?
* What breaks when a request is code-switched?
* When is fusing adapters better than routing to one, and what does it cost?
