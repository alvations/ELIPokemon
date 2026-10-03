---
id: "m129"
slug: electrolyte-derangement-as-a-syndrome
style: pokemon
category: emergency
difficulty: advanced
question: "Why is electrolyte and metabolic derangement better understood as a presenting syndrome than as a laboratory finding?"
tags: [electrolytes, metabolic, excitability, correction, revision]
---

# Seven numbers nothing displays, each multiplying into a different calculation

`gBattleMons[battler].statStages` is an array of `NUM_BATTLE_STATS` entries, which is `NUM_STATS +
2` — eight slots: HP, Attack, Defence, Speed, Special Attack, Special Defence, Accuracy and
Evasion. `STAT_HP` is slot 0 and the battle engine never reads it, because there is no HP stat
stage; it is set to the neutral value at switch-in and sits there. So the panel is eight entries
wide and **seven of them do anything**, which is already a fact about the layout rather than about
the biology.

Nothing in the third generation displays any of them. The healthbox draws HP, a level, a name and
one status graphic from `MON_DATA_STATUS` — question m126 reads that function in full — and
`statStages` is not among the things it consults. There is no screen in the battle menu that shows
a stage. The only two ways a player ever learns the value are the message printed at the moment it
changed, and the output of the next calculation being wrong.

That is the whole shape of this answer. **A parameter that is read by everything and shown by
nothing presents as the behaviour of the system, and is confirmed by a number you have to go and
get.**

## The stored value and the reported value differ by a constant

```
   #define MIN_STAT_STAGE      0
   #define DEFAULT_STAT_STAGE  6
   #define MAX_STAT_STAGE     12
```

Everybody talks about stat stages as running from `−6` to `+6`. The storage runs from `0` to `12`.
The two differ by `DEFAULT_STAT_STAGE`, and the consequence is sharp: **`0` in the array is the
floor, not the neutral value.** A reader who sees a zero and reads it as *unchanged* has read the
worst possible state as normal, and the only thing standing between those two readings is knowing
which convention the number is in. The offset is why question m128's accuracy formula has to add
`DEFAULT_STAT_STAGE` back in after subtracting one stage from another.

## One stage is not one quantity, and the table says so

`gStatStageRatios` is thirteen pairs in `src/pokemon.c`, applied by `APPLY_STAT_MOD`:

```
   {10, 40}  -6   = x0.250        {15, 10}  +1 = x1.500
   {10, 35}  -5   = x0.286        {20, 10}  +2 = x2.000
   {10, 30}  -4   = x0.333        {25, 10}  +3 = x2.500
   {10, 25}  -3   = x0.400        {30, 10}  +4 = x3.000
   {10, 20}  -2   = x0.500        {35, 10}  +5 = x3.500
   {10, 15}  -1   = x0.667        {40, 10}  +6 = x4.000
   {10, 10}   0   = x1.000
```

Read down the left column and the increments shrink: the step from `0` to `−1` moves the
multiplier by `0.333`, and the step from `−5` to `−6` moves it by `0.036`. **The same single stage
is worth roughly ten times as much near the middle as it is near the floor.** Read up the right
column and they are constant: every step up adds exactly `0.5`. One table, two completely
different senses of what "one stage" costs, depending on which direction and where you started
from.

And the accuracy and evasion slots do not use that table at all. They use `sAccuracyStageRatios`,
a separate thirteen-entry array in `src/battle_script_commands.c` running `{33, 100}` at `−6`
through `{1, 1}` at neutral to `{3, 1}` at `+6`. So two of the eight slots in one array are scaled
by one function and six by another, and the ranges differ — a quarter to four times against a
third to three times. *Which entry moved* changes what the movement means, and nothing in the
array itself records that.

Here the analogy's limit has to be stated where the device is used rather than at the end. The
engine's non-linearity is in the **level**: the table says a step is worth less at the extremes.
The clinical non-linearity is largely in the **rate**: the same value matters differently
according to how fast it arrived. Those are not the same shape, and the table is a model of the
first and not of the second. What it does carry correctly is the more basic point — that a
numerically equal change in a parameter is not an equal change in consequence, and that the
reference point has to be known before the change can be read.

## The multiplier is applied at use time, and the stored stat never moves

```
   #define APPLY_STAT_MOD(var, mon, stat, statIndex)                      \
   {                                                                      \
       (var)  = (stat) * (gStatStageRatios)[(mon)->statStages[(statIndex)]][0]; \
       (var) /= (gStatStageRatios)[(mon)->statStages[(statIndex)]][1];     \
   }
```

