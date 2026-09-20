---
id: "209"
slug: distillation-from-a-frontier-parent
style: serious
category: frontier
difficulty: advanced
question: "Open models like Gemma are distilled from closed frontier models. What survives that transfer and what does not?"
tags: [distillation, capacity-gap, open-weights, calibration, licensing]
---

# The behaviour transfers. The capacity does not.

Gemma 4 is Apache 2.0, openly described as distilled from Gemini, and ships as a family — dense
checkpoints from small to around 31B plus a sparse 26B-with-roughly-4B-active variant, with
grouped-query and multi-query attention, sliding-window attention over long context, RMSNorm and
RoPE. The interesting thing is not the architecture list. It is that **a downloadable model is
carrying the behaviour of a training run nobody outside Google could afford.**

## What distillation actually moves

The student trains against the teacher's *distribution*, not against hard labels. A one-hot
target says "the answer is B". A teacher's softened distribution says "B, but C was close and D
was never in contention" — the relative structure over wrong answers is the extra signal, and
it is worth many times more per example than the label alone.

Beyond the logits, three things transfer well:

* **Format and register.** Response shape, hedging behaviour, refusal style, how it lays out
  code. This is why distilled models *feel* like their parent long before they match it.
* **The teacher's data curation, indirectly.** You inherit the benefit of filtering and mixture
  decisions you never see, because they are baked into what the teacher says.
* **Common-case competence.** The head of the distribution transfers almost completely.

## What does not

```
   ┌── teacher (frontier scale) ──────────────────────────────────┐
   │                                                              │
   │   head of distribution        long tail        rare skills   │
   │   ████████████████████        ██████████       ███████       │
   └──────────┬──────────────────────┬─────────────────┬──────────┘
              │ transfers            │ partial         │ mostly lost
              ▼                      ▼                 ▼
   ┌── student (1-5% of the size) ────────────────────────────────┐
   │   ████████████████████        ███·······       ·······       │
   └──────────────────────────────────────────────────────────────┘
        ▲                              ▲                  ▲
        │                              │                  └ facts that
        │                              │                    need storage
        │                              └ multi-step reasoning depth
        └ style, format, refusals: nearly free

   Capacity gap: a teacher too far above the student transfers WORSE
   than a mid-sized one. Distilling from the biggest thing you have
   is not automatically the best move.
```

* **The hard tail.** Long multi-step reasoning, unusual domains, anything needing stored facts the
  student has no parameters to hold.
* **Calibration.** Students routinely come out *more* confident than their teachers, because
  matching the argmax is easier than matching the shape of the distribution. If you care about
  the probability, measure it again after distilling (question 202).
* **Long-horizon reliability.** A 50-turn agentic trace compounds small divergences. Per-turn
  parity and trajectory parity are different results.
* **The teacher's ceiling.** A student cannot exceed what it was shown, on the distribution it
  was shown. Prompts unlike the distillation set are where the gap reopens.

There is also a **capacity gap** effect worth naming: distilling from a teacher enormously larger
than the student can underperform distilling from a mid-sized intermediate, which is why
teacher-assistant chains exist.

## The part that is legal, not technical

Gemma-from-Gemini is legitimate because one organisation owns both ends. **Distilling from
somebody else's API almost always violates their terms of service**, and several open releases
have been accused of exactly this. If you are planning to distil, the licence of the *outputs*
you train on is the first question, not the last.

## What an interviewer is listening for

That you can say what soft targets carry that labels do not. Then the honest list of what does
not survive — and especially that calibration degrades, which almost nobody mentions. The
strongest answers bring up the capacity gap and the terms-of-service question unprompted.

## Where this stands, September 2026

Gemma 4's specifics are as reported in September 2026 and the model card is the authority.
Distillation itself long predates this generation and the failure modes above have been stable
across several.
