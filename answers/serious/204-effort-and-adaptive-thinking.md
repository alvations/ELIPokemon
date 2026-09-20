---
id: "204"
slug: effort-and-adaptive-thinking
style: serious
category: frontier
difficulty: intermediate
question: "Modern reasoning models expose an effort dial instead of a thinking-token budget. How do you tune it?"
tags: [effort, adaptive-thinking, inference-cost, prompt-caching, latency]
---

# A dial that moves every output token, not a budget

The older interface was explicit: turn thinking on, give it `budget_tokens`, and the model spends
up to that. The current Claude models replace it with **adaptive thinking** — the model decides
whether and how long to think — steered by a single `output_config.effort` value with five
levels: `low`, `medium`, `high` (the default), `xhigh` and `max`. Claude Opus 5, Claude Sonnet 5
and Claude Fable 5.1 all take it; Claude Haiku 4.5 does not.

Three properties of that dial catch people out.

**It is a behavioural signal, not a cap.** Low effort does not forbid thinking. A genuinely hard
problem still gets thought about; it gets thought about *less than the same problem would at
`high`*. If you need a hard ceiling, that is `max_tokens`, which bounds thinking **plus** visible
response together — which is why running at `xhigh` with a small `max_tokens` truncates the answer
rather than the reasoning.

**It moves the whole response, not just the thinking.** Tool calls included. At lower effort a
model batches operations into fewer calls, drops the preamble and confirms tersely; at higher
effort it explains the plan first and summarises after. For an agent loop, effort is as much a
control over *how many tool calls you pay for* as over how long it thinks.

**It is not a verbosity control.** On Claude Opus 5, lowering effort does not reliably shorten the
visible answer — it lowers thinking volume. If you want a shorter reply, ask for one in the
prompt.

```
      effort:   low        medium        high        xhigh        max
                │            │            │            │           │
   thinking     ▏           ▎▎           ▍▍▍▍        ▊▊▊▊▊▊▊     ████████
   tool calls   ▏▏          ▎▎▎          ▍▍▍▍▍       ▊▊▊▊▊▊      ███████
   latency      ▏           ▎▎           ▍▍▍         ▊▊▊▊▊       ███████
   quality      ▔▔▔▔▔▔▔▔▁▁▁▁▁▁▁▁▔▔▔▔▔▔▔▔▁▁▁▁▁▁▁▁▔▔▔▔▔▔▔▔▁▁▁▁▁▁▁▁▔
                ╰── task-dependent: the curve flattens somewhere,
                    and where it flattens is what your evals are for

   max_tokens ────────────────────────────────────► hard ceiling on
                                                    thinking + response
```

## How to actually tune it

1. **Sweep it on your own evals.** Start at the default and step down until quality breaks, rather
   than starting low and hoping. Settings carried over from a previous model generation are not
   transferable — re-run the sweep after any model change.
2. **Split by workload, not by request.** Coding and long-horizon agentic work sit high; routing,
   extraction and summarisation usually hold at `low` or `medium`. Subagents are the classic
   `low` case.
3. **Mind the prompt cache.** Changing the top-level effort between requests re-renders the prompt
   and **invalidates the cached prefix**. On models that support per-message effort, an
   effort-only system message changes the level from the next turn while keeping the cache. On
   models that do not, pick a level at the start of a session and hold it.
4. **Raise effort instead of prompting around shallowness.** If reasoning looks thin on a hard
   problem, the dial is the fix. Adding "think carefully" at `low` is a workaround for a setting
   you could have changed.
5. **At `xhigh` and `max`, set `max_tokens` generously.** 64k is a reasonable starting point for
   agentic work. And note that on Claude Opus 5, thinking cannot be disabled at those levels at
   all — the request is rejected.

## Failure modes

* **Overthinking.** On structured-output and low-intelligence-sensitivity tasks, `max` can cost
  substantially more for no measurable gain, and occasionally does worse.
* **Effort as a cost lever with no eval behind it.** Dropping to `low` across the board looks like
  a 3× saving on the invoice and shows up as a quality regression nobody attributes to it.
* **Confusing the two controls.** `adaptive` is a thinking mode, not an effort level; passing it
  as one is an error.

## What an interviewer is listening for

That you treat inference-time compute as a **tunable axis with its own eval**, not a checkbox.
The strongest answer connects it to caching and to tool-call volume, because in an agent those
dominate the bill long before thinking tokens do.

## Where this stands, September 2026

Level names, defaults and per-model support are documented and change with each generation;
check the current docs rather than a remembered table. The transferable idea — one dial over
inference-time compute, swept against your own evals — is not specific to any vendor.
