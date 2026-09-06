---
id: "125"
slug: speech-recognition
style: serious
category: multimodal
difficulty: intermediate
question: "How does modern speech recognition work?"
tags: [asr, whisper, ctc, rnn-t, log-mel, wer, streaming]
---

# Modern speech recognition

Speech is a waveform: 16,000 numbers per second, carrying words, speaker identity, emotion, room
acoustics and noise all superimposed. ASR is the problem of extracting only the first of those.

## The front end: audio becomes an image

Almost nothing operates on raw samples. The standard front end turns audio into a **log-mel
spectrogram** — a 2D array of energy by frequency and time — and from there the problem looks like
the vision problems in questions 117-118.

```
   waveform     ~~~/\~~/\/\~~~~~~~~~~/\/\~~~     16 kHz samples
        │
        ├─ 25 ms windows, 10 ms hop  ──►  100 frames per second
        ├─ FFT ──► power spectrum
        ├─ mel filterbank (80 bins, spaced by perceived pitch, not Hz)
        └─ log
                          freq ▲  ░░▓▓██▓░░  ░▓██▓░   ░░▓▓░
                            80 │  ░▓███▓░░  ▒▓██▓▒   ░▓██▓░
                           bins│  ▓██▓░     ░▓█▓░     ▓██░
                               └──────────────────────────► time
```

Mel spacing is the one piece of human-perception prior left in an otherwise learned pipeline:
frequency resolution is fine at low pitches and coarse at high ones, matching the ear.

## Three output architectures

The hard part is **alignment** — 3000 audio frames must become perhaps 40 tokens, and nothing tells
you which frames produced which token.

| | How it aligns | Streaming? | Language model |
| --- | --- | --- | --- |
| **CTC** | emits a token or a blank per frame, then collapses repeats | yes, natively | none — conditionally independent outputs |
| **RNN-T (transducer)** | joint network over audio + prediction network | yes — the production default on devices | built in, small |
| **Encoder-decoder (Whisper)** | cross-attention learns alignment implicitly | no, needs the full window | full autoregressive decoder |

CTC's conditional independence is its weakness: it cannot model that "recognise" follows "speech"
more often than "recognize" does, so it is usually paired with an external LM at decode time.
RNN-T fixes that while staying streamable, which is why it runs on phones. Encoder-decoder models
give the best accuracy on complete utterances and cannot start emitting until the audio ends.

## Whisper-style training and its consequences

Whisper's contribution was scale and task formatting: 680k hours of weakly-supervised web audio,
with the task specified by **special tokens in the decoder prompt** — language, transcribe versus
translate, timestamps or not. One model, many tasks, no task-specific heads.

The consequences are worth knowing:

* **It hallucinates on silence and noise.** An autoregressive decoder trained on speech will
  produce fluent text from a segment that contains none — commonly a subtitle-farm artefact like
  "Thank you for watching". Mitigate with voice activity detection before the model, no-speech
  probability thresholds, and repetition detection.
* **Long audio is chunked**, so errors at chunk boundaries compound through the sequential
  conditioning.
* **Timestamps are approximate**, because alignment is implicit. Forced alignment afterwards is
  more accurate if you need word-level timing.

## Evaluation

**WER** = (substitutions + insertions + deletions) / reference words. Report it, but know its
faults: it weights every word equally, so "not" and "the" cost the same; it punishes
formatting/normalisation differences unless you normalise both sides; and it is unbounded above,
because insertions have no cap. For multilingual work use **CER** on scripts without word
boundaries (question 114).

Always break WER down by **accent, speaker, noise condition and domain**. An aggregate WER of 8%
routinely hides 25% on accented speech — a fairness problem, not just an accuracy one.

## Adjacent problems people conflate with ASR

* **Diarization** ("who spoke when") is a separate system.
* **Punctuation and casing** are usually a separate post-processing model, or absent.
* **Language identification** on the audio itself (question 108's problem, one modality over).

## What an interviewer digs into next

* Why does CTC need an external language model?
* Why can't an encoder-decoder ASR model stream?
* Why does Whisper hallucinate on silence, mechanistically?
* What does an aggregate WER hide?
