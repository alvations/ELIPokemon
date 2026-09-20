---
id: "222"
slug: open-weight-licence-patchwork
style: serious
category: open-weights
difficulty: advanced
question: "Two checkpoints from the same Qwen release carry different licences. How does that change what you are allowed to build?"
tags: [qwen, licensing, open-weights, compliance, procurement]
---

# Two days apart, one announcement, two completely different deals

`Qwen3.8-2.4T-A95B` was published on **2026-08-12**. `Qwen3.8-27B` was published on
**2026-08-14**. Same family, same launch, same team. The 27B's card declares **Apache 2.0**. The
2.4T's card declares `license: other`, and the file next to the weights is titled **Qwen3.8-Max
License**.

That is not a metadata difference. It is a constraint on what *shape of product* you are permitted
to build, and it is the axis that gets checked last and kills deployments (question 208).

## What the Qwen3.8-Max License actually says

The grant is broad and MIT-shaped. It permits, in its own words, *"use, copy, modify, merge,
publish, distribute, sublicense, sell, deploy, host, fine-tune, and create derivative works
from"* the weights. Then two conditions:

```
   ┌─ CONDITION 1 — attribution, at scale ────────────────────────────────┐
   │  If the Software (or derivative works) is used for a commercial      │
   │  product or service with                                             │
   │        > 100,000,000  monthly active users     OR                    │
   │        > US$ 20,000,000  monthly revenue                             │
   │  the model name must be PROMINENTLY DISPLAYED on that product's UI.  │
   └──────────────────────────────────────────────────────────────────────┘

   ┌─ CONDITION 2 — a separate licence, at scale, for two businesses ─────┐
   │  If you or your affiliates run a                                     │
   │        "Model as a Service"    OR    "AI Work Assistant"  business   │
   │  and your aggregate revenue exceeds US$ 50,000,000 over ANY          │
   │  consecutive twelve months, you must obtain a separate licence from  │
   │  Qwen before ANY commercial use of the weights or their derivatives. │
   │                                                                      │
   │  Carve-out: internal use is exempt — provided the Software, its      │
   │  OUTPUTS, or its underlying model CAPABILITIES are not made          │
   │  available to any third party.                                       │
   └──────────────────────────────────────────────────────────────────────┘

        Model as a Service  = giving third parties access to inference or
                              fine-tuning where THEY control inputs,
                              parameters or training data.
                              Merely relaying requests to someone else's
                              hosted model is explicitly NOT this.

        AI Work Assistant   = an independent product primarily for
                              AI-assisted coding or office productivity.
                              NOT: single-purpose tools (a translation
                              tool is the licence's own example), nor
                              assistants for other domains, nor an AI
                              feature inside a product that is about
                              something else.
```

The conditional checkpoint is not the weaker artefact — the 2.4T is by far the stronger model of
the two. That is exactly what makes the licence an engineering decision rather than a filter: the
cheaper terms and the better model are on different files.

## Five ways that lands on an engineering decision

**1. It is a roadmap constraint, not a footnote.** Both checkpoints are downloadable. Only one of
them can become an inference API you sell at any scale. If "we might offer this as an endpoint"
is on the roadmap, the licence has already chosen your checkpoint for you.

**2. Derivatives inherit, and "derivative" is broad here.** The text says *"the Software or its
derivative works"*. A LoRA adapter, a full fine-tune, a distilled student trained on the weights,
a community GGUF — all of them carry the condition. Pulling a quantised re-upload from a third
party does not launder it.

**3. The carve-outs are drawn on product category, which is not a technical fact.** "Primarily
designed for AI-assisted coding or office productivity" is a positioning question. A code-review
bot is squarely inside the named category. A translation tool is explicitly outside it. An AI
feature inside a CRM is outside it. Where your product sits is decided by how it is sold, which
means the people who answer it do not work in engineering.

**4. The internal-use carve-out is narrower than it reads.** It survives only while the outputs
and the *underlying model capabilities* stay away from third parties. An internal tool whose
generated text is emailed to customers has left the carve-out, and nothing in your architecture
changed.

**5. Relaying is exempt, and that is a real architectural fork.** Proxying to somebody else's
hosted Qwen is explicitly not Model as a Service under this text. Host the weights yourself and
you are in scope. That is a licence clause that prices a build-versus-buy decision.

## The rule this generalises to

**Pin the licence to the artefact, not to the family name.** "Qwen is Apache" was a reasonable
sentence for the Qwen3 series — that repository's README stated flatly that *"All our open-weight
models are licensed under Apache 2.0."* The Qwen3.8 repository's Licence section says only
*"Please find the license file released with the model weights."* The disappearance of the blanket
claim is the whole story, and it appears nowhere in a benchmark table.

Concretely, in the artefact registry: repository id, revision hash, the card's `license:` field,
and a stored copy of the LICENSE file *at the revision you pulled*, diffed on every bump. A
licence can change between revisions of the same repository, and a name tells you nothing —
question 210.

Also: **open weights is not open source.** This grant is permissive in scope and conditional in
application. It would not clear the Open Source Definition, and saying "open source" in a customer
deck about it is a claim you cannot support.

## What an interviewer is listening for

That licence review happens at the *start* of a model evaluation, not after the benchmarks come
back. Then that you can name which clause bites at which business shape, rather than saying "it's
restrictive". The strongest answers observe that the two Qwen3.8 checkpoints are not substitutable
even where their quality would allow it — the 27B is Apache and the 2.4T is not — so "which is
better" and "which can we ship" are different questions with different answers.

## Where this stands, September 2026

The licence clauses above are quoted from the LICENSE file distributed with the weights, read
through a verbatim third-party reproduction because `huggingface.co` is blocked from this
environment; two independent reproductions agree word for word, and the file in the model
repository is the authority. The `license: apache-2.0` and `license: other` card fields and the
two release dates come from the same evidence set plus the Qwen team's own repository, read
directly. **Nothing here is legal advice** — the thresholds, the definitions and the carve-outs
are exactly the sort of text that a lawyer reads differently from an engineer, and the licence
names a contact address for precisely that reason. Licences get revised. Re-read the file.
