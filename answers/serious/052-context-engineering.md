---
id: "052"
slug: context-engineering
style: serious
category: prompting
difficulty: intermediate
question: "What is context engineering, and how is it different from prompt engineering?"
tags: [context-engineering, prompt-engineering, agents, context-rot, memory]
---

# Context engineering

Prompt engineering is writing good instructions. **Context engineering is deciding what occupies the
context window at each step** — a systems problem rather than a wording problem. The shift in
terminology tracks a real shift in what matters: once you are building agents that run for many
turns with tools and retrieved documents, the instructions are a small fraction of what the model
sees, and everything else is being assembled by your code.

```
  ┌── THE CONTEXT WINDOW: a scarce, contested resource ────────────────┐
  │                                                                    │
  │  system prompt / role         ← stable, cacheable                  │
  │  tool definitions             ← grows with every tool you add      │
  │  retrieved documents          ← the biggest and most variable      │
  │  conversation history         ← grows without bound                │
  │  tool call results            ← can be enormous (logs, API dumps)  │
  │  scratchpad / plan state      ← the agent's working memory         │
  │  the actual user request      ← often the smallest part            │
  │                                                                    │
  │  every token competes with every other token for attention         │
  └────────────────────────────────────────────────────────────────────┘
```

## Why it is the harder problem

**Context rot.** Quality degrades with length even far inside the advertised window: instructions
placed early compete with everything since, mid-context material is attended to poorly (question
013), and each additional distractor is another opportunity to be misled.

**Cost and latency are linear in prefill.** A 100k-token context is not "free because it fits".

**Tool results are unbounded.** A single `grep` or API call can return 50k tokens of noise. Naïvely
appending tool output is the most common way agents die.

**Multi-turn accumulation.** Twenty turns of an agent loop, each appending observations, and turn 20
is reasoning over a context mostly composed of stale intermediate state.

## The techniques

* **Compaction / summarisation.** When the context approaches a threshold, summarise the older
  portion into a compact state and continue. Essential for long agent runs; the risk is summarising
  away a detail that mattered.
* **Structured note-taking.** Have the agent maintain an explicit external artifact (a plan file, a
  todo list, a findings document) rather than relying on conversation history as memory. Persists
  across compaction, and is inspectable.
* **Just-in-time retrieval.** Load identifiers and paths, not contents; fetch the content only when
  needed. Mirrors how a human works with a filesystem.
* **Tool result truncation and filtering.** Cap tool output, paginate, and prefer tools that return
  summaries with drill-down over tools that return everything.
* **Sub-agents.** Delegate a bounded investigation to a fresh context and return only the conclusion.
  The parent never sees the 100k tokens of intermediate exploration.
* **Prompt caching.** Order the context stable-prefix-first (system, tools, then variable content) so
  the cacheable portion is a genuine prefix. This is both a latency and a cost decision, and it
  constrains layout.
* **Tool curation.** More tools means more tokens and more confusion. Overlapping or ambiguously
  described tools measurably degrade selection accuracy.

## The design principle

> Find the **smallest set of high-signal tokens** that maximises the probability of the desired
> outcome.

Not "use the whole window because we have it". Every token you add has a cost in money, latency, and
— crucially — in attention diluted away from the tokens that mattered.

## What an interviewer digs into next

* How would you keep a 50-turn agent within a context budget?
* What are the risks of automatic compaction, and how would you mitigate them?
* Why does prompt-cache-aware ordering constrain your context layout?
* Why can adding a tool make an agent worse?
