---
id: "246"
slug: point-release-model-versions
style: serious
category: open-weights
difficulty: advanced
question: "DeepSeek shipped V4.1-Flash four months after V4-Flash. What does a minor version bump on a model actually promise?"
tags: [versioning, deepseek, evaluation, migration, serving]
---

# Nothing. A model's version number is a product name with a decimal point in it.

A library's version is a claim about compatibility, made against a written scheme, enforced by an
installer. A model's version is a label a marketing team chose. The two look identical in a
planning document and they mean entirely different things, and the cleanest demonstration
available right now is DeepSeek's own **V4-Flash → V4.1-Flash**, which moves a decimal point and
changes almost every field that determines how you serve it.

```
   field                    V4-Flash (0731)        V4.1-Flash        change
   ─────────────────────────────────────────────────────────────────────────────
   announced                24 Apr 2026 preview    10 Sep 2026       ~4.5 months
   total / backbone params  284B                   552B              ×1.94
   active per token         13B, flat              8B prefill        NOT ONE NUMBER
                                                   16B decode        ANY MORE
   modality                 text only              native image+text A NEW INPUT
   reasoning control        discrete modes         continuous dial   DIFFERENT TYPE
   context / max output     1M / 384K              1M                unchanged
   KV cache                 baseline               ≈ ¼ of it         a serving change
   price (reasoning, max)   $0.44 in / $1.32 out   $0.30 / $1.20     per 1M tokens
   Terminal-Bench 2.1       82.7                   90.6              vendor-published
   DeepSWE                  54.4                   74.2              vendor-published
   ─────────────────────────────────────────────────────────────────────────────
   Every figure in this table is COVERAGE, not a reading. See the note below.
```

Look at row two and row three together. The backbone nearly doubled *and* the active-parameter
count went down. Those are not in tension — it is a sparser mixture — but any capacity plan built
on "active parameters" now needs two numbers where it had one, and any cost model built on the
old single number is wrong in both directions at once.

## The asymmetry is the interesting part

An MoE that activates 8B reading and 16B writing has a different cost *shape*, not just a
different cost. Do the FLOPs for a long-context request — 200K tokens in, 1K tokens out — using
the `2 × active_params × tokens` rule of thumb for the dense part:

```
   V4-Flash, flat 13B active
     prefill  2 × 13e9 × 200e3  = 5.20e15 FLOPs
     decode   2 × 13e9 × 1e3    = 2.60e13 FLOPs
                                   ─────────
                          total ≈ 5.23e15

   V4.1-Flash, 8B prefill / 16B decode
     prefill  2 ×  8e9 × 200e3  = 3.20e15 FLOPs     ← 1.6× CHEAPER
     decode   2 × 16e9 × 1e3    = 3.20e13 FLOPs     ← 1.23× DEARER
                                   ─────────
                          total ≈ 3.23e15

   ┌───────────────────────────────────────────────────────────────────┐
   │ A 200K-in / 1K-out workload gets ~38% cheaper in dense FLOPs.     │
   │ A 2K-in / 8K-out workload moves the other way.                    │
   │ The headline "smaller active parameters" is true and is not your  │
   │ number. YOUR number depends on YOUR prompt-to-completion ratio.   │
   └───────────────────────────────────────────────────────────────────┘
```

Add the reported quartering of the KV cache and the long-context case improves again — cache is
what caps your batch size, and batch size is what sets cost per token. None of this is visible
from the string `4.1`.

## So what actually triggers a re-run?

A point bump is a prompt to check, not a licence to skip. Re-run the evaluations when **any** of
these moved, and in this case six of the seven did:

1. **Active-parameter shape** — one number became two, phase-dependent.
2. **Modality** — an image path exists now, so your input validation and your safety filters see
   traffic they did not see before.
3. **The control surface** — discrete reasoning modes replaced by a continuous dial. Your
   existing request parameters may not map at all, and "max effort" in the new scheme is not
   guaranteed to be the old maximum.
4. **Tokenizer or vocabulary** — the cheapest thing to check and the one that silently rewrites
   every token count, every price estimate and every context-window headroom calculation.
5. **Default sampling** — a changed default temperature or top-p moves your eval scores with no
   entry in any changelog.
6. **Serving shape** — a different KV footprint changes throughput, latency and tail behaviour.
7. **The served build string** — `0731` and `0813` are dated builds behind the friendly name.
   Log what answered, not what you asked for.

The honest summary of this particular bump: **it changes the architecture family.** Coverage
describes V4-Flash as a decoder with hybrid attention and V4.1-Flash as a causal
encoder-decoder. Whatever the number says, that is not a patch. It is a new model that inherited
a name.

## Migrating, in the order that saves you

Pin the dated build and keep the old one live. Replay **your** traffic, not the benchmark suite —
the vendor's Terminal-Bench pair, 82.7 to 90.6, is a real claim about a real harness and tells
you nothing about your documents. Re-price at your own prompt-to-completion ratio. Re-read the
licence file rather than assuming the previous release's terms carried over. Re-check `max
output`, because a generation-length regression is the cheapest failure to catch and the most
embarrassing to find in production. Then cut over by traffic fraction, not by date.

## What an interviewer is listening for

That you say "a model version promises nothing" without hedging, and then immediately ask what
*did* change rather than arguing about semantics. That you spot the prefill/decode split as a
change in the shape of the cost curve and can say which workloads win. And that you ask for the
dated build string. Candidates who read `4.1` as "small" have accepted a number in place of a
diff.

## Where this stands, September 2026

**Every DeepSeek figure above is coverage, not a reading.** `deepseek.com`,
`api-docs.deepseek.com` and `huggingface.co` are all blocked by this environment's egress proxy,
so no model card, changelog entry or pricing page was opened first-hand; the parameter counts,
dates, prices and benchmark pairs come from third-party write-ups, several of which are copies of
each other. The authority is DeepSeek's own model cards and API changelog — open them before you
quote any number here. Questions 213–217 cover this family's architecture, licensing and cost
claims; this one is only about the number on the front. The specific release will be superseded
within months. The seven triggers will not.
