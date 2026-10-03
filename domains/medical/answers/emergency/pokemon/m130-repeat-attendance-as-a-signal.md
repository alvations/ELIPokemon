---
id: "m130"
slug: repeat-attendance-as-a-signal
style: pokemon
category: emergency
difficulty: intermediate
question: "Why is repeat attendance a clinical signal rather than a nuisance, and what makes the pattern the finding?"
tags: [reattendance, pattern, records, diagnosis, revision]
---

# Seen is one bit, so the fortieth Zubat writes exactly what the first one wrote

`GetSetPokedexFlag` is the whole of the Pokédex's storage model, and the arithmetic in its first
four lines decides everything else:

```
   nationalDexNo--;
   index = nationalDexNo / 8;
   bit   = nationalDexNo % 8;
   mask  = 1 << bit;
```

One species, one bit. `FLAG_SET_SEEN` is then an unconditional OR into three arrays:

```
   case FLAG_SET_SEEN:
       gSaveBlock2Ptr->pokedex.seen[index] |= mask;
       gSaveBlock1Ptr->seen1[index]        |= mask;
       gSaveBlock1Ptr->seen2[index]        |= mask;
       break;
```

`|= mask` on a bit that is already set is a no-op. So the first encounter and the four-hundredth
produce identical memory, and there is nowhere for the difference to go. **The count is not lost
later; it is discarded at the instant of recording**, which is a property of the storage layout
and not of anybody's attention.

`HandleSetPokedexFlag` makes it explicit, with the comment in the source:

```
   u8 getFlagCaseId = (caseId == FLAG_SET_SEEN) ? FLAG_GET_SEEN : FLAG_GET_CAUGHT;
   if (!GetSetPokedexFlag(nationalNum, getFlagCaseId))   // don't set if it's already set
   { ... }
```

The repeat encounter is explicitly short-circuited. A player who meets forty Zubat on the way
through Mt. Moon and one Clefairy has two set bits, and the save file cannot tell those two
experiences apart in any way at all. Question m012 puts the clinical use of exactly that pair —
you do not clear Mt. Moon of Clefairy by meeting ten Zubat — and this is the storage reason the
arithmetic was never available to begin with.

## And the counter that does exist counts the wrong thing

`GetNationalPokedexCount(FLAG_GET_SEEN)` loops the whole national dex and totals the set bits. It
is a count — of **species**, not of encounters. The number the Pokédex proudly displays is the
width of the set and says nothing about the multiplicity of any member, which is exactly the
available-but-wrong statistic.

There is one more wrinkle worth having, because it is the shape of a record that erases itself.
The `FLAG_GET_SEEN` read holds three copies and compares them:

```
   if (gSaveBlock2Ptr->pokedex.seen[index] & mask)
   {
       if (same bit in seen1 and seen2 agrees) retVal = 1;
       else { clear it in all three; retVal = 0; }
   }
```

A disagreement between the copies is resolved by **deleting the record and returning zero**, and
zero is indistinguishable from never-encountered. Question m084 reads this same function for the
opposite property — that no case in it ever clears a bit deliberately — and this is the one path
that does, as an integrity measure, and it reports its deletion as an absence.

## The one place in the engine where "I have met this before" is arithmetic

`Cmd_handleballthrow` reads the record of previous encounters exactly once, and it is the Repeat
Ball:

```
   case ITEM_REPEAT_BALL:
       if (GetSetPokedexFlag(SpeciesToNationalPokedexNum(species), FLAG_GET_CAUGHT))
           ballMultiplier = 30;
       else
           ballMultiplier = 10;
       break;
```

A threefold multiplier, conditioned on nothing but whether this species is already in the record.
Everything else in that switch reads the present: the Net Ball reads the target's type, the Dive
Ball reads `GetCurrentMapType()`, the Nest Ball computes `40 - level`, and `sBallCatchBonuses`
gives the Poké Ball 10, the Great Ball 15, the Ultra Ball 20 and the Safari Ball 15. One case out
of all of them consults the history, and the engine's designers put a factor of three on it.

Note what this is being used for here and what it is not. `CONVENTIONS.md` Part III fences off
catching as a mapping for diagnosis or admission, and that fence holds: nothing in this answer
maps the act of throwing a ball onto anything a clinician does. What is being read is the
**arithmetic** — a prior-encounter record entering a probability as a multiplier — which is the
use questions m011 to m013 established for ball mechanics and the only one available.

