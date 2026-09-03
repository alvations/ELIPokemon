---
id: "053"
slug: react-agents
style: serious
category: agents
difficulty: core
question: "What is ReAct, and what is the anatomy of an LLM agent?"
tags: [react, agents, tool-use, agent-loop, planning]
---

# ReAct and the anatomy of an agent

**ReAct** ([Yao et al., 2022](https://arxiv.org/abs/2210.03629)) interleaves *reasoning* and
*acting* in one loop, rather than doing one then the other.

```
   ┌──────────────────────────────────────────────────────────────┐
   │  THOUGHT   "I need the current price. I should search."       │
   │  ACTION    search("NVDA stock price")                         │
   │  OBSERVE   "$847.32 as of 2026-09-03"                         │
   │  THOUGHT   "Now I need the P/E ratio to compare."             │
   │  ACTION    get_financials("NVDA")                             │
   │  OBSERVE   {...}                                              │
   │  THOUGHT   "I have enough. Let me answer."                    │
   │  ANSWER    ...                                                │
   └──────────────────────────────────────────────────────────────┘
        ▲                                                    │
        └──────────────── loop until done or budget ─────────┘
```

The two halves fix each other's failures. Pure reasoning (chain-of-thought) hallucinates facts and
cannot check anything. Pure acting (tool calls without reasoning) has no plan and no way to recover
from an unexpected result. Interleaving means observations ground the reasoning, and reasoning
decides the next action in light of what just came back.

## The anatomy

Every agent, regardless of framework, has five parts:

| Component | What it is | Where it goes wrong |
| --- | --- | --- |
| **Model** | the reasoning and decision engine | weak models loop or give up |
| **Tools** | typed functions with descriptions | ambiguous or overlapping tools |
| **Loop** | the orchestrator: call, execute, append, repeat | no termination or budget |
| **Context/memory** | what the model sees each turn | unbounded growth, stale state |
| **Termination** | when to stop | the most neglected component |

The loop itself is about twenty lines of code. Everything hard is in the other four.

## What actually breaks in production

**1. No termination condition.** The classic failure: an agent that never decides it is done, or
oscillates between two actions. Always enforce a hard step budget, a wall-clock timeout, and a cost
ceiling. Detect repeated identical actions and break.

**2. Error handling.** Tools fail — timeouts, rate limits, malformed arguments. Return the error *as
an observation* so the model can adapt, rather than crashing the loop. But cap retries: models will
happily retry an impossible call twenty times.

**3. Context growth.** Every observation is appended. By step 30 the context is mostly stale tool
output. This is where context engineering (question 052) becomes the binding constraint —
summarisation, truncation, and sub-agents.

**4. Compounding error.** With per-step reliability `p`, a 20-step task succeeds with probability
`p²⁰`. At `p = 0.95` that is 36%. **This arithmetic is the single most important thing to
understand about agents**: reliability must be very high per step, or tasks must be short, or the
agent needs verification and recovery at each step.

**5. Tool proliferation.** Beyond ~15–20 tools, selection accuracy degrades. Group tools, use
namespacing, or route to sub-agents with smaller tool sets.

## Variants

* **Plan-and-execute** — plan fully up front, then execute. Fewer model calls, cheaper, brittle when
  reality diverges from the plan.
* **Reflexion** — after failure, generate a written critique and retry with it in context.
* **Tree-of-thought / LATS** — search over action sequences with backtracking. Expensive, better on
  hard search problems.
* **Multi-agent** — specialised agents with a coordinator (question 056).
* **Native tool-calling loops** — modern models are post-trained for tool use, so the explicit
  "Thought:/Action:" text scaffolding of original ReAct is largely obsolete; the structure is now in
  the model's trained behaviour and the API's message format.

That last point is worth making explicitly: ReAct's *pattern* won so thoroughly that it stopped
being a prompting technique and became part of how models are trained and how APIs are shaped.

## What an interviewer digs into next

* Why interleave reasoning and acting rather than planning first?
* Work out the success probability of a 20-step agent at 95% per-step reliability.
* How would you stop an agent from looping?
* At what point do you split one agent into several?
