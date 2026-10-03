---
id: "m127"
slug: fever-when-immunity-is-compromised
style: pokemon
category: emergency
difficulty: advanced
question: "Why do the usual thresholds for fever stop applying when someone's immune system is compromised, and what replaces them?"
tags: [fever, immunocompromise, thresholds, empirical-therapy, revision]
---

# Shield Dust deletes the secondary effect and prints nothing, and the damage has already landed

`SetMoveEffect` runs **after** the damage is applied. By the time it is reached, HP has gone. Its
first job is to decide whether the move's secondary effect happens, and its first test is this:

```
   if (gBattleMons[gEffectBattler].ability == ABILITY_SHIELD_DUST
       && !(gHitMarker & HITMARKER_STATUS_ABILITY_EFFECT)
       && !primary
       && gBattleCommunication[MOVE_EFFECT_BYTE] <= 9)
       INCREMENT_RESET_RETURN
```

And `INCREMENT_RESET_RETURN` is three statements:

```
   gBattlescriptCurrInstr++;
   gBattleCommunication[MOVE_EFFECT_BYTE] = 0;
   return;
```

No string. No animation. No flag set anywhere that anything later reads. The instruction pointer
advances, the pending effect is zeroed, and the function returns. **Shield Dust is the only
protection in this engine that works and leaves no evidence whatsoever that it worked.** Compare
`BattleScript_SafeguardProtected`, immediately below it in the same chain, which prints — question
m103 makes the point that that string is the *only* evidence Safeguard ever did anything, and
Shield Dust is the case with no string at all.

The clinical shape is in that asymmetry. The hit did full damage. The paralysis, the burn, the
flinch — the *secondary readout the defender would have produced* — is gone, silently. A player
watching the screen sees a normal amount of damage and nothing else, and concludes correctly that
nothing extra happened and incorrectly that nothing extra was attempted.

## The secondary's size is a property of the pairing, not of the move

`Cmd_seteffectwithchance` is the other end of the same wire:

```
   if (gBattleMons[gBattlerAttacker].ability == ABILITY_SERENE_GRACE)
       percentChance = gBattleMoves[gCurrentMove].secondaryEffectChance * 2;
   else
       percentChance = gBattleMoves[gCurrentMove].secondaryEffectChance;
```

So the printed number on the move is a base rate that gets multiplied by a property of **whoever
is holding the move**, and then the result is tested against a roll. Serene Grace doubles it;
Shield Dust on the far side takes it to zero. The same move entry, the same
`secondaryEffectChance` field, three completely different observed frequencies depending on a pair
of abilities neither of which is on the move.

And there is a third branch above both: `MOVE_EFFECT_CERTAIN` skips the chance test entirely.
Where the effect is marked certain, the roll is not performed, and the magnitude of the readout
stops being a probabilistic statement at all.

Shield Dust is also written **twice**, in two different places, for two different jobs. The site
above is in `SetMoveEffect`. The second is inside `ChangeStatBuffs`:

```
   else if (gBattleMons[gActiveBattler].ability == ABILITY_SHIELD_DUST && flags == 0)
       return STAT_CHANGE_DIDNT_WORK;
```

One ability, two hand-written check sites, two different return paths. Nothing in the engine
composes them; each had to be put there by somebody who thought of that case.

## One defect, one route — and not even all of that route

`ABILITYEFFECT_ABSORBING` is the whole of the engine's type-specific immunity machinery in the
third generation, and it has exactly three cases:

```
   case ABILITY_VOLT_ABSORB:   if (moveType == TYPE_ELECTRIC && gBattleMoves[move].power != 0)  -> drain
   case ABILITY_WATER_ABSORB:  if (moveType == TYPE_WATER    && gBattleMoves[move].power != 0)  -> drain
   case ABILITY_FLASH_FIRE:    if (moveType == TYPE_FIRE     && !(status1 & STATUS1_FREEZE))    -> boost
```

Three one-line comparisons. Jolteon has Volt Absorb and nothing else; Vaporeon has Water Absorb
and nothing else; Flareon has Flash Fire and nothing else. Lanturn carries Volt Absorb beside
Illuminate, and Quagsire carries Water Absorb as its second ability behind Damp. Each of those
covers **one type**, and the question *is this Pokémon protected* has no answer until you say
protected from what.

Two details in those three lines are the whole argument.

**`power != 0` means the cover is partial even within its own type.** Volt Absorb absorbs
Thunderbolt and does nothing at all about Thunder Wave, because Thunder Wave's `power` field is
zero. Jolteon is immune to the damaging half of Electric and wide open to the half that sets a
status. The defect-to-route mapping is not just type-specific; it is specific to a subset of a
type, defined by a field that has nothing to do with the type.

