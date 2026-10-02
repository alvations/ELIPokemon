---
id: "m073"
slug: documentation-and-pertinent-negatives
style: pokemon
category: nursing
difficulty: core
question: "Why is the clinical record treated as an instrument other people act on, and what makes a pertinent negative worth writing down?"
tags: [documentation, record-keeping, pertinent-negative, continuity, audit]
---

# A flag is one bit, and one bit cannot hold the difference between "no" and "nobody asked".

The Advance games store the whole history of a save in two different ways, and the difference
between them is the entire argument of this answer. `FlagGet` reads a single bit out of a byte
array:

```
   bool8 FlagGet(u16 id)
   {
       u8 *ptr = GetFlagPointer(id);
       if (!ptr)
           return FALSE;                       ◄── here
       if (!(((*ptr) >> (id & 7)) & 1))
           return FALSE;
       return TRUE;
   }
   ──────────────────────────────────────────────────────────────────────────────────────
   Read that marked line again. An id that does not resolve to anything at all —
   a lookup that FAILED — returns exactly the same value as a flag that is
   genuinely clear. Two completely different situations, one answer, and the
   caller cannot tell which it got.
```

`VarGet`, sitting a few dozen lines above it in the same file, handles the identical failure
differently: with no valid pointer it returns the **id itself**, a value the caller can notice is
wrong. One storage class fails quietly into "no". The other fails loudly into nonsense. The quiet
one is the one the whole game is built on, and it is also the shape of a blank in a chart.

## Four states, three entries

```
   what happened in the save                      what a reader of the save can tell
   ─────────────────────────────────────────────  ──────────────────────────────────────
   the event happened; the flag was set           TRUE. Unambiguous.
   the event did not happen; the flag is clear     FALSE
   the event happened but nothing set a flag       FALSE
   the id was never valid; nothing exists at all   FALSE
   ──────────────────────────────────────────────────────────────────────────────────────
   FOUR states, THREE of them returning FALSE, and nothing in the save distinguishes
   them. The header makes the scale of it visible: of the 1,545 names beginning
   FLAG_ in Emerald's flag header, 394 carry the comment "Unused Flag". Several
   hundred bits of storage that nothing ever writes, every one of them reading
   FALSE forever, indistinguishable from a bit that means something and is off.
```

## The engine's own fix is a second array, and it is exactly the clinical fix

The **Pokédex** is the one place in the save that refuses to let one bit do two jobs. `struct
Pokedex` holds **two** separate bit arrays — `owned` at offset 0x10 and `seen` at 0x44, fifty-two
bytes each — because *encountered* and *confirmed* are different claims and the game's designers
were not willing to conflate them. m037 builds the sepsis-suspicion argument on exactly that pair;
here it is the documentation argument. **When one bit is not enough, the answer is a second field,
not a more careful reader.**

Two further details in the same struct are worth having:

```
   field                 the comment in the header          what it means for a record
   ────────────────────  ─────────────────────────────────  ──────────────────────────────
   unownPersonality      "set when you first see Unown"     the FIRST observation, kept
   spindaPersonality     "set when you first see Spinda"    forever, never updated
   ────────────────────────────────────────────────────────────────────────────────────────
   Every Unown after the first, every Spinda after the first — and Spinda's spots are
   per-individual, which is m016's whole point — writes nothing. The record holds the
   earliest thing you saw and has no room for the series. A chart that records an
   admission observation and nothing since has the same defect.
```

## The write is conditional on context, and nobody is told when it is skipped

Here is the part that is genuinely unsettling. `Cmd_switchinanim` is where a wild or opposing
creature gets recorded as seen, and the call is guarded:

```
   HandleSetPokedexFlag(... FLAG_SET_SEEN ...) runs only when BOTH hold:
     * the battler is on the OPPONENT's side, and
     * the battle type is NOT any of: link, e-reader trainer, recorded link,
       Trainer Hill, Battle Frontier
   ────────────────────────────────────────────────────────────────────────────────────
   Five battle types in which you can face something, fight it, win, and have
   nothing whatsoever written down. No message says so. The battle happened. The
   record of it is a flag that reads FALSE, and FALSE is also what it would read
   if the battle had never taken place.
```

That is the structure of an undocumented escalation, and it is why the record of *who was told* is
the entry worth guarding most. The event is real. The trace is absent. And nothing distinguishes
an absent trace from an absent event.

The same shape runs through the battle engine: an opposing Ability is written into the record
**only when it fires**, which is the device m055 is built on. **Zoroark**'s Illusion is the
limiting case m037 names — a record that is not merely missing but confidently wrong.

## What can be recovered later, and what the recovery is actually reading

The games have a clean experiment on this, and it is a pair of named services in two named towns.

**The Move Deleter** in **Lilycove City** is free, immediate and irreversible.
`MoveDeleterForgetMove` has exactly **one** guard in front of it: `IsLastMonThatKnowsSurf`, which
refuses when this is your last **Surf**. One hand-written special case, for the one deletion that
would strand the player, and nothing at all protecting anything else.

**The Move Reminder** in **Fallarbor Town** — the Move Tutor, in his own text — is the recovery,
and it costs one **Heart Scale** per move. The crucial fact is *where his list comes from*.
`GetMoveRelearnerMoves` reads `gLevelUpLearnsets[species]`: every move the **species** learns at
or below this level, minus the four it currently knows. It does not read any record of what this
individual ever knew, because no such record exists.