Two more cases in the same switch are worth having. **Luxury Ball and Premier Ball share a
single case** and both return `ballMultiplier = 10` — two differently named objects with
byte-identical arithmetic, so a player who believes the name is doing something is wrong in a
way the interface will never correct. And a few lines further down the engine writes
`gBattleResults.usedMasterBall = TRUE`: the Master Ball is recorded as **one boolean**, so the
save knows that a Master Ball was used at some point and not how many or when. That is the same
storage decision as the Pokédex's seen bit, taken again for a different fact.

The Timer Ball immediately below it is the other half of the idea:

```
   case ITEM_TIMER_BALL:
       ballMultiplier = gBattleResults.battleTurnCounter + 10;
       if (ballMultiplier > 40) ballMultiplier = 40;
       break;
```

Elapsed turns entering the same multiplier slot, capped at 40. So the engine has a representation
of *how long this has been going on* and a representation of *whether this has happened before*,
in adjacent cases of one switch, each worth up to a factor of three or four — and neither of them
is ever consulted by anything other than a ball.

## Unusual frequency is stored on the route, not on the species

The game does model something happening more often than usual. It is the mass outbreak, and the
striking thing is where the state lives:

```
   static bool8 DoMassOutbreakEncounterTest(void)
   {
       if (gSaveBlock1Ptr->outbreakPokemonSpecies != SPECIES_NONE
        && gSaveBlock1Ptr->location.mapNum   == gSaveBlock1Ptr->outbreakLocationMapNum
        && gSaveBlock1Ptr->location.mapGroup == gSaveBlock1Ptr->outbreakLocationMapGroup)
       {
           if (Random() % 100 < gSaveBlock1Ptr->outbreakPokemonProbability)
               return TRUE;
       }
       return FALSE;
   }
```

Three fields and a roll. The species, the **map**, and a probability — and the test fails on the
map before it ever looks at the species. The frequency is a property of the *place*, held in the
save block against a location, which is question m081's reading of the same mechanic and the
correct shape for a pattern that belongs to a context rather than to an individual.

The list it is drawn from is five hand-written entries in `src/tv.c`, chosen by
`Random() % ARRAY_COUNT(sPokeOutbreakSpeciesList)`, and the struct's fields are the giveaway —
`species`, four `moves`, a `level` and a `location`:

```
   Seedot   level  3   Route 102    Bide, Harden, Leech Seed
   Nuzleaf  level 15   Route 114    Harden, Growth, Nature Power, Leech Seed
   Seedot   level 13   Route 117    Harden, Growth, Nature Power, Leech Seed
   Seedot   level 25   Route 120    Giga Drain, Frustration, Solar Beam, Leech Seed
   Skitty   level  8   Route 116    Growl, Tackle, Tail Whip, Attract
```

Seedot appears four times across three routes at three levels, and every entry is a *place plus
a species plus a level*, never a species on its own. `outbreakDaysLeft` is then set to `2` when
the show is watched, so the state carries a **duration** as well as a location — the one clock
in this whole answer, and it is attached to the outbreak and not to any Seedot.

And the filtering is inconsistent in a way nobody intended. The land path calls
`SetUpMassOutbreakEncounter(WILD_CHECK_REPEL | WILD_CHECK_KEEN_EYE)`; the water path calls
`SetUpMassOutbreakEncounter(0)`. Same signal, same function, and on one route every filter is
applied and on the other none is. This is the same class of defect as Sweet Scent's `flags = 0` in
question m048 and the fishing path's missing flags in question m045 — except that Sweet Scent's
zero is deliberate and these two are a parameter nobody threaded through. A signal that is
filtered on one route into a system and not on another will be seen at different rates for reasons
that have nothing to do with the signal.

## Where the game has nothing

**No structure anywhere in the third generation counts how many times one species has been
encountered.** Not the Pokédex, which holds bits. Not `gBattleResults`, which holds the last
battle. Not the Pokédex area screen, which maps where a species *can* be found rather than where
it *was*. The quantity this whole answer is about has no field, and that is the finding rather
than a gap to be papered over: the engine will cheerfully tell you the width of your experience
and has no way of telling you its depth.

