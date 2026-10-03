---
id: "m114"
slug: the-account-of-a-worried-adult
style: pokemon
category: general-practice
difficulty: advanced
question: "When an unwell child is brought by a worried parent, what is being assessed in the adult's account, and why is a report of change from baseline information the encounter cannot supply?"
tags: [paediatrics, history-taking, third-party-account, baseline, safety-netting]
---

# Nothing stores yesterday's encounter table, so only a resident can say today is different

**No Pokémon stands in for a child in this answer, and nothing here is a creature whose health is
in question.** The subject throughout is a **route** — what is normally in its grass, how often,
at what levels — and the question is how a Trainer who has never walked it finds out that today is
not like other days. The reporter is a resident. The thing reported is the route. That mapping is
available and the obvious one is not, so this answer uses it and says so.

The specialty's vocabulary is filters and tables. m081 took the **Repel** threshold and m082
separated the encounter rate from the encounter table; m084 used the **Pokédex** flags for a
record that outlives what it recorded. This question needs a fourth object from the same family:
the one thing in the cartridge that encodes *this place is behaving unusually today*, which is the
**mass outbreak**, and it arrives only as a report.

## What the standing record holds, and what it cannot hold

```
   READ OUT OF src/pokedex_area_screen.c, src/wild_encounter.c AND src/tv.c.

   THE POKEDEX AREA SCREEN is the standing record of where a species occurs. The
   function that drives it is:

       static bool8 MapHasSpecies(const struct WildPokemonHeader *info, u16 species)

   A BOOL. It walks the land list, the water list, the rock-smash list and the
   fishing list, and returns TRUE on the first match. So the record can answer

       "does Seedot occur on Route 102?"                      ... yes

   and cannot answer, because the return type has no room for it,

       "in which slot?"          "at what percentage?"       "at what level?"
       "how often per step?"     "and is today different?"

   THREE FURTHER PROPERTIES OF THAT RECORD, ALL IN THE SOURCE

     - one species is excluded by hand:  sSpeciesHiddenFromAreaScreen = { WYNAUT }
     - the fishing search passes the LAND slot count instead of the fishing one, so
       it reads past the end of the fishing array. The source says so in a comment
     - and the SEEN bit behind it never clears. m084 established that: there is no
       case in GetSetPokedexFlag that clears a bit

   AND THE THING THAT IS NOT STORED ANYWHERE AT ALL

     yesterday's table. There is no previous-state copy of any encounter table in
     the save file, so no routine can compute a difference. A Trainer arriving on a
     route can read what is normally there and cannot, by any means the engine
     provides, discover that it is not behaving normally.
```

That is the whole of the baseline problem in one sentence of C. The standing record is a yes/no
per map. The comparison a Trainer actually wants is a difference between today and normal, and the
engine stores exactly one of the two terms.

Two of those three further properties are worth a moment each. **Wynaut** is the one species the
Area screen refuses to show, by a hand-written one-entry exclusion list — a record that is
complete except where somebody decided it should not be. And the fishing overrun means the record
can report presence on a map from array entries that are not fishing entries at all. A standing
record is not neutral and it is not error-free; it was written by somebody, for a purpose, with
the defects of the person who wrote it.

## The report carries what the table cannot

The mass outbreak is announced, by somebody, over the air. What `StartMassOutbreak` copies out of
that report and into the save block is strikingly more than the encounter table ever holds:

| From the standing table | From the report |
| --- | --- |
| species, min level, max level, and the slot's fixed percentage | species, **one** level, a **location**, a **probability**, and **four named moves** |

Four moves. The twelve-slot table carries no move data whatsoever — a wild Pokémon's moves are
generated from its level — and the report carries them explicitly, because
`SetUpMassOutbreakEncounter` writes `outbreakPokemonMoves[0..3]` into the encounter slot by slot.
An account from somebody who was there contains categories of detail the standing record has no
field for.

And the hand-written list is worth reading, because five reports is the whole supply:

```
   sPokeOutbreakSpeciesList[] — five entries, written out by hand

     Seedot   lv 3   Route 102   Bide, Harden, Leech Seed
     Nuzleaf  lv15   Route 114   Harden, Growth, Nature Power, Leech Seed
     Seedot   lv13   Route 117   Harden, Growth, Nature Power, Leech Seed
     Seedot   lv25   Route 120   Giga Drain, Frustration, Solar Beam, Leech Seed
     Skitty   lv 8   Route 116   Growl, Tackle, Tail Whip, Attract

   NOTE THE FIRST ENTRY. Four slots, three moves written. The fourth is left as
   MOVE_NONE, and nothing anywhere flags the difference. A hand-written account is
   not uniform in its detail, and the gaps are not marked as gaps.
```

