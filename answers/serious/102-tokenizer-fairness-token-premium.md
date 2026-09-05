---
id: "102"
slug: tokenizer-fairness-token-premium
style: serious
category: multilingual
difficulty: core
question: "Why do non-Latin scripts consume more tokens, and what does that token premium cost?"
tags: [tokenization, fairness, fertility, byte-fallback, cost]
---

# The token premium

The same sentence, translated faithfully, costs a different number of tokens in every language —
and the spread is enormous. [Petrov et al. (2023)](https://arxiv.org/abs/2305.15425) measured up
to a **15× difference** across languages for equivalent content on widely used tokenizers.
Burmese, Amharic, Telugu and Khmer sit at the expensive end; English at the cheap end. Nobody
designed this. It falls out of what the tokenizer was trained on.

## Mechanism

BPE and unigram tokenizers learn merges from a corpus. Frequent sequences become single tokens;
rare ones stay fragmented. If the tokenizer's training mix is 90% English, English words become
whole tokens and Amharic words never accumulate enough frequency to merge. Two effects stack:

1. **Under-merged subwords.** The script is in the vocabulary but the words are not, so you pay
   one token per character or per two characters.
2. **Byte fallback.** A character absent from the vocabulary is emitted as its UTF-8 bytes. A
   Devanagari character is 3 bytes, so one character becomes **three tokens**.

```
  "The weather is nice today"        ─►  5 tokens      (1.0× baseline)
  "Il fait beau aujourd'hui"         ─►  8 tokens      (1.6×)
  "今日はいい天気です"                  ─►  ~11 tokens    (2.2×)
  "आज मौसम अच्छा है"                    ─►  ~25 tokens    (5×)
  "ዛሬ የአየር ሁኔታው ጥሩ ነው"                 ─►  ~40 tokens    (8×)

  ┌────────────────────────────────────────────────────────────┐
  │ fertility = tokens per word.  ~1.3 for English,            │
  │ 3-8 for scripts the tokenizer barely saw. Fertility is the │
  │ number to report; it is what everything below scales with. │
  └────────────────────────────────────────────────────────────┘
```

## What it costs, concretely

* **Money.** APIs bill per token. [Ahia et al. (2023)](https://arxiv.org/abs/2305.13707) showed
  users writing in some languages pay several times more for the same request. The people
  charged most are, on average, in the poorest markets.
* **Context.** A 128k context window is 128k *tokens*, not 128k meanings. In a high-fertility
  language the effective window can be five times smaller, so documents get truncated that
  would have fit in English.
* **Latency.** Generation is per-token and autoregressive. More tokens per sentence means
  proportionally slower responses.
* **Quality.** Over-segmentation costs accuracy: the model spends capacity reassembling words
  instead of reasoning about them, and long-range dependencies stretch further in token space.

That last one matters most and is discussed least. The billing gap is visible; the quality gap
is invisible and correlated with it.

## Mitigations, with their tradeoffs

| Fix | What it buys | What it costs |
| --- | --- | --- |
| Rebalance tokenizer data | Lower fertility everywhere | Bigger vocab, or worse English |
| Larger vocabulary | Headroom for more scripts | Embedding/softmax params grow |
| Vocab expansion + continued pretraining | Fixes one language | New embeddings to train |
| Byte-level, tokenizer-free (q. 112) | No script special-cased | Longer sequences, more FLOPs |
| Language-specific tokenizers | Optimal per language | Breaks a single shared model |

Vocabulary size is the real lever and it is not free: the embedding and output matrices scale
linearly with it, and at small model sizes they can dominate the parameter budget.

## What an interviewer digs into next

* Why does byte fallback triple the cost for some scripts and not others?
* How would you measure fertility, and what would you compare it against?
* If you added 50k vocabulary entries for Indic scripts, what breaks?
* Does the token premium show up in accuracy as well as cost, and how would you isolate it?
