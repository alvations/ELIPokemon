---
id: "m046"
slug: chronic-disease-review
style: pokemon
category: general-practice
difficulty: intermediate
question: "Why does a structured review at a fixed interval outperform reactive consulting for a condition that produces no symptoms, and what makes a review a clinical act rather than an administrative one?"
tags: [chronic-disease, review, recall, registers, asymptomatic]
---

# The number on the summary screen is from the last time something forced a recalculation

In **Red** and **Blue** every Pokémon carries five hidden counters that nobody ever sees. Beat
something, and each counter gains that species' base stat for the matching slot: a **Zubat** has
base stats 40, 45, 35, 55 and 40 — HP, Attack, Defence, Speed, Special — so defeating one adds 45
to the Attack counter and 35 to the Defence counter, every time, for ever, up to a ceiling of
65 535 in each. This is **Stat Experience**, and the engine does not print it anywhere.

What it prints is the stats on the summary screen, and those are a *cached value*. Exactly four
events in the whole game make the engine turn those hidden counters into visible stats: a
level-up, a vitamin, a **Rare Candy**, and a withdrawal from a box. Nothing else does — a wild
Pokémon's stats are computed on arrival with the stat-experience term switched off, and nothing
in the course of a battle recomputes yours. So a Pokémon can walk the length of **Kanto**
carrying thousands of points of accumulated state while the screen shows, truthfully and
uselessly, the numbers it had the last time one of those four things happened.

Contrast the thing a Trainer *does* watch. The HP bar is drawn continuously, every turn, and when
it drops the Trainer reaches for a **Potion** or a **Super Potion** or walks back to the
**Pokémon Center**. That loop works beautifully, and it works because HP announces itself. Stat
Experience has no bar. It is the same Pokémon, in the same battles, accumulating at the same time,
and the two are sampled in completely different ways for one reason: one of them is displayed.

That gap is the whole subject, and it has arithmetic.

## What a single floor of Mt. Moon puts into the hidden counters

```
   EVERY NUMBER BELOW IS REAL, READ OUT OF THE CODE. Mt. Moon 1F, 256 rolls of its table.
   Slot chances are 51 51 39 25 25 25 13 13 11 3 out of 256, in slot order, as on every
   land table in Red and Blue. Base stats are in the order HP ATK DEF SPD SPC.

   species     /256    base stats           contributed per 256 rolls
   ─────────   ────    ──────────────────   ─────────────────────────────────────────
   Zubat        202    40 45 35 55 40       8080  9090  7070 11110  8080
   Geodude       38    40 80 100 20 30      1520  3040  3800   760  1140
   Paras         13    35 70 55 25 55        455   910   715   325   715
   Clefairy       3    70 45 48 35 60        210   135   144   105   180
   ─────────   ────    ──────────────────   ─────────────────────────────────────────
                                    TOTAL  10265 13175 11729 12300 10115

   Attack alone picks up 13 175 points per 256 encounters — one fifth of the way to the
   65 535 ceiling — and not one digit on the summary screen moves while it happens.

   And the rate is a property of the place, not of the walk. Compare one Chansey, from
   slot 10 of the Safari Zone's centre area at 3/256:

        Chansey  base HP 250   →  one defeat is worth 250 HP points
        Zubat    base HP  40   →  one defeat is worth  40 HP points

   Six and a quarter Zubat to one Chansey, in the counter nobody reads. Which floor a
   Trainer walks determines what accumulates, and the summary screen shows neither.
```

## And the interval between refreshes gets *longer* the more has accumulated

This is the part that is genuinely uncomfortable, and it is pure arithmetic. Zubat is in the
**Medium Fast** growth group, whose curve is the plainest in the table: the experience needed for
level *n* is exactly *n*³. Experience gained is the defeated Pokémon's base experience × its level
÷ 7, so a level-8 Zubat (base experience 54) hands over 61 points and a level-10 **Geodude** (base
experience 86) hands over 122.

```
   REAL NUMBERS. Averaged over Mt. Moon 1F's ten slots at their printed levels, one
   encounter is worth about 70 experience and about 51 points of Attack Stat Experience.

   level     exp needed      encounters until    hidden Attack points
   step      for the step    the next refresh    piled up in between
   ───────   ───────────     ────────────────    ────────────────────
   20 → 21        1 261            ~18                  ~930
   50 → 51        7 651           ~109                ~5 600
   99 → 100      29 701           ~424               ~21 800

                 ▲                 ▲                    ▲
                 n³ grows as 3n²    so the gap between   so the amount the screen
                                    look-ins grows too   is wrong by grows with it

   A level-99 Pokémon goes twenty-three times as long between refreshes as a level-20
   one, through no decision by anybody. The engine never chose that interval. The curve did.
```

