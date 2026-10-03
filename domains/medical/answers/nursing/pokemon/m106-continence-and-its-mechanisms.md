---
id: "m106"
slug: continence-and-its-mechanisms
style: pokemon
category: nursing
difficulty: intermediate
question: "Why is continence a mechanism problem as well as a dignity problem, and what does a continence assessment actually have to separate?"
tags: [continence, bladder, assessment, dignity, overflow]
---

# One counter, two completely different ways to empty it, and one identical state.

The Advance games contain exactly one store that you fill on purpose and empty on purpose, and the
whole of it is three fields and three moves. **Gulpin** learns all three at **level 34** — in the
learnset file, three consecutive `LEVEL_UP_MOVE(34, ...)` lines, Stockpile then Spit Up then
Swallow — and **Swalot** learns the same three together at **40**. The engine ships the store and
both of its releases as one unit, at one level, because they are one system and half of it is
useless.

Markers used below, because this half carries clinical claims as well as mechanical ones:
(**mechanism**) follows from physiology; (**definitional**) is what the word means;
(**consensus**) is mainstream agreement across major guidance; (**country-dependent**) means the
reader's own guidance decides. Everything in a code block is from the Emerald decompilation and
carries no marker, because it is not a clinical claim.

## The store is three states wide, and it refuses the fourth

```
   static void Cmd_stockpile(void)
   {
       if (gDisableStructs[gBattlerAttacker].stockpileCounter == 3)
       {
           gMoveResultFlags |= MOVE_RESULT_MISSED;
           gBattleCommunication[MULTISTRING_CHOOSER] = B_MSG_CANT_STOCKPILE;
       }
       else
       {
           gDisableStructs[gBattlerAttacker].stockpileCounter++;
           ...
   ──────────────────────────────────────────────────────────────────────────────────────────
   A counter, three deep. Nothing else. In the third generation Stockpile raises no stat —
   the Defence and Special Defence boosts people remember are a FOURTH-generation addition,
   and `Cmd_stockpile` above is the entire move. All it does is hold a number.
```

Storage, in other words, is not a passive property in the engine either: it is a thing a move
does, it costs a turn, and the number it holds is read by two other moves that do opposite things
with it. (**mechanism**) That is the clinical division. Holding urine at low pressure is an
actively maintained state — a relaxed detrusor, a closed outlet, and cortical inhibition deferring
a reflex — and emptying is a separate coordinated event in which the detrusor contracts *as* the
outlet opens. (**mechanism**) The switch between them is a third function, distinct from either,
and when the switch fails the pressures go up and the emptying is incomplete. (**mechanism**,
**consensus**)

## Two releases, one indistinguishable state

```
   move          what it reads                 what it does                        on empty
   ───────────── ───────────────────────────── ─────────────────────────────────── ──────────────
   Spit Up       stockpileCounter              base power 100 × counter, outward,  jumps away:
                                               FLAG_PROTECT_AFFECTED               the move fails
   Swallow       stockpileCounter              maxHP / (1 << (3 - counter)) inward B_MSG_SWALLOW_
                                               — a quarter, a half, or ALL of it   FAILED
   ─────────────────────────────────────────────────────────────────────────────────────────────
   Same counter. Same precondition. One sends the contents at somebody else, one takes them
   back in, and NOTHING about the stored state tells you which was intended. The store knows
   how much. It does not know what for.
```

That is the shape of the clinical problem. A full bladder is not a finding. Leaking is not a
finding either, because the same observation — this person is wet — is produced by mechanisms that
are opposites of each other, and the treatment for one of them makes the other worse.

The patterns the serious half tabulates are a classification of *mechanism* and not of symptom,
(**definitional**) and the reason to learn them that way is the overflow row. A bladder that is
not emptying leaks. (**consensus**) At the bedside that looks identical to a bladder that is
contracting too early, and a drug that relaxes the detrusor — the right answer for the second —
makes retention worse in the first. (**consensus**) Establishing the residual volume is what
separates them; the volume that counts as significant is (**country-dependent**).

## The release that is refused and empties the store anyway

Here is the detail worth the whole answer. Both releases destroy the counter, and at least one of
them destroys it while achieving nothing:

