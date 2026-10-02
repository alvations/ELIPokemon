---
id: "m081"
slug: referral-thresholds-and-gatekeeping
style: pokemon
category: general-practice
difficulty: advanced
question: "Why is a referral decision a threshold rather than a judgement, and what is a gatekeeper actually optimising?"
tags: [referral, decision-threshold, gatekeeping, case-mix, capacity]
---

# A Repel is a threshold, and the number it uses is not the one you think

The **Repel** family is this specialty's referral filter. m011 pinned it down and m048 reused it;
this answer is about the one quantity those two left alone — **the number**. Because a Repel does
not refuse weak Pokémon or boring Pokémon. In Emerald the engine rolls the encounter slot, rolls
the level from that slot, and only then compares that level against one number, and if the rolled
level is below it the encounter is cancelled outright. Everything interesting about referral
thresholds is in the choice of that number.

The number is the level of **the first Pokémon in your party with any HP left that is not an
egg**. Not the lead. The routine walks the party in order and stops at the first conscious one. So
the threshold can change mid-route without anybody choosing to change it, and when the whole
party is out of action the routine falls through to its final return and cancels *everything*. A
Repel with nothing conscious behind it is a filter that refers nobody.

## One route, three thresholds, and the arithmetic done

```
   EVERY NUMBER BELOW IS REAL, READ OUT OF THE EMERALD ENCOUNTER DATA AND THE WILD
   ENCOUNTER ROUTINE. Generation III land tables have TWELVE slots, and the slot
   chances are percentages — 20 20 10 10 10 10 5 5 4 4 1 1 — not the ten-slot
   x/256 table that Red and Blue use. Do not carry one across.

   ROUTE 116.  Table encounter rate 20, so the per-step odds are 20 × 16 = 320
   against MAX_ENCOUNTER_RATE 2880:  320/2880 = 11.1% per eligible step.

     slot  %    species      level          slot  %    species      level
     ────  ──   ──────────   ─────          ────  ──   ──────────   ─────
       1   20   Poochyena      6              7    5   Taillow        7
       2   20   Whismur        6              8    5   Taillow        8
       3   10   Nincada        6              9    4   Poochyena      7
       4   10   Abra           7             10    4   Poochyena      8
       5   10   Nincada        7             11    1   Skitty         7
       6   10   Taillow        6             12    1   Skitty         8

     by level:   L6 = 60%      L7 = 30%      L8 = 10%
     the thing being hunted:   Skitty, in two slots, 2% in total

   NOW SET THE THRESHOLD. Per 1 000 eligible steps, hunting Skitty:

   ┌──────────────┬───────────┬──────────────┬───────────────┬──────────────────┐
   │ threshold    │ slot rolls│ encounters   │ Skitty as a   │ Skitty actually  │
   │ (first       │ surviving │ per 1 000    │ share of what │ met per 1 000    │
   │ conscious)   │           │ steps        │ gets through  │ steps            │
   ├──────────────┼───────────┼──────────────┼───────────────┼──────────────────┤
   │ no Repel     │  100 %    │  111.1       │   2.0 %       │   2.22           │
   │ level 7      │   40 %    │   44.4       │   5.0 %       │   2.22           │
   │ level 8      │   10 %    │   11.1       │  10.0 %       │   1.11           │
   │ level 9      │    0 %    │    0         │   undefined   │   0              │
   └──────────────┴───────────┴──────────────┴───────────────┴──────────────────┘

   READ THE LAST TWO COLUMNS TOGETHER. That is the whole argument.

   6 ──► 7   FREE. The excluded region (every level-6 slot) contains no Skitty, so
             yield goes up two and a half times and not one Skitty is lost.
   7 ──► 8   PAID. The criterion now cuts THROUGH the thing being hunted. Yield
             doubles again and half the Skitty go with it — and not a random half:
             slot 11 specifically, the level-7 one, every single time.
   8 ──► 9   The route reads EMPTY. Perfect precision, nothing found, and a Trainer
             who only kept the yield column would call this their best walk yet.

   Abra is the other casualty and it is cleaner. Abra sits in exactly one slot at
   level 7, 10% of the table. At threshold 8 it does not become rare. It becomes
   unreachable, and no amount of walking recovers it.
```

