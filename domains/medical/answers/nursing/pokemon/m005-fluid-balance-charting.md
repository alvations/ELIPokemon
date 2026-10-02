---
id: "m005"
slug: fluid-balance-charting
style: pokemon
category: nursing
difficulty: advanced
question: "What does a fluid balance chart actually measure, what does it miss, and how does it connect to the circulation?"
tags: [fluid-balance, urine-output, perfusion, charting, assessment]
---

# You could add up every Leftovers tick. Or you could read the number on the screen.

A fluid balance chart is the per-turn ledger, kept by hand. The games are full of effects that
move HP by a fixed share every turn, and every one of them could be written in a column:

```
   ┌──────────── COUNTED, and therefore in the ledger ───────────────────────────┐
   │  IN                                   OUT                                   │
   │  Leftovers, a sixteenth of maximum    Life Orb, a tenth of maximum every    │
   │    HP at the end of every turn          time the holder attacks             │
   │  Black Sludge, a sixteenth — but      Black Sludge, an EIGHTH — if it is    │
   │    only to a Poison-type holder         anything else                       │
   │  a Sitrus Berry, 30 in one go in the   Leech Seed, an eighth every turn,    │
   │    Advance games; a Potion there, 20    handed to the other side            │
   └─────────────────────────────────────────────────────────────────────────────┘
                 │                                      ▲
                 │                                      │
   ┌─────────────▼──────────────────────────────────────┴────────────────────────┐
   │  NOT COUNTED, and therefore invisible to the arithmetic                     │
   │                                                                             │
   │  THE WEATHER — a Sandstorm takes a sixteenth off everything that is not     │
   │    Rock, Ground or Steel, every turn, and you did not set it, were not      │
   │    asked, and may have forgotten it is running. The more trouble the        │
   │    Pokémon is in, the bigger the thing the ledger cannot see                │
   │  WHAT SOMEONE ELSE DID — a berry eaten automatically off the field, a       │
   │    Pokémon healed while you were not looking                                │
   │  WHERE IT WENT — see below. This is the big one                             │
   └─────────────────────────────────────────────────────────────────────────────┘
```

Two things follow before anything else. **The ledger is a trend instrument**, and one turn's entry
is noise. And **every entry is something somebody counted**, so the ledger's relationship to the
Pokémon's actual state runs entirely through what nobody counted.

Which is why the HP bar exists. The exact number on the summary screen is not an estimate and it
does not inherit a missed turn — it is the net, after everything, including the Sandstorm you
forgot. The arithmetic is only as good as the worst-recorded turn. The number is just right.

## Where it went: why a balanced ledger is not a reassuring ledger

**Substitute** costs a quarter of the user's maximum HP and builds a decoy that holds exactly that
much. The HP came off the bar. It did not leave the battle.

```
   everything the Pokémon has             the part that actually takes hits
   ┌──────────────────────────────┐       ┌──────────────────────┐
   │                              │       │  the Pokémon itself  │
   │  the Substitute ████████████ │       │  ░░░                 │  ◄── everything
   │  a quarter of maximum HP,    │       │                      │      that matters
   │  standing in front, taking   │       │  nearly empty        │      happens HERE
   │  the hits, holding HP that   │       └──────────────────────┘
   │  can never come back         │
   │                              │
   │  the Pokémon ░░░             │
   └──────────────────────────────┘
          plenty of HP in the room             and almost none where it counts
```

That is the whole point. A Pokémon behind a fat **Substitute** with a nearly empty bar has HP
accounted for and HP unavailable at the same time, and no sum over the ledger can tell the two
apart. **Belly Drum** is the same lesson in one action rather than many: it halves the user's
maximum HP outright to drive Attack to +6, the biggest single swing in the game, and nothing in a
per-turn ledger predicted it.

## The resource that runs out first

Here is the part people miss. **PP, not HP, is usually what runs out.**

PP is counted in four small separate columns, one per move, and the games enforce the **Four-Move
Limit** so there are never more than four. When all four reach zero the Pokémon is reduced to
**Struggle** — it attacks anyway, with nothing, and hurts itself doing it. A full HP bar and four
empty columns is a Pokémon that cannot do the thing you are relying on it for, and the bar will
tell you nothing about it at all.

So the small columns are an early warning that the big number does not carry. And like every early
warning they can be read wrong:

```
   what you see                       what it might mean instead
   ─────────────────────────────────  ──────────────────────────────────────────────
   the move cannot be used            DISABLE. The PP is there. The move is simply
                                      blocked from outside, and nothing about the
                                      Pokémon has changed. CHECK THIS FIRST before
                                      concluding anything about the Pokémon
   the move cannot be used            Taunt, if it is a status move; Encore, if it is
                                      being forced to repeat a different one
   PP is gone and nothing was used    somebody took it. Spite removes PP from the
                                      last move used without it being spent
   PP looks fine                      a Leppa Berry restored 10 of it automatically.
                                      The reading was repaired; the problem that
                                      emptied it was not
   PP looks fine                      an Ether put 10 back into one move, or a
                                      Max Elixir refilled all four — so the reading
                                      is now about the bag, not the Pokémon
```

The Disable line is the one to hold onto. It is the only entry in the table where the correct
first action is to check the equipment rather than examine the Pokémon, and it is also the
commonest.

## Where the ledger fails as a measurement

**A missing turn is not a small error.** Leave one turn out and the cumulative total is wrong from
there on, permanently and silently. It does not degrade — it breaks.

**It is coarser than it looks.** A sixteenth of maximum HP on a Pokémon with 9 HP is rounded to 1,
because the game refuses to let it be zero. Every figure in the column is a rounding of something.

**One turn is not a reading.** The slope across many turns is the measurement.

**And it is not on the main screen.** None of this appears in the status slot or the stat stages —
the composite read from the summary screen and this ledger are two instruments, read together, and
neither contains the other.

## Where the metaphor stops

The mechanism above is a mechanism. What it is attached to is not, and it goes wrong in both
directions.

Too little fluid causes poor perfusion, kidney injury, delirium, falls, and in a frail older
person a cascade that is hard to reverse. Too much causes fluid on the lungs, breathlessness,
longer time on a ventilator, wounds that will not heal, and a swollen patient who cannot get out
of bed. The second direction is the one that gets underestimated, and it is iatrogenic — it is
something done to a patient rather than something that happened to them.

A fluid balance chart is one of the dullest documents on a ward and one of the few continuous
measurements of whether a person's circulation is being managed correctly. It is also among the
most frequently left incomplete. Both of those are true at once, and the second is the reason the
first is worth insisting on at the end of a long shift.

## What Nurse Joy is listening for

Why the thing the ledger cannot see gets *bigger* in exactly the Pokémon whose ledger matters
most. How a healthy-looking total and an empty bar sit together, and what else to look at to tell
them apart. Why the exact number beats the sum of the increments. The whole confounder list for
the small columns, starting with **Disable**. And why none of this appears on the status screen,
and what is done about that.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* The fluid balance chart and fluid management policy in use in the reader's own institution — the
  authority for what is charted, how the cumulative total is presented, and what the local
  oliguria definition and escalation point are.
* The reader's national guidance on intravenous fluid therapy in hospital, for assessment,
  monitoring and the reasoning behind replacement decisions.
* The reader's national or international guidance on acute kidney injury, for urine output as a
  monitoring parameter and for its confounders.
* A standard renal or applied physiology textbook, for the compartment reasoning and for the
  continuous unmeasured losses, which are mechanism rather than guideline.
* The reader's institutional audit of fluid chart completion, if one exists, for the
  measurement-quality claim — the claim here a reviewer should check first, because its strength
  depends entirely on which audit is read.
* Guidance on hydration and fluid management in older people and in frailty from the reader's
  national body.

Separately, and unlike the above: the fractions, the restored amounts, the Four-Move Limit and the
item and move effects in this answer were checked against the games' published data and their
public disassemblies, which this environment could reach.

## Scope and safety

This explains what a measurement is and is not, for someone already training in or qualified for
clinical practice. It is not a protocol, not a decision aid, and it contains no clinical volumes,
no replacement regimens and no thresholds, deliberately — every number in it belongs to a video
game. Fluid prescribing, oliguria definitions and escalation points are set by local guidance,
which is the authority; this is not, and it has had no clinical review. Nothing here is for use in
an emergency or for a decision about any person's care, including any decision about how much
anyone should drink. If someone is unwell right now, the local emergency number is the correct
response.

## Where this stands, October 2026

The physiology does not move: compartments, continuous unmeasured losses, the kidney's sensitivity
to perfusion, and the conservation of mass that makes a weight better than a sum. What dates is
the guidance wrapped around it — fluid therapy recommendations, replacement fluid composition,
acute kidney injury definitions and their urine output criteria, and the chart itself, which is
increasingly electronic and sometimes totalled automatically. The reader's own policy is the
authority for every clinical number. Leftovers, by contrast, has restored a sixteenth a turn since
Johto.
