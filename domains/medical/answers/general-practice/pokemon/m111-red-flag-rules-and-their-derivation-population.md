---
id: "m111"
slug: red-flag-rules-and-their-derivation-population
style: pokemon
category: general-practice
difficulty: advanced
question: "Why does a red-flag rule derived in secondary care behave differently at first contact, and what about such a rule fails to transport?"
tags: [red-flags, derivation-population, spectrum-bias, decision-rules, transportability]
---

# The Repel number that empties Route 116 removes two encounters in five on Victory Road

This specialty already owns the **Repel**. m011 used it, m081 pinned down the quantity it reads,
and m082 separated the encounter *rate* from the encounter *table*. What none of those three did
is take **one** threshold and walk it to a second route. That is the whole of this question,
because a threshold is a number fitted somewhere, and `IsWildLevelAllowedByRepel` does not record
where.

The routine is three lines of comparison. Roll the slot, roll the level from that slot, and
cancel the encounter if the rolled level is below one number. The number is the level of the first
party member with HP remaining that is not an egg — not the lead, which is m081's correction and
is worth repeating because the two filters in this same file disagree about it. So the cut-point
is read off **the user**, never off the route, and nothing in the save file records which route
the user was standing on when they chose their party.

## One threshold, two routes, the arithmetic done

```
   EVERY NUMBER BELOW IS REAL, READ OUT OF THE EMERALD ENCOUNTER DATA AND THE WILD
   ENCOUNTER ROUTINE. Generation III land tables have TWELVE slots and the percentage
   vector is fixed for every land table in the game:
      20  20  10  10  10  10  5  5  4  4  1  1

   ROUTE 116  (table rate 20, so 20 x 16 = 320 against MAX_ENCOUNTER_RATE 2880
               = 11.11% of eligible steps)

     slot   %   species     lv        slot   %   species     lv
     ────  ──   ─────────   ──        ────  ──   ─────────   ──
       1   20   Poochyena    6          7    5   Taillow      7
       2   20   Whismur      6          8    5   Taillow      8
       3   10   Nincada      6          9    4   Poochyena    7
       4   10   Abra         7         10    4   Poochyena    8
       5   10   Nincada      7         11    1   Skitty       7
       6   10   Taillow      6         12    1   Skitty       8

     by rolled level:   lv6  60 %      lv7  30 %      lv8  10 %

   VICTORY ROAD 1F  (table rate 10, so 160/2880 = 5.56% of eligible steps)

     slot   %   species     lv        slot   %   species     lv
     ────  ──   ─────────   ──        ────  ──   ─────────   ──
       1   20   Golbat      40          7    5   Golbat      38
       2   20   Hariyama    40          8    5   Hariyama    38
       3   10   Lairon      40          9    4   Aron        36
       4   10   Loudred     40         10    4   Whismur     36
       5   10   Zubat       36         11    1   Aron        36
       6   10   Makuhita    36         12    1   Whismur     36

     by rolled level:   lv36  30 %     lv38  10 %     lv40  60 %

   NOW RUN ONE THRESHOLD ON BOTH. The rule is the same rule: cancel if the rolled
   level is below T. Only T moves.

                              cancelled on          cancelled on
                              ROUTE 116             VICTORY ROAD 1F
     T = 8   (fitted upstream)     90 %                   0 %
     T = 40  (fitted downstream)  100 %                  40 %

   READ THE DIAGONAL. Fitted downstream, T = 40 is a selective instrument: it cancels
   eight of the twelve slots but only two encounters in five, and leaves the four
   level-40 slots, which are 60 per cent of the table, to come through. Carry that same 40 upstream and Route 116 reads EMPTY.
   Every one of its twelve slots is cancelled, the walk is silent, and nothing in the
   game tells you the difference between a route with nothing in it and a filter that
   is refusing everything.

   And the other diagonal is the inert failure. T = 8 was fitted where it removed nine
   encounters in ten. On Victory Road it removes none, and a Trainer who trusts it
   walks into Hariyama at level 40 believing a filter is running.
```

## Only one species is in both tables, and it is 20 per cent of one and 5 of the other

The threshold is the easy half. The harder half is that a rule keyed on *what* comes out, rather
than on a level, has an even shorter reach. Compare the two casts:

| Route 116 | Victory Road 1F |
| --- | --- |
| **Poochyena**, **Whismur**, **Nincada**, **Abra**, **Taillow**, **Skitty** | **Golbat**, **Hariyama**, **Lairon**, **Loudred**, **Zubat**, **Makuhita**, **Aron**, **Whismur** |

**Whismur** is the only entry in both. On Route 116 it is slot 2 at 20 per cent, at level 6. On
Victory Road 1F it is slots 10 and 12 — four per cent and one per cent, five per cent together —
at level 36. The one shared species is a fifth of the upstream table and a twentieth of the
downstream one, thirty levels apart, and the thing a Trainer learns to recognise about a level-36
**Whismur** is not what a level-6 one looks like.

So a rule of the form *if you see a Lairon, act* is 10 per cent of Victory Road and literally
unfireable on Route 116, where **Lairon** is not in the table at all. A rule of the form *if you
see a Poochyena, act* is 28 per cent upstream and unfireable downstream. The rule is not weaker
in the other place. It has no entry to match.

## The filter that reads slot 0, and the dead zone nobody wrote down

The Repel is not the only threshold in `src/wild_encounter.c`. `IsAbilityAllowingEncounter` is a
second one, and it is instructive because it fails in three different ways at once:

* **It reads a different party member.** It takes `gPlayerParty[0]` and nothing else, where the
  Repel walks the party for the first conscious one. Two filters, one file, two definitions of
  whose level sets the cut-point.
* **Its cut-point is relative, not absolute.** With **Keen Eye** or **Intimidate** in slot 0 it
  cancels encounters at or below the lead's level minus five. On Route 116 with a level-8 lead
  that is level 3 and below, and the lowest entry on Route 116 is level 6, so the ability fires on
  nothing. On Victory Road with a level-40 lead it is level 35 and below, and the lowest entry
  there is 36, so it fires on nothing there either. The same ability, running in both places,
  doing nothing in both — and then take that level-40 lead back to Route 116 and it is suddenly
  cancelling half of everything.
* **It has a region where it cannot fire at all.** The guard is `playerMonLevel > 5`, so with a
  lead at level 5 or below the whole check is unreachable code. A Trainer on Route 101, whose
  table is levels 2 and 3, can hold **Keen Eye** in slot 0 for the entire route and have it never
  once be consulted.

And the coin flip: when the level condition does pass, the cancellation is `!(Random() % 2)`. Half
the eligible encounters get through anyway. A filter that is half a filter is not a filter you can
reason backwards from after a single walk.

## What transports: the vector, and nothing else in the file

This is the useful separation and it is visible in the data layout. The file
`wild_encounters.json` declares the percentage vector **once**, at the top, for every land table
in Hoenn.
Underneath it, per map, it declares the species and the level ranges. So:

* **The twelve-slot structure transports**, perfectly and everywhere. Slot 1 is 20 per cent of
  Route 101, of Route 116, of Granite Cave and of Victory Road 1F. This is m011's portable term.
* **The species and levels do not transport at all**, and they are the entire content. This is
  m011's local term, and it is where the thing you are looking for lives.
* **The table rate is a third thing**, and m082 already separated it: 20 on Route 116 against 10
  on Victory Road 1F is how often you are asked the question, not what the answer is. A
  transported rule gets the *table* wrong. It does not get the rate wrong, because it never
  touched the rate.

**And here the analogy has a hard edge, stated where the device is used rather than at the end.**
The Repel reads its number off the Trainer's own party, and a clinical rule's cut-point is not
read off the clinician — it is read off the cohort the rule was fitted on, and then the clinician
inherits it. The mechanism the two share is that the number comes from somewhere other than the
place it is applied, and that the place it came from is not recorded anywhere the user can see.
Beyond that the mapping stops, and the difference is worth holding on to, because *whose level is
it* is exactly the question a Trainer can answer and a reader of a published rule frequently
cannot.

## Where the metaphor stops

The two failure modes above both land on people, and neither of them looks like a mistake at the
time. A rule that flags nearly everyone sends well people into investigation they did not need,
with procedures that carry their own complications, waiting, time away from work and family, and a
lasting shift in how somebody understands their own body. A rule that is inert does the quieter
harm: somebody is told the rule is negative, hears *this has been checked*, and the checking was
done by an instrument that could not have found their illness at the stage it had reached.

