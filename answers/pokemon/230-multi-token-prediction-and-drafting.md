---
id: "230"
slug: multi-token-prediction-and-drafting
style: pokemon
category: open-weights
difficulty: advanced
question: "Multi-token prediction shows up as a training objective and as a decoding trick. Are they the same thing?"
tags: [multi-token-prediction, speculative-decoding, deepseek, inference, throughput]
---

# Xatu calls two turns out. Sometimes to win, sometimes just to go faster.

It is the same foresight doing two different jobs. While you are **raising** **Xatu**, making it
name where the opponent will be two turns from now makes it better at *this* turn — that is a
quality argument. Once **Xatu** is raised, the same foresight is a free scout you have already
paid for — that is a speed argument. The interesting case is when it is literally the same move:
trained as **Future Sight**, kept beside **Psychic** and **Roost** in the moveset, and re-used at
the **Battle Tower** to call the next turn before it happens.

Question [033](033-speculative-decoding.md) covers why a wrong call can never change the outcome.
This is the part that decides whether calling ahead is worth doing at all.

## Learning to aim two turns out

**Xatu** does not fire **Future Sight** and then wait idly. Future Sight lands two turns after it
is used, which means aiming it is a claim about a board that does not exist yet — who will have
switched, whether **Gengar** is still standing, whether the **Light Screen** and the **Reflect**
will have run out, whether the **Leftovers** will have made the difference. **Jirachi** does the
same thing with **Doom Desire**, and **Espeon** learns the same foresight off a much faster body.

```
   raising                                          battling

   this turn ─┬─► the move you use now              this turn ─┬─► the real move  (kept)
              │                                                │
              └─► Future Sight ─► where they will  ►           └─► Future Sight ─► the call
                   │             be two turns on                     │
                   └ same trainer, same moveset,                     └ same move, now
                     one more slot's worth of work                     a guess to check

   both sharpen the same Pokémon.                   the call is optional; drop it and
   that is the quality claim.                       the battle goes exactly the same.
```

Two things follow. Every turn now teaches twice — once about now, once about two turns from now —
and the Pokémon is pushed to set up rather than react, because this turn's read has to still be
good two turns later. The claim is that it stays better even with Future Sight taken back off the
moveset. Treat that as a claim: it is one Trainer's own testing, not a law of the chart.

## Calling ahead, and what a call costs

Let the scout call the next few turns, resolve them all in one go, keep the longest run that
survives, and take the one turn you were always going to get anyway. With `α` the share of calls
that hold:

```
   E[turns per check]  =  (1 − α^(γ+1)) / (1 − α)

   cost of a round  ≈  γ · c + 1     c = what a call costs ÷ what a real turn costs  (≈ 0.1)
   gain             ≈  E[turns] / (γ · c + 1)
```

```
        α       γ=1              γ=2              γ=4              γ=7
   ─────────────────────────────────────────────────────────────────────────
      0.90   E 1.90  ×1.73    E 2.71  ×2.26    E 4.10  ×2.93    E 5.70  ×3.35
      0.80   E 1.80  ×1.64    E 2.44  ×2.03    E 3.36  ×2.40    E 4.16  ×2.45
      0.60   E 1.60  ×1.45    E 1.96  ×1.63    E 2.31  ×1.65    E 2.46  ×1.45
      0.40   E 1.40  ×1.27    E 1.56  ×1.30    E 1.65  ×1.18    E 1.67  ×0.98
   ─────────────────────────────────────────────────────────────────────────
                                                                    ▲
                      at α = 0.4 and seven turns called, you are slower
                      than if you had just battled
```

Read that corner first. The turns you gain never go *down* as you call further ahead — but the
gain does, because every call you threw away still cost you the calling. The further ahead it is
worth guessing falls as your guessing gets worse, and past some point the right answer is to stop
guessing.

The published numbers sit on this table exactly, and the coincidence is a nice one. Every damage
calculation is multiplied by one of sixteen rolls between **85 and 100** — the low roll and the
high roll of the same move. A call that holds on fourteen of those sixteen rolls holds 87.5% of
the time, and with one turn called the formula is just `1 + α`: 1.88 turns a check. The reported
figures for the best of these — an 85–90% hit rate on the second turn, and 1.8× the turns per
minute — land right there, with the difference being what the calling itself cost. That is the
check to run on anybody who tells you their scout doubled their speed.

## Who you are facing decides everything

`α` is not something the Pokémon has. It is something the **matchup** has, and five things move
it:

* **How predictable the opponent is.** **Youngster Joey**'s **Rattata** leads with **Tackle**
  every single time and your scout will call it perfectly. **Cynthia**'s **Garchomp** will not be
  called — **Ice Beam** answers it at 4×, which is exactly why she does not let it sit there —
  and the first turn after a switch is the worst call of the battle. A **Clefairy** using
  **Metronome** cannot be called at all: it is a different move every turn by design.
* **How wide the rolls are.** An **Earthquake** that kills on all sixteen rolls is a call that
  always holds. A **Stone Edge** that kills on nine of sixteen is a coin flip you paid to guess.
  **Focus Blast** at 70% accuracy is worse still, and **Sheer Cold** at 30% worse again — the call
  can be right about everything and still miss.
* **How many battles you are running, and this is the one people miss.** One battle at a time in
  the **Battle Tower**, you are waiting on **Xatu** and the scout's work is free. Running every
  floor of the **Battle Frontier** at once, every called turn is a turn somebody else wanted, and
  the calling starts taking the floor away from the battling. Any **Battle Maison** worth the name
  stops scouting above a certain number of simultaneous battles — so a gain measured in one quiet
  battle tells you nothing about a full building.
* **How long the record is.** Checking a call means reading back over everything that has already
  happened, and at turn 200,000 that is not the cheap step it was at turn 2,000 — the same
  **Vs. Recorder** arithmetic as [228](228-attention-variants-and-kv-arithmetic.md).
* **Who is scouting.** A strong Pokémon is not automatically a good scout. What matters is
  agreeing with the one who actually decides, not being strong — which is why foresight raised on
  **Xatu** itself calls **Xatu** better than a separately raised **Alakazam** of the same cost,
  even though Alakazam is plainly the better Pokémon.

What never moves is the result. A wrong call is discarded and the real turn happens exactly as it
would have — **Sucker Punch** simply fails when you read it wrong, and nothing else changes. A bad
scout costs you time and can never cost you the battle. That asymmetry is why calling ahead is
safe to try on a live streak: the worst case is that it does not help.

## Where this stands, September 2026

Purpose-raised scouts are reported to have arrived in all three of the big halls during early
2026, and "comes with foresight already in the moveset" is now a normal line on a Pokémon's
paperwork — DeepSeek's line carries one, and so do the GLM-5.x and Kimi releases. Treat the
headline speed-ups as the perishable part: they were measured at a number of simultaneous battles,
a record length and a roll spread that are probably not yours. The durable parts are the two sums
above, and the habit of asking of any claimed gain: *how many battles at once, and how often did
the call hold?* The paperwork itself was behind a gate I could not pass, so the hit rates and hall
support here come from write-ups rather than first hand.

## What a Gym Leader is listening for

* Why do the turns gained keep rising while the gain itself falls?
* Why does scouting stop paying once the hall is full?
* Is the stronger Pokémon always the better scout?
