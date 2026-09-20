---
id: "207"
slug: sparse-moe-serving
style: pokemon
category: frontier
difficulty: advanced
question: "An open model advertises 250B total parameters with 15B active. What does that buy you when you go to serve it?"
tags: [mixture-of-experts, serving, memory, routing, quantisation]
---

# Charizard is on the field. Onix, Ditto and four others are still in the bag.

A party holds six and exactly one stands on the field. **VGC** makes the split explicit: you
register six, you bring four, and in Doubles two are out at a time. That is a sparse
mixture-of-experts, and it has been the format since Kanto.

Solar Open 2 is the cleanest version to reason about: reported as roughly **250 billion
parameters registered and about 15 billion on the field per turn**, a window up to a million, and
a claim that it fits on **two NVIDIA H200s**. The same lab built its earlier model by stacking a
smaller one on itself — the **Magneton** trick, three **Magnemite** linked into one — so wringing
capacity out of a fixed budget is the house style.

The sentence that matters: **whoever is out decides what the turn costs, and nothing decides what
the team costs.** All six are registered, because any turn might need any of them.

## Why the two-card figure is exactly the arithmetic you should do

```
   the whole registered team
      × light build                = 250 GB to carry
      × full build                 = 500 GB to carry

   one H200 holds ≈ 141 GB
      two cards                    = 282 GB   ◄── light build fits,
                                                  ~32 GB spare
      four cards                   = 564 GB   ◄── what the full build needs

   ┌───────── what that 32 GB still has to hold ──────────┐
   │  the battle log  │  the field  │  slack  │  headroom │
   └───────────────────────────────────────────────────────┘
        ▲
        └ a million-token PC does not travel free. "Fits on two
          cards" and "fits with Bill's PC open" are two claims.

   Work per turn ∝ the one on the field.
   Weight in the bag ∝ all six. These do not move together.
```

So the honest reading is **the turn cost of one Pokémon and the registration cost of six**.
Excellent if you have the bag; no trade at all if you do not — which is why this buys a Trainer
with a single card nothing. The widely repeated result on Gemma 4's small mixture checkpoint has
it running **slower** on an RTX 4090 than a plain Pokémon of the same field size: **U-turn** costs
a turn, and with that little out there is not enough saved to pay for the switch.

## The four problems the announcement leaves out

1. **A Doubles bracket gets harder, not easier.** **Bronzong** wants a Fire move, **Gyarados**
   wants **Thunderbolt**, and the **Onix** in slot four wants **Surf** — every opponent pulls a
   different member out. You cannot answer them with one clean action, and throughput is entirely
   a question of how well you group opponents by who answers them.
2. **A split team means running back and forth.** Leave half in **Bill's PC** and every switch is
   a trip to the nearest **Pokémon Center**. That floor is set by the distance, not by the
   Pokémon.
3. **Charizard does all the work.** Left alone you lean on the starter, **Onix** never comes out,
   and it is level 12 at the **Elite Four**. **Exp. Share** is the fix and it has to be switched
   on deliberately — a team does not share by hoping.
4. **Cutting corners does not cut them evenly.** Trim everyone's training and the ones who rarely
   battle degrade first, because they had the least to learn from. Your **Ditto** and your
   **Smeargle** are exactly the two you registered for the strange matchups.

## What a Gym Leader is listening for

That you separate the two counts and attach each to the right cost — the field and the bag. Then
that you weigh it out loud: how heavy the registered six are against how much the bag holds is a
thirty-second sum that decides whether the run is possible at all. The strongest answers add that
"fits on two cards" is always measured with the PC closed, a light build and one **Youngster** in
front of you, and say what they would measure instead: turns per minute against the opponents and
the storage they actually face.

## Where this stands, September 2026

The Solar Open 2 numbers above come from coverage of the release; the model card is the authority
and should be read before anyone buys a bag. The reasoning — the field decides the turn, the
team decides the weight — is older than the model and will outlive it.
