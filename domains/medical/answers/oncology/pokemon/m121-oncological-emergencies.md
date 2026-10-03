---
id: "m121"
slug: oncological-emergencies
style: pokemon
category: oncology
difficulty: advanced
question: "Why are a few complications of cancer and its treatment mechanism-driven emergencies rather than severe versions of ordinary problems, and what does each mechanism change about the response?"
tags: [oncological-emergencies, mechanism, acute-oncology, escalation, prevention]
---

# Sonic Boom writes twenty into the damage variable and never opens the damage formula at all

Almost every damaging move in Emerald arrives at its number the same way. The script reaches
`damagecalc`, which calls `CalculateBaseDamage` and then multiplies the result:

```
   gBattleMoveDamage = CalculateBaseDamage(attacker, target, move, sideStatus,
                                           gDynamicBasePower, dynamicMoveType, ...);
   gBattleMoveDamage = gBattleMoveDamage * gCritMultiplier * gBattleScripting.dmgMultiplier;
```

That is a product, and every lever a player holds is one of its terms. Base power, the attacker's
Attack or Special Attack, the target's Defence or Special Defence, Reflect and Light Screen
through `sideStatus`, the stat stages, the same-type bonus, the type chart, the random factor, the
critical multiplier, Helping Hand's fifteen-tenths. Raise a term and the number goes up; resist a
term and it comes down. You can reason about *more* and *less* all day inside that product.

A handful of effects never enter it. `BattleScript_EffectSonicboom` has no `damagecalc`
instruction and no `critcalc` instruction. It runs `typecalc`, deletes two flags, and then:

```
	setword gBattleMoveDamage, 20
	adjustsetdamage
```

Twenty. Not a base power of twenty — the damage itself, assigned. Dragon Rage assigns forty.
Seismic Toss and Night Shade run `dmgtolevel`. Psywave runs `psywavedamageeffect`. None of them is
a big number inside the product; each one **is not in the product**, which means not one of the
levers you were holding is connected to it.

That is this answer's clinical claim with the machinery exposed. A few complications of cancer and
its treatment are not the severe end of a dial. The quantity that is dangerous was assigned by a
different mechanism, and *more of the usual, sooner* is not the response, because the usual is not
a term in it.

As elsewhere in this specialty, **the objects of study are formulas, tables and gates.** No
Pokémon in this answer stands in for a person, nothing faints, and nothing in the game stands for
anyone's outcome. The analogy is dropped entirely where the subject changes.

Clinical claims carry the same marks as the rigorous half: (**mechanism**), (**definitional**),
(**consensus**), (**country-dependent**).

## The product, and the effects that are not in it, drawn

```
   THE ORDINARY ROUTE — a product, and every lever is a term

      base power ──┐
      Atk / SpAtk ─┤
      Def / SpDef ─┤      ┌──────────────────────┐
      stat stages ─┼──────►  CalculateBaseDamage  ├──► × crit × dmgMultiplier ──► damage
      Reflect /    │      └──────────────────────┘
        Light Screen ┤        (sideStatus)
      same-type    ─┤
      type chart   ─┤
      random factor┘

      TURN ANY TERM AND THE ANSWER MOVES.  "Worse" and "better" are
      meaningful words here.

   ═══════════════════════════════════════════════════════════════════════════

   AND THE FOUR THAT ARE NOT IN IT

   ┌─ THE SHAPE THE CARTRIDGE DOES NOT HAVE ─────────────────────────────────┐
   │  nothing accumulates irreversible harm as a function of elapsed time.   │
   │  Toxic's counter is the nearest thing and the cure deletes it BY NAME.  │
   │       ►  the clinical window has no mapping, and that is the finding    │
   └─────────────────────────────────────────────────────────────────────────┘

   ┌─ THE READOUT, DELETED ON PURPOSE ───────────────────────────────────────┐
   │  typecalc runs, then:                                                   │
   │    bicbyte gMoveResultFlags, MOVE_RESULT_SUPER_EFFECTIVE                │
   │                            | MOVE_RESULT_NOT_VERY_EFFECTIVE             │
   │  the grading vocabulary is withheld because it would be FALSE           │
   └─────────────────────────────────────────────────────────────────────────┘

   ┌─ TWENTY, ALWAYS ────────────────────────────────────────────────────────┐
   │    setword gBattleMoveDamage, 20          (Sonic Boom)                  │
   │    setword gBattleMoveDamage, 40          (Dragon Rage)                 │
   │  a magnitude NEITHER side contributed to                                │
   └─────────────────────────────────────────────────────────────────────────┘

   ┌─ THE ATTACKER'S OWN PROPERTY, AND NOTHING ELSE ─────────────────────────┐
   │    gBattleMoveDamage = gBattleMons[gBattlerAttacker].level;             │
   │  Seismic Toss and Night Shade: one line, and the target is not read     │
   └─────────────────────────────────────────────────────────────────────────┘

   ───────────────────────────────────────────────────────────────────────────

   WHAT ALL FOUR SHARE

      .power = 1  in every one of their data entries.  The field that
      normally carries the magnitude holds a placeholder, present only so
      the move counts as a damaging one for the routines that test it.
```