The stored `attack` field is not touched. It is read, multiplied and discarded, and the product
exists only for the duration of one calculation. The summary screen shows the stored number.

So two Pokémon of the same species, level and nature, with identical numbers on the summary
screen, can behave completely differently — and the summary screen is right about what it reports
and silent about everything that modifies it. `GetWhoStrikesFirst` in `src/battle_main.c` does
exactly this with Speed: it reads the stored value, applies `gStatStageRatios` for the Speed slot,
and only then compares. Metagross at base Speed 70, Tentacruel at 100 and Skarmory at 70 are three
stored numbers that predict turn order only if you also know three invisible ones.

The convention this is reusing, and worth naming: question m006's Super Fang point is that a
proportion and an absolute are different quantities. This is the same distinction one level down —
a stored amount and an effective amount are different quantities, and the readout shows the one
that does not vary.

## Protection against the parameter moving is six hand-written checks in one function

`ChangeStatBuffs`, decrease branch, in order:

```
   gSideTimers[side].mistTimer         && !certain && move != MOVE_CURSE  -> BattleScript_MistProtected
   move != MOVE_CURSE && JumpIfMoveAffectedByProtect(0)                   -> BattleScript_ButItFailed
   ability == CLEAR_BODY || WHITE_SMOKE && !certain && move != MOVE_CURSE  -> BattleScript_AbilityNoStatLoss
   ability == KEEN_EYE     && !certain && statId == STAT_ACC              -> AbilityNoSpecificStatLoss
   ability == HYPER_CUTTER && !certain && statId == STAT_ATK              -> AbilityNoSpecificStatLoss
   ability == SHIELD_DUST  && flags == 0                                  -> (silent)
```

Six refusal sites, three blanket and two stat-specific, each written out by hand with its own
message, and **four of them repeat the same two exemptions** — a `certain` reduction and Curse by
name. This is the correction in `CONVENTIONS.md` Part IV: Mist and Clear Body do *not* block every
stat reduction, and the carve-outs are visible in the source. Clear Body is Metagross and
Tentacruel; White Smoke is the equivalent written as a second ability name; Keen Eye on Skarmory
protects accuracy and nothing else; Hyper Cutter on Pinsir and Mawile protects Attack and nothing
else. A blanket protection and a stat-specific one are not the same object, and asking *is this
protected* has no answer until you say which slot.

## The floor and the ceiling are not handled symmetrically

The end of the same function:

```
   if (statStages[statId] == MIN_STAT_STAGE) MULTISTRING_CHOOSER = B_MSG_STAT_WONT_DECREASE;
   ...
   if (statStages[statId] == MAX_STAT_STAGE) MULTISTRING_CHOOSER = B_MSG_STAT_WONT_INCREASE;

   statStages[statId] += statValue;
   if (statStages[statId] < MIN_STAT_STAGE) statStages[statId] = MIN_STAT_STAGE;
   if (statStages[statId] > MAX_STAT_STAGE) statStages[statId] = MAX_STAT_STAGE;

   if (MULTISTRING_CHOOSER == B_MSG_STAT_WONT_INCREASE && flags & STAT_CHANGE_ALLOW_PTR)
       gMoveResultFlags |= MOVE_RESULT_MISSED;
   if (MULTISTRING_CHOOSER == B_MSG_STAT_WONT_INCREASE && !(flags & STAT_CHANGE_ALLOW_PTR))
       return STAT_CHANGE_DIDNT_WORK;

   return STAT_CHANGE_WORKED;
```

`B_MSG_STAT_WONT_INCREASE` is tested twice afterwards. **`B_MSG_STAT_WONT_DECREASE` is tested
nowhere.** So a Swords Dance into a maxed Attack slot reports as a *miss* and returns
`STAT_CHANGE_DIDNT_WORK`, while a Growl or a Screech into a floored slot prints its message and
returns `STAT_CHANGE_WORKED`. Same bound, same array, opposite ends, and the engine reports one as
a failure and one as a success.

Swords Dance is `EFFECT_ATTACK_UP_2`, accuracy 0, 30 PP; Agility is `EFFECT_SPEED_UP_2`; Harden is
`EFFECT_DEFENSE_UP`; Double Team is `EFFECT_EVASION_UP`. Against them, Growl is
`EFFECT_ATTACK_DOWN` at accuracy 100 and 40 PP, Screech is `EFFECT_DEFENSE_DOWN_2` at accuracy 85,
and Sand Attack is `EFFECT_ACCURACY_DOWN`. The raising moves mostly carry accuracy 0 and never
miss; several of the lowering ones carry a real accuracy and can. Up and down are different moves
with different failure modes acting on one array, which is the asymmetry again, one level higher.

