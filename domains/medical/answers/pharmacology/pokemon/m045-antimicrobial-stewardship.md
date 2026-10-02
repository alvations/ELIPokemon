---
id: "m045"
slug: antimicrobial-stewardship
style: pokemon
category: pharmacology
difficulty: advanced
question: "What is antimicrobial stewardship optimising, and why does the way resistance spreads make it a collective-action problem rather than an individual prescribing decision?"
tags: [antimicrobial-stewardship, resistance, horizontal-gene-transfer, de-escalation, collective-action]
---

# Smeargle learns nothing but Sketch, and the function that runs it is called copymovepermanently.

There are two ways a Pokémon can come to know something it did not know before, and the Game Boy
Advance code keeps them in entirely separate files. One is slow, one-directional and gated by a
whitelist. The other takes one encounter with a stranger. That difference is the whole of why
antimicrobial resistance is a collective-action problem and not a prescribing preference.

## The slow way: the Day Care, and how strict it is

`BuildEggMoveset` is unsentimental. A hatchling gets an **Egg Move** only if the **father** knows
it *and* the move is on the hatchling species' own egg-move list. The mother's moves are loaded
into an array and then, for this purpose, contribute nothing by themselves. One parent, a
whitelist, one generation per pass.

That is descent, and descent is slow. A trait spreads at the rate things breed, down lineages,
inside a species. If that were the only route, you could reason about where a capability would end
up.

## The fast way: Sketch

```
   SMEARGLE'S ENTIRE LEVEL-UP LEARNSET, straight out of the data file

   level     1    11    21    31    41    51    61    71    81    91
   move    Sketch Sketch Sketch Sketch Sketch Sketch Sketch Sketch Sketch Sketch

   ...and nothing else, ever. Its base stats are 55 / 20 / 35 / 75 / 20 / 45 --
   unremarkable in every single slot. Smeargle has no capabilities of its own.
   EVERYTHING it can do, it took from something it met.

   SKETCH, from the move data and the engine:
     · 1 PP. One use.
     · no accuracy check at all
     · the command that implements it is literally named copymovepermanently
     · it writes the TARGET'S LAST USED MOVE into the Sketch slot, with that
       move's own full PP, and keeps it

   And the failure conditions, which are the instructive part:
     · fails if the user is Transformed
     · fails if the target's last move was Struggle, or Sketch itself
     · fails if the user ALREADY knows that move

   Note what is NOT on that list. No egg group. No shared species. No relation of
   any kind. No generation. Smeargle does not have to be anything like the thing
   it copies from, and one turn is the entire cost.
```

```
   THE TWO ROUTES, SIDE BY SIDE

   EGG MOVES                               SKETCH
   ───────────────────────────────────     ──────────────────────────────────────────
   father → hatchling                      any Pokémon → any Pokémon
   one lineage                             across lineages entirely
   gated by a per-species whitelist        gated by "did they just use it"
   one generation per pass                 one turn
   ───────────────────────────────────     ──────────────────────────────────────────
   "it stays in the line I bred"           THE LINE IS NOT THE BOUNDARY

   ┌──────────────────────────────────────────────────────────────────────────────────┐
   │  Everything structural about stewardship follows from the right-hand column.    │
   │  If a capability could only descend, "the consequence lands on the thing I      │
   │  treated" would be nearly true. It can also move sideways, so it is not.        │
   └──────────────────────────────────────────────────────────────────────────────────┘
```

**And the place the analogy is thinner than the biology, said rather than hidden.** The games keep
acquisition and inheritance in separate mechanics: a Sketched move does not then travel down a
breeding line the way an egg move does. Real mobile elements do both at once, and that combination
is why resistance spreads faster than either route alone would manage. The games give you the two
halves and not the compound.

**There is a second gap, and it is the bigger one.** Nothing in the Game Boy Advance code makes a
move work *less well* because it has been used a lot. Selection has no in-game mechanic. The
nearest real phenomenon is in competitive play, where the more heavily a strategy is used the more
counters appear on other people's teams until it stops paying — individually rational choices
degrading the format for everybody. That is a true thing about players, not a line of code, and it
is named here as general knowledge of the competitive scene rather than as something read from the
decompilation.

*(And **PP** carries no analogy in this answer, though Sketch's single point of it is quoted above
as a fact about the move. In this specialty PP already stands for one drug changing the rate at
which another is consumed — see `m009` — and borrowing it for antibiotic supply would muddle a
vocabulary worth keeping clean.)*

## Spectrum, from three lines of targeting data

