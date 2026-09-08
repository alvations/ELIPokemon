---
id: "173"
slug: audio-and-music-generation
style: serious
category: multimodal
difficulty: advanced
question: "How is audio and music generated, and what makes it harder than images?"
tags: [music-generation, audio-codecs, long-range-structure, tts, rights, evaluation]
---

# Generating audio and music

Audio generation shares its machinery with image generation (question 137) and differs on one axis
that changes everything: **the ear is far less forgiving of structural error than the eye is.**

A visually implausible region of an image is a flaw you may not notice. A note out of key, a beat
that slips, or a voice that changes identity mid-sentence is **immediately and unambiguously wrong**
to any listener, trained or not.

## The two representations

```
   DISCRETE TOKENS (codec)              CONTINUOUS (spectrogram / waveform diffusion)
   ───────────────────────              ────────────────────────────────────────────
   audio ─► RVQ codec ─► integers       audio ─► mel spectrogram ─► diffuse ─► vocoder
        ─► language model over them
                                        no tokenizer, no codebook loss;
   reuses all LLM machinery;            harder to condition on symbolic structure
   quantisation is a quality floor
```

Codec-token models (MusicGen, AudioLM lineage) dominate because they inherit transformer scaling
and conditioning. Diffusion approaches (Stable Audio and relatives) reach high fidelity and are
strong for fixed-duration generation. Both are now common; the choice is mostly about whether you
need language-model-style conditioning and streaming.

## Why long-range structure is the hard problem

Music has structure at several timescales simultaneously: timbre at milliseconds, rhythm at
hundreds of milliseconds, phrases at seconds, and **form** — verse, chorus, return — at minutes. A
model with a few thousand tokens of context at 50 Hz across 8 codebooks sees a handful of seconds.

The result is the characteristic failure: locally excellent, globally aimless. It wanders, never
returns to the theme, and stops rather than ends. Mitigations mirror question 157's long-video
problem — hierarchical generation (structure first, then audio), longer context, and conditioning on
an explicit plan — and they help without solving it.

## Speech generation is a different job

TTS shares the codec machinery and is judged differently: intelligibility, speaker similarity, and
prosodic appropriateness (question 138). The frontier is **controllability** — asking for an
emotion, a pace, an emphasis — rather than raw fidelity, which is largely solved.

Everything in question 153 about voice cloning consent applies here with more force, because
generating a voice from a text prompt has no source speaker to have consented at all.

## Rights are not a footnote here

Music generation sits on top of an actively litigated question about training data. Practical
positions a serious team should hold:

* Know your training data's provenance and licensing. "It was on the internet" is a position, and
  it is one you will have to defend.
* **Artist style prompting** ("in the style of X") is the sharpest edge — legally in several
  jurisdictions and ethically everywhere. Many providers block named-artist prompts for this reason.
* Watermark outputs (question 166); audio watermarking is comparatively robust and this is the case
  that most needs it.
* Support opt-out and, better, licensed corpora with revenue share.

## Evaluation

Automatic measures (FAD, the audio analogue of FID) have the same weaknesses as FID plus poor
sensitivity to structure — the failure that matters most. Report:

* **Human listening tests** for overall quality and for prompt adherence, separately.
* **Structural probes**: does a theme return? Is the tempo stable? Is the key consistent?
* **Speaker/instrument consistency** across the clip's duration.
* For speech: intelligibility (WER through an ASR system) alongside naturalness.

## What an interviewer digs into next

* Why is the ear less forgiving of structural error than the eye?
* Why do codec-token models dominate over diffusion for music?
* What causes the wandering failure, and what actually helps?
* Why is FAD insensitive to the failure that matters most?
