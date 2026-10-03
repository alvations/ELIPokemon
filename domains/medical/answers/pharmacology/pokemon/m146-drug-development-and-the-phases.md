---
id: "m146"
slug: drug-development-and-the-phases
style: pokemon
category: pharmacology
difficulty: advanced
question: "Why does each phase of drug development answer a question the previous phase could not, and what does a licence at the end of it actually certify?"
tags: [drug-development, clinical-trials, endpoints, licensing, regulation]
---

# The Battle Frontier is seven buildings because seven questions do not fit in one building.

A Gym is a single test repeated eight times with the type changed. The Battle Frontier is not
that. `include/constants/battle_frontier.h` defines seven facilities and
`NUM_FRONTIER_FACILITIES` is 7, and the reason there are seven is that each one **removes a
different thing you were relying on**. Beating Anabel in the Battle Tower tells you nothing about
whether you can beat Noland in the Battle Factory, because the Factory takes your own Pokémon away
from you before the first turn.

That is the entire structure of drug development, and the cartridge is more explicit about it than
most textbooks.

In this answer the Pokémon is the **candidate agent** and the Trainer is the development
programme. Nothing here stands in for a patient; the facilities are study designs.

| Facility | What it takes away | The question only it can answer |
| --- | --- | --- |
| **Battle Tower** | nothing — the standard format at a fixed level | does this beat a like-for-like comparator under controlled conditions |
| **Battle Factory** | your own team; you are handed rentals you did not raise | does the approach work in bodies you did not select |
| **Battle Dome** | the chance to play most of the bracket | what can be concluded when the other comparisons are computed rather than run |
| **Battle Arena** | the whole battle; it is judged after three turns | what a pre-declared composite endpoint measures |
| **Battle Palace** | your choice of move | what happens when the agent, not the operator, decides |
| **Battle Pike** | the ability to choose what you meet at all | what unselected exposure looks like |
| **Battle Pyramid** | your bag; you start empty and use what you find | what happens over a long run with whatever supply exists |

Where the mapping is loose, and it is worth saying here rather than at the end: the Frontier's
seven are **parallel** — you can walk into any of them — while the phases are **sequential**, each
needing a number the last one produced. The Frontier is the right device for *why there are
several designs and what each buys*, and the wrong device for *why they must be done in order*.
The escalation ladder below is the part that carries the order.

## The ladder: eight rungs, overlapping, and the last two identical

`sFixedIVTable` in `src/battle_factory.c` is the dose-escalation design written out as data. It
sets the Individual Values given to facility Pokémon by challenge number, and
`GetFactoryMonFixedIV(challengeNum, isLastBattle)` picks the low or the high column.

```
   sFixedIVTable[][2]        low   high
   ─────────────────────────────────────
   challenge 1               3     6
   challenge 2               6     9        ← the windows OVERLAP by design:
   challenge 3               9     12         rung n's ceiling is rung n+1's floor
   challenge 4              12     15
   challenge 5              15     18
   challenge 6              21     31       ← and then the step widens
   challenge 7              31     31       ┐ the ceiling. MAX_PER_STAT_IVS is 31,
   challenge 8              31     31       ┘ so two rungs are the same rung

   and in the same file, line for line with it:

   GetFactoryMonFixedIV(challengeNum, isLastBattle)
       useHigherIV = isLastBattle         ← the LAST opponent of a round is the
                                            tougher column. The hardest test in a
                                            round is placed at the end of it.
```

Three features of a real escalation design, all of them in nine lines of a header: the rungs
ascend, **adjacent rungs overlap** rather than jumping, and the top of the ladder is a **ceiling
that repeats** — two challenges at `{31, 31}` because there is nothing above 31. An escalation
that has reached its ceiling stops being an escalation and becomes a repeat, which is exactly what
happens when a dose-finding study has found the dose.

And there is a documented out-of-bounds read at the top of it: the comment in `battle_factory.c`
says that for `challengeNum == 8` the index runs off the end of `sFixedIVTable` and lands on a
number above 31, which the generator then interprets as "random Individual Values". A ladder read
one rung past its last rung does not fail loudly; it returns noise that looks like a value. Keep
that one.

