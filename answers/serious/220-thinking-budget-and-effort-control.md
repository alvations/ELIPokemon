---
id: "220"
slug: thinking-budget-and-effort-control
style: serious
category: open-weights
difficulty: advanced
question: "Qwen controls reasoning with a thinking switch, a token budget and an effort level. How does that differ from a single effort dial?"
tags: [qwen, reasoning-effort, thinking-budget, latency, prompt-caching]
---

# A cap and a disposition are different instruments, and Qwen ships both

Qwen has now run this experiment in public three times, and the sequence is the argument.

**Round one (Qwen3, 2025): one checkpoint, hybrid.** A boolean `enable_thinking`, soft `/think`
and `/no_think` switches in the prompt, and a `thinking_budget` — reported on the hosted platform
as an integer from 1 to 32768 with a default of 4000 — capping chain-of-thought tokens.

**Round two (the 2507 refresh, 2025): the hybrid was abandoned.** Qwen shipped *separate* Instruct
and Thinking checkpoints instead, on the stated grounds that training one model to be direct and
to reason at length pulls the objective in two directions and both halves end up worse.

**Round three (Qwen3.6 / Qwen3.8, 2026): one checkpoint again, with a named level.** The Qwen3.8
repository's own feature list reads: *"Reasoning depth can be tuned with `reasoning_effort`, and
reasoning context from historical messages is retained via `preserve_thinking`."* Qwen3.6
introduced the preservation half as "Thinking Preservation".

So the current interface is **two instruments, not one**: a *disposition* (`reasoning_effort`)
and, where the platform exposes it, a *cap* (`thinking_budget`). Question 204 describes a family
that exposes only the disposition, with `max_tokens` as the single hard ceiling over thinking plus
response together. The difference matters more than it sounds.

```
   DISPOSITION                                CAP
   ─────────────────────────────────          ──────────────────────────────────
   reasoning_effort = low|medium|xhigh        thinking_budget = 1 .. 32768
   "how hard should you try"                  "you may spend this many tokens"

   shapes the whole response:                 stops the clock:
     · how long it thinks                       · mid-chain, wherever it is
     · how many tool calls it makes             · answer produced from an
     · how much preamble it writes                unfinished deliberation

   degrades gracefully                        does NOT degrade gracefully
   ──────────────────────────────────────────────────────────────────────────────

        effort:      low          medium                    xhigh (default)
                      │             │                             │
   thinking          ▏            ▎▎▎                        ████████████
   wall clock        ▏            ▎▎▎                        ████████████
                                                                   ▲
   budget cap  ─────────────────────────┤                          │
                                        └─ truncation lives here,  │
                                           and a truncated chain   │
                                           is a THIRD population,  │
                                           not a shorter one ──────┘
```

## Three things about this interface that catch people out

**1. The level names are not a standard, and a wrong one is a 500, not a worse answer.** Issue
#217 on the Qwen team's own repository reports exactly this: the Qwen3.8-27B chat template raises
on an unknown level, and the error text is `Unexpected reasoning effort high. Supported types are
xhigh (default), medium, and low.` Three levels. **`high` is not one of them** — and `high` is the
default an agent harness built against a different family will send. This is an integration test,
not a quality sweep, and it fails deterministically on the first request.

**2. The default is `xhigh`.** That is the top of the range, shipped on. Coverage of local
deployments reports single trivial tasks consuming over twenty-two thousand reasoning tokens and
tens of minutes on consumer hardware. A default selected to look good on a benchmark table is an
expensive production default, and the fix is one line — but you have to know to write it.

**3. Some checkpoints have no off switch.** The open `Qwen3.8-2.4T-A95B` is reported as always
reasoning: `enable_thinking=false` is not supported on the weights, although the hosted
`qwen3.8-max` endpoint does offer a non-thinking mode. "The same model" has a switch in one form
and not in the other (question 219).

## How to actually tune it

1. **Decide whether you need the cap at all.** A budget is a latency SLO or a cost ceiling. It is
   not a quality control, and it is not a cheaper way to spell "think less" — that is the
   disposition's job. Reach for the cap only when a hard bound is a product requirement.
2. **Set the disposition per workload, not per request.** Extraction, routing and subagent calls
   sit at `low`; long-horizon agentic coding is what `xhigh` is for. Sweep it on your own evals
   starting from the default and stepping *down*, exactly as in question 204.
3. **Report the truncation rate as a first-class metric.** If a non-zero fraction of requests hit
   the budget, your quality number is an average over two different behaviours and the aggregate
   hides which one is moving.
4. **Pin the level strings per model id, and test them.** Not per family, not per vendor. These
   are template-level strings and they change between checkpoints.
5. **Watch the cache when `preserve_thinking` is on.** Carrying prior `reasoning_content` into the
   next request grows the prefix every turn. It buys continuity in iterative work and it costs
   prompt length; on a long agent loop those two facts fight.

## What an interviewer is listening for

That you separate "how hard" from "how long" and can say which of your requirements is which.
Then that you treat the level vocabulary as an interface contract that needs a test, rather than a
knob you tune. The strongest answers notice that Qwen removed the hybrid interface and then
brought it back in a different shape, and read that as evidence that the trade-off is real rather
than as indecision: the 2507 split bought quality by giving up the control, and the effort level
is an attempt to get the control back without paying that price again.

## Where this stands, September 2026

The `reasoning_effort` and `preserve_thinking` features, and the Qwen3.6 "Thinking Preservation"
description, are quoted from the Qwen team's own GitHub repository, read directly; the exact
rejected-level error string is from issue #217 in that same repository. The `thinking_budget`
range and default, the `xhigh` default, the overthinking reports and the always-on behaviour of
the 2.4T weights come from coverage and community reports, because the developer documentation
and the model cards are blocked from this environment — those pages are the authority. Parameter
names and level vocabularies are the single most volatile thing in this answer. The
cap-versus-disposition distinction is not.
