---
id: "m131"
slug: delegation-and-supervision
style: pokemon
category: nursing
difficulty: advanced
question: "What can be delegated in nursing care, what cannot, and where does accountability sit once a task has been handed over?"
tags: [delegation, supervision, accountability, skill-mix, scope-of-practice]
---

# One list of tasks, four callers, and a sentinel one value apart decides who may read how much.

The third generation keeps what a move may hand on to another move in a single array, and then
lets four different mechanics read it under three different rules. That array is the best object
in the cartridge for thinking about delegation, because it makes visible the thing the clinical
version hides: **the list of what may be handed over is not a property of the task. It is a
property of the route.**

Markers used below, because this half carries clinical claims. (**mechanism**) means it follows
from the structure of the arrangement; (**definitional**) is what the word means;
(**consensus**) is mainstream agreement across major guidance; (**country-dependent**) means the
reader's own regulator or employer decides, and for this subject that is most of it. Code blocks
carry no marker. No staffing level, ratio, supervision interval or competency threshold appears
anywhere here.

## The array, and the two sentinels that are numerically adjacent

```
   #define MIMIC_FORBIDDEN_END       0xFFFE        ◄── these two differ by ONE
   #define METRONOME_FORBIDDEN_END   0xFFFF
   #define ASSIST_FORBIDDEN_END      0xFFFF        ◄── and this one IS the one above

   static const u16 sMovesForbiddenToCopy[] =
   {
       MOVE_METRONOME, MOVE_STRUGGLE, MOVE_SKETCH, MOVE_MIMIC,
       MIMIC_FORBIDDEN_END,                        ◄── index 4. Mimic stops reading HERE
       MOVE_COUNTER, MOVE_MIRROR_COAT, MOVE_PROTECT, MOVE_DETECT, MOVE_ENDURE,
       MOVE_DESTINY_BOND, MOVE_SLEEP_TALK, MOVE_THIEF, MOVE_FOLLOW_ME, MOVE_SNATCH,
       MOVE_HELPING_HAND, MOVE_COVET, MOVE_TRICK, MOVE_FOCUS_PUNCH,
       METRONOME_FORBIDDEN_END                     ◄── index 19. Metronome and Assist stop here
   };
   ──────────────────────────────────────────────────────────────────────────────────────────
   ONE list. Mimic's loop terminates on 0xFFFE and therefore sees FOUR exclusions.
   Metronome's and Assist's terminate on 0xFFFF and see NINETEEN. Nothing about
   Protect or Destiny Bond or Trick changed; what changed is which caller asked.
```

That is the scope-of-practice argument in one array, and it is worth saying slowly. **Counter is
not an intrinsically unhandable act.** Mimic may copy it quite happily. Metronome and Assist may
not, and the reason is not a property of Counter — it is the terminator that the asking route was
written to stop at. A ward's list of what a support worker may do is the same kind of object: the
task appears on one role's list and not another's, and the difference lives in the list rather
than in the task (**country-dependent**, and this is the whole reason a published task list
cannot be carried from one institution to the next).

And **Sleep Talk reads the same situation under a fourth rule entirely**, which is where the
analogy earns its place:

```
   static bool8 IsInvalidForSleepTalkOrAssist(u16 move)
   {
       if (move == MOVE_NONE || move == MOVE_SLEEP_TALK || move == MOVE_ASSIST
        || move == MOVE_MIRROR_MOVE || move == MOVE_METRONOME)  return TRUE;
   }

   Cmd_trychoosesleeptalkmove then ALSO excludes, by hand, in the same loop:
        MOVE_FOCUS_PUNCH,  MOVE_UPROAR,  IsTwoTurnsMove(...)
   and finally runs:
        CheckMoveLimitations(gBattlerAttacker, unusableMovesBits, ~MOVE_LIMITATION_PP)
   ──────────────────────────────────────────────────────────────────────────────────────────
   Four routes — Mimic, Metronome, Assist, Sleep Talk — one shared array, and two of them
   with extra hand-written clauses on top. The ~MOVE_LIMITATION_PP is the detail to notice:
   Sleep Talk deliberately switches OFF one of the eight limitation checks, so a slot with
   no PP left is still available to it. A route that relaxes exactly one condition that
   every other route enforces.
```

Four readers, one list, no single answer to "may this be handed over". The clinical version of
that question is answered the same way and for the same reason: by the route, which means by the
reader's own regulator and employer (**country-dependent**).

## Assist draws from what the party actually holds, weighted by how much each one holds

