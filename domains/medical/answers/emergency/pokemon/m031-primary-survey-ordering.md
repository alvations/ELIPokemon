---
id: "m031"
slug: primary-survey-ordering
style: pokemon
category: emergency
difficulty: intermediate
question: "Why is the primary survey ordered airway, breathing, circulation, and what is that ordering actually sorting on?"
tags: [primary-survey, abcde, prioritisation, protocol-design, revision]
---

# Priority is read before Speed, and nothing done to Speed ever changes that

Every move in the games carries a priority number, and the turn-order routine compares those
numbers **before it looks at a Speed stat at all**. In Emerald's `GetWhoStrikesFirst` the two
Speed values are computed first, complete with the badge boost, Swift Swim, Agility's stat stage
and paralysis — and then, if the two chosen moves sit in different brackets, the function returns
on the bracket comparison and those Speed numbers are never read. They were calculated and thrown
away. That is the whole shape of the structured primary survey: a forced ordering on top, and
everything about how fast and how good anyone is underneath it.

So *which of these looks worst* is the wrong question, in the same way that *which Pokémon has the
higher Speed* is the wrong first question. Base Power is a different key. Type Effectiveness is a
different key. A Hyper Beam off a huge Attack stat is the most dramatic thing on the field and it
is in bracket 0, so **Quick Attack** off a feeble one resolves first every single time. The
bracket is the sort; everything else is the tie-break.

## What the sort looks like

Emerald's table, read off `src/data/battle_moves.h` and exact:

```
  bracket   moves that sit in it                                   consulted
  ──────────────────────────────────────────────────────────────────────────────
    +5      Helping Hand                                              1st
    +4      Snatch, Magic Coat                                        then
    +3      Protect, Detect, Endure, Follow Me                        then
    +1      Quick Attack, Mach Punch, Extreme Speed, Fake Out         then
     0      almost every move in the game                             then
    -1      Vital Throw                                               then
    -3      Focus Punch                                               then
    -4      Revenge                                                   then
    -5      Counter, Mirror Coat                                      then
    -6      Whirlwind, Roar                                           last
  ──────────────────────────────────────────────────────────────────────────────
       Speed, the Dynamo Badge, Agility, Swift Swim, Macho Brace,
       paralysis, Quick Claw ─────────────────┘  all of it lives in here,
                                                 inside one bracket, never across
```

## Three properties that make the ordering forced rather than conventional

**It is also a dependency order, and the two agree.** The brackets are not arbitrary rankings of
how exciting a move is. **Counter** and **Mirror Coat** sit at -5 because they can only work on a
hit that has already landed — resolve them early and they have nothing to answer. **Focus Punch**
sits at -3 because the whole move is a wager that nothing interrupts the wind-up. **Snatch** at +4
has to be in place before the thing it steals is used, or it steals nothing. Each bracket number
is a statement that this action is useless unless something else has or has not happened yet, and
the urgency ordering and the dependency ordering come out the same. That coincidence is what lets
the whole system be a single number on each move instead of a web of conditions.

**The stat belongs to the Pokémon; the bracket belongs to the move.** This is the part people
argue with, and **Quick Claw** settles it. Its hold effect parameter is 20, and the check in
Emerald is `gRandomTurnNumber < (0xFFFF * 20) / 100` — one turn in five. What the item then does
is not promote the holder a bracket. It sets that Pokémon's Speed value to the largest number the
field can hold. Infinite Speed. And infinite Speed in bracket 0 still resolves after a Quick
Attack, every time, because the comparison that decides the turn never reaches the Speed numbers.
Everything that makes a Pokémon fast behaves the same way: the **Dynamo Badge** — Wattson's, the
third in Hoenn — multiplies the player's Speed by 110/100, **Swift Swim** and **Chlorophyll**
double it in rain and sun, **Agility** raises the stat stage, **Macho Brace** halves it and
paralysis quarters it. Ten different modifiers, all of them inside one bracket.

**The bracket numbers themselves get revised, and that is the proof, not the flaw.** Emerald puts
**Extreme Speed** at +1 and **Fake Out** at +1. In current generations Extreme Speed is +2 and
Fake Out is +3, and **Trick Room** sits below Whirlwind at the very bottom of the table. The
machinery did not change at all — brackets are still read before Speed, and Speed is still the
tie-break. What changed is a judgement about which actions deserve to resolve sooner, and when the
judgement changed the number moved. An ordering that is revised on a cycle while its principle
holds still is exactly what a derived ordering looks like.

