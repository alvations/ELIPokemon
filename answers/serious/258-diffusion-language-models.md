---
id: "258"
slug: diffusion-language-models
style: serious
category: optimization
difficulty: advanced
question: "Diffusion language models generate a whole sequence at once instead of left to right. What has actually shipped, and what does the approach cost?"
tags: [diffusion, decoding, non-autoregressive, parallel-decoding, inference]
---

# A canvas of masks, revised in place

A diffusion language model does not extend a prefix. It starts from a block of positions that are
all `[MASK]`, runs a forward pass that predicts **every** position at once, commits the positions
it is most confident about, re-masks the rest, and repeats. Almost everything shipping under the
name is **discrete masked diffusion** — an absorbing-state process over tokens, as in
[MDLM](https://arxiv.org/abs/2406.07524) — not Gaussian noise on embeddings, which is where the
research line started and is not where it ended up. The selling point is that a forward pass
yields many tokens instead of one, and that a token written at step 3 can be taken back at step 7.
The bill arrives as quality per unit of compute, and as a conditional-independence problem that
every practical system pays down by *giving the parallelism back*.

```
  AUTOREGRESSIVE                        MASKED DIFFUSION (4 steps over one block)
  ──────────────                        ─────────────────────────────────────────
  t1  The                               step 0  [M][M][M][M][M][M][M][M]
  t2  The cat                           step 1  [M][M] sat [M][M] the [M][M]   <- 2 committed
  t3  The cat sat                       step 2  The [M] sat [M][M] the mat [M] <- 2 more
  t4  The cat sat on                    step 3  The cat sat on [M] the mat .
  ...                                   step 4  The cat sat on  the  mat .   > done

  1 forward pass  ->  1 token           1 forward pass  ->  k tokens, k set by confidence
  KV cache: exact, causal prefix        KV cache: approximate; the canvas keeps changing
  length: decided by EOS                length: decided by the canvas you allocated
```

## What has actually shipped, by tier

**Open weights you can download today (primary — repository READMEs read first-hand).** The
LLaDA line is the reference open dLLM: `LLaDA-8B-Base` and `-Instruct` (February 2025, MIT,
[2502.09992](https://arxiv.org/abs/2502.09992)), `LLaDA 1.5`, `LLaDA-MoE-7B-A1B` (11 September
2025, described in the repo as the first diffusion LM pretrained from scratch with an MoE
architecture, roughly 1B active parameters), and `iLLaDA-8B` (24 June 2026, Apache 2.0). HKU
NLP's **Dream 7B** (April 2025) is the other one, with `Dream-Coder` and `DreamOn` — the latter
existing specifically to attack variable-length generation and infilling. NVIDIA's **Fast-dLLM**
family is the serving work: v1 ([2505.22618](https://arxiv.org/abs/2505.22618)) is training-free
KV caching plus confidence-gated parallel decoding over LLaDA and Dream; v2 is block diffusion
with hierarchical caching; `Fast-dVLM` (April 2026) claims up to **6.18× over an AR baseline
while matching quality across 11 benchmarks**; `Fast-dDrive` (May 2026) claims over 200
tokens/second on a single H100 for a driving VLA. Both v1 and v2 were accepted at ICLR 2026.

**Open weights from a frontier lab (coverage).** **DiffusionGemma** (`26B-A4B`, ~4B active,
reported 10 June 2026, Apache 2.0) is the most useful data point in the field, because it is a
diffusion model built on the *same* Gemma 4 MoE architecture as its autoregressive sibling. It
denoises **256-token blocks** in parallel, is reported at over 1,000 tokens/second on one H100 and
roughly 4× the throughput of the AR model — and it is reported as **below** `Gemma 4 26B-A4B` on
every benchmark measured, with the vendor guidance being to use standard Gemma 4 when quality
matters most. I could not reach `ai.google.dev` or `blog.google` from this environment; treat
those figures as coverage and read the model card before quoting them.

**A commercial API (coverage).** Inception's **Mercury** family is the first commercial-scale
dLLM; `Mercury 2.5` (9 September 2026) is reported at 1,107 tokens/second with a 260K context,
served through Inception's own OpenAI-compatible API and through Baseten, OpenRouter and Azure AI
Foundry. `inceptionlabs.ai` is blocked from here; the vendor's model page is the authority.

**Still experimental.** **Gemini Diffusion** was shown in May 2025 and, as far as coverage
indicates, has not become a generally available product. That is the line to hold in an interview:
one open frontier checkpoint, one commercial API, and a demo that is still a demo.

## What the approach buys

* **Tokens per forward pass instead of per token.** The unit of work changes, which is why the
  throughput claims are large and the *latency* claims are not.
* **Revisability, natively.** Infilling and editing are the training objective, not a bolted-on
  fill-in-the-middle mode. A position can be re-masked after it was filled — which is also why a
  diffusion model can emit its final answer before the reasoning that supports it, and the LLaDA
  repository shows exactly that happening.
* **Any-order modelling.** The masked-diffusion objective is an upper bound on the negative
  log-likelihood and is equivalent to an any-order autoregressive objective, which is the honest
  reason people expect it to handle reversal-style tasks better than a left-to-right model.

## What it costs

1. **Quality per unit of compute.** DiffusionGemma against Gemma 4 is the cleanest available
   ablation and it goes the wrong way. The LLaDA repository's own FAQ is blunter: sampling is
   *slower* than the autoregressive baseline, for three stated reasons — a fixed context length,
   no usable KV cache, and best quality only when the number of sampling steps equals the response
   length. Take one step per token and you have rebuilt autoregression with worse caching.
2. **Conditional independence, which is the real one.** Within a step, positions are sampled
   independently given the current canvas. A product of marginals is not the joint. Each position
   picks something locally reasonable and the pair does not cohere. Every deployed fix is the same
   fix: commit fewer positions per step (confidence thresholds, Fast-dLLM v1), or bound the window
   inside which you are willing to assume independence (block diffusion,
   [2503.09573](https://arxiv.org/abs/2503.09573); DiffusionGemma's 256-token blocks).
   **The parallelism you keep is the parallelism you can show you did not need.**
3. **Length is an allocation, not an outcome.** You size the canvas up front. `DreamOn` exists
   because variable-length generation is unsolved, and the constraint rhymes with the hard-length
   problem in question 144.
4. **Serving maturity.** Caching is approximate and engine support lags: `vLLM` integration is
   still an open TODO in the LLaDA repository as of this writing. Block diffusion also trades
   **higher time-to-first-token for higher throughput**, which is backwards for a streaming chat
   UI and right for batch work.

Two neighbours worth separating. Question 201's typed decision model is also non-autoregressive,
but it escapes left-to-right by *enumerating* the answer space rather than generating over it — a
different trade entirely, and one that gives up open-ended output to get its guarantee. And image
diffusion (093, 137) is continuous; text diffusion is discrete masking, and the shared word hides
more than it reveals.

## What an interviewer digs into next

* Why does committing more positions per step hurt, and what exactly is the independence
  assumption?
* Why can a diffusion LM not use a standard KV cache?
* Where does the speed actually show up — time-to-first-token, tokens/second, or cost per request?
* Would you deploy one today, and for what? (Batch, latency-tolerant, edit-shaped work is the
  honest answer.)

**Citation note.** The arXiv identifiers linked above are given from working knowledge.
`arxiv.org` is blocked from the environment this was written in, so **not one of them was
resolved while writing**. Resolve every identifier before you cite it.

## Where this stands, September 2026

Primary, read first-hand: the LLaDA, Dream and Fast-dLLM repository READMEs, including release
dates, licences, the open `vLLM` TODO and the sampling-efficiency FAQ. Coverage only: every
DiffusionGemma and Mercury figure, and the claim that Gemini Diffusion is still experimental —
those vendor pages are blocked from here and their model cards are the authority. The durable part
is not the leaderboard. It is that a whole-sequence generator has to buy back coherence with
serial steps, and how much it buys back is the whole argument.