```
   WHAT A MOVE REACHES -- the target flags, verbatim from the move data

   Flamethrower   MOVE_TARGET_SELECTED        one thing
   Surf           MOVE_TARGET_BOTH            both opponents
   Blizzard       MOVE_TARGET_BOTH            both opponents
   Earthquake     MOVE_TARGET_FOES_AND_ALLY   both opponents AND YOUR OWN PARTNER

   And then, separately, in the damage routine:
     a move targeting BOTH does HALF damage in a double battle with two
     defenders alive.

   So the broad option, in one line:
       reaches more       · hits each one for less       · hits your own side
```

Three properties, all of them in the code, and all three are the broad-spectrum profile exactly:
greater coverage, lower potency against any individual target, and collateral to things that were
never the problem. **Earthquake** is the one that makes the point land, because the collateral is
not hypothetical — your partner takes it, every time, and the move data says so.

## Buying information before committing

The Game Boy Advance games have **no Team Preview**. You send something out and commit a move
knowing only the species facing you: not its item, not its ability, not its four moves. So the
first turn is a guess from whatever you know about the trainer class and the route, and the
information arrives afterwards — which means the right play is to revise, not to keep executing
the guess.

The games also sell you the alternative, at a price. **Lock-On** and **Mind Reader** spend an
entire turn to set `STATUS3_ALWAYS_HITS` on the target for two turns, recording which Pokémon is
owed the guarantee. A turn, for certainty on the next one. Taking a culture before the first dose
is the same trade and the same arithmetic: you give up something now so the next decision can be
narrow instead of a guess.

(Later generations added Team Preview, showing the six species but still not their sets. That is
from general knowledge of those games, not from the code read here.)

## The commons, actually written down in the cartridge

This is the strongest fact in the answer. The **Battle Frontier**'s eligibility check,
`AppendIfValid`, is a stewardship document compiled into the cartridge. It refuses a Pokémon if:

| The rule | What it is in the code |
| --- | --- |
| It is on the reserve list | `gFrontierBannedSpecies` — **Mew**, **Mewtwo**, **Ho-Oh**, **Lugia**, **Celebi**, **Kyogre**, **Groudon**, **Rayquaza**, **Jirachi** and **Deoxys** |
| You already picked that species | a scan of the chosen species so far, and a refusal on a match |
| You already picked that held item | the same scan over held items, applied when the slot is not empty |
| It is over the cap | the Level 50 mode refuses anything above its own ceiling |

Nobody is claiming **Kyogre** is a bad Pokémon. That is the entire point. The list exists so that
the format continues to be a format — so that a facility with a shared player base stays worth
entering — and the cost of each individual exclusion falls on whoever wanted to bring that
Pokémon, while the benefit is spread across everyone who plays there afterwards.

A restricted antimicrobial list is the same object. It is not a judgement about the drug; it is a
statement that the drug's usefulness is a shared, depletable thing, and that the decision about
spending it should not sit entirely with whoever happens to be holding the prescription pad at two
in the morning.

## The review that nobody set

**Fire Spin** lands and sets a counter to `(Random() & 3) + 3` — three to six, rolled by the game,
chosen by nobody. It then ticks down and takes a sixteenth of the holder's maximum HP each turn
while it lasts. The duration was never a decision, nothing on the attacking side can change it,
and it simply runs until it stops.

**Rapid Spin** is the only thing that revisits it, and the code is pointed about how little it
does at once: one use clears exactly **one** thing, in a fixed order — trapping first, then
**Leech Seed**, then **Spikes**. Three problems need three turns. The review is not free, it is
not automatic, and it only ever unwinds one thing per visit.

A course length set at the start and never looked at again is a counter nobody chose. The review
point exists because, by default, nothing revisits anything.

## Where the metaphor stops

Everything above is mechanism, and mechanism is what the analogy is for. The consequence is not,
and here the Pokémon framing stops completely.

A resistant infection is not a fact about the future. It means a person whose infection does not
respond to the drug that should have worked, treated instead with something more toxic, or less
effective, or only available by injection, for longer, with a worse outcome. People die of this
now, and there is no version of that which belongs in a battle.

The honest and uncomfortable half: a prescription that contributed was almost never reckless. It
was written under uncertainty, often out of hours, with incomplete information, by someone trying
to protect the person in front of them, in a system that gave them no way to see or feel the cost
they were passing on. That is exactly why the answer is structural — restriction lists,
authorisation routes, stop dates, audit and feedback. Blaming individual prescribers for a commons
failure is both unjust and ineffective.

And the misreading that does the most harm has to be named directly. Stewardship is **not**
withholding antibiotics from someone who needs them. In sepsis, delay in effective treatment is
itself a major cause of death, and the stewardship act in a septic patient is the review, the
narrowing and the stopping — not hesitation at the front door. Untreated bacterial infection kills
people far more reliably than resistance does, and "antibiotics are overused" has been heard by
some as a reason to wait before seeking help. It is not one.

