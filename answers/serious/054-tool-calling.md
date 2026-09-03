---
id: "054"
slug: tool-calling
style: serious
category: agents
difficulty: core
question: "How does function/tool calling actually work under the hood?"
tags: [tool-calling, function-calling, json-schema, constrained-decoding]
---

# Tool calling under the hood

The most important thing to say first: **the model never executes anything.** It emits structured
text requesting a call. Your code parses it, executes it, and feeds the result back. The model is a
planner with a very restricted output format, not a runtime.

```
   1. You send: messages + tool definitions (JSON Schema)
                     │
   2. Model emits a structured tool-call block:
                     │   { "name": "get_weather",
                     │     "arguments": {"city": "Tokyo", "unit": "c"} }
                     ▼
   3. YOUR CODE validates the arguments and executes the function
                     │
   4. You append the result as a tool-result message
                     ▼
   5. Model continues — either answering, or calling another tool
```

## What actually makes it work

**Training.** Tool use is post-trained. Models are fine-tuned on many examples of (tools available →
correct call → result → continuation), with special tokens delimiting tool-call blocks. Without that
training, a base model asked to emit JSON produces JSON-ish text unreliably.

**The schema is the prompt.** Tool definitions are serialised into the context. The *description
field is the actual instruction* the model follows, and this is where most tool-calling bugs live.
`"Gets data"` is a bad tool description; `"Returns the current weather for a city. Use only for
present conditions — for forecasts use get_forecast."` is a good one. Parameter descriptions,
enums, examples and explicit units all measurably improve selection and argument accuracy.

**Constrained decoding.** To guarantee syntactically valid output, providers mask the logits at each
step to only tokens permitted by the schema's grammar. If the schema says the next token must be `{`
or a specific key, everything else is set to `-∞`. This makes malformed JSON structurally impossible
— though it does *not* guarantee semantic correctness: you can get a perfectly valid object with a
hallucinated city name.

```
   generating:  {"city": "
   grammar says next must be a string, then a closing quote, then , or }
   → mask every token that would break the schema
   → sample from what remains
```

## Design that works

* **Few, distinct tools.** Beyond ~20, selection accuracy drops noticeably. Overlapping tools are
  worse than missing ones.
* **Descriptions written for the model**, including when *not* to use the tool.
* **Enums over free strings** wherever the value set is closed — this eliminates a whole class of
  hallucinated arguments.
* **Return errors as observations**, structured and actionable: `{"error": "city not found",
  "suggestion": "use search_cities first"}` lets the model recover; a stack trace does not.
* **Idempotency and confirmation.** The model will sometimes call a destructive tool twice. Make
  writes idempotent, and gate genuinely irreversible actions behind explicit confirmation.
* **Parallel calls.** Modern APIs allow several independent calls in one turn. Use them — three
  sequential round trips for three independent lookups is pure latency.

## Failure modes

* **Hallucinated arguments** — plausible values for parameters the model has no information about.
  Validate server-side; never trust the arguments.
* **Wrong tool selection** with similar tools — almost always a description problem.
* **Premature answering** without calling the tool at all, especially when the model "knows" the
  answer.
* **Retry loops** on a call that cannot succeed.
* **Injection through tool results.** Tool output enters the context as trusted-looking text. If a
  tool returns attacker-controlled content — a fetched web page, a user-submitted record — it can
  carry instructions. This is the main attack surface of agentic systems (question 059).

## What an interviewer digs into next

* Why does constrained decoding guarantee valid syntax but not valid semantics?
* What makes a good tool description, concretely?
* How would you handle a model that calls a destructive tool twice?
* Why are tool results a security boundary?
