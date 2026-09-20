---
id: "206"
slug: million-token-context
style: serious
category: frontier
difficulty: advanced
question: "Million-token context windows are now standard, including in open weights. What does that change, and what does it not?"
tags: [long-context, retrieval, prompt-caching, tokenizer, prefill]
---

# The input grew five-fold. The output did not.

A million tokens is no longer a frontier feature. Claude Fable 5.1, Claude Opus 5 and Claude
Sonnet 5 sit at 1M; the GPT-5.6 tiers are at 1.05M; and on the open-weight side Moonshot's Kimi
K3 and Upstage's Solar Open 2 both advertise 1M as well. The question stopped being *can you fit
it* and became *should you*.

## What genuinely changed

Whole artefacts fit. A mid-sized repository, a full deposition, a year of a support queue, a
long video's transcript with its frames. For those, an entire layer of engineering — chunk size,
overlap, hierarchical summarisation, re-ranking chunks that never needed splitting — simply stops
being necessary. That is a real reduction in moving parts and it is the main thing to celebrate.

## What did not change, in the order it will bite you

**The output cap.** Max output is 128K on the same models with 1M in. The window grew on one
side only, so "summarise these 900K tokens" is fine and "translate these 900K tokens" is not.
Long-output work is still a chunking and stitching problem.

**The bill.** You pay per input token, every call. A 900K-token prompt at $5 per million is
$4.50 before the model emits anything, and it is charged again on the next turn unless the prefix
is cached. **Prompt caching stops being an optimisation and becomes the architecture**: cache
reads run at a small fraction of the base input price, so the difference between a cached and
uncached long-context design is an order of magnitude, not a percentage.

**Position is not uniform.** Retrieving one fact from anywhere in a long window is close to
solved; *reasoning jointly over material spread across it* is not the same task and does not
have the same pass rate. A needle-in-a-haystack score is a floor, not a ceiling.

**Prefill latency.** Time-to-first-token scales with the prompt. On an interactive path, a large
uncached context is felt by the user even when it is affordable.

**Tokens are not a stable unit.** Anthropic's current tokenizer fits roughly 555K English words
into 1M tokens; the previous one fitted about 750K. The number on the spec sheet went up while
the amount of text it holds went down. Any budget, chunker or truncation rule carried across a
model generation needs re-measuring, not re-scaling.

```
   ┌──────────────────────── 1,000,000 tokens in ─────────────────────────┐
   │ system │ cached corpus ······················· │ turn │ query        │
   └────────┴───────────────────────────────────────┴──────┴──────────────┘
        ▲                    ▲                          ▲
        │                    │                          └ the only part
        │                    │                            that changes
        │                    └ cache this or pay full price every turn
        └ ~555K English words on the current tokenizer, not 750K

                                   ────────►  ┌──────────────┐
                                              │ 128K out max │
                                              └──────────────┘
                                              unchanged. 8:1 asymmetry.
```

## When retrieval still wins

Not as a fallback — on the merits. Retrieval gives you **precision** (the model reads ten
relevant pages, not ten thousand), **freshness** (an index updates; a cached prompt does not),
**citation** (you know which document the claim came from), **access control** (you can filter
per user before the model sees anything) and **cost** that does not scale with corpus size. The
honest summary is that long context killed *chunking as a workaround* and left *retrieval as a
design choice* entirely intact — often as a first pass that fills a long window with the right
100K rather than an arbitrary 900K.

## What an interviewer is listening for

The asymmetry, first — many candidates have not noticed that output limits barely moved. Then
caching as the thing that makes long context economically viable at all. The strongest answers
resist "we can stop doing RAG now" and say which of the five properties above their application
actually needs.

## Where this stands, September 2026

Window sizes and tokenizers both change per generation; the figures here are September 2026.
The asymmetry between input and output has held across several generations, which is the part
worth planning around.
