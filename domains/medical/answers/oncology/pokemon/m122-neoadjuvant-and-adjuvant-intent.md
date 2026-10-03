---
id: "m122"
slug: neoadjuvant-and-adjuvant-intent
style: pokemon
category: oncology
difficulty: advanced
question: "Why does the same systemic treatment given before surgery answer a different question from the same treatment given after it?"
tags: [neoadjuvant, adjuvant, treatment-intent, response, trial-design]
---

# `CalculateBaseDamage` is called from two places, and the two calls are not the same call

Emerald computes damage with one function. It is called from exactly two kinds of place, and the
difference between them is this answer.

The first is `Cmd_damagecalc`, in `src/battle_script_commands.c`. It runs inside a move's script,
after the move has been committed to. Its result becomes an effect: HP leaves the bar.

The second is `AI_CalcDmg`, called from the opponent's thinking routines in
`src/battle_ai_script_commands.c`. It runs *before* anything is committed to, over moves that have
not been used. Its result becomes information: a number in `moveDmgs[]` that decides which move
gets chosen.

Same function. Same battlers. Same `gDynamicBasePower`, same `gCritMultiplier`, same
`gBattleScripting.dmgMultiplier`. Put the call before the commitment and you get knowledge. Put it
after, and you get an effect and no knowledge at all, because by the time the number exists the
choice has already been made.

That is neoadjuvant against adjuvant with the machinery exposed. One drug, one dose, one schedule.
Given before the operation, the tumour is still there to be measured, so the treatment is
simultaneously a treatment and a test. Given afterwards, there is nothing left to measure, so it
is a treatment with no test attached — and the thing it is aimed at is disease that is presumed
rather than demonstrated.

And the cartridge is better than the analogy deserves on one point: **the predicting call is not
free, it is not identical to the executing one, and the source says so in a comment.**

As elsewhere in this specialty, **the objects of study are call sites, tables and gates.** No
Pokémon in this answer stands in for a person, and the analogy is dropped entirely at the end
where the subject changes.

Clinical claims carry the same marks as the rigorous half: (**mechanism**), (**definitional**),
(**consensus**), (**country-dependent**).

## The two call sites, drawn

```
   PREDICTING — AI_CalcDmg, before the commitment

      gCurrentMove = moves[checkedMove];
      AI_CalcDmg(sBattler_AI, gBattlerTarget);
      TypeCalc(gCurrentMove, sBattler_AI, gBattlerTarget);
      moveDmgs[checkedMove] = gBattleMoveDamage
                              * AI_THINKING_STRUCT->simulatedRNG[checkedMove] / 100;
      if (moveDmgs[checkedMove] == 0) moveDmgs[checkedMove] = 1;
            │
            ├──► OUTPUT: a number you can compare against three others
            │
            └──► AND THREE THINGS THAT ARE NOT THE SAME AS EXECUTION:
                   ►  gDynamicBasePower = 0   — the estimate WRITES to shared
                      state; running it changes the field it ran on
                   ►  simulatedRNG   — a STAND-IN for the random factor, not
                      the draw that will actually occur
                   ►  TypeCalc, not Cmd_typecalc — and TypeCalc does not set
                      gMoveResultFlags, which the source comments on twice

   ═══════════════════════════════════════════════════════════════════════════

   APPLYING — Cmd_damagecalc, after the commitment

      gBattleMoveDamage = CalculateBaseDamage(...);
      gBattleMoveDamage = gBattleMoveDamage * gCritMultiplier
                                            * gBattleScripting.dmgMultiplier;
            │
            └──► OUTPUT: an effect.  The bar moves.  Nothing is learned that
                 could have changed the choice, because the choice is spent.

   ═══════════════════════════════════════════════════════════════════════════

   AND THE GATE IN FRONT OF THE PREDICTOR

      gBattleMoves[moveConsidered].power > 1            — power 1 is invisible
      sIgnoredPowerfulMoveEffects[] != IGNORED_MOVES_END  — twelve effects skipped

      the predictor estimates DAMAGE.  It therefore cannot see a move whose
      magnitude is assigned elsewhere, and it refuses outright to rank the
      twelve whose real cost is not a damage number.
```

