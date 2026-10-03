---
id: "m147"
slug: prescribing-errors-as-a-system-property
style: pokemon
category: pharmacology
difficulty: intermediate
question: "Why are prescribing errors better described as a property of the system than of the prescriber, where do they cluster, and why are the clusters predictable?"
tags: [medication-safety, prescribing-errors, human-factors, system-design, transitions]
---

# The engine computes with `species` and shows you `nickname`, and nothing in the games keeps the two in step.

Every error cluster in this topic is a place where the thing on the screen and the thing in the
computation are allowed to drift apart, or a place where two entries are one character from each
other, or a place where a counter is reset and no record is kept that it existed. The Game Boy
Advance games have all three, in the data, and none of them is a bug. They are consequences of how
the structures were laid out — which is exactly the claim about prescribing error.

The Trainer here is the prescriber and the Pokémon is the medicine being prescribed. Nothing in
this answer stands in for a patient.

## The label is initialised from the identity and then left alone

```
   struct BattlePokemon, two of its fields
   ──────────────────────────────────────────────────────────────────
   0x00   species      ← EVERY calculation reads this
   ...
   0x30   nickname     ← every MESSAGE and the HP bar read this

   and in CreateBoxMon, src/pokemon.c:
       GetSpeciesName(speciesName, species);
       SetBoxMonData(boxMon, MON_DATA_NICKNAME, speciesName);
                             ──────────────────
       the label is SEEDED from the identity, once, and after that the
       two strings are independent. Nothing ever re-synchronises them.
```

That is the whole shape of a labelling error. Use the **Name Rater** and the displayed string
changes while `species` does not; nothing records what the string used to be. The identity is
intact, the label is wrong, and every routine that matters is reading the field you cannot see.
`m073` makes the adjacent point about the **Move Deleter** being free and irreversible; here the
irreversible thing is the only part a reader looks at.

**Transform** is the sharpest demonstration, and `m079` works through the copy boundary in full.
`Cmd_transformdataexecution` copies `BattlePokemon` up to `offsetof(struct BattlePokemon, pp)`,
which is `0x24`. The nickname is at `0x30`. So a **Ditto** that has Transformed into an
**Alakazam** is, to the engine, an Alakazam — species, types, moves, stat stages, ability, every
Individual Value — while the name beside the HP bar still says Ditto. Two fields, both correct in
their own terms, and one of them is the only one displayed.

## Two species, one trailing glyph

`src/data/text/species_names.h` is where the look-alike problem is written down.

```
   [SPECIES_NIDORAN_F] = _("NIDORAN♀"),        [SPECIES_NIDORAN_M] = _("NIDORAN♂"),
   [SPECIES_NIDORINA]  = _("NIDORINA"),        [SPECIES_NIDORINO]  = _("NIDORINO"),
   [SPECIES_NIDOQUEEN] = _("NIDOQUEEN"),       [SPECIES_NIDOKING]  = _("NIDOKING"),

   and the two lines sit three apart in the SAME array, in this order:
       NIDORAN♀, NIDORINA, NIDOQUEEN, NIDORAN♂, NIDORINO, NIDOKING
```

Two species names that differ in exactly one trailing character, interleaved with their own
evolution lines so that the correct and the incorrect choice are three rows apart in whatever menu
is built from the array. The downstream consequences diverge completely — **Nidoqueen** and
**Nidoking** are different Pokémon with different stats — and the thing that decides which one you
end up with is a glyph a tired reader cannot distinguish from the other glyph at the same
position.

That is not a failure of attention. It is a property of the list. And the Nido pair is not the
worst of them — the games are full of pairs built to be confusable with each other and with
nothing else, and the data shows exactly how little there is to tell them apart.

| pair | rows apart in `species_names.h` | base HP | typing | ability |
| --- | --- | --- | --- | --- |
| **Lunatone** / **Solrock** | adjacent | 70 / 70 | Rock-Psychic both | **Levitate** both |
| **Plusle** / **Minun** | adjacent | 60 / 60 | Electric both | **Plus** against **Minus** |
| **Volbeat** / **Illumise** | adjacent | 65 / 65 | Bug both | **Illuminate** against **Oblivious** |
| **Silcoon** / **Cascoon** | two apart | 50 / 50 | Bug both | **Shed Skin** both |
| **Nidoran♀** / **Nidoran♂** | three apart | 55 / 46 | Poison both | **Poison Point** both |

