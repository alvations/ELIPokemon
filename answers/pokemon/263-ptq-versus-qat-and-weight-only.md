---
id: "263"
slug: ptq-versus-qat-and-weight-only
style: pokemon
category: optimization
difficulty: intermediate
question: "When does quantisation-aware training earn its cost over post-training quantisation, and what does weight-only quantisation buy that W8A8 does not?"
tags: [quantisation, ptq, qat, weight-only, inference]
---

# Moving it forward is an afternoon. Breeding it again is a season.

There are two ways to get a finished **Garchomp** onto a team in a game it was not raised in.

**Move it forward through Pokémon HOME.** The **Gible** you hatched in **Sinnoh** goes up the
chain and comes out the other end in **Paldea**. It takes an afternoon. It is also **one-way** —
nothing walks back down — you take its held item off before it goes, and if the species is not in
the destination **Pokédex** it does not travel at all.

**Or breed it again where it is going to battle.** Leave a **Ditto** with a parent holding an
**Everstone** so the Nature passes down, and a **Destiny Knot** on the other so five of the twelve
parent **IVs** come with the egg — at the **Day Care**, the nursery, the picnic table, whatever
the destination happens to call it. Hatch, discard, hatch, discard. **EV** train the one that
comes out right. That is a season, not an afternoon, and at the end you have a **Garchomp** built
inside the rules it will fight under.

The honest summary: for a well-made Pokémon of a species that transfers cleanly, **the afternoon
is enough**. Breeding it again earns its cost in exactly three places — when the species has
almost no stat budget to lose, when you are working at the bottom of a tier where every point
shows, and when the format checks something the transfer cannot supply.

```
   MOVE IT FORWARD                           BREED IT AGAIN, THERE
   ───────────────                           ─────────────────────
   the finished Pokémon                      the finished Pokémon
            │                                         │
            ▼                                         ▼
   a few boxes looked over                   Everstone · Destiny Knot ·
   nothing is retrained                      an Egg Group that matches
            │                                         │
            ▼                                         ▼
   trim what will not travel                 HATCH AND HATCH AGAIN in the
            │                                 game it will battle in
            ▼                                         │
   same Pokémon, less written down                    ▼
                                             a new Pokémon, made KNOWING
   cost: one afternoon                       what the new rules keep
   needs: a few boxes to compare
   risk:  you compared the wrong boxes       cost: a whole season
                                             needs: the parents, the eggs
                                             risk:  now you own two of them
```

## What each one costs and what it buys

| | Move it forward | Breed it again |
| --- | --- | --- |
| To produce | an afternoon at the terminal | weeks of eggs |
| Needs | a few boxes to check against | the parents, the items, the **Egg Move** chain |
| Use it for | anything ordinary | the last few points, small species, strict formats |
| On the field | identical — it is a Pokémon | identical |
| If it goes wrong | do the transfer again | hatch the whole line again |

Look at the fourth row. **The referee cannot tell which way it got there.** Breeding again does
not make it faster or hit harder than the transfer would have; it makes it *more exactly what you
meant* at the same size. If the transferred one already wins the match-up you built it for,
breeding again buys nothing whatsoever — and knowing whether it wins that match-up is the whole of
[267](267-evaluating-a-quantised-model.md).

There is a cheap middle that is usually the right answer and worth saying out loud: **move it
forward, then do the small local work in the new game.** A **Heart Scale** at the **Move
Reminder** for the move the new format wants it knowing instead, a Mint so the Nature pushes the
right stat, an afternoon of **EV** training on local routes. You get much of what the season would
have given you for a fraction of the eggs, and it is the same trade [028](028-qlora.md) makes.

## The other axis: what is coarse, the record or the sums

That is one decision. Here is a different one, and it changes the shape of a turn.

**A shorter record** is the summary screen with fewer digits on it. You find what you need faster
because there is less to read. But the working-out afterwards is exactly the same working-out,
done to exactly the same width. Nothing about the sum got cheaper.

**Coarser sums** is the working-out itself done in whole numbers — and the games genuinely do
this. Damage is the attacker's Attack over the defender's Defense, and **every division throws the
remainder away**, one truncation after another, with a floor that says a move that connects does
at least 1. That is why a handheld can resolve a turn at all. It is also why two Pokémon whose
stats differ by one point can deal identical damage.

## The arithmetic that decides it

```
   ONE BATTLE AT A TIME — you are looking things up, not working them out
   ─────────────────────────────────────────────────────────────────────
   read the whole summary   16 units   ← six stats, four moves, the Ability,
                                          the held item, the Type Chart
   work out the damage       1 unit    ← one multiply, two divides
   ─────────────────────────────────────────────────────────────────────
   total 17.  Cut the summary to a quarter: 4 + 1 = 5.   3.4× faster,
   and not one sum was made any cheaper.

   A HUNDRED BATTLES AT ONCE — one summary, a hundred damage sums
   ─────────────────────────────────────────────────────────────────────
   read the whole summary   16 units   ← read ONCE, used a hundred times
   work out the damage     100 units
   ─────────────────────────────────────────────────────────────────────
   total 116. Cut the summary to a quarter: 4 + 100 = 104.  1.1×. Nothing.
   The sums are the wall now, and only coarser sums move a wall like that.
```

Somewhere around a hundred battles at once the two lines cross. Below it you are reading, and a
shorter record is the entire win. Above it you are calculating, and only cheaper calculation
helps. That is why one Trainer swears by a trimmed summary and another swears by whole-number
working-out: they are answering different questions. And neither column counts what the battle
itself piles up turn after turn, which at length swamps both —
[266](266-kv-cache-quantisation.md).

## What goes wrong

* **Trimming costs you at the top end.** Unpacking a short record into a usable one takes a
  moment. At one battle that moment hides inside the page-turn; at a hundred at once it is on the
  clock.
* **You compared against the wrong boxes.** Check a transfer against **Blissey** and **Chansey**
  and it will look perfect, then fall over the first time a **Machamp** is in front of it.
* **Breeding again leaves you with two.** The bred one is not a copy of the transferred one. Two
  Pokémon, two sets of numbers to keep straight, two things to undo.
* **Small species have nothing spare.** **Garchomp** can lose a point and never notice. Something
  scraping along the bottom of its tier notices every one, and that is where the eggs earn the
  season.

## What a Gym Leader is listening for

* Why does a shorter summary not make the damage sum any cheaper?
* Fixed working-out or working-out done fresh each turn — what does each get wrong?
* Would you breed a **Garchomp** again rather than move it forward? (Almost never. Say why.)
* What is the game really doing when it throws the remainder away, and why does that hold up?

## Where this stands, September 2026

Two of these are from the games' own code, which I read: damage really is Attack over Defense with
the remainder discarded at every division and a floor of 1, and a move that lands never does 0.
The transfer rules — one way only, nothing in its hands, and no travel at all for a species the
destination has never heard of — are as the services have worked for several generations, and they
are the part most likely to change with the next one. What does not change is the shape: moving it
forward and breeding it again cost wildly different amounts to *do* and nothing different to
*battle with*, while a shorter record and coarser sums cost nothing different to do and change the
battle completely.