## Applying it: an effect, and no information

`Cmd_damagecalc` is four lines of arithmetic and one increment of the script pointer. It produces
the number and the number is immediately spent. Nothing in the engine compares it with what might
have happened instead, because nothing else happened.

That is adjuvant treatment, and the reason is one biological claim: by the time a primary tumour
is large enough to be found, cells may already have left it, and some of those may be capable of
founding a metastasis later (**mechanism**). This specialty's answer on how a cancer spreads sets
out why the cascade is lossy at every step, which is why the word is *may* in both halves of that
sentence.

Three consequences, all structural.

**There is no target to point at.** The disease being treated is below the detection limit of
every available instrument, or it is not there at all, and nobody can tell which for any
individual at the time of the decision (**mechanism**).

**So there is no per-patient readout, ever.** Nothing shrinks, because there is no lesion. The
only observable is whether the cancer returns, and one person's outcome is one draw: somebody who
takes adjuvant treatment and does not recur may have been cured by the operation alone, and
somebody who recurs may have had the recurrence delayed. Neither case is interpretable. This is
the general- practice argument about an intervention that prevents many cases across a population
while offering almost nobody a benefit they could notice, and the mechanism is the same mechanism
(**mechanism**).

**Therefore the justification can only be a randomised comparison.** Adjuvant therapy is one of
the places where a randomised trial is not the best available evidence but the only possible
evidence, because the counterfactual is unobservable in principle rather than in practice
(**consensus**). This specialty's answer on randomisation against registries sets out why no
amount of adjustment substitutes.

What falls out of that is the familiar clinical shape, and it is worth deriving. Benefit is a
reduction in the risk of recurrence across a population, and the absolute size of that reduction
depends on baseline risk — so the same relative benefit is worth a great deal to somebody at high
risk and very little to somebody at low risk (**mechanism**). The cost, by contrast, is paid up
front with certainty by everybody treated. This specialty's answer on why toxicity is predictable
sets out which tissues and when, and its answer on survivorship sets out the consequences that
arrive years later; all of it is incurred by people who were, in a proportion nobody can identify,
already cured.

## Predicting it: information, and a side effect

Now read the other call site properly, because every line of it earns its place.

```
   void AI_CalcDmg(u8 attacker, u8 defender)
   {
       u16 sideStatus = gSideStatuses[GET_BATTLER_SIDE(defender)];
       gBattleMoveDamage = CalculateBaseDamage(&gBattleMons[attacker], &gBattleMons[defender],
                                               gCurrentMove, sideStatus, gDynamicBasePower,
                                               gBattleStruct->dynamicMoveType, attacker, defender);
       gDynamicBasePower = 0;
       gBattleMoveDamage = gBattleMoveDamage * gCritMultiplier * gBattleScripting.dmgMultiplier;
       ...
   }
```

Line by line it is `Cmd_damagecalc`, with one extra statement in the middle:
`gDynamicBasePower = 0;`. `Cmd_damagecalc` does not have it. **Asking the question clears a global
the battle was holding.** The estimate is not an observation of the system from outside; it is a
write.

Move the same treatment in front of the operation and four things become available, and the fourth
is where that write matters.

**Downstaging, and an operation that was not previously offerable.** Where the limiting problem is
local extent — a structure that cannot be resected, a margin that cannot be obtained — shrinking
the tumour can convert an inoperable situation into an operable one (**consensus**). This is the
oldest and least contested rationale.

**A smaller operation for the same result.** Where surgery is possible but extensive, response can
permit a less destructive procedure: breast conservation instead of mastectomy, sphincter
preservation, a smaller nodal dissection in some settings (**consensus**, with the specific
indications strongly (**country-dependent**)).

