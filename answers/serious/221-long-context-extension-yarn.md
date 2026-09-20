---
id: "221"
slug: long-context-extension-yarn
style: serious
category: open-weights
difficulty: advanced
question: "Qwen's checkpoints are 262K native and advertised as extensible to 1M with YaRN. What degrades when you stretch a window instead of training it?"
tags: [qwen, long-context, yarn, rope, linear-attention]
---

# Three different numbers, and only one of them was trained

Every recent Qwen open checkpoint carries the same line in its model card. `Qwen3.5-397B-A17B`:
*"Context Length: 262,144 natively and extensible up to 1,010,000 tokens."* `Qwen3.8-2.4T-A95B`:
the same sentence, verbatim. The serving examples in the Qwen team's own repository all launch at
`--max-model-len 262144`.

Notice that 262,144 × 4 is 1,048,576, and the cards advertise 1,010,000. The gap is small and it
is honest: the arithmetic ceiling and the usable figure are not the same number, and the lab says
so. That distinction is the whole subject.

```
   ① TRAINED OVER        262,144      what the model saw during training
   ② SERVER ACCEPTS      whatever     --max-model-len is a config line; it
                         you set      will happily take 1,010,000
   ③ ACTUALLY USABLE     ???          an empirical question about YOUR
                                      documents that nobody answers for you

   ┌──────────────────────────────────────────────────────────────────────┐
   │  ①──────────────────────────┤                                        │
   │  ②──────────────────────────────────────────────────────────────┤    │
   │  ③────────────────────?                                              │
   │                       ▲                                              │
   │                       └─ everything to the right of here is a claim  │
   └──────────────────────────────────────────────────────────────────────┘
```

## What the stretch actually is

[YaRN](https://arxiv.org/abs/2309.00071) (Peng, Quesnelle, Fan and Shippole, 2023) is
NTK-by-parts RoPE interpolation: leave the high-frequency rotary dimensions alone, interpolate the
low-frequency ones so positions beyond the trained range land inside the learned space, and apply
an attention temperature correction to compensate. On a Qwen checkpoint it is a **config edit** —
set `rope_type` to `yarn`, `factor` to `4.0`, and `original_max_position_embeddings` to `262144`,
and the window is four times larger. No retraining, no new weights, no new data.

Which is exactly why it costs something.

## Four things that degrade, in the order you will meet them

**1. Short prompts, unconditionally.** Every mainstream open framework implements **static** YaRN:
the scaling factor is applied to every request regardless of its actual length. A 900-token prompt
on a 1M-configured server is being interpolated too. Qwen's own model cards say not to enable it
unless the long window is required — which means the 1M setting is a **global mode you switch the
server into**, not a capability that lies dormant until needed.

**2. Positional resolution at the tail.** Interpolation compresses the positional space, so
adjacent positions become less distinguishable the further out you go. A single distinctive span
survives this well, which is why needle-in-a-haystack scores stay high and why they are the wrong
eval. Multi-hop reasoning that has to hold several spans at 700K apart is the thing that breaks,
and it is not what the headline number measures.

**3. Thinking, if you shrink the window instead.** Qwen's card carries an unusual warning in the
other direction: *"because Qwen3.5 leverages extended context for complex tasks, we advise
maintaining a context length of at least 128K tokens to preserve thinking capabilities."* That is
a **floor**. The model spends context on its own reasoning, so trimming `--max-model-len` to save
KV cache also trims how hard it can think (question 220). Two knobs, one number.

**4. Prefill, which is the actual bill.** A million-token request is a million tokens of prefill
before the first output token. Question 206 makes this point in general; here it interacts with
the architecture in a way worth knowing.

## The architecture changes what "degrades" even means

Qwen3.5 is not a pure-attention stack. The Qwen team describes it as "Gated Delta Networks
combined with sparse Mixture-of-Experts", and vLLM's configuration class for the family defaults
`full_attention_interval` to **4**, laying the layers out as three `linear_attention` blocks
(Gated DeltaNet) for every one `full_attention` block.

```
   layer:  1     2     3     4     5     6     7     8   ...
           GDN   GDN   GDN   ATTN  GDN   GDN   GDN   ATTN
           ───────────────   ────  ───────────────   ────
           fixed-size        exact  fixed-size       exact
           recurrent state   KV     recurrent state  KV

   KV cache is paid on 1 layer in 4  ──►  1M tokens becomes affordable
   3 layers in 4 carry a SUMMARY     ──►  and a summary does not grow
                                          when the input does
```

That is the second degradation mechanism, and it is structural rather than positional. On a pure
attention stack, a stretched window blurs *where* things are. On a hybrid stack, three quarters of
the layers were compressing the whole past into a fixed-size state all along — lengthening the
input does not lengthen that state. Whatever reaches the tail reached it through the quarter of
layers that can still look things up exactly.

The trade is real and it is good: it is why these checkpoints can offer a 262K native window
without a KV cache that dominates the memory budget. But it means "how far back can it see" is
answered by the full-attention layers, not by the advertised number.

## What to do about it

1. **Run two configurations, not one.** The native config for ordinary traffic, a YaRN config for
   the long job. One server permanently in 1M mode taxes every short request you have.
2. **Evaluate on a multi-hop task over your own documents.** A retrieval needle tells you almost
   nothing about the failure you will actually hit.
3. **Budget prefill separately from weights.** "It fits" and "it answers in time" are different
   acceptance tests.
4. **Do not cut below the card's floor** to save memory on a reasoning checkpoint.
5. **Treat 1,010,000 as an acceptance result, not a capability result.** The server took it.

## What an interviewer is listening for

That you separate trained-over from accepted-by-the-server from usable, and know which of the
three a vendor number refers to. Then that you know the stretch is a config edit with a global
cost rather than a free upgrade. The strongest answers bring up the hybrid stack unprompted and
observe that on a linear-attention model there are two independent things that can fail at depth.

## Where this stands, September 2026

The context-length sentences, the 128K thinking floor and the licence-adjacent metadata are quoted
from the Qwen model cards, read through a verbatim third-party reproduction because
`huggingface.co` is blocked from this environment; the cards themselves are the authority. The
`full_attention_interval = 4` layout is read directly from vLLM's Qwen3.5 configuration class.
The YaRN parameters are the standard published recipe. **One thing I could not verify:** Qwen's
earlier million-token line was reported to pair dual chunk attention with YaRN, and the current
cards specify YaRN alone — I could not reach a primary page that confirms or rules out dual chunk
attention in the 3.5 / 3.8 checkpoints, so do not assume it either way.

**Citation note.** The arXiv identifier linked above is given from working knowledge.
`arxiv.org` is blocked from the environment this was written in, so it was **not resolved
while writing** — the paper is named because the result is its authors', not because it was
re-read. Resolve it before you cite it.