## The second filter, which announces nothing

The level comparison is not the only thing the engine runs. If the Pokémon in party slot one has
**Keen Eye** or **Intimidate**, is above level 5, and the rolled level is at least five levels
below it, the encounter is cancelled on a coin flip — `Random() % 2`. A soft threshold, on the
same quantity, with a completely different shape.

Walk Route 116 behind a level-12 **Pidgey**, which has Keen Eye, and with no Repel at all:

* levels 6 and 7 are 90% of the table and all of it is five or more levels down, so each of those
  rolls survives half the time; level 8 is untouched
* slot rolls surviving: 90 × ½ + 10 = **55%**
* Skitty met per 1 000 steps: 111.1 × (½ × 1% + 1%) = **1.67**, against 2.22 with nothing running

A quarter of the Skitty, gone, from a filter nobody switched on. And note which Pokémon each
filter reads. The Repel threshold comes from the first *conscious* party member; the ability check
reads party slot one whether it is conscious or not. Two filters, two different Pokémon, one
walk. A **Mightyena** lead with Intimidate does the same thing and the Trainer experiences neither
as a decision.

The asymmetry that matters is in the reporting. A Repel has a step counter — 100 for a Repel, 200
for a **Super Repel**, 250 for a **Max Repel** — the engine counts it down and runs a script to
tell you when the last step is spent. It also refuses to be topped up: use another one while the
first is still running and the game says the effects lingered and nothing happens, which is the
same refuse-to-refresh behaviour m057 found in the terrain routine. Keen Eye prints nothing, ever.
A declared threshold can be audited. An undeclared one is just inherited.

## Urgency is a different dial, and the mass outbreak is the proof

A **mass outbreak** is an encounter with an expiry date on it, which very little else in Emerald
has. The television reports a species, a location and a level; the engine stores them along with a
probability taken from the report, and sets `outbreakDaysLeft` to **2**. Each day the counter is
decremented, and when it runs out the whole thing is cleared — species, level, moves, probability,
all back to zero.

The probability is whatever the report fixed it at. The window is the part that does the work
here, and the two dials come apart cleanly:

* **how likely** the thing is, which decides whether it is worth acting on at all
* **how long it will still be there**, which decides whether acting can wait

And then the part that should make a gatekeeper sit up. The outbreak path in the step routine is
called with `WILD_CHECK_REPEL | WILD_CHECK_KEEN_EYE` — *the standing filters still apply to it*.
A Repel set an hour ago for an ordinary reason will cancel the two-day opportunity exactly as
readily as it cancels a **Whismur**, and it will not say that it did. The only route that reaches
an outbreak with every filter off is the one that passes a flag word of zero: **Sweet Scent**.

A threshold tuned for routine traffic is applied to the time-critical case too, unless something
is built to exempt it. That is the whole argument for a separate fast route, and it is why a route
that exists on paper but inherits the ordinary filters is not a fast route.

## What the Trainer is optimising, which is four things at once

1. **Which instrument, in which order.** **Sweet Scent** costs one turn and 1 PP out of 20 and
   draws the real table with every filter off, because the field routine is called with its flag
   word set to zero. It is the cheap second look, and it is almost never used.
2. **What the next place sees.** A filtered walk hands the next decision a different population
   from the one in the table, which is exactly why the reading taken there performs differently.
   That is m011's point, read from the filter's end rather than the floor's.
3. **The doubt that stays behind.** Threshold 8 leaves slot 11 in the table, untouched, every
   step. Setting a threshold is a decision to carry what it excludes, which is why m012's net is
   the other half of this answer and not an optional extra.
4. **A budget that someone else is also spending.** The **Safari Zone** states this in the
   hardest possible form: 30 Safari Balls, a step counter set to 500, and the visit ends on the
   counter rather than on the business. Every ball thrown at an **Oddish** is a ball not available
   for the **Wobbuffet** in slot 12, and m049 worked that arithmetic through in full.

## Where the metaphor stops

