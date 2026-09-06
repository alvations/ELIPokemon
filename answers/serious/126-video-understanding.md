---
id: "126"
slug: video-understanding
style: serious
category: multimodal
difficulty: advanced
question: "How do you extend a vision-language model to video?"
tags: [video, frame-sampling, temporal, token-budget, long-context, needle-in-haystack]
---

# Video in a vision-language model

A video is images plus **time**. Both halves cause trouble: the images arrive in industrial
quantities, and the ordering between them carries meaning that per-frame processing throws away.

## The token budget is the design constraint

```
   3-minute clip at 30 fps               =  5,400 frames
   at 576 tokens per frame               =  3.1 million tokens        ✗ impossible

   sample 1 fps                          =    180 frames
   pooled to 64 tokens per frame         =  11,520 tokens             ✓ feasible
   plus a few frames at full detail      =  +1,700 tokens             ✓ where it matters
```

Everything in video modelling is a way of spending a fixed token budget well. The levers:

* **Frame rate.** 1 fps is the common default. Fine for "what is happening"; useless for anything
  fast — a hand gesture, a ball's trajectory, a UI click.
* **Spatial pooling per frame.** Frames are highly redundant with their neighbours, so each one
  can afford far fewer tokens than a standalone image. Pooling 576 to 64 is routine.
* **Temporal merging.** Merge tokens across adjacent frames when they barely change. Static shots
  compress enormously; a cut costs full price. This is where the real savings live.
* **Keyframe selection.** Detect shot boundaries, or select frames by relevance to the *query*
  before encoding. Query-aware selection is far more efficient and introduces a retrieval failure
  mode: if selection misses the frame with the answer, no amount of model quality recovers it.

## Making time mean something

Sampled frames spliced into a sequence give the model *what* but not reliably *when* or *in what
order*. Three approaches, cheapest first:

1. **Temporal position encoding.** Give each frame a timestamp embedding, or extend RoPE
   (question 002) to a third axis — as in M-RoPE, where height, width and time each get part of the
   dimension. Cheap and effective.
2. **Explicit textual timestamps.** Literally interleave "at 00:14" text tokens between frames.
   Crude, works surprisingly well, makes the model able to *cite* a time.
3. **Temporal attention layers.** Attention across frames at the same spatial position, in the
   vision tower. Most expensive, best at motion.

Without any of these the model degenerates into a bag-of-frames — which, notably, is enough to win
on several video benchmarks, and that says more about the benchmarks than the models.

## Evaluating video honestly

The dominant failure of video evaluation is that **many questions are answerable from one frame**.
If a benchmark's questions can be answered from a random still, it is measuring image
understanding with extra steps.

What to insist on:

* **Order-sensitive questions.** "Did she pick up the cup before or after opening the door?"
  Shuffle the frames as a control: a real temporal model should degrade, a bag-of-frames model
  will not.
* **Single-frame baselines, always reported.** The gap between the best single frame and the full
  video is the only honest measure of temporal gain.
* **Needle-in-a-haystack for long video.** Insert a frame containing the answer at a known
  position and sweep the position. Accuracy that falls off in the middle of the clip is the same
  lost-in-the-middle problem as long-context text (question 046).
* **Counting and repetition** ("how many times does he serve?") — nearly impossible for
  bag-of-frames, so a good diagnostic.

## Audio is half of video and usually discarded

Most "video" models see frames only. Speech (question 125), music and sound effects carry an
enormous share of the content — often *the* content, in instructional and conversational video.
A pipeline that transcribes audio and interleaves the transcript with sampled frames beats a
frames-only model on most real tasks, for a fraction of the compute.

## What an interviewer digs into next

* Why can frames afford fewer tokens each than a standalone image?
* How would you test whether a model uses temporal order at all?
* What breaks with query-aware keyframe selection?
* Why is a transcript-plus-frames pipeline such a strong baseline?
