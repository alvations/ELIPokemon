---
id: "182"
slug: vlm-distillation
style: serious
category: multimodal
difficulty: intermediate
question: "How do you make a small vision-language model that is actually useful?"
tags: [distillation, small-models, quantization, on-device, specialisation, evaluation]
---

# Small VLMs

The interesting question is not "how small can it be" but "how narrow can the task be". A 2B VLM
that does one job well beats a 70B one you cannot afford to run at the volume you need — and it
beats it on **your** metric, which is cost per correct answer, not accuracy.

## The three levers, and their different characters

* **Distillation.** Train the small model on the large one's outputs — ideally on *your* input
  distribution rather than a generic corpus. This is the highest-value lever because it transfers
  capability *and* the teacher's behaviour on your data. Generate teacher outputs for real traffic,
  filter them (question 146's caution: the teacher's errors become ground truth), and train.
* **Quantisation** (question 030). Cheap, mostly lossless to 8-bit, and worth checking on the
  **vision tower separately** — quantisation error in the encoder propagates into every downstream
  token, and stacks are inconsistent about whether they quantise it at all.
* **Architectural reduction.** Fewer visual tokens (question 121), a smaller LLM, a smaller encoder.
  Note the asymmetry from question 165: cutting visual tokens saves prefill, cutting LLM size saves
  less than the parameter ratio implies.

## Specialisation beats generality, hard

A small model asked to do everything is bad at everything. A small model asked to do **receipt
field extraction** can match a frontier model on receipts. The recipe:

```
   frontier model ─► label your real inputs ─► human-check a sample ─► fine-tune the small model
                          │
                    this is the expensive step, and it is a ONE-OFF.
                    Inference is then cheap forever.
```

The break-even is usually low: at meaningful volume, a day of labelling plus a fine-tune pays back
within weeks. Teams frequently pay frontier prices for a narrow, high-volume task for a year
because nobody did the arithmetic.

## What small models lose first

Worth knowing before you are surprised in production:

* **Instruction-following robustness** — small models are much more sensitive to prompt phrasing.
* **Multi-image and long-context reasoning** (question 124) degrade sharply.
* **Reading small text** — this is resolution, not capacity (question 121), so it is often
  recoverable by tiling rather than by a bigger model.
* **Calibration** — small models are more confidently wrong, which matters if you route on
  confidence (question 132).
* **Refusal behaviour** — safety tuning transfers unevenly through distillation, so re-test it
  (question 139) rather than assuming it came along.

## Evaluation

Report **cost per correct answer**, not accuracy. A model at 92% and 1/50th the price beats one at
96% for most products, and the accuracy-only comparison actively obscures that.

Then measure on **your** distribution. Public benchmarks tell you about public benchmarks
(question 147); a 200-example set from your real traffic is worth more than all of them for this
decision.

## What an interviewer digs into next

* Why distil on your own traffic rather than a public corpus?
* Why check quantisation of the vision tower separately?
* What capability degrades first as you shrink, and which apparent degradation is really resolution?
* Why is cost per correct answer the right metric here?