## What the product is, and why severity reasoning works inside it

Worth saying before the exceptions, because the contrast is the argument.

Inside the product the inputs and the output move together, monotonically. A heavier attacker
hits harder; a resisted type hits softer; Reflect halves the physical branch and Light Screen the
special one, which this domain's nursing answer on transmission-based precautions shows are two
moves because `CalculateBaseDamage` has two branches split on `IS_TYPE_PHYSICAL`. A player who
knows which terms exist can predict the direction of every change.

Ordinary complications of cancer treatment behave that way. Their magnitude is a monotone function
of the tumour burden, the dose, the number of cycles and the organ function to start with
(**mechanism**). This specialty's answer on why toxicity is predictable derives the list of
affected tissues from turnover rate and the timing from shelf life; its answer on how the systemic
therapies differ derives each class's toxicity profile from its mechanism. Both are descriptions
of a product with known terms.

Grading works on a product too. An ordinal severity scale is useful exactly because the thing
being graded is one thing at different amounts, so a change in grade means a change in amount
(**definitional**). That is what makes toxicity grading the workhorse of dose modification and of
trial reporting.

Each section below breaks that in a different place.

## The shape the cartridge does not have: a closing window

Start with the gap, because inventing a mapping here would be worse than naming it.

**Metastatic compression of the spinal cord** is an emergency because of a window. The cord
tolerates compression for a while and then does not, and the clinically decisive fact is that the
neurological state when treatment begins is the strongest determinant of the neurological state
afterwards — recovery of function already lost is much less reliable than preservation of function
still present (**mechanism**, **consensus**). Pain typically precedes neurological signs, often by
a substantial interval, which is why the history is the instrument rather than the examination.
And the current picture does not contain the quantity that matters, because it does not say how
long the compression has been there.

**Nothing in Emerald has that shape.** The cartridge is full of counters, and not one of them
leaves a mark. The nearest candidate is the Badly Poisoned counter, which the endocrinology and
dermatology answers on that status already own: it increments while the condition persists, and
`DoBattlerEndTurnEffects` caps it with `(status1 & STATUS1_TOXIC_COUNTER) !=
STATUS1_TOXIC_TURN(15)` under a comment reading `// not 16 turns`. It is the one mechanic where
damage is a function of elapsed time.

And then look at what the cure does:

```
   gBattleMons[battler].status1 &= ~(STATUS1_PSN_ANY | STATUS1_TOXIC_COUNTER);
```

The counter is named in the same instruction that clears the status. Somebody had to type
`STATUS1_TOXIC_COUNTER` into the cure to make sure nothing was left behind — which tells you how
deliberately the cartridge refuses to carry residue. **Cure the condition and the elapsed time is
gone as if it never ran.** There is no store anywhere in the battle engine for *harm already done
that the cure cannot reach*, and that is precisely the thing a closing window is.

So the clinical consequence has to be stated without a device: the response to a window is keyed
to the clock rather than to the picture. Urgent imaging of the whole spine rather than of the
painful level alone, because multiple levels are frequently involved; a treatment decision —
radiotherapy, surgical decompression, or both, with systemic measures alongside — taken without
waiting for the picture to declare itself (**consensus**, with pathway details strongly
(**country-dependent**)); and the baseline neurological state recorded, because it is the quantity
that matters.

**Raised pressure inside the skull** from intracranial disease is the same shape with a mechanical
reason behind it. A nearly fixed volume absorbs added volume by displacing cerebrospinal fluid and
blood, and once that compliance is exhausted a small further increase in volume produces a large
increase in pressure (**mechanism**). The relationship between how much disease there is and how
dangerous the situation is turns a corner, and the position of the corner is not visible from
outside. That is a non-linearity, and the game's damage product is linear in every one of its
terms by construction.

