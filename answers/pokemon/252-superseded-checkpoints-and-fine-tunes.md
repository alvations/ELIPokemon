---
id: "252"
slug: superseded-checkpoints-and-fine-tunes
style: pokemon
category: open-weights
difficulty: intermediate
question: "The open checkpoint you deployed and fine-tuned has just been superseded. What actually changes?"
tags: [open-weights, fine-tuning, lifecycle, pinning, reproducibility]
---

# The **Everstone** is still in its hands, and nobody came to take it away

A Pokémon holding an **Everstone** does not evolve when it levels up. That is the whole item. It
is a decision you made, it is reversed only when you take the stone off, and **nothing in the
world overrides it** — a **Chansey** with an Everstone stays a Chansey however fond of you it
gets.

And it is not a sentimental choice. **Eviolite** raises the Defense and Special Defense of a
Pokémon that can *still* evolve, by half. A Chansey holding Eviolite is bulkier than the
**Blissey** it refuses to become — and that same Chansey was a **Happiny** that only got this far
because you handed it an **Oval Stone** and walked it through a morning. **Pikachu** is the same
argument without the stone: the **Light Ball** does nothing whatsoever in **Raichu**'s hands, so
the **Thunder Stone** stays in the bag. Declining to evolve buys something specific and real.

That is what "superseded" is. Your Pokémon is in your box. Your **ID No.** is on it. Its **EVs**
are where you put them, its moves are the ones you taught it, and no announcement anywhere takes a
single one of those away.

```
   STILL YOURS                          NOT YOURS AND MOVING
   ──────────────────────────────       ────────────────────────────────────────
   the individual in your box      │    what "the strong one" means to everyone
   its stats, its four moves       │    which one the guides are written about
   the terms on the ball it came   │    which quantised builds stay maintained
     in, as they read that day     │    whether the rented one still behaves so
   your **Heart Scale** notes      │    what anyone upstream will fix for you
   ──────────────────────────────  │    the sign over the workshop door
                                   │
                  only the left column is in your **PC box**
```

## The six things that do move

**1. It stops being the one everybody measures against.** Every comparison — inside your team and
out — is now against the new one. That is not a battle problem, it is a noticeboard problem, and
it arrives as "why are we fourteen points down" from someone who never asked which Gym we fight
(question 250).

**2. The guides retarget.** Strategy pages, the recipes, the tuned kernels: all of it follows.
Your setup keeps working for exactly as long as you keep it frozen — and freezing means you own
every crack that appears in it. That is the price of the Everstone, and it is an upkeep price, not
a strength price.

**3. The community's work migrates.** Fourth-party compressed builds, shared move sets, **EV**
spreads, prompt libraries. Your 4-bit build was somebody's hobby, and it is now somebody's *old*
hobby — the way nobody writes **Steelix** sets for a **Johto** the world walked past regions ago.

**4. Your raising is re-priced, not destroyed.** Two different questions that people mash
together:

- *Do the moves I taught it still work?* Yes — **on that individual, and only on it**. What you
  taught is bound to the Pokémon you taught it to. There is no **Move Deleter** trick that lifts a
  moveset off one and drops it onto another. Moving means **going back to the Move Tutor with the
  new one**, not copying anything across.
- *Do I still need them?* Often not. When a generation's whole gain is in the raising, the newer
  one may already know the thing you spent a season teaching. The first battle to run on a new
  arrival is the **untrained** one, against your own gauntlet, before you spend another **Heart
  Scale**.

**5. The rented one moves under you.** If any part of your team is a rental called by name rather
than by individual, that name now points at a different Pokémon and nobody wrote to tell you
(questions 210, 219).

**6. The sign over the door changes, literally.** The Qwen workshop has been renamed forward at
every open generation. Ask for the noticeboard under Qwen3-Next, Qwen3.5, Qwen3.6 or Qwen3.8 and
you get the same page, byte for byte, one fingerprint across four names — checked by hand. The
page that describes Qwen 3.6 now hangs under the 3.8 sign and describes 3.6 in the past tense.
Meanwhile Qwen3.6-27B was never taken off the shelf. **"Superseded" and "gone" are different
words**, and only one of them was true.

## What you should have done, and should do now

1. **Keep your own copy of the individual, exactly as it was** — the weights, the vocabulary, the
   configuration, and the **terms printed on the ball as they read that day**. Terms can differ
   between two individuals of the same species from the same shelf (question 222), and a shelf can
   be cleared.
2. **Keep the raising, not just the Pokémon.** What you fed it, in what order, from which starting
   individual, and the gauntlet you judged it on. **A trained Pokémon is a procedure you can
   repeat; the one in your box is only the result.** Trainers who kept the Pokémon and not the
   notes discover at the worst moment that they cannot raise it again.
3. **Keep the gauntlet frozen.** It turns "should we switch" from a season of arguing into one
   afternoon of battles (question 251).
4. **Put a review date on it the day you catch it**, not a retirement date. Retirement dates get
   ignored. A date written on somebody's **Trainer Card**, with their **ID No.** beside it, gets
   done.
5. **Decide, out loud, that you are holding the Everstone.** Good reasons to hold it: a league
   that checks legality, a baseline you are contractually measured against, a box with no link
   cable, a fixed budget, a long experiment that only means anything if nothing moves. The bad
   reason, and the usual one: **nobody owns the evolution.** Refusing to evolve is a real
   strategy. Forgetting to is not.

And the second half of the item is the part worth keeping. From Generation V, a parent holding an
**Everstone** always passes its **Nature** down to the Egg. The stone freezes this one *and*
carries its disposition into the next one. Pin the individual; carry the raising forward.

## What a Gym Leader is listening for

That you separate what is in your box from what is on somebody else's shelf, and that you know a
ball already in your hand is not emptied by a new one going on sale. Then that you treat the
raising as a procedure rather than a trophy. The strongest answers volunteer the uncomfortable
part: when a generation's whole gain is in the raising, the likeliest outcome of testing the new
arrival is that **your season of training has been made redundant** — and finding that out costs
one afternoon, while assuming otherwise costs a season.

## Where this stands, September 2026

The four-names, one-fingerprint rename chain, the 404 where a Qwen3.7 sign would be, and the
continued presence of Qwen3.6-27B on the lab's own dated list were all checked by hand here.
**Coverage, not first-hand:** the terms attached to each individual, whether the older ones are
still on the hubs, and how the 3.6 and 3.8 checkpoints compare — the model cards and the blog are
behind an egress block, and they are the authorities. **Nothing here is legal advice**; "the ball
in your hand stays yours" is how a permissive grant ordinarily reads and is not a substitute for
reading the one you hold. These particular individuals will be superseded again before you finish
reading. The difference between *superseded* and *gone* will not move.
