---
id: "153"
slug: speech-to-speech-translation
style: serious
category: translation
difficulty: advanced
question: "How do you translate speech into speech while keeping the speaker's voice?"
tags: [s2st, voice-preservation, cascade, discrete-units, prosody-transfer, consent]
---

# Speech-to-speech translation

The goal is audio in, audio out, across languages — and increasingly with the **original speaker's
voice** preserved. Each of those requirements pulls against the others.

## The pipeline, and what each stage costs

```
   CASCADE          audio ─► ASR ─► text ─► MT ─► text ─► TTS ─► audio
                                     ▲              ▲
                         speaker identity dies   prosody dies
                         here, and every         here, and the TTS
                         later stage is blind    invents new prosody
                         to what was lost        from nothing

   DIRECT           audio ─► encoder ─► discrete units ─► vocoder ─► audio
                    voice and prosody can be carried through, if the
                    representation keeps them (question 138)
```

Cascades still dominate production because each stage trains on far more data than any end-to-end
system has. Direct S2ST (Translatotron-style, or speech-unit models like SeamlessM4T) trains
against discrete speech units as the target instead of text, which lets the output carry prosody
the text never encoded.

## Voice preservation is a design decision, not a feature

Three levels, and it is worth being explicit about which you are building:

* **Generic voice.** Any TTS voice, matched only for language. Simplest, and it makes the
  translation obviously a translation — which is sometimes exactly what you want.
* **Voice matching.** A voice with the speaker's rough characteristics (age, pitch range, gender
  presentation) but not their identity.
* **Voice cloning.** The output sounds like the speaker. Powerful, and it is a **consent and
  provenance problem before it is an engineering one** (question 138): the speaker must have agreed,
  the output should be watermarked, and the system must refuse voices it cannot verify.

Prosody transfer is a related but separate problem: carrying emphasis, pace and emotion across
languages where the prosodic systems differ. A flat translation of an emphatic sentence is a
mistranslation of it, and no text metric will notice.

## The specific hard parts

* **Length mismatch.** The translation may be much longer or shorter than the source utterance
  (question 144). For live translation this compounds with latency (question 143); for anything
  aligned to video it is a hard constraint (question 154).
* **Errors compound across three stages.** An ASR error becomes a confident mistranslation becomes
  fluent, well-articulated nonsense. Nothing downstream can detect it, because each stage trusts its
  input.
* **Disfluency.** Real speech has restarts and fillers. Translating them literally is wrong;
  deleting them silently can remove meaning (a hesitation before "yes" is information).
* **Code-switching** within an utterance (question 107) breaks systems that commit to one source
  language up front.

## Evaluation

Text metrics on the transcript are necessary and insufficient — they measure the middle of the
pipeline, not the product. Add:

* **ASR-BLEU / ASR-COMET**: transcribe the *output* audio and score that. Catches synthesis errors
  the text metrics cannot see, and inherits the ASR system's own errors, so report which ASR you
  used.
* **Speaker similarity** to the source, when voice preservation is claimed.
* **Naturalness (MOS)** by human listeners.
* **Latency**, always, for anything live (question 143).

## What an interviewer digs into next

* What exactly does a cascade lose that a direct system can keep?
* Why score the output audio rather than the intermediate text?
* Why is voice cloning a consent problem before an engineering one?
* How does length mismatch interact with live latency?
