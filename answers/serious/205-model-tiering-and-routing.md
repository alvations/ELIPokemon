---
id: "205"
slug: model-tiering-and-routing
style: serious
category: frontier
difficulty: intermediate
question: "Frontier families now ship three or four tiers that share a context window. What actually differs, and how do you route between them?"
tags: [routing, cascades, cost, model-selection, tiering]
---

# When the spec sheet is identical, the difference is capability

Both major families now ship a tier ladder. OpenAI's GPT-5.6 generation is Sol, Terra and Luna;
Anthropic's current lineup runs Claude Fable 5.1, Claude Opus 5, Claude Sonnet 5 and Claude
Haiku 4.5. The instructive thing about the GPT-5.6 tiers is that **all three carry the same
1.05M-token context window and the same 128K max output** — the ladder is not a ladder of window
sizes. Anthropic's is nearly the same story: Fable 5.1, Opus 5 and Sonnet 5 all sit at 1M in and
128K out, and only Haiku 4.5 is smaller at 200K and 64K.

So the tiers differ on exactly two things you can see — **price** and **capability** — plus a
third you can only find by measuring: how the failure rate is distributed across *your* traffic.

## The cascade, and why it is not free

The standard move is a cascade: try the cheap tier, detect a bad answer, escalate. The arithmetic
is less flattering than it first looks.

```
   naive:      cost = C_big

   cascade:    cost = C_small + (1 - p) × (C_small_wasted + C_big + C_verify)
                            │                     │
                            │                     └─ the cheap call is not
                            │                        refunded when you escalate
                            └─ p = fraction the cheap tier gets right

   Break-even on a 25:1 price ratio (Luna → Sol, roughly) needs p well above
   0.9 once you count the verifier, and every point of p you lose costs twice:
   once in money, once in the added latency of a second round-trip.

   ┌──────────┬─────────┬──────────┬──────────────────────────────────┐
   │ tier     │ window  │ rel. $   │ what it is actually for          │
   ├──────────┼─────────┼──────────┼──────────────────────────────────┤
   │ top      │  same   │  25×     │ the 2% that decides the product  │
   │ middle   │  same   │  10×     │ production default               │
   │ bottom   │  same   │   1×     │ routing, extraction, subagents   │
   └──────────┴─────────┴──────────┴──────────────────────────────────┘
```

## How to route, in order of how well it works

1. **By workload, statically.** Boring and effective. Extraction, classification and subagent
   work go to the bottom tier; the user-facing reasoning path goes to the middle; the top tier is
   reserved for a named list of hard cases. Most of the achievable saving is here.
2. **By a cheap difficulty signal computed before the call.** Input length, whether tools are
   needed, whether the request matches a known-hard pattern. Crude, but it costs nothing.
3. **By verification after the call.** Only worth it where verification is genuinely cheaper than
   generation — schema checks, unit tests, a retrieval-grounded citation check. An LLM judge at
   the same tier as the generator is not a saving.
4. **By calibrated self-report.** Attractive, and the weakest in practice: models are poor
   at knowing when they are wrong, which is the argument behind purpose-built calibrated
   decision models (question 202).

## What people get wrong

* **Benchmarking the tiers on public evals instead of their own traffic.** The published gap
  between tiers is an average over a distribution that is not yours.
* **Forgetting the effort dial.** A middle tier at high effort and a top tier at low effort are
  two different points, and the cross-over is workload-specific (question 204).
* **Ignoring the cache.** Routing the same conversation between tiers throws away the prompt
  cache on every hop. A cascade that switches models mid-session can cost more than never
  cascading.
* **Treating latency as a constant.** The bottom tier is not just cheaper; on interactive paths
  its latency is often the whole reason to use it.

## What an interviewer is listening for

That you notice the window is the same and ask what is actually different. Then the cascade
arithmetic, including the un-refunded first call and the verifier. The strongest answers say
which fraction of traffic they would put where **and** how they would measure whether the split
was right — escalation rate, per-tier error rate, and cost per successful task rather than cost
per call.

## Where this stands, September 2026

Tier names, prices and windows move every few months; the figures above are as published in
September 2026 and should be re-checked before anyone builds a budget on them. The structural
observation — that vendors now differentiate on capability at a fixed window — is the part worth
remembering.