**An in-vivo test of sensitivity, which has no adjuvant equivalent.** The tumour is exposed to the
drug while it can still be observed, so the degree of response is measurable: on imaging during
treatment, and definitively in the resected specimen afterwards (**definitional**). A tumour that
has largely or entirely disappeared from the specimen and one that is unchanged are two different
pieces of information about the same person, obtained by the same treatment, and neither is
obtainable once the primary has gone.

**A decision downstream that can use it.** In several diseases the pathological response now
determines what is offered after surgery, with further or different systemic treatment where the
response was poor (**consensus**, one of the fastest-moving areas in the specialty, so strongly
(**country-dependent**) and dated). The engine makes the same point: `moveDmgs[]` exists only
because the next instruction compares it against the other three. A test with nothing attached
would be interesting and not useful — the argument this specialty's answer on biomarker-driven
treatment selection makes about an assay and the drug it selects for.

And one argument that cuts against the usual intuition: treatment given before surgery is given to
somebody who has not yet had an operation, so it is more likely to be delivered at full intensity
than treatment offered to somebody recovering from major surgery (**consensus**). Adjuvant
treatment is frequently delayed, reduced or declined for reasons that have nothing to do with the
cancer.

## What the prediction costs, in three documented ways

`gDynamicBasePower = 0` is the first cost and the cartridge has two more, both sharper.

**The random factor is simulated, not drawn.** The predictor multiplies by a stand-in array,
populated once and used for ranking. The execution path takes its own fresh draw. So the estimate
and the event are the same function over the same inputs, differing in exactly the term neither
side controls — and the gap is not small, because the damage formula's random factor is a real
spread and moves carry real miss rates on top of it. **Blizzard** is a hundred and twenty base
power at seventy accuracy; **Thunder** is the same pair of numbers; **Hydro Pump** is a hundred
and twenty at eighty. An opponent choosing between them is choosing between distributions, and
what then happens to a **Wailord** is one sample from the one it picked.

A response observed in one person is one realisation. It is informative about the drug and the
tumour, and it is not the same object as the number a model produced beforehand.

**The two paths do not even run the same type routine, and the source says so.** The prediction
calls `TypeCalc`; the execution calls `Cmd_typecalc`. And the comment, which appears twice, in
both of the AI's type-effectiveness commands:

```
    // TypeCalc does not assign to gMoveResultFlags, Cmd_typecalc does
    // This makes the check for gMoveResultFlags below always fail
    // This is how you get the "dual non-immunity" glitch, where AI
    // will use ineffective moves on immune pokémon if the second type
    // has a non-neutral, non-immune effectiveness
```

A named consequence, a `#ifdef BUGFIX` beside it, and the whole thing written down by somebody who
found it. **The readout available before the commitment is produced by different code from the
readout available after it, and it silently loses a field.**

That is the clinical point about the specimen, exactly. Pathological assessment after systemic
therapy is assessment of *treated tissue*: extent is altered, nodes may have been cleared, and
there may be fibrosis where tumour was. This is why the staging notation distinguishes clinical
assessment, assessment of the resected specimen, and assessment of a specimen resected after
pre-operative systemic therapy — this specialty's answer on staging against grading makes the
point that a prefix says where the information came from and that the three must not be pooled
(**definitional**). Somebody who pools them is comparing populations measured by different
instruments, which is the `TypeCalc` comment restated in a pathology report.

Two more costs follow and neither has a mechanic:

**Time passes with the primary in place.** Most tumours treated this way respond or remain stable.
A minority progress during treatment, and where an operation was available at the start,
progression can remove it (**mechanism**, **consensus**). That is the central argument against the
approach in any disease where the operation alone would have been curative in most people.