## The readout the script deletes on purpose

Here the cartridge is sharper than any analogy I could build.

Every fixed-damage script contains this line, immediately after `typecalc`:

```
	bicbyte gMoveResultFlags, MOVE_RESULT_SUPER_EFFECTIVE | MOVE_RESULT_NOT_VERY_EFFECTIVE
```

`bicbyte` clears bits. It is there because `ModulateDmgByType` would otherwise have set those
flags: its super-effective and not-very-effective branches are guarded only by
`gBattleMoves[gCurrentMove].power`, and these moves have `.power = 1`, which is nonzero. So the
generic path *would* print a grade, and the grade would be a lie — the multiplier never touched
the number, because the number had not been assigned yet. **Somebody deleted the readout rather
than let a false grade reach the screen.**

That is **infection during profound neutropenia**, which is an emergency for a reason that has
nothing to do with how bad the infection is.

Most of what clinicians use to localise and grade an infection is produced by neutrophils:
purulence, the radiographic infiltrate, the local signs of inflammation, much of the visible
reaction at a line site (**mechanism**). Remove the neutrophils and you remove the signal, not the
process. Fever may be the only manifestation, and in some people even fever is absent or blunted
(**consensus**).

Two consequences, both structural.

**The absence of localising signs carries almost no information** about whether there is a serious
infection (**mechanism**). The grading vocabulary is withheld for the same reason the script
withholds it: applying it would produce a confident reading from a mechanism that did not generate
one.

**Treatment precedes the information.** Empirical broad-spectrum antibacterial therapy is started
on suspicion, before the source is known and long before an organism is identified, with cultures
taken but not waited for (**consensus**). Services audit the interval from recognition to the
first dose rather than the interval to a diagnosis (**consensus**, strongly
(**country-dependent**) in which agents and which pathway).

Notice what the `bicbyte` does *not* clear. `MOVE_RESULT_DOESNT_AFFECT_FOE` survives it, so
immunity still works: Night Shade is Ghost-typed and the row `TYPE_GHOST, TYPE_NORMAL,
TYPE_MUL_NO_EFFECT` still zeroes it against a **Snorlax**. The table is consulted for
*whether*, and its gradations are discarded for *how much* — which is the same split as asking
whether this person is at risk at all, a structural question that remains answerable, while
refusing to grade the episode from an examination that cannot grade it.

## Twenty, always: a magnitude neither side contributed to

`setword gBattleMoveDamage, 20` is the whole of Sonic Boom's magnitude. Its data entry is
`.effect = EFFECT_SONICBOOM`, `.power = 1`, `.type = TYPE_NORMAL`, `.accuracy = 90`, `.pp = 20`.
Dragon Rage is the same shape with forty, Dragon type and an accuracy of one hundred. A
**Blissey** and a **Shuckle** take exactly the same twenty, and so does a Blissey behind Reflect
with its Defence at plus six.

That is **hypercalcaemia of malignancy**. The mainstream account is that most cases are humoral —
a factor released by the tumour acts on bone and kidney at a distance, with a
parathyroid-hormone-related peptide mechanism the usual one — alongside a local osteolytic
mechanism where bone is directly involved, and a less common route in some lymphomas acting
through the vitamin D pathway (**mechanism**, **consensus**).

The structural consequence is the one the instruction shows: **the dangerous quantity is decoupled
from bulk.** A circulating concentration is not a tumour dimension, the relationship between how
much tumour there is and how high the calcium is is loose, and a small tumour can produce a large
effect. Symptoms are non-specific — thirst, polyuria, constipation, nausea, confusion — so it is
found by considering it rather than by it announcing itself (**consensus**). And the first
intervention is aimed at the mechanism and not at the tumour: restoration of circulating volume,
because the renal handling of calcium is volume-dependent, and then antiresorptive therapy,
because bone resorption is the source (**consensus**). Treating the cancer is the durable answer
and is not the immediate one.

**Obstruction of the superior vena cava** is the same decoupling with geometry instead of
chemistry, and the game's version of fixed geometry is the move's `.accuracy` and `.target`
fields rather than its power: what matters is the cross-sectional consequence of a mass in a
confined space, how quickly it developed, and whether collateral venous channels have had time to
open — so the severity of the syndrome tracks the rate of onset rather than the size of the
tumour (**mechanism**). Two further points hold. The historical teaching that this condition
requires treatment before a diagnosis has been substantially revised: where it is safe to do so, a
histological diagnosis first is preferred, because the right treatment depends on the tumour type
and some causes are highly treatable (**consensus**). And genuine airway compromise, rather than
facial swelling alone, is what converts it into an immediate-threat situation (**consensus**).

