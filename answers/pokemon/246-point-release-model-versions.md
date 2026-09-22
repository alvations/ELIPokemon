---
id: "246"
slug: point-release-model-versions
style: pokemon
category: open-weights
difficulty: advanced
question: "DeepSeek shipped V4.1-Flash four months after V4-Flash. What does a minor version bump on a model actually promise?"
tags: [versioning, deepseek, evaluation, migration, serving]
---

# Nothing. "Crystal is just Gold with a shinier box" is how people talk, and it is wrong.

A cartridge's name is a product, not a promise. **Pokémon Crystal** arrived after **Gold** and
**Silver** looking like a re-release — same region, same eight badges, same **Elite Four** — and
underneath it is a different game. **Yellow** did the same to **Red** and **Blue**. **Emerald**
did it to **Ruby** and **Sapphire**. **Platinum** did it to **Diamond** and **Pearl**. Every one
of them is sold as the small one and every one of them moves things a serious Trainer has to
re-check.

```
   what "the third one" actually changed
   ────────────────────────────────────────────────────────────────────────────
   Yellow    your starter is Pikachu, it walks behind you and refuses to
             evolve; you can obtain Bulbasaur, Charmander AND Squirtle in
             one playthrough; Jessie and James turn up in person
   Crystal   the first game you can play as a girl; the first Battle Tower;
             animated sprites; a whole new Suicune storyline with Eusine
             and the Clear Bell that Gold and Silver simply do not have
   Emerald   Kyogre AND Groudon both wake, and Rayquaza is what stops them;
             the Battle Frontier is added on top of the whole game
   Platinum  the Distortion World, and Giratina gets a second forme it did
             not have in Diamond or Pearl
   ────────────────────────────────────────────────────────────────────────────
```

Look at Crystal and Emerald together. The roster on the box barely moved. What you can *do* moved
enormously. Any plan built on "it is the same game" is wrong in both directions at once: it
overestimates what carries over and underestimates what is new.

## The asymmetry is the interesting part

The number on the front of a competitive team tells you almost nothing either, because **reading**
and **acting** cost completely different amounts. In **VGC** you register six Pokémon, **Team
Preview** shows you all six of your opponent's before a single turn is played, you choose four,
and two stand on the field at a time.

```
   A 20-TURN MATCH
     reading   one look at 6 opposing Pokémon                 =  6 evaluations
     acting    2 Pokémon on the field × 20 turns              = 40 commitments
                                                                ──
     reading is roughly SEVEN TIMES the cheaper half

   A 4-TURN MATCH
     reading   still 6                                        =  6 evaluations
     acting    2 × 4                                          =  8 commitments
                                                                ──
     now they are nearly the same, and the look is the expensive part

   ┌───────────────────────────────────────────────────────────────────┐
   │ Both matches register six Pokémon. The box number is identical    │
   │ and useless. What it costs YOU depends on how long YOUR matches   │
   │ run — and a Trainer who plays long games and a Trainer who plays  │
   │ short ones should not copy each other's team.                     │
   └───────────────────────────────────────────────────────────────────┘
```

## So what actually makes you replay your matches?

A new cartridge is a prompt to check, not a licence to skip. Go back through your notes when any
of these moved, and across the generations most of them have:

1. **What a move's damage is calculated from.** The single worst offender in the history of the
   games: before Generation IV, whether a move used Attack or Special Attack was decided by its
   **type**. From Generation IV it is decided by the **move**. Not one name changed, not one
   number on the screen changed, and every Ghost and Dark attacker in the game became a different
   Pokémon overnight.
2. **A new input.** Pokémon that could not be obtained before now can be, and the answer you
   prepared for a Gym is not the answer any more.
3. **The control you were using.** A facility that took a streak now takes a rental team instead;
   the dial you were turning is not the same dial.
4. **What counts as a level.** The cheapest thing to check and the one that silently rewrites
   every estimate you made about how long a grind takes.
5. **Defaults you never set.** A **Pokémon Center** heal, an item's stack size, who moves first
   on a tie — changed quietly, felt loudly.
6. **How it plays on the field.** Animated sprites are cosmetic. A **Battle Tower** being added is
   not: there is now a place where your team is tested against rules you did not write.
7. **Which cartridge actually answered.** Write down which version you were playing, not which
   generation. **Gold** and **Crystal** are not the same evidence.

The honest summary of the third versions: **they change the kind of game it is.** Whatever the
box says, Emerald with a Battle Frontier bolted on is not Ruby with a patch. It is a new game
that inherited a region.

## Migrating, in the order that saves you

Keep the old cartridge. Replay **your** battles, not the ones in the magazine — a published
tournament result is a real claim about a real bracket and tells you nothing about the six
Pokémon you actually own. Re-count the grind at your own pace. Re-read what the new facility
actually allows rather than assuming the last one's rules carried over. Re-check the level cap
you are allowed to bring, because turning up over the limit is the cheapest failure to catch and
the most embarrassing to discover at the door. Then move across one Pokémon at a time.

## What a Gym Leader is listening for

That you say "the name on the box promises nothing" without hedging, and then ask immediately
what *did* change instead of arguing about it. That you spot the reading-against-acting split as
a change in the shape of the cost and can say which kind of Trainer wins. And that you ask which
exact version someone was playing. A Trainer who reads "Crystal" as "Gold, slightly" has accepted
a name in place of a difference.

## Where this stands, September 2026

The cartridge facts above are from published histories and are settled: Crystal really was the
first with a female player character and the first with a Battle Tower, Yellow really does give
you a Pikachu that will not evolve and all three Kanto starters, Emerald really does wake both
Kyogre and Groudon, and the split between physical and special really did move from the type to
the move in Generation IV. The VGC counts — six registered, four brought, two on the field, with
Team Preview before any of it — are the format's own rules. The match-length arithmetic is my
own sketch and depends entirely on how you play. Which third version is current changes every
few years. The seven things to re-check do not.
