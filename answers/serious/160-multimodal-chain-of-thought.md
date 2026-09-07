---
id: "160"
slug: multimodal-chain-of-thought
style: serious
category: multimodal
difficulty: advanced
question: "Does chain-of-thought reasoning help vision-language models?"
tags: [multimodal-cot, visual-reasoning, test-time-compute, cropping, verification, tools]
---

# Chain-of-thought over images

Text chain-of-thought works because reasoning steps decompose a problem the model can already
represent. Applied naively to vision it often **does not help, and sometimes hurts** — and the
reason why is the useful part.

## Why naive CoT can hurt

```
   PERCEPTION FAILURE                        REASONING FAILURE
   ─────────────────                         ─────────────────
   the model cannot read the axis label      the model read everything correctly
   (question 121, 127)                        and did the arithmetic wrong

   more thinking:  elaborates confidently     more thinking:  genuinely helps
   on a misreading. Longer, more fluent,
   equally wrong — and now the error has
   a justification attached.
```

Most "visual reasoning" failures are **perception** failures wearing a reasoning costume. Extra
tokens do not add pixels. Worse, a long reasoning chain drifts away from the image exactly as a
long caption does (question 122): later steps condition on earlier text and proportionally less on
what was seen.

**The diagnostic:** if giving the model a perfect textual description of the image fixes the
answer, you have a perception problem and CoT will not touch it.

## What actually works: thinking *with* the image

The productive versions keep returning to the pixels rather than reasoning away from them.

* **Crop and zoom as an action.** Let the model request a magnified region and look again. This
  directly attacks the resolution bottleneck (question 121) instead of narrating around it. It is
  the single most effective multimodal reasoning technique.
* **Extract, then compute.** Emit the structured data first — the table, the coordinates, the list
  of objects — and reason over *that* (question 127). Separates perception from arithmetic and makes
  the failure visible.
* **Ground each step.** Require a box or region reference for every claim in the chain
  (questions 122, 128). A step that must point somewhere is much harder to invent.
* **Tools.** A detector, an OCR engine, a calculator, a segmenter. The model orchestrates; the
  specialists perceive. Reliably better than asking one model to do all of it, at the cost of a
  pipeline.
* **Verification.** Generate, then check the answer against the image in a separate pass. Cheap and
  effective, because checking is easier than answering.

## Test-time compute, and where it pays

Spending more compute at inference helps unevenly:

| Task type | Does more thinking help? |
| --- | --- |
| Multi-step visual maths, charts, diagrams | Yes, substantially |
| Multi-image comparison, counting with occlusion | Yes, especially with re-looking |
| Object recognition, attribute reading | No — perception-bound |
| Small-text reading | No — resolution-bound; raise resolution instead |

Spending inference budget on **re-looking** (more crops, higher resolution) rather than on **more
tokens** is usually the better trade for vision, and it is the opposite of the instinct carried over
from text.

## Evaluation

* **Report with and without CoT, per category.** An aggregate gain hides that CoT helped charts and
  hurt recognition.
* **Check the chain, not just the answer.** Right answer via wrong reasoning is common and does not
  generalise; sample chains and read them.
* **Measure the cost.** A three-point gain for six times the tokens and four extra image encodings
  is a real trade, not a free win.

## What an interviewer digs into next

* How would you distinguish a perception failure from a reasoning failure?
* Why does a long reasoning chain drift away from the image?
* Why is re-looking a better use of inference budget than more tokens?
* Why report CoT gains per category rather than in aggregate?
