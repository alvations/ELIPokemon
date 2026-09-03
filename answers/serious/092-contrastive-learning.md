---
id: "092"
slug: contrastive-learning
style: serious
category: training
difficulty: intermediate
question: "What is contrastive learning? Explain InfoNCE and CLIP."
tags: [contrastive, infonce, clip, simclr, negatives, collapse]
---

# Contrastive learning

Learn representations by pulling **positive pairs** together and pushing **negatives** apart, without
any class labels. The supervision comes from knowing which things *should* be similar.

$$\mathcal{L}_{\text{InfoNCE}} = -\log\frac{\exp(\text{sim}(z_i, z_j)/\tau)}
{\sum_{k=1}^{2N}\mathbb{1}_{[k\neq i]}\exp(\text{sim}(z_i,z_k)/\tau)}$$

This is exactly a **cross-entropy over the batch**: given anchor `i`, classify which of the `2N−1`
candidates is its positive. That framing makes the design choices obvious — it is a classification
problem whose difficulty you control.

## The three levers

**1. What counts as a positive.**

| Method | Positive pair |
| --- | --- |
| SimCLR / MoCo | two augmentations of the same image |
| CLIP | an image and its caption |
| Sentence embeddings | a query and a passage that answers it |
| SimCSE | the same sentence passed twice through dropout |

**2. Negatives.** Random negatives are trivially separable and teach little; **hard negatives** —
similar but wrong — are what force fine distinctions and are the main quality lever in practice
(question 043). In-batch negatives are free, which is why batch size matters so much: SimCLR needed
batches of 4096–8192, and MoCo's contribution was a momentum-updated **queue** of negatives that
decouples the negative count from the batch size.

**3. Temperature `τ`.** Controls how sharply the loss concentrates on the hardest negatives. Small `τ`
(0.05–0.1) is aggressive; too small and training destabilises. This is a genuinely sensitive
hyperparameter, not a formality.

## Why augmentation choice is decisive

For SimCLR, the augmentation defines what invariances the representation learns — you are literally
telling the model "these two things should be the same". Random crop + colour jitter was essential;
**colour jitter in particular**, because without it the model can match two crops by their colour
histogram alone and learn nothing else. Every contrastive method's core design question is *what
shortcut can the model take to solve this too easily?*

## CLIP

[CLIP](https://arxiv.org/abs/2103.00020) trains an image encoder and a text encoder jointly on 400M
web (image, caption) pairs, contrasting across a batch:

```
              text embeddings →
              T₁    T₂    T₃    T₄
          ┌─────┬─────┬─────┬─────┐
   I₁     │ ✅  │  ✗  │  ✗  │  ✗  │   maximise the diagonal,
   I₂     │  ✗  │ ✅  │  ✗  │  ✗  │   minimise everything else
   I₃     │  ✗  │  ✗  │ ✅  │  ✗  │
   I₄     │  ✗  │  ✗  │  ✗  │ ✅  │   loss is symmetric:
          └─────┴─────┴─────┴─────┘   image→text AND text→image
```

The result is a **shared embedding space**, which enables zero-shot classification: embed the class
names as "a photo of a {class}", embed the image, take the nearest. No training on the target
classes at all. CLIP's encoders became the backbone for text-to-image generation and for most
vision-language models.

## Collapse, and the methods that avoid negatives

The trivial solution is to map everything to one point — every pair is then "similar". Negatives
prevent this, which is why they were thought essential.

**BYOL** and **DINO** removed them and still avoided collapse, using asymmetry instead: an
exponential-moving-average teacher, a predictor head on the student only, and stop-gradient. **VICReg**
and **Barlow Twins** take another route, adding explicit variance and decorrelation terms to the loss.
That negatives turned out to be optional was one of the more surprising results in the area.

## What an interviewer digs into next

* Why is InfoNCE a cross-entropy loss, and over what?
* Why does batch size matter so much, and how does MoCo sidestep it?
* Why was colour jitter specifically necessary in SimCLR?
* How does BYOL avoid collapse without negatives?
