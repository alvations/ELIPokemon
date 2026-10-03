---
id: "m139"
slug: significant-event-analysis
style: pokemon
category: general-practice
difficulty: intermediate
question: "Why is individual blame the wrong instrument after a significant event in primary care, and what has to replace it for the review to be worth doing?"
tags: [significant-event-analysis, patient-safety, human-factors, quality-improvement, hindsight-bias]
---

# The engine reads whose name to store out of a byte of the running script, and keeps it until the turn resolves

This specialty's vocabulary is filters, and this answer leaves them, because the question is not
about what arrives — it is about **the record that gets written when something happens, and who it
names**. That record exists in Generation III, it is eight bytes wide, four different mechanisms
read it for four different purposes, and the way it decides whose name to store is one of the
strangest things in the battle engine.

Read the register carefully before going on. **Nothing here stands in for a patient and nothing
here stands in for an injury to a person.** A Pokémon losing HP is not standing in for somebody
being harmed; the conventions file forbids that mapping and it stays forbidden. What is being
studied is the **attribution machinery**: which fields the engine keeps when an event occurs,
where it reads the name from, which events it declines to record at all, and how long any of it
survives. The half of the subject that is about the person affected is in the plain-prose section,
because the cartridge cannot carry it and should not be asked to.

## One block of code writes three records of the same event

```
   src/battle_script_commands.c, inside the HP-update command. Everything below
   happens at the single instant the HP is deducted.

   gHpDealt = what was ACTUALLY removed   (clamped: if hp <= damage, gHpDealt = hp)

   RECORD 1 - for Shell Bell, the item that heals its holder a fraction of damage done
      if (shellBellDmg == 0 && !(gHitMarker & HITMARKER_PASSIVE_HP_UPDATE))
            gSpecialStatuses[battler].shellBellDmg = gHpDealt;
      first write only. A second hit in the same turn does not overwrite it.

   RECORD 2 and 3 - for Counter and Mirror Coat, split on the MOVE'S TYPE
      if (IS_TYPE_PHYSICAL(moveType) && !(gHitMarker & HITMARKER_PASSIVE_HP_UPDATE)
          && gCurrentMove != MOVE_PAIN_SPLIT)
            physicalDmg = gHpDealt;
            physicalBattlerId = (gBattlescriptCurrInstr[1] == BS_TARGET)
                                   ? gBattlerAttacker      <-- THE NAME IS READ OUT
                                   : gBattlerTarget;       <-- OF THE SCRIPT BYTE
      else if (!IS_TYPE_PHYSICAL(moveType) && !(gHitMarker & PASSIVE))
            specialDmg / specialBattlerId, by the same rule

   RECORD 4 - for Bide, which is the only accumulating one
      if (!(gHitMarker & HITMARKER_IGNORE_BIDE))
            gBideDmg[battler] += gBattleMoveDamage;   <-- NOT gHpDealt
            gBideTarget[battler] = same script-byte rule

   FOUR THINGS TO NOTICE, AND EVERY ONE OF THEM MATTERS

   1  THE IDENTITY IS NOT OBSERVED, IT IS INFERRED FROM THE INSTRUCTION. The byte
      after the opcode says whose HP this command is updating; the engine reads
      that byte to decide whether the attacker or the target is the one to name.
      Change which script runs and the same event records a different name.

   2  TWO RECORDS OF ONE EVENT, WITH TWO DIFFERENT QUANTITIES. The retaliation
      store keeps gHpDealt - what was delivered. Bide's accumulator keeps
      gBattleMoveDamage - what was INTENDED, before the clamp. Against a target
      with little HP left those two numbers are not the same, and both are "the
      damage" in their own part of the engine.

   3  Pain Split IS EXCLUDED BY NAME, in the condition, as a special case.

   4  CATEGORY IS DERIVED FROM A PROXY. Generation III has no per-move damage
      class: IS_TYPE_PHYSICAL(moveType) asks about the TYPE and takes the
      answer as the category.
```

## Harms with nobody to name are not recorded at all

`HITMARKER_PASSIVE_HP_UPDATE` is the marker a script sets when HP is coming off for a reason that
is not somebody's attack, and its presence suppresses records 1 to 3 entirely.

It appears **thirteen times across the battle scripts**, set per effect by hand.
`BattleScript_DamagingWeatherLoop` — **Sandstorm** and **Hail** — sets it along with
`HITMARKER_IGNORE_BIDE`, `HITMARKER_IGNORE_SUBSTITUTE` and `HITMARKER_GRUDGE` in a single
`orword`, and clears all four when the loop ends. `BattleScript_LeechSeedTurnDrain` sets it twice,
once for each side of the transfer. **Bide**'s accumulator is suppressed differently again:
`DoBattlerEndTurnEffects` sets `HITMARKER_IGNORE_BIDE` *around the whole end-of-turn block* and
clears it afterwards, so the entire class of end-of-turn harms — poison, burn, **Leech Seed**,
**Curse**, **Nightmare** — is excluded by the caller rather than by the scripts.

