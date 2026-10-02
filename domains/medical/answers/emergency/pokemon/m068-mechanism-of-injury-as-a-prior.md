---
id: "m068"
slug: mechanism-of-injury-as-a-prior
style: pokemon
category: emergency
difficulty: intermediate
question: "Why does the mechanism of injury change what is looked for in trauma, when the examination itself is the same either way?"
tags: [trauma, mechanism-of-injury, priors, occult-injury, revision]
---

# Future Sight is computed the moment it is used, stored, and shown to nobody for three turns

`Cmd_trysetfutureattack` in Emerald's `src/battle_script_commands.c` is the cleanest piece of code
in the game for this subject. When Future Sight is used, the engine immediately calls
`CalculateBaseDamage` against the state of both Pokémon *at that instant*, writes the result into
`gWishFutureKnock.futureSightDmg[gBattlerTarget]`, records the move and the attacker, and sets
`futureSightCounter` to 3.

Then nothing happens. No animation on the target. No health bar movement. No message about the
target at all — `gFutureMoveUsedStringIds` prints a line about the *attacker*. For the next two
turns the field looks exactly as it would if the move had failed, and the entire consequence is
already fixed, sitting in a struct, computed from a situation that has since stopped existing.

That is the shape the mechanism of injury is reasoning about. The event is over. Its consequence
was determined when it happened. And for a while there is nothing to find by looking.

## What a move's entry predicts, which is not what it proves

Every move in `src/data/battle_moves.h` carries the same nine fields, and reading the entry tells
you what to go and check even when the battle printed nothing:

```
   .effect   .power   .type   .accuracy   .pp   .secondaryEffectChance   .target   .priority   .flags
   ───────────────────────────────────────────────────────────────────────────────────────────────────
   Flamethrower  EFFECT_BURN_HIT     95 power  chance 10  → check status1 for a burn
   Rock Slide    EFFECT_FLINCH_HIT   75 power  chance 30  → check status2 for a flinch flag
   Twister       EFFECT_TWISTER      40 power  chance 20  → a flinch, and a doubling if airborne
   Thunder       EFFECT_THUNDER     120 power  chance 30  → paralysis; 70 accuracy, but sure in rain
   Sludge Bomb   EFFECT_POISON_HIT   90 power  chance 30  → check status1 for poison
   Stomp         EFFECT_FLINCH_MINIMIZE_HIT   65 power  chance 30  → a flinch, doubled if Minimized
   Doom Desire   EFFECT_FUTURE_SIGHT 120 power chance  0  → nothing to check; it is in a counter
   Future Sight  EFFECT_FUTURE_SIGHT  80 power chance  0  → nothing to check; it is in a counter
   ───────────────────────────────────────────────────────────────────────────────────────────────────
   the entry tells you which flag MIGHT be set.  It never tells you that it IS.
```

Two things can make the prediction come out false without anything being wrong. **Shield Dust**,
which **Dustox** and **Wurmple** and **Caterpie** carry, cancels a secondary effect outright, so
Flamethrower's burn bit never gets set against a Dustox however the roll lands. And the condition
can be blocked rather than prevented: **Water Veil** on **Wailord** refuses the burn, **Immunity**
on **Snorlax** refuses the poison, **Inner Focus** refuses the flinch. The entry describes what
the move does to a typical target, which is precisely what a prior is.

That distinction is the whole of the clinical point. Knowing Flamethrower was used does not tell
you a burn was applied; `secondaryEffectChance = 10` is a probability, and `seteffectwithchance`
rolls it. What the entry buys is **where to look**, and a search aimed at the right field is a
different thing from a search aimed at whatever is most visible. It raises a prior; it does not
produce a finding.

## The state of the target at the moment of transfer changes what the same move does

Four hand-written branches in `data/battle_scripts_1.s` exist for exactly this, and all four work
by setting `sDMG_MULTIPLIER` to 2:

* **`BattleScript_EffectEarthquake`** checks `STATUS3_UNDERGROUND` on the target and doubles if it
  is mid-Dig — a **Trapinch** or a **Flygon** underground, both of which learn Dig from the same
  TM. Same move, same user, **Golem**'s Earthquake at the same base power of 100 — twice the
  transfer, because of where the target was.
* **`BattleScript_EffectGust`** and **`BattleScript_EffectTwister`** check `STATUS3_ON_AIR` and
  double against a target mid-Fly or mid-Bounce — a **Skarmory** that just went up, say.