## The four things that force a refresh, and what each one costs

```
   ┌────────────────────────┬──────────────────┬──────────────┬──────────────────────────┐
   │ what forces a          │ scheduled by     │ costs        │ its limit                │
   │ recalculation          │                  │              │                          │
   ├────────────────────────┼──────────────────┼──────────────┼──────────────────────────┤
   │ gaining a level        │ the n³ curve     │ nothing      │ the interval grows as    │
   │                        │ — nobody         │              │ the square of the level  │
   │ a vitamin: Protein,    │ you              │ ¥9 800 each  │ adds 2 560, and is       │
   │ Iron, Calcium, Carbos, │                  │              │ REFUSED once that stat   │
   │ HP Up                  │                  │              │ already holds 25 600     │
   │ a Rare Candy           │ you              │ ¥4 800       │ refused at the level cap │
   │                        │                  │              │ of 100, and it RESETS    │
   │                        │                  │              │ experience to the bare   │
   │                        │                  │              │ minimum for the new      │
   │                        │                  │              │ level, discarding any    │
   │                        │                  │              │ surplus already banked   │
   │ withdrawing it from a  │ you              │ nothing      │ none. Any time. Any      │
   │ box in Bill's PC       │                  │              │ number of times.         │
   └────────────────────────┴──────────────────┴──────────────┴──────────────────────────┘

   Only the last row is both free and under your control, and it is the one nobody does
   on purpose. Reactive play uses the first row: it waits for a level-up to happen.
```

The vitamin row deserves a note, because it is the row that looks like the answer and is not. Ten
**Protein** is ¥98 000 and takes the Attack counter to exactly 25 600, which is 39% of the
ceiling, and the eleventh is refused outright. The remaining 39 935 points have to come 51 at a
time out of the grass. So the expensive intervention cannot substitute for the cheap deliberate
look — it tops up one counter, by a capped amount, and happens to force a refresh on the way past.

## The register, which is the actual mechanism

The experience routine walks the **party** — six slots — and inside that it only pays Pokémon
whose gain-experience flag is set, which means the ones that were actually sent out. Everything in
storage is outside the loop entirely: twelve boxes of twenty, 240 Pokémon, none of which gains a
point, levels up, or has its stats recalculated while it sits there. Six visible, 240 invisible,
and the only way the 240 become visible is a deliberate decision to open the box.

That is the difference between a service and a template. A Trainer who refreshes whoever happens
to be in the party has refreshed the six that were already in front of them. The register is the
box list, and the only place it is written down is **Bill's PC**.

The **Pokédex** is the other half of the same idea, and it is the half that already works. SEEN
and OWN are separate counters on purpose, so the gap between them is a standing list of things
still open — exactly the structure a recall list needs, kept by the save file rather than by the
Trainer. What the Pokédex has and the boxes do not is a **reason to look**: the counters are
printed on the front screen. Nothing prints how long it has been since box eight was opened.

And a note on what the summary screen *does* carry reliably. The **Original Trainer**'s name and
the **ID No.** are on it and they never change, which makes them the one thing on that screen a
later Trainer can trust without refreshing anything. Identity is permanent and legible; state is
neither.

## The thing a refresh does not do

It changes what is legible, not what is true. The 13 175 points were already there; withdrawing
the Pokémon from a box did not create them and does not act on them. A Trainer who deposits and
withdraws six Pokémon without once opening the summary screen has performed the operation,
produced the record, and learned nothing — and the engine will cheerfully let them, because
`CalcStats` does not care whether anybody reads its output. The test of the look-in is whether
anything would have been done differently had a number come back differently.

Two more honest limits. The visible stats are themselves capped at 999, so beyond a point the
refresh has nothing left to show even though the hidden counters keep climbing. And the levels
printed in a table are a property of the place — Mt. Moon 1F offers Zubat at six different levels,
6 through 11, so the same lap of the same floor contributes a different amount depending on which
slots came up. An interval chosen against an average is not an interval that is right for any
particular walk.

