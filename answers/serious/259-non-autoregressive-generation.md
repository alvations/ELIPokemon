---
id: "259"
slug: non-autoregressive-generation
style: serious
category: optimization
difficulty: advanced
question: "Non-autoregressive generation has been reinvented every few years since 2018. Why does the field keep returning to it, and why does it keep retreating?"
tags: [non-autoregressive, machine-translation, distillation, speculative-decoding, latency]
---

# The idea that keeps almost working

Non-autoregressive generation drops the conditioning between output positions: predict a length,
then emit every target token in one pass. It was born in machine translation, not in LLM serving —
[Gu et al. (2018)](https://arxiv.org/abs/1711.02281) reported about 15× faster decoding with a
clear BLEU loss — and it has come back roughly every three years since, each time with a better
trick and each time retreating for the same two reasons. The first is **the multimodality
problem**, which is a real property of the task. The second is **an unfair baseline**, which is a
property of how the field measured itself.

## The multimodality problem, exactly

The target distribution is multimodal: "Thank you", "Thanks a lot" and "Many thanks" are all
correct. An autoregressive model never has to choose between modes globally, because position 2 is
conditioned on position 1. Drop that conditioning and each position marginalises over all modes
independently.

```
  AUTOREGRESSIVE                         NON-AUTOREGRESSIVE (one pass)

  p(y2 | y1="Thank") -> "you"   0.95     p(y1) = Thank .45  Thanks .40  Many .15
  p(y2 | y1="Thanks") -> "a"    0.80     p(y2) = you   .45  a      .40  thanks .15
                                                  |            |
  the chain forbids the mixture           argmax each position, independently
                                                  v
       "Thank you"                          "Thank a"        <- fluent nowhere
```

The same defect shows up as token repetition and as dropped content. It is not a training bug; it
is what a product of marginals does to a multimodal joint. Everything that made NAT work is a way
of *reducing the multimodality* or *reintroducing some conditioning*.

## The recurring fixes, and what each one really admits

| Fix | What it does | What it concedes |
| --- | --- | --- |
| **Sequence-level distillation** (Gu 2018 onward) | Train on an AR teacher's outputs, not the real corpus | You need the serial model to exist before the parallel one can be trained |
| **Iterative refinement / Mask-Predict** ([Ghazvininejad 2019](https://arxiv.org/abs/1904.09324)) | Mask, predict all, re-mask the least confident, repeat `T` times | Serial steps come back; `T` is the dial you were trying to remove |
| **CTC-based NAT** (Libovický & Helcl 2018; Gu & Kong 2021) | Emit a longer blank-padded sequence and collapse it | Length prediction was doing more damage than anyone admitted |
| **Edit-based** (Levenshtein Transformer, 2019) | Insert and delete over several passes | The output is now a program of edits, not a single pass |
| **Glancing training** (GLAT, 2021) | Curriculum that feeds some gold tokens during training | Conditioning, smuggled in at training time |

The distillation line is the tell. **Sequence-level knowledge distillation is not an optimisation;
it is load-bearing.** It works because the teacher's outputs are far less multimodal than the real
data — the teacher has already picked one way to say it. A parallel model that can only be trained
on a serial model's preferences has not escaped serial modelling. It has moved it to training
time.

## Why it kept retreating

1. **The baseline was never tuned.** [Kasai et al. (2020)](https://arxiv.org/abs/2006.10369)
   showed that an ordinary autoregressive transformer with a deep encoder and a **one-layer
   decoder** matches NAT latency at better quality. Nearly all of the published speedup was
   against a 6-layer decoder nobody had tried to make fast.
2. **The speedups do not survive batching.** Helcl, Haddow and Birch's *Non-Autoregressive Machine
   Translation: It's Not as Fast as it Seems* (NAACL 2022) is the honest audit: parallel decoding
   wins at batch size one and loses most of its advantage once the GPU is saturated with a real
   queue. Batch-one latency is exactly the regime production systems try not to be in.
3. **The quality gap was measured with a forgiving metric.** BLEU is relatively tolerant of the
   specific errors NAT makes; under neural metrics and human evaluation the gap read wider.
4. **The teacher never left.** If you must train, distil from, and often rerank with an AR model,
   you are maintaining two systems to avoid running one.

## What actually won

Two things, and neither is "pure NAR".

**Speculative decoding** (questions 033, 215, 230) took the parallelism and refused the trade. A
cheap proposer — which may itself be a non-autoregressive drafter — proposes several tokens, and
the autoregressive model verifies them in one batched pass, accepting a prefix and resampling at
the first disagreement. The output distribution is provably the AR model's. The serial model keeps
its veto, and the parallelism is free because it was only ever a guess. This is where NAT research
actually shipped: as drafting.

**Masked diffusion language models** (question 258) are Mask-Predict with a principled training
objective, a scaling story and vastly more compute. Note the lineage: Mask-Predict's "predict all,
re-mask the least confident, repeat" is the same decoding loop, seven years earlier. Diffusion MT
is an active 2026 topic in its own right, and the open questions are the ones from 2018 — length,
and what happens when two positions are decided blind of each other.

Where NAR genuinely earns its place today: single-stream low-latency work, simultaneous and
streaming translation, on-device decoding with no batching to exploit, and short
highly-constrained outputs. Notice that these are all batch-size-one problems.

## What an interviewer digs into next

* Explain the multimodality problem without using the word "multimodality".
* Why does sequence-level distillation help, and why is that embarrassing?
* What is the fair latency baseline for a decoder, and what batch size are you measuring at?
* How does speculative decoding get the parallelism without the quality loss?

**Citation note.** The arXiv identifiers linked above are given from working knowledge.
`arxiv.org` is blocked from the environment this was written in, so **not one of them was
resolved while writing**. Resolve every identifier before you cite it.

## Where this stands, September 2026

The history above is working knowledge of the MT literature; treat every paper claim as coverage
and read the papers before quoting numbers. What is primary here is small and load-bearing: the
LLaDA repository's own statement that its sampling is slower than an autoregressive baseline, read
first-hand (question 258), which is the 2018 story repeating with a bigger budget. The durable
lesson is a measurement discipline, not an architecture: **before you believe a decoding speedup,
ask what the baseline was, what batch size it ran at, and whether the fast model needed the slow
one to be trained.**