## Correction is bilateral, total, and does not undo anything else

`Cmd_normalisebuffs` is Haze, and it is six lines:

```
   for (i = 0; i < gBattlersCount; i++)
       for (j = 0; j < NUM_BATTLE_STATS; j++)
           gBattleMons[i].statStages[j] = DEFAULT_STAT_STAGE;
```

Every battler on the field. Every slot. One pass, no timer, no gradation, and
`STRINGID_STATCHANGESGONE` printed once. Haze's entry is power 0, Ice type, accuracy 0 — so it
cannot miss — 30 PP, and `MOVE_TARGET_USER`, which makes it a move that targets itself and
rewrites the opponent. Ekans learns it at 44, Zubat at 46, Koffing and Weezing at 33, Murkrow at
22, Surskit at 37, Vaporeon at 42, Seviper at 43, Wooper at 51, Arbok and Golbat and Crobat at 56,
Quagsire at 61.

And the thing it does not do is the point. `SwitchInClearSetData` does the same reset on one
battler when it leaves the field — all eight slots back to `DEFAULT_STAT_STAGE`, `status2` zeroed,
`gStatuses3` zeroed, the whole `DisableStruct` wiped byte by byte — and it **never touches
`status1`**. So a Pokémon that was burned while its Attack was floored comes back with a neutral
panel and the burn. Normalising every parameter does not undo what happened while they were
abnormal. Question m070 reads that function for what crosses a boundary; this is the reading where
what crosses is the consequence and what is reset is the cause.

## Where the game has nothing

Two absences, and reporting them is better than inventing a mapping.

**There is no half-stage.** `statValue` is a whole number of stages and `GET_STAT_BUFF_VALUE`
extracts one; the array is `u8` indices into a thirteen-entry table. The engine therefore has no
representation of a parameter moving gradually, and no finer resolution to reason about.
Everything is a step.

**Nothing anywhere reads the rate.** No mechanic in the third generation asks how fast a stage
moved, how long it has been where it is, or by what path it arrived. There is no timestamp on a
stat stage and no history of one. Since the rate of change is the single most important thing
about the quantity this is standing for, the engine is simply silent on the most important
variable, and that silence is the honest report rather than something to paper over.

## Where the metaphor stops

Plain prose from here, with no game in it, because the subject is somebody who may be confused,
frightened and disbelieved.

A laboratory result is the usual way a clinician meets an electrolyte derangement, and that order
of encounter teaches the wrong model: the number arrives, it is outside a printed range, it is
treated as the problem, and the problem is treated by moving it back. The better model is the
reverse. Sodium, potassium, calcium, magnesium, phosphate, glucose and hydrogen ion concentration
are **parameters in the equations governing excitable tissue and enzyme function**, not findings
that happen to be measurable. They shift the operating point of every nerve, every muscle fibre
including cardiac muscle, every secretory cell and every enzyme at once, so the presentation is a
syndrome — confusion, weakness, seizure, arrhythmia, ileus, tetany, reduced consciousness — and
the value is the confirmation of a hypothesis the bedside generated. (**Mechanism.**)

The output set is wide and the mapping from output to cause is not invertible: somebody confused
and weak is consistent with a derangement of any of several ions, with sepsis, with a drug effect,
with a structural neurological event and with much else. (**Mechanism.**) Two corollaries make
this an emergency topic. The first manifestation can be the most dangerous one, because for some
derangements the cardiac consequence does not arrive after a sequence of milder warnings, so the
derangement is not graded by how unwell the person currently looks. (**Consensus.**) And several
move together — these ions share causes in gastrointestinal losses, renal handling, diuretics,
refeeding and endocrine disease — so finding one raises the probability of the others, and in some
well-recognised pairings correcting one is futile until the other has been addressed; the specific
pairings and their management are formulary and guideline material and are not described here.
(**Consensus.**)

