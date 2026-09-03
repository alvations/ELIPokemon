---
id: "051"
slug: in-context-learning
style: serious
category: prompting
difficulty: core
question: "What is in-context learning and how does it work mechanistically?"
tags: [in-context-learning, few-shot, induction-heads, task-location]
---

# In-context learning

Give a model a few input/output examples in the prompt and it performs the task on a new input —
with **no weight updates**. This was the headline capability of GPT-3
([Brown et al., 2020](https://arxiv.org/abs/2005.14165)) and it is still the most useful practical
property of LLMs, because it makes adaptation free and instant.

## The finding that reframed it

[Min et al. (2022)](https://arxiv.org/abs/2202.12837) replaced the labels in few-shot examples with
**random** ones. Performance barely dropped.

That rules out "the model is learning the input→output mapping from the demonstrations". What
actually matters, per that work and its successors:

* **The label space** — which labels exist at all.
* **The input distribution** — what kind of inputs to expect.
* **The format** — the exact shape of the input/output pairing.
* Whether examples are present at all — zero-shot is much worse than random-label few-shot.

The best framing is therefore **task location, not task learning**. Pretraining already contains
sentiment classification, translation, and extraction, in many formats. The demonstrations do not
teach the task; they *specify which task and which format* out of the many the model already knows.

The caveat: with enough demonstrations (many-shot, hundreds to thousands of examples), true
input-output learning *does* emerge and label correctness starts to matter again. So the honest
statement is that few-shot ICL is mostly location, and many-shot ICL is genuinely learning.

## The mechanism

**Induction heads** ([Olsson et al., 2022](https://arxiv.org/abs/2209.11895)) are the best-understood
substrate. An induction head implements: *find an earlier occurrence of the current token, and
predict what followed it.*

```
   context:  ... [A] [B] ... ... ... [A] → predict [B]

   ┌───────────────────────────────────────────────────────────────┐
   │ head 1 (previous-token head): writes "the token before me was │
   │         X" into each position's residual stream               │
   │ head 2 (induction head): looks for an earlier position whose  │
   │         "previous token" matches the CURRENT token, and copies│
   │         what came after it                                    │
   └───────────────────────────────────────────────────────────────┘

   applied to few-shot:
      "cat → gato,  dog → perro,  bird → "
                                    ▲
      the pattern "<word> → <translation>" is matched, and the head
      copies the STRUCTURE, letting later layers fill the content
```

These heads form abruptly during a narrow window of training, and the in-context learning score
jumps at exactly that point — one of the few clean cases of a genuine phase transition in training.

A second, more speculative account: transformers performing ICL may implement something like
**gradient descent in their forward pass** on the demonstrations
([von Oswald et al., 2022](https://arxiv.org/abs/2212.07677)), with constructions showing attention
layers can implement one step of gradient descent on a linear regression objective. Suggestive for
simple settings; not established for real LLMs on real tasks.

## Practical implications

* **Format consistency matters more than label correctness.** Use the same separators, casing and
  structure in every example, and in the query.
* **Show the output format you want**, precisely. This is what demonstrations do best.
* **Cover the label space** — include an example of every class, especially rare ones.
* **Order effects are real**, particularly recency: the last example has outsized influence. If
  results vary between runs of the same prompt, permutation is often the cause.
* **More examples help**, with diminishing returns after ~8–32 for most tasks — until you get to
  many-shot regimes with long contexts, where gains resume.
* **Prefer examples similar to the query** (retrieved few-shot) over a fixed set.

## What an interviewer digs into next

* If random labels barely hurt, what are demonstrations doing?
* What is an induction head, and what does its formation coincide with?
* Why does many-shot ICL behave differently from few-shot?
* How would you debug a few-shot prompt that works inconsistently?