The consequence is exact. **Spikes**, weather, a status condition, recoil, confusion damage, an
ability like **Rough Skin** firing on contact — none of these leaves an attacker in the store, and
most leave no amount either. So:

```
   Wobbuffet uses Counter. The engine runs Cmd_counterdamagecalculator:

      if (physicalDmg                                   <- is there a record?
          && sideAttacker != sideTarget                 <- is the named one on the
          && gBattleMons[physicalBattlerId].hp)            other side, and still here?
              gBattleMoveDamage = physicalDmg * 2;
      else
              -> BattleScript_FailedFromAtkString

   THE HARM HAPPENED. THE HP IS GONE. AND THE RETALIATION FAILS, printing the
   same generic failure string that emergency m101 found 95 jumps from 55 labels
   arriving at. A mechanism that can only act on an attributable act has nothing
   to act on when the cause was in the environment.
```

Nursing m036 put Spikes in `gSideStatuses` because the hazard belongs to the ground and whoever
laid it has gone; emergency m105 added that there is no screen indicator for it while
`STRINGID_PKMNHURTBYSPIKES` names the entrant every single time. This is the third face of the
same fact: not only is the cause stored where nothing displays it and the effect announced against
whoever walked in, but the engine's one mechanism for assigning consequence **cannot see
environmental causes at all**. It is not that it blames the wrong party. It is that an
unattributable harm is, to that mechanism, not an event.

## And when there is a name, it can be redirected to whoever drew attention

This is the part worth carrying out of the whole answer, and it is four lines of C.

```
   Cmd_counterdamagecalculator, after the three conditions pass:

      if (gSideTimers[sideTarget].followmeTimer
          && gBattleMons[gSideTimers[sideTarget].followmeTarget].hp)
               gBattlerTarget = gSideTimers[sideTarget].followmeTarget;
      else
               gBattlerTarget = gProtectStructs[gBattlerAttacker].physicalBattlerId;

   Cmd_mirrorcoatdamagecalculator is, in the source's own words, "a copy of Cmd
   with the physical -> special field changes", and it carries the identical clause.

   SO: the record correctly holds who did it. The consequence goes to whoever used
   Follow Me. The recorded name is checked SECOND, and only if nobody on that side
   put their hand up.
```

The store is accurate. The attribution is accurate. And the thing that actually lands, lands on
the visible one. No defect is involved anywhere — every line is behaving as designed, and the
designed behaviour is that drawing attention is sufficient to receive what was aimed at somebody
else.

## One store, four readers, four different questions

```
   READER                       READS                         ASKS
   ──────────────────────────── ───────────────────────────── ─────────────────────────────
   Counter                      physicalDmg, physicalBattlerId  how much, and by whom
   Mirror Coat                  specialDmg, specialBattlerId    the same, other category
   Focus Punch                  either field, non-zero          did anything happen at all
     (Cmd_jumpifnodamage)                                        (if yes, the punch is lost)
   Revenge                      either field, AND the id        was it THIS opponent
     (Cmd_doubledamagedealtifdamaged)                            (if yes, double power)
   ──────────────────────────────────────────────────────────────────────────────────────
   AND THE SOURCE SAYS SO ITSELF, in a comment above the write: the two fields are
   "only distinguished between for Counter/Mirror Coat" but "used in combination as
   general damage trackers for other purposes", specialDmg additionally helping to
   decide whether a Fire move should defrost its target.
```

Four mechanisms, four questions, one eight-byte record that was written for the first two. A
record kept for one purpose and consumed for several is not a hypothetical risk here; it is in the
comment.

**Wobbuffet** is worth a sentence because its whole level-up learnset is four moves, all at level
1: **Counter**, **Mirror Coat**, **Safeguard** and **Destiny Bond**. Two of the four are the
readers above. The third belongs to emergency m103's prevention-at-the-point-of-entry argument.
The fourth maps onto nothing that this directory permits to be mapped, and it is named here only
to complete the list.

## It survives exactly as long as the turn is still being resolved