The rate of change does more work than the value, because the tissues adapt: cells move solute and
water, the brain adjusts its own osmolality over hours to days, and an adapted tissue tolerates a
value an unadapted one does not. (**Mechanism.**) So the same number can be incidental in one
person and an emergency in another, with the slope as the only difference; a previous result is
therefore part of the test, since a value with no prior is a level with no derivative — the same
structural point as the single abdominal examination in question m126. And correction has a rate
of its own which is an intervention with its own harms, because the adaptation that made the
abnormal value tolerable makes the normal one intolerable, which is why correction is prescribed
as a rate with a ceiling and monitored against it rather than as a target to be reached.
(**Consensus** for rate-limited correction; (**country-dependent**) for every number attached to
it.) The high and low states of one ion are also not mirror images — different presentations,
different speeds, different first manifestations, different treatments — and a reader who learned
the two-sided reference range as *too much or too little of the same thing* learned a symmetry
that is not there. (**Consensus.**)

And what is measured is not what is present. The number is a concentration in one compartment, not
a total body amount; it is the result of a distribution that can shift in minutes; it is a
measurement on a specimen whose handling, site and collection can change it, so the first response
to an implausible result is to ask whether the specimen explains it; and for the ions carried
partly bound, the measured total and the active fraction diverge whenever the binding partner or
the pH moves, which is exactly when the patient is unwell. (**Consensus** for the pre-analytic
point; (**mechanism**) for the rest.) A normal concentration with a large total deficit is
routine, and so is a concentration that moves with no change in total content. No reference range,
threshold, correction rate, monitoring interval, fluid, agent, dose or electrocardiographic
criterion appears in this answer, because they are local, several are actively revised, and this
is precisely the area in which a remembered number does harm.

What is at stake for a person is not in any of that. The presentation is frequently behavioural,
and behaviour is the presentation most likely to be attributed to the person rather than to a
mechanism: confusion, agitation, drowsiness, apparent uncooperativeness, slurred speech,
unsteadiness, a change in personality are all produced by metabolic derangement and are all also
what a frightened, exhausted or unwell person looks like, and all are routinely attributed to
intoxication, to dementia, to a psychiatric cause or to difficulty. The label then suppresses the
search — the same mechanism as question m105, where a word naming the location of a cause is read
as naming the absence of one — and the person least likely to be believed is the one whose
presentation is most likely to be metabolic. The information needed to interpret the number also
lives with the person and whoever is with them: what has been going in and coming out and for how
long, which medicines and which were started or changed recently, whether there has been a period
of eating almost nothing. Someone who is confused cannot supply that, so the account of whoever is
with them is not background but the history, and often the only route to the mechanism. Bloods
hurt and repeated bloods hurt more, so a plan involving repeated sampling should be explained
rather than simply happening to someone — which is also what makes the fifth sample possible.
Someone whose confusion has resolved after correction often has no memory of a period in which
they were frightened and behaved unlike themselves, and may have been told about it afterwards;
that deserves care. Nothing about prognosis or outcome appears anywhere in this answer, which is
deliberate.

No Pokémon stands for a patient anywhere in this answer. No creature is unwell, nothing is
deranged, and no stat stands for anybody's physiology. The game is carrying four narrow ideas:
that a parameter read by every calculation and displayed by none presents as the behaviour of the
system rather than as a reading; that a numerically equal change is not an equal change in
consequence, and that the reference point has to be known before any change can be read at all;
that the stored number and the effective number are different quantities and the readout shows the
one that does not vary; and that normalising every parameter at once does not undo what happened
while they were abnormal. Confusion, disbelief, repeated needles and the memory of having behaved
unlike oneself are stated above without ornament and are not mechanics.

## What a Gym Leader is listening for

* How many slots does `statStages` have, how many does the battle engine read, and which one does
  it ignore?
* Name the two ways a player can ever learn a stat stage in the third generation.
* `MIN_STAT_STAGE` is 0 and `DEFAULT_STAT_STAGE` is 6. What goes wrong if you confuse the
  conventions?
* In `gStatStageRatios`, compare the step from 0 to −1 with the step from −5 to −6.
* Which two slots do not use that table, and what do they use instead?
* `APPLY_STAT_MOD` leaves the stored stat alone. What does the summary screen therefore show?
* List the six refusal sites in the decrease branch of `ChangeStatBuffs`, and say which two are
  stat-specific.
* Which two exemptions are written out by hand at four of those sites?
* A blocked increase and a blocked decrease return different things. What, and why does that
  matter?
* What does `Cmd_normalisebuffs` reset, and name one thing it does not.
* Name the two things this engine has no representation of at all.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md), and they
apply here. Specific to this answer:

* A current standard textbook of **medical physiology** and one of **clinical chemistry**, for the
  relationship between plasma concentration, membrane potential and enzyme function, for
  compartment distribution, and for bound and unbound fractions.