```
   what was selected                        resolution order
   ───────────────────────────────────────────────────────────────────
   two moves in bracket 0                   Speed, then a coin flip
   Quick Attack against a move at 0         Quick Attack, at any Speed
   Whirlwind against a move at 0            the other one, at any Speed
   Helping Hand against Quick Attack        Helping Hand, at any Speed
   ───────────────────────────────────────────────────────────────────
   one routine, four input pairs, four orders
```

## What the ordering gives up

* **A bracket is coarse.** +1 says *sooner*. It does not say how much sooner, and it cannot say
  that two things should land together. Doubles play needs **Follow Me** and **Helping Hand** as
  separate explicit moves precisely because the bracket number cannot express coordination.
* **It reads as a queue when the real structure is a field.** In a double battle four actions are
  ordered, not two, and the ordering says only who wins a collision. A player who reads the
  bracket list as a strict to-do list and ignores three of the four slots has wasted most of the
  field.
* **A declared number is a judgement, and judgements are sometimes wrong.** That is why the table
  has errata. **Prankster** was added later to lift an entire class of move by one bracket, which
  is an admission that the per-move numbers had not captured something.
* **Reaching the bottom of the table is not the same as having understood the turn.** Resolving
  everything is not winning anything.

## Why it is a number on the move at all

Because the alternative is what Red and Blue did, and it did not scale: `engine/battle/core.asm`
checks by name whether the selected move is Quick Attack, then by name whether it is Counter, and
then falls through to Speed. Two hand-written special cases in the battle loop, and no table
anywhere. Question m032 is about why that got replaced with a written-down number on every entry.

## Where the metaphor stops

Plainly, and without the metaphor, because this is the part it is not for.

The clinical ordering sorts on how quickly an unaddressed failure in a person's body causes harm
that cannot be undone. The airway's clock is the shortest; ventilation's is next; circulation's is
next and depends on the rate of loss; brain injury and loss of body heat are slower. That is
(**mechanism**) — it follows from how oxygen reaches tissue, and it is checkable by reasoning
rather than by citation. That both of the re-sorted sequences exist is (**consensus**); how each
is worded, bounded and named is **council-dependent**. Nothing in Pokémon stands for a person
here, and nothing should. The game is being used for one thing only: the shape of a rule in which
a forced ordering is read first and skill is read second. The reason that shape is used in an
emergency is not a mechanic and is not entertaining, and an answer that tried to make it
entertaining would be a defect in this dataset rather than a flourish.

## What a Gym Leader is listening for

* What does the turn-order routine compare first, and what does it do with the Speed numbers it
  already computed?
* Why is Quick Claw the decisive example rather than just a cute one?
* Why do the bracket numbers and the dependency requirements agree, and what would follow if they
  did not?
* Extreme Speed moved from +1 to +2. What does that tell you about the table, and what does it
  tell you about guidance that gets revised?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md).
Specific to this answer:

* The current adult basic and advanced life support guidelines issued by **the national
  resuscitation council for the country the reader practises in**. There is no single global
  document, the councils differ from one another, and each revises on its own cycle.
* The current consensus on science with treatment recommendations issued by **the International
  Liaison Committee on Resuscitation**, which is the evidence synthesis the national councils
  write their own guidelines from.
* The current primary survey and catastrophic-haemorrhage guidance issued by **the reader's
  regional or national trauma network**.
* **The reader's own employing organisation's** resuscitation and trauma policy, which is the
  document that actually governs practice where they work and which outranks every general account
  including this one.

No guideline number, document title or identifier is given, and nothing is quoted, because none of
these was opened. The Pokémon side of this answer is in the opposite position and is sourced in
the closing note: those facts were read from the decompilations and are named file by file.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *why a protocol has the shape it has*, written for someone already
trained, and the Pokémon framing covers the ordering and nothing else. It is deliberately not a
protocol: no sequence of actions, no rates, no depths, no ratios, no doses, no settings, and not
something to consult while acting. Resuscitation and trauma guidance **differs between national
councils and is revised on a cycle**. The reader's own council and local protocol are the
authority; this is not, and it has had no clinical review. Nothing here describes any real person.

## Where this stands, October 2026

The Pokémon facts are pinned to source and are stable: the Emerald bracket values above are read
from `src/data/battle_moves.h`, the Quick Claw parameter and the discard of the Speed comparison
from `GetWhoStrikesFirst` in `src/battle_main.c`, and the Red and Blue special-casing from
`engine/battle/core.asm`. The *current*-generation values for Extreme Speed, Fake Out and Trick
Room are stated from working knowledge of later games rather than read from those two
decompilations, and the priority table has genuinely been revised more than once, so a reader
checking today's values should check today's game. On the clinical side, the sort-key argument is
mainstream and the specifics are not: wording, thresholds and the re-sorted sequences vary by
council and move with each revision cycle. Principle dated October 2026; read your own council's
current document for anything past the principle.