Psywave belongs in this section as the variance case rather than a separate shape. Its damage is
`level * (randDamage + 50) / 100`, where `randDamage` is drawn by rejection — `while ((randDamage
= Random() % 16) > 10);` — then multiplied by ten, giving eleven equally likely multipliers from
half to one and a half. The spread is wide and *none of it comes from the target*. A quantity can
be both highly variable and completely uninformative about the thing you were measuring.

## `dmgtolevel` reads the attacker and nothing else

The shortest command in this answer:

```
   static void Cmd_dmgtolevel(void)
   {
       gBattleMoveDamage = gBattleMons[gBattlerAttacker].level;
       gBattlescriptCurrInstr++;
   }
```

One line. The target is not read. Not its Defence, not its stat stages, not its HP, not its
screens. Seismic Toss and Night Shade share this effect — `.power = 1` both, accuracy one hundred
both — and differ in type, in flags (Seismic Toss carries `FLAG_MAKES_CONTACT` and Night Shade
does not), and in nothing that touches the number.

That is **the metabolic syndrome that follows rapid tumour lysis**, and it inverts the usual logic
in three ways.

**It is a complication of success.** Intracellular contents — potassium, phosphate, and nucleic
acids whose breakdown yields urate — are released into the circulation when a large number of
cells die at once; the resulting disturbance threatens the kidney and the heart, and renal
impairment then worsens the clearance of everything that caused it (**mechanism**). It is most
likely where the tumour is bulky, dividing fast, and highly sensitive to the treatment about to be
given, which are the same features that predict the treatment will work (**mechanism**). The
magnitude comes from the attacker's own property, exactly as in the command: from the tumour, not
from the kidney.

**It is predictable before anything is given.** `gBattleMons[gBattlerAttacker].level` is readable
before the move is chosen. Clinically the risk is estimated from the disease, its bulk, and the
person's renal function at baseline, all available in advance (**consensus**), and the risk
categories are disease-specific rather than generic.

**So it belongs to prevention.** The response is anticipatory: attention to circulating volume and
urine output, urate-lowering treatment chosen by risk category, biochemical monitoring at an
interval set by that category, and the resources to manage a deterioration arranged beforehand
(**consensus**, with agents, thresholds and monitoring intervals (**country-dependent**)). A
syndrome diagnosed and then treated has, in this one case, usually already represented a failure
of anticipation.

The type pair carries the last part of the point, and it is the same structure the answer on how a
cancer spreads found in `sMovesForbiddenToCopy`: a hand-written table with a conditional sentinel
in the middle of it. `TYPE_GHOST, TYPE_NORMAL, TYPE_MUL_NO_EFFECT` sits *before* the
`TYPE_FORESIGHT` sentinel in `gTypeEffectiveness`, so Night Shade is unconditionally zero against
a Normal-type. `TYPE_FIGHTING, TYPE_GHOST, TYPE_MUL_NO_EFFECT` sits *after* it, so Seismic Toss is
zero against a **Gengar** only until somebody uses Foresight. Same arithmetic, two reachability
rules: one barrier is a property of the disease and cannot be changed, and the other is a state
you can alter before you start. That is the difference between a risk category and a prophylaxis.

## Why the classification is the point

The four shapes share one feature: in none of them is the dangerous quantity the same quantity as
*how advanced is the cancer*. Each therefore has to be recognised as itself rather than graded,
and each names its own response (**mechanism**):

* a **window** means the clock is what is being managed, imaging and treatment are not sequenced
  behind reassurance, and the baseline neurological state is recorded;
* a **missing readout** means a normal examination does not change the plan, and treatment starts
  before the information arrives;
* a **remote driver** means the first act is aimed at the mechanism rather than the tumour, and a
  small cancer does not argue against a large effect;
* a **treatment-caused, predictable** hazard means the work is done before the first dose, and the
  question is asked of the disease rather than of the patient's appearance.

And the honest limit, stated where the device is used rather than at the end: real situations are
mixtures, somebody can have more than one of these at once, and several of them share presenting
features with ordinary complications. The game's four effects are cleanly separated because
somebody wrote them into separate scripts. Clinical presentations are not written into separate
scripts, which is the reason the classification is worth learning rather than a reason to doubt
it.

