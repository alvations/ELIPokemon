---
id: "201"
slug: system-one-models
style: serious
category: frontier
difficulty: intermediate
question: "What is a System One model, and when would you reach for one instead of an LLM?"
tags: [system-one, non-autoregressive, classification, latency, jev]
---

# A model that returns a decision, not a paragraph

A System One model is a transformer that does not generate text. You hand it unstructured state
plus a question whose answer space you have **enumerated in advance**, and it returns a
distribution over that enumeration in a single forward pass. TypeSafe AI's Jev, released in
September 2026, is the first widely discussed example; the class name is theirs, after
Kahneman's fast, automatic System 1.

The distinction that matters is not "small versus large". It is **autoregressive versus not**. An
LLM decodes one token at a time, and each token is conditioned on the ones before it, so latency
scales with how much it says and the output space is every string the tokenizer can spell. A
System One model scores every option in your schema in parallel, once, so latency is a constant
that depends on the input, not the answer.

## The mechanism

```
  LLM (autoregressive)                    System One (single pass)
  ────────────────────                    ────────────────────────
  state ─► [ decode t1 ]                  state ────┐
             │                            schema ───┤
             ▼                                      ▼
           [ decode t2 ]                   ┌──────────────────┐
             │                             │  encoder stack   │
             ▼                             └────────┬─────────┘
           [ decode t3 ] … tN                       ▼
             │                              ┌───────────────┐
             ▼                              │ scoring head  │  one pass,
      "the user seems to want a refund,"    └───────┬───────┘  all options
      then JSON-parse, then hope                    ▼
                                            refund   0.81
   cost ∝ tokens produced                    escalate 0.14
   answer ∈ every string                     ignore   0.05
                                            cost ∝ input only
                                            answer ∈ your enum, always
```

The published primitives are narrow on purpose: a **Choice** over labelled options, a **Score**
on a bounded scale, and a nullable variant for "the state does not support an answer". Anything
you cannot phrase that way is not a System One problem.

## When it is the right tool

The shape to look for is **high-volume, repeated decisions over a shared state where the
options are known before the request arrives**: routing a ticket, deciding whether a retrieval
hit is relevant, gating a tool call, flagging a transaction, choosing the next step in a
workflow. These are places where teams currently call a chat model, ask for JSON, and then write
a parser and a retry loop — paying generation latency and generation prices for what is
structurally a classification.

The economics follow from the architecture rather than from a discount. Jev is priced at
$0.042 per million input tokens with output free, because there is almost no output; TypeSafe
reports 40–200× speedups against frontier LLMs on comparable tasks. Treat vendor speedup ranges
as marketing until you measure your own workload, but the *direction* is a property of the
design, not a claim.

## When it is the wrong tool

* **You need the reasoning, not just the verdict.** No chain of thought, no explanation, no
  argument you can show a reviewer. If an auditor has to read *why*, this is not your model.
* **The option set is genuinely open.** Summarisation, drafting, code. Enumerate those and you
  have destroyed the task.
* **The schema is the hard part.** A badly cut set of options is an unfixable bug: the model
  cannot tell you that the right answer was not on the list unless you gave it the null option.
* **You wanted a single model.** In practice this is a two-model architecture — a fast decider in
  the loop, an LLM behind it for the cases the decider is unsure about. That is more moving
  parts, not fewer.

## What an interviewer is listening for

That you can say what changes structurally — parallel scoring over a closed set versus
sequential decoding over an open one — instead of repeating a benchmark. And that you reach for
the confidence number: a distribution over options is only worth more than a label if you use
the number to route, and most teams throw it away.

## Where this stands, September 2026

Jev is a hosted API with open-source client SDKs (TypeScript, Python, Go, Rust) and community
directories of integrations; **the weights are not open.** The idea is older than the product —
encoder classifiers have always worked this way — and what is new is the packaging and the
calibration training (question 202), not the discovery that classification is faster than
generation.
