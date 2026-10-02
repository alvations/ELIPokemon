---
id: "m096"
slug: targeted-therapy-and-resistance
style: pokemon
category: oncology
difficulty: advanced
question: "Why does a targeted therapy that is working stop working, and what does the mechanism of escape tell you about what to do next?"
tags: [targeted-therapy, resistance, biomarkers, progression, mechanism]
---

# Kecleon's type changes to the move that just worked, and it only changes when the move worked

Read `AbilityBattleEffects` in the Emerald decompilation, case `ABILITYEFFECT_ON_DAMAGE`, and
**Color Change** is six conditions and one line of consequence.

The conditions: the move was not a no-effect; the move is not Struggle; the move's power field is
non-zero; `TARGET_TURN_DAMAGED` is true, which is a macro testing whether the target's physical or
special damage this turn was non-zero; the target is **not already** of the move's type; and the
target is still standing. If all six hold, `SET_BATTLER_TYPE` writes the move's type into **both**
of the target's type slots and the old identity is gone.

Read the fourth condition again, because it is the whole answer. The type change happens **only
when the hit landed and did damage**. A miss changes nothing. A resisted-to-zero hit changes
nothing. A status move changes nothing. The only hit that produces the new type is the hit that
worked — and once it has, the move that worked is now the move being resisted.

And the capacity was never created by the attack. **Kecleon**'s ability list in Emerald's species
data is `{ABILITY_COLOR_CHANGE, ABILITY_NONE}`: Color Change is the only ability it can have, and
it was in the table before the battle started.

As elsewhere in this specialty: **the objects of study are abilities, lookup tables, damage
branches and reachability lists.** No Pokémon in this answer stands in for a person with cancer or
for a tumour, and the analogy is dropped entirely at the end, where the subject changes.

Clinical claims carry the same marks as the rigorous half: **mechanism**, **definitional**,
(**consensus**, **country-dependent**).

## The four routes out, drawn as what they are

```
   (i)  THE TARGET CHANGES                 Color Change / Cmd_critcalc

        hit Kecleon with a move that        the alteration is SELECTED BY THE
        DOES DAMAGE  ──►  its types         HIT THAT WORKED, and it is in the
        become that move's type             species table before the battle
                                            ─────────────────────────────────
        and the amplification variant:      a Critical Hit IGNORES the
        the defender banks Defense          defender's Defense stat stages
        Stat Stages  ──────────────────►    above DEFAULT_STAT_STAGE.
                                            Not a bigger hit.  A DIFFERENT
                                            BRANCH of the same function.

   ─────────────────────────────────────────────────────────────────────────

   (ii) THE SIGNAL ARRIVES ANOTHER WAY     Reflect / Light Screen

        CalculateBaseDamage has TWO         Reflect's test lives in the
        branches.  Reflect is tested        PHYSICAL branch.  Light Screen's
        in one.  Light Screen in the        is a separate test in the SPECIAL
        other.  Same shape, same halving,   branch.  Putting up one does
        same doubles exception.             NOTHING AT ALL to the other.
                                            Two screens because two routes.

   ─────────────────────────────────────────────────────────────────────────

   (iii) THE THING STOPS BEING THAT THING  Forecast

        CastformDataTypeChange:             Sun ──► Fire.  Rain ──► Water.
        species == CASTFORM, ability ==     Hail ──► Ice.  Anything else, or
        FORECAST, hp != 0.  Then the        WEATHER_HAS_EFFECT false ──►
        FIELD decides the type.             Normal.  The pressure, not the
                                            attack, rewrote the identity.

   ─────────────────────────────────────────────────────────────────────────

   (iv) THE MOVE NEVER GOT THERE           STATUS3_ON_AIR / UNDERGROUND /
                                           UNDERWATER

        AccuracyCalcHelper tests all        and each test is skipped only if
        three, in that order, and sets      a HITMARKER_IGNORE_* bit is set —
        MOVE_RESULT_MISSED.                 which individual battle scripts
                                            set BY NAME.  A hand-written
                                            list, not a power threshold.
```

