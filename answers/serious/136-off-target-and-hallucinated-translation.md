---
id: "136"
slug: off-target-and-hallucinated-translation
style: serious
category: translation
difficulty: advanced
question: "Why do translation systems output the wrong language or invent content?"
tags: [off-target, hallucination, zero-shot, language-tags, detection, oscillatory]
---

# Off-target output and hallucination in translation

Two failures that look like bugs and are consequences of how the systems are built. Both are rare
in aggregate and unacceptable individually, which makes them evaluation problems as much as
modelling ones.

## Off-target: translating into the wrong language

The output is fluent, correct-ish, and in Spanish when you asked for Catalan.

**Where it comes from:**

* **Zero-shot directions in multilingual models.** Train on X-English and English-Y pairs, ask for
  X-Y, and the model has never been supervised on that direction. It frequently emits English —
  the pivot it was actually trained through (question 130).
* **Weak language control.** A target-language tag is one token competing with thousands of tokens
  of source. In LLMs the "tag" is an instruction, which is even weaker.
* **Related-language bleed.** Catalan drifts to Spanish, Ukrainian to Russian, Urdu to Hindi,
  Afrikaans to Dutch. The model has far more data in the dominant relative and falls into it.
* **Dirty training data.** Pairs mislabelled by an upstream language identifier (question 108)
  teach the model that this tag sometimes means that language.

```
   source (Basque) ──► [ tag: eu ] ──► model ──► output in Spanish
                            ▲                          ▲
                     one token of control      thousands of Spanish-adjacent
                                               training signals pulling this way
```

**Detection is cheap and everyone should do it:** run language identification on every output and
alarm on mismatch. It is one of the highest-value guards in a multilingual pipeline and it is
frequently absent.

**Mitigation:** filter training data with LID on both sides; add explicit target-language tags on
both encoder and decoder side; include some genuinely direct (non-English-pivoted) data for the
pairs you care about; lower the sampling temperature; and, at serving time, retry with a stronger
instruction when LID flags a mismatch.

## Hallucination: fluent content with no source

Output that is well-formed target-language text bearing little or no relation to the input.

**Two distinct shapes:**

* **Detached hallucination** — a fluent, plausible sentence about something else entirely.
* **Oscillatory hallucination** — repeated n-grams, a phrase looping, degenerate repetition.
  Visually obvious and trivially detectable by a repetition check.

**Triggers**, in rough order of how often they cause it in practice:

* **Out-of-distribution or noisy source.** Garbage in, fluent garbage out. Perturbed, misspelled or
  wrong-script input is the classic trigger.
* **Very short segments.** A single word or a UI label gives almost nothing to condition on.
* **Low-resource directions**, where the model's source-side representation is weak and the
  language-model prior takes over — the same mechanism as visual hallucination in question 122.
* **Domain shift** at inference.
* **Corpus noise** — misaligned pairs in training teach the model that unrelated output is
  acceptable.

**Detection:**

* **Reference-free QE** (question 132), which is what it is for.
* **Source-attention mass.** A hallucinating model attends weakly to the source; methods like
  ALTI+ measure source contribution directly, and low source contribution is a strong signal.
* **Repetition detectors** for the oscillatory kind.
* **Round-trip translation** as a cheap heuristic — noisy, but catches gross detachment.
* Note that **sequence log-probability is a poor detector**: hallucinations are fluent, so the
  model is confident. This is the same trap as in question 122.

**Mitigation:** clean the training corpus (LID + alignment filtering are the biggest levers), avoid
beam search with very large beams (which correlates with hallucination in NMT), cap repetition at
decode time, and gate on QE with a fallback to a second system rather than publishing.

## Why the aggregate metric will not save you

Both failures are rare. A system that hallucinates on 0.5% of segments loses a fraction of a COMET
point and is unshippable in any context where someone acts on the output. **Report them as
counts and rates with their own targets**, exactly as with critical errors in question 132 — never
as part of a mean.

## What an interviewer digs into next

* Why do zero-shot directions produce English specifically?
* Why is log-probability a poor hallucination detector?
* What is oscillatory hallucination, and why is it the easy case?
* How would you set an alarm for off-target output in production?