## Where the metaphor stops

Everything above is formulas, tables and flags, and the cartridge is a good place to see them
because the instruction that assigns the damage is right there to read. What follows is about
people, so the analogy stops here and nothing below leans on it.

The person in each of these situations is usually frightened and usually unwell, frequently has
been unwell for a while, and has often already been told something about their cancer that they
are still absorbing. Several of these presentations arrive through a route that was not designed
for them — a call to a helpline, a general emergency department, a routine appointment brought
forward — and the people they meet first may not know the oncological history. That is a system
problem and not a personal failing, and it is why acute oncology services exist where they exist.

Two things follow that matter more than any mechanism above. The first is that the history is
often the whole diagnosis, and getting it requires asking rather than looking. Back pain that has
changed in character, weakness the person has been attributing to tiredness, a rate of change over
days: none of that is on an observation chart. The second is that somebody who has been told to
call if something changes needs the call answered by a route that can act, or the instruction was
decoration.

Nothing in either half of this answer says anything about what will happen to any individual, and
nothing in either half is a protocol. The reasoning is here so that the response written down
where you work makes sense; the response written down where you work is the one to follow. And
nothing in the game stands in for a person in any of this — the subject throughout has been where
a number comes from, which is a property of code and of biology and not of anybody's situation.

## What a Gym Leader is listening for

* `BattleScript_EffectSonicboom` has no `damagecalc` instruction. Which clinical reasoning does
  that absence stand for, and which levers does it disconnect?
* Why does the script need an explicit `bicbyte` to clear two flags, when the moves have
  `.power = 1`?
* `MOVE_RESULT_DOESNT_AFFECT_FOE` survives the `bicbyte`. What is the clinical version of keeping
  *whether* and discarding *how much*?
* The cure clears `STATUS1_TOXIC_COUNTER` by name. What does that tell you about whether the
  cartridge can model a closing window?
* `Cmd_dmgtolevel` does not read the target. Which complication is that, and what follows for when
  the work gets done?
* Night Shade's immunity row sits before the `TYPE_FORESIGHT` sentinel and Seismic Toss's sits
  after it. What is the clinical difference between those two barriers?
* Psywave's spread is wide and none of it comes from the target. What does that separate?
* Where does this analogy break, and why is the break the most useful paragraph on the page?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific to
this answer:

* Your own service's **acute oncology** pathway, and the pathway for suspected metastatic spinal
  cord compression specifically. These name who to contact, what imaging is arranged and in what
  interval, and they differ between institutions even within one country. They are the authority
  for everything operational here.
* Your national guideline for suspected metastatic spinal cord compression, from the body that
  issues guidelines where you work, for the imaging standard and the treatment pathway.
* Your service's **neutropenic sepsis** policy and its empirical antibacterial regimen, which is
  set locally against local resistance patterns and is the only place that regimen should be read.
* Your national guideline on neutropenic sepsis, for the recognition criteria and the interval
  standard.
* The published guidance on prevention and management of the syndrome following rapid tumour lysis
  from the professional body that issues it in your region, for the risk categories and what each
  triggers.
* A current standard textbook of the specialty, for the mechanisms of hypercalcaemia of
  malignancy, for the physiology of a closed cranial compartment, and for the natural history of
  obstruction of the superior vena cava.
* The primary literature, for neurological outcome against the state at presentation in cord
  compression, and for the shift in practice on obtaining a histological diagnosis before treating
  venous obstruction.

The Pokémon side is in the opposite position and is sourced file by file in the closing note.

## Scope and safety

This is revision material about why a handful of complications are emergencies by mechanism,
dressed in a game so that the instruction which assigns the number stays visible. It has had no
clinical review. **It is not a protocol and must not be used as one**, and no dose, agent choice,
threshold, interval or monitoring schedule appears here, deliberately — those are set locally and
nationally, they differ between countries and between institutions in the same country, and they
are revised; the policy in force where you work is the authority and this is not. It says nothing
about what will happen to any individual. Anyone who is unwell now should use their local
emergency number or their acute oncology contact route rather than reading this, and anyone
affected by cancer — their own diagnosis or someone else's — should be talking to the clinical
team looking after that person, who have the history and the examination, neither of which is
here. The analogy carries arithmetic and table lookups only: no part of it stands in for a person,
nothing in it faints, and no creature's situation is the subject of any sentence in it.