Read the **Lunatone** and **Solrock** row and then try to say which one you selected. Same maximum
HP, same two types, same ability, adjacent entries, and names of the same length. Nothing in the
data you can see distinguishes them, which is the situation a prescriber is in when two products
differ by a syllable and a strength.

**Silcoon** and **Cascoon** are worse again: identical on every field in that table, and they
evolve into **Beautifly**, a Bug-Flying with **Swarm**, and **Dustox**, a Bug-Poison with **Shield
Dust**. The two things you cannot tell apart become two things that are not remotely alike. The
structural answer is never "look harder". It is to change how the list is presented.

## Two species, one hidden digit

```
   src/pokemon.c, GetEvolutionTargetSpecies -- the Wurmple branch
   ──────────────────────────────────────────────────────────────────────────
   case EVO_LEVEL_SILCOON:
       if (param <= level && (upperPersonality % 10) <= 4)   → SILCOON
   case EVO_LEVEL_CASCOON:
       if (param <= level && (upperPersonality % 10) >  4)   → CASCOON

   upperPersonality = personality >> 16.  One decimal digit of a 32-bit word
   drawn once by Random32(), displayed nowhere, decides which of two
   near-identical cocoons a WURMPLE becomes -- and therefore whether the adult
   is a BEAUTIFLY or a DUSTOX.
```

**Silcoon** and **Cascoon** are the look-alike pair whose difference is not even on the label: one
hidden digit, no display, and two outcomes that then diverge all the way to **Beautifly** and
**Dustox**. `m077` uses the same `personality` word as a genotype. Here it is the two-strengths
problem: the box, the name and the sprite are nearly the same, the consequence is not, and the
field that decides is one nobody can read at the point of choosing.

## One character in a denominator

The games keep the twofold arithmetic error in two files, four lines apart in effect.

```
   src/battle_util.c, the end-of-turn ticks
   ──────────────────────────────────────────────────────────────────────────
   HOLD_EFFECT_LEFTOVERS          gBattleMoveDamage = maxHP / 16;
                                  if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;

   STATUS1_POISON                 gBattleMoveDamage = maxHP /  8;
                                  if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;
   ──────────────────────────────────────────────────────────────────────────
   Same expression. Same guard. Same variable. One character different, and the
   sign of the whole thing is set elsewhere by  gBattleMoveDamage *= -1.
```

This is `m005`'s and `m002`'s **Leftovers** denominator standing next to `m024`'s and `m054`'s
poison denominator, and the point of putting them side by side is that the difference between a
gain and a loss of twice the size is one keystroke in one expression, with no redundancy anywhere
to catch it. A decimal point is the same object: one character, a factor of ten, and nothing in
the notation to tell a reader which was meant.

Note the shared guard. Both floor at 1, so against a **Shedinja** — one maximum HP, the species
`m006` and `m041` both reach for — the two expressions produce **the same number**. The arithmetic
error is invisible in precisely the case where the margin is smallest, which is the worst possible
place for an error to be undetectable.

## Eight causes, one greyed-out slot

```
   CheckMoveLimitations(battler, unusableMoves, check), src/battle_util.c
   ──────────────────────────────────────────────────────────────────────────
     for each of the four slots:
         empty slot          →  unusableMoves |= gBitTable[i]
         zero PP             →  unusableMoves |= gBitTable[i]
         Disable             →  unusableMoves |= gBitTable[i]
         Torment             →  unusableMoves |= gBitTable[i]
         Taunt               →  unusableMoves |= gBitTable[i]
         Imprison            →  unusableMoves |= gBitTable[i]
         Encore              →  unusableMoves |= gBitTable[i]
         the Choice lock     →  unusableMoves |= gBitTable[i]

     and then:
         if (unusable == ALL_MOVES_MASK) → noValidMoves → Struggle
```