* **`BattleScript_EffectHit`** opens with a special case for Surf alone, checking
  `STATUS3_UNDERWATER` and doubling against a target mid-Dive — a **Sharpedo** under the surface,
  hit by a **Wailord**'s Surf.
* **`BattleScript_EffectStomp`** checks `STATUS3_MINIMIZED` and doubles against a target that made
  itself smaller — a **Clefairy** that used Minimize, which it learns at level 21, against a
  **Miltank**'s Stomp, which Miltank learns at 13.

Nothing about the attacker changed in any of those. The *situation at the instant of contact* did,
and that is the entire content of the clinical distinction between the label of an event and its
mechanics: restrained or not, braced or not, which way the head was turned, what was between the
energy and the tissue. Dig's own entry is 60 base power in Emerald and Fly's is 70, so the
multiplier on the incoming move is often larger than anything the semi-invulnerable move itself
contributes — the state matters more than the action.

## Anchoring, written into the engine as a bug class

Look at what `BattleScript_EffectEarthquake` has to do on the branch where the target is *not*
underground:

```
   BattleScript_HitsAllNoUndergroundBonus::
       bicword gHitMarker, HITMARKER_IGNORE_UNDERGROUND
       setbyte sDMG_MULTIPLIER, 1
```

It explicitly writes 1 back. It would be shorter not to, and it would be wrong: the multiplier is
shared state, and Earthquake loops over every target in a double battle. Without that reset, an
assumption formed about the first target would be carried silently into the calculation for the
second. The engine has to clear the prior between cases or the prior contaminates them.

That is anchoring, implemented. And the loop structure is the reason it bites:
`BattleScript_HitsAllWithUndergroundBonusLoop` re-enters with `movevaluescleanup` and re-checks
the status for each target, so the question is asked again per target rather than once per move.
Asking once and reusing the answer is precisely the failure mode.

## Why the prior cannot be run backwards

Three facts about the engine make this concrete.

**A flag can be set with nothing having been announced.** `Cmd_trysetfutureattack` is the extreme
case — and **Jirachi**'s Doom Desire, which it learns at level 50 and which is the only other move
carrying `EFFECT_FUTURE_SIGHT`, is stored the same way in the same struct. The general case is
more ordinary: the field's state is a set of bitfields in `status2`, `gStatuses3`,
`gDisableStructs` and `gProtectStructs`, and most of them produce no per-turn message. The absence
of a message is not the absence of state.

**The stored consequence does not update.** `futureSightDmg` was computed against the stats and
stages that existed when the move was used. Boost the target's defence afterwards and the stored
number does not care. A consequence fixed at the moment of the event is not responsive to anything
that happens later, which is why it has to be anticipated rather than watched for.

**And the prior is about the move, not about this instance of it.** Rock Slide's
`secondaryEffectChance` is 30, so seven times in ten nothing was flinched, and a move whose entry
says 30 that produced no flinch has behaved normally. The same is true the other way: a **King's
Rock**, whose `holdEffectParam` is 10, can add a flinch to a move whose own entry says nothing
about one, so an unexpected flag is not evidence the entry was misread. Reading a high-risk entry
as evidence that something happened is as wrong as reading a low-risk entry as evidence that
nothing did — and of those two errors, the second is the one that gets people.

## Where the metaphor stops

Plain prose from here, with no game in it. This part is about people and the metaphor is set down.

The mechanism of injury is not a finding. It is a description of a physical event — how much
energy was transferred, in what direction, over what time, into which tissues, with the body in
what state — and what it provides is a prior probability over possible injuries, formed before
anybody has examined anything. The examination afterwards is the same examination; what changes is
the weight its results carry, which is why acting differently on an identical finding under a
different mechanism is coherent rather than inconsistent. That is (**mechanism**): Bayesian
reasoning applied to a physical event, checkable by reasoning.

It earns its place mainly on one thing. Some consequences of energy transfer are complete at the
instant of the event and produce no sign for a long time afterwards, so no examination at the time
can find them, and the only way they are caught early is that something about the event said to
look. Beyond that it sets a search pattern — energy travels in a line, and the second injury along
that line is more likely than chance — and it shifts the threshold for acting on an equivocal
result.

