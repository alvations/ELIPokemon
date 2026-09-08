---
id: "195"
slug: multilingual-reasoning
style: serious
category: translation
difficulty: advanced
question: "Do models reason as well in other languages as they do in English?"
tags: [multilingual-reasoning, pivot-language, chain-of-thought, cross-lingual-gap, culture]
---

# Reasoning across languages

No. And the shape of the gap is more interesting than the fact of it.

## What is actually observed

Ask a multi-step reasoning question in English and in another language, and accuracy differs —
sometimes substantially, and the gap tracks how much of that language was in pretraining. But it is
not that the model is *worse at reasoning* in the other language. It is that:

```
   understanding the question    ─► transfers well across languages
   the reasoning itself           ─► appears to happen in a largely shared,
                                     English-skewed internal representation
   producing the answer IN the
   target language                ─► transfers less well, and degrades under
                                     the load of reasoning at the same time
```

Interpretability work supports a picture where multilingual models process through a
representation closer to their dominant training language and translate at the edges. That is why
**"think in English, answer in the target language" often beats reasoning natively** — and it is
also why that trick is a diagnosis of a limitation rather than a satisfying solution.

## The practical techniques, and their costs

* **Translate the question to English, reason, translate back.** Reliable and cheap. Loses whatever
  the source encoded that English does not (question 130's pivot losses), and fails on
  culture-specific content where the English rendering is not the same question.
* **Reason in English, answer in the target.** Better than translate-and-back, because the final
  generation is conditioned on the original. Standard practice, and the answer's fluency in the
  target may exceed its faithfulness.
* **Native chain-of-thought**, which is what you want and currently costs accuracy for most
  languages. The gap narrows with pretraining data, so it is a data problem more than an
  architecture problem.
* **Self-consistency across languages** — ask in several, take the majority. Expensive, and a
  genuinely useful signal: disagreement across languages flags an unreliable answer.

## The part that is not about reasoning at all

Some cross-lingual gaps are **cultural, not linguistic**. A question about legal procedure,
measurement conventions, school grading, or family relationships has a different *correct answer*
in different places (question 150). A benchmark translated from English carries English assumptions
and marks the locally correct answer wrong.

This is why translated benchmarks systematically overstate the gap for some tasks and understate it
for others, and why locally authored evaluation sets matter (question 196).

## What to do about it

* **Measure per language on the same underlying items**, and separately on locally authored items.
  The difference between those two numbers tells you how much of your gap is reasoning and how much
  is cultural.
* **State your pivot behaviour.** If your system reasons in English internally, that is a design
  decision with consequences, and it should be documented rather than emergent.
* **Watch language consistency** — the model reasoning in English and leaking English into the
  answer is question 136's off-target failure in a new place.
* **Do not assume the gap is uniform.** It is largest for multi-step reasoning and smallest for
  retrieval-like tasks, so a single "multilingual gap" number is not actionable.

## What an interviewer digs into next

* Why does "think in English, answer in the target" beat native reasoning, and why is that unsatisfying?
* How would you separate a reasoning gap from a cultural-knowledge gap?
* Why is cross-lingual disagreement a useful reliability signal?
* Why is a single multilingual-gap number not actionable?