**Flash Fire has a second condition that is about something else entirely.** `!(status1 &
STATUS1_FREEZE)` — a frozen Flareon loses its Fire immunity, because the branch that would grant
it is gated on an unrelated status. A cover that fails when another condition is also present is
not a cover you can reason about one condition at a time.

That is the Part I convention from m007 and m031 — type effectiveness as a **zero** and not as a
reduction — used here for the opposite reading. There the point was that no amount of repetition
gets past a zero. Here the point is that each zero is one entry in a table, and knowing that some
entry is zero tells you nothing about any other.

## A route encoded as a list fails differently from one encoded as a test

Soundproof is the comparison case, and it is not in `ABILITYEFFECT_ABSORBING` at all. It is in
`ABILITYEFFECT_MOVES_BLOCK`, and it works by walking a table:

```
   static const u16 sSoundMovesTable[] =
   {
       MOVE_GROWL, MOVE_ROAR, MOVE_SING, MOVE_SUPERSONIC, MOVE_SCREECH, MOVE_SNORE,
       MOVE_UPROAR, MOVE_METAL_SOUND, MOVE_GRASS_WHISTLE, MOVE_HYPER_VOICE, SOUND_MOVES_END
   };
```

Ten moves and a sentinel, maintained by hand. Volt Absorb asks a question about the move — *what
is your type* — and gets a correct answer about any move ever added. Soundproof consults a list,
and the eleventh audible move is not on it. Question m075 reads this table for exactly that
property. A defence defined by a *property of the threat* and a defence defined by an *enumeration
of known threats* behave identically right up to the point where something new arrives.

## Breadth is a bitmask in one byte

The engine's own distinction between a targeted treatment and an empirical one is six bytes long.
`src/data/pokemon/item_effects.h`:

```
   const u8 gItemEffect_Antidote[6]  = { [3] = ITEM3_POISON };                  // 0x10 — one bit
   const u8 gItemEffect_BurnHeal[6]  = { [3] = ITEM3_BURN };                    // 0x08 — one bit
   const u8 gItemEffect_FullHeal[6]  = { [3] = ITEM3_STATUS_ALL };              // six bits
   const u8 gItemEffect_FullRestore[7] = { [3] = ITEM3_STATUS_ALL,
                                           [4] = ITEM4_HEAL_HP,
                                           [6] = ITEM6_HEAL_HP_FULL };
```

`ITEM3_STATUS_ALL` is `CONFUSION | PARALYSIS | FREEZE | BURN | POISON | SLEEP`. Same array, same
index, same mechanism — the only difference between the narrow item and the broad one is **how
many bits are set in byte 3**.

And that is the point about empirical cover stated as cleanly as it can be stated. Antidote
requires you to already know the answer: used against a burn it does nothing, because `0x10 &
0x08` is zero. Full Heal requires you to know nothing at all, and it is *not a better item* — it
is a wider mask on the same byte, bought by not needing the diagnosis first. Question m003 in
nursing established this trio for safe administration; this is the same three items read for
breadth rather than for specificity, and the reading is the opposite one: there, Antidote's
narrowness is the hazard, and here it is Full Heal's width that is the deliberate purchase.

Note also what Full Restore does that Full Heal does not: it writes bytes 4 and 6 as well. Breadth
in one dimension and depth in another are separate fields, and an item can have one without the
other.

## The mapping this answer refuses

The obvious device for a compromised host is Wonder Guard, and the obvious species is Shedinja —
one maximum HP, immune to everything that is not super-effective, ended by a single point of
anything. It is the best-fitting mechanic in the game and it is not available here, because every
version of it requires a Pokémon to *be* the patient whose defences are the subject.
`../SAFETY.md` forbids that outright and `CONVENTIONS.md` Part III records a previous writer
reaching for the same mapping, seeing the same problem and writing something else. Shedinja
remains available for a type-override point with nobody attached, which is how question m047 uses
it. It is not available for this.

So this answer is built entirely out of **check sites**: where a test is written, how wide its
mask is, whether it consults a property or a list, and whether it leaves a record. Nothing in it
is a creature with an illness. That is a narrower device than Wonder Guard would have been and it
costs some of the force of the analogy, which is the correct trade.

## Where the metaphor stops

Plain prose from here, with no game in it, because the subject is somebody who may be seriously
unwell while looking well.

The ordinary reasoning about fever contains an unexamined link: that a higher temperature means a
bigger insult and a normal one means a small or absent insult. **The temperature is produced by
the host, not by the organism** (**mechanism**), so every inference from its magnitude is an
inference about the host's capacity to mount it.

