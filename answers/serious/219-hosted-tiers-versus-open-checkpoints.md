---
id: "219"
slug: hosted-tiers-versus-open-checkpoints
style: serious
category: open-weights
difficulty: intermediate
question: "Qwen sells Flash, Plus and Max endpoints and also publishes downloadable checkpoints. Which of those can you actually run yourself?"
tags: [qwen, open-weights, api-products, naming, procurement]
---

# One naming system describes files. The other describes endpoints. They are not aligned.

**Flash, Plus and Max are product tiers on a hosted API.** They are not parameter counts, they
are not checkpoints, and they do not map one-to-one onto anything you can download. The
downloadable artefacts use an entirely different naming system: a parameter count, and for the
sparse ones an active-parameter count after an `A` — `Qwen3.5-397B-A17B`, `Qwen3.8-27B`.

If a Qwen name contains a number, it is probably a file. If it contains an adjective, it is
probably an endpoint. That heuristic is crude and it will still get you further than most of the
coverage does.

## The two ladders, side by side

```
   DOWNLOADABLE  (Qwen team's own repo, "News" list — read directly)
   ────────────────────────────────────────────────────────────────────────
   2025-09-11   Qwen3-Next-80B-A3B
   2026-02-16   Qwen3.5-397B-A17B
   2026-02-24   Qwen3.5-122B-A10B · Qwen3.5-35B-A3B · Qwen3.5-27B
   2026-03-02   Qwen3.5-9B · Qwen3.5-4B · Qwen3.5-2B · Qwen3.5-0.8B
   2026-04-16   Qwen3.6-35B-A3B
   2026-04-22   Qwen3.6-27B
                ┌──────────────────────────────────────────────┐
                │  ← nothing here. No Qwen3.7 weights exist.   │
                └──────────────────────────────────────────────┘
   2026-08-12   Qwen3.8-2.4T-A95B
   2026-08-14   Qwen3.8-27B

   ENDPOINT ONLY  (Alibaba Cloud Model Studio / QwenCloud)
   ────────────────────────────────────────────────────────────────────────
   qwen3.5-flash · qwen3.5-plus · qwen3.6-flash · qwen3.6-plus
   qwen3.7-plus  · qwen3.7-max  · qwen3.8-flash · qwen3.8-max

                     ▲
                     └─ Qwen3.7 shipped Max (May 2026) and Plus (June 2026)
                        as products and never as weights. The open line
                        skipped 3.7 entirely and resumed at 3.8.
```

The 3.7 gap is the proof. If the two ladders were the same ladder, a whole generation could not
exist on one and not the other.

## The trap: "the open weights of Qwen3.8-Max"

The Qwen team's own introduction says Qwen3.8 "brings a Qwen-Max-class model to open release",
and the checkpoint is `Qwen3.8-2.4T-A95B`, released under a licence literally called the
*Qwen3.8-Max License*. Three signals all pointing at the same conclusion, and the conclusion is
wrong: **the checkpoint and the endpoint are different artefacts.** As reported in coverage of the
release and in the model card's own front matter:

| | `Qwen3.8-2.4T-A95B` (file) | `qwen3.8-max` (endpoint) |
| --- | --- | --- |
| Input | text only | text, image, video |
| Thinking | always on; cannot be disabled | switchable |
| Context | 262,144 native, YaRN to ~1,010,000 | 1M by default |
| Tools | whatever you build | server-side built-ins |
| Licence | Qwen3.8-Max License (conditional) | terms of service |
| Identity | a revision hash | a name that moves |

Provisioning hardware from the endpoint's capability page is how teams end up with a rack and no
vision encoder. This is question 210's problem with the volume turned up: the *same name* is being
used for two artefacts that differ in modality, in reasoning behaviour, in default window and in
legal status.

## Three checks that settle it in a minute

1. **Does the name carry a parameter count?** `-27B`, `-397B-A17B`, `-2.4T-A95B` are files.
   `-max`, `-plus`, `-flash` are SKUs.
2. **Is it in the weight-release list?** The lab's repository keeps a dated "News" list of weight
   drops. That list — not a blog post, not a pricing page — is the index of what exists as bytes.
3. **Can you resolve it to a repository id and a revision?** If you cannot name the commit you
   would pin, you are buying a service, and it can change under you between two Tuesdays.

## What each one actually buys

An **endpoint** buys you capability you did not build: multimodal input, a million-token default
window, server-side tools, and somebody else's capacity planning. It costs you inspection,
pinning, air-gapping, and any fine-tune beyond what the platform offers.

A **checkpoint** buys you the bytes: a hash you can pin, a model you can fine-tune, an offline
deployment, and a licence you can read (question 222). It costs you everything the endpoint was
adding — and on the 3.8 pair, that list includes *vision* and *the ability to turn thinking off*,
which are not usually thought of as platform features.

## What an interviewer is listening for

That you do not treat "Qwen3.8 is open" as a sentence with a single truth value. Then that you
ask which artefact the benchmark, the price and the capability list each refer to, because in this
family they routinely refer to three different things. The strongest answers say what they would
record in a decision log: repository id, revision hash, licence file, and the date, so that the
next person is not re-deriving it from a product page.

## Where this stands, September 2026

The weight-release dates and the absence of any Qwen3.7 checkpoint come from the Qwen team's own
GitHub repository, read directly. The endpoint list, the pricing and the file-versus-endpoint
capability differences come from coverage and aggregator pages, because `alibabacloud.com`,
`qwen.ai`, `docs.qwencloud.com` and `huggingface.co` are all blocked from this environment — the
Model Studio catalogue and the model cards are the authorities. Tier names and prices move fastest
of anything here. The structural point — two naming systems, one for files and one for
services — is what transfers.