**The pre-treatment information has to be gathered more carefully, and sometimes it cannot be.**
Because the operation will no longer establish the baseline, everything the untreated specimen
would have shown must come from biopsy and imaging first — a smaller sample, with the limitations
this specialty's answer on tumour heterogeneity and the single biopsy describes, standing in for a
whole resection (**mechanism**).

## The gate at `power > 1`, and the twelve the predictor refuses

Two conditions sit in front of every prediction:

```
   if (gBattleMoves[gBattleMons[sBattler_AI].moves[checkedMove]].power > 1
       && sIgnoredPowerfulMoveEffects[i] == IGNORED_MOVES_END)
```

The first is `power > 1`. This specialty's answer on the oncological emergencies is about the
family whose power fields all read one — **Sonic Boom**, **Dragon Rage**, **Seismic Toss**,
**Night Shade**, **Psywave** — because their magnitude is assigned directly rather than computed.
**Those are precisely the moves the predictor cannot see.**

Make it concrete. Give a **Machamp** two attacks: **Cross Chop** at a hundred base power and
eighty accuracy, and **Seismic Toss**, which simply deals damage equal to Machamp's own level
against anything it can reach. Against a **Blissey** — enormous HP, feeble physical defence —
Seismic Toss is the predictable one and Cross Chop is the gamble. The predictor ranks **only Cross
Chop**. Seismic Toss's power field reads one, the gate rejects it, and it is scored as doing
nothing at all. The estimator is blind to the option whose magnitude is *certain*, because
certainty here comes from not being in the formula.

A pre-treatment estimate of recurrence risk is in the same position with respect to a
mechanism-driven emergency: the model's output is a probability of recurrence, and nothing about
that quantity contains the hazards that are not on its dial.

The second condition is an exclusion list, twelve entries and a sentinel:

```
   static const u16 sIgnoredPowerfulMoveEffects[] =
   {
       EFFECT_EXPLOSION, EFFECT_DREAM_EATER, EFFECT_RAZOR_WIND, EFFECT_SKY_ATTACK,
       EFFECT_RECHARGE, EFFECT_SKULL_BASH, EFFECT_SOLAR_BEAM, EFFECT_SPIT_UP,
       EFFECT_FOCUS_PUNCH, EFFECT_SUPERPOWER, EFFECT_ERUPTION, EFFECT_OVERHEAT,
       IGNORED_MOVES_END
   };
```

Read what they have in common. Explosion ends the user's participation. Razor Wind, Sky Attack,
Skull Bash and Solar Beam spend a turn first. Recharge spends one after — the pharmacology
answer's Hyper Beam, which always recharges. Superpower and Overheat drop the user's own stats on
success. Spit Up and Focus Punch fail on a condition set earlier in the turn. Eruption scales with
the user's remaining HP. **Every one of them carries a cost or a condition that is not a damage
number**, and the predictor, whose whole output is a damage number, declines to rank them at all
rather than rank them wrongly.

That is the honest shape of a model used for a sequencing decision. An estimate of recurrence-risk
reduction says nothing about a late effect, because a late effect is not in the quantity being
estimated — which is why this specialty's answer on survivorship treats the record of what was
given as the organising document, and why the decision to give adjuvant treatment is not the same
object as the model that supports it (**mechanism**). Declining to rank is a better behaviour than
ranking on an incomplete number, and the cartridge chose it.

## Where the two placements are genuinely equivalent, and where they are not

The honest position is that this is disease-specific, and asserting a general answer would be
wrong.

In several diseases, trials comparing the two placements of the same regimen have found similar
long-term outcomes, with the neoadjuvant placement offering surgical and informational advantages
rather than a survival advantage (**consensus**). There the choice is made on the surgical
question and on the value of the response information, which is a legitimate basis and not a
fudge.

In others they are not interchangeable at all: where the standard regimen differs before and after
surgery, where the operation alone is curative in most people, or where the disease responds
poorly enough that waiting is a real hazard (**consensus**, **country-dependent**).