## Eligibility: the window widens, and it is written down

`sInitialRentalMonRanges` decides which of the facility's roster you may be offered, by round.

```
   Level 50 mode, the rental draft, by challenge
   ──────────────────────────────────────────────────────────────────
   challenge 1   FRONTIER_MON_GRIMER     .. FRONTIER_MON_FURRET_1      (110-199)
   challenge 2   FRONTIER_MON_DELCATTY_1 .. FRONTIER_MON_CLOYSTER_1    (162-266)
   challenge 3   FRONTIER_MON_DELCATTY_2 .. FRONTIER_MON_CLOYSTER_2    (267-371)
   challenge 4   FRONTIER_MON_DUGTRIO_1  .. FRONTIER_MON_SLAKING_1     (372-467)
   ...
   challenge 8   FRONTIER_MON_DUGTRIO_1  .. FRONTIER_MONS_HIGH_TIER    (372-849)

   Open Level mode, final rows
                 FRONTIER_MON_DUGTRIO_1  .. NUM_FRONTIER_MONS - 1      (372-881)

   and the gate between them, in GenerateOpponentMons:
       if (lvlMode == FRONTIER_LVL_50 && monId > FRONTIER_MONS_HIGH_TIER)
           continue;                      ← the high tier is UNREACHABLE at
                                            level 50. Not rare. Absent.
```

Say the index ranges as names and the shape is obvious. Round one of the Level 50 division offers
the stretch of the roster that begins at **Grimer** and ends at **Furret**. Round two moves to
**Delcatty** through **Cloyster**. From round four it is **Dugtrio** through **Slaking**, and by
round eight the top of the range is the high tier. A **Grimer** in the first round and a
**Slaking** in the fourth are not the same test, and the thing that changed is not the engine —
it is two integers in a table.

A programme's eligible population widens as it proceeds, the widening is written as index ranges
rather than derived from anything, and one whole band of the roster is **excluded by rule from the
controlled format** and only reachable in the open one. That is the eligibility-criteria argument
and the restricted-population argument in one table. `m085` makes the related point about the
difference between a rare slot and a rare species; here the point is that an unreachable band is
not a thin band — a **Slaking** you cannot be offered at level 50 is not a rare **Slaking**.

## The controlled format, and the one where the control is removed

```
   FRONTIER_MAX_LEVEL_50     50        and in AppendIfValid, frontier_util.c:
   FRONTIER_MIN_LEVEL_OPEN   60            if (lvlMode == FRONTIER_LVL_50
   FRONTIER_MAX_LEVEL_OPEN   MAX_LEVEL          && monLevel > FRONTIER_MAX_LEVEL_50)
                             (= 100)              return;
```

In the Level 50 division every entrant is scaled to the same level, so a win cannot be explained
by having trained more — the one obvious confounder is removed by construction, not adjusted for
afterwards. Open Level removes the scaling and the floor jumps to 60, so the division is no longer
like-for-like and a result in it means something different. Two divisions, one engine, and the
difference between them is the difference between a randomised comparison and an observation.
`m050` is where the badge boost makes the related point that a relative multiplier widens an
absolute gap while improving everybody.

## The Battle Arena: a composite endpoint, declared in advance

This is the best mechanic in the games for the endpoint question, because the weights are a table
you can read.

```
   battle_util.c, the trigger
   ──────────────────────────────────────────────────────────────────────────────
       if ((gBattleTypeFlags & BATTLE_TYPE_ARENA)
        && gBattleStruct->arenaTurnCounter == 2
        && gBattleMons[0].hp != 0 && gBattleMons[1].hp != 0)
               -> BattleScript_ArenaDoJudgment

   The counter is set to 0xFF on switch-in and incremented each turn, so it reads 0
   on the first turn and judgment lands at the end of the third -- a FIXED duration,
   fixed before the battle starts. And the second condition is the decision rule's
   escape clause: if either side has already fallen there is nothing to judge.

   battle_arena.c, the three categories
   ──────────────────────────────────────────────────────────────────────────────
   ARENA_CATEGORY_MIND    sMindRatings[gCurrentMove], summed
   ARENA_CATEGORY_SKILL   effectiveness and outcome of what landed
   ARENA_CATEGORY_BODY    (hp * 100) / hpAtStart          ← the only OUTCOME term

   each category: winner +2, tie +1, loser nothing.
```

