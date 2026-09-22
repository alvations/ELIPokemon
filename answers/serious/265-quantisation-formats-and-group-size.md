---
id: "265"
slug: quantisation-formats-and-group-size
style: serious
category: optimization
difficulty: advanced
question: "What is actually inside a quantised model file? Walk me through k-quants, group size, and the hardware 4-bit formats."
tags: [gguf, k-quants, group-size, mxfp4, nvfp4]
---

# "A 4-bit model" is a container of a dozen different quantisations, plus the receipts.

A quantised file is never uniformly quantised. Open one and you find several tensor types side by
side, each with its own block layout, and a metadata block saying how to undo each of them. Three
questions get you all the way through any format: **how big is the block that shares a scale, what
else does the block store besides the codes, and which tensors were exempted?** The interesting
engineering is entirely in the answers, because the codes themselves are just nibbles.

## The granularity ladder, priced

Every scale you store is metadata, and metadata is paid for in the same currency as the weights.

```
   4096 × 4096 tensor, 16.78M weights, 4-bit codes = 8.39 MB of nibbles

   granularity        scales stored       overhead        bits/weight
   ─────────────────────────────────────────────────────────────────────
   per-tensor                 1  × fp16   2 B             4.000
   per-row (out channel)   4096  × fp16   8 KB  (0.1%)    4.001
   per-group of 128      131072  × fp16   256 KB          4.125
   per-group of 32       524288  × fp16   1.0 MB          4.500
   ─────────────────────────────────────────────────────────────────────

   The last row is llama.cpp's Q4_0: 32 values + one fp16 scale = 18 bytes.
   Half a bit per weight, spent on ONE number per group of 32.
```

Group size is the entire quality dial at 4 bits. Bigger groups are cheaper and let one bad value
in the group set the scale for all of it; smaller groups spend real bits on metadata. Per-tensor
for weights is generally a mistake, per-row is nearly free and should be the floor, and 32–128 is
where everyone actually lives.

## k-quants: the same half-bit, spent much better

`ggml`'s k-quants use a **super-block of 256** (`QK_K`) split into sub-blocks, with a two-level
scale hierarchy. `Q4_K` is the one to know, and the struct is worth reading literally:

```
   block_q4_K, 256 weights                               bytes
   ──────────────────────────────────────────────────────────
   d      fp16   super-block scale for the sub-scales       2
   dmin   fp16   super-block scale for the sub-MINS         2
   scales 12 B   8 scales AND 8 mins, 6 bits each          12
   qs     128 B  8 sub-blocks × 32 nibbles                128
   ──────────────────────────────────────────────────────────
                                                    total 144  = 4.5 bpw

   Q4_0, same 4.5 bpw:  1 fp16 scale per 32 values, symmetric, no min.

   SAME BUDGET. Different purchase:
     Q4_0  buys  one scale per 32
     Q4_K  buys  eight scales + eight MINS per 256, each 6-bit, both
                 rescaled by a shared fp16 — i.e. asymmetric coding,
                 so a sub-block that sits entirely above zero does not
                 waste half its levels on values that never occur.

   And it shows. Llama-3-8B, Wikitext-2 (llama.cpp's own scoreboard):
     q4_0    4.34 GiB   PPL 6.700
     q4_K_S  4.37 GiB   PPL 6.501
     q4_K_M  4.58 GiB   PPL 6.407   (f16 baseline: 6.233)
```

The rest of the family, with the effective rates the header itself records: `Q2_K` 2.625, `Q3_K`
3.4375, `Q5_K` 5.5, `Q6_K` 6.5625 bits per weight. The `IQ` types go lower still by replacing
independent nibbles with **codebook lookups** over groups of eight, which is why they need an
importance matrix to build at all while the plain k-quants do not.

## `_M` and `_S` are not types. They are policies.

This is the part people get wrong. `Q4_K_M` is not "Q4_K". It is a *recipe* that assigns a type
per tensor, and reading the assignment rules is more informative than any table:

* `output.weight` is promoted — `Q6_K` under most 4-bit recipes.
* `attn_v.weight` and `ffn_down.weight` are promoted to `Q6_K` on a subset of layers.
* The subset is `i < n/8 || i >= 7n/8 || (i − n/8) % 3 == 2` — **the first eighth, the last
  eighth, and every third layer in between.** Early and late layers get more bits; the middle is
  sampled.
* the fused QKV tensor goes to `Q5_K` under `Q4_K_M`.
* 1-D tensors (norms, biases) are not quantised at all.

So a "Q4_K_M" file contains Q4_K, Q5_K and Q6_K tensors, and its average bits-per-weight is an
emergent property of that policy rather than a number anyone chose. The same logic — spend extra
bits where the error propagates furthest — is what every serious pipeline does under different
names.