Four cautions carry more weight than the elegance of any of it. It cannot be run backwards: a
reassuring mechanism is not a negative test, and mechanism-based criteria are deliberately built
to be sensitive at the cost of specificity, so they over-trigger by design. A benign-sounding
account talking a clinician out of a real abnormal finding is the dangerous direction of the
error, particularly in the very old and the very young, whose tissues tolerate less; under-triage
of older patients on mechanism-based criteria has been an active problem for years. The reported
mechanism is frequently wrong, incomplete or absent, and a prior inherits the reliability of the
account it was built from. And the specifics — energy, direction, the state of the body — are the
part that carries the information and the part most easily lost at a handover, where only the
label tends to survive. **(Consensus** that occult and delayed-presenting injury is a major source
of avoidable harm and that such criteria are constructed for sensitivity; (**country-dependent**)
for every criterion, threshold and imaging indication, none of which is stated here.**)**

No Pokémon stands for a person, a casualty or an injury anywhere in this answer, nothing in the
game represents anyone's outcome, and nothing here is a sequence of actions. The game is carrying
two ideas and no others: that a consequence can be fully determined at the moment of an event and
invisible for a while afterwards, and that a prior has to be re-formed per case rather than
carried over. What is at stake when that consequence belongs to a person is stated above, plainly,
because it is not a mechanic and nothing would be gained by dressing it up.

## What a Gym Leader is listening for

* What exactly does `Cmd_trysetfutureattack` do at the moment the move is used, and what does the
  field show?
* `secondaryEffectChance = 10` on Flamethrower. What does knowing the move tell you, and what does
  it not?
* Four scripts double `sDMG_MULTIPLIER` against a target in a particular state. What is the
  general principle, and why does it matter that the attacker did not change?
* Why does the Earthquake script write `sDMG_MULTIPLIER, 1` on the branch where nothing applies?
* `futureSightDmg` does not update after it is stored. What does that imply about watching and
  waiting?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md), and they
apply here. Specific to this answer:

* The current major trauma assessment and triage guidance issued by **the reader's regional or
  national trauma network**, which is where mechanism-based criteria, imaging indications and
  triage thresholds live. These differ substantially between networks and are revised.
* The current trauma guidance issued by **the reader's own national body for clinical
  guidelines**, for the decision rules in use where they practise.
* A current standard textbook of **emergency medicine or of trauma surgery**, for injury
  biomechanics and for which injuries characteristically declare themselves late.
* **The reader's own employing organisation's** trauma policy and imaging pathways, which govern
  practice where they work and outrank every general account including this one.

No guideline number, document title or identifier is given, and nothing is quoted, because none of
these was opened. The Pokémon side is in the opposite position and is sourced file by file in the
closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *why a kind of reasoning is structured the way it is*, written for
someone already trained, and the Pokémon framing covers two ideas only: a consequence fixed at the
moment of an event, and a prior that must be re-formed per case. It is deliberately not a protocol
and not a decision aid — no triage criteria, no imaging indications, no thresholds, no sequence of
actions, no doses, no settings, and nothing to consult while acting. Mechanism-based criteria
differ substantially between trauma networks and are revised. The reader's own network guidance
and local policy are the authority; this is not, and it has had no clinical review. Nothing here
describes any real person, case or event.

## Where this stands, October 2026

The Pokémon facts are pinned to source and are stable. Future Sight's damage being computed and
stored at the moment of use, with `futureSightCounter` set to 3 and nothing shown on the target,
is `Cmd_trysetfutureattack` in `src/battle_script_commands.c`; the nine fields of a move entry and
the specific values quoted — Flamethrower 95 power with chance 10, Rock Slide 75 with chance 30,
Twister 40 with chance 20, Future Sight 80, Dig 60, Fly 70 — are from `src/data/battle_moves.h`;
and the four doubling branches, the Surf special case at the head of `BattleScript_EffectHit`, the
explicit `setbyte sDMG_MULTIPLIER, 1` reset and the per-target loop are from
`data/battle_scripts_1.s`. Those are Generation III figures and several have changed since — Dig,
Fly, Flamethrower and the semi-invulnerable interactions have all been revised in later games — so
a reader checking today's values should read today's game rather than this page. On the clinical
side the reasoning is long-standing and every specific built on it is not: mechanism-based
criteria, imaging indications and the age modifiers attached to them differ between trauma systems
and have been revised repeatedly. Principle dated October 2026; read the current network and
institutional documents for anything past the principle.
