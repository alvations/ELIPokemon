---
id: "257"
slug: acceptance-rate-in-production
style: serious
category: optimization
difficulty: intermediate
question: "How would you tell whether speculative decoding is actually paying for itself in production?"
tags: [speculative-decoding, acceptance-rate, observability, benchmarking, serving]
---

# By measuring output tokens per second per GPU at your real concurrency. The rest is clues.

Acceptance rate is a diagnostic, not a verdict. It is not a property of the model — it is a
property of target, drafter, prompt distribution, sampling parameters, position within the draft,
and batch size, all at once, and it moves by thirty points between two endpoints on the same
deployment. The number that decides whether to keep speculation on is end-to-end: output tokens
per second per GPU at your p90 concurrency, and time-per-output-token at p99. Acceptance rate
tells you *why* that number moved and what to change; it never tells you whether you are winning.

## Acceptance varies enormously by workload

The mechanism is [253](253-speculative-decoding-exactness.md)'s identity, `α = 1 − TV(p, q)`. Text
whose continuation is nearly determined has a low-entropy `p`, so almost any drafter sits close to
it. Text with real choice at every position does not.

```
   workload                                      typical α    why
   ─────────────────────────────────────────────────────────────────────────────────
   schema-constrained / JSON echoing a schema     0.90-0.97   p is near-deterministic
   code completion inside a known file            0.85-0.95   syntax closes itself
   diff application, RAG answers quoting source   0.85-0.95   the tokens are in the prompt
   long chain-of-thought                          0.50-0.70   novel, but templated in parts
   general chat prose                             0.60-0.75
   creative writing at temperature 1.0            0.40-0.60   p is deliberately flat
   rare languages, unusual scripts                0.30-0.50   drafter undertrained there
   ─────────────────────────────────────────────────────────────────────────────────
   [coverage — these are order-of-magnitude expectations, not measurements. Measure yours.]
```

Two structural consequences. **Temperature is a dial on your speedup**: raising `T` flattens `p`,
which raises `TV(p, q)`, which lowers `α`. And **the same fleet should not run one
configuration**. A code endpoint and a creative-writing endpoint sit at opposite ends of that
table; configuring them identically means one of them is mistuned by construction.

## Instrument the per-position curve, not just the mean

vLLM's speculative decoding stats carry `num_drafts`, `num_accepted_tokens` and
`num_accepted_tokens_per_pos`, and derive `draft_acceptance_rate = accepted/drafted` and
`mean_acceptance_length = 1 + accepted/drafts` (primary, read from the repository). The
per-position vector is the one worth a dashboard, because it is what sets `γ`.

Position `i`'s entry is the unconditional probability that a draft reached and passed position
`i`, so `E[τ] = 1 + Σᵢ rateᵢ` and the marginal value of extending the draft by one is just
`rate_{γ+1}`. Extending pays while that exceeds `c × (current speedup) / 1`, where `c` is the
draft cost per token relative to a target step. With `c = 0.1`:

```
   position   accept rate   E[τ]    step cost   speedup    threshold   verdict
   ──────────────────────────────────────────────────────────────────────────────
       1         0.90       1.900     1.10       1.727       0.100      extend
       2         0.78       2.680     1.20       2.233       0.173      extend
       3         0.67       3.350     1.30       2.577       0.223      extend
       4         0.58       3.930     1.40       2.807       0.258      extend
       5         0.49       4.420     1.50       2.947       0.281      extend
       6         0.42       4.840     1.60       3.025       0.295      extend
       7         0.36       5.200     1.70       3.059       0.302      extend
       8         0.31       5.510     1.80       3.061       0.306      extend (flat)
       9         0.27         —         —          —         0.306      STOP
   ──────────────────────────────────────────────────────────────────────────────
     γ = 8 is optimal, and γ = 6 gives 98.8% of the benefit for a quarter less draft work
```

Two things a mean acceptance rate hides and this does not. A curve that falls off a cliff at
position 2 is a drafter with no memory — Medusa-style independent heads look like this
([254](254-draft-and-verify-families.md)). A curve that is flat and low everywhere is a drafter
trained on the wrong distribution, and no amount of `γ` tuning will fix it.

## The verdict metrics

* **Output tokens/s per GPU at p90 concurrency.** Not at batch 1. A benchmark at batch 1 measures
  a regime you do not serve in, and [256](256-speculative-decoding-at-high-batch.md) is the reason
  that matters more than anything on this page.
* **TPOT at p50 and p99.** Speculation makes inter-token latency *lumpy* — a step now emits
  between 1 and `γ+1` tokens. Mean TPOT improves while p99 inter-token gaps can get worse, which
  users of a streaming UI will notice before your dashboard does.
* **Cost per million output tokens.** The number that survives a conversation with finance, and
  the one that correctly charges you for the drafter's HBM.
* **Goodput under your SLO**, if you have one: requests per second served within the latency
  target. This is the metric that makes the throughput-for-latency trade legible rather than
  accidental.

## How to run the test

1. **Verify exactness first, or the rest of this is invalid.** Confirm the acceptance mode is the
   strict rejection sampler and not a "typical", "synthetic" or "block" variant; confirm your
   truncation sampler is applied to the target before the correction. If either is off, you have a
   quality change and you now need an eval, not just a latency test.
2. **Shadow before you A/B.** Replay real traffic through both configurations offline and read the
   per-position curve. This is where you discover that 3% of your traffic is a batch job whose `α`
   is 0.2.
3. **A/B on live traffic, split by request, at real load.** Because the output distribution is
   unchanged, the experiment is a pure systems experiment: no quality eval, no human raters, no
   preference test. That is the cheapest A/B in the whole serving stack and it is a direct
   consequence of the exactness proof.
4. **Alert on `α` per endpoint, not just on latency.** Acceptance drifts when the system prompt
   changes, when a new client onboards with a different workload, when the prompt template gains a
   field, and above all when the target model is upgraded and the drafter is not. Latency alerts
   will fire eventually; the acceptance alert fires on the deploy.

The failure mode to name in an interview is the one that costs real money: a team benchmarks
speculation at batch 1 on a code-completion prompt, sees 2.8×, enables it fleet-wide, and quietly
loses throughput on the chat endpoint at peak — where `α` is 0.65, the batch is 96, and
[256](256-speculative-decoding-at-high-batch.md)'s ceiling has already turned the speedup into a
0.7×. Nothing breaks. Nothing looks wrong. The fleet is just 30% smaller than it should be.

## What an interviewer digs into next

* Why does the per-position acceptance curve tell you more than the mean?
* Why can mean TPOT improve while p99 inter-token latency gets worse?
* What would make you turn speculation off for one endpoint but not another?

## Where this stands, September 2026

The method is durable: instrument the per-position curve, decide on tokens/s per GPU at real
concurrency, and lean on exactness to keep the A/B cheap. That will outlive every drafter named in
this arc. The metric names and fields above were read from the vLLM tree in September 2026 and are
primary for that snapshot; the `α` ranges in the workload table are coverage and expectation, not
measurements, and are the single thing here most likely to be wrong for your traffic. The one
claim I would defend unchanged in five years is the last paragraph: the expensive failure is not a
wrong number, it is a right number measured in a regime nobody serves in.
