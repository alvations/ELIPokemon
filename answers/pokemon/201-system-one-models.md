---
id: "201"
slug: system-one-models
style: pokemon
category: frontier
difficulty: intermediate
question: "What is a System One model, and when would you reach for one instead of an LLM?"
tags: [system-one, non-autoregressive, classification, latency, jev]
---

# Four move slots, and a Choice Scarf

Every Pokémon in the games knows **at most four moves**. That limit is the whole idea. Before the
battle starts, the answer space is enumerated: Jolteon will do one of four things, and the only
question is which. A System One model is a Pokémon in a battle — not a Trainer describing the
battle afterwards.

The contrast is not big versus small. It is **Metronome versus a moveset**. Metronome picks from
the entire move pool, hundreds of possibilities, and you discover what you got only once it
resolves. That is autoregressive generation: an open output space, revealed a piece at a time.
Jolteon with four slots resolves in one action over a closed set.

## The mechanism

```
  METRONOME (open set)                    FOUR SLOTS (closed set)
  ────────────────────                    ───────────────────────
  "Pokémon used Metronome!"               field state ──┐
        │  rolls the whole move pool      four slots ───┤
        ▼                                               ▼
   Splash? Hydro Pump? Explosion?          ┌──────────────────────┐
        │  find out afterwards             │  read the matchup    │
        ▼                                  └──────────┬───────────┘
   then work out what it did                          ▼
                                             Thunderbolt   0.81
   cost ∝ how long it takes to resolve       Volt Switch   0.14
   result ∈ anything in the game             Shadow Ball   0.05
                                            cost ∝ reading the field
                                            result ∈ the four, always
```

The published primitives are as narrow as a moveset: pick one of the labelled options, put a
number on a bounded scale, or return nothing. **Struggle** is the nothing — when not one of the
four moves can be used, the game does not invent a fifth. It returns the null and hurts you for
it. A schema without that option is a Pokémon with no PP left and no Struggle.

## When it is the right tool

Look for **Quick Attack**: a decision you make again and again, where what matters is that it
lands first. Quick Attack has +1 priority, so it resolves before the opponent regardless of Speed
stats — a fixed, low cost paid for a narrow effect. Routing a ticket, judging whether a retrieval
hit is relevant, gating a tool call. Teams currently answer these with the Trainer's full
monologue and then try to parse a decision back out of it.

The price follows from the design: $0.042 per million tokens in, nothing for output, because
there is barely any output — the fee is for reading the field, not for the speech. TypeSafe
reports 40–200× against frontier models. Treat the range like an advertised base stat until you
measure your own team, but the direction is architectural, not a sale.

## When it is the wrong tool

* **You need to see the reasoning.** Quick Attack does not explain itself. If a Gym Leader has to
  be shown *why*, this is the wrong move slot.
* **The options are genuinely open.** Some battles are not four moves wide. Enumerate those and
  you have thrown the match away by narrowing it.
* **The four slots are the hard part.** A badly built moveset loses to things it could have
  covered, and the Pokémon cannot tell you what it was never taught. Sucker Punch only works if
  the target is attacking; give it the wrong job and it simply fails.
* **You wanted one Pokémon.** This is a **Volt Switch** team. Jolteon takes the fast decision and
  pivots out to the heavy hitter when the matchup is wrong — two Pokémon in the loop, not one.

## What a Gym Leader is listening for

That you can name what actually changed — one action over four known options, instead of a
sentence assembled word by word from every word there is — rather than quoting a damage roll. And
that you use the **accuracy number**. Focus Blast is 70% and the game means it. A model that hands
you a confidence and a Trainer who ignores it have wasted the same information.

## Where this stands, September 2026

Jev is a hosted battle: open client SDKs in four languages, community lists of teams built on it,
but **the Pokémon itself is not distributable** — no open weights. And the idea is old. Four move
slots have been the rule since Red and Blue. What is new is the training that makes the
confidence number honest (question 202), not the discovery that acting is faster than narrating.