Only one of those two comes back to the person who did it, which is m084's asymmetry, and it
pushes professional habit steadily toward more rules applied more loosely. Nothing about caring
more corrects an asymmetry in what is observable.

And the part that is not about arithmetic at all. A clinician applying a published rule to the
population in front of them is doing exactly what they were trained to do. The defect sits in the
distance between where evidence is produced — wherever the confirmed outcomes accumulate — and
where it is used, and that distance is a property of how medical knowledge gets made. Treating a
rule that failed as a system finding rather than as somebody's carelessness is both kinder and
more likely to fix it.

## What a Gym Leader is listening for

Whether the Trainer runs one threshold on two tables rather than asserting that thresholds are
local. Then the diagonal: 90 against 0, and 100 against 40, with the direction of each failure
named. Then the species comparison, and the observation that **Whismur** is the only shared entry
and arrives at 20 per cent against 5 per cent and thirty levels apart. Then the structural
separation — the vector at the top of the file against the species underneath it — and whether
they can say which of the two m011 called portable. Then `IsAbilityAllowingEncounter`, with the
dead zone below level 6 and the coin flip, offered as a second threshold rather than a restatement
of the first. Then the hard one: how they would find out what a threshold does on a route they
have not walked, given that the cancelled encounter and the empty route look identical.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The derivation and validation publications for whichever specific rule is in question, read
  for their setting, recruitment and reference standard before their headline figures.
* Any current reporting-standards statement for diagnostic accuracy studies, and any current one
  for multivariable prediction model studies, each issued by the relevant methodology group, for
  what must be disclosed about setting and spectrum and for what external validation means.
* A standard textbook of clinical epidemiology or clinical prediction modelling, for spectrum
  effects and for why transported models lose performance.
* The suspected-cancer or urgent-referral criteria issued by the body governing the reader's own
  practice, which is where the locally authoritative lists live (**country-dependent**).

The Pokémon figures are a separate matter and are not covered by the line above. The
Generation III twelve-slot land percentage vector of 20 20 10 10 10 10 5 5 4 4 1 1 declared once
in `src/data/wild_encounters.json`; the Route 116 and Victory Road 1F land tables with their
species, level values and table rates of 20 and 10; the rate test multiplying the table rate by
16 and comparing against a maximum encounter rate of 2 880; `IsWildLevelAllowedByRepel` walking
the party and stopping at the first member with HP that is not an egg, cancelling any rolled level
below that member's; and `IsAbilityAllowingEncounter` reading `gPlayerParty[0]` only, requiring
the lead to be above level 5, cancelling only at or below the lead's level minus five, and doing
so on a one-in-two roll with **Keen Eye** or **Intimidate**, were all read directly from the pret
decompilation projects, which this environment can reach. The levels quoted are Emerald's; other
third-generation titles differ by table.

## Scope and safety

This is revision material about what happens to a decision rule when it is moved between
populations, written for someone already training in or qualified for the field. It is not a
clinical reference, not a decision aid, and nothing here should inform whether any individual is
referred or investigated — that belongs with the clinician who has assessed them and with current
local criteria. No clinical rule is named, reproduced or paraphrased here, and no feature,
cut-point, sensitivity or timescale appears, on purpose. The encounter percentages, levels and
thresholds above are real and stand in for a mechanism; not one of them is a clinical quantity
and no clinical figure should be read out of them. If someone is unwell right now, the relevant
action is to contact local urgent care or the local emergency number, not to read this.

## Where this stands, October 2026

The methodological claims — that transport depends on spectrum as well as prevalence, that
external validation is a separate step, and that a rule-in instrument is not a rule-out
instrument — are settled and will not move. The stock of rules will: which exist, which have been
validated at first contact, which have been withdrawn, and which have been replaced by models
built on laboratory values rather than clinical features. The number validated specifically in
first-contact populations has grown over the last decade and is still small next to the number in
use. The Emerald tables are stable because the games are finished. Check any particular rule
against the current literature and against local guidance rather than against this answer, as of
October 2026.