## What "targeted" commits you to, and why Flygon is the right picture of it

A targeted agent's effect is **contingent**, and contingent in a strong sense (**mechanism**). Not
"better when the lesion is present" — without the dependency there is no mechanism for it to act
through at all, which is this repository's **Type Effectiveness** zero: Ground into **Flygon** is
nothing, because **Levitate** is Flygon's only ability in Emerald's species data, and no dose,
duration or repetition gets you past a zero. A biomarker-negative population is not a low-response
subgroup.

Two things follow at once. The agent's whole value rests on a test, which is why the test and the
drug are treated as one object — the subject of its own answer in this specialty, where the
species check and the doubling share a line. And anything that removes the dependency removes the
effect **entirely** rather than blunting it, which is why three of the four routes below are not
dose problems.

## Route one: Color Change, and the amplification variant

So the first route out is a change **in the target itself**: a second alteration that keeps the
target working while stopping the drug binding it (**consensus**). Color Change is that, exactly,
including the part people get wrong — the alteration is **selected** rather than created, and the
hit that selected it is the hit that worked.

The answer to this route is chemical. A molecule that binds the altered target, or binds a
different site on it, restores the block, which is why one target accumulates successive
generations of inhibitor (**consensus**). It is also the route most often visible to sequencing
rather than to a microscope, so a plasma assay can usually find it. And it has a sequel: a drug
built against the second alteration selects for a third, narrowing the escape space rather than
closing it (**mechanism**).

The **amplification** variant — more of the target rather than an altered one — has its own exact
counterpart. In `CalculateBaseDamage`, when `gCritMultiplier == 2`, the physical branch checks
whether the defender's Defense stat stage is **below** `DEFAULT_STAT_STAGE`; if it is not, the
boost is simply skipped and the raw stat is used. The special branch does the same thing with
Special Defence. A **Critical Hit** does not out-muscle banked stat stages. It takes a different
path through the function and declines to read them.

The crit itself is instructive about how such a path is bought. `Cmd_critcalc` sums a ladder —
Focus Energy two, a high-critical move one, a **Scope Lens** one, a **Lucky Punch** two *only if
the holder is* **Chansey**, a Stick two *only if the holder is* **Farfetch'd** — and indexes
`sCriticalHitChance`, which is `{16, 8, 4, 3, 2}`, with the roll `!(Random() % chance)`. You can
move along the ladder and you cannot leave it. And two abilities, Battle Armor and Shell Armor,
refuse the whole thing before the roll. A route around a block is still a route with its own
gates.

## Route two: Reflect and Light Screen are two moves because there are two branches

`CalculateBaseDamage` is one function with two large arms. **Reflect** is tested inside the
physical arm. **Light Screen** is tested inside the special arm. The two tests are
character-for-character the same shape — halve the damage, or take two-thirds of it in a double
battle with two defenders still standing, and in both cases **only when `gCritMultiplier == 1`**.
Neither test is reachable from the other arm. Putting up Reflect does not reduce special damage by
a point, and no amount of Reflect ever will.

That is bypass activation (**consensus**). The pathway the drug blocks is rarely the only route to
the same output; escape is the switching-on of a parallel input, leaving the target inhibited and
irrelevant. The counter is to block both nodes.

And which arm a move goes down, in the third generation, is decided by its **type** —
`IS_TYPE_PHYSICAL` is literally `moveType < TYPE_MYSTERY` and `IS_TYPE_SPECIAL` is
`moveType > TYPE_MYSTERY`, with `TYPE_MYSTERY` sitting at nine as the divider. This specialty's
first answer is about a classification computed from a proxy, and this is that proxy doing useful
work for once: because the route is predictable from a field you can read, you know in advance
which screen you still need.