```
   BattleTurnPassed(), in src/battle_main.c, in order:

      TurnValuesCleanUp(TRUE)      <- clears protected and endured. TWO FIELDS.
                                      The damage record SURVIVES this.
      DoFieldEndTurnEffects()      \
      DoBattlerEndTurnEffects()     |  weather, status, Leech Seed, Wish, Perish
      HandleFaintedMonActions()     |  Song - all of it able to read the record
      HandleWishPerishSongOnTurnEnd()/
      TurnValuesCleanUp(FALSE)     <- dataPtr = (u8 *)&gProtectStructs[battler];
                                      for (i = 0; i < sizeof(struct ProtectStruct); i++)
                                          dataPtr[i] = 0;
                                      THE WHOLE STRUCT. A byte loop. Everything.

   AND THE OTHER CLEAR-DOWN IS HAND-WRITTEN. SwitchInClearSetData - the function
   emergency m070 took apart for what a handover deletes and what survives -
   clears NINETEEN named booleans of the same struct, one assignment each:
   protected, endured, noValidMoves, helpingHand, bounceMove, stealMove,
   flag0Unknown, prlzImmobility, confusionSelfDmg, targetNotAffected, chargingTurn,
   fleeType, usedImprisonedMove, loveImmobility, usedDisabledMove, usedTauntedMove,
   flag2Unknown, flinchImmobility, notFirstStrike.

   It does not mention physicalDmg, specialDmg, physicalBattlerId or specialBattlerId.
   One clear-down enumerates nineteen fields by name; the other zeroes all of them
   in a loop. m070's truantSwitchInHack is the same shape: a field list is what you
   get after somebody discovers a loss.
```

**Bide** is the only exception, and it is instructive about the other direction. `Cmd_setbide`
zeroes `gBideDmg` at the start and the accumulator then runs across turns — but `gBideTarget` is
*overwritten* on every recorded hit, so what survives is a running total and the name of the most
recent contributor only. An aggregate that loses the names, beside a case record that loses the
history. Between them the engine has both failure modes of an incident file.

## Changing the actor changes nothing; the only lever is the field

The engine is unusually clear about where a remedy can be applied.

Nothing can be done to a Pokémon that makes **Counter** work against **Spikes**. Not a level, not
an effort value, not a different nature, not a better-chosen moveset: the store is empty because
the script that removed the HP set `HITMARKER_PASSIVE_HP_UPDATE`, and no property of the creature
reaches that decision. The *only* thing that changes the outcome is changing the field — and the
cartridge prices that honestly. **Rapid Spin** clears **exactly one thing per use**, in a fixed
order: trapping first, then **Leech Seed**, then Spikes. One use, one layer, in an order somebody
chose, while the hazard was laid in a single action by someone who has since left.

So the hierarchy is in the code: a change to the holder is unavailable, a change to the field is
available, costed, partial and ordered. That is the whole argument for why a review whose output
is addressed to a person has produced nothing, and the reason the useful outputs are the ones that
alter a default rather than a disposition.

## What the cartridge has no field for

Here the game has nothing, and saying so is better than inventing something.

There is no field anywhere in `struct ProtectStruct`, `gSpecialStatuses`, `gDisableStructs` or
`gBattleStruct` for the **conditions** under which an act was chosen. Nothing stores what the
alternatives were, what was known at the time, what the player could see on screen, or that a move
was the only one with PP left — which is a real and common reason for a choice, and which nursing
m071 found is rendered identically to every other cause of an unusable move in one greyed-out menu
entry. The engine records what was done, how much it cost and whose name is attached. It has no
representation at all of what made the act the reasonable one.

Which is precisely the gap the subject is about, and it is more useful to point at the missing
fields than to invent a device that pretends they are there.

## Where the metaphor stops

There is a person in the middle of this and it is usually two people.

The patient, or the family, needs an account: what happened, what is known, what is not yet known,
what is being done, and — where it is owed — an apology. In many systems that duty is explicit and
statutory, and what it requires differs by jurisdiction. What is consistent is that a review
conducted so that an organisation can show it reviewed something, and which never reaches the
person affected, has failed at the only part of itself that was owed to anybody.

And the clinician. Being the named person at the end of that chain is one of the hardest things
that happens in a professional life. People involved in serious events describe a reaction that
outlasts the event by a long way and that changes their subsequent practice, usually towards more
caution and sometimes towards leaving. This is well described, and the support available is uneven
and often absent. If you are in that position, the sentence that matters is that this is a known
and expected reaction to something difficult rather than evidence about your competence, and that
support — occupational health, a professional body, a defence organisation, a colleague who has
been there — exists and is better used early than late. A review process that leaves that person
worse is not a rigorous process. It is a broken one, and it is also a less informative one,
because whoever is next in that position will have watched this.

The harder thing to say is that a systems account is sometimes experienced by a family as evasion
— as the mechanism by which nobody ends up responsible. That reaction is reasonable, and it is not
answered by explaining human factors. It is answered by an organisation taking responsibility as
an organisation, in public, for something it built, and by the change actually happening. Where
the change does not happen, the family's reading was the correct one.

## What a Gym Leader is listening for