```
   how the move was learned     deleted by the Move Deleter     can the Move Reminder restore it?
   ───────────────────────────  ──────────────────────────────  ────────────────────────────────
   by levelling up              yes, instantly                  YES — it is in the species table
   from a TM                     yes, instantly                  NO
   as an Egg Move                yes, instantly                  NO
   from a one-off Move Tutor     yes, instantly                  NO
   ─────────────────────────────────────────────────────────────────────────────────────────────
   What you can reconstruct afterwards is what the species table PREDICTS, not what
   actually happened. Everything particular to this individual — the part that was
   worth writing down precisely because it was not predictable — is gone.
```

And the games have the opposite extreme too. **Sketch** has a PP of **1**. **Smeargle** uses it
once, `Cmd_copymovepermanently` writes the result into the move slot, and that write survives the
battle, the box and the save. One entry, made once, permanent. Both extremes are in the same
cartridge: the irreversible write and the irrecoverable deletion, with nothing in between except
the one special case for **Surf**.

## Where the metaphor stops

A save file is a fair model of an ambiguous blank, and nothing above is a person.

Documentation is the part of the job most often done tired, last, and after the thing that needed
doing. It is also the part that reaches furthest: an entry written in four minutes is read by
people who will never meet the writer, for years, sometimes in circumstances nobody anticipated.

Records are read by patients and by families, increasingly as a right of access, and the words in
them land. A phrase like "poor historian" or "refused care" carries a judgement that travels with
someone through every later encounter, and writing what was observed rather than what was
concluded about the person is a kindness as well as a professional standard.

And the record is often the only trace a patient leaves of having tried to raise something.
"Daughter concerned that he is not himself" is an entry that has changed outcomes. Its absence is
not neutral — it removes the one piece of evidence that somebody noticed early.

The context has to be said too. Documentation quality is substantially a function of time,
staffing and whether the system is usable. An institution that answers a records failure by asking
individuals to document better, while changing none of those three, has identified the wrong
variable.

## What Nurse Joy is listening for

Why `FlagGet` returning FALSE on a failed lookup is the same defect as a blank box. Which of the
four states collapse, and what writing the negative actually buys. Why the **Pokédex** needs two
arrays and what the clinical equivalent of the second one is. Why `unownPersonality` holds only
the first **Unown**. Which five battle types record nothing, and what the ward equivalent of an
unrecorded battle is. Why the **Move Reminder** can restore a levelling move and not a **TM** one,
and what that says about reconstructing a shift from memory. And which single entry, if only one
could be guaranteed, is the one worth having — because in this answer's reading it is who was
told.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to this
answer:

* The reader's own professional regulator's standards on record keeping — the document that binds
  them personally, and the one this answer is least able to substitute for.
* The reader's institutional record-keeping policy, including retrospective entries, corrections,
  countersigning and the locally prohibited abbreviations list.
* The reader's national guidance on information governance and on patient access to records, for
  the access point in the plain-prose section.
* A current textbook or professional-body publication on clinical documentation, for the elements
  of an entry and for the pertinent-negative concept.
* The published literature on electronic health record safety, for copy-forward, alert fatigue and
  mandatory-field defects.
* The reader's legal jurisdiction's position on the evidential status of clinical records, which
  is law and differs profoundly between countries.

Separately, and unlike the above: the body of `FlagGet` and the return of `VarGet` on a failed
lookup, the count of 1,545 names beginning `FLAG_` and the 394 carrying the "Unused Flag" comment,
the two **Pokédex** bit arrays with their offsets and sizes, the `unownPersonality` and
`spindaPersonality` comments, the guard on the seen-flag call in `Cmd_switchinanim` and the five
excluded battle types, the **Move Deleter**'s single `IsLastMonThatKnowsSurf` exception,
`GetMoveRelearnerMoves` reading the species level-up table, the **Heart Scale** price, and
**Sketch**'s PP of 1 were all read directly out of the public disassemblies of the games, which
this environment could reach. The flag and variable counts are counts of lines in the header as it
stands in that disassembly, not figures published anywhere.

## Scope and safety

This explains what the clinical record is for and what follows for how it is written, for someone
already training in or qualified for clinical practice. It is not a documentation standard, not a
template and not legal advice, and it deliberately states no rule about retrospective entries,
corrections, abbreviations or countersigning — all of which are set by the reader's regulator and
institution, which are the authority. The only numbers in it belong to a video game. Nothing here
has had clinical or legal review, none of it is for use in an emergency or for a decision about
any person's care, and nothing in it should be relied on in a complaint, an investigation or any
legal process. If someone is unwell right now, the local emergency number is the correct response.

## Where this stands, October 2026

The argument is structural and does not date: a record read by somebody who was not there, and a
blank that cannot separate "not asked" from "asked and negative", are properties of records rather
than of any era's policy. What dates is the procedural and legal layer — regulator standards,
prohibited abbreviations, retrospective entry rules, correction mechanics — and, faster than that,
the technology layer: patient access, automated and ambient documentation, and the handling of
machine-generated entries are all moving quickly and in different directions in different
countries. The reader's regulator and institution are the authority throughout. The save-file
facts above are pinned to the Advance-generation disassembly and no claim is made about any other
generation.
