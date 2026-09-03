---
id: "090"
slug: transfer-learning
style: serious
category: training
difficulty: core
question: "What is transfer learning and how do you decide what to freeze?"
tags: [transfer-learning, freezing, feature-extraction, discriminative-lr, domain-shift]
---

# Transfer learning

Reuse representations learned on one task for another. It works because early layers learn features
that are **general** — edges, textures, syntax, common word senses — while later layers learn features
that are **task-specific**. The general part transfers; the specific part does not.

[Yosinski et al. (2014)](https://arxiv.org/abs/1411.1792) measured this layer by layer:
transferability declines with depth, and there is a middle region where features are co-adapted to
their neighbours and transfer *worse* than either extreme.

```
   ┌──────────────────────────────────────────────────────────────┐
   │  early layers    edges, textures, tokens, morphology         │
   │                  ✅ transfer almost anywhere                  │
   ├──────────────────────────────────────────────────────────────┤
   │  middle layers   parts, phrases, entities, relations         │
   │                  ⚠️ transfer within a domain                  │
   ├──────────────────────────────────────────────────────────────┤
   │  late layers     "is this a Persian cat", "is this spam"     │
   │                  ❌ task-specific; usually replaced           │
   └──────────────────────────────────────────────────────────────┘
```

## The decision: what to freeze

Two axes determine the answer — **how much data you have**, and **how similar your task is to the
pretraining task**:

```
                     data:  SMALL                    LARGE
                          ┌──────────────────────┬──────────────────────┐
   task    SIMILAR        │ freeze everything,   │ fine-tune everything │
   is                     │ train a new head     │ (low LR)             │
                          │ (linear probing)     │                      │
                          ├──────────────────────┼──────────────────────┤
           DIFFERENT      │ freeze early layers, │ fine-tune everything,│
                          │ tune late ones —     │ or retrain from      │
                          │ the hardest quadrant │ scratch if very      │
                          │                      │ different            │
                          └──────────────────────┴──────────────────────┘
```

The bottom-left is genuinely hard: too little data to adapt, too different for the pretrained
features to be right. It is where PEFT (question 027), aggressive augmentation, and synthetic data
earn their keep.

## Techniques

* **Linear probing** — freeze the backbone, train only a new head. Fast, needs little data, cannot
  adapt features. Also a useful *diagnostic*: if a linear probe does well, the representation already
  contains what you need.
* **Full fine-tuning** — everything trainable at a low learning rate (10–100× below pretraining).
* **Gradual unfreezing** — train the head, then unfreeze layers from the top down. Reduces the
  catastrophic-forgetting risk of hitting a pretrained network with large gradients from a randomly
  initialised head.
* **Discriminative learning rates** — lower rates for earlier layers, higher for later ones,
  reflecting how much each should change.
* **PEFT / LoRA** — freeze everything, learn a small adapter. The modern default for LLMs.

## The pitfalls

* **Learning rate too high.** The single most common failure: a large rate destroys pretrained
  features in the first few steps. Warm up, and use a much lower rate than you would from scratch.
* **A randomly initialised head.** Its large initial gradients propagate into the backbone. Train the
  head alone for an epoch first, or use a lower backbone LR.
* **Preprocessing mismatch.** Use the *same* normalisation, tokenizer, and image resolution as
  pretraining. A different tokenizer makes the embeddings meaningless.
* **Frozen BatchNorm statistics.** Freezing weights but leaving BatchNorm in training mode updates
  running statistics and silently changes the "frozen" backbone.
* **Negative transfer** — when the source task is unhelpful or harmful, transfer is worse than random
  initialisation. Rare with large pretrained models, real for small ones on distant domains.

## What an interviewer digs into next

* Why does transferability decline with depth?
* When would you use linear probing rather than fine-tuning?
* Why train the head before unfreezing the backbone?
* How would you detect negative transfer?
