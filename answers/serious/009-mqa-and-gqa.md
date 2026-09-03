---
id: "009"
slug: mqa-and-gqa
style: serious
category: inference
difficulty: intermediate
question: "Explain Multi-Query Attention and Grouped-Query Attention."
tags: [mqa, gqa, kv-cache, inference, llama]
---

# MQA and GQA

Standard multi-head attention gives every head its own `K` and `V`. At inference that means the
KV cache scales linearly with head count, and decoding is memory-bandwidth bound, so the cache
*is* the latency. MQA and GQA attack this by noticing an asymmetry: the **queries** are where
head diversity earns its keep; the keys and values are largely redundant across heads.

```
  MHA  (n_q = 8, n_kv = 8)      GQA  (n_q = 8, n_kv = 2)      MQA  (n_q = 8, n_kv = 1)

  Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q8       Q1 Q2 Q3 Q4  Q5 Q6 Q7 Q8      Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q8
  │  │  │  │  │  │  │  │        └──┬──┴──┘   └──┬──┴──┘        └──┴──┴──┬─┴──┴──┴──┘
  K1 K2 K3 K4 K5 K6 K7 K8          KV1           KV2                   KV1
  V1 V2 V3 V4 V5 V6 V7 V8

  cache: 8 units                cache: 2 units                cache: 1 unit
  quality: baseline             quality: ≈ baseline           quality: measurable drop
```

**MQA** ([Shazeer, 2019](https://arxiv.org/abs/1911.02150)) collapses to a single shared KV
head. Cache shrinks by `n_heads` (typically 32–64×), decode gets dramatically faster — and
quality degrades, with training instability reported at scale.

**GQA** ([Ainslie et al., 2023](https://arxiv.org/abs/2305.13245)) interpolates: partition the
query heads into `g` groups, one KV head per group. `g = n_heads` recovers MHA; `g = 1` recovers
MQA. In practice `g = 8` gives near-MHA quality at ~8× cache reduction, which is why Llama 2
70B, Llama 3, Mistral and most current open models use it.

GQA also comes with a practical trick: you can **uptrain** an existing MHA checkpoint into GQA
by mean-pooling the KV heads within each group and fine-tuning on ~5% of the original compute,
rather than pretraining from scratch.

## Why the asymmetry works

A head's *selectivity* comes from its query projection — what it is looking for. The key and
value spaces are more like a shared description of "what each token is and offers", and several
heads can read the same description while asking different questions of it. Sharing keys
constrains what distinctions heads can draw, which is why MQA does lose something; sharing them
in small groups keeps enough diversity.

## Choosing

| | MHA | GQA (g=8) | MQA |
| --- | --- | --- | --- |
| KV cache | 1× | ~1/8 | ~1/32 |
| Quality | best | ≈ MHA | slight drop |
| Max batch size | low | high | highest |
| Used by | GPT-2, early models | Llama 2/3 70B, Mistral | PaLM, Falcon, Gemini-class |

The related-but-different approach is **MLA** (multi-head latent attention, DeepSeek-V2): cache
a single low-rank *latent* per token and project it back up to per-head K/V on the fly, trading
a little compute for a much smaller cache while claiming quality above GQA.

Note the training-time picture barely changes: with prefill you compute the full `n × n`
attention either way, so GQA's win is almost entirely an **inference** win.

## What an interviewer digs into next

* Why do keys and values share more gracefully than queries?
* How would you convert an MHA checkpoint to GQA without retraining from scratch?
* Does GQA help prefill, decode, or both — and why?
* When would you still pick MHA?