`Cmd_assistattackselect` is delegation to "the team" rather than to a named individual, and
reading it is the fastest cure for assuming that handing a task to a team hands it to someone
suitable.

```
   for (monId = 0; monId < PARTY_SIZE; monId++)
   {
       if (monId == gBattlerPartyIndexes[gBattlerAttacker])  continue;   ◄── not yourself
       if (species == SPECIES_NONE)                          continue;   ◄── not an empty slot
       if (species == SPECIES_EGG)                           continue;   ◄── not an egg

       for (moveIndex = 0; moveIndex < MAX_MON_MOVES; moveIndex++)
           ... validMoves[chooseableMovesNo++] = move;        ◄── EVERY valid move, from
   }                                                              EVERY other member

   if (chooseableMovesNo)
       gCalledMove = validMoves[((Random() & 0xFF) * chooseableMovesNo) >> 8];
   else
       gBattlescriptCurrInstr = T1_READ_PTR(gBattlescriptCurrInstr + 1);   ◄── jump away
   ──────────────────────────────────────────────────────────────────────────────────────────
   The draw is uniform over MOVES, not over MEMBERS. A party member holding four legal
   moves is FOUR TIMES as likely to supply the answer as one holding a single legal move.
   Allocation is weighted by how much each one has available, which is not the same thing
   as how well suited any of them is.
```

Two things fall out of that, and both have exact clinical counterparts.

The first is that the pool is **what the party actually holds**, enumerated at the moment of
asking — not what you believe it holds. The engine reads `MON_DATA_MOVE1 + moveIndex` off each
member every time. Competence is task-specific, it is established rather than inferred, and the
established version is a record you can read (**mechanism**, **consensus**). An **Abra** with
nothing but **Teleport** contributes exactly one option however long it has been in the party,
and seniority is not in the structure anywhere.

The second is the `else` branch. When nothing in the party qualifies, Assist **jumps away**: the
PP is gone, the turn is spent, and the only thing printed is a failure. Nothing anywhere says
*"nobody present could do this"*. That is delegation by absence, which is the commonest failure in
the clinical version and the hardest to see, because an unsafe handover is at least visible in a
record and an un-made one leaves a blank (**mechanism**). m073's four-state collapse is the same
shape arriving from a different direction.

## The order and the act are two fields, and one script byte decides whether the order survives

The engine keeps three separate globals, and the distinction between them is the whole
accountability question.

```
   gChosenMove    what was ORDERED        (gChosenMoveByBattler[] holds it per battler)
   gCalledMove    what the delegating route PRODUCED
   gCurrentMove   what is actually being EXECUTED right now

   static void Cmd_jumptocalledmove(void)
   {
       if (gBattlescriptCurrInstr[1])
           gCurrentMove = gCalledMove;                  ◄── the ORDER IS PRESERVED
       else
           gChosenMove = gCurrentMove = gCalledMove;    ◄── the order is OVERWRITTEN
       ...
   }
   ──────────────────────────────────────────────────────────────────────────────────────────
   One byte of script argument decides whether the record of what was asked for survives
   the act. And there are exactly THREE call sites in data/battle_scripts_1.s:

     BattleScript_SleepTalkUsingMove        jumptocalledmove TRUE    order kept
     BattleScript_EffectAssist              jumptocalledmove TRUE    order kept
     BattleScript_IgnoresAndUsesRandomMove  jumptocalledmove FALSE   order DESTROYED
```

Read that table twice. Where the handover was **deliberate** — Sleep Talk, Assist — the engine
keeps both fields: there is a record of what was asked for and a separate record of what was done.
Where the instruction was **not followed**, the engine overwrites the order with the act, and the
one case in which you would most need to know what was asked for is the only case in which the
game does not keep it.

That is the clinical shape exactly. Accountability for the decision to hand a task over, and
accountability for the execution of it, are two different objects held concurrently, and neither
cancels the other (**consensus**; the legal construction is (**country-dependent**)). They are
separable in the record only if the record holds both — what was asked, by whom, of whom, with
what to report back — and the commonest real-world defect is a note that holds only the act. The
engine has a field for the order and a field for the act; a clinical record frequently has one
box.

## Authority is a flag in the save file, and it sits on the instructor's side

This is m015's device, reused on purpose and for a different job. m015 reads the Kanto obedience
ladder for continuity of care — a Pokémon somebody else raised arrives with a full record and no
history with you — and the point there is about the relationship. The point here is about
**where the engine stores the authority**, which is a question m015 does not ask.

