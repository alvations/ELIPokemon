---
id: "203"
slug: constrained-output-and-hallucination
style: serious
category: frontier
difficulty: advanced
question: "If a model can only emit options from a fixed schema, has hallucination been solved?"
tags: [hallucination, constrained-decoding, schema, type-safety, abstention]
---

# Well-typed is not the same as true

The claim attached to typed decision models — that they **cannot hallucinate**, as a
mathematical property rather than a training outcome — is precisely true about one thing and
quietly false about the thing people care about.

What it guarantees is real: the output is drawn from an enumeration you wrote, so there is no
invented enum value, no malformed JSON, no fabricated function name, no citation string that
looks like a DOI and is not. An entire tier of production engineering — parse, validate, retry,
repair — stops existing. That is worth paying for.

What it does not guarantee is that the option it picked is **the right one**. In a generation
setting we call an unsupported assertion a hallucination. In a decision setting the exact same
failure is "confidently returned `refund` for a message that was asking about delivery". The
schema constrained the *form* of the error, not its existence.

## The two axes people collapse into one

```
                     │  TRUE of the state      │  FALSE of the state
   ──────────────────┼─────────────────────────┼──────────────────────────
    WELL-TYPED       │  what you wanted        │  ◄── STILL A WRONG ANSWER
    (in the schema)  │                         │      the schema cannot
                     │                         │      see this column
   ──────────────────┼─────────────────────────┼──────────────────────────
    MALFORMED        │  rare: right idea,      │  the classic LLM failure
    (off-schema)     │  unparseable            │
                     │                         │
   ──────────────────┴─────────────────────────┴──────────────────────────

   Constraining the output space deletes the bottom row.
   Everything anyone actually loses money on lives in the top right.
```

## Three ways a constrained model still gets it wrong

1. **Forced choice.** If the true answer is "none of these" and you did not provide a null
   option, the model must return something. The schema has converted an abstention into an
   error, and the confidence attached to it can be high, because the alternatives really were
   worse.
2. **A wrong schema.** Options that overlap, options that are missing, options whose labels mean
   something different to the model than to you. The model cannot report a defect in the
   question it was asked.
3. **Misreading the input.** Nothing about a closed output space improves perception. Ambiguous
   state, adversarial state, state that has gone stale since it was assembled — all unchanged.

It is also worth saying plainly that **well-typedness is not exclusive to this architecture**.
Grammar-constrained decoding, structured-output modes and finite-state decoding give an ordinary
LLM the same guarantee. The interesting claim for a decision model is the calibration
(question 202) and the cost, not type safety.

## What to do about it

* **Always include the null option**, and measure how often it fires. A null rate of zero on real
  traffic means the option is decorative.
* **Threshold on the confidence, do not argmax it.** The whole point of a calibrated
  distribution is that you can refuse below a line and escalate.
* **Evaluate on held-out data with the production class balance.** Accuracy on a balanced sample
  tells you very little about a 200:1 decision.
* **Version the schema like an API.** Adding an option changes the meaning of every historical
  prediction.

## What an interviewer is listening for

Whether you accept a marketing claim at its own framing. "Cannot hallucinate" is a statement about
the codomain of a function. The strongest answer names the guarantee precisely, says which
failure it removes, and then says which failure it does not — and notices that the remaining one
is the expensive one.

## Where this stands, September 2026

The phrasing comes from TypeSafe's launch material for Jev and has been repeated widely since.
The guarantee is genuine and narrower than the sentence sounds. Read it as "no type errors",
which is what the company also says when writing more carefully.