Eight ORed conditions, read from six different stores, one of them on the other side of the field
through `GetImprisonedMovesCount`. All eight write **the same bit**. The screen shows a greyed-out
slot and there is no field anywhere that records which of the eight greyed it.

That is the omission cluster. Nothing happened; there is no artefact; and the readout is identical
whichever cause produced it. `m071` and `m073` both use this shape — five named mechanics, one
display — and it earns a third outing here because the clinical version is the hardest error class
to audit: you cannot count what left no trace. And the endpoint of the function is worth keeping:
when every option is blocked the engine does not stop. It uses **Struggle**, which hurts the user,
because the rules require an action. A system that forces an action when every correct action is
unavailable produces the forced-workaround error, and `m045`'s point applies — the behaviour is
the structure's, not the operator's.

## Nine moves out of 354 can hurt the user, and they are a list you can hold in your head

The serious half's claim that a short, stable list of drug groups accounts for most serious harm
has an exact counterpart in the move data, and it is countable.

```
   src/data/battle_moves.h -- every move whose use can damage its own user

   EFFECT_RECOIL            Take Down      power  90
                            Submission     power  80
                            Struggle       power  50

   EFFECT_DOUBLE_EDGE       Double-Edge    power 120
                            Volt Tackle    power 120

   EFFECT_RECOIL_IF_MISS    Jump Kick      power  70
                            Hi Jump Kick   power  85

   EFFECT_EXPLOSION         Self-Destruct  power 200
                            Explosion      power 250
   ─────────────────────────────────────────────────────────────────
   Nine entries, four effect classes, out of MOVES_COUNT = 355.
```

Nine. Out of three hundred and fifty-four real moves, nine can cost the user something, and they
fall into four classes with four different cost structures: a fraction of the damage dealt, a
larger fraction of the damage dealt, a cost paid only on **failure** — the **Hi Jump Kick** case
`m008` works through — and the whole of the user's bar.

That is why a high-risk medicines list is short and why it is worth memorising rather than
deriving. The hazard is not spread thinly over the formulary; it is concentrated in a handful of
entries whose mechanism is *inherently* two-sided, and you can learn the handful. **Rock Head**
sharpens it further: the ability waives the recoil of **Take Down** and **Double-Edge** and does
**not** waive **Hi Jump Kick**'s crash damage or **Struggle**'s recoil, because the jump to the
ability check sits in one script branch and not the others. A safeguard that covers most of a
high-risk class and not all of it is more dangerous than one that covers none, because it teaches
the wrong rule. `m008` establishes that device and this is the error-cluster reading of it.

## The interruption that does not pause

```
   void CancelMultiTurnMoves(u8 battler)
   ──────────────────────────────────────────────────────────────────────
       status2  &= ~STATUS2_MULTIPLETURNS;
       status2  &= ~STATUS2_LOCK_CONFUSE;
       status2  &= ~STATUS2_UPROAR;
       status2  &= ~STATUS2_BIDE;
       gStatuses3 &= ~STATUS3_SEMI_INVULNERABLE;
       rolloutTimer      = 0;
       furyCutterCounter = 0;
```

Seven pieces of accumulated state, discarded in one call, and **zeroed rather than suspended**.
`m071` works through what that does to **Rollout**, whose doubling schedule runs 30, 60, 120, 240,
480: an interruption at the fourth hit does not cost you a turn, it costs you the whole ramp, and
the counter afterwards says zero, which is indistinguishable from never having started.

An interrupted prescribing task behaves the same way. The person resuming it is not resuming; they
are starting again from a state that has no memory of how far they had got, and the record cannot
distinguish "not yet done" from "was being done". `m074`'s point about the night handover is the
same mechanism with a worse clock.

## The handover: this is m002's device, doing this job

Admission and discharge are the densest cluster, and the right device is already in the corpus, so
it is reused rather than reinvented. `m002` establishes the **traded Pokémon**: the record arrives
complete — species, moves, Individual Values, the original Trainer's name and id, every byte of it
— and what does not arrive is the history with *you*. The obedience check is the sharp end, and it
is badge-gated by level: a traded Pokémon above the level your badges cover will ignore an
instruction, and the game's own data decides when.