The nearest thing to a count anywhere in the save is the Pokérus byte, and it is instructive
because it is a *pair* of queries rather than a tally. `CheckPartyPokerus` reads
`MON_DATA_POKERUS & 0xF` — the active-days nibble, meaning *is this happening now* — while
`CheckPartyHasHadPokerus` reads the whole byte, meaning *has this ever happened*. Two functions,
one mask apart, answering now and ever and nothing in between. Question m084 reads the same pair
for a marker that outlives what it marked; the point here is that the engine thought it worth
writing two functions to separate *now* from *ever* and never wrote one for *how often*.

**And there is no interval anywhere either.** Even if the count existed, nothing records when. The
Timer Ball's `battleTurnCounter` resets with the battle; there is no timestamp on a dex flag. So
the two quantities that would make a pattern readable — how many, and how far apart — are the two
the save format has no room for.

## Where the metaphor stops

Plain prose from here, with no game in it, because the subject is somebody who has been labelled
for coming back.

Somebody returns: third time this month, second time this week, fourth time since the spring. The
clinical content of that sentence is almost entirely in the **number and the spacing**, and almost
nothing about the way the information is stored makes either available. Each attendance is
recorded as an episode with a complaint, an assessment and an outcome, and there is no field
saying *this is the fourth*; the system that would compute it is usually not the one in front of
the assessing clinician. (**Mechanism** — a property of how the information is held, not a claim
about anybody's diligence.) Two claims then get fused that should not be. *This person has
attended repeatedly* is a datum. *This person is attending unnecessarily* is a conclusion, and it
is what the word *frequent* is routinely heard as containing; the second does not follow from the
first, and the assessment that would test it is the one the fused reading prevents.

Given that somebody has come back, a small number of structurally different things may be
happening. The original problem was correctly characterised and has progressed, in which case the
return is the safety-net working as designed. It was mis-characterised, in which case the return
is the only mechanism that will ever correct it and the previous assessment is now a source of
anchoring rather than reassurance. There is a separate new problem, and the record of the old one
is actively misleading. The characterisation was right and the plan failed — the medicine could
not be obtained, the follow-up could not be reached, it could not be afforded, it was not
understood, nobody was free to bring them. The underlying condition relapses, and the interval
between relapses is itself the clinical measure, so the count *is* the severity marker and no
single visit shows it. Or the need being presented is real and is not the one the department
treats, which is still a clinical problem — question m105's argument about a label that names
where a cause is and gets read as naming its absence. The branch cannot be determined from the
current visit alone, which is what makes the pattern a finding rather than a context: it is the
only observation that discriminates, and the alternative to using it is not a neutral assessment
but a repeat of the previous one. (**Mechanism.**) Two of those branches are the most often
collapsed. For a relapsing condition the frequency is the measure, and a clinician who treats each
episode as self-contained has not measured what the condition is graded by — the specific
conditions, their control measures and their escalation steps are guideline material and are not
described here. (**Consensus.**) And a failed plan looks identical to a failed patient from inside
one consultation; the two are separated only by asking what happened after the last visit, which
is cheap, rarely asked, and distinguishes a dispensing or transport problem from a disease
problem. (**Mechanism.**)

The previous record is simultaneously the best information available and the main threat to the
current assessment. It anchors, because a documented conclusion is read before the person is seen
and every later observation is interpreted against it — question m068's anchoring and question
m048's premature closure, with the unusual feature that the anchor carries a colleague's
signature. (**Consensus.**) *Nothing found* is not a negative finding unless somebody recorded
what was looked for, since an episode logged as *no acute pathology* with no account of the search
is indistinguishable from one in which little was looked for — question m070's missing pertinent
negative and question m037's distinction between documented-as-seen and documented-as-confirmed.
(**Mechanism.**) The record of a *different* problem misleads in a specific direction, because a
person known for one thing is at structural risk of having the next thing attributed to it. And
the reassurance compounds: each visit at which nothing was found raises the subjective prior that
nothing will be found, which is not updating on new evidence but the same evidence counted
repeatedly. (**Mechanism.**) The consequence is not to ignore the record but to read it for **what
was looked for** rather than **what was concluded**, and to discount a conclusion whose search is
unrecorded.

Making the pattern usable rather than merely present is structural, and (**country-dependent**) in
every particular. The count has to be computed and surfaced rather than remembered, because a
count that depends on somebody noticing is noticed on quiet shifts. The window is a clinical
choice, since reattendance within hours, days and months mean different things and a single flag
with a single interval conflates them — and the intervals used in measurement are set for audit
purposes as much as clinical ones. The flag has to reach somebody who can act on the sequence
rather than only the person assessing today's episode, because the first gets a better single
assessment and the second gets the diagnosis. And reattendance used as a quality indicator is not
the same quantity as reattendance used as a clinical signal; once the count is a performance
measure, the incentive attached to it points away from treating it as information. (**Consensus**
that this tension exists; its handling is local.) No interval, threshold, flagging system or
care-planning process is named in this answer, because all of them are local and revised.

What is at stake for a person is not in any of that. The informal labels in use for this are
judgements wearing the clothes of descriptions, and people know: somebody who has attended six
times knows exactly how they are being read, often before anyone speaks, and that knowledge
changes what they say — so the label degrades the quality of the history that would resolve the
question it stands in for. Coming back is frequently the exact behaviour that was asked for, since
the previous safety-net advice said to return if things worsened, and somebody punished for
compliance will weigh the next necessary return against this experience. The people most likely to
attend repeatedly are in aggregate the people with the fewest alternatives, the least ability to
wait, the least access to a regular clinician and the worst health; the inverse care law is a
mechanism rather than a complaint — question m050's argument — and this is where it is most
visible and most often mistaken for a behavioural trait. The frustration in a department under
pressure is real and is not a reason: the resources that would change the pattern are usually
elsewhere, and the correct response to a problem whose solution lies elsewhere is to characterise
it accurately and refer it rather than attach it to the person standing there. And a person who
expects to be dismissed is disarmed by being told plainly that coming back was right, and that a
fourth visit is itself a reason to look at the whole sequence; that sentence costs nothing, it is
true, and it changes the consultation. A proportion of reattendances genuinely are for problems
the department cannot help with, and pretending otherwise is not kindness — the argument is not
that every return is a missed diagnosis, but that the number and the spacing are information, that
they are routinely discarded, and that the discarding happens at the point of recording.

No Pokémon stands for a patient anywhere in this answer, and nothing in it maps catching onto
anything a clinician does. No creature attends anything, nobody is assessed, and no encounter
represents a person arriving anywhere. The game is carrying three ideas: that a record can discard
a count at the instant of writing, so the count is unavailable later for reasons of layout rather
than attention; that one place in a large system can treat *this has happened before* as
arithmetic, which shows the quantity was computable all along; and that unusual frequency can be a
property of a place rather than of an individual, and can be filtered differently depending on
which route it arrives by. Labels, compliance punished, and the knowledge of being read before
being spoken to are stated above without ornament and are not mechanics.

## What a Gym Leader is listening for

* How many bits does the Pokédex spend on *seen*? What does that do to the fortieth encounter?
* `FLAG_SET_SEEN` is an unconditional OR, and `HandleSetPokedexFlag` guards it anyway. Why does
  that not matter?
* `GetNationalPokedexCount` is a count of what, exactly?
* Three copies of the seen bit disagree. What does the read return, and what is that
  indistinguishable from?
* Which single case in `Cmd_handleballthrow` reads the history, and what multiplier does it apply?
* Name three cases in the same switch that read only the present, and say what each reads.
* What does the Timer Ball read, and where is it capped?
* Where is a mass outbreak stored, and which of its three conditions is tested first?
* `SetUpMassOutbreakEncounter` is called with two different flag arguments. Name them and say what
  follows.
* Luxury Ball and Premier Ball share a case. What does that tell a player about the names?
* How is a Master Ball's use recorded, and what does that record not contain?
* `CheckPartyPokerus` and `CheckPartyHasHadPokerus` differ by one mask. What does each ask?
* Name the two quantities the save format has no field for at all.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md), and they
apply here. Specific to this answer:

* The current standards for emergency department assessment, documentation and reattendance issued
  by **the reader's national emergency medicine college** — where the expectation about recording
  what was looked for sits, and where any reattendance interval used in measurement is defined.
* **The reader's own employing organisation's** policy on reattendance flagging, on individual
  care planning for people who attend frequently, and on referral to community and specialist
  services.
* The current national definitions used for measuring unplanned reattendance, issued by **the
  reader's national body for health service statistics or performance measurement**, which is a
  different document written for a different purpose.
* A current standard textbook of **emergency medicine**, and the literature on **diagnostic
  error**, for anchoring, premature closure and the handling of a previous diagnostic conclusion.
* **The primary literature**, for the characteristics of populations who attend frequently and for
  the evidence on interventions aimed at them. No proportion, rate or effect size is quoted here.

Markers used in the plain-prose section above: (**mechanism**) (follows from the structure of the
problem or of the record and is checkable by reasoning), (**consensus**) (agreed across mainstream
sources as of writing), (**country-dependent**) (genuinely differs between countries, services or
institutions). No interval, threshold, flagging system, care-planning process or statistic is
given, and nothing is quoted, because none of these was opened. The Pokémon side is in the
opposite position and is sourced file by file in the closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *how a pattern across episodes becomes a clinical finding and why
it is usually lost*, written for someone already trained, and the Pokémon framing covers only
record layout, a history entering an arithmetic, and frequency stored against a place. It is
deliberately not a protocol and not a decision aid: no reattendance interval, no threshold, no
flagging system, no care-planning process and no statistic. It contains no account of capacity,
consent, or the protection of adults or children at risk, because those are matters of law that
differ by jurisdiction and the reader's own legislation and statutory guidance are the only
acceptable source. Record systems, reattendance definitions, flagging arrangements and service
availability differ enormously between countries and institutions. The reader's own national
guidance and local policy are the authority; this is not, and it has had no clinical review.
Nothing here describes any real person.