The comment above `sMindRatings` in `battle_arena.c` states the weighting in full: every move with
power gives 1 point, **except** Counter, Mirror Coat and Bide, which give 0, and **Fake Out**,
which gives −1; every move without power gives 0, **except** Protect, Detect and Endure, which
give −1.

Read that again as an endpoint. Two of the three categories score *how you played*, and only the
body score measures *what happened*. Work it through with real moves. A **Blissey** that uses
**Protect**, **Protect** and **Soft-Boiled** scores −1, −1 and 0 on the mind category and nothing
on skill, and finishes the third turn on a full bar. A **Machamp** that uses **Cross Chop** three
times into something that resists it scores +1, +1, +1 on mind and −1, −1, −1 on skill, and
finishes worse off. The **Blissey** wins the body category outright and still loses the composite
two categories to one.
Nothing is broken: the endpoint is measuring what its designers decided to weigh, and they wrote
the weights down in advance, which is the honest version of the thing. The failure mode is reading
the total and not the components — and the components are three separate sprites on the screen,
which is more transparency than most composite endpoints offer.

## The Battle Dome: the comparison that is computed rather than played

`DOME_TOURNAMENT_TRAINERS_COUNT` is 16 and `DOME_ROUNDS_COUNT` is 4, so a Dome challenge is 15
matches of which you play 4. The other eleven are settled by `DecideRoundWinners` in
`src/battle_dome.c`, and the formula is worth having in front of you.

```
   for each still-standing NPC pair:

     points = Σ over (my 3 mons × my 4 move slots × their 3 mons)
                  GetTypeEffectivenessPoints(move, theirSpecies, AI_VS_AI)
            + Σ over my 3 mons  (baseHP + baseAttack + baseDefense
                                 + baseSpeed + baseSpAttack + baseSpDefense) / 10
            + (Random() & 0x1F)        ← a 0-31 noise term
            + tournamentId             ← a SYSTEMATIC bias toward the higher id

     if either side is TRAINER_FRONTIER_BRAIN: that side wins, unconditionally,
     before the formula is reached at all.

   and, from the source comment:
     "BUG: points1 and points2 are not cleared at the beginning of the loop
      resulting in not fair results."
```

Everything about an indirect comparison is in those eight lines. The matches you did not run are
resolved by a model built from the data you happen to hold. The model has a noise term. It has a
bias term that favours one side for a reason that is not about the contest. One competitor cannot
lose. And the whole thing carries a defect that produces plausible output, which is why nobody
playing it notices.

Two further details sharpen it. `GetTypeEffectivenessPoints` reads
`gSpeciesInfo[targetSpecies].abilities[0]` only — so a species whose relevant ability sits in the
second slot is scored as if it did not have it, which is `m077`'s one-bit locus coming back as a
measurement error. And the Levitate branch in that function is missing its `return`, so a move
that would have no effect at all scores 0 points instead of the 8 the mode intends. A zero and an
absence are different things, as `m007` argues, and this function confuses them.

The Dome also hands you the opponent's card before your own match —
`BATTLE_DOME_FUNC_SHOW_OPPONENT_INFO`, their species, moves and summary — which is the one thing a
bracket can offer that a formula cannot: information before you commit. That is what a phase II
result is for.

## The Battle Pike: unselected exposure

