---
id: "210"
slug: model-name-collisions
style: pokemon
category: frontier
difficulty: intermediate
question: "Two labs shipped something called Astra in the same year. Why is model naming an engineering problem?"
tags: [reproducibility, model-ids, versioning, evaluation, provenance]
---

# "Raichu" is not enough to know what you are facing

**Raichu** is Electric. **Raichu** is also Electric/Psychic, if it is the Alolan one, and then it
has **Surge Surfer** instead of **Static** and doubles its Speed in **Electric Terrain**.
Ponyta is Fire in Kanto and **Psychic** in Galar. Same name. Different Pokémon. Sending out a Ground-type
because "Raichu is Electric" loses you the turn and the battle.

Two labs shipped something called Astra in 2026 — a Google DeepMind research prototype whose
abilities ship inside a live assistant, and an OpenAI model released on 3 September. One word,
two organisations, nothing in common. Upstage's **Solar** and a GPT-5.6 tier called **Sol** are
unrelated. There is a **Luna** tier; there is no "Lunar", and the slip is easy. The brief that
produced this whole arc made exactly that mistake, and used "Astra" as though it named one thing.
Observed in the wild, in one sentence.

## Why this is battling and not pedantry

```
   WHAT TRAINERS SAY               WHAT ACTUALLY DECIDES THE TURN
   ─────────────────               ──────────────────────────────
   "Raichu"                   ──►  which region's form?
   "my strongest one"         ──►  which Pokémon, at what level?
   "an Eeveelution"           ──►  Vaporeon? Jolteon? Umbreon?
   "I used Deoxys"            ──►  Normal, Attack, Defense or Speed?
   "standard setup"           ──►  Nature, Ability, held item, EVs
   "I beat the Gym"           ──►  which badge, which generation?

   A result reported from the left column cannot be repeated,
   cannot be compared, and will not survive a rematch.
```

Three hazards follow.

**The number does not always save you.** **Deoxys** is #386 in the Pokédex in all four of its
forms, and Normal, Attack, Defense and Speed distribute the same total so differently that they
are not interchangeable in any battle. A label that stays fixed while the thing behind it changes
is worse than no label, because you will trust it. Some identifiers really are pinned to one
exact thing; check which kind yours is before you build a record on it.

**The Pokémon that came out is not always the one you sent.** **Dragon Tail** and **Whirlwind**
drag a different party member onto the field whether you wanted it or not. Write down what
*fought*, not what you *chose*. A battle log that records intent rather than outcome is fiction.

**A family name is not a Pokémon.** "An Eeveelution beat it" is meaningless across **Vaporeon**,
**Jolteon**, **Flareon**, **Espeon**, **Umbreon**, **Leafeon**, **Glaceon** and **Sylveon** —
eight different types answering eight different problems. Most second-hand battle reports commit
exactly this, which is why they disagree with each other so reliably.

## The minimum record, which the games already keep

Open the summary screen. It shows the **species**, the Pokédex number, the **Original Trainer**,
the **ID No.**, the **Nature**, the **Ability**, the **Held Item**, and the place and level it was
**met**. That is the provenance record, and it is durable on purpose — the **Name Rater** will
happily change a nickname, and will refuse to touch a Pokémon whose OT is someone else. The
nickname is decoration. The OT and the ID number are the identity.

## What a Gym Leader is listening for

That you treat which Pokémon it is as recorded data, not as a story. The strongest answers go
straight to Whirlwind — what fought is not what you picked — because that is the one that has
actually ruined somebody's notes, and add that two regions using one name makes any written
record unreliable the moment somebody else tries to follow it.

## Where this stands, September 2026

Both Astras are real and current in September 2026. Names churn faster than anything else here,
so this particular collision will be replaced by another. The habit — write down the ID number,
not the nickname — will not be.