For this answer the load-bearing half is `otId` and `otName` sitting at `0x54` and `0x3C` of
`BattlePokemon` while the thing that decides obedience is read from the badge flags, which are
somewhere else entirely. The list is complete and the authority over it is distributed. A
medication list rebuilt at a transition from several sources that each hold part of the truth
produces omissions for the same reason, and the named answer — a reconciliation task with an owner
— is the equivalent of making one routine responsible for the whole struct.

## And here the game has nothing, which is worth saying

The single most important thing about electronic prescribing is alert fatigue: a system that
interrupts for every theoretically possible interaction trains its users to dismiss interruptions,
and then the one that mattered is dismissed with the rest.

**Nothing in Pokémon models this.** Every message the battle engine prints is a *consequence* — it
already happened, and you are being told. There is no mechanic anywhere in the Advance games that
warns you before committing to something, which means there is nothing to over-warn with and no
habituation to model. The nearest candidates are not close: the confirmation prompt before using
an item is not a risk assessment, and the type chart is `m083`'s point about information that
exists in the cartridge and is never surfaced at all — the opposite failure.

Saying the game has nothing here is more useful than building a strained device for it, and it is
the honest shape of the gap: the games have no predictive warnings because they have no model of a
prescriber who could have known. That absence is itself the reason the mapping stops.

## Where the metaphor stops

Everything above is about structures and displays. Three things about medication error are about
people, and they are said here without analogy.

**At the end of a preventable medication error there is a person who was harmed, and that is why
any of this matters.** The systems vocabulary is a tool for preventing that, not a way of making
it abstract. Where harm has occurred the duty in most jurisdictions is explicit: tell the person
what happened, say plainly that it should not have, explain what is being done about it, and
record it. Being open about an error is not what ends a career. Concealment is, and it also
destroys the only information that would have prevented the next one.

**An inaccurate record causes durable harm of its own.** The clearest case is an allergy label
applied to what was an intolerance or an unrelated rash: it follows a person for life, removes
first-line options from every future prescriber, and the documented consequences include worse
outcomes from the alternatives used instead. Recording accurately — what happened, when, and how —
is a clinical act with a very long tail. `m010` holds the reaction classification that makes an
accurate record possible.

**Blame removes information.** A culture that treats error as a character failing produces fewer
reports rather than fewer errors, and the reports it does produce are only the ones that could not
be hidden. The alternative is not an absence of accountability: a just culture distinguishes human
error from at-risk behaviour from genuinely reckless choice and responds differently to each.
Staff involved in a serious error also need support, which is a practical requirement rather than
a kindness, because an unsupported person makes the next one. No mechanic in any Pokémon game
should be asked to carry that, and none here is.

Nothing in this pair indicates what anyone should take, start or stop, and no prescribing decision
should be made from it.

## What a Gym Leader is listening for

* Which field does the engine compute with, which one does it display, and what seeds the second
  from the first?
* Why is a Transformed **Ditto** the cleanest demonstration of a labelling error in the games?
* **Nidoran♀** and **Nidoran♂**: how many characters apart, how many rows apart, and why is "look
  harder" not the fix?
* Which digit of which word decides **Silcoon** against **Cascoon**, and where is it displayed?
* Write out the Leftovers tick and the poison tick. What is the difference, and why does it vanish
  against a **Shedinja**?
* `CheckMoveLimitations` has eight conditions and one output bit. What error class is that, and
  why is it the hardest to audit?
* What exactly does `CancelMultiTurnMoves` discard, and why is zeroed worse than suspended?
* Name the thing the games cannot model here, and say why the absence is the point.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer, and to its technical twin:

* **Your own institution's medicines policy and incident-reporting procedure.** Everything about
  what is actually required where you work — second checks, high-risk drug lists, who owns
  reconciliation, whether a verbal order is permitted — is in the local document, and that is what
  you will be held to.
* **Your national patient-safety body's medication-safety alerts**, including its list of
  error-prone abbreviations and its guidance on injectable medicines. The body and the list are
  both national.
* **The world health organization's global patient safety challenge on medication safety**, for
  the high-risk situations framing and the transitions-of-care material.
* **The prescribing competency framework used where you train**, for what a complete prescription
  must contain.
