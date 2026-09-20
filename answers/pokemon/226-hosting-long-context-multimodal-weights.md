---
id: "226"
slug: hosting-long-context-multimodal-weights
style: pokemon
category: open-weights
difficulty: advanced
question: "An open checkpoint advertises a 1M-token window and native vision. What does self-hosting cost that renting hides?"
tags: [long-context, kv-cache, multimodal, serving, open-weights]
---

# Baton Pass hands over seven numbers. The Battle Video hands over every turn.

Question 206 is about how much the box holds. This one is about **who owns the box**. Using the
one at the **Pokémon Center** and owning **Bill's PC** are different arrangements, and the
difference only shows up on the turns when it is full.

The room has been getting bigger for a while. One release held a battle log of moderate length;
the two after it each held twice that; the newest holds a million turns' worth — and that last
figure comes straight off the release's own summary table, not from somebody describing it. It
also, for the first time, *looks* at things.

## It did not get bigger by remembering harder

The trick is what a Pokémon actually hands over when it leaves the field. There are two ways to
carry a battle forward.

**The Battle Video** is the honest, expensive one: every turn, in order, kept forever, re-watched
from the top whenever you need to know what happened. **Vs. Recorder** will do exactly that, and
the recording gets longer every turn, without limit.

**Baton Pass** is the other one. It switches the user out and hands the incoming Pokémon its
**Stat Stage** numbers — seven of them, each somewhere between -6 and +6 — plus the **Substitute**
still standing and the **Leech Seed** still draining. That is all. The incoming Pokémon does not
receive the history of how any of it happened, and it does not need to. **Ninjask** raises its own
Speed a stage at the end of every turn through **Speed Boost** and passes the result on;
**Espeon** stacks **Calm Mind** behind a **Substitute** and passes that. Seven numbers, whatever
the battle's length.

Two things follow that matter to whoever is holding the box.

* **You stop needing turn numbers at all.** The stages carry where you got to. Nobody consults the
  recording to find out what the Speed stage is; it is simply +3. Which is why a team built this
  way can go far past the length it trained at without anything being re-tuned.
* **Not everything travels.** A burn from **Will-O-Wisp** stays with the Pokémon that has it and
  does not go down the **Baton Pass**. In a team where most members hand over seven numbers and a
  few still carry the whole recording, **the few are your entire memory bill.** "Mostly passes a
  baton" does not mean nobody is holding a tape. Count the ones who are.

```
   per battle, at a million turns

   most of the team      ┌───┐  seven numbers, -6 to +6. Same size at turn
                         │ S │  ten and at turn a million. Cheap to hold,
                         └───┘  cheap to hand over, reusable next battle.

   the rest of the team  ┌──────────────────────────────────────────┐
                         │ every turn ..................... 1M turns│  ◄── grows
                         └──────────────────────────────────────────┘

   the roster itself     heavy, once, always in the bag
   the per-battle state  x however many battles you are running at once
                                                          ▲
                                                          └ THIS is the
                                                            number that
                                                            decides how
                                                            many at once
```

## The Pokédex is not free room either

**Professor Oak** hands you a **Pokédex** and it identifies what it is pointed at. In **Alola** a
**Rotom** lives inside it, so it is part of the thing rather than a gadget you remembered to
bring — and that is the real difference. A Trainer who *knows* a species on sight is not the same
as one who stops and looks it up.

But an entry is a couple of lines, not the photograph. The screen you point at a Pokémon is
enormous and what gets written down is small, and it has to be, because **the entries and the
battle log share one book**. Room spent on what you looked at is room not spent on what happened.
Question 206's warning that the unit is not stable is sharper here: how much of the book one
glance costs is a detail of how the **Pokédex** was built, it changes between versions, and it is
never the number on the box.

## Borrowing the box versus owning it

```
   ┌──────────────┬──────────────────────────┬─────────────────────────────┐
   │              │  THE POKEMON CENTER      │  BILL'S PC, YOURS           │
   ├──────────────┼──────────────────────────┼─────────────────────────────┤
   │ the roster   │  not your problem        │  heavy, in your bag, always │
   │ per battle   │  folded into the fee     │  YOUR room, x how many at   │
   │              │                          │  once                       │
   │ reusing what │  already built for you   │  you build it, and handing  │
   │ you had      │                          │  over seven numbers needs a │
   │              │                          │  different shelf from       │
   │              │                          │  handing over a tape        │
   │ a long first │  their waiting time      │  a recording cannot be      │
   │ turn         │                          │  watched out of order — you │
   │              │                          │  cannot split the watching  │
   │              │                          │  the way you split the bag  │
   │ trimming     │  chosen for you          │  chosen by you, and it was  │
   │              │                          │  done while it was being    │
   │              │                          │  raised, not afterwards     │
   │ the bill     │  a flat fee per turn     │  hardware you already own;  │
   │              │                          │  only cheap if it is busy   │
   └──────────────┴──────────────────────────┴─────────────────────────────┘
```

**Pokémon HOME** is somebody else's shelves and it works. Owning the shelves is not a virtue; it
is a bet on how often you will use them. Borrow until the box is busy and steady, then work out
the crossover **with the per-battle room included**. Most Trainers who buy their own shelves for
bursty traffic are paying for empty ones and calling it independence.

## What a Gym Leader is listening for

That you name the per-battle room as the thing borrowing hides, and that you know a team can have
two different memory habits inside it. The strongest answers ask how many members are still
carrying a tape before quoting any saving, and notice that **Pokédex** entries and battle turns
come out of the same book.

## Where this stands, September 2026

**Baton Pass**, the **Stat Stage** range and what does and does not travel are from the games and
do not rot. Which release holds how many turns, and how the team splits between batons and tapes,
comes from what each one published about itself and moves every few months. Re-read the split, not
the headline number, when the next one lands.