`IsMonDisobedient`, in `src/battle_util.c`, is where Emerald decides whether an instruction is
carried out at all. It is a chain of early returns, and every one of them is about the
*arrangement* rather than about the task.

```
   return OBEDIENT if ...                        what the condition is actually about
   ──────────────────────────────────────────── ───────────────────────────────────────────────
   BATTLE_TYPE_LINK | RECORDED_LINK              the FORMAT. In a link battle the check does
                                                  not run at all
   the battler is on the opponent's side         whose arrangement this is
   BATTLE_TYPE_FRONTIER, RECORDED,               three more formats in which it is switched off
   INGAME_PARTNER at position 2
   !IsOtherTrainer(otId, otName)                 PROVENANCE: one you raised yourself always
                                                  obeys. The check exists only for one somebody
                                                  else trained
   FlagGet(FLAG_BADGE08_GET)                     a single flag that makes everything obey,
                                                  regardless of level
   ──────────────────────────────────────────── ───────────────────────────────────────────────
   otherwise:  obedienceLevel = 10
               FLAG_BADGE02_GET → 30    FLAG_BADGE04_GET → 50    FLAG_BADGE06_GET → 70
               and level <= obedienceLevel → OBEDIENT
   ─────────────────────────────────────────────────────────────────────────────────────────────
      This ladder is EMERALD's, read out of src/battle_util.c; do not carry it to another
   cartridge without opening that cartridge. The four THRESHOLDS are the same four m015
   gives for Kanto — 10, 30, 50, 70 — but the four BADGES consulted are named differently
   there, so the numbers travel and the flags do not. The structure is the point: every term
   is either a flag in the player's save file or a property of the format. Not one of them
   is a property of the move being ordered.
```

Authority to direct is held on the *delegator's* side, it is granted externally, and it scales
with the level of what is being attempted — which is as close as the engine gets to the clinical
rule that the supervision a task needs is a function of the task's risk and of how new the
delegate is to it, not of how busy the shift is (**consensus**).

One more structural detail, and it is the sharpest one. The obedience check is skipped entirely
when `gBattleMons[gBattlerAttacker].status2 & STATUS2_MULTIPLETURNS` is set — a **Thrash**, a
**Petal Dance**, an **Outrage** already under way is not re-authorised mid-sequence — and
`HITMARKER_OBEYS` is cleared between actions in `HandleAction_NothingIsFainted`, so the check
re-runs for each fresh action and never during one. The clinical failure mode is precisely that
asymmetry: the delegation decision is made once, at the point of initiation, against a patient's
condition at that moment, and the task then recurs for the rest of the shift with nothing in the
routine prompting a re-decision (**mechanism**).

And here the cartridge runs out, which is worth saying where the device is used rather than at the
end. **Nothing in the games models a delegate declining a task.** The engine's branches for an
instruction not carried out are a random substitute move, a self-inflicted hit, falling asleep,
and four interchangeable strings about turning away and pretending not to notice — and every one
of those is the game making a joke at the expense of the one being instructed. The clinical answer
needs the opposite object: a competent person recognising that a task is outside what was agreed
and **saying so**, which is not non-compliance but the system's last safety check (**consensus**).
There is no mechanic for it, the loafing strings are not it, and a forced mapping here would teach
something false about the most important element in the subject. m045's reading of
`gFrontierBannedSpecies` is as near as the cartridge comes to a refusal, and it is a rule about
entry rather than a judgement made in the moment.

## Where the metaphor stops

It stops at the person being delegated to, and it stops completely.

Everything above is about lists, fields and flags, because that is what the subject is made of
when you look at the structure. What the structure cannot carry is that delegation is a
relationship between two people, usually of unequal standing, usually under time pressure, and
that the safety of it rests on the less powerful of the two being able to say no.

Being asked to do something beyond your competence is frightening. Refusing costs something real:
the shift goes badly, you are remembered as difficult, and the person asking is often senior to
you and will be writing about you at some point. Teaching that stops at "you can always decline"
puts the weight of a staffing failure on the least protected person in the room. What makes
declining actually possible is structural — a named route to raise it, a culture in which it is
heard without cost, and seniors whose response to a refusal is to fix the gap rather than find
someone more compliant. Bank staff, agency staff, students and the newly qualified are the people
most likely to be asked and least able to refuse, which means the safety mechanism fails first in
exactly the population it most needs to protect.

