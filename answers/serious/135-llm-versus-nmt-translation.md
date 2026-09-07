---
id: "135"
slug: llm-versus-nmt-translation
style: serious
category: translation
difficulty: intermediate
question: "When should you use an LLM for translation instead of a dedicated NMT model?"
tags: [nmt, llm, mbr, quality-aware-decoding, latency, cost, controllability]
---

# LLMs versus dedicated NMT systems

Classical NMT is a small encoder-decoder trained on parallel data for one direction or one
multilingual family. An LLM is a large decoder-only model that translates because translation is
in its pretraining distribution and its instructions. They fail differently, and the choice is a
systems decision, not a quality ranking.

## Where each one wins

| | Dedicated NMT | LLM |
| --- | --- | --- |
| Cost per segment | very low | 10-100x higher |
| Latency | tens of ms | hundreds of ms to seconds |
| Determinism | high | lower; sampling and version drift |
| Document context | weak (sentence-trained) | strong — the whole document fits |
| Style / register control | needs retraining | ask for it in the prompt |
| Terminology | needs constrained decoding | ask, plus check (question 133) |
| Low-resource pairs | poor without data | often better, via transfer from related languages |
| Off-target output | rare | a real failure mode (question 136) |
| Length control | trainable | poor |
| Explaining a choice | impossible | free |

The honest summary from recent WMT general MT evaluations: **strong LLMs match or beat dedicated
systems on high-resource pairs into English, the gap narrows or reverses out of English, and
dedicated systems remain competitive where throughput and cost dominate.** Anyone claiming a clean
victory in either direction is selling something.

## The architectural asymmetry that explains most of it

```
   NMT (encoder-decoder)                     LLM (decoder-only)
   ─────────────────────                     ──────────────────
   source ─► ENCODER ─┐                      [instruction][source] ─► one stack ─► output
                      ├─► DECODER ─► target
   target prefix ─────┘                      the source is just... earlier tokens

   the source has its own bidirectional      no architectural distinction between
   representation, attended to at every      "what I must be faithful to" and
   decoding step                             "what I have already written"
```

That missing distinction is why LLMs drift, embellish, answer the source instead of translating
it, and occasionally continue in the wrong language. It is also why they use document context so
well: there is nowhere for context to *not* reach.

## Making an LLM translate well

* **Give it the document, not the sentence.** This is the single biggest advantage and it is free
  (question 131).
* **Few-shot with retrieved examples** from a translation memory (question 134).
* **State the target variant explicitly** — "European Portuguese", "Simplified Chinese",
  "formal register" — rather than hoping.
* **Quality-aware decoding.** Sample n candidates and pick the best by a QE model or by **MBR
  decoding** (choose the candidate with highest average similarity to the others, under a utility
  like COMET). This is a large, reliable gain and it costs n forward passes — the standard way to
  buy quality with compute here.
* **Fine-tune a mid-size model for translation specifically.** ALMA-style recipes — continued
  pretraining on target-language monolingual text, then fine-tuning on a small amount of very
  high-quality parallel data — get close to frontier translation quality at a fraction of the
  serving cost. This is usually the right answer for a production translation product.
* **Constrain the output format.** Ask for the translation and nothing else; LLMs add preambles,
  notes and apologies, and downstream systems break on them.

## Production reality

Most serious deployments are **hybrid**: a fast NMT system for the bulk, quality estimation
(question 132) to detect segments it handled badly, and an LLM for those plus anything needing
document context, style or terminology reasoning. That routing is where the cost-quality curve
actually bends, and it is more effective than either system alone.

Also budget for **non-determinism**: an LLM's output changes across model versions in ways an NMT
checkpoint does not. If you have approved translations in a compliance workflow, pin the version
and re-validate on upgrade.

## What an interviewer digs into next

* Why does the decoder-only architecture make faithfulness harder?
* What is MBR decoding, and what does it cost?
* Why do LLMs handle document context so much better?
* How would you design a hybrid system, and what routes what?