## Where this stands, October 2026

The Pokémon facts are read from Emerald's own source and nothing here is claimed about any
generation but the third. In `data/battle_scripts_1.s`, `BattleScript_EffectSonicboom` runs
`attackcanceler`, `accuracycheck`, `attackstring`, `ppreduce`, `typecalc`, then `bicbyte
gMoveResultFlags, MOVE_RESULT_SUPER_EFFECTIVE | MOVE_RESULT_NOT_VERY_EFFECTIVE`, then `setword
gBattleMoveDamage, 20`, `adjustsetdamage` and a jump to `BattleScript_HitFromAtkAnimation`; it
contains no `damagecalc` and no `critcalc`. `BattleScript_EffectDragonRage` is identical with
`setword gBattleMoveDamage, 40`; `BattleScript_EffectLevelDamage` substitutes `dmgtolevel` and
`BattleScript_EffectPsywave` substitutes `psywavedamageeffect`. In `src/battle_script_commands.c`,
`Cmd_damagecalc` calls `CalculateBaseDamage` and multiplies by `gCritMultiplier` and
`gBattleScripting.dmgMultiplier`, doubling again for a charged-up Electric move and applying
fifteen-tenths for Helping Hand; `Cmd_dmgtolevel` is the single assignment `gBattleMoveDamage =
gBattleMons[gBattlerAttacker].level`; `Cmd_psywavedamageeffect` is `while ((randDamage = Random()
% 16) > 10);` then `randDamage *= 10;` then `gBattleMoveDamage =
gBattleMons[gBattlerAttacker].level * (randDamage + 50) / 100`; and `ModulateDmgByType` guards its
super-effective and not-very-effective branches with `gBattleMoves[gCurrentMove].power` while its
no-effect branch carries no such guard. `src/data/battle_moves.h` gives Sonic Boom `.power = 1`,
`.type = TYPE_NORMAL`, `.accuracy = 90`, `.pp = 20`; Dragon Rage `.power = 1`, `.type =
TYPE_DRAGON`, `.accuracy = 100`, `.pp = 10`; Seismic Toss `.power = 1`, `.type = TYPE_FIGHTING`,
`.accuracy = 100`, `.pp = 20`, with `FLAG_MAKES_CONTACT`; Night Shade `.power = 1`, `.type =
TYPE_GHOST`, `.accuracy = 100`, `.pp = 15`, without it; and Psywave `.power = 1`, `.type =
TYPE_PSYCHIC`, `.accuracy = 80`, `.pp = 15`. `gTypeEffectiveness` in `src/battle_main.c` is three
hundred and thirty-six bytes, one hundred and twelve triplets, of which one is the
`TYPE_FORESIGHT` sentinel and one is `TYPE_ENDTABLE`; `TYPE_GHOST, TYPE_NORMAL,
TYPE_MUL_NO_EFFECT` appears before the sentinel and `TYPE_NORMAL, TYPE_GHOST` and `TYPE_FIGHTING,
TYPE_GHOST` after it, and `Cmd_typecalc` breaks out of the scan at the sentinel when the target
carries `STATUS2_FORESIGHT`. In `src/battle_util.c`, `DoBattlerEndTurnEffects` tests `(status1 &
STATUS1_TOXIC_COUNTER) != STATUS1_TOXIC_TURN(15)` under the comment `// not 16 turns`, and the
cure is `gBattleMons[battler].status1 &= ~(STATUS1_PSN_ANY | STATUS1_TOXIC_COUNTER)`.
`include/constants/battle.h` gives `STATUS1_TOXIC_COUNTER` as bits eight to eleven. Snorlax is
Normal-typed and Gengar is Ghost and Poison, from their species entries.

The clinical reasoning is structural and will not date: a window, a missing readout, a driver
remote from the bulk and a hazard generated by successful treatment are four different shapes, and
the response each one implies follows from the shape rather than from current guidance. What moves
is everything operational — which service holds the pathway, what imaging standard applies and in
what interval, which empirical antibacterial regimen is used, which urate-lowering agent suits
which risk category, and whether a histological diagnosis is obtained before treating venous
obstruction in a given centre are all set locally and nationally and are being revised. Risk
stratification for the syndrome following rapid tumour lysis has been extended as newer agents
with rapid cell kill have entered practice; the place of endovascular stenting in venous
obstruction has grown and varies substantially between services. No threshold, agent or interval
is quoted here, deliberately.
