---
id: "018"
slug: pretraining-sft-rlhf
style: serious
category: training
difficulty: core
question: "What is the difference between pretraining, supervised fine-tuning, and RLHF?"
tags: [pretraining, sft, rlhf, post-training, alignment]
---

# Pretraining, SFT, and RLHF

Three stages, three different objectives, three different kinds of data, and — crucially — three
different things they can teach.

```
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 1. PRETRAINING                                          months, ~$10M+      │
 │    data:   10–20T tokens of scraped/curated text (unlabelled)               │
 │    loss:   next-token cross-entropy                                         │
 │    result: knows everything, obeys nobody. Continues text.                   │
 │            Prompt "What is 2+2?" → may reply "What is 3+3? What is 4+4?"    │
 ├─────────────────────────────────────────────────────────────────────────────┤
 │ 2. SUPERVISED FINE-TUNING (SFT)                         days, ~10k–1M pairs │
 │    data:   (instruction, ideal response) demonstrations, human or synthetic │
 │    loss:   same next-token cross-entropy, on the response tokens only       │
 │    result: answers questions. Adopts the assistant persona and format.       │
 ├─────────────────────────────────────────────────────────────────────────────┤
 │ 3. PREFERENCE OPTIMISATION (RLHF / DPO)                 days, ~10k–1M pairs │
 │    data:   (prompt, chosen, rejected) human preference comparisons          │
 │    loss:   maximise reward (PPO) or preference likelihood (DPO), KL-anchored │
 │    result: answers *well*. Helpful, honest, refuses appropriately, formats  │
 │            the way people actually prefer.                                   │
 └─────────────────────────────────────────────────────────────────────────────┘

    knowledge ──────────────────────────────────────────────────────► from stage 1
    behaviour ──────────────────────────────────────────► from stages 2–3
```

## Why SFT is not enough

SFT teaches the model to imitate a demonstration. Two limits:

1. **Demonstrations are expensive and capped by the demonstrator.** Writing an ideal answer to a
   hard question is slow, and a human writer's ceiling becomes the model's.
2. **Imitation cannot express "this is better than that."** Cross-entropy on one good answer gives
   no signal about the space of bad ones. It also cannot easily teach *not* doing something.

Preference data flips the economics: **comparing two answers is far cheaper and more reliable than
writing one**, and it directly encodes relative quality. This is the core argument for stage 3,
and it is worth stating in exactly those terms.

## What each stage can and cannot change

| | Pretraining | SFT | RLHF/DPO |
| --- | --- | --- | --- |
| Adds new factual knowledge | ✅ | ⚠️ barely | ❌ |
| Sets response format/persona | ❌ | ✅ | ✅ |
| Teaches refusal & safety behaviour | ❌ | partly | ✅ |
| Improves subtle quality/helpfulness | ❌ | ⚠️ | ✅ |
| Cost | dominant | small | small |

The point interviewers look for: **post-training elicits and shapes capabilities; it rarely
installs new ones.** If a model does not know a fact after pretraining, no amount of SFT will
reliably teach it — you will more likely teach it to *confidently guess*, because you have shown
it examples of confidently answering questions of that shape.

## Modern practice

The clean three-stage picture is now blurrier: mid-training / annealing phases inject
high-quality data at the end of pretraining; SFT data is largely model-generated and filtered;
RLVR (RL with verifiable rewards) trains reasoning against automatic checkers rather than human
preferences; and iterated rounds of SFT → preference optimisation → distillation are standard.
The *conceptual* separation still holds and is still what gets asked.

## What an interviewer digs into next

* Why is loss masked to response tokens only during SFT?
* Why does teaching new facts via SFT tend to increase hallucination?
* Why is preference data cheaper than demonstration data, and where does that break down?
* What does the KL penalty in stage 3 protect against?
