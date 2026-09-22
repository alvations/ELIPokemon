---
id: "257"
slug: acceptance-rate-in-production
style: pokemon
category: optimization
difficulty: intermediate
question: "How would you tell whether speculative decoding is actually paying for itself in production?"
tags: [speculative-decoding, acceptance-rate, observability, benchmarking, serving]
---

# By counting fish in the bucket per hour, on the pier you actually fish. The rest is clues.

How often your guess holds is a clue, not a verdict. It is not something the rod has. It belongs
to the rod, the water, the lead Pokémon, which round of the cast you are on and how many people
are on the pier — all at once — and it swings by thirty points between two spots on the same
route. The number that decides whether to keep guessing ahead is the one at the end of the day:
fish in the bucket per hour, at the crowd you actually fish in, and the longest you ever stood
there between two catches. How often the guess holds tells you *why* that number moved and what to
change. It never tells you whether you are winning.

## Where you stand changes everything

It comes back to the gap from [253](253-speculative-decoding-exactness.md): a guess holds as often
as one minus the gap between your guess's table and the water's. Water with one thing in it has no
gap to speak of. Water with twelve things in it has an enormous one.

```
   where you are standing                     a good guess holds    why
   ──────────────────────────────────────────────────────────────────────────────────────
   Route 119 water, Super Rod                    every cast         all five slots: Carvanha
   Route 102 water, Super Rod                    every cast         all five slots: Corphish
   Route 119 water, Old Rod                      7 in 10            Magikarp 70, Tentacool 30
   Route 119 water, Good Rod                     3 in 5             Magikarp 60, then two others
   Route 118 water, Super Rod                    3 in 5 at best     Sharpedo takes 40 of it
   Route 119 Tall Grass                          1 in 5             twelve slots, the best at 20
   a Feebas tile on Route 119                    2 in 300           6 of 447 spots, half the casts
   ──────────────────────────────────────────────────────────────────────────────────────
   [the last three are the ones that break a plan made on the first two]
```

Two things follow. **Which rod you hold is a dial on how predictable the water is** — the **Old
Rod** opens two slots, the **Good Rod** three, the **Super Rod** five, and stepping into the
**Tall Grass** opens twelve. Reach for a rod that shows you more of the route and you have made
every single guess harder by doing it. And **one plan should not cover the whole map**. Route
119's water and Route 119's grass are two ends of that table, twenty paces apart. Fishing them the
same way means one of them is set up wrong on purpose.

## Count which round you lost it on, not just how often you lost

Keep a proper tally: how many casts came back **"Not even a nibble…"**, how many reached **"Oh! A
bite!"**, how many ended with **"A POKéMON's on the hook!"** — and, the one that actually sets how
far ahead to plan, **which round of the cast it went wrong on**. The Super Rod asks for up to six
rounds in a row; a tally that says only "I lost four in ten" tells you nothing about whether to
plan two ahead or eight.

Each round's entry is the share of casts that got that far and kept going, so what the whole cast
is worth is one plus the entries added up, and what one more round is worth is just that round's
entry. Adding a round pays while its entry beats a tenth of what the cast is currently worth:

```
   round    held     cast worth    what it cost    gain     must beat    verdict
   ──────────────────────────────────────────────────────────────────────────────
     1      0.90       1.900          1.10        1.727       0.100      go on
     2      0.78       2.680          1.20        2.233       0.173      go on
     3      0.67       3.350          1.30        2.577       0.223      go on
     4      0.58       3.930          1.40        2.807       0.258      go on
     5      0.49       4.420          1.50        2.947       0.281      go on
     6      0.42       4.840          1.60        3.025       0.295      go on
     7      0.36       5.200          1.70        3.059       0.302      go on
     8      0.31       5.510          1.80        3.061       0.306      go on (flat)
     9      0.27         —              —           —         0.306      STOP
   ──────────────────────────────────────────────────────────────────────────────
     eight is the best depth, and six gets you 98.8% of it for a quarter less guessing
```

Two things the bare "four in ten" hides and this does not. A tally that falls off a cliff after
round one is a guess with no memory of the round before it — **Suction Cups** on the lead looks
exactly like this, because it lifts each round on its own and never carries anything forward
([254](254-draft-and-verify-families.md)). A tally that is low and flat all the way down is a
guess made for different water, and no amount of planning further ahead will rescue it.

## What actually settles it

* **Fish in the bucket per hour, on a busy pier.** Not alone at dawn. A time trial on an empty
  pier measures a day you do not have, and [256](256-speculative-decoding-at-high-batch.md) is why
  that matters more than anything else here.
* **The wait between catches, typical and worst.** Guessing ahead makes the day **lumpy** — a stop
  now brings home anywhere from one to four — so the average wait improves while the longest wait
  can get worse. And the better rod is the less forgiving one: the Super Rod gives you the
  shortest moment to strike when the line goes, shorter than the Good Rod's, shorter again than
  the Old Rod's. A worse worst case is a real cost even when the average looks lovely.
* **What the trip cost you.** Balls thrown, the **Bag** slot the second rod took, the party slot
  at the front. The honest total charges you for all three.
* **How many runs finished inside the time you had**, if you are on a clock. That is what makes
  trading fish for less standing around a decision instead of an accident.

## How to run it

1. **Check the keep rule first, or none of the rest counts.** Make sure the hall is running the
   strict throw-back rule and not a "close enough" house rule, and that anything narrowing the
   table — a **Repel** in the grass, a tile that overrides the slots — is narrowing it for the
   guess too. If either is off, your **Pokédex** is going to fill up differently and you have a
   much bigger question than timing.
2. **Fish both ways over your own logged spots before you change anything.** This is where you
   find out that one spot in thirty is a **Feebas** tile where nothing you guess will ever hold.
3. **Split the day, at the crowd you really fish in.** Because the bucket comes out the same
   either way, this is purely a question of the clock — no need to check the fish, no need to
   compare **Pokédex** entries, no arguing about quality. That is the cheapest comparison
   available to you, and it is a straight gift from the throw-back rule.
4. **Watch the hold rate per spot, not just the clock.** The phrase going round **Dewford Town**
   changes and all six Feebas tiles move. Somebody swaps the lead Pokémon. A **Lilycove City**
   restock puts a Repel in the bag. The clock notices eventually; the hold rate notices the same
   afternoon.

The mistake worth naming is the one that costs real fish. You time yourself alone at Route 119's
water with the Super Rod, where every slot is Carvanha, see the day fly past, and switch your
whole streak over. Then you walk to Route 118's water at a full pier, where Sharpedo takes 40% and
you are rationing Balls, and you are slower than if you had never guessed at all. Nothing breaks.
Nothing looks wrong. The bucket is just a third emptier than it should be.

## What a Gym Leader is listening for

* Why does the round-by-round tally say more than the overall hold rate?
* Why can the average wait get shorter while the longest wait gets longer?
* What would make you stop guessing at one spot but not at another?

## Where this stands, September 2026

The method is permanent: tally by round, decide on fish per hour at the crowd you actually fish
in, and lean on the throw-back rule to make the comparison cheap. That outlives every rod in this
arc. The slot tables, the six Feebas spots among 447, and the round counts are read off the routes
themselves and are exact. The hold rates in the first table are what you should *expect*, not what
anyone measured — they are the thing here most likely to be wrong for your water, and the one I
would replace first with your own tally. The claim I would defend unchanged in five years is the
last paragraph: the expensive mistake is not a wrong number. It is a right number, measured on a
pier nobody fishes.