Two things change together in someone immunocompromised, and they pull opposite ways. The signal
gets weaker — fever may be blunted or absent, and the localising signs that normally point at a
site are substantially made of the cells that are missing, so pus, a convincing film and an
impressive examination can all be absent from an established infection. (**Mechanism.**)
Corticosteroids and other immunosuppressants attenuate the febrile response itself, so the
treatment that created the vulnerability also suppresses the sign of its consequence.
(**Consensus.**) Meanwhile the consequence gets worse and faster. A threshold is a function of how
much a signal shifts the probability and of what the two errors cost, so when both terms move the
same way the threshold moves twice in that direction: a weaker signal is acted on, and acted on
sooner. (**Mechanism.**) The replacement for the missing number is a wider set of admissible
signals — hypothermia rather than fever, isolated new hypotension, unexplained tachycardia, new
confusion, rigors without a recorded temperature, or a carer's report that the person is not
themselves. (**Consensus.**)

"Immunocompromised" is not one state, and the useful question is which component is missing,
because each defends a different class. Impaired neutrophil number or function opens gut and skin
flora, with invasive fungal disease becoming relevant as the duration lengthens. Impaired
cell-mediated immunity opens intracellular bacteria, mycobacteria, some fungi and reactivating
latent viruses. Impaired antibody or complement, and an absent or non-functioning spleen, open
encapsulated bacteria with a course that can escalate very fast. A breached barrier — mucositis,
vascular access, a catheter, a wound — opens whatever is colonising that barrier, which is why the
device is part of the history. And recent antimicrobials, recent hospitalisation or known
colonisation shift both the spectrum and the resistance. (**Consensus** as a broad pattern; local
epidemiology and resistance are (**country-dependent**).) The defects combine in the same person
on the same day, and the history — which agent, how long ago, which device, which previous
organism — is frequently held in a record the assessing clinician cannot see.

The decision structure that follows is *empirical now or targeted later*, and later is after the
harm, because the test that names the organism takes longer than the window in which treatment
changes the outcome. (**Mechanism.**) Cultures are taken first and must not delay treatment,
because the specimens are what make narrowing possible afterwards. Broad cover is a statement
about uncertainty rather than about severity, its width is set by the defect and by local
resistance (**country-dependent**), and narrowing is part of the plan rather than an afterthought
— the collective-action problem that makes narrowing hard is question m045's and it is at its
sharpest here. No temperature, cell count, time target, agent, dose or risk-stratification
instrument appears in this answer, and no criterion of any such instrument is listed, because all
of them are local and revised and because an instrument used from memory is one of the failure
modes this subject is about.

The usual failure is not bad reasoning about the temperature. It is that nobody knew the person
was immunocompromised. The structural answers are patient-held information that makes the person
the carrier of the fact, direct-access arrangements that bypass a queue calibrated for a
population whose signals mean something else, and a triage question asked of everybody rather than
of whoever looks unwell. (**Consensus** that these are the recognised responses; their names,
availability and funding are (**country-dependent**).)

And what is at stake for a person is not in any of that. The first person who has to act is
usually at home, tired, at two in the morning, deciding with a thermometer whether this is the
thing they were warned about. So the instruction has to survive being frightened — one written
sentence saying what to do and where to go is worth more than an explanation of neutrophil
kinetics, because people keep the card and not the explanation. This is also the group for whom
waiting in a waiting room is itself a harm, both for the delay and for the room, and a department
that cannot act on that should own it as its own problem rather than attach it to the person
sitting there. Being sent home five times teaches someone, correctly, that most of these episodes
resolve, which is exactly what the advice asks them to override, so treating the sixth attendance
as a nuisance is a predictable error — question m130's argument. A partner or parent saying *she
is not right* is measuring against a baseline nobody in the department has, and in a group whose
signals are blunted that is often the strongest observation available. The advice is deliberately
over-inclusive because the alternative is worse, and saying so out loud is part of making it work.

No Pokémon stands for a patient anywhere in this answer. The best-fitting mechanic in the game for
a compromised host is Wonder Guard on Shedinja, and it is refused above for exactly that reason.
What the game carries is four narrow ideas: that a suppressed secondary effect can leave no record
while the damage lands in full; that the magnitude of a readout is a property of the pairing
rather than of the event; that an immunity is one entry in a table and tells you nothing about any
other entry; and that breadth of cover is a mask rather than a strength. Fear, exhaustion, the
waiting room and the fifth journey home are stated above without ornament and are not mechanics.

## What a Gym Leader is listening for

* When does `SetMoveEffect` run relative to the damage, and what does Shield Dust therefore not
  prevent?
