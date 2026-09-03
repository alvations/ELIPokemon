---
id: "029"
slug: finetuning-vs-peft-vs-prompting
style: serious
category: fine-tuning
difficulty: core
question: "When would you choose full fine-tuning vs PEFT vs prompting?"
tags: [fine-tuning, peft, prompting, rag, decision-framework]
---

# Choosing between prompting, PEFT, and full fine-tuning

The honest ordering is **cheapest first**, and most teams should stop earlier than they do.

```
   ┌─ 1. PROMPTING ───────────────── minutes ── $0 ──────────────────┐
   │    system prompt, few-shot examples, output schema              │
   │    ✅ instant iteration  ✅ no infra  ✅ works across models     │
   │    ❌ costs tokens every call  ❌ limited by context             │
   └────────────────────────┬────────────────────────────────────────┘
   ┌─ 2. RAG ────────────────▼────── hours ── $ ─────────────────────┐
   │    retrieve relevant context at request time                    │
   │    ✅ knowledge updates instantly  ✅ citable  ✅ no forgetting   │
   │    ❌ retrieval quality is now your bottleneck                   │
   └────────────────────────┬────────────────────────────────────────┘
   ┌─ 3. PEFT (LoRA/QLoRA) ──▼────── days ── $$ ─────────────────────┐
   │    learn a small adapter on 1k–100k examples                    │
   │    ✅ cheap  ✅ swappable  ✅ base preserved                      │
   │    ❌ needs labelled data  ❌ another artifact to version         │
   └────────────────────────┬────────────────────────────────────────┘
   ┌─ 4. FULL FINE-TUNING ───▼────── weeks ── $$$$ ──────────────────┐
   │    update every parameter                                       │
   │    ✅ maximum adaptation  ❌ forgetting  ❌ per-task model copy   │
   └─────────────────────────────────────────────────────────────────┘
```

## The decision rule

**What kind of gap are you closing?**

| The problem is... | The fix is... |
| --- | --- |
| The model doesn't know a *fact* | RAG. Never fine-tuning. |
| The model doesn't follow your *format* | Prompting, then PEFT if the prompt gets long |
| The model has the wrong *tone/style* | PEFT — this is exactly what it is good at |
| The model can't do the *task* at all | PEFT with real data, or a better base model |
| You need a *new language or modality* | Full fine-tuning or continued pretraining |
| Latency/cost is too high | Distil into a smaller model (fine-tuning a small model) |

The one people get wrong repeatedly is the first row. Fine-tuning to inject facts is expensive,
stale the moment your data changes, unauditable, and — as
[Gekhman et al. (2024)](https://arxiv.org/abs/2405.05904) measured — actively increases
hallucination, because you are teaching the *form* of confident answering on content the model
does not reliably know.

## When fine-tuning genuinely wins

* **Prompt amortisation.** If a 3,000-token system prompt is prepended to every one of ten million
  daily calls, baking that behaviour into an adapter pays for itself quickly. (Prompt caching
  narrows this gap but does not close it.)
* **Format reliability.** Getting 99.9% valid structured output is often easier with a few
  thousand examples than with any prompt.
* **Distillation.** Fine-tuning a small model on a large model's outputs to cut cost and latency
  by 10× at equal task quality. This is probably the single highest-ROI use of fine-tuning today.
* **Behaviour that resists description.** House writing style, domain-specific judgement,
  proprietary conventions — things easier to demonstrate than to specify.

## Practical sequencing

1. Build the eval set **first**. Without it you cannot tell whether any of this helped.
2. Try a good prompt. Measure.
3. Add retrieval if the gap is knowledge. Measure.
4. Only now consider PEFT — and use the prompt-engineered version to *generate* training data.
5. Full fine-tuning only when you have a strong reason and the data to justify it.

The most common expensive mistake is jumping to step 5 from step 1, without an eval set, to fix a
problem that was a retrieval problem.

## What an interviewer digs into next

* Why does fine-tuning to add facts increase hallucination?
* At what call volume does a fine-tune beat a long system prompt?
* How would you build a distillation pipeline, and how would you know it worked?
* What would make you choose full fine-tuning over LoRA?
