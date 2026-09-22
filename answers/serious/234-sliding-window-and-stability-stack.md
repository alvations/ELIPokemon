---
id: "234"
slug: sliding-window-and-stability-stack
style: serious
category: open-weights
difficulty: advanced
question: "Walk me through the attention and stability stack in a small open model — sliding windows, GQA, KV sharing and the norms. What is each one actually buying?"
tags: [sliding-window-attention, gqa, kv-cache, rope, normalisation]
---

# Five of every six layers are not allowed to remember anything older than a thousand tokens

Gemma 4's text stack is a pile of separate decisions that all spend the same currency: how much
of the past each layer is permitted to hold. Interleaved local and global attention sets *how
far back*; grouped-query and multi-query attention set *how many copies*; KV-cache sharing sets
*how many layers pay at all*; and a second family — QK-norm, pre- and post-norm, a dual RoPE and
a final logit cap — spends nothing on memory and exists purely so the thing trains and decodes
without blowing up. Take them one at a time, because they fail in different ways.

Everything numeric below is read out of `gemma/gm/nn/gemma4/_gemma4.py` and `_config.py` in
[`google-deepmind/gemma`](https://github.com/google-deepmind/gemma).

## The ladder

```
   Gemma 4 31B — 60 layers, pattern (local ×5, global ×1), sliding window 1024

   L L L L L G   L L L L L G   L L L L L G   ...   L L L L L G     10 global
   └─────────┘                                                     50 local
    5:1, and every G is a full-context layer

   per token, per layer, BF16:
     local   2 × 16 KV heads × 256 dims × 2 B  = 16,384 B   but only 1,024 rows live
     global  1 × 4 KV heads × 512 dims × 2 B   =  4,096 B   and every row lives

   at a 131,072-token context, batch 1:
     50 local  × 1,024   × 16,384 B  =   0.84 GB   ███
     10 global × 131,072 ×  4,096 B  =   5.37 GB   ████████████████████
                                      ──────────
                                         6.21 GB

     same 60 layers with no window at all      =  112.7 GB   (18× worse)

   E4B — 42 layers, 5:1, window 512, and the last 18 layers compute no K/V at all
     24 layers pay (20 local @ 2,048 B, 4 global @ 4,096 B)
     18 layers read someone else's                    →  57 KB/token, not 98 KB/token
     at 131,072 tokens:   0.02 GB local + 2.15 GB global  =  2.17 GB
```

**Sliding-window attention** is the big one and it is a bet, not a free lunch. Five layers in six
see a 1024-token window; the sixth sees everything. The bet is that a token far in the past
reaches the present *through* the global layers rather than directly, and that ten hops of full
context across sixty layers is enough. When it is not — a fact stated once at token 400 and needed
at token 120,000, with nothing in between to carry it — this is the architecture that drops it.
That failure is invisible on short benchmarks and shows up as "it forgot the system prompt".

**GQA and MQA** are the same knob at different settings. E2B runs 8 query heads against **1** KV
head — genuine multi-query. E4B runs 8 against 2. The 31B runs 32 against 16 locally and 32
against 4 globally. What you give up is distinct key/value subspaces, and the smaller the model
the more aggressively Gemma 4 gives them up, which is the right direction: on a phone the cache is
the constraint, on a server it is not.

**KV-cache sharing** is the one people miss. In E2B the last 20 of 35 layers and in E4B the last
18 of 42 do not compute key and value projections at all — they read the K and V tensors of the
last non-shared layer *of the same attention type*. That is 43% off E4B's per-token footprint and
it removes those projections from the weights too. The cost is that eighteen layers now attend
over a representation built for layer 23, so depth stops buying fresh keys past that point.

**Keys reused as values** is the same idea one level down. In the 31B and 26B-A4B configs
`k_eq_v_global=True`: the global layers derive K and V from a single projection. Read the code and
you can see it — `output = self.k_einsum(...)` then `key_proj, value_proj = output, output`, with
different norms applied afterwards. Half the projection parameters, and in a serving stack that
exploits it, half the distinct values in the global cache.

## The half that costs no memory at all

* **Dual RoPE.** Local layers use base frequency 10,000 and rotate the whole head dimension.
  Global layers use base 1,000,000 and `rope_proportion=0.25` — only a quarter of each
  512-dimension global head carries rotation, 128 dims, the rest positionless. The local layers
  only ever resolve 1,024 positions, so they do not need a stretched frequency; the global layers
  resolve 131,072 and do.
* **QK-norm instead of attention soft-capping.** Every Gemma 4 config sets
  `attn_logits_soft_cap=None`. The `tanh(x/c)·c` squash that Gemma 2 applied to attention logits
  is gone; in its place, RMSNorm on the query and on the key before the dot product. Both control
  the same failure — attention logits growing until softmax saturates and gradients vanish — but
  normalising the inputs is cheaper than squashing the outputs and does not interfere with fused
  attention kernels, which is why the whole field moved.
* **Pre-norm and post-norm, both.** `use_post_attn_norm` and `use_post_ffw_norm` are `True`
  throughout: RMSNorm before each sublayer for gradient flow and again after it to keep the
  residual stream's scale bounded with depth.
* **The one soft cap that survives.** `final_logit_softcap=30.0`. Output logits are squashed to
  ±30 before the softmax over 262,144 vocabulary entries. One cap, at the one place where an
  unbounded value meets a softmax over a quarter of a million options.

## What an interviewer is listening for

That you treat "we use sliding-window attention" as a claim with a failure mode attached, and can
say what the failure looks like. Then that you separate the memory family from the stability
family instead of reciting one list — they are chosen against different constraints and they trade
against each other only indirectly. The strongest answers notice that the attention soft cap was
*removed* between generations and can say what replaced it and why; a candidate who lists soft
capping as a current Gemma feature has learned the stack from a two-year-old summary.

## Where this stands, September 2026

Every number above — layer counts, head counts, window sizes, RoPE bases and proportions, the
`None` on the attention soft cap, the 30.0 on the final one, and which layers share K/V — was read
first-hand from the model definitions in `google-deepmind/gemma`, and the config surface was
cross-checked against `Gemma4TextConfig` in `huggingface/transformers`. Both **primary**. The
cache sizes at 131,072 tokens are my arithmetic over those configs, not quoted figures. The
published claim that these measures cut the global KV footprint by up to 37.5% is **coverage** and
I could not reach the report that states it. Configs change between point releases; read the one
in the checkpoint you downloaded. The reasoning about what a bounded window costs you does not
change.