What generalises is the asymmetry of information, and there the cartridge has the last word.
`Cmd_damagecalc` and `AI_CalcDmg` wrap the same function, and one of them is the only one of the
two that can be compared against an alternative — and even that one is paying for the privilege
with a write to a global, a simulated random factor and a type routine that loses a field.

## Where the metaphor stops

Everything above is call sites, globals and exclusion lists, and the cartridge is a good place to
see them because the same function appears in both paths and the differences are three lines you
can count. What follows is about people, so the analogy stops and nothing below leans on it.

Somebody being offered adjuvant treatment is being asked to accept certain harm now for a benefit
nobody will ever be able to confirm they received. That is a genuinely difficult thing to be told
and it is frequently told badly — in relative terms that sound larger than the absolute change, or
in a form that implies the treatment is a continuation of the operation rather than a separate
decision with its own balance. People are entitled to the absolute numbers for their own
situation, and they are entitled to decline. Somebody who declines has not made a mistake; they
have weighted a trade differently.

Somebody being offered neoadjuvant treatment is being asked to wait, with a cancer in their body
that they know is there, while treatment that may or may not be working happens first. The waiting
is the hard part and it is not made easier by being told that it is informationally efficient. The
question people actually ask — *what if it grows while we wait* — is the right question, is not
neurotic, and deserves a direct answer about what is monitored and what would happen if it did.

Neither conversation is improved by precision about mechanism. Both are improved by saying what is
known, what is not, what this person's own numbers are, and that the decision is theirs. Nothing
in either half of this answer says anything about what will happen to any individual, and no
clinical figure of any kind appears in either half. Both omissions are deliberate. And nothing in
the game stands in for a person anywhere in it: the subject throughout has been where a number
comes from and what it can be compared against.

## What a Gym Leader is listening for

* `CalculateBaseDamage` is called from two places. Name the clinical difference the two call sites
  stand for.
* `AI_CalcDmg` contains `gDynamicBasePower = 0` and `Cmd_damagecalc` does not. What is the
  clinical version of an estimate that writes to the thing it estimated?
* Why is `simulatedRNG` the right picture of the difference between a modelled benefit and an
  observed response?
* The source comments twice that `TypeCalc` does not set `gMoveResultFlags`. Which pathology
  convention is that comment, and what goes wrong when it is ignored?
* The predictor is gated on `power > 1`. Which complications does a recurrence-risk model have the
  same blind spot for?
* Read `sIgnoredPowerfulMoveEffects` and say what its twelve entries have in common. What does the
  predictor do about it, and why is that the right behaviour?
* Why can an individual never know whether their adjuvant treatment worked?
* Why is pathological response such an attractive trial endpoint, and what is the catch?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific to
this answer:

* Your national guideline for the specific disease in question, which is the only place the
  sequencing question is actually answered. Whether a regimen is given before or after surgery,
  and what a poor pathological response triggers, are disease-specific and differ between
  countries.
* The current edition of the anatomical staging classification used where you work, for the
  notation that distinguishes clinical assessment, pathological assessment and assessment after
  pre-operative therapy. The edition matters.
* Your own institution's protocols for the regimens concerned, and its multidisciplinary meeting's
  record of how the sequencing decision is made for each disease.
* The published guidance on reporting pathological response from the pathology body that issues it
  in your region. The grading systems differ between diseases and the reporting standard defines
  them.
* A current standard textbook of the specialty, for the rationale of adjuvant therapy and for the
  history of neoadjuvant trials in the diseases where the two placements have been compared
  directly.
* The primary literature, for the trials comparing the two placements of a single regimen, and for
  the strength of the relationship between pathological response and long-term outcome in each
  disease. The second is the claim here most likely to have moved.

The Pokémon side is in the opposite position and is sourced file by file in the closing note.

## Scope and safety