## The report sits between the rate test and the table, and changes neither

This is the structural point and it is exact. In `StandardWildEncounter`, on a land tile, the
order is:

```
   1   is this a land encounter metatile
   2   if you have just stepped onto a different metatile type:
          AllowWildCheckOnNewMetatile()  — a 40 PER CENT CHANCE OF SKIPPING THE
          WHOLE CHECK. Random() % 100 >= 60 returns FALSE and nothing is rolled
   3   WildEncounterCheck(encounterRate)  — the nine levers of m082, x16, capped
       at MAX_ENCOUNTER_RATE 2880. How often you are asked
   4   TryStartRoamerEncounter()
   5   DoMassOutbreakEncounterTest()      — THE REPORT
          requires mapNum AND mapGroup to match the reported location exactly,
          then Random() % 100 < outbreakPokemonProbability, which the TV show
          sets to 50
       and if it passes:
          SetUpMassOutbreakEncounter(WILD_CHECK_REPEL | WILD_CHECK_KEEN_EYE)
          — BOTH FILTER BITS STILL SET
   6   otherwise the ordinary twelve-slot table, also with both filter bits
```

Read what that ordering means. The report does **not** touch the rate: how often you are asked is
unchanged. It does **not** edit the table: the twelve slots are exactly what they were. What it
does is get consulted first, on the right map only, half the time — and then still run through
both filters, so a Repel cancels a reported outbreak exactly as it cancels anything else.

A report is a prior that is consulted before the table and does not replace it, and the filters
you were already running are not switched off by having been told something. That is the whole of
"the concern raises the probability and the assessment still happens", written as a branch order
in somebody's encounter routine.

Step 2 deserves its own note. Two times in five, the first step onto new ground is not checked at
all. The engine itself declines to answer on a single first look, and a Trainer who concludes
anything from one step has read a sample the code deliberately threw away.

## It is about one place, it has a date, and it expires

Three more properties, each of which has an obvious counterpart in a real account:

* **It is about one map.** `DoMassOutbreakEncounterTest` compares both `mapNum` and `mapGroup`
  against the reported location. One route off and the report does nothing whatever. A report is
  not a general statement about the region.
* **It has a delay.** The show carries `daysBeforeOutbreak = 1`: the thing reported is not
  reported at the moment it starts.
* **It expires.** `StartMassOutbreak` sets `outbreakDaysLeft = 2`, and the daily update subtracts
  the elapsed days and calls `EndMassOutbreak` when they run out — which zeroes the species, the
  level, the location, all four moves and the probability. The report is not archived. It is
  erased, which is exactly the opposite of the **Pokédex** SEEN bit's behaviour in m084, and the
  two together make the point: the record that cannot be cleared is the one about *what exists*,
  and the record that is wiped on a two-day timer is the one about *what is happening now*.

So the window in which the report is usable is short, it is held in one place, and when it lapses
there is nothing in the save file that says a report was ever made. If a Trainer wants the
information to survive, they have to write it down themselves.

## Where the metaphor stops

The adult in the room is not only a source of history. They may be frightened, they may not have
slept, they may be managing other children or a job they cannot leave, and they may be the person
who most needs something from the consultation. Treating them as an instrument is both unkind and
clinically worse, because an exhausted and unheard carer is a less reliable net. Sometimes the
most useful thing available is to say plainly that bringing the child was the right thing to do.

Being disbelieved while frightened about a child is a specific and lasting injury, and it is
distributed unequally — it falls hardest on people whose first language is not the system's, who
have attended often, who are young, who are poor, or who have been doubted before. That is m050's
pattern arriving in the most charged consultation in the specialty. The clinical cost and the
human cost run the same way here, which is unusual and worth stating: a carer who feels believed
gives a better history and returns sooner.

And two things are deliberately absent. Safeguarding is set aside: a presentation may raise a
concern about a child's safety, that is not a diagnostic question, and local safeguarding
procedure is the authority and is followed rather than reasoned about from first principles. The
prognosis of serious childhood illness is not discussed at all. Neither omission is an oversight,
and no part of the analogy above reaches either of them — which is the reason the route and not a
creature is the thing being assessed in this answer.