## Where this stands, October 2026

The Pokémon facts are pinned to source and are stable. `GetSetPokedexFlag`'s `index = n / 8` and
`mask = 1 << (n % 8)` arithmetic, its three-copy integrity check that clears all three and returns
zero on disagreement, `FLAG_SET_SEEN` as an unconditional OR into three arrays, and
`GetNationalPokedexCount` totalling set bits are read from `src/pokedex.c`;
`HandleSetPokedexFlag`'s already-set guard, with its comment, is from `src/pokemon.c`. The ball
cases in `Cmd_handleballthrow` — Repeat Ball's 30 against 10 on `FLAG_GET_CAUGHT`, Timer Ball's
`battleTurnCounter + 10` capped at 40, Net Ball's Water or Bug test, Dive Ball's
`GetCurrentMapType()`, Nest Ball's `40 - level`, and `sBallCatchBonuses` giving the Poké, Great,
Ultra and Safari Balls 10, 15, 20 and 15 — are from `src/battle_script_commands.c`.
`DoMassOutbreakEncounterTest`'s three conditions and its `Random() % 100` roll, and the two
different flag arguments passed to `SetUpMassOutbreakEncounter` on the land and water paths, are
from `src/wild_encounter.c`; the five-entry `sPokeOutbreakSpeciesList` with its `species`,
`moves`, `level` and `location` fields, its `Random() % ARRAY_COUNT` draw and
`outbreakDaysLeft = 2` are from `src/tv.c`; Luxury Ball and Premier Ball sharing one case and
`gBattleResults.usedMasterBall` as a boolean are from `src/battle_script_commands.c`; and
`CheckPartyPokerus` masking `& 0xF` against `CheckPartyHasHadPokerus` reading the whole byte is
from `src/pokemon.c`. All of it is **third generation**, read from `pokeemerald`; later
games change the Pokédex record substantially, add encounter-chaining mechanics that do count
repeats, and change ball catch modifiers, so a reader checking today's game should read today's
game — the claim that nothing counts repeat encounters is a claim about this generation only. On
the clinical side the argument is stable and the implementation is not: record systems and what
they surface change with each procurement, the intervals defining unplanned reattendance are set
nationally for measurement and are revised, individual care planning for frequent attendance
exists in some systems and not others and is contested where it exists, the evidence on
interventions keeps being restudied with mixed results, and the availability of the community
services that would change the pattern is a political variable rather than a clinical one. The law
on the protection of adults and children at risk differs by jurisdiction and is not described here
at all. Principle dated October 2026; read the current guidance for anything past the principle.
