---
id: "031"
slug: knowledge-distillation
style: serious
category: training
difficulty: intermediate
question: "What is knowledge distillation and why does a student sometimes beat its teacher?"
tags: [distillation, dark-knowledge, temperature, soft-targets, model-compression]
---

# Knowledge distillation

Train a small **student** to imitate a large **teacher** rather than to fit hard labels
([Hinton et al., 2015](https://arxiv.org/abs/1503.02531)). The insight is that the teacher's full
output distribution carries far more information than the correct answer alone.

```
   HARD LABEL                       TEACHER'S SOFT DISTRIBUTION
   ──────────                       ───────────────────────────
   Charmander: 1                    Charmander:  0.85
   Charmeleon: 0                    Charmeleon:  0.11   ← "these two are similar"
   Squirtle:   0                    Squirtle:    0.02
   Pikachu:    0                    Pikachu:     0.02

   one bit of information            a full similarity structure over classes
```

Hinton called the ratios among the wrong answers **dark knowledge**: the teacher has learned that
Charmander is much more confusable with Charmeleon than with Squirtle, and that relational
information is a far richer training signal than a one-hot vector.

## Temperature

Soften both distributions before comparing them:

$$p_i = \frac{\exp(z_i/T)}{\sum_j \exp(z_j/T)}$$

At `T = 1` a confident teacher's non-target probabilities are ~1e-8 and contribute nothing. At
`T = 3..10` the structure becomes visible. The loss is usually

$$\mathcal{L} = \alpha\,T^2\,\text{KL}(p^T_{\text{teacher}} \,\|\, p^T_{\text{student}})
+ (1-\alpha)\,\text{CE}(y, p^{T=1}_{\text{student}})$$

The `T²` factor compensates for gradients scaling as `1/T²`, keeping the two terms balanced when
you change `T`.

## Variants for LLMs

* **Sequence-level / hard distillation** — the teacher *generates* outputs, the student
  fine-tunes on them as ordinary text. This is what "distillation" almost always means for LLMs
  today, and it needs only API access to the teacher, not logits.
* **Logit distillation** — match full next-token distributions. More signal per token, requires
  white-box access and a shared tokenizer.
* **On-policy / GKD** — the student generates, the teacher scores *the student's own* outputs.
  Fixes the exposure-bias mismatch of training only on teacher-generated text, and is
  meaningfully better.
* **Reverse KL** vs forward KL — forward KL is mode-covering (the student spreads mass over
  everything the teacher might say, producing hedging); reverse KL is mode-seeking (the student
  commits to one mode). Reverse KL is generally preferred for generation quality.
* **Feature/attention distillation** — match intermediate hidden states or attention maps
  (TinyBERT, DistilBERT).

## Why the student can beat the teacher

Not folklore — it happens, and there are real mechanisms:

1. **Regularisation.** Soft targets carry less label noise than hard labels, and the similarity
   structure acts as a strong prior. Self-distillation (identical architectures) improves accuracy
   for exactly this reason.
2. **Label noise removal.** A teacher averaged over a dataset smooths mislabelled examples; the
   student never sees the raw error.
3. **Ensemble compression.** Distilling an ensemble of teachers into one student captures much of
   the ensemble gain in a single model.
4. **Data amplification.** The teacher can label unlimited unlabelled data, so the student trains
   on far more supervised examples than existed originally.
5. **Best-of-n distillation.** Sample `n` teacher outputs, keep only the best by some verifier, and
   train the student on those. The student learns from a distribution *better* than the teacher's
   average behaviour — this is the mechanism behind many strong small models.

## Limits

The student inherits the teacher's errors and biases, cannot exceed it on capabilities it never
demonstrates, and distillation of a much larger teacher into a much smaller student hits a
capacity wall. There are also licensing constraints on distilling from commercial APIs.

## What an interviewer digs into next

* Why does temperature reveal dark knowledge, and why the `T²` correction?
* Forward vs reverse KL — which produces hedging, and why?
* Why is on-policy distillation better than training on teacher-generated text?
* Explain concretely how best-of-n distillation lets a student beat its teacher.