* **A current human-factors or patient-safety textbook**, for the slip, mistake and violation
  classification, the active-failure and latent-condition model, and the hierarchy of intervention
  effectiveness.
* **The primary literature**, for any figure about error rates, interception rates or alert
  override rates. Neither half of this pair states one, because they vary enormously with the
  setting and with how the study counted.

The Pokémon figures are a different matter and were read directly from the public decompilation of
the Game Boy Advance games rather than recalled: the `struct BattlePokemon` field offsets with
`species` at `0x00`, `nickname` at `0x30`, `otName` at `0x3C` and `otId` at `0x54`; `CreateBoxMon`
calling `GetSpeciesName` and writing the result into `MON_DATA_NICKNAME`;
`Cmd_transformdataexecution` copying up to `offsetof(struct BattlePokemon, pp)` = `0x24`, which is
the boundary `m079` works through; the `species_names.h` entries for the six Nido-line species in
array order, with `NIDORAN♀` and `NIDORAN♂` differing in the final character; the
`EVO_LEVEL_SILCOON` and `EVO_LEVEL_CASCOON` branches of `GetEvolutionTargetSpecies` testing
`(upperPersonality % 10)` against 4; the `HOLD_EFFECT_LEFTOVERS` tick at `maxHP / 16` and the
`STATUS1_POISON` tick at `maxHP / 8`, both with the `== 0 → 1` guard, in `src/battle_util.c`;
`CheckMoveLimitations`' eight ORed conditions and the `ALL_MOVES_MASK` branch to `noValidMoves`;
and `CancelMultiTurnMoves` clearing four `status2` bits, `STATUS3_SEMI_INVULNERABLE`,
`rolloutTimer` and `furyCutterCounter`; the confusable-pairs table's base HP, typings and
abilities for Lunatone, Solrock, Plusle, Minun, Volbeat, Illumise, Silcoon, Cascoon, Beautifly,
Dustox and both Nidoran, read from `src/data/pokemon/species_info.h` with the array positions from
`species_names.h`; and every move in the game whose use can damage its own user, found by
filtering `src/data/battle_moves.h` on effect — `EFFECT_RECOIL` for Take Down, Submission and
Struggle, `EFFECT_DOUBLE_EDGE` for Double-Edge and Volt Tackle, `EFFECT_RECOIL_IF_MISS` for Jump
Kick and Hi Jump Kick, and `EFFECT_EXPLOSION` for Self-Destruct and Explosion — nine entries, with
`MOVES_COUNT` 355 from `include/constants/moves.h`. The Rock Head ordering is from
`data/battle_scripts_1.s`, where `jumpifmove MOVE_STRUGGLE` precedes the ability check and
`ABILITY_ROCK_HEAD` appears exactly once in the file. Rollout's 30/60/120/240/480 schedule and the
traded-Pokémon obedience rule are `m071`'s and `m002`'s, verified there, and the Take Down and
Double-Edge recoil ratios are `m008`'s. Shedinja's single maximum HP is `m006`'s.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in this pair are the Pokémon ones.** Neither half
gives an error rate, an interception rate, a dose, a high-risk threshold or an override figure:
those are properties of particular settings and particular studies. The high-risk drug groups the
serious half names are a widely used framing, not an authoritative list; the list that applies
where you work is in your local policy. Nothing here indicates what anyone should take, start or
stop, and a concern about a specific medicine in a specific person belongs with their prescriber
or pharmacist.

## Where this stands, October 2026

The mechanisms — a label that drifts from an identity, a list whose entries are one character
apart, a counter that is zeroed rather than paused, a readout with eight possible causes — are
mechanism and do not date, and the game mechanics quoted are fixed in released software, pinned to
the Game Boy Advance games. The clinical scaffolding dates. **What counts as a reportable
incident** and who investigates it is national and is revised. **Error-prone abbreviation lists
and high-risk drug lists** are maintained documents that change. **Electronic prescribing** is the
fastest-moving part: the new error types depend on the product and its local configuration,
decision support is being rebuilt around automated and predictive components whose own failure
modes are not yet well characterised, and anything written now about alert design will date
quickly. Check your institution's current policy and your national patient-safety body.
