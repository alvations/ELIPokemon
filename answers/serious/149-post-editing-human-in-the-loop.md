---
id: "149"
slug: post-editing-human-in-the-loop
style: serious
category: translation
difficulty: intermediate
question: "How does machine translation post-editing work, and what does it cost?"
tags: [post-editing, hter, post-editese, anchoring, transcreation, feedback-loop]
---

# Post-editing: humans fixing machine output

Almost all professional translation now starts from machine output. The translator's job has
shifted from producing text to **repairing it**, and that shift has consequences that are
frequently underestimated.

## The workflow

```
   source ─► MT ─► QE score (question 132)
                        │
        ┌───────────────┼───────────────┐
     high            medium            low
        │               │               │
   publish        light post-edit   full post-edit,
   (or spot-check)  (fix errors)    or discard and translate fresh
                        │
                        └──► edits captured ──► training data / TM (question 133)
```

Two levels are conventionally distinguished. **Light post-editing** fixes what is *wrong* —
mistranslation, terminology, grammar — and tolerates clumsiness. **Full post-editing** aims for
publishable quality indistinguishable from human translation. They are different jobs, priced
differently, and confusing them in a brief is the most common source of dispute.

## Measuring effort

**HTER** (Human-targeted Translation Edit Rate) is edit distance between the MT output and the
post-edited version, normalised by length. It is the standard proxy for effort and it is a proxy:
it counts keystrokes, not thought. A single word change that required reading the whole document to
get right scores as one edit; reformatting a sentence scores as many.

Better measures of actual effort: **time per word** (the thing being paid for), **pauses** and
keystroke telemetry, and translator-reported cognitive load. Productivity gains from post-editing
are real — commonly 20-60% for suitable content — but they vary enormously by language pair, domain
and MT quality, and reporting a single number across a programme hides the pairs where post-editing
is *slower* than translating fresh.

## Two effects people miss

**Post-editese.** Post-edited text carries fingerprints of the machine: it is more literal, uses
simpler syntax, and mirrors the source's structure more closely than a from-scratch translation
would. It is measurably distinguishable from human translation. This matters when the output is
itself training data — you are training the next model on text shaped by the previous one — and it
matters for anything where style is the product.

**Anchoring.** A translator shown a fluent wrong translation is measurably less likely to
restructure the sentence than one starting from blank. The machine's framing constrains the human's
thinking. This is why "just post-edit it" is bad advice for creative work: you are not getting a
human translation with fewer errors, you are getting a machine translation with the errors removed.

## When not to post-edit

* **Marketing and creative copy.** The right process is **transcreation** — recreate the intent for
  the target audience, which may share no sentences with the source. Post-editing produces literal,
  lifeless copy that technically says the right thing.
* **Very low MT quality.** Below some threshold, editing is slower than translating fresh.
  Translators know where that line is; QE (question 132) can route around it, and asking translators
  where the line sits for their pair is cheaper than discovering it in throughput data.
* **High-stakes content with critical-error exposure** — where a missed negation is unacceptable,
  the process needs independent review, not editing of a draft that primes the reviewer.

## Closing the loop

Post-edits are the highest-quality training signal you will ever get: real errors, corrected by
experts, in your exact domain. Capture them into a translation memory (question 133) and into
fine-tuning data. Two cautions: this creates a feedback loop that can amplify post-editese, and
consent and compensation for using translators' work as training data is an ethical and often
contractual matter, not a technical detail.

## What an interviewer digs into next

* Why is HTER a proxy rather than a measure of effort?
* What is post-editese, and why does it matter for a training pipeline?
* Why is post-editing the wrong process for marketing copy?
* When is post-editing slower than translating from scratch?
