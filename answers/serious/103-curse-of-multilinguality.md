---
id: "103"
slug: curse-of-multilinguality
style: serious
category: multilingual
difficulty: intermediate
question: "What is the curse of multilinguality, and how do you fight it?"
tags: [multilingual, capacity, xlm-r, moe, interference]
---

# The curse of multilinguality

At **fixed model capacity**, adding languages to the pretraining mix helps for a while and then
hurts everyone. [Conneau et al. (2019)](https://arxiv.org/abs/1911.02116), the XLM-R paper, named
this and measured it: going from 7 to 100 languages at constant size improves the low-resource
tail at first, because related languages share structure, and then degrades all languages —
including English — because the parameters have to be split more ways.

It is capacity dilution plus interference, not a mysterious property of language.

```
   quality
      ▲
      │        ╭──────╮  low-resource languages: transfer helps first
      │      ╭─╯      ╰──╮
      │    ╭─╯           ╰────╮
      │ ───┴─────╮            ╰────────  high-resource languages:
      │          ╰──────────────────────  interference from turn one
      └──────────────────────────────────────────────►
        7      30      50      100     200   languages in the mix

   Fix capacity, add languages: every curve eventually points down.
   Raise capacity with the language count and the curves flatten.
```

## The three levers

**1. More parameters.** The dumbest fix and the one that works. The curse is stated *at fixed
capacity*; XLM-R's own answer was a much larger model with a 250k vocabulary. Every dimension has
to grow together — depth, width and vocabulary — or you shift the bottleneck rather than remove
it (question 105).

**2. Conditional capacity: give each language its own parameters.**

* **Adapters** — small per-language modules on a shared frozen trunk (question 110). MAD-X
  ([Pfeiffer et al., 2020](https://arxiv.org/abs/2005.00052)) is the canonical design.
* **Sparse mixture-of-experts** with language-aware routing.
  [NLLB-200](https://arxiv.org/abs/2207.04672) used exactly this for 200 languages: total
  parameters grow, per-token compute does not, and
  the model can dedicate experts to language groups. Its own analysis shows the sparse model
  helps low-resource pairs most, precisely because it reduces interference.
* **Language-specific layers or embeddings**, the crude version of the same idea.

**3. Curriculum and grouping.** Train on families rather than the world at once, or sample
carefully (question 104). Related languages interfere less and transfer more, so a
Romance-focused model of a given size beats a global model of that size on Romance.

## What actually interferes

Not everything competes equally. Evidence from adapter and pruning studies suggests the shared
upper layers hold task-general structure that different languages happily reuse, while the
contested resources are the **embedding table and the lowest layers**, which have to represent
every script and morphology. That is why enlarging vocabulary and embedding capacity buys
disproportionate improvement.

## The tradeoff nobody escapes

Massively multilingual models exist because one model for 100 languages is operationally far
cheaper than 100 models, and because low-resource languages have nowhere else to get signal.
That is a deployment argument, not a quality argument. If you only care about five languages,
a five-language model of the same size will beat the 100-language one on all five, every time.

## What an interviewer digs into next

* Why is the curse stated "at fixed capacity", and what happens if capacity scales?
* Why does MoE help low-resource languages more than high-resource ones?
* Which parameters are actually contested — is it uniform across the network?
* When is one model per language group the right answer?