```
   Swallow, at full HP:                       Spit Up, into Protect:
   ─────────────────────────────────────────  ──────────────────────────────────────────────
   stockpileCounter = 0;                      the CalculateBaseDamage branch is skipped
   gBattlescriptCurrInstr = jumpPtr;          (gBattleCommunication[MISS_TYPE] == B_MSG_
   B_MSG_SWALLOW_FULL_HP                       PROTECTED), and then, unconditionally:
                                              gDisableStructs[...].stockpileCounter = 0;
   ─────────────────────────────────────────────────────────────────────────────────────────
   The zeroing in both cases sits OUTSIDE the branch that did the useful work. Three turns
   spent filling the counter, one turn spent on a release the engine then declines, and the
   store is gone. Nothing warns you first. The "failed" message arrives after the write.
```

And here the picture runs out, which is worth saying where the device is used rather than at the
end. **A counter that is full refuses further input. A bladder does not.** `B_MSG_CANT_STOCKPILE`
is the message the body does not have: there is no refusal at capacity, which is precisely why
chronic retention with overflow exists at all. The engine's cap is a clean edge and the clinical
reality is a leak, and anyone carrying this analogy forward needs that difference in front of them
rather than behind them.

## The one thing in the cartridge that fires without being chosen

Every effect above costs a turn and a decision. Exactly one class of effect does not:

```
   case HOLD_EFFECT_RESTORE_HP:
       if (gBattleMons[battler].hp <= gBattleMons[battler].maxHP / 2 && !moveTurn)
       {
           gBattleMoveDamage = battlerHoldEffectParam;
           ...
           BattleScriptExecute(BattleScript_ItemHealHP_RemoveItem);
   ──────────────────────────────────────────────────────────────────────────────────────────
   A threshold on one quantity, tested between turns, with no input from anybody. The
   berry is eaten, the item is consumed, and the message is printed AFTERWARDS. There is
   no menu, no prompt and no way to defer it. In the third generation nothing suppresses
   it: you either hold a Sitrus Berry or you do not.
```

A threshold crossed, a release that fires without permission, and a notification that arrives
after the event — that is urgency, as a mechanism rather than as a complaint. What urgency removes
is not the bladder's function but the *interval*: the gap between the signal and the act, which is
the only thing that makes getting to a toilet possible. (**mechanism**) Behavioural work —
retraining, timed voiding, reviewing what and when someone drinks — is first-line in most national
guidance precisely because it works on the interval. (**consensus**)

Two numbers from the same table are worth having, because they are the house device from m006 and
m041 in miniature. `holdEffectParam` is **30** for a **Sitrus Berry** and **10** for an **Oran
Berry**, and those are flat HP, not fractions — so the same berry restores the same 30 to
**Blissey**'s enormous bar and to **Shedinja**'s single point. And a **Leppa Berry**, same price
of 20, same shelf, restores **PP** instead: an item that looks identical and acts on a completely
different resource. A litre is not a litre, and a bag is not a bag.

## What the record cannot hold, and the instrument that suppresses its own signal

m073 built an answer on `FlagGet` returning `FALSE` both for a genuinely clear bit and for a
lookup that failed outright — one storage class failing quietly into "no". Continence is that
argument with one extra term, and the extra term is the part worth carrying.

```
   what happened                             what the chart holds    what the next reader sees
   ───────────────────────────────────────── ─────────────────────── ─────────────────────────
   asked privately; the answer was no         "continent"             a usable negative
   asked; the answer was yes                  a pattern and a plan    something to act on
   never asked                                nothing                 nothing
   asked across a four-bedded bay, and        nothing                 nothing
   denied
   ──────────────────────────────────────────────────────────────────────────────────────────
   The last two collapse into one blank, exactly as in m073 — but the fourth state is
   CREATED by the act of recording. The instrument suppresses the signal it is measuring.
   No flag in Emerald does that, and this is the point at which the save file stops being
   a fair model.
```

Continence data is self-reported and the reporting is systematically suppressed, so any prevalence
figure in any record is a floor rather than an estimate. (**consensus**) Containment has the same
property from the other direction: a pad is often exactly the right answer and is the person's own
preference more often than services assume, but once it is in place the episodes stop being
counted, because there is no event left to record. (**mechanism**) The decision to contain is also
a decision to stop measuring, and that is a second reason it needs a review point.

Two conclusions that belong to other answers in this specialty and are not re-derived here. m038
is the full argument that catheterisation is not an indicated management for incontinence — the
held item nobody reviews, with a per-day hazard. m004 separates moisture-associated skin damage
from pressure damage, which is the commonest consequence of getting continence wrong and the
commonest thing to be misattributed. And m040's falls channels include this one directly: the
reason a frail person gets up in an unfamiliar room at night is usually to pass urine, so a
toileting plan is a falls intervention. (**consensus**)

## Where the metaphor stops

