---
id: "145"
slug: gui-computer-use-agents
style: serious
category: multimodal
difficulty: advanced
question: "How do agents that operate a computer from screenshots actually work?"
tags: [computer-use, gui-agents, grounding, action-space, osworld, error-recovery]
---

# Agents that drive a screen

A computer-use agent runs a loop: look at the screen, decide on an action, execute it, look again.
Everything hard about it is that **the actions are real** — there is no undo for a sent email — and
that a long task is a long chain where any broken link ends it.

```
   ┌──────────────────────────────────────────────────────────┐
   │  screenshot ─► VLM ─► action ─► executed on the machine  │
   │      ▲                                       │           │
   │      └───────────────────────────────────────┘           │
   │            history of previous steps carried forward       │
   └──────────────────────────────────────────────────────────┘
```

## Pixels or the accessibility tree?

Two ways to perceive the screen, and hybrids beat either.

| | Accessibility tree / DOM | Screenshots |
| --- | --- | --- |
| Precision | exact element bounds and roles | grounding must be learned (question 128) |
| Coverage | misses canvas, custom widgets, images, native apps | sees whatever a person sees |
| Tokens | can be enormous and mostly noise | bounded by resolution |
| Availability | web and some native; absent elsewhere | always |

In practice: use the tree where it exists to get reliable element IDs, use the screenshot for
layout and anything the tree cannot express, and **prefer indexing into a list of detected elements
over emitting raw coordinates**. Set-of-mark prompting (question 128) turns a continuous pointing
problem into a multiple choice, and it is the single biggest accuracy lever available.

## The action space

Keep it small and typed: `click(element_id)`, `type(text)`, `scroll(direction)`, `key(combo)`,
`wait()`, `done()`, `ask_user()`. Two design points that matter more than they look:

* **`wait()` and `ask_user()` are real actions.** Without a wait, the agent acts on a half-loaded
  page. Without an escape hatch, it guesses when it should stop.
* **Actions should be verifiable.** After each step, check the screen changed in the expected
  direction. An agent that cannot tell whether its click landed will cheerfully continue against a
  dialog it did not notice.

## Why long tasks fail

Per-step accuracy compounds. At 95% per step, a 20-step task succeeds 36% of the time. This
arithmetic is the whole story of the field, and it means **error recovery matters more than error
rate**.

The failures, in the order they actually happen:

* **Grounding misses** — clicked next to the button. Mitigated by set-of-mark.
* **State drift** — the agent's belief about where it is diverges from the screen. Mitigated by
  re-reading the screen rather than trusting history, and by keeping an explicit written plan it
  re-checks.
* **Loops** — the same failing action, repeatedly. Detect repetition and force a different branch.
* **Irreversible mistakes.** Sent, deleted, purchased, released. Not recoverable by any retry
  policy, which is why they need a different mechanism entirely: a confirmation gate.
* **Prompt injection from the screen itself** (question 139). Anything the agent reads is untrusted
  data, never an instruction, and this must be enforced architecturally rather than hoped for.

## Evaluation

* **Task success rate, end to end.** Not step accuracy — a run with one wrong step and a recovery is
  a success, and a run with perfect steps that ends in the wrong place is not. OSWorld, WebArena and
  similar environments measure this with execution-based checks rather than string matching, which
  is the right design.
* **Steps taken and cost per task.** An agent that succeeds in 90 steps where a person takes 6 is a
  demonstration, not a product.
* **Failure taxonomy**, not just a number. Which of the categories above dominates tells you what
  to fix; a bare success rate does not.
* **Safety evaluations on the deployment surface**: injected instructions in pages, and refusal
  behaviour on consequential actions.

## What an interviewer digs into next

* Why does per-step accuracy compound so brutally, and what follows from that?
* When is the accessibility tree not enough?
* Why is `ask_user()` an action rather than a failure?
* Why measure task success rather than step accuracy?
