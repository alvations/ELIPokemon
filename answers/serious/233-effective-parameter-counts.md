---
id: "233"
slug: effective-parameter-counts
style: serious
category: open-weights
difficulty: intermediate
question: "Gemma 4 ships checkpoints called E2B and E4B whose effective parameter count is not their parameter count. What is that label actually telling you?"
tags: [gemma, per-layer-embeddings, on-device, parameter-counts, memory]
---

# "Effective" is a residency claim, not a capability claim

E4B is roughly **7.5B parameters on disk and 4.7B that have to be in fast memory at once**. The
gap is a second embedding table — Per-Layer Embeddings — that is indexed rather than multiplied,
so it can sit in slow memory, on flash, or on the CPU side of the bus and be read 256 values at a
time. The `E` is telling you which of the two numbers predicts whether the thing runs on your
phone. It is not telling you it performs like a 4B model, and reading it that way is the mistake
the label invites.

I read this out of the reference implementation rather than a blog post. In
[`google-deepmind/gemma`](https://github.com/google-deepmind/gemma), `gemma/gm/nn/gemma4/` defines
four checkpoints — `Gemma4_E2B`, `Gemma4_E4B`, `Gemma4_31B`, `Gemma4_26B_A4B` — and the E-models
are the only two with `per_layer_input_dim=256`. The other two set it to zero.

## The arithmetic, from the config

The per-layer embedding table has shape `(vocab_size, num_layers, per_layer_input_dim)`, and
Gemma 4's vocabulary is 262,144. That is the whole trick, and it is one multiplication:

```
   E2B  35 layers · d_model 1536          E4B  42 layers · d_model 2560
   ──────────────────────────────────     ──────────────────────────────────
   blocks (attn + MLP)        1.88 B      blocks (attn + MLP)        4.00 B
   input embedding 262,144×1536  0.40 B   input embedding 262,144×2560  0.67 B
                             ───────                                 ───────
   EFFECTIVE                  2.28 B      EFFECTIVE                  4.67 B
   PLE 262,144 × 35 × 256     2.36 B      PLE 262,144 × 42 × 256     2.82 B
                             ───────                                 ───────
   RAW TOTAL                  4.65 B      RAW TOTAL                  7.52 B
                                          (published: ~2.3B / ~4.5B effective,
                                           ~5B / ~8B raw — within rounding)

   what a single token costs you out of that table, per layer:

        262,144 rows                    ┌── one row ──┐
        ┌───────────────────────────────┴─────────────┴──────────┐
        │  ...                                                   │
        │  token 18,422  →  [256 numbers]  ← this is the fetch    │
        │  ...                                                   │
        └────────────────────────────────────────────────────────┘
          2.82 B parameters resident      42 × 256 = 10,752 values read
          = 1.41 GB at int4               = 5.25 KB at int4, per token

          ratio: you hold 1.41 GB to read 5 KB.  That asymmetry is the
          entire argument for moving the table off the accelerator.
```

A weight matrix has to be *there* because every output touches every element of it. A lookup
table does not: for a given token you need exactly one row of it, and you know which row before
the forward pass starts. So you can mmap it, page it, keep it in CPU DRAM and DMA the rows across,
or hold it in int4 while the blocks run in higher precision. None of that is available for the
attention and MLP weights, which is why those 4.67B are the number that has to fit.

## What this is not

It is **not** MatFormer. Gemma 3n paired PLE with a nested-submodel scheme plus AltUp and Laurel;
grepping `gemma/gm/nn/gemma4/` for `matformer`, `altup` and `laurel` returns nothing, while
`gemma/gm/nn/gemma3n/` returns all three. E2B and E4B are also not nested in each other — 35
layers at d_model 1536 against 42 at 2560. They are two separately trained models that share one
memory trick. If you have read about Gemma 3n and assumed the slicing story carried forward, it
did not.

It is also **not** a capability claim, and here is the honest tension in the label. A vendor
naming a checkpoint E4B is making the useful claim "budget for 4.5B of resident weights". A reader
hears "this is a 4B model", compares it against a dense 4B, and has been handed a favourable
comparison for free: the E4B was trained with 7.5B of parameters' worth of capacity, and the PLE
table is not decoration — it feeds a per-layer signal into every block. The number you should
compare against a dense 4B on quality is 7.5B. The number you should compare on memory is 4.7B.
One label, two readings, and the flattering one is the one that spreads.

## The three places it bites

1. **Your app bundle is sized by the raw number.** You ship 7.5B of weights. A 4-bit E4B download
   is a few gigabytes, and "E4B" does not tell your users that.
2. **The saving is conditional on your runtime supporting it.** A stack that materialises the PLE
   table into accelerator memory alongside everything else gets no benefit at all and just loads
   a 7.5B model. Check what your runtime actually does before you budget for 4.7B.
3. **It does not apply upward.** `Gemma4_31B` and `Gemma4_26B_A4B` both set
   `per_layer_input_dim=0`. On a server, HBM is not the constraint that PLE relieves, and the
   added complexity buys nothing.

## What an interviewer is listening for

That you separate *parameters that must be resident* from *parameters that must exist* before you
answer anything. Then that you can name the mechanism — an indexed table, not a multiplied one —
and say why indexing is what makes offload legal. The strongest answers volunteer the reading
failure: an effective-parameter label is a deployment number that will be read as a quality
number, and the candidate who says so unprompted has understood what the label is for.

## Where this stands, September 2026

The layer counts, dimensions, vocabulary size and `per_layer_input_dim` values above were read
first-hand from `gemma/gm/nn/gemma4/_gemma4.py` and `_config.py` in `google-deepmind/gemma`, and
cross-checked against `Gemma4TextConfig` in `huggingface/transformers`
(`vocab_size_per_layer_input=262144`, `hidden_size_per_layer_input=256`) — both **primary**. The
parameter totals are my own arithmetic over those configs, not quoted figures; they land within
rounding of the published effective counts, which is the check that they are right. The published
"~2.3B / ~4.5B effective" figures themselves are **coverage**: `arxiv.org`, `huggingface.co` and
`ai.google.dev` are all blocked from this environment, so the technical report and the model
cards were not read. Those are the authority. The reasoning — that "effective" answers a
residency question — will outlive the checkpoints.