* The current national guidance on each specific derangement, issued by **the reader's national
  guideline body or the relevant national specialist society** — nephrology, endocrinology and
  intensive care societies all publish here and do not agree in every particular. These documents
  carry the thresholds, correction rates and monitoring intervals, none of which appears here.
* **The reader's national formulary**, for every fluid, replacement preparation, route and
  monitoring requirement.
* **The reader's own laboratory's** reference ranges, assay methods and sample-handling
  requirements, which are assay-specific and local — one reason no range is stated here.
* **The reader's own employing organisation's** policy on administration and monitoring of
  replacement, which is procedural and which the reader will be held to.

Markers used in the plain-prose section above: (**mechanism**) (follows from physiology or the
structure of the problem and is checkable by reasoning), (**consensus**) (agreed across mainstream
sources as of writing), (**country-dependent**) (genuinely differs between countries,
laboratories, services or institutions). No reference range, threshold, correction rate,
monitoring interval, fluid, agent, dose or electrocardiographic criterion is given, and nothing is
quoted, because none of these was opened. The Pokémon side is in the opposite position and is
sourced file by file in the closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *why a class of abnormalities presents as behaviour and is
confirmed by a number*, written for someone already trained, and the Pokémon framing covers only
hidden parameters, non-linear scaling, stored against effective values, and what a reset does not
undo. It is deliberately not a protocol and not a decision aid: no reference range, no threshold,
no correction rate, no monitoring interval, no fluid, no replacement preparation, no agent, no
dose and no electrocardiographic criterion, and it is not something to consult while assessing or
treating anyone. Replacement and correction are areas in which an error causes direct harm, and
the formulary and the local protocol are the only acceptable sources. Reference ranges are
assay-specific and laboratory-specific; correction guidance differs between national bodies and
between specialist societies within one country. The reader's own formulary, laboratory and local
policy are the authority; this is not, and it has had no clinical review. Nothing here describes
any real person.

## Where this stands, October 2026

The Pokémon facts are pinned to source and are stable. `NUM_BATTLE_STATS` as `NUM_STATS + 2`,
`STAT_ACC` as 6 and `STAT_EVASION` as 7 with the comment that both are battle-only, and
`MIN_STAT_STAGE` 0, `DEFAULT_STAT_STAGE` 6 and `MAX_STAT_STAGE` 12 are read from
`include/constants/pokemon.h`. `gStatStageRatios`'s thirteen pairs from `{10, 40}` to `{40, 10}`
and the `APPLY_STAT_MOD` macro are from `src/pokemon.c`; `GetWhoStrikesFirst` applying that table
to the stored Speed is from `src/battle_main.c`, as is `SwitchInClearSetData` resetting all eight
slots, `status2`, `gStatuses3` and the whole `DisableStruct` while never touching `status1`.
`sAccuracyStageRatios`'s separate thirteen entries from `{33, 100}` to `{3, 1}`, the six refusal
sites in the decrease branch of `ChangeStatBuffs` with their `!certain` and `MOVE_CURSE`
exemptions, the clamp, and the asymmetric testing of `B_MSG_STAT_WONT_INCREASE` against
`B_MSG_STAT_WONT_DECREASE` are from `src/battle_script_commands.c`, as is `Cmd_normalisebuffs`.
The move entries for Haze, Swords Dance, Agility, Harden, Double Team, Growl, Screech and Sand
Attack are from `src/data/battle_moves.h`, the Haze level-up entries from
`src/data/pokemon/level_up_learnsets.h`, and Metagross's and Tentacruel's Clear Body, Skarmory's
Keen Eye and Pinsir's and Mawile's Hyper Cutter from `src/data/pokemon/species_info.h`. All of it
is **third generation**, read from `pokeemerald`; the stat-stage multiplier tables, the protecting
abilities and the display all change in later generations, so a reader checking today's game
should read today's game. On the clinical side the physiology is stable and the numbers are not,
and the gap is unusually wide here: reference ranges are assay-specific and revised by
laboratories, correction-rate recommendations differ between national bodies and between
nephrology, endocrinology and intensive-care sources and are periodically restudied, available
preparations and licensed routes differ by country, some of these syndromes have been reclassified
more than once, and electrocardiographic interpretation in this area is taught differently in
different places. Principle dated October 2026; read the current national guidance, the current
formulary and the reader's own laboratory's documentation for anything past the principle.