This is revision material about treatment intent and sequencing, dressed in a game so that the
difference between estimating a quantity and causing it stays visible. It has had no clinical
review. **No regimen, dose, interval, response threshold or sequencing recommendation for any
disease appears here, and none should be inferred** — the sequencing question is answered disease
by disease, the answers differ between countries and institutions, and they are being revised
quickly; the guideline and protocol in force where you work are the authority and this is not. It
is not a decision aid, it says nothing about what will happen to any individual, and it describes
no individual's situation. Anyone affected by cancer — their own diagnosis or someone else's —
should be talking to the clinical team looking after that person, who have the history, the
pathology and the imaging, none of which is here. The analogy carries call sites and arithmetic
only: no part of it stands in for a person, and no creature's situation is the subject of any
sentence in it.

## Where this stands, October 2026

The Pokémon facts are read from Emerald's own source and nothing here is claimed about any
generation but the third. `Cmd_damagecalc` in `src/battle_script_commands.c` calls
`CalculateBaseDamage` with `gSideStatuses[GET_BATTLER_SIDE(gBattlerTarget)]`, `gDynamicBasePower`
and `gBattleStruct->dynamicMoveType`, then multiplies by `gCritMultiplier` and
`gBattleScripting.dmgMultiplier`, doubles again for a charged-up Electric move and applies
fifteen-tenths for Helping Hand. `AI_CalcDmg`, in the same file, is the same sequence with
`gDynamicBasePower = 0;` inserted after the `CalculateBaseDamage` call and before the
multiplications. In `src/battle_ai_script_commands.c`, `Cmd_get_how_powerful_move_is` loops over
`MAX_MON_MOVES`, requires `gBattleMoves[...].power > 1` and that the move's effect is absent from
`sIgnoredPowerfulMoveEffects`, calls `AI_CalcDmg` then `TypeCalc`, and stores `gBattleMoveDamage *
AI_THINKING_STRUCT->simulatedRNG[checkedMove] / 100` with a floor of one.
`sIgnoredPowerfulMoveEffects` holds twelve effects — `EFFECT_EXPLOSION`, `EFFECT_DREAM_EATER`,
`EFFECT_RAZOR_WIND`, `EFFECT_SKY_ATTACK`, `EFFECT_RECHARGE`, `EFFECT_SKULL_BASH`,
`EFFECT_SOLAR_BEAM`, `EFFECT_SPIT_UP`, `EFFECT_FOCUS_PUNCH`, `EFFECT_SUPERPOWER`,
`EFFECT_ERUPTION`, `EFFECT_OVERHEAT` — terminated by `IGNORED_MOVES_END`. The comment quoted above
appears in both `Cmd_get_highest_type_effectiveness` and `Cmd_if_type_effectiveness`, each beside
an `#ifdef BUGFIX` that assigns `TypeCalc`'s return to `gMoveResultFlags`; two further AI commands
gate on `gBattleMoves[AI_THINKING_STRUCT->moveConsidered].power < 2` and return without
estimating. `Cmd_get_highest_type_effectiveness` seeds `gBattleMoveDamage = 40` and reads the
result back against the constants `AI_EFFECTIVENESS_x2`, `AI_EFFECTIVENESS_x4`,
`AI_EFFECTIVENESS_x0_5`, `AI_EFFECTIVENESS_x0_25` and `AI_EFFECTIVENESS_x0`.

The clinical reasoning will not date in its informational half: a treatment given while the tumour
is present produces a measurement and one given afterwards does not; a target that cannot be seen
can only be studied at population level; a test that alters the specimen is not free. Almost
everything else is moving, and in one direction — towards the neoadjuvant placement in more
diseases, and towards response-adapted treatment after surgery. What a poor pathological response
triggers has changed substantially in several diseases within the past few years and will change
again. The use of circulating markers of residual disease to give adjuvant treatment a readout it
has never had is an active area with no settled place, and if it becomes routine it would alter
the central asymmetry this answer is built on, which is worth saying plainly rather than leaving
for a reader to find. No regimen, threshold or indication is quoted here, deliberately.