The practical limit on blocking both is not logic, it is tolerance. Two agents acting on pathways
normal tissue also needs produce overlapping toxicity at the dose each one requires, and the
combination is capped by whichever organ both of them burden (**mechanism**). That is why
combination development is slow where the biology is obvious, and why the useful question about a
combination is which toxicities it stacks rather than which pathways it covers. It is also the
argument for giving a combination **together rather than in sequence** where the evidence supports
it: a sequence leaves the resistant subpopulation a single step to take between treatments, and
simultaneous blockade denies it that step (**mechanism**; the actual choice is disease-specific
and **consensus**).

## Route three: Forecast, and what Air Lock tells you about reversibility

`CastformDataTypeChange` begins with three identity checks — the species must be **Castform**, the
ability must be **Forecast**, and the battler's HP must be non-zero — and then hands the decision
to the field. Harsh sunlight makes it Fire. Rain makes it Water. Hail makes it Ice. Any other
weather, or no weather, makes it Normal, and Castform's species entry has Normal in both type
slots as its resting state.

Nothing attacked it. **The pressure rewrote the identity**, and this specialty already puts
systemic therapy in the weather.

That is lineage and phenotype change (**consensus**): the tumour's histology or state shifts, and
the dependency the drug exploited goes with it. Two things follow and both are practical. The
diagnosis is **morphological**, so a plasma assay can miss it completely and tissue is what
establishes it. And the answer is not another inhibitor of anything — it is a different class of
treatment, chosen for the new histology rather than for the original target (**consensus**).

The game also marks the distinction that matters most here. **Air Lock** and **Cloud Nine** do not
change Castform's type; they make `WEATHER_HAS_EFFECT` false, and the same routine then returns
Castform to Normal. Remove the pressure and the form reverts. **That is the reversible tolerant
state and not the completed transformation** — a non-genetic, reversible drug-tolerant state is
expected to reverse when the pressure is removed, and a completed histological change is not
(**mechanism**). Conflating the two is the commonest error in this territory, and Castform models
only the first of them. Said plainly, because this is where the analogy would mislead: no mechanic
in the game models an irreversible lineage change, and none is claimed to.

## Route four: the reachability list, which is a list

A target using **Fly**, **Dig** or **Dive** carries `STATUS3_ON_AIR`, `STATUS3_UNDERGROUND` or
`STATUS3_UNDERWATER`. `AccuracyCalcHelper` tests all three in that fixed order, and each test is
skipped only if the matching `HITMARKER_IGNORE_*` bit is already set. Otherwise it sets
`MOVE_RESULT_MISSED` and the move is over before accuracy is consulted at all.

Which moves set those bits is not a power threshold or a type rule. It is a **hand-written list**,
one script at a time:

* **ON_AIR** — Gust and Twister set it conditionally and also set the damage doubling; Thunder and
  Sky Uppercut set it unconditionally with no doubling at all.
* **UNDERGROUND** — **Earthquake**'s hit-everything loop sets it, and Magnitude reaches the same
  loop by a `goto`, which is why the two behave identically here.
* **UNDERWATER** — the generic hit script sets it only after `jumpifnotmove MOVE_SURF`, and the
  trapping script only after `jumpifnotmove MOVE_WHIRLPOOL`. **Surf** and **Whirlpool** are the
  list, and it is two moves long.

Clinically this is not resistance at all, and the distinction matters (**mechanism**). Viable
disease in a compartment the agent penetrates poorly progresses while everything else stays
controlled. The clue is the **pattern** rather than the fact of progression — one site or one
compartment advancing while the rest does not — and the answer is a different instrument: local
treatment to that site, or an agent whose penetration is a property of the molecule rather than
something a larger dose achieves (**consensus**, (**country-dependent**) in availability).

Which is also why **progression is not one event**. Progression confined to one or a few sites
with everything else controlled is handled differently from widespread progression in several
diseases: continuing the systemic agent and treating the progressing site locally is an
established option, and continuing an agent past radiological progression rests on
disease-specific evidence rather than on a general rule (**consensus**, strongly
**country-dependent**). The emergency answer on mechanism of injury takes the same
semi-invulnerable states apart for the doubling; this answer wants the reachability list instead.

