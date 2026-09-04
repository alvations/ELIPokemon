---
id: "082"
slug: activation-functions
style: pokemon
category: deep-learning
difficulty: core
question: "Compare ReLU, GELU, and SwiGLU. Why did LLMs settle on gated activations?"
tags: [relu, gelu, swiglu, activations, gating]
---

# Activation functions: how does a Pokémon decide to react?

A Gyarados switches in. Your Ferrothorn has to decide **how strongly to respond.** That decision
rule is the activation function.

And first, why it must be a *rule* and not just arithmetic:

> **Without a decision rule, a hundred Gyms collapse into one.**

If Brock, Misty and Lt. Surge each just add their opinion to a running total, you could have added
all eight badges up at the start and skipped the journey. The **non-linearity** — some genuine threshold, some "no, that doesn't
matter" — is what makes Giovanni capable of teaching something Brock couldn't.

## The three rules 📊

```
   🚪 THE BOUNCER              🌫️ THE SOFT BOUNCER        🎚️ THE DIMMER
      max(0, x)                    smooth version              x · gate

        │    ╱                       │    ╱                     │    ╱
        │   ╱                        │   ╱                      │   ╱
   ─────┼──╱───                 ─────┼──╱───               ─────┼──╱───
        │ ╱                       ╲__│╱                      ╲__│╱
        │                            │                          │

   Attack or don't.          Mostly don't, but a       Same idea, cheaper
   Nothing in between.       whisper gets through.     to run.
```

**🚪 The Bouncer.** Above the threshold, through at full strength — Thunderbolt, no hesitation.
Below it, **nothing.**

Simple, fast, and — crucially — it doesn't weaken the message passing through, which is what made
deep Leagues possible at all.

Its flaw: a Pokémon that gets turned away often enough becomes **permanently** switched off. Never
reacts to anything again. Nothing can revive it, because it never produces feedback to learn from.

**🌫️ The Soft Bouncer.** Nearly identical, except borderline cases get through **faintly** instead of
being hard-refused. That whisper is enough to keep a Pokémon from switching off forever.

## 🎚️ The real innovation: two knobs, not one

Here's what actually changed things, and it isn't a nicer curve.

All three above ask **one** question: *"how much of this gets through?"*

Gating asks **two**, separately:

```
   🎚️ THE GATED RULE

   Knob A: "What's my reaction?"        → "Thunderbolt the Gyarados."
   Knob B: "How much does this matter?" → "...20%. It has a Focus Sash,
                                            so it survives anyway."

   ✅ ANSWER = A × B  →  Thunderbolt, but held back.
```

Two independent judgements — **what to do**, and **how much it matters** — multiplied together.

The old rules couldn't express that. They had one dial: react or don't. Now your Pokémon can have a
strong opinion and simultaneously recognise it's a low-stakes moment.

📌 That **multiplication** is the real gain. It's not a smoother curve — it's an operation the layer
genuinely couldn't perform before.

## The catch, and the fix 📏

Two knobs need two dials to build, plus the original. **Three components instead of two** — a 50%
bigger Pokédex for free.

So you don't get it for free: **you shrink the book to compensate.** Roughly two-thirds the pages,
three columns instead of two, same total size.

That's what makes the comparison fair. Anyone reporting that gating is better *without* shrinking the
book is measuring a bigger Pokédex, not a better rule.

## What to use 🎯

| Situation | Rule |
| --- | --- |
| 🏆 A modern language model's Pokédex | 🎚️ **Gated** (with a shrunk book) |
| 📚 Older transformer designs | 🌫️ Soft bouncer |
| ⚡ Anything speed-critical | 🚪 Bouncer |
| 🎬 The final decision | none — just say the answer |

## The honest note 🤷

The gap between any two sensible modern choices is **small.** Under a percent, usually — and utterly
dwarfed by how much footage you trained on and how big your Pokémon is.

The person who introduced the gated rule benchmarked it thoroughly, confirmed it consistently wins,
and then cheerfully admitted **nobody really knows why**, attributing it to divine benevolence.

Worth getting right if you're building at the frontier. Not worth a week of your life otherwise.
