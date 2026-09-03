---
id: "056"
slug: multi-agent-systems
style: serious
category: agents
difficulty: advanced
question: "When is a multi-agent system worth it, and how do you design one?"
tags: [multi-agent, orchestrator, context-isolation, coordination]
---

# Multi-agent systems

Start from scepticism. A multi-agent system is more expensive, harder to debug, and slower than a
single agent, and most of the time a single well-designed agent with good tools wins. The question is
what specifically justifies the complexity.

## The three real justifications

**1. Context isolation.** The strongest argument. A sub-agent explores 100k tokens of documentation
and returns a 500-token summary; the parent never sees the 100k. This directly addresses the binding
constraint of long agent runs (question 052) and is the reason most successful multi-agent designs
exist.

**2. Parallelism.** Genuinely independent subtasks — researching five competitors, checking eight
files, testing four hypotheses — run concurrently. Wall-clock time drops roughly by the fan-out
factor.

**3. Specialisation.** Different subtasks want different tools, prompts, or models. A cheap model can
triage while an expensive one handles the hard branch.

## The topologies

```
   ORCHESTRATOR-WORKER              PIPELINE
   ───────────────────              ────────
        ┌────────┐                   ┌───┐   ┌───┐   ┌───┐
        │ lead   │                   │ A │──►│ B │──►│ C │
        └───┬────┘                   └───┘   └───┘   └───┘
       ┌────┼────┐                   fixed sequence, easy to
       ▼    ▼    ▼                   reason about and test
     ┌──┐ ┌──┐ ┌──┐
     │w1│ │w2│ │w3│                  DEBATE / CRITIC
     └──┘ └──┘ └──┘                  ───────────────
   most common; lead decomposes,      ┌──────┐   ┌────────┐
   workers execute in parallel,       │ gen  │◄─►│ critic │
   lead synthesises                   └──────┘   └────────┘
                                      quality via adversarial review
```

Orchestrator-worker is the default for a reason: it maps onto the parallelism and context-isolation
arguments directly, and it keeps a single point of synthesis.

## Where they fail

* **Coordination overhead.** Each hop costs tokens and latency. A three-layer hierarchy can spend
  more on coordination than on work.
* **Error compounding across agents.** Same arithmetic as question 053, now with handoffs — and a
  misunderstanding at the handoff propagates silently.
* **Instruction dilution.** The lead's intent degrades as it is paraphrased down the chain. The
  standard fix is to make sub-agent task descriptions extremely specific: objective, output format,
  tools available, and explicit scope boundaries.
* **Cost.** Multi-agent research systems reportedly use on the order of 15× the tokens of a single
  chat turn. That is defensible for high-value work and absurd for routine tasks.
* **Debuggability.** Non-deterministic, concurrent, multi-context. Tracing is not optional.
* **Shared-state conflicts.** Parallel agents writing to the same files or resources need
  coordination you have to build.

## Design rules that hold up

1. **One writer.** Parallel agents should read freely and have a single agent perform writes, or
   write to disjoint resources. Concurrent edits to shared state are the top source of
   multi-agent bugs.
2. **Specify sub-tasks completely.** Objective, expected output shape, tool list, boundaries. Vague
   delegation produces duplicated and conflicting work.
3. **Return summaries, not transcripts.** The whole point is context isolation; returning full
   histories defeats it.
4. **Bound everything** — per-agent step budgets, total cost ceilings, timeouts.
5. **Prefer read-only parallelism.** Fan out for investigation, converge for action.
6. **Trace every agent** with a correlation id, or you will never debug it.

## The honest heuristic

> Use one agent until you can name the specific constraint a second one relieves. If the answer is
> "the context is full" or "these five things are independent", you have a case. If it is "it feels
> more modular", you do not.

## What an interviewer digs into next

* What is the strongest argument for a sub-agent, and why is it about context?
* How do you stop parallel agents from conflicting?
* How would you write a sub-agent task description?
* When is a pipeline better than an orchestrator?
