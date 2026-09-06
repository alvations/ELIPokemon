---
id: "112"
slug: byte-level-and-tokenizer-free
style: serious
category: multilingual
difficulty: advanced
question: "Should a multilingual model go byte-level or tokeniser-free?"
tags: [byte-level, byt5, canine, blt, robustness, sequence-length]
---

# Byte-level and tokeniser-free models

A tokenizer is a frozen, corpus-dependent, non-differentiable preprocessing step that decides
before training which languages are cheap (question 102). Removing it removes that bias — at the
cost of much longer sequences.

## The options

* **Byte-level.** Model raw UTF-8 bytes. [ByT5](https://arxiv.org/abs/2105.13626) (Xue et al.,
  2021) is the reference: a 256-entry vocabulary, no unknown tokens ever, every script treated
  identically by construction. It rebalances the encoder/decoder depth because byte sequences
  need more encoder work per unit of meaning.
* **Character-level with downsampling.** [CANINE](https://arxiv.org/abs/2103.06874) (Clark et al.,
  2021) hashes characters and strides down before the deep stack, then upsamples for token-level
  tasks. Charformer learns the segmentation as part of the model.
* **Learned patching.** The modern form: keep bytes at the boundary, but group them dynamically
  into patches so compute is spent unevenly — more on hard regions, less on predictable ones
  ([Byte Latent Transformer](https://arxiv.org/abs/2412.09871), Pagnoni et al., 2024). This is
  the design that makes byte-level compute-competitive rather than merely principled.

```
   SUBWORD                          BYTE-LEVEL
   ┌─────────────────────────┐      ┌───────────────────────────────────┐
   │ "unbelievable"          │      │ u n b e l i e v a b l e           │
   │ ► [un][bel][iev][able]  │      │ ► 12 steps                        │
   │   4 steps               │      │                                   │
   │ "ትምህርት" ► 15 byte-      │      │ "ትምህርት" ► 15 steps                │
   │   fallback pieces       │      │   same rule as English. No bias.  │
   └─────────────────────────┘      └───────────────────────────────────┘
      cheap IF the tokenizer          uniformly ~4x longer, uniformly fair
      saw your language
```

## What you gain

* **Script neutrality.** No language is under-merged, because nothing is merged. The token
  premium disappears as a *fairness* problem (though the length cost remains for scripts with
  multi-byte characters — Devanagari is still 3 bytes per character).
* **Robustness.** Typos, mixed scripts, code-switching, unusual casing and social-media noise
  degrade gracefully instead of exploding the segmentation. ByT5's headline result is exactly
  this: large gains on noisy text.
* **No out-of-vocabulary anything.** New scripts, emoji, code, DNA — all just bytes.
* **Morphology.** Character-level access helps on tasks that require seeing inside words
  (question 113), and on word games and spelling tasks that subword models notoriously fail.

## What you pay

* **Sequence length, and therefore compute.** 4-5× more positions, with attention cost growing
  faster than linearly unless you patch or downsample. This is the whole reason subwords won.
* **Effective context shrinks** in units of meaning, which partly undoes the fairness gain.
* **Weaker long-range modelling** at equal depth: the same dependency now spans four times as
  many positions.

## The honest summary

Byte-level is clearly the more principled design and is not yet the default, because subword
models are simply cheaper at the quality levels people currently ship. The interesting work is
in the middle — dynamic patching, learned segmentation, and hybrid schemes that keep the
tokenizer for well-covered languages and fall back to bytes elsewhere. If your problem is noisy,
multi-script, or in a language your tokenizer under-serves, byte-level is a live option today.

## What an interviewer digs into next

* Why did ByT5 change the encoder/decoder balance?
* Why does removing the tokenizer not remove the length disadvantage for Indic scripts?
* What does dynamic patching buy over fixed downsampling?
* Where would you still choose subwords, knowing everything above?