The other half of the honesty is about the people this question is usually asked about. Most
direct care in most health systems is given by people who are not registrants, and that is not a
deficiency to be managed. It is frequently the most skilled, most attentive and most continuous
care anybody receives, and a support worker often knows a patient better than any qualified person
on the ward does. Nothing in this answer should be read as suggesting otherwise: the question is
whether a decision was made and recorded, not whether the person at the bedside was good at their
job. A system that delegates well does not delegate less.

And the context, because every failure mode above worsens along the same axis. These decisions are
made under establishment constraints that the person making them did not set and cannot change
during a shift. Where a role has quietly absorbed work permanently because of gaps, each
individual handover can look defensible while the aggregate is a workforce change made one shift
at a time, without training, assessment or agreement. Calling that delegation conceals it. An
institution that answers a delegation incident by retraining individuals, without examining the
staffing that made the delegation necessary, has identified the wrong variable.

## What Nurse Joy is listening for

The separation of task, authority and accountability, and which of the three actually transfers.
The three concurrent accountabilities named as three objects rather than as a ranking. The five
conditions for a delegable task, and why the predictability of the outcome is the one doing the
work. Why assessment, interpretation, planning and escalation never delegate, with a worked pair
of examples that share a verb — "check his observations" against "check on him". The grades of
supervision and what sets the grade. Why the array read by four callers is the right picture of a
local task list, and therefore why a task list cannot travel between institutions. Why the
initiation-only check is the structural failure rather than any individual bad decision. What has
to be true around a delegate for "you may decline" to be a real option. And what the reader's own
regulator and employer say, because that is the document that binds them personally and no two
countries' versions agree.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to
this answer:

* The reader's **own professional regulator's standards on delegation, accountability and
  supervision** — the document that binds them personally, the most important source for this
  topic, and one that differs substantially between countries and between professions.
* The reader's institutional delegation policy: the local list of what may be delegated to each
  role, the competence assessment and recording requirements, and the named route for escalating
  a delegation that should not have been made.
* The reader's national regulatory framework for support worker and assistant roles, which is
  actively changing in several countries.
* The reader's employment law and vicarious liability position. This is law, it differs profoundly
  between jurisdictions, and no revision answer substitutes for it.
* The published literature on skill mix and outcomes, and on speaking up and psychological safety,
  for the plain-prose section. These rest on observational and survey evidence.
* A current professional-body publication on accountability, for the three-accountabilities
  framing and the task-versus-judgement distinction.

The Pokémon material is from the **pret/pokeemerald** decompilation of Pokémon Emerald:
`sMovesForbiddenToCopy` with its three sentinel defines, `IsMoveUncopyableByMimic`,
`Cmd_metronome`, `IsInvalidForSleepTalkOrAssist`, `Cmd_trychoosesleeptalkmove`,
`Cmd_assistattackselect` and `Cmd_jumptocalledmove` in `src/battle_script_commands.c`;
`IsMonDisobedient` and `HandleAction_NothingIsFainted` in `src/battle_util.c`; the three
`jumptocalledmove` call sites in `data/battle_scripts_1.s`; and `gChosenMove`, `gCalledMove` and
`gChosenMoveByBattler` declared in `src/battle_main.c`. The obedience ladder was read out of that
file rather than recalled, and it is stated as Emerald's because the badge flags used differ
between cartridges.

## Scope and safety

This explains what delegation transfers and what it does not, through a game's move-copying and
obedience code, at the level of someone already training in or qualified for clinical practice. It
is not a delegation policy, not a scope-of-practice determination and not legal advice. It
deliberately names no task as delegable or non-delegable in the reader's setting, because that
list belongs to the reader's regulator and employer, which are the authority and which differ by
country and by role; and it states no staffing level, ratio or supervision interval for the same
reason. Nothing here has had clinical or legal review, and nothing here should be relied on in a
complaint, an investigation, or any disciplinary or legal process. Nothing here is for use in an
emergency or for a decision about any person's care. If someone is unwell right now, the local
emergency number is the correct response.

## Where this stands, October 2026

The mechanical material is fixed, and the structural argument — that the task and the authority
transfer while the accountability for deciding does not — is not the sort of claim that dates.
What is moving quickly is the regulatory status of the roles being delegated to: registration,
protected titles and national competence frameworks for support and assistant roles are being
introduced or extended in several countries, and each change alters both what may be handed over
and who answers for it. The surrounding debate about skill mix and establishment is active,
politically contested, and supported by observational evidence rather than by mechanism.
Everything procedural and legal here — local task lists, competence records, supervision grades
and the liability position — belongs to the reader's regulator, employer and jurisdiction, which
are the authority throughout.