## Where the metaphor stops

A review invites someone who feels well to come and be told about something they cannot feel. That
is a genuinely odd thing to ask of a person, and it is worth not glossing over. The offer is an
offer: attending, and acting on what is found, are decisions for the person, and a service that
treats non-attendance as non-compliance has misunderstood its own position.

The burden is real and is mostly invisible to whoever books the appointment. Time off work,
transport, childcare, the cost where there is one, the blood test the week before, the waiting
room, and the cumulative experience of being a person who is managed. For someone with several
conditions this is not one morning a year; it is a recurring part of life that nobody has added
up. When that burden becomes the reason someone stops coming, it is usually recorded as
disengagement.

And the thing the structure cannot supply. Being given the name of a condition changes how a
person understands their own body, and it does so permanently. Someone who arrives well and
leaves as a patient has had something taken as well as given, even when the exchange is clearly
worth it. Saying so out loud, in the appointment, is not a softening of the message; it is part of
the accuracy of it.

## What a Gym Leader is listening for

Whether the Trainer identifies the *cache* as the thing at issue, rather than listing what is on
the summary screen. Then the interval: that the n³ curve sets it, that it lengthens as the level
rises, and that nobody chose it. Then the three refresh triggers, with the cost and the limit of
each, and why the free one is the one that gets skipped. Then the box list, and why refreshing the
party is not refreshing the register. Then the awkward one: how you would tell a Trainer who
reviewed their boxes from one who deposited and withdrew 240 Pokémon without reading a screen,
given that the save file looks identical either way.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The national guideline for whichever long-term condition is in question, issued by the body that
  governs the reader's practice, for the review interval and the variables it expects
  (**country-dependent**).
* The specification of the reader's own incentive or quality framework for primary care, which is
  what actually determines what a review contains and is recorded for in that system
  (**country-dependent**).
* Any systematic review of the effect of pay-for-performance or indicator-based schemes in primary
  care, in the health-services-research literature, for the direction of effect and for the
  authors' assessment of how much is recording behaviour.
* The reader's own organisation's register, recall and failed-attendance policy, which is the only
  authority on what coverage is locally achievable.
* Any published analysis of coverage by deprivation, ethnicity or disability for the programme in
  question, which is where the gradient appears if it appears at all.

The Pokémon figures are a separate matter and are not covered by the line above. The Stat
Experience mechanism and its 65 535 ceiling, the four events that reach the stat-recalculation
routine with its stat-experience term enabled, the Mt. Moon 1F encounter table with its levels,
the Safari Zone centre area's 30/256 rate and its Chansey in slot 10, the ten slot chances, the
base stats and base experience of Zubat, Geodude, Paras, Clefairy and Chansey, the Medium Fast
curve being exactly *n*³, the experience formula being base experience × level ÷ 7, the vitamin
adding 2 560 and being refused above 25 600, the ¥9 800 vitamin and ¥4 800 Rare Candy prices, the
Rare Candy resetting experience to the minimum for the new level and being refused at level 100,
the 999 stat ceiling, the party of six and the twelve boxes of twenty, the separate Pokédex SEEN
and OWN counters, and the experience routine walking only the party, were all read directly from
the pret decompilation projects, which this environment can reach.

## Scope and safety

This is revision material about how a clinical process is designed, written for someone already
training in or qualified for the field. It is not a clinical reference, not a decision aid, and
not for use in making a decision about any person's care. No review interval, target value or
indicator threshold is reproduced here on purpose: those are local, they are revised, and the
authoritative version is the one issued for the reader's own setting. The Pokémon numbers are
real; they stand in for a mechanism, and no clinical figure should be read out of them. If someone
is unwell right now, the relevant action is to contact local urgent care or the local emergency
number, not to read this.

## Where this stands, October 2026

The sampling argument — that waiting to be consulted is a biased way to look at anything that
produces no symptoms, and that a register plus a clock removes that bias — is settled and is not
expected to move. What moves, and quickly, is the content of review templates, the intervals
themselves, and the incentive frameworks attached to them; several systems are moving from
single-disease annual reviews toward combined reviews for people with more than one condition, and
the evaluation of that shift is still arriving. Remote and asynchronous review is now routine
where it was experimental, and its effect on the access gradient is actively contested. The Red
and Blue numbers are stable because the games are finished. Take intervals, variables and
indicators from current local guidance rather than from here, as of October 2026.
