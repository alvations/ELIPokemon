---
id: "091"
slug: self-supervised-learning
style: serious
category: training
difficulty: intermediate
question: "What is self-supervised learning and why did it beat supervised pretraining?"
tags: [self-supervised, pretext-task, masked-modelling, contrastive, labels]
---

# Self-supervised learning

Create the supervision signal **from the data itself** rather than from human labels. The label comes
from a structural property you deliberately hide and ask the model to recover.

```
   SUPERVISED                          SELF-SUPERVISED
   ──────────                          ───────────────
   (image, "cat")   ← human labels     (image, image)     ← hide part, predict it
   (text, "spam")                      "The cat sat on the [MASK]"
                                       "The cat sat on the ___" → next token

   bottleneck: human annotation        bottleneck: compute
   ~10⁶–10⁷ labelled examples          ~10¹²–10¹³ tokens, free
```

## The families

**Generative / predictive** — reconstruct hidden parts.
* Next-token prediction (GPT) — the dominant one, and the densest signal available: every position is
  a labelled example.
* Masked language modelling (BERT) — hide 15%, predict them. Bidirectional context, but only 15% of
  positions produce gradient.
* Masked image modelling (MAE) — mask 75% of image patches and reconstruct. The high mask ratio is
  necessary because images are far more redundant than text.

**Contrastive** — pull augmented views of the same instance together, push different instances apart
(SimCLR, MoCo, CLIP; question 092). Requires careful negative sampling and large batches.

**Self-distillation** — a student matches a slowly-updated teacher's output on different views
(BYOL, DINO). Notably needs **no negatives at all**, which was a surprise; asymmetry (a predictor
head, stop-gradient, EMA teacher) is what prevents collapse.

## Why it won

**1. Labels were the bottleneck, and they were removed.** ImageNet took years and enormous cost for
1.3M labels. The web has trillions of tokens for free. Since capability scales with data (question
014), removing the data ceiling was decisive.

**2. The supervision is richer.** A label of "cat" is ~10 bits. Predicting the next token requires
modelling syntax, semantics, facts, and reasoning — everything needed to produce the text. A
classification label tells the model only what humans chose to categorise; the raw data contains
everything else too.

**3. Labels induce a narrow objective.** A model trained to classify 1000 ImageNet categories learns
features useful for *those* categories and may discard everything else. Self-supervised objectives do
not pre-commit to a downstream task, so the representations generalise more broadly.

**4. It scales without human cost.** Doubling supervised data doubles annotation spend. Doubling
self-supervised data is a storage and compute problem.

## The catches

* **Pretext task design matters enormously.** Early ones (predicting rotation, jigsaw puzzle order,
  colourisation) worked poorly because they admitted shortcuts. The winners are those with no easy
  shortcut — you genuinely cannot predict the next token without understanding the text.
* **Compute-hungry.** You traded annotation cost for GPU cost, which was the right trade but is not
  free.
* **Data quality re-emerges as the bottleneck.** Once labels are unlimited, filtering, deduplication
  and curation become the levers — and are now most of the work in pretraining.
* **Evaluation is indirect.** There is no validation accuracy for "did the representation get better";
  you evaluate by probing or by downstream transfer.

## What an interviewer digs into next

* Why is next-token prediction a denser signal than masked language modelling?
* Why does MAE mask 75% while BERT masks 15%?
* How does BYOL avoid collapse without negatives?
* What replaced labels as the bottleneck once labels were unlimited?
