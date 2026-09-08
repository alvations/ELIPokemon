---
id: "198"
slug: building-an-evaluation-suite
style: serious
category: multimodal
difficulty: advanced
question: "How do you build an evaluation suite for a multimodal system from scratch?"
tags: [evaluation-design, capability-decomposition, controls, contamination, prioritisation]
---

# Building the evaluation you will actually make decisions with

Public benchmarks tell you about public benchmarks (question 147). The suite that decides what you
ship has to be built, and it is usually the highest-return week of engineering on a multimodal
project.

## Decompose the capability, do not average it

The first mistake is one number. "Multimodal accuracy" averages together skills with nothing in
common, so it moves for reasons you cannot attribute.

```
   split by CAPABILITY:      recognition · OCR · counting · spatial · chart reading
                             · multi-image · instruction following · refusal
   split by INPUT TYPE:      photo · document · screenshot · chart · diagram
   split by CONDITION:       resolution · language/script · image quality
   ─────────────────────────────────────────────────────────────────────────
   report a grid. Every cell is a decision you can act on.
   One number is a decision you cannot.
```

## The controls matter more than the items

An evaluation without controls cannot support a conclusion. Build in, from the start:

* **The blind baseline** — same questions, no image (question 147). The gap is your visual
  capability.
* **A resolution sweep** — the same items at 336px and at full tiling. This separates perception
  problems from reasoning problems (question 160) and it is one command.
* **Option shuffling** for anything multiple choice.
* **A text-only regression set**, to catch question 148's silent cost.
* **Order-shuffled or masked variants** for anything temporal or spatial.

Each of these is cheap and each converts an ambiguous result into an attributable one.

## Build it in this order

1. **Twenty examples from real traffic, labelled by hand.** Before anything else. You will learn more
   about your actual failure distribution here than from any benchmark, and it takes an afternoon.
2. **A hundred more, stratified** across the grid above. This is the set you make decisions with.
3. **The controls.** Blind, resolution sweep, text-only.
4. **Adversarial and safety items** (question 139), on your actual deployment surface.
5. **A canary subset** for production (question 192).
6. *Only then* public benchmarks, for comparability with others' claims.

Teams do this in exactly the reverse order and wonder why the leaderboard gains do not show up in
the product.

## Keep it honest

* **Freeze it, version it, and keep it out of the training loop** (question 189).
* **Decontaminate**: if your items came from the web, assume the model has seen them. For images,
  match perceptually, not by filename.
* **Include items you expect to fail.** A suite everything passes has stopped being informative;
  refresh it upward when the ceiling is hit, and report both old and new for one release.
* **Record the prompt, the resolution, the model version and the date** with every result. Numbers
  without those cannot be compared to each other, including to your own from last quarter.
* **Look at the failures.** Read fifty. The categories you discover become the next version of the
  grid, and no aggregate will hand them to you.

## What an interviewer digs into next

* Why is a single multimodal accuracy number not actionable?
* Which control separates perception failures from reasoning failures?
* Why start with twenty hand-labelled examples rather than a benchmark?
* What does it mean when your suite has no failures left?