Whether the Trainer identifies where the *name* comes from — a byte of the running script, not an
observation of the event — and says what follows from that. Then the two quantities: `gHpDealt` in
the retaliation store against `gBattleMoveDamage` in **Bide**'s accumulator, delivered against
intended. Then `HITMARKER_PASSIVE_HP_UPDATE`, its thirteen hand-written sites, and the consequence
that **Spikes**, **Sandstorm**, **Leech Seed** and recoil leave no attributable record — with
**Counter** failing into the generic string rather than mis-firing. Then the **Follow Me** clause,
read in the right order: the record is checked second. Then the four readers of one store and the
source comment that admits the reuse. Then the hierarchy, with no property of the holder reaching
the decision and **Rapid Spin** clearing one thing per use in a fixed order. Then the two
clear-downs — nineteen fields by name against a `sizeof` byte loop — and why a hand-written field
list is a sign of a loss already discovered. Then the absence: no field anywhere for the
conditions under which the act was chosen. Then the hard one — what the engine would have to
store, at the moment of the act rather than afterwards, for a review of the turn to be able to say
why the move was chosen.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The patient-safety incident framework in force in the reader's own system, for what must be
  reported, to whom, and how a review is expected to be conducted (**country-dependent**).
* The reader's professional regulator's guidance on being open and honest when something goes
  wrong, and the statutory duty of candour where one exists (**country-dependent**).
* The reader's own appraisal and revalidation requirements, which in several systems determine the
  form a significant event analysis has to take to count.
* The human-factors and safety-science literature, for active failures against latent conditions,
  work-as-imagined against work-as-done, and the hierarchy of effectiveness of interventions.
* The published work on the effects of involvement in a serious incident on the clinicians
  involved, and the support arrangements offered by the reader's own organisation, professional
  body or defence organisation.

The Pokémon facts are a separate matter and are not covered by the line above. The HP-update
block's four records and their conditions, including `gHpDealt` against `gBattleMoveDamage`, the
`gBattlescriptCurrInstr[1] == BS_TARGET` test that selects whose name is stored, the Pain Split
exclusion by name, the `IS_TYPE_PHYSICAL(moveType)` category test and the source's own comment
about the fields doubling as general damage trackers and helping decide defrosting; the thirteen
`HITMARKER_PASSIVE_HP_UPDATE` sites in `data/battle_scripts_1.s`, the four markers set together in
`BattleScript_DamagingWeatherLoop`, and `DoBattlerEndTurnEffects` wrapping the whole end-of-turn
block in `HITMARKER_IGNORE_BIDE`; `Cmd_counterdamagecalculator` and
`Cmd_mirrorcoatdamagecalculator` with their three conditions, their doubling, their Follow Me
redirection and their failure jump; `Cmd_jumpifnodamage` under `BattleScript_EffectFocusPunch` and
`Cmd_doubledamagedealtifdamaged` under `BattleScript_EffectRevenge`; `Cmd_setbide` zeroing the
accumulator and `gBideTarget` being overwritten per hit; `BattleTurnPassed` calling
`TurnValuesCleanUp(TRUE)` before the end-of-turn effects and `TurnValuesCleanUp(FALSE)` after it,
the `sizeof(struct ProtectStruct)` byte loop, and the nineteen named fields `SwitchInClearSetData`
clears; and Wobbuffet's four-move level-up learnset, were all read directly from the pret
decompilation projects, which this environment can reach. These are Emerald's; Generation IV moved
the physical/special split onto the move and the category test above does not transport.

## Scope and safety

This is revision material about the structure of a retrospective review, written for someone
already training in or qualified for the field. It is not a clinical reference, not a decision
aid, and it is **not a procedure for conducting an investigation or for handling a complaint, a
claim or a concern about a colleague** — all of those are governed by local policy, by regulation
and in places by law, and the local documents are the authority. No timescale, reporting
threshold, grading scheme or disclosure requirement is named here on purpose. Nothing here
describes or judges any real event; every example is constructed, and no Pokémon in this answer
stands in for a person who was harmed. If you are the person involved in a serious incident, the
support routes named in the sources above exist for that and are worth using early. If someone is
unwell right now, the relevant action is to contact local urgent care or the local emergency
number, not to read this.

## Where this stands, October 2026

The structural claims — that a backward enquiry terminates at the first nameable sufficient cause,
that hindsight bias is not corrected by good intentions, that a blame-bearing process reduces its
own input, that work-as-done differs from work-as-imagined, and that one event cannot estimate a
rate — are mechanism and mainstream, and they have been stable for decades. The institutional
layer moves: what reporting systems exist, what they require, how reviews are graded, what must be
disclosed and to whom, and how a safety review is kept apart from processes about conduct. Several
systems have replaced their incident frameworks in the last few years, generally towards
systems-based review and proportionate response. The Emerald code is stable because the games are
finished. Take the framework and the duties from current local requirements rather than from here,
as of October 2026.
