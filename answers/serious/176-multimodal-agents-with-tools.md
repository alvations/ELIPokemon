---
id: "176"
slug: multimodal-agents-with-tools
style: serious
category: multimodal
difficulty: advanced
question: "How do you design a multimodal agent that uses tools rather than doing everything itself?"
tags: [agents, tool-use, orchestration, specialists, error-attribution, cost]
---

# Orchestrating specialists instead of one model doing everything

A general VLM asked to read a chart, count objects, locate a button and compute a difference does
all four badly. The alternative is an agent that **calls specialists** and reasons over their
output. It is reliably better, and it introduces a distinct set of problems.

## The tool inventory

| Tool | Replaces the VLM doing | Why the specialist wins |
| --- | --- | --- |
| OCR engine | reading small text | resolution-independent, gives boxes, cheap |
| Detector / segmenter | counting, locating | counts past four (question 128), gives masks |
| Crop-and-zoom | squinting at a region | the highest-value action in question 160 |
| Code interpreter | arithmetic over extracted values | exact, and the working is inspectable (question 127) |
| Retrieval | recalling a fact about the image content | grounded, citable (question 140) |
| Image search | "what product is this" | a database beats parametric memory |

The VLM's job becomes **deciding what to call, and interpreting what comes back**. That is a
different competence from perception, and it is worth evaluating separately.

## Design decisions that matter

```
   PLAN-THEN-EXECUTE                    INTERLEAVED (ReAct-style)
   ─────────────────                    ─────────────────────────
   decide all steps, then run           observe ─► act ─► observe ─► act
   + cheap, parallelisable              + adapts when a tool returns junk
   - cannot react to a surprise         - serial, more calls, can loop

   use plan-then-execute when the task shape is known;
   interleave when the image might contain anything.
```

* **Type the tool outputs.** A detector returns structured boxes, not prose. Free-text tool output
  re-introduces the parsing errors you called a tool to avoid.
* **Give the model the tool's confidence**, and teach it to distrust low-confidence results. A
  specialist that is wrong silently is worse than no specialist.
* **Budget the loop.** Maximum steps, maximum cost, and a `give_up()` that reports what it tried.
  Unbounded agents fail by spending, not by erroring.
* **Cache aggressively.** The same image is passed to several tools; encode once (question 165).

## Error attribution is the operational problem

When the answer is wrong, *which component* was wrong? A pipeline without per-step logging is
undebuggable, and the failure distribution is rarely what the team guesses:

* the OCR misread a digit;
* the detector missed an object, so the count was right about what it saw;
* the VLM chose the wrong tool;
* the VLM called the right tool and **ignored what it returned** — the most common and most
  frustrating, and it happens when the tool result contradicts the model's prior (question 122's
  language prior, one level up).

Log every call, its inputs, its outputs, and the model's stated reason. Report a **per-component
failure breakdown**, not just end-to-end accuracy — the breakdown tells you where to spend and the
aggregate does not.

## When not to build this

If a single well-chosen model at adequate resolution answers your task, a tool-using agent adds
latency, cost and failure modes for nothing. The honest test: measure the monolithic VLM at your
target resolution first. A surprising number of "we need an agent" problems are
"we downsampled the image" problems (question 121).

## What an interviewer digs into next

* When would you interleave rather than plan up front?
* Why should tool outputs be typed rather than prose?
* What does it mean when the model ignores a correct tool result, and why does it happen?
* How would you decide an agent is not warranted?
