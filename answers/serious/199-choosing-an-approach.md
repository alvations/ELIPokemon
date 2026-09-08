---
id: "199"
slug: choosing-an-approach
style: serious
category: synthesis
difficulty: advanced
question: "Given all these techniques, how do you decide which one your problem needs?"
tags: [decision-framework, prioritisation, cost, synthesis, diagnosis]
---

# Choosing, rather than collecting

Most of this dataset describes techniques. This one is about not reaching for the wrong one, which
is where most project time is actually lost.

## Diagnose before you prescribe

Almost every multimodal and multilingual failure falls into one of five buckets, and each has a
different cheapest fix. Running the diagnosis costs an afternoon; skipping it costs a quarter.

```
   ┌─ Is the information even in the input? ────────────────────────────────┐
   │  give the model a perfect textual description. Does it now answer?     │
   │      YES ─► PERCEPTION problem. Raise resolution, tile, use OCR        │
   │             (q121, q123, q127). More reasoning will not help (q160).   │
   │      NO  ─► continue                                                   │
   ├─ Does it get it right in the dominant language / on the easy split? ───┤
   │      YES ─► COVERAGE problem. Data, adapters, per-group work           │
   │             (q103, q110, q162, q185). Not an architecture problem.     │
   │      NO  ─► continue                                                   │
   ├─ Is the answer fluent, confident and wrong? ───────────────────────────┤
   │      YES ─► GROUNDING problem. Retrieval, citations, contrastive       │
   │             decoding, preference pairs (q122, q136, q140, q167).       │
   │      NO  ─► continue                                                   │
   ├─ Does it know the right answer but produce the wrong FORM? ────────────┤
   │      YES ─► CONSTRAINT problem. Glossary, length control, schema,      │
   │             validation (q133, q144, q156). Cheap. Do this first.       │
   │      NO  ─► continue                                                   │
   └─ Only then: a REASONING problem. CoT, tools, a stronger model.         ┘
```

The ordering is deliberate. The last bucket is the one everybody reaches for first, and it is the
rarest and most expensive.

## Cheapest-first, in general

1. **Fix the input.** Resolution, source authoring, preprocessing, normalisation (questions 121, 179,
   115). Consistently the highest leverage and the least glamorous.
2. **Fix the retrieval or the context.** Give it the document, the previous segments, the glossary
   (questions 131, 133, 140).
3. **Fix the constraints.** Validate mechanically instead of hoping (questions 156, 136).
4. **Route.** Send the hard 5% somewhere better rather than upgrading everything (questions 132, 180).
5. **Only then, train something.** Adapters before fine-tuning, fine-tuning before pretraining.

## The questions to ask before building anything

* **What is the cost of being wrong, and is it symmetric?** If a critical error is categorically
  worse than an average one, your metric must reflect that (questions 132, 187).
* **Is the action reversible?** If not, no accuracy number substitutes for a confirmation gate
  (questions 145, 181).
* **Who cannot check the output?** If the user cannot verify it, hallucination is a different class
  of problem (questions 183, 155).
* **What is the volume?** At high volume, distillation arithmetic usually wins (question 182). At low
  volume it never pays back.
* **What must not leave the device or the jurisdiction?** This constrains architecture before quality
  does (questions 174, 187, 194).

## The honest default

For most problems: a strong general model, at adequate resolution, with retrieval, a glossary,
mechanical output validation, quality-based routing, and a small hand-built evaluation set. That
combination beats a cleverer architecture almost every time, and it is boring enough that teams skip
straight past it.

## What an interviewer digs into next

* How would you distinguish a perception failure from a reasoning failure in one test?
* Why is the reasoning bucket the last one to consider?
* Which questions constrain architecture before quality does?
* Why does the boring default win?
