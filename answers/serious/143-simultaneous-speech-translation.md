---
id: "143"
slug: simultaneous-speech-translation
style: serious
category: translation
difficulty: advanced
question: "How does simultaneous speech translation work, and why is it hard?"
tags: [speech-translation, simultaneous, wait-k, latency, word-order, re-translation]
---

# Simultaneous speech translation

Offline speech translation has the whole utterance. **Simultaneous** translation must emit output
while the speaker is still talking, which turns it from a quality problem into a **quality-latency
trade-off** with no free lunch anywhere on the curve.

## Why waiting is sometimes mandatory

```
   German (verb-final):  "Ich habe das Buch, das mir mein Bruder gab, ... gelesen."
                          I  have the book  that to-me my  brother gave    READ
                                                                            ▲
                          the verb — the thing the whole sentence is about —
                          arrives LAST. You cannot begin the English clause
                          without it, or you must guess and risk retracting.
```

Word-order divergence is the fundamental obstacle. English-to-French can be translated almost
monotonically. Japanese-to-English or German-to-English cannot: the target's early words depend on
the source's late words. **No policy makes this go away**; it can only be traded against delay or
against the risk of a wrong guess.

## Read-write policies

The system alternates READ (consume more source) and WRITE (emit target). The policy decides which.

* **wait-k.** Read k source words, then alternate one-for-one. Trivially simple, no training
  needed, and a surprisingly strong baseline. k is the whole quality-latency dial.
* **Adaptive policies** (MMA, monotonic attention, or an LLM asked "do you have enough to commit?")
  wait longer at genuinely ambiguous points and less elsewhere. Better on the curve, more complex.
* **Re-translation.** Retranslate the whole prefix every time new audio arrives and overwrite the
  display. Quality is near-offline. The cost is **flicker** — text changing after the reader has
  read it — which is acceptable on a screen and impossible in speech output. Measure flicker
  explicitly, not just latency.

## Cascaded versus end-to-end, again

Cascaded (ASR → MT) is easy to build and compounds three problems: ASR errors propagate as
confident nonsense, segmentation into "sentences" is itself a hard decision made with no future
context, and latency stacks. End-to-end speech translation avoids the intermediate commitment and
keeps prosody, which disambiguates (questions 125, 138). Cascades remain common because ASR and MT
components are separately trainable on far more data.

**Segmentation is underrated.** Spontaneous speech has no sentence boundaries; the system must
invent them, in real time, and a boundary in the wrong place is a mistranslation that no downstream
component can fix.

## Measuring it: two numbers, always together

Quality alone is meaningless here. Report a quality metric **and** a latency metric, as a curve:

* **AL (Average Lagging)** — how far behind an ideal simultaneous speaker the system is, in words
  or milliseconds. The standard.
* **AP** (average proportion) and **DAL** (differentiable average lagging) as alternatives with
  different pathologies.
* **Computation-aware latency**, which includes actual inference time. A policy that looks fast on
  paper and runs a 70B model per token is not fast.

A system reported with quality only should be assumed to be waiting for the end of the utterance.

## Practical realities

* **Speaker overlap and disfluency.** Real speech has restarts, "um", corrections. A model trained
  on clean read speech falls apart.
* **Terminology in real time.** Names and jargon must be right on first emission, because there is
  no editing pass (question 133).
* **Numbers are the classic disaster.** "Twenty-five thousand" arrives across several words and
  changes meaning as it completes. Committing early to "twenty" is a real failure mode with real
  consequences in medical and financial settings.
* **Human interpreters do not do this either.** They chunk, summarise, and use their knowledge of
  the domain to predict. Expecting word-level fidelity at zero latency is expecting something no
  professional interpreter delivers.

## What an interviewer digs into next

* Why does word order make some language pairs fundamentally harder to do simultaneously?
* What is wait-k, and why is it a strong baseline despite its simplicity?
* Why must latency and quality always be reported together?
* Why is re-translation acceptable on a screen and not in audio?