* What exactly does `INCREMENT_RESET_RETURN` print? Compare `BattleScript_SafeguardProtected`.
* `secondaryEffectChance` is a field on the move. Name three things that change the observed
  frequency without touching it.
* Shield Dust is written at two check sites. Name both and say what each returns.
* `ABILITYEFFECT_ABSORBING` has three cases. What does `power != 0` do to Volt Absorb against
  Thunder Wave?
* Why does a frozen Flareon lose its Fire immunity?
* Volt Absorb consults a property and Soundproof consults a list. What happens to each when a new
  move is added?
* Antidote and Full Heal differ in one respect. State it, and say what Full Heal is bought with.
* Why is Wonder Guard refused in this answer, and what is Shedinja still available for?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md), and they
apply here. Specific to this answer:

* The current national guideline on fever in a person with neutropenia, issued by **the reader's
  own national guideline body or national cancer organisation** — the document that carries the
  temperature value, the cell-count value, the time target and the stratification instrument, none
  of which appears here.
* The current empirical antimicrobial policy of **the reader's own employing organisation**, which
  is set from local resistance data and outranks any general recommendation on choice of agent.
* **The reader's national formulary**, for anything about an agent, a route or monitoring.
* A current standard textbook of **infectious diseases** and one of **haematology or oncology**,
  for the mapping between immune defect and organism class and for the physiology of the febrile
  response.
* The current guidance on an absent or non-functioning spleen issued by **the reader's national
  haematology society**, which is a separate document with separate advice.

Markers used in the plain-prose section above: (**mechanism**) (follows from physiology or the
structure of the problem and is checkable by reasoning), (**consensus**) (agreed across mainstream
sources as of writing), (**country-dependent**) (genuinely differs between countries, services or
institutions). No guideline number, document title, temperature, cell count, time target, agent,
dose or stratification instrument is given, and nothing is quoted, because none of these was
opened. The Pokémon side is in the opposite position and is sourced file by file in the closing
note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *why an inference from a sign depends on who produces the sign*,
written for someone already trained, and the Pokémon framing covers only where a check is written,
how wide its mask is, whether it consults a property or a list, and whether it leaves a record. It
is deliberately not a protocol and not a decision aid: no temperature, no cell count, no time
target, no antimicrobial agent, no dose, no risk-stratification instrument and no criterion of
one. Empirical antimicrobial choice is set locally from local resistance data and nothing general
can substitute for it. Definitions, thresholds, targets and service arrangements differ sharply
between countries and institutions. The reader's own national guidance and local policy are the
authority; this is not, and it has had no clinical review. Nothing here describes any real person.

## Where this stands, October 2026

The Pokémon facts are pinned to source and are stable. `SetMoveEffect`'s Shield Dust clause with
its `!primary` and `MOVE_EFFECT_BYTE <= 9` conditions, the Safeguard clause below it at `<= 7`,
the `INCREMENT_RESET_RETURN` macro's three statements, `Cmd_seteffectwithchance` doubling
`secondaryEffectChance` under Serene Grace and skipping the roll on `MOVE_EFFECT_CERTAIN`, and the
second Shield Dust site inside `ChangeStatBuffs` at `flags == 0` are read from
`src/battle_script_commands.c`. `ABILITYEFFECT_ABSORBING`'s three cases with their `power != 0`
and `STATUS1_FREEZE` conditions, and `sSoundMovesTable`'s ten moves and sentinel under
`ABILITYEFFECT_MOVES_BLOCK`, are from `src/battle_util.c`. Jolteon's Volt Absorb, Vaporeon's Water
Absorb, Flareon's Flash Fire, Lanturn's Volt Absorb beside Illuminate and Quagsire's Damp and
Water Absorb are from `src/data/pokemon/species_info.h`. The six-byte item effect arrays for
Antidote, Burn Heal, Full Heal and Full Restore, and `ITEM3_STATUS_ALL`'s six bits, are from
`src/data/pokemon/item_effects.h` and `include/constants/item_effects.h`. All of it is **third
generation**, read from `pokeemerald`. Later generations add abilities, change Lightning Rod from
a redirection into an immunity, and add type-absorbing abilities that do not exist here, so a
reader checking today's game should read today's game; Lightning Rod in this generation grants no
immunity at all and only redirects in a double battle. On the clinical side the mechanism is
stable and the operational detail is not: definitional temperature and cell-count values differ
between national guidelines, time-to-treatment targets are periodically re-examined,
stratification instruments and outpatient management are actively revised, empirical regimens are
rewritten as local resistance changes on a shorter cycle than guidelines are republished, and the
classification of immunosuppressive agents keeps moving as new biologics enter use. Principle
dated October 2026; read the current national guideline and the current local antimicrobial policy
for anything past the principle.
