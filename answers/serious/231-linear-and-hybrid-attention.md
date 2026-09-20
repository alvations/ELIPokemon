---
id: "231"
slug: linear-and-hybrid-attention
style: serious
category: open-weights
difficulty: advanced
question: "Linear and hybrid attention promise to kill the quadratic term. What do they actually give up?"
tags: [linear-attention, hybrid, minimax, long-context, sparse-attention]
---

# A growing log becomes a fixed-size state. Everything follows from that one substitution.

Softmax attention keeps every past token and compares against all of them. Linear attention keeps
a **fixed-size recurrent state** and folds each token into it. That kills the quadratic prefill
term and the linearly-growing KV cache in one move, and it gives up the thing the cache was for:
exact recall of any individual earlier token. Hybrids exist because that trade is too sharp at
100% and fine at 25%.

## The arithmetic, on one configuration

Take a 64-layer model, 32 query heads, 8 KV heads, head_dim 128, BF16 — an ordinary open-weight
shape. Question [228](228-attention-variants-and-kv-arithmetic.md) gives the cache formula; here
is what happens when you push `L` out to a million.

```
   full softmax layer
        KV per token = 2 · 8 · 128 · 2                  =       4,096 B
        × 64 layers                                     =     262,144 B per token
        at L = 1,000,000                                =         262 GB
        prefill attention FLOPs per layer  ∝  L²        ← the quadratic term

   linear layer (state S of shape d_k × d_v, per head, FP32)
        state per layer = 32 · 128 · 128 · 4            =   2,097,152 B
        × 48 layers                                     =         101 MB
        …and that number does not move when L does.     ← constant in L
        per-token FLOPs  ∝  d_k · d_v,  not L

   crossover:   4,096 · L  =  2,097,152   →   L ≈ 512 tokens
                above ~512 tokens, the state is cheaper than the tape
```

Put them in a 3:1 hybrid — three linear layers to every full one, the schedule Qwen3-Next and
Kimi Linear both use — and you get:

```
   16 full layers × 4,096 B = 65,536 B per token   → 65.5 GB at 1M
   48 linear layers, fixed                         →  0.1 GB total
   ────────────────────────────────────────────────────────────────
   total ≈ 65.6 GB   against 262 GB for all-full   →  4.0× less
```

That 4× is not a coincidence: it is `1/(1 − 3/4)` inverted, and it is the same order as the ~25 GB
per 1M tokens that community measurements of Qwen3-Next-style stacks report. **The ratio is the
design knob, and it is linear in the fraction of layers you keep full.** Keeping 1 in 8 (the 7:1
schedule MiniMax-01 shipped) gets 8×; keeping 1 in 4 gets 4×. You cannot get 20× this way without
going to 1 in 20, and that is where quality starts to fail.

## What the fixed state actually loses

The state is a sum of outer products: every token writes into the same matrix, and reading it back
is an approximate, interfering lookup rather than an index. Three consequences, in the order they
bite:

1. **Associative recall degrades with load.** "What was the API key on line 40,000" is a lookup.
   A fixed state that has absorbed a million tokens has limited capacity to hold that one pair
   distinctly, and no amount of training buys unbounded capacity into a fixed matrix.
2. **Multi-hop reasoning suffers before single-hop retrieval does.** Finding one fact is
   comparatively easy; chaining three facts spread across the window requires holding several
   precise things simultaneously, which is exactly what a saturating state is bad at. This is the
   failure MiniMax reported, and it is why a needle-in-a-haystack score is a poor test here.
3. **Prefix caching breaks.** A recurrent state is not addressable by position, so the "resume
   from a cached 100K-token prefix" trick that makes long-context serving affordable does not
   apply unaltered. This is a serving regression that never appears in a quality benchmark, and
   engines have had to grow explicit support for hybrid state.

Gating and delta rules — [Gated DeltaNet](https://arxiv.org/abs/2412.06464), Kimi's per-channel
KDA, Mamba-2's selective state — are all attempts to make the state **forget deliberately** rather
than by interference. They help. They do not make it unbounded.

## The field disagreed in public, which is the useful part

```
   MiniMax-01   Jan 2025   7 lightning : 1 softmax        the bet
   MiniMax-M1   2025       kept the hybrid                the bet, scaled
   MiniMax-M2   2025/26    full attention everywhere      the retraction
   MiniMax-M3   Jun 2026   block-sparse (MSA) on GQA      a different bet
        ─────────────────────────────────────────────────────────────────
   Qwen3-Next / Qwen3.5    3 gated DeltaNet : 1 full      stayed hybrid
   Kimi Linear / K3        ~3 KDA : 1 gated MLA           stayed hybrid
   DeepSeek-V3.2           MLA + sparse top-k (DSA)       went sparse
   Llama 4 Scout           NoPE full every 4th, 8K
                           chunked RoPE between           a third kind of hybrid
```

MiniMax published their reasoning for the retraction, and it is the most useful paragraph in this
whole area: no efficient-attention variant reliably matched full attention across reasoning,
coding and agentic work in production; the hybrid looked equal to full attention at small scale on
leaderboards, and at larger scale showed clear deficits on complex multi-hop reasoning. That is
the same failure mode as point 2 above, observed by a lab that had shipped the alternative twice.

Then M3 came back with something else entirely. MiniMax Sparse Attention is *not* linear: it keeps
real, uncompressed keys and values on a GQA backbone, cuts them into blocks, scores the blocks
with a small index branch, and runs exact attention over the top-k blocks per GQA group. Reported
figures: parity with GQA on a 109B model, per-token attention compute down 28.4× at 1M context,
and 14.2× prefill and 7.6× decode wall-clock on H800. M3 itself is reported at 428B total with
about 23B active, 1M context, under a custom MiniMax community licence.

The shape of the 2026 consensus, then: **flagships went sparse; hybrids kept linear layers as a
cost floor rather than as the whole stack.** Sparse keeps exact lookup available for the tokens it
selects. Linear does not keep it for anything.

## How to tell whether the trade lands for you

* Find your real `L` distribution. Below a few thousand tokens none of this matters and the
  constant factors make hybrids *slower*.
* Evaluate on **multi-hop recall over your own documents**, not perplexity and not a single-needle
  test. The gap only shows up where several precise facts must be live at once.
* Check the serving stack supports hybrid state with prefix caching for *your* engine version, not
  in principle.
* Measure prefill and decode separately. Linear layers help both; sparse attention mostly helps
  prefill until the indexer is also cheap at decode.

## Where this stands, September 2026

The checkpoint names will rot fastest, the schedule ratios next, the mechanism not at all. The
MiniMax retraction document, the MSA paper (arXiv 2606.13392) and the Qwen and Moonshot model
cards are the authorities, and I could reach none of them from this environment — every figure
about M1, M2, M3, Qwen3-Next and Kimi above came from coverage and search summaries, so verify
before citing. The part that transfers: a fixed-size state buys you a cost that does not grow, and
charges you exact recall; a sparse selector buys you a cost that grows slowly, and charges you
whatever it failed to select. Those are different bills and you should know which one you are
paying.

## What an interviewer digs into next

* Why does multi-hop reasoning break before needle-in-a-haystack does?
* What does a recurrent state do to your prefix cache?
* Why is MiniMax's MSA not a linear-attention method?

**Citation note.** The arXiv identifiers linked above are given from working knowledge and
checked against search results. `arxiv.org` is blocked from the environment this was written
in, so **not one of the papers was opened while writing**. Resolve every identifier before
you cite it.