## What a Gym Leader is listening for

Whether the Trainer identifies the missing term first: that the standing record holds what is
normally there and nothing holds what was there yesterday, so no routine can compute a
difference. Then `MapHasSpecies` returning a bool, with the four questions its return type cannot
answer named. Then the report's extra content — one level, a location, a probability and four
named moves — against a table that carries no move data at all, and the first list entry's
missing fourth move noticed. Then the branch order, with the two things the report does not do
stated before the one thing it does. Then both filter bits surviving the report. Then the 40 per
cent skip on new ground, offered as the engine refusing to answer on one look. Then the two-day
counter against m084's unclearable SEEN bit, and the asymmetry between the two kinds of record.
Then the hardest one: how a Trainer would record a report so that the next Trainer on that route
inherits it, given that the engine erases it.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The national or regional guidance on assessment of the unwell or feverish child issued by the
  body governing the reader's practice, which is the authority on what is assessed and with what
  thresholds and differs between systems (**country-dependent**).
* A current standard textbook of paediatrics or paediatric primary care, for the examination
  sequence, for the observations that must precede handling, and for age-specific normal ranges,
  which are deliberately not reproduced here.
* The published literature on carer concern as a predictor of serious illness in children, read
  for effect size and for the population it was measured in, because m111's transport argument
  applies to it directly.
* The published literature on diagnostic delay and repeat attendance in children, for the
  re-presentation mechanism in the plain-prose section.
* The local safeguarding procedure applying where the reader works, which is procedural authority
  and not a reasoning document (**country-dependent**).

The Pokémon facts are a separate matter and are not covered by the line above. `MapHasSpecies`
returning a `bool8` after walking the land, water, rock-smash and fishing lists; the Area screen
excluding **Wynaut** by a one-entry hand-written list; the fishing search being passed the land
slot count, which the source notes in a comment; the absence of any stored previous state for an
encounter table; the five hand-written entries of `sPokeOutbreakSpeciesList` with their species,
levels, locations and moves, including the first entry's three moves against the others' four; the
report's `daysBeforeOutbreak` of 1, its `probability` of 50 and the `outbreakDaysLeft` of 2 set
when it is taken up; `EndMassOutbreak` zeroing the species, level, location, moves and
probability; `DoMassOutbreakEncounterTest` comparing both map group and map number and then
rolling `Random() % 100` against the probability; the branch order in `StandardWildEncounter`
placing the outbreak test after the rate test and before the ordinary table, with
`SetUpMassOutbreakEncounter` receiving both the Repel and **Keen Eye** filter bits; and
`AllowWildCheckOnNewMetatile` skipping the check 40 per cent of the time on first stepping onto a
new metatile type, were all read directly from the pret decompilation projects, which this
environment can reach. These are Emerald's; the outbreak mechanic is a Ruby, Sapphire and Emerald
feature and the species list differs between them.

## Scope and safety

This is revision material about the structure of a third-party history, written for someone
already training in or qualified for the field. It is not a clinical reference, not a decision
aid, and nothing here should inform the assessment or management of any individual child — that
belongs with the clinician who has assessed them and with current local guidance. No age-specific
normal range, observation threshold, red-flag feature, intake figure or timescale appears here on
purpose: those are age-dependent, locally specified and revised. Safeguarding is deliberately not
treated: where there is any concern about a child's safety, the local safeguarding procedure is
the authority and takes precedence over anything here. The percentages, counters and level values
above are real properties of a twenty-year-old video game and stand in for a mechanism; none of
them is a clinical quantity and no clinical figure should be read out of them. If a child is
unwell right now, the relevant action is to contact local urgent care or the local emergency
number, not to read this.

## Where this stands, October 2026

The structural claims — that the baseline comparison is available only through the account, that
observation precedes handling because handling destroys the observations, and that the net is held
by the carer — are mechanism and will not move. The specific guidance will and does: assessment
frameworks for the unwell child have been revised repeatedly, recommended observation thresholds
differ between countries and are periodically restated, and the evidence on carer concern as a
predictor continues to accumulate with effect sizes that vary by setting. The Emerald code is
stable because the games are finished. Take the thresholds and the frameworks from current local
guidance rather than from here, as of October 2026.