## What the classification is for

Progression is an instruction to find out which of the four this is, because three of them cannot
be reached by changing the dose. That is the case for repeat tissue sampling at progression
**where the result would change management**, and for plasma circulating tumour DNA as a
complementary route with a different blind spot — it samples shed material from many places at
once and cannot see a change of histology, so a negative plasma result at progression is a reason
to consider tissue rather than a reason to stop asking (**consensus**). Why one biopsy is a sample
of a population under selection is the next answer in this specialty.

## Where the metaphor stops

Everything above is abilities, damage branches and a reachability list, and code is a good place
to see them because the conditions are written down. What follows is about people, so it is said
plainly and without the analogy.

A deep response to a targeted agent often restores ordinary life quickly and completely enough
that the disease moves out of the foreground. Being told that the scan has changed is therefore
not a gradual disappointment; it is an interruption of something that had begun to feel settled,
and it frequently arrives at a routine appointment with nothing new to have noticed. The account
above — that the population changed, that this was expected, that there is a next class of answer
— is useful to a clinician and is not comfort.

Repeat biopsy deserves naming too. It is another procedure, with its own risk and its own wait,
offered to someone who has just had bad news, and it is justified by whether the result would
change what is done rather than by completeness. Whether it is right for a particular person is a
conversation, not a protocol, and nothing here settles it.

## What a Gym Leader is listening for

* Color Change fires only when `TARGET_TURN_DAMAGED` is true. What is that condition an analogy
  for, and why is it the most important line in the routine?
* Kecleon's ability list has Color Change in it before the battle starts. Which argument does that
  settle?
* Reflect and Light Screen are tested in different branches of one function. Name the clinical
  claim, and then name what actually limits the answer to it.
* A Critical Hit ignores banked Defense stat stages rather than overwhelming them. Which escape
  mechanism is that the counter to?
* Air Lock returns Castform to Normal. Which distinction does that draw, and which half of it does
  Castform not model?
* Surf and Whirlpool are the entire underwater list. What does the shortness of that list say
  about how a sanctuary site is answered?
* Which of the four routes is a plasma assay least able to detect, and why?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific
to this answer:

* The summary of product characteristics or equivalent label for the agent in question, published
  by the licensing authority in your country — for what it is licensed against, which test defines
  that population, and what is said about continuing it after progression.
* Your national or regional disease-specific guidance, for whether repeat tissue sampling at
  progression is recommended in that disease and whether a plasma assay is accepted where tissue
  cannot be obtained. These differ between countries.
* Your own institution's molecular tumour board or equivalent pathway, which governs what is
  tested at progression and who decides.
* A current standard textbook of the specialty, for the escape-mechanism classification and for
  the pharmacology of compartment penetration.
* The primary literature, for any particular drug–resistance pairing and for the trials behind
  simultaneous rather than sequential combination.

The Pokémon side is in the opposite position and is sourced file by file in the closing note.

## Scope and safety

This is revision material about why targeted agents fail, dressed in a game so that the difference
between an altered target and an unused route stays concrete. It has had no clinical review. **No
drug, gene, disease, dose, response rate or interval appears here, and none should be inferred** —
licensed indications, the tests that define them and the options at progression differ between
countries and institutions and are revised frequently; the label and the local pathway in force
where you work are the authority, and this is not. It is not a prescribing guide and not a
decision aid, and it describes no individual's situation. Anyone affected by cancer — their own
diagnosis or someone else's — should be talking to the clinical team looking after that person,
who have the imaging, the molecular results and the history, none of which are here. The analogy
carries contingency, selection and routing only: no part of it stands in for a person or for a
tumour, and none of it says anything about what happens to anybody.

## Where this stands, October 2026