```
   NUM_PIKE_ROOMS        14
   NUM_PIKE_ROOM_TYPES    9

   PIKE_ROOM_SINGLE_BATTLE   PIKE_ROOM_HEAL_FULL   PIKE_ROOM_NPC
   PIKE_ROOM_STATUS          PIKE_ROOM_HEAL_PART   PIKE_ROOM_WILD_MONS
   PIKE_ROOM_HARD_BATTLE     PIKE_ROOM_DOUBLE_BATTLE   PIKE_ROOM_BRAIN

   three doors -- PIKE_ROOM_LEFT, PIKE_ROOM_CENTER, PIKE_ROOM_RIGHT -- and the
   only thing you get before choosing is a HINT:
   PIKE_HINT_NOSTALGIA, PIKE_HINT_WHISPERING, PIKE_HINT_POKEMON,
   PIKE_HINT_PEOPLE, PIKE_HINT_BRAIN.
```

Fourteen rooms and only three of the nine types are the battle you came for. One room applies a
status through a Kirlia or a Dusclops — `PIKE_STATUS_FREEZE`, `PIKE_STATUS_BURN`,
`PIKE_STATUS_TOXIC`, `PIKE_STATUS_PARALYSIS`, `PIKE_STATUS_SLEEP` — and nothing told you it was
coming. You cannot restrict the Pike to the comparison you wanted to make, and the hint is a
category, not a fact. That is post-licensing use: enormous, uncontrolled, and the only place some
things are ever seen. The Pike's reward for that is the largest streak requirement in the
building, which is the next section.

The Battle Pyramid adds the supply half. Its bag is emptied on entry — every slot set to no item —
so you walk in with nothing and use what is on the floor, and what is on the floor is a
ten-entry-per-round table with the cumulative distribution `{30, 40, 50, 60, 70, 80, 85, 90, 95,
100}` behind it. In the first round that table is a **Hyper Potion**, a **Fluffy Tail**, a **Cheri
Berry**, an **Ether**, a **Lum Berry**, **Bright Powder** and a **Shell Bell**; in the second it
is a **Hyper Potion**, a **Dire Hit**, a **Pecha Berry**, an **Ether**, a **Leppa Berry**,
**Leftovers**, a **Choice Band** and a **Full Restore**. The round decides which. You are running
a long course on whatever supply happens to exist, from a distribution somebody fixed in advance,
and the **Leftovers** that would carry you are in the second round's column and not the first's.

## The threshold is a number somebody wrote

`sFrontierBrainStreakAppearances` in `src/frontier_util.c` holds, per facility, the streak at
which the Silver Symbol becomes available, the streak for the Gold, and the interval after that.

```
   facility        silver   gold   then every
   ──────────────────────────────────────────────
   Battle Tower       35      70       35
   Battle Dome         4       9        5
   Battle Palace      21      42       21
   Battle Arena       28      56       28
   Battle Factory     21      42       21
   Battle Pike        28     140       56
   Battle Pyramid     21      70       35
```

Each of those rows has a person at the end of it, and naming them is the quickest way to see that
the thresholds are judgements rather than measurements: **Anabel** at the Tower asks for 35,
**Greta** at the Arena for 28, **Spenser** at the Palace and **Noland** at the Factory for 21
each, and the Pike's and the Pyramid's Brains for 28 and 21 — with the Pike's gold at 140, four
times the Arena's. **Anabel**'s Silver Symbol team opens with an **Alakazam** holding **Bright
Powder**, and whether you get to meet it is decided by an integer in a table rather than by
anything about your own team.

Seven facilities, fourteen symbols, and **not one of those numbers is derived from anything**. The
Dome asks for 4 because a Dome round is a 16-trainer bracket and the Tower asks for 35 because a
Tower round is 7 battles; the Pike asks for 140 for the gold, four times what the Arena asks,
because the Pike is the facility where the least is under your control. The amount of evidence
demanded is a judgement about the design, made in advance, written as an integer, and different
for every facility. `FRONTIER_BRAIN_SILVER` and `FRONTIER_BRAIN_GOLD` are two separate grants at
two separate thresholds — and `FRONTIER_BRAIN_STREAK` and `FRONTIER_BRAIN_STREAK_LONG` exist
afterwards, because the obligation does not end when the second symbol is handed over.

