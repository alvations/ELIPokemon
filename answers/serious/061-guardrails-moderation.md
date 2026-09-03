---
id: "061"
slug: guardrails-moderation
style: serious
category: safety
difficulty: intermediate
question: "How do you design guardrails and a moderation pipeline?"
tags: [guardrails, moderation, classifiers, defence-in-depth, over-refusal]
---

# Guardrails and moderation

A guardrail is any check outside the model that constrains what goes in or comes out. The design
principle is **defence in depth with graduated response**: multiple cheap layers, each catching what
the previous missed, and a response proportional to confidence rather than a binary block.

```
   user input
       │
   ┌───▼─────────────────┐  ① fast deterministic checks
   │ rules, regex, PII    │     length limits, known-bad patterns,
   │ detection, rate      │     PII redaction, rate limits
   │ limits               │     ~1 ms, catches the obvious
   └───┬─────────────────┘
   ┌───▼─────────────────┐  ② input classifier
   │ small model:         │     policy violation, injection attempt,
   │ harmful? injected?   │     off-topic
   │ off-domain?          │     ~50 ms
   └───┬─────────────────┘
   ┌───▼─────────────────┐  ③ the model, with a system prompt
   │ generation           │     encoding policy + few-shot refusals
   └───┬─────────────────┘
   ┌───▼─────────────────┐  ④ output classifier   ← often the best layer
   │ harmful content?     │     harmful output is easier to detect
   │ PII leak? grounded?  │     than harmful intent
   │ schema valid?        │
   └───┬─────────────────┘
   ┌───▼─────────────────┐  ⑤ deterministic post-checks
   │ schema validation,   │     JSON parses, citations resolve,
   │ citation check,      │     no internal URLs, no secrets
   │ secret scanning      │
   └───┬─────────────────┘
       ▼  response      + ⑥ logging, monitoring, human review queue
```

## Why output filtering carries the most weight

Harmful *intent* is genuinely ambiguous — "how do explosives work?" is a chemistry question, a
novelist's research, or an attack, and the text alone does not distinguish them. Harmful *output* is
much more concrete. Layer ④ therefore usually has better precision and recall than layer ②, and
should not be skipped in favour of aggressive input filtering, which is the common mistake.

## Graduated response

Binary block/allow wastes information. Better:

| Confidence | Action |
| --- | --- |
| Very high | block, log, respond with an explanation |
| High | block, queue for human review |
| Medium | allow with a caveat, or regenerate with stricter instructions |
| Low | allow, log for analysis |

Regeneration is under-used: a borderline response can often be re-produced with a tighter system
prompt rather than refused outright.

## The over-refusal problem

The failure mode nobody measures until it hurts. Every guardrail has a false-positive rate, and false
positives are *invisible* — the user gets a refusal, is annoyed, and leaves. You will never see it in
your incident log.

Therefore: **measure over-refusal explicitly.** Maintain a set of legitimate-but-sensitive-sounding
requests (medical questions, security research, historical violence, mental-health topics) and track
what fraction are wrongly refused. Report it next to the block rate. A system with a 0% harmful
output rate and a 15% false-refusal rate is not safe, it is broken.

## Operational realities

* **Latency budget.** Sequential checks add up. Run input checks in parallel; stream output while
  buffering for the output check, or check in chunks.
* **Cost.** A classifier per request at scale is a real line item. Use a small model.
* **Policy versioning.** Policies change; log which version made each decision, or you cannot audit
  past behaviour.
* **Appeals and feedback.** Users must be able to report a wrong refusal, and those reports must
  reach whoever tunes thresholds.
* **Don't reveal the guardrail's reasoning.** Detailed refusal explanations are a free oracle for
  probing the boundary.

## What an interviewer digs into next

* Why is output filtering usually more effective than input filtering?
* How would you measure over-refusal, and what rate is acceptable?
* How do you keep guardrail latency acceptable when streaming?
* What is the risk of explaining exactly why something was refused?
