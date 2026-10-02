---
id: "m085"
slug: the-prevention-paradox
style: pokemon
category: general-practice
difficulty: advanced
question: "Why can an intervention prevent many cases across a population while offering almost no individual in it a benefit they could notice?"
tags: [prevention, population-strategy, high-risk-strategy, attributable-risk, public-health]
---

# Riding the bike removes ten times more encounters than deleting the rarest slot could

Both of those are interventions on the same cave. One of them is dramatic, targeted, and aimed at
the slot a Trainer would point to if asked what the problem was. The other is a background
multiplier that no single step could detect. The arithmetic says which one matters, and it is not
close.

## One cave, two strategies, priced

```
   EVERY NUMBER BELOW IS REAL, READ OUT OF THE EMERALD ENCOUNTER DATA AND THE RATE
   TEST. Generation III land tables have twelve slots at 20 20 10 10 10 10 5 5 4 4
   1 1 per cent. Granite Cave 1F has a table rate of 10, so 10 × 16 = 160 against
   MAX_ENCOUNTER_RATE 2880:  160/2880 = 5.56% per eligible step.

     slot   %    species     level            slot   %    species     level
     ────  ──    ─────────   ─────            ────  ──    ─────────   ─────
       1   20    Zubat         7                 7    5   Makuhita     10
       2   20    Makuhita      8                 8    5   Makuhita      6
       3   10    Makuhita      7                 9    4   Geodude       7
       4   10    Zubat         8                10    4   Geodude       8
       5   10    Makuhita      9                11    1   Geodude       6
       6   10    Abra          8                12    1   Geodude       9

   BY SPECIES, WHICH IS WHERE THE ARGUMENT LIVES

     Makuhita  ████████████████████  50 %   (five slots, including both 5% ones)
     Zubat     ████████████          30 %   (two slots, both of them 10% or more)
     Abra      ████                  10 %   (one slot)
     Geodude   ████                  10 %   (FOUR slots: 4, 4, 1 and 1)

   OVER 10 000 ELIGIBLE STEPS, expected encounters = 10 000 × 5.56% = 555.6

     A. TARGETED AT THE TAIL. Abolish both 1% slots — slots 11 and 12, the two
        slots any Trainer would call rare.
        removed = 2% × 555.6  =  11.1 encounters

        AND NOTE WHAT IT DID NOT DO. Both rare slots are Geodude, and Geodude is
        not rare: it holds 10% of the table, because 8 of those 10 points are in
        slots 9 and 10 at four per cent each. The intervention aimed squarely at
        the tail removed a fifth of one species and left four fifths of it, plus
        every Makuhita, Zubat and Abra, exactly where they were.

     B. POPULATION. Get on the Mach Bike. The rate test multiplies the rate by
        80/100, 160 → 128, so 128/2880 = 4.44% a step.
        encounters = 444.4,  removed  =  111.1 encounters

                                         B / A  =  TEN TIMES

     and the engine offers four more levers of the same kind, in its own order:
        Mach Bike or Acro Bike    × 80/100
        Black Flute               ÷ 2
        Cleanse Tag on the lead   × 2/3
        Stench or White Smoke in slot one   ÷ 2

        bike and Black Flute together:  160 → 128 → 64  = 2.22% a step
        encounters = 222.2,  removed  =  333.3 encounters

   NOW THE SAME THING FROM ONE STEP'S POINT OF VIEW

        on the bike      4.44 % chance of an encounter on this step
        off it           5.56 %
        difference       1.11 percentage points

        → 99 steps in 100, the bike did nothing whatever for that step. On the
          hundredth you cannot tell either, because the step that did not produce
          an encounter looks exactly like the 94 that were never going to.
```

The two blocks are both correct and they are sums over different things. That is the same shape
m049 found in the **Safari Zone**, and the attribution point is identical: of the 111 encounters
the bike removed, **not one of them can be named**. There is no step to point at. The saving is a
rate, and what a Trainer experiences is a step.

## The second form: maxHP/16, to everybody, every turn

```
   REAL MECHANICS. Sandstorm damage, Generation III, out of the weather routine:

     every battler loses maxHP/16 at the end of the turn, minimum 1, UNLESS it is
     Rock, Ground or Steel, has Sand Veil, or is underground or underwater.

   RUN IT OVER THE SAME CAVE'S CAST, WITH THEIR REAL TYPES

     Geodude    Rock/Ground   exempt twice over, by two of its own types
     Zubat      Poison/Flying  maxHP/16 a turn
     Makuhita   Fighting       maxHP/16 a turn
     Abra       Psychic        maxHP/16 a turn

        per turn        6.25% of a bar       — nothing anybody plans around
        eight turns     50% of a bar         — and that is what the sixteenth
                                               turn turns out to have needed
        and Leftovers   restores maxHP/16    — the same denominator, which is
                                               why the pair cancel exactly

   AND THE UPSTREAM ACT IS ONE ACT. Tyranitar's Sand Stream fires when it enters
   the field and sets the weather for everybody present, on both sides, including
   the battlers that arrive later. Nobody experiences it as aimed at them, and the
   battle text never attributes any outcome to it.
```

Small, universal, unattributable, and decisive in aggregate. The established device for this is
**Leftovers**, which m002, m005, m022 and m026 all use for the same property from the other
direction; this is its sign reversed, and a population measure is the Leftovers tick applied to a
whole region.

## The counterweight, stated as strongly as the argument

A population lever is indiscriminate, and that cuts both ways. Suppose what the Trainer actually
wants out of Granite Cave is the **Makuhita** in slot 7, the level-10 one, 5% of the table:

* **On the bike**, that slot arrives 22.2 times per 10 000 steps instead of 27.8. The population
  lever took exactly a fifth of the thing being hunted along with a fifth of every **Zubat**,
  every **Geodude** and every other **Makuhita**. It has no idea what you are looking for.
* **With a Repel and a level-10 first conscious party member**, every slot below level 10 is
  cancelled and slot 7 is the only survivor. The same 27.8 encounters arrive, all of them the one
  you wanted, and the walk is quiet in between. That is m081's threshold doing the job no
  multiplier can do.

So where the thing you care about really is concentrated in one slot, the targeted instrument is
the only one that works, and it is more efficient per use than anything applied to the whole cave.
The error is not choosing one. The error is running the targeted instrument and claiming it
covered the cave, when 80% of what comes out of the ground is in the first six slots and nothing
aimed at the tail can reach it.

## Where the metaphor stops

Someone can take a medicine, or make a change, every day for twenty years, derive nothing
detectable from it, and have been entirely right to do it. That is a hard thing to be told and it
should not be dressed up: the expected value was positive, the realisation for that individual was
zero, both statements are true, and neither cancels the other. Saying so in advance — that what is
on offer is a small shift in a probability rather than a promise — is more respectful than
implying a benefit that cannot be delivered to a named person.

The second thing is about who carries the burden. A population measure delivered as individual
advice asks for daily effort, money, time and attention, and those are not equally available.
Advice is cheapest to follow for the people who already have the most room to follow it, so a
population strategy run entirely through exhortation can widen the gap it was meant to close.
That is m050's argument and it applies here at full strength. Measures that change the default
rather than the instruction are preferred partly because they work and partly because they do not
charge the people with the least capacity the most to comply.

And a closing caution that belongs outside any analogy: none of this makes one person's own
decision unimportant, and none of it licenses pressing a population measure on somebody who has
weighed it and declined. That decision is theirs, and m083 is about how it should be held.

## What a Gym Leader is listening for

Whether the Trainer does the sum rather than asserting the conclusion — slot percentages against
the step rate, with the 80/18/2 split named. Then the ten-fold comparison, and the per-step figure
of 1.11 points beside it. Then the attribution point: that no removed encounter can be identified,
and what that implies about arguing the case one step at a time. Then the sandstorm, as the same
property with the sign flipped. Then the counterweight, offered unprompted, including what the
bike does to the slot you actually wanted. Then the hard one: how they would recommend the bike to
a Trainer who will walk 10 000 steps and feel nothing.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The published monograph on preventive strategy associated with Geoffrey Rose, in its current
  edition. It is named by author rather than by title or year here because the title and edition
  were not checked against the book itself, and a reader should confirm both before citing it.
* A current textbook of epidemiology or public health, for population attributable fraction, for
  the distinction between relative and absolute risk reduction, and for the derivation of the
  number needed to treat.
* The national prevention or public-health strategy applying where the reader works, for which
  measures are population measures locally and what is actually delivered
  (**country-dependent**).
* The primary literature on whichever specific preventive intervention is in question, for the
  absolute effect size and the harms, since the argument here is structural and supplies no
  figures.
* Any systematic review of structural or default-changing interventions against advice-based ones
  for the same risk factor, for the comparison this answer's third claim rests on.

The Pokémon figures are a separate matter and are not covered by the line above. The Generation
III twelve-slot land encounter percentages, the Granite Cave 1F table with its species, levels
and encounter rate of 10, the rate test multiplying by 16 and comparing against a maximum
encounter rate of 2 880, the bike multiplier of 80/100, the Black Flute's halving, the Cleanse
Tag's two-thirds and the halving by Stench or White Smoke in the lead slot with the order they
are applied in, the Rock/Ground, Poison/Flying, Fighting and Psychic typings of Geodude, Zubat,
Makuhita and Abra, Tyranitar's Sand Stream setting the weather on entry, the Repel check
cancelling any rolled level below that of the first party member with HP remaining, sandstorm
damage of maxHP/16 per turn with a floor of 1 and its exemptions for Rock, Ground and Steel
types, for Sand Veil and for the semi-invulnerable states, and Leftovers restoring the same
maxHP/16, were all read directly from the pret decompilation projects, which this environment
can reach. Generation III sandstorm carries no Special Defence boost for Rock-types; that is a
later change and is not in this weather routine.

## Scope and safety

This is revision material about the structure of preventive reasoning, written for someone
already training in or qualified for the field. It is not a clinical reference, not a decision
aid, and nothing here is advice to any individual about whether to take, continue or stop a
preventive intervention — that belongs with the clinician who knows them. No risk factor,
threshold, effect size or number needed to treat is named here on purpose: those are specific to
the intervention and the population, several are contested, and all are revised. The encounter
percentages and damage fractions above are real and stand in for a mechanism; none of them is a
clinical quantity and no clinical figure should be read out of them. If someone is unwell right
now, the relevant action is to contact local urgent care or the local emergency number, not to
read this.

## Where this stands, October 2026

The arithmetic is arithmetic and will not move, and the population-against-high-risk distinction
has been stable for decades. What moves is everything applied: which interventions are offered as
population measures, at what thresholds, with what evidence of absolute benefit, and whether
delivery is structural or advisory. The evidence base for default-changing and environmental
measures has grown substantially over the last decade and continues to; the balance between
population and high-risk approaches for specific risk factors is argued about actively and differs
by country. The Emerald numbers are stable because the games are finished. Take specific
thresholds, effect sizes and programme details from current local guidance rather than from here,
as of October 2026.