And a symbol is facility-specific. Fourteen of them, each naming one facility, and
`GetFacilitySymbolCount` counts them one building at a time. There is no symbol for "the Battle
Frontier". `m045`'s formulary point and `m008`'s substitution point both land here: a grant for
one format is not a grant for another, and the only thing that makes it feel like one is that they
are all in the same town.

## Where the metaphor stops

Everything above is about study design, and three things about clinical trials are about people.
They are said here without analogy, because no mechanic in any Pokémon game should carry them.

**A trial is not treatment.** Participants very commonly understand a randomised trial as care
chosen individually for their benefit — this is well described and it is called therapeutic
misconception. It is invited by the setting, the attention and the language, and consent that does
not address it is not informed. The honest framing is that nobody yet knows which arm is better,
which is the whole reason the study is being run.

**Randomising is only defensible while the answer is genuinely unknown.** That condition is called
equipoise, and it can end part-way through a trial. This is why data monitoring committees
independent of the sponsor exist, and why trials are stopped early both for harm and for benefit.
Nothing in the Frontier models an obligation to stop a contest because you have learned enough to
know it is unfair to continue it, and that absence is worth noticing rather than papering over.

**Who takes part decides who the evidence is about.** Women, older people with several conditions,
people with impaired kidney or liver function, and ethnic-minority and lower-income populations
are all under-represented in trials, consistently and measurably. The consequence is that the
evidence is thinnest for the people whose care is hardest, and the remedy is representative
recruitment rather than confident extrapolation. The Frontier's eligibility ranges are a sharp
device for *how* a population gets narrowed; they say nothing about the fact that in medicine the
narrowing falls on particular groups of actual people, and repeatedly on the same ones.

One more, about the record rather than the method: trials with unwelcome results have been less
likely, and slower, to be published. Registries and results-reporting rules exist to make that
visible, compliance is incomplete, and anyone reading only the published literature is reading a
biased sample.

Nothing in this pair indicates what anyone should take, start or stop. A question about whether to
join a trial belongs with the treating team and the study's own information.

## What a Gym Leader is listening for

* Name the thing each of the seven facilities takes away, and the question that removal makes
  askable.
* `sFixedIVTable` — why do adjacent rungs overlap, and why are the last two the same?
* What happens when `GetFactoryMonFixedIV` is called one rung past the end of its table, and why
  is that the dangerous kind of failure?
* Level 50 against Open Level. Which confounder does the scaling remove, and what is lost with it?
* In the Arena, two of three categories score the play and one scores the outcome. Which one, and
  what is the exam point?
* Write out `DecideRoundWinners`' formula and name the noise term, the bias term and the
  competitor that cannot lose.
* Why does the Battle Pike demand 140 for a Gold Symbol when the Battle Dome demands 9?
* Why is there no symbol for the Battle Frontier?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer, and to its technical twin:

* **Your national medicines regulator's guidance on clinical trial and marketing authorisation**,
  for what is required where you work and for the conditional and accelerated routes. This differs
  between jurisdictions and decides most of what the serious half says about licensing.
* **The international council for harmonisation's guideline series on good clinical practice and
  on statistical principles for clinical trials**, which is where the terms used above are
  defined, including the endpoint and non-inferiority vocabulary.
* **The world medical association's declaration on ethical principles for medical research
  involving human subjects**, together with your national research ethics framework, for equipoise
  and consent.
* **The reporting guidance for randomised trials and its extensions**, as the quickest way to see
  what a given trial report has left out.
* **A current clinical trials or clinical pharmacology textbook chapter**, for escalation designs,
  surrogate and composite endpoints, and intention-to-treat against per-protocol analysis.
* **The primary literature and the trial registries**, for any figure about how often surrogates
  mislead or how large the publication gap is. Neither half of this pair states such a figure.

