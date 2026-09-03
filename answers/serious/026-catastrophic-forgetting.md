---
id: "026"
slug: catastrophic-forgetting
style: serious
category: training
difficulty: intermediate
question: "What is catastrophic forgetting and how do you mitigate it?"
tags: [catastrophic-forgetting, continual-learning, ewc, replay, alignment-tax]
---

# Catastrophic forgetting

Train a network on task A, then train it on task B, and performance on A collapses. The weights
that encoded A are freely overwritten because nothing in the task-B loss preserves them — gradient
descent has no memory of what a weight was for.

```
   accuracy
      │ ████████████████╗  task A trained
   A  │                 ╚═════╗
      │                       ╚══════════════════  ← collapses during B
      │
   B  │                    ╔══════════════════════
      │ ───────────────────╝
      └────────────────────┬───────────────────────► training time
                    switch to task B
```

For LLMs this is not a theoretical concern. It is what happens when you fine-tune a chat model on
your domain corpus and discover it has become worse at instruction following, worse at refusing
unsafe requests, and worse at everything outside your domain. The general form — safety and
general capability degrading during specialisation — is often called the **alignment tax**.

## Mitigations, roughly in order of practicality

**1. Data mixing (replay).** The workhorse. Mix 5–30% of general/instruction/safety data into your
fine-tuning set. Cheap, effective, and it is what almost everyone actually does. The mixing ratio
is the main knob.

**2. Parameter-efficient fine-tuning.** LoRA and friends freeze the base weights entirely and
learn a low-rank update. The original knowledge is *literally still there* — you can unload the
adapter and get the base model back. This structurally limits how much can be forgotten, and it
is a large part of why PEFT is the default for domain adaptation.

**3. Lower learning rates and fewer epochs.** Most forgetting during LLM fine-tuning is caused by
training too hard. One to three epochs at `1e-5` or below is standard, and "it forgot everything"
usually means someone ran ten epochs at `1e-4`.

**4. Regularisation toward the original.** Penalise drift from the base model — KL divergence on
output distributions (the same idea as RLHF's KL penalty), or L2 on the weights. **EWC** (Elastic
Weight Consolidation, [Kirkpatrick et al., 2017](https://arxiv.org/abs/1612.00796)) is the
principled version: weight each parameter's penalty by its Fisher information, so parameters that
mattered for the old task are held firmly and unimportant ones move freely.

**5. Modularity.** Keep separate adapters per domain and route between them; or use a
mixture-of-experts structure where new capability lands in new experts. Avoids interference by
avoiding shared weights.

**6. Don't fine-tune at all.** Frequently the right answer. If the requirement is "know our
internal documentation", retrieval is better than fine-tuning: no forgetting, updatable in
seconds, and citable.

## Why it happens

There is no mechanism preserving old behaviour. In the multi-task setting, gradients for A and B
are averaged and the optimiser finds a solution good for both; in the sequential setting, only B's
gradient exists, and the loss landscape for B is full of minima that are terrible for A. Joint
training is not a *fix* for forgetting so much as a way of never inducing it.

## Diagnosing it

Always evaluate on a **held-out general benchmark** during domain fine-tuning, not only on your
domain metric. The classic failure is a dashboard showing domain accuracy climbing beautifully
while the model quietly loses the ability to refuse, to follow formatting instructions, or to
handle anything off-topic. If you only measure what you are optimising, you will not see the cost.

## What an interviewer digs into next

* Why does LoRA reduce forgetting structurally rather than incidentally?
* What is EWC computing, and why the Fisher information specifically?
* How would you choose the replay mixing ratio?
* Given a domain-adaptation task, how would you decide between fine-tuning and RAG?