Both errors land on people, and they land on different people. A threshold set too high sends
someone back to a waiting room with something that is quietly progressing, and the reasoning that
sent them there was defensible and was wrong about them. A threshold set too low means another
person waits longer for the assessment that would have changed their management, and nobody will
ever be able to name them, because the harm of a longer queue is spread across everyone in it.
Those two harms cannot be compared by feel in the moment, which is precisely why the comparison
is worked out in advance as a ratio of costs.

A second thing belongs here rather than inside an analogy. The people least likely to be referred
are frequently the least likely to come back, for reasons that have nothing to do with their
chance of being ill — work, language, cost, transport, caring responsibilities, confidence, or
having previously not been believed. A threshold is applied to presentations, never to need, and
the two populations are not the same.

## What a Gym Leader is listening for

Whether the Trainer can state the threshold as a *number* and then say what the number is made of
— which two costs, and who pays each. Then the free move against the paid one: why 6 to 7 cost
nothing and 7 to 8 cost half the Skitty, without being prompted. Then which slot was lost, by
name, and the observation that it is the same slot every time. Then the filters nobody switched
on, and which party member each one reads. Then the budget point: that the 30 balls and the 500
steps belong to the whole visit. Then the awkward one — how a Trainer would ever discover that
their threshold is wrong, given that the walk that finds nothing looks exactly like the route
that holds nothing.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The suspected-cancer and urgent-referral criteria issued by the national or regional body
  governing the reader's practice, which are the actual thresholds and are revised on a cycle
  *[country-dependent]*.
* The referral and acceptance policy of the receiving service the reader refers into, for the
  second threshold — the one applied after the referral leaves.
* A current textbook of clinical epidemiology or clinical decision analysis, for the derivation
  of the test and treatment thresholds from the ratio of error costs.
* The reader's own organisation's referral audit and rejected-referral data, which is where the
  local evidence about where the threshold actually sits lives.
* The published literature on referral variation between practices and between clinicians, for
  how much of the variation is explained by case mix and how much is not.

The Pokémon figures are a separate matter and are not covered by the line above. The Generation
III twelve-slot land encounter percentages, the Route 116 table with its levels and its encounter
rate of 20, the rate being multiplied by 16 and compared against a maximum encounter rate of
2 880, the Repel check reading the first party member with HP that is not an egg and cancelling
when the rolled level is lower, the same routine's final return cancelling everything when no
such Pokémon exists, the Keen Eye and Intimidate check reading party slot one with its
greater-than-level-5 condition, its five-level gap and its one-in-two roll, the mass outbreak
storing a species, level and probability with a days-left counter set to 2 and clearing every
field when it expires, the outbreak encounter path being called with both the Repel and Keen
Eye check flags set while the Sweet Scent path passes zero, Pidgey's Keen Eye and
Mightyena's Intimidate, the Repel step counts of 100, 200 and 250, the script that reports a
Repel wearing off, the refusal to stack a second Repel, Sweet Scent's 20 PP and its field call
passing a flag word of zero, and the Safari Zone's 30 balls and 500-step counter, were all read
directly from the pret and rh-hideout decompilation projects, which this environment can reach.

## Scope and safety

This is revision material about the structure of a referral decision, written for someone already
training in or qualified for the field. It is not a clinical reference, not a decision aid, and
nothing here should inform whether any individual is referred — that belongs with the clinician
who has assessed them and with current local criteria. No referral criterion, age cut-off,
timescale, probability or threshold value is named here on purpose: all of them are local, several
are contested, and all are revised. The encounter percentages above are real and stand in for a
mechanism; none of them is a clinical probability and no clinical figure should be read out of
them. If someone is unwell right now, the relevant action is to contact local urgent care or the
local emergency number, not to read this.

## Where this stands, October 2026

The structural claim — that a referral threshold is a ratio of two error costs, that prevalence
positions a person against it rather than moving it, and that raising it loses cases
systematically rather than randomly — is settled decision theory and will not move. Everything
operational will: which routes exist, what they promise, which criteria they require, what the
downstream capacity is, and which investigations can be requested before referral rather than
after it. Direct-access testing has moved several of these decisions upstream in some systems and
that process is continuing unevenly. The Emerald numbers are stable because the games are
finished. Take criteria and routes from current local guidance rather than from here, as of
October 2026.