## The importance matrix

The `imatrix` tool runs the model over calibration text and accumulates, per tensor, the **sum of
squared activations** on each input channel. The quantiser then weights its rounding objective by
those numbers, so a channel that is large and frequently active is fitted more carefully than one
that is dormant. It is AWQ's insight ([264](264-outlier-channels-and-quantisation-algorithms.md))
in a different wrapper: importance comes from the activations, not the weights.

Two honest things about it. It buys less than people expect at 4 bits — 6.407 → 6.383 PPL on the
scoreboard above — and the tool's own documentation reports **no consistent improvement from using
more calibration tokens**, across runs from 1K to 10M. Below 3 bits it stops being optional: the
`IQ1`, `IQ2` and `IQ3_XXS` types refuse to build without one. What it introduces is a leak,
because you now have a dataset in the loop, and evaluating on anything resembling it flatters the
result ([267](267-evaluating-a-quantised-model.md)).

## The hardware-native 4-bit formats

FP8 (E4M3 for weights and activations, E5M2 where range beats precision) has been the datacentre
default since Hopper and is covered for training in [216](216-fp8-training-and-cost-figures.md).
The 4-bit pair is newer and the difference between them is a clean piece of engineering:

```
   MXFP4  (OCP microscaling)          NVFP4  (Blackwell)
   ──────────────────────────         ───────────────────────────────
   block of 32                        block of 16
   scale: 1 byte, E8M0                scale: 1 byte, UE4M3 (an fp8)
          — a POWER OF TWO only              — a real fractional scale
   elements: E2M1, 4 bits             elements: E2M1, 4 bits
   ──────────────────────────         ───────────────────────────────
   1 + 16 = 17 B / 32 values          4 + 32 = 36 B / 64 values
        = 4.25 bits/weight                 = 4.50 bits/weight

   MXFP4's scale can only halve and double, so a block whose maximum
   sits just above a power of two throws away nearly a bit of range.
   NVFP4 pays 0.25 bits/weight more and a finer block to fix exactly
   that, and adds a per-tensor fp32 scale above it.
```

Both are in `ggml` as real block types, so the same file can now carry k-quants and microscaling
side by side. The strategic point: these are **formats the tensor cores read natively**, so unlike
GPTQ or AWQ output they give compute speedup and not only bandwidth
([263](263-ptq-versus-qat-and-weight-only.md)).

## What a real file's metadata looks like

GGUF is a header, a key-value metadata block, a table of tensor descriptors, then aligned tensor
data. The fields you actually read:

```
   header      magic "GGUF" · version · tensor_count · metadata_kv_count
   metadata    general.architecture      = "llama"
               general.file_type         = 15          ← 15 is Q4_K_M,
               general.quantization_version            ← 38 MXFP4, 39 NVFP4
               general.alignment         = 32 (default if absent)
               llama.block_count, llama.attention.head_count_kv, ...
               tokenizer.ggml.* (the whole tokenizer lives in the file)
   tensors     name (≤64 bytes) · n_dims · dims[] · ggml_type · offset
               ──────────────────────────────────────────────────────
               token_embd.weight        [4096, 128256]   Q6_K
               blk.0.attn_q.weight      [4096, 4096]     Q4_K
               blk.0.attn_v.weight      [4096, 1024]     Q6_K   ← promoted
               blk.0.ffn_down.weight    [14336, 4096]    Q6_K   ← promoted
               blk.5.ffn_down.weight    [14336, 4096]    Q4_K
               output_norm.weight       [4096]           F32    ← 1-D
```

Dump that table before you trust a filename. `general.file_type` is documented as *optional and
inferrable*, the quantisation version can change without the scheme's name changing, and uploaders
rename files freely. The per-tensor column is the ground truth; everything else is a label.

## What an interviewer digs into next

* Q4_0 and Q4_K are both 4.5 bits per weight. Why is one clearly better?
* What does a per-group *min* buy that a per-group scale does not?
* Why does MXFP4 restrict its scale to powers of two, and what does that cost?
* Which tensors would you spend extra bits on if the recipe were yours to write?

## Where this stands, September 2026

Nearly everything above is **primary**: the block layouts and bit rates, the per-tensor promotion
rules, the file-type enumeration, the container layout, the importance-matrix behaviour and the
perplexity figures were all read directly out of the llama.cpp and GGUF sources rather than from
coverage of them. What is **coverage** is the framing of MXFP4 and NVFP4 as OCP and NVIDIA formats
respectively, and the per-tensor FP32 scale in the NVFP4 definition; the vendor specifications are
unreachable from here, so check them. The formats will keep arriving — 1-bit and 2-bit block types
are already in the header — and the three questions at the top will keep working on all of them.
