---
id: "138"
slug: speech-language-models
style: serious
category: multimodal
difficulty: advanced
question: "How do you build a model that listens and speaks, rather than reads and writes?"
tags: [speech-llm, audio-tokens, cascaded, end-to-end, duplex, prosody, voice-cloning]
---

# Speech-in, speech-out language models

Two architectures, and the choice determines what the system can and cannot do far more than model
size does.

## Cascaded versus end-to-end

```
   CASCADED
   audio ─► ASR ─► TEXT ─► LLM ─► TEXT ─► TTS ─► audio
                     ▲                ▲
              everything not in the words is destroyed here,
              and cannot be recovered downstream

   END-TO-END
   audio ─► audio encoder ─► LLM (audio + text tokens) ─► audio decoder ─► audio
                     ▲
              tone, emphasis, hesitation, emotion, overlapping speakers,
              accent and background all survive into the reasoning
```

Cascaded is easy to build from parts you already have, easy to debug (you can read the transcript),
easy to moderate (screen the text), and it **throws away everything that is not words**. Latency
compounds across three models, typically 1-3 seconds before the first sound comes back.

End-to-end keeps the paralinguistics — *how* something was said — and can respond in kind. It is
harder to train, harder to inspect, and harder to make safe, because the thing you must moderate is
no longer text.

## How audio becomes tokens

The LLM needs a discrete sequence. Neural audio codecs (SoundStream, EnCodec, DAC) provide it via
**residual vector quantisation**: quantise the encoder output against a codebook, quantise the
*residual* against a second codebook, and so on for 8-32 layers.

Two token families matter and are frequently confused:

* **Semantic tokens** — derived from self-supervised speech models (HuBERT, w2v-BERT). Carry
  *what was said*. Low rate, good for language modelling.
* **Acoustic tokens** — from the codec. Carry *how it sounded*: speaker identity, prosody, room.
  High rate, necessary for reconstruction.

Most systems model semantic tokens with the LLM and use acoustic tokens for synthesis, because
modelling everything at acoustic rate is prohibitively long. The frame rate is the design
constraint: 50 Hz across 8 codebooks is 400 tokens per second of audio, so a one-minute exchange is
24,000 tokens before anyone has said anything interesting.

## Duplex conversation is the hard part

Real conversation is not turn-taking with clean boundaries. It has interruption, backchannels
("mm-hm"), overlap, and silences that mean something.

A half-duplex system waits for you to stop, decides, then speaks. A **full-duplex** system models
listening and speaking simultaneously — a continuous stream where the model may emit silence or
speech at every frame, and keeps listening while it talks. That is what makes interruption work,
and it changes the training objective: the model must learn *when* to speak, not just what to say.

**Latency budget** is the whole user experience. Humans notice above roughly 300 ms of gap. That
budget must cover encoding, the LLM's first token, and vocoding — which is why streaming decoders
and small-first-chunk synthesis matter more here than raw quality.

## Safety, specifically

* **Voice cloning.** Modern systems clone a voice from seconds of audio. Consent, watermarking, and
  refusal to clone without verification are baseline requirements, not features.
* **Moderation moves.** In a cascade you screen text. End-to-end, harmful content may never exist
  as text, so you need audio-domain classification or an internal transcript path purely for
  safety.
* **Speaker inference.** Audio leaks age, gender, health, region and emotional state. A system that
  infers and acts on those is making decisions nobody asked it to make.

## Evaluation

WER on the ASR path is necessary and wildly insufficient — it measures the words and this whole
architecture exists for what is not the words. Add: **latency distribution** (p50 and p95 to first
sound), **interruption handling**, **prosodic appropriateness**, **speaker consistency** across a
session, and **MOS-style human listening tests**. Report the gap between cascaded and end-to-end on
tasks where tone carries the meaning — sarcasm, questions marked only by intonation, emotional
support — because that is the only place the extra complexity pays for itself.

## What an interviewer digs into next

* What exactly does a cascade destroy, and can any downstream stage recover it?
* Why separate semantic from acoustic tokens?
* What changes in the training objective for full-duplex?
* Why is text moderation insufficient for an end-to-end system?
