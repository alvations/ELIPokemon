---
id: "247"
slug: reading-changelogs-and-cadence
style: pokemon
category: open-weights
difficulty: intermediate
question: "How do you read a library's changelog and release cadence to tell a real capability change from a repackaging?"
tags: [semver, changelogs, release-engineering, deepspeed, dependencies]
---

# Read how the TM numbers are handed out before you read what the TM does.

A number is only as informative as the scheme that assigned it, and the scheme is almost never
printed on the item — it is in how the list was built. **TMs** are a good subject because their
scheme is unusually legible once you look at it instead of assuming.

```
   how a TM number is assigned, in order            what it tells you
   ──────────────────────────────────────────────────────────────────────────────
   1. a generation decides which moves get TMs   ── the LIST is the thing
   2. the moves are laid out in a fixed order    ──   the number is a slot in it
   3. slot one becomes TM01, slot two TM02 …     ── the counter goes up by one
   4. the list stops: Kanto has exactly TM01–    ──   per slot, regardless of
      TM50, plus HM01–HM05, and nothing else     ──   how big the move is
   5. the next generation lays out a NEW list    ──────────────────┐
   ──────────────────────────────────────────────────────────────────┘
        │
        └─ and reuses the same numbers for different moves

   CONSEQUENCE: TM01 and TM26 sit on one scale and Earthquake, which is
   TM26 in Red and Blue, is worth vastly more than whatever is in slot one.
   The number tells you a move is in the list. It tells you NOTHING about
   how much the move is worth.
```

And it has never promised otherwise. Across six generations of lists, not one TM number has been
guaranteed to mean the same thing in the next region. That is not a complaint. It is information,
and it is the opposite of what most Trainers assume when they write "teach it TM01" in a guide.

## Two re-numberings that were not re-numberings

Both of these are worth checking yourself, and both are why "it's the same TM" is not a plan.

**TM01 in Kanto is Mega Punch. TM01 in Hoenn is Focus Punch.** Identical slot, identical label on
the disc, two moves with nothing in common — one is a straightforward punch, the other only lands
if the user has not been hit that turn. A guide written for **Red** and **Blue** that says "put
TM01 on it" is, in **Ruby** and **Sapphire**, advice to do something completely different.

**TMs used to be consumed.** Through Generation IV, teaching a TM destroyed it: one disc, one
Pokémon, forever, and a TM you found in the **Celadon Department Store** was a decision. From
Generation V they are reusable and you can teach the same TM to all six. Not one number changed.
The entire economy of building a team changed.

## The five diffs, in order of how often they bite

```
   1. WHAT THINGS DO        Not the list of names — the effects. A move that
                            kept its name and changed its base power, or an
                            item that kept its sprite and changed what it
                            restores, is a change to a plan you did not
                            rewrite. This is number one for a reason.

   2. WHAT IS OBTAINABLE    which species appear, on which routes, at which
                            levels, and which have quietly stopped appearing
                            at all. The answer you prepared for a Gym may no
                            longer be catchable before that Gym.

   3. THE DATA BEHIND THE   the box copy is a summary. The move's actual
      BOX COPY              numbers are the artefact. Open the two or three
                            moves the headline points at and read them.

   4. WHAT IS ACTUALLY      which facilities exist in THIS version, and what
      TESTED                rules they run. A Battle Tower in one cartridge
                            and none in another is not a cosmetic difference:
                            there is now somewhere your team is tested against
                            rules you did not write.

   5. DID THE GENERATION    a new box with the same generation behind it is a
      MOVE AT ALL?          re-release. The region is the same, the data is
                            the same, and nothing you know has expired.
```

**Repackaging against real change**, as a test you can apply without thinking: new sprites, a new
box, a new town layout, an animated intro — the set of things that can happen in a battle is
unchanged. A changed base power, a changed item effect, a changed catch rate — that is a real
change, however small the note is. **If it touches a number that a damage calculation reads, it
is a real change.**

## A ladder that actually does keep its promise

Not every number in the games is a slot. The fishing rods are a genuine ordered ladder with a
published contract at every step:

```
   Old Rod     from the Fishing Guru in Vermilion City
               → Magikarp. Level 5. Every time, in every body of water.
   Good Rod    from the Fishing Guru in Fuchsia City
               → Poliwag, Goldeen and friends, around level 10.
   Super Rod   → the widest list and the highest levels of the three.
```

You can plan against that. You know exactly what the next step buys before you take it, it never
means something different in the next town, and nobody can hand you an Old Rod that behaves like
a Super Rod. **Know which kind of ladder you are standing on** — a rod, where the step is
enforced and the contract is printed, or a TM number, where the digit is a position in a list
somebody rebuilt for a different region.

## And the contrast that matters

The cartridge is enforced. Put **Red** back in the slot and you get exactly the game you got
before — the same **Magikarp** from the same water, the same fifty TMs in the same order, today
and in ten years. A **nickname** is not that. The **Name Rater** will change it on request,
nothing in the game depends on it, and the Pokémon underneath is unaffected either way. When
somebody proposes planning around the nickname and the cartridge in the same breath, that is the
difference to put on the table.

## What a Gym Leader digs into next

* You changed cartridges and the same team suddenly loses a matchup it used to win. Where do you
  look first?
* What is the difference between a new *version* and a new *generation*, and which one expires
  your notes?
* Which is worse: a move that changed base power, or a move removed from the game entirely — and
  why is it the first one?
* How would you spot a changed item effect without reading the whole guide?
* When would you deliberately stay on the old cartridge?

## Where this stands, September 2026

The TM facts here are from the published lists and are settled: Kanto's TM01 is Mega Punch and
Hoenn's is Focus Punch, Earthquake is TM26 in Red and Blue, Kanto has exactly fifty TMs and five
HMs, and TMs were consumed on use through Generation IV and reusable from Generation V. The rod
contracts are equally fixed — the Old Rod from the Vermilion City guru gives Magikarp at level 5
and nothing else, the Good Rod comes from Fuchsia City. Which moves occupy which slots changes
with every generation, and will keep changing. Reading how the list was built before trusting a
number in it does not.
