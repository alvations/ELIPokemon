---
id: "254"
slug: draft-and-verify-families
style: pokemon
category: optimization
difficulty: intermediate
question: "A separate draft model, Medusa heads, EAGLE, lookahead, n-gram lookup — how do the drafting families differ?"
tags: [speculative-decoding, eagle, medusa, lookahead, prompt-lookup]
---

# Every way of guessing what is on the line differs in one thing: how much water it gets to see.

The keep-or-throw-back rule from [253](253-speculative-decoding-exactness.md) is the same
whichever way you guess, so none of these can put a wrong species in your **Poké Ball**. What
separates them is **what the guess is allowed to look at**. A guess made from the route sign sees
only what is printed. A second rod sees the water through its own table. An ability on your lead
sees only whether something is still on the line. Reading the thing that seeds the water sees the
most of all. The share of casts you get to keep climbs in roughly that order, and so does what the
guess costs you to obtain — a slot in the **Bag**, a Pokémon at the front of the party, or an
afternoon.

Since the keep rate is one minus the gap between your guess's table and the real one, none of this
is mysterious. Each step up the list hands the guess more of what the water is actually using.

## The families

```
  how you guess        costs you        must be raised?  what it sees               time per guess
  ───────────────────────────────────────────────────────────────────────────────────────────────
  the route sign         nothing            no            the printed slots, and      none
                                                          nothing else
  a notebook of every    nothing            no            the slots plus every        none
  route you have fished                                   route you already fished
  guess-and-cross-out    nothing            no            the water itself, one       a full cast
                                                          full cast at a time           per pass
  ───────────────────────────────────────────────────────────────────────────────────────────────
  stop your own cast     nothing            you must       the first round of the     a fifth of a
  after round one                           practise it    cast you were making       cast
  Suction Cups on        a party slot       no (you own    only whether something     next to none
  the lead                                  it already)    is still on the line
  reading the trend      nothing            learning       what seeds the water,      a small part
  in Dewford                                which words    not what surfaced from it    of a cast
  a rod that came        nothing            already done  the same water the rod     about a tenth
  with the Pokémon                                         itself draws from            of a cast
  ───────────────────────────────────────────────────────────────────────────────────────────────
  a second rod in        a Bag slot         no            its own table, and         a fiftieth to
  the Bag                                                  nothing else                 a tenth
```

**The route sign.** On **Route 119**, all five of the **Super Rod**'s slots are **Carvanha**. Not
mostly Carvanha — Carvanha, Carvanha, Carvanha, Carvanha, Carvanha. On **Route 102** all five are
**Corphish**. You do not need a rod to guess what is coming up; you need to read the sign and say
the name. It costs nothing, it is right every single time on water like that, and on **Route
118**, where **Sharpedo** takes 40% of the Super Rod's casts, it falls apart immediately. That is
the whole character of this one: perfect where the water repeats itself, worthless where it does
not.

**A notebook.** The same trick, kept between trips: write down every route you have already fished
and what came up, and guess from the book instead of the sign. It is still free. It just covers
more water, and the entries you have only seen once are the ones to distrust.

**Guess and cross out.** Carry no rod for guessing at all. Write down a guess for the next several
casts, make them, cross out everything that was wrong, guess again for what is left. It settles —
and it cannot settle anywhere except on what you would have got casting them one at a time,
because every line in the book has been checked against the water. It is free of items and free of
raising anything. What it costs is full casts, so it only pays if the book stops changing quickly.

**Stopping your own cast early.** The **Super Rod** plays between one and six rounds of dots
before anything is on the hook; the **Good Rod** plays between one and three; the **Old Rod**
plays exactly one. So make the Super Rod cast you were going to make, take what you know after
round one as the guess, and finish the cast to check it. No second item. But a rod's first round
tells you very little unless you have practised reading it, which is an afternoon you have to want
to spend.

**Suction Cups on the lead.** Put **Octillery** at the front of the party — or **Cradily**, or
**Muk** with **Sticky Hold** — and every round of every cast gets easier: it holds 85 times in 100
outright, and the 15 that fail still take the ordinary coin flip, so 92.5 rounds in 100 survive
instead of 50. You bought nothing. You reordered a party you already had. The limit is what it can
tell you: it lifts each round on its own and knows nothing about the round before it, so it will
never name the species — only that something is still down there.

**Reading the trend.** Six of Route 119's 447 fishing spots hold **Feebas**, and which six is
decided by the phrase going round **Dewford Town**. Guess the tiles from the surface and you are
hunting six needles in 447. Read the phrase and you are not guessing at all. This is the strongest
family for exactly that reason: it looks at the thing that *makes* the water, not at what floated
up out of it, and it keeps being right several casts deep where the shallower guesses have already
lost the thread.

**A rod that came with the Pokémon.** Some lines arrive already knowing how to call the next turn,
at no cost to you because somebody else did the raising —
[215](215-multi-token-prediction-and-speculation.md) and
[230](230-multi-token-prediction-and-drafting.md) are about exactly that. In rod terms it is a rod
you never had to walk to **Mossdeep City** for.

**A second rod in the Bag.** The original way. Carry the **Old Rod** the fisherman in **Dewford
Town** gave you alongside the good one, cast the cheap one, keep or throw back. It costs a Bag
slot and it costs the time to get the thing out. And it only works if the two rods are fishing the
*same water*: on Route 118 the Old Rod pulls **Magikarp** and **Tentacool** while the Super Rod
pulls Sharpedo and Carvanha, which share nothing at all, so every cast gets thrown back and you
have spent an afternoon to end up exactly where you started.

## How to choose

Read the sign first. It is free, it stacks with everything else, and it settles whether guessing
ahead helps you here at all before you have spent a Bag slot or a party slot on it. If the Pokémon
came knowing how to call ahead, use that next — somebody already paid for it. Put the afternoon
into reading the trend when the water you fish is water you fish a lot, because a guess tuned to
*your* route beats a generally excellent rod on somebody else's. Carry a second rod last, when a
good one for that water already exists and you have the Bag slot going spare.

## What a Gym Leader is listening for

* Why does an ability that helps every round equally still never name the species?
* When does reading the sign beat every rod in the Bag?
* What happens when the two rods are not fishing the same water?

## Where this stands, September 2026

The ordering is permanent: guesses will always be ranked by how much of the water they see and
what they cost to get, and that was true before any of these rods existed. The names are the part
that moves. The round counts, the 85-in-100 and the five Carvanha slots were read off the water
itself in September 2026 and are as solid as anything here; which route is fashionable to fish,
and which rod the halls hand out by default, will not be. Whatever three ways of guessing are in
favour when you read this, ask both questions of each: what does the guess get to see, and who
paid to raise it.