The Pokémon figures are a different matter and were read directly from the public decompilation of
the Game Boy Advance games rather than recalled: `NUM_FRONTIER_FACILITIES` and the seven facility
constants, `FRONTIER_STAGES_PER_CHALLENGE` of 7, `FRONTIER_MAX_LEVEL_50`,
`FRONTIER_MIN_LEVEL_OPEN` of 60 and `FRONTIER_MAX_LEVEL_OPEN`; `sFixedIVTable` and
`GetFactoryMonFixedIV` with its `isLastBattle` column and its documented out-of-bounds read at
`challengeNum == 8`; `sInitialRentalMonRanges` with the index ranges quoted from the source
comments, and the `FRONTIER_MONS_HIGH_TIER` exclusion at level 50; `AppendIfValid`'s level check
in `src/frontier_util.c`; the Arena trigger in `src/battle_util.c` with `arenaTurnCounter == 2`
and the both-still-standing condition, `arenaTurnCounter` initialised to 0xFF in
`src/battle_main.c`, and the three `ARENA_CATEGORY_*` constants with `(hp * 100) / hpAtStart` for
the body score and the +2/+1 scoring in `ShowJudgmentSprite`; the `sMindRatings` weighting quoted
from the table's own source comment; `DOME_ROUNDS_COUNT` of 4 with sixteen tournament trainers,
`DecideRoundWinners`' formula including `(Random() & 0x1F)`, the `tournamentId` term, the
unconditional Frontier Brain branch and the "BUG: points1 and points2 are not cleared" comment,
and `GetTypeEffectivenessPoints` reading `abilities[0]` with the missing `return` in its Levitate
branch; `NUM_PIKE_ROOMS` of 14 with the nine room types, three doors and five hint constants and
the `PIKE_STATUS_*` set; `InitPyramidBag` writing `ITEM_NONE`, `sPickupItemsLvl50` and
`sPickupPercentages`; and `sFrontierBrainStreakAppearances` with the seven rows quoted exactly;
the Battle Pyramid's round-one and round-two pickup rows from `sPickupItemsLvl50`; the
`FRONTIER_MON_*` endpoint names of each rental range, read from the source comments beside
`sInitialRentalMonRanges`; and the Battle Tower Brain's Silver Symbol lead entry in
`sFrontierBrainsMons`, an Alakazam holding Bright Powder with a fixed Individual Value of 24. For
the Arena worked example, Protect's and Soft-Boiled's zero power and Cross Chop's power 100 and
accuracy 80 are from `src/data/battle_moves.h`; Blissey learns Soft-Boiled at level 10 and Machamp
learns Cross Chop at level 46 in `src/data/pokemon/level_up_learnsets.h`, and Blissey's Protect
compatibility is `TRUE` in `src/data/pokemon/tmhm_learnsets.h`, so the example's moveset is legal.
The Frontier Brain name-to-facility pairing is from the object-event table in the same file. The
arithmetic in the blocks above is recomputed from those figures.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in this pair are the Pokémon ones.** Neither half
gives participant numbers, escalation increments, non-inferiority margins or doses, deliberately:
those belong to individual protocols and to regulatory guidance, and an invented one would be a
more serious defect than an invented game mechanic. Nothing here indicates whether anyone should
join a trial, or take, start or stop any medicine. The regulatory structure described is the
common shape across major jurisdictions; the detail differs in each and yours is the authority.

## Where this stands, October 2026

The design logic is mechanism and does not date, and the game mechanics quoted are fixed in
released software — every figure here is pinned to the Game Boy Advance games, where Individual
Values run 0 to 31 and the Battle Frontier has seven facilities, and later generations changed
both the facility set and the Individual Value handling. The clinical half dates faster. **Which
evidence routes a regulator offers**, and what obligations attach, has changed repeatedly and
differs by jurisdiction. **Trial design is moving**: adaptive and platform designs deliberately
blur the phase boundaries, master protocols test several agents against one control, and the
legitimate use of real-world evidence in regulatory submissions is actively contested.
**Results-reporting rules** are being tightened and enforced unevenly. Check the current guidance
from your national regulator rather than this answer.
