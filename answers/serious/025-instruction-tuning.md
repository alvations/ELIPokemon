---
id: "025"
slug: instruction-tuning
style: serious
category: training
difficulty: core
question: "What is instruction tuning and why does so little data go so far?"
tags: [instruction-tuning, sft, lima, superficial-alignment, chat-template]
---

# Instruction tuning

A pretrained model is a *text continuer*. Prompt it with "What is the capital of France?" and a
plausible continuation is another list of quiz questions — because that is what such a string is
usually followed by on the internet. Instruction tuning fine-tunes on (instruction, response)
pairs so the model treats a request as something to *fulfil* rather than *continue*.

Mechanically it is ordinary supervised fine-tuning:

```
  <|system|>You are a helpful assistant.<|end|>
  <|user|>What is the capital of France?<|end|>
  <|assistant|>The capital of France is Paris.<|end|>
                └──────────────────────────────┘
                    loss computed on THESE tokens only

  ✗ no loss on the system prompt or the user turn — you are teaching the
    model to *respond*, not to *impersonate the user*.
```

The special tokens matter more than they look. They mark role boundaries that the model learns to
treat as structural, which is what makes it possible (imperfectly) to distinguish instructions
from data — the foundation, such as it is, of defences against prompt injection.

## Why so little data works

[LIMA](https://arxiv.org/abs/2305.11206) fine-tuned a 65B model on **1,000** carefully curated
examples and got performance competitive with models trained on far more. That result crystallised
the **Superficial Alignment Hypothesis**:

> Nearly all of a model's knowledge and capability is learned during pretraining. Alignment
> teaches it *which sub-distribution of formats and styles to use* when interacting with users.

The model already knows the capital of France, already knows how to write a polite paragraph,
already knows how to structure an explanation — pretraining contained all of it. Instruction
tuning does not install those abilities; it selects the mode in which they are expressed. A mode
selector needs far less data than a knowledge base.

## The practical consequences

* **Quality ≫ quantity.** A thousand excellent, diverse examples beat a hundred thousand
  mediocre ones. Diversity of *task type* matters more than volume within a type.
* **Never teach new facts here.** SFT on facts the base model does not know teaches the *form* of
  confident answering without the substance — a direct, measurable increase in hallucination
  ([Gekhman et al., 2024](https://arxiv.org/abs/2405.05904)). New knowledge belongs in
  pretraining or in retrieval.
* **Format is contagious.** If most of your examples are bulleted lists, the model will bullet
  everything. Response-length distribution in your SFT set becomes the model's default verbosity.
* **Task diversity buys generalisation.** [FLAN](https://arxiv.org/abs/2109.01652) showed that
  tuning on many task *types* produces zero-shot generalisation to unseen ones — the model learns
  "follow instructions" rather than "do these instructions".
* **Synthetic data is the norm now.** Self-Instruct, Evol-Instruct and distillation from stronger
  models generate most SFT sets; the human effort has moved to filtering and verification.

## The counter-argument worth knowing

The superficial alignment hypothesis is a useful simplification, not a law. Evidence against it:
RLVR-trained reasoning models genuinely improve at maths and code beyond eliciting existing
behaviour, and large-scale SFT on tool use teaches skills that base models plainly do not have.
The honest statement is that **style and format are superficial; some capabilities are not**.

## What an interviewer digs into next

* Why mask the loss on prompt tokens?
* Why does SFT on unfamiliar facts increase hallucination?
* How would you build an SFT set for a domain assistant — and how would you decide it is diverse
  enough?
* Where does the superficial alignment hypothesis break down?