Nothing in this answer or its technical twin names an antibiotic, a dose or a course length, and
nothing in either is advice about anyone's own treatment. Nobody should stop, decline or delay a
prescribed antibiotic on the strength of anything here; the person to ask is the prescriber or
pharmacist who can see the records and the results.

## What a Gym Leader is listening for

* Why is **Sketch** a different kind of thing from an **Egg Move**, and which difference is the
  one that matters?
* Name three conditions under which **Sketch** fails. Is "not related to the target" one of them?
  (No.)
* **Earthquake** against a single-target move. Name all three differences, from the move data.
* What does a turn spent on **Lock-On** buy, and what is the clinical trade with the same shape?
* Why does `gFrontierBannedSpecies` exist, given that nobody thinks **Rayquaza** is weak?
* **Rapid Spin** clears one thing per use. What is the general point hiding in that?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer, and to its technical twin:

* **Your institution's own antimicrobial guideline and its local antibiogram** — the authority for
  every empirical choice in this topic, overriding a national guideline where the two differ.
* **Your institution's antimicrobial stewardship policy**, for the restriction list, the
  authorisation route, the review requirement and the stop-date rules.
* **Your national guideline body's antimicrobial prescribing guidance**, issued per-infection in
  most countries and revised frequently — course lengths above all.
* **The World Health Organization's publications on antimicrobial resistance and its access, watch
  and reserve categorisation of antibiotics.**
* **Your national surveillance report on antimicrobial resistance and consumption.**
* **The primary literature** for any course-length claim, which is where the evidence has moved
  most.

The Pokémon figures are a different matter and were checked against the public decompilation of
the Game Boy Advance games, read directly: Smeargle's level-up learnset consisting of Sketch at
level 1 and again at 11, 21, 31, 41, 51, 61, 71, 81 and 91 and nothing else; Smeargle's base stat
line of 55 / 20 / 35 / 75 / 20 / 45; Sketch having 1 PP and no accuracy check, being implemented
by a command named `copymovepermanently`, writing the target's last used move into the Sketch slot
with that move's own full PP, and failing if the user is Transformed, if the target's last move
was Struggle or Sketch, or if the user already knows the move; `BuildEggMoveset` granting an egg
move only when the father knows it and it appears on the hatchling species' egg-move list; the
target flags of Flamethrower, Surf, Blizzard and Earthquake, and the halving of a both-opponents
move's damage in a double battle with two live defenders; Lock-On and Mind Reader setting
`STATUS3_ALWAYS_HITS` for two turns with the guaranteeing battler recorded; `AppendIfValid`
refusing a banned species, a duplicate species, a duplicate non-empty held item and a Pokémon
above the Level 50 mode's ceiling, and the contents of `gFrontierBannedSpecies`; Fire Spin's trap
counter being `(Random() & 3) + 3` with `maxHP / 16` taken per turn while it remains; and Rapid
Spin clearing exactly one of trapping, Leech Seed or Spikes per use, in that order.

**Two Pokémon claims here are not from code**, and both are flagged where they appear: that heavy
use of a strategy in competitive play draws out counters until it stops paying is a social fact
about players rather than a line of code; and Team Preview belongs to the later generations, whose
source was not read. Those are the two to check before repeating.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **No antibiotic, dose, course length or empirical regimen is named in either
half of this pair**, deliberately: empirical choice is a function of local susceptibility data and
local policy, and a regimen remembered from revision material is exactly the wrong thing to carry
to a bedside. Nothing here should be used to make a decision about anyone's treatment, including
your own, and nothing in it is a reason for anyone to delay seeking help for an infection or to
stop or decline a prescribed antibiotic. The institution's guideline, the microbiology service and
the local antibiogram are the authority. A banlist in a cartridge protects a format. It is not a
decision about a person.

## Where this stands, October 2026

The mechanism — mobile elements, transfer between unrelated organisms, selection by removal of
competitors — is established biology and does not date, and the commons analysis is structural.
The game mechanics cited are fixed in released software, though the series has changed several of
them between generations and this answer pins the ones it uses to the Game Boy Advance games. What
dates, and fast, is everything operational in the twin: recommended **course lengths**, which have
shortened repeatedly across many indications and continue to; restriction and reserve lists,
revised locally and nationally; local susceptibility patterns, which change continuously and are
the input to every empirical choice; and the categorisation of individual agents. Rapid
diagnostics and biomarker-guided stopping have been moving the review step at different rates in
different health systems. Check your institution's current guideline and your current local
antibiogram.