The Pokémon facts are read from the projects' own source, all of it Emerald. Kecleon's species
entry gives types Normal and Normal, an ability list of `{ABILITY_COLOR_CHANGE, ABILITY_NONE}`,
and base Special Defence of one hundred and twenty against base Speed of forty. Color Change sits
in `AbilityBattleEffects` under `ABILITYEFFECT_ON_DAMAGE` and requires, in order: no
`MOVE_RESULT_NO_EFFECT`, the move not being Struggle, a non-zero `power` field,
`TARGET_TURN_DAMAGED` — itself a macro testing `gSpecialStatuses[target].physicalDmg != 0 ||
specialDmg != 0` — the target not already being of the move's type, and non-zero HP;
`SET_BATTLER_TYPE` then assigns the move's type to `types[0]` and `types[1]` both.
`CalculateBaseDamage` lives in `src/pokemon.c` and tests `SIDE_STATUS_REFLECT` in its physical
branch and `SIDE_STATUS_LIGHTSCREEN` in its special branch, each gated on `gCritMultiplier == 1`,
each halving damage or taking two-thirds of it when the battle is double and two defenders are
alive. The same function, on a critical hit, uses the raw Defence when the defender's stat stage
is not below `DEFAULT_STAT_STAGE`, and the raw Attack when the attacker's is not above it.
`IS_TYPE_PHYSICAL` and `IS_TYPE_SPECIAL` in `include/battle.h` are comparisons against
`TYPE_MYSTERY`, which `include/constants/pokemon.h` gives as nine. `Cmd_critcalc` builds its index
from Focus Energy, the high-critical move effects, Scope Lens, and Lucky Punch and Stick with
explicit species comparisons against Chansey and Farfetch'd, indexes `sCriticalHitChance` = `{16,
8, 4, 3, 2}` with `!(Random() % chance)`, and is refused outright by Battle Armor, by Shell Armor,
by `STATUS3_CANT_SCORE_A_CRIT` and in the Wally tutorial and first battle. Flygon's species entry
is Ground and Dragon with `{ABILITY_LEVITATE, ABILITY_LEVITATE}`. `CastformDataTypeChange` in
`src/battle_util.c` checks species, Forecast and non-zero HP, then maps `B_WEATHER_SUN` to Fire,
`B_WEATHER_RAIN` to Water, `B_WEATHER_HAIL` to Ice and everything else — including a false
`WEATHER_HAS_EFFECT` — to Normal; Castform's species entry is Normal and Normal with
`{ABILITY_FORECAST, ABILITY_NONE}`, and the Air Lock and Cloud Nine cases call that same routine
for every battler. `AccuracyCalcHelper` in `src/battle_script_commands.c` tests `STATUS3_ON_AIR`,
then `STATUS3_UNDERGROUND`, then `STATUS3_UNDERWATER`, each skipped only when the matching
`HITMARKER_IGNORE_*` bit is set; in `data/battle_scripts_1.s`, Gust and Twister set the on-air bit
after a `jumpifnostatus3` and add `setbyte sDMG_MULTIPLIER, 2`, Thunder and Sky Uppercut set it
with no multiplier, Earthquake's `BattleScript_HitsAllWithUndergroundBonusLoop` sets the
underground bit and Magnitude reaches that same label by `goto`, and the underwater bit is set
only behind `jumpifnotmove MOVE_SURF` in the generic hit script and `jumpifnotmove MOVE_WHIRLPOOL`
in the trapping script. Gust and Twister are base power forty, Thunder one hundred and twenty at
accuracy seventy, Earthquake one hundred, Sky Uppercut eighty-five at accuracy ninety. Behaviour
in later generations differs in several of these places and none of it is claimed here.

The clinical reasoning is structural and should age well: a contingent drug, a population under
selection, and four ways for the contingency to fail are not facts about any particular era's
drugs. Everything attached to it moves — which escape mechanisms are known in which disease, which
have a drug built against them, whether a combination is given up front, whether plasma sequencing
substitutes for tissue, and whether an agent is continued past progression are all
disease-specific, revised on a short cycle, and unevenly adopted between countries. No agent,
target or clinical figure is quoted here for that reason.