It stops before the part that matters most to the person, and it has to be said without any of the
above.

Continence is among the first things a child is taught, it is tied to adult standing in almost
every culture, and losing it is experienced by many people as a loss of status rather than as a
symptom. That is why people do not raise it. They manage alone for years. They restrict what they
drink, which causes its own harm. They stop going to places where they do not know where the
toilet is, and that isolation is frequently more disabling than the symptom itself. Some stop
leaving the house at all.

In hospital the stakes are immediate. Being wet and waiting is one of the most distressing things
people report about inpatient care, and the distress is out of all proportion to the clinical
weight of the event. Being changed by a stranger, in a bay with a curtain that does not quite
reach, having been told that someone will come back — these are the parts people describe years
later, and they are the parts least likely to appear anywhere in the record of the admission.
There is no mechanic for any of that, and there should not be one.

Three things follow and none of them are soft. The question has to be asked, privately and in
plain words, because the circumstances of the asking determine the answer. The language matters:
"incontinent" used of a person rather than of an event travels with them into every subsequent
encounter. And a plan is only a plan if somebody can deliver it — a toileting plan written on a
ward that cannot staff it is a record of an intention, and the person still waits.

For families, continence is one of the commonest reasons a care arrangement at home stops being
sustainable, and one of the commonest triggers for a move into residential care. The consequences
run far past the clinical description.

## What Nurse Joy is listening for

Why storage is an actively held state and not an absence of voiding, and why coordination is a
third function rather than a property of the other two. Each pattern's mechanism, and which
first-line intervention follows from it rather than from the symptom. The overflow inversion, in
both tracts, and what the wrong treatment does. What has to be excluded before this is called a
continence problem. Why the chain is mostly outside the bladder for an inpatient. Why
catheterisation is not a continence management, which is m038. The moisture-associated skin damage
distinction, which is m004. And the local arrangements — who assesses, who scans, what the
continence service will see — because those are the things that decide what actually happens.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to
this answer:

* The reader's national clinical guideline body's guidance on urinary incontinence in women, and
  its separate guidance on lower urinary tract symptoms in men.
* The reader's national guidance on urinary catheterisation and on continence care.
* The reader's institutional policy on bladder scanning and post-void residual measurement,
  including who may perform and interpret it.
* A current textbook of continence care or of urogynaecology, for the classification and the
  physiology of storage and voiding.
* The reader's national guidance on faecal incontinence, for the overflow inversion in the other
  tract.
* Published literature on anticholinergic burden in older people, which rests on observational
  evidence.
* The reader's local continence service's referral criteria, which are institutional.

The Pokémon material is from the **pret/pokeemerald** decompilation of Pokémon Emerald:
`Cmd_stockpile`, `Cmd_stockpiletobasedamage` and `Cmd_stockpiletohpheal` in
`src/battle_script_commands.c`; the `HOLD_EFFECT_RESTORE_HP` case in `src/battle_util.c`; the
`holdEffectParam` values in `src/data/items.h`; and Gulpin's and Swalot's entries in
`src/data/pokemon/level_up_learnsets.h`. The fourth-generation Stockpile stat boosts are named as
*not* being in this code, which is checkable by reading `Cmd_stockpile` above.

## Scope and safety

This explains the mechanisms behind continence through a game's storage mechanic, for someone
already training in or qualified for clinical practice. It is not a continence assessment tool,
not a care plan and not a guide to managing anyone's symptoms. It names no residual volume, no
drug, no dose, no toileting interval and no referral threshold, because those are set by the
reader's national guidance and local policy, which are the authority. Nothing here has had
clinical review. New incontinence, incontinence with pain or visible blood, and incontinence with
any new neurological symptom — weakness, altered sensation around the perineum, or new bowel
symptoms — need assessment through the reader's local urgent pathway and are not matters for a
revision answer. If someone is unwell right now, the local emergency number is the correct
response.

## Where this stands, October 2026

The mechanical material is fixed: Emerald's code does not change, and the third-generation
Stockpile really does only hold a number. The physiology does not date either. What dates is the
terminology — "overactive bladder" against "urge incontinence", and the retirement of older labels
— so a reader should expect their local documents to use different words from these. Drug
treatment for urgency is the fastest-moving part, particularly the weight given to anticholinergic
burden in older people, and the device and procedural options differ considerably by country and
by what the local service commissions. The position on catheterisation for containment has
hardened in the same direction everywhere over two decades, but the local bundle is institutional.
The reader's national guidance and local continence service are the authority throughout.
