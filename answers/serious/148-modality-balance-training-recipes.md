---
id: "148"
slug: modality-balance-training-recipes
style: serious
category: multimodal
difficulty: advanced
question: "How do you balance modalities when training a multimodal model?"
tags: [data-mixture, curriculum, forgetting, stage-training, ablation, loss-weighting]
---

# Balancing the training mixture

The data mixture is the least-published and most consequential part of any multimodal recipe. It is
also where the most expensive mistakes get made, because a bad mixture produces a model that is
worse at something you were not measuring.

## The stages, and why there are stages

```
   STAGE 1  ALIGNMENT       vision frozen, LLM frozen, train the connector only
                            data: image-caption pairs
                            goal: teach the projector to speak the LLM's language

   STAGE 2  PRETRAINING     unfreeze the LLM (and often the top vision blocks)
                            data: interleaved documents + captions + OCR + text-only
                            goal: broad multimodal capability

   STAGE 3  INSTRUCTION     high-quality curated instruction data, small and clean
                            data: multimodal instructions + text-only instructions
                            goal: following visual instructions, not just describing
```

Collapsing these into one stage is the classic error. Training the connector while the LLM is also
moving means the LLM adapts to a projector that is itself garbage, and both end up worse than if
you had done it in order.

## The mixture, and the ratio nobody publishes

| Component | What breaks without it |
| --- | --- |
| Caption pairs (recaptioned, question 146) | attribute binding, precise grounding |
| Interleaved documents (question 124) | multi-image reasoning, in-context learning |
| **Text-only** | **language ability, measurably** |
| OCR / document / chart data | anything with text in the image |
| Grounding data (boxes, referring expressions) | pointing, spatial relations |

**Text-only data is the one people cut and regret.** Train a multimodal stage without it and
text-only benchmarks fall — often by several points — while every multimodal number goes up. If you
are not measuring text-only performance during multimodal training, you are not measuring the cost
of what you are doing.

Typical text-only fractions in published recipes run from 20% to 50% of the multimodal stages. That
is a wide range because it depends on how far you are pushing the LLM, and it is worth ablating
rather than copying.

## Resolution and length curricula

Train at low resolution first and raise it late. High resolution is quadratically expensive
(question 121), and most of what the model needs to learn — objects, relations, instruction
following — is learnable at 336px. Reserve the expensive high-resolution stage for the end, and for
the data that needs it (documents, charts).

The same logic applies to video frame counts and audio length: start short, extend late.

## Loss weighting and token accounting

Two traps:

* **Long sequences dominate.** If loss is averaged per token, a 4,000-token document contributes 40x
  what a 100-token caption does. Decide deliberately whether you want per-token or per-example
  weighting; the default is rarely what you meant.
* **Image tokens should usually not be predicted.** Mask the loss on image-token positions in
  projection-style models; training the LLM to predict patch embeddings is wasted capacity and
  distorts the objective.

## Ablate, and ablate at small scale

Mixture decisions are the highest-leverage and cheapest thing to ablate: they need no architecture
change and small models rank mixtures roughly as larger models do. Run the mixture sweep at 1B
before committing 70B-scale compute to a guess.

**Always evaluate the whole surface after every mixture change** — text-only, each multimodal
category, and instruction following. A mixture change that improves your headline number and
silently costs three points of text reasoning is a bad trade you will discover months later.

## What an interviewer digs into next

* Why train the connector before unfreezing the LLM?
* What happens to text-only performance during multimodal training, and why?
* Why is a resolution curriculum worth the complexity?
* Why is per-token loss averaging a trap in a mixed corpus?
