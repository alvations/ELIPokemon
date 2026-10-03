---
id: "m080"
slug: placebo-and-nocebo-as-real-effects
style: pokemon
category: pharmacology
difficulty: intermediate
question: "In what sense are placebo and nocebo effects real and measurable, and why does the placebo arm of a trial not actually measure the placebo effect?"
tags: [placebo, nocebo, trial-design, regression-to-the-mean, attribution]
---

# A Scope Lens moves the rate from one in sixteen to one in eight, and one battle cannot see it.

The Game Boy Advance battle engine is the cleanest teaching instrument for this topic that exists,
for one reason: **every term is separately readable in the source, and the observable is their
sum.** You see a number. The number came from a product of real effects and at least one draw, and
nothing on the screen decomposes it for you.

## What is actually inside one observation

```
   term                     the mechanic, exactly                          what it is
   ────────────────────────────────────────────────────────────────────────────────────────
   it got better anyway     Leftovers restores maxHP / 16 at the end of    natural history
                            every turn, whatever you did that turn
                            (m002, m005)

   selection on a noisy     ApplyRandomDmgMultiplier:                      regression to
   measurement                  randPercent = 100 - (Random() % 16)         the mean
                            A Damage Roll: sixteen equally likely values, 85 to 100,
                            mean 92.5. Pick out the turns where it came
                            up 85 and the NEXT draw averages 92.5. The
                            improvement is in the SELECTION, not in you.

   the readout is coarse    the health bar is 48 pixels and never renders  measurement
                            empty while any HP remains (m029, m064)         artefact

   the ritual               Splash: 40 PP, an animation, an entry in       the context of
                            GAME_STAT_USED_SPLASH, and the message          being treated
                            "But nothing happened!"

   the real effect          sCriticalHitChance[] = { 16, 8, 4, 3, 2 }      the thing the
                            and the items and moves that index into it      word names
   ────────────────────────────────────────────────────────────────────────────────────────
```

Read the second row twice, because it is the row everyone skips. **Nothing improved.** The
distribution did not change, the roll is still uniform over sixteen values, and the group you
picked out regressed because you picked it out on the draw. That is arithmetic and it would happen
in a spreadsheet with no Pokémon in it.

And the first row deserves its own sentence, because it is the term that most often gets credited
to the treatment. **Leftovers** restores `maxHP / 16`, floored to 1, every end of turn, with no
condition except that the holder is not already full. On a **Blissey**, with 255 base HP, that is
a large absolute amount every turn. On a **Shuckle**, with 20, it is a trickle. Same fraction,
nothing like the same quantity — `m006`'s **Super Fang** point, applied to the thing that would
have happened anyway. If you want to attribute an improvement to what you did, you first have to
know how much of it was the **Leftovers**.

## Real effects, correctly sized, and invisible in a single trial

```
   Cmd_critcalc

     critChance = 2 × (status2 & STATUS2_FOCUS_ENERGY)
                + (effect == EFFECT_HIGH_CRITICAL)
                + (effect == EFFECT_SKY_ATTACK) + (effect == EFFECT_BLAZE_KICK)
                + (effect == EFFECT_POISON_TAIL)
                + (holdEffect == HOLD_EFFECT_SCOPE_LENS)
                + 2 × (HOLD_EFFECT_LUCKY_PUNCH && species == SPECIES_CHANSEY)
                + 2 × (HOLD_EFFECT_STICK      && species == SPECIES_FARFETCHD)
     if (critChance >= 5) critChance = 4;
     ... && !(Random() % sCriticalHitChance[critChance])   ──►  gCritMultiplier = 2

   stage   0      1      2      3      4
   rate   1/16   1/8    1/4    1/3    1/2

   SO:  nothing          1 in 16
        Scope Lens       1 in 8      a real doubling of the rate
        Focus Energy     1 in 4      a real quadrupling
        both             1 in 3

   And the evasion items, from the accuracy routine: calc = calc × (100 - param) / 100
        Bright Powder    param 10    every incoming accuracy × 0.90
        Lax Incense      param  5    every incoming accuracy × 0.95
```

Every one of those is a genuine, deterministic change to a probability, and **not one of them is
detectable in a single battle.** Hold a **Bright Powder**, lose to a 100-accuracy move, and you
have learned nothing: a one-in-ten shift cannot be read off one attempt. Hold a **Scope Lens**,
land a critical hit on the first turn, and you have learned nothing either, because one in sixteen
also happens.

The same routine also names a subpopulation in whom the whole table is simply skipped:

```
   if (target->ability != ABILITY_BATTLE_ARMOR && target->ability != ABILITY_SHELL_ARMOR
       && !(gStatuses3[attacker] & STATUS3_CANT_SCORE_A_CRIT)
       && !(gBattleTypeFlags & (BATTLE_TYPE_WALLY_TUTORIAL | BATTLE_TYPE_FIRST_BATTLE))
       && !(Random() % sCriticalHitChance[critChance]))
           gCritMultiplier = 2;

   Shell Armor:   Shellder, Cloyster       { Shell Armor }
   Battle Armor:  Armaldo                  { Battle Armor }
                  Kabutops                 { Swift Swim, Battle Armor }   ◄── one bit
```

Against a **Cloyster** the **Scope Lens**, the **Focus Energy** and the **Lucky Punch** all index
into a table that is never consulted, and the effect of every one of them is exactly zero. And
**Kabutops** carries `{Swift Swim, Battle Armor}`, so whether the table applies to it at all comes
down to `personality & 1` — `m077`'s locus, deciding here whether an intervention has any
mechanism against this individual. A real effect, correctly sized, and null in a subgroup you
cannot identify by looking.

This is the whole epistemic position of a placebo arm. The effect is real, the effect size is
modest, and the observation available to you is one draw.

## An item that does exactly nothing unless you are Chansey

Look again at those two `2 ×` lines. **Lucky Punch** adds two stages **if and only if** the holder
is a **Chansey**. The **Stick** adds two **if and only if** the holder is a **Farfetch'd**. On
anything else, both are a held item with a route, a name, a sprite, a shop price and an effect of
identically zero.

```
   Lucky Punch on Chansey      critChance += 2   ──►  1 in 4
   Lucky Punch on Blissey      critChance += 0   ──►  1 in 16     and Blissey is
                                                                  Chansey's own
                                                                  evolution
   Lucky Punch on Snorlax      critChance += 0   ──►  1 in 16
```

Hand it to a **Blissey** and the species check fails, even though it is the same line's own
evolution. The item is unchanged, the ritual is unchanged, the expectation is entirely reasonable
— and the mechanism is not there. `m007`'s zero one more time, and the honest shape of an inert
intervention: it is not a weak intervention, and it is not a fake one. It is an intervention whose
precondition does not hold.

## Splash: a route, a cost, a record, and no mechanism

```
   BattleScript_EffectSplash::
       attackcanceler
       attackstring
       ppreduce                                     ◄── it COSTS something
       attackanimation
       waitanimation                                ◄── it LOOKS like something
       incrementgamestat GAME_STAT_USED_SPLASH       ◄── it is COUNTED
       printstring STRINGID_BUTNOTHINGHAPPENED
       waitmessage B_WAIT_TIME_LONG
       goto BattleScript_MoveEnd

   MOVE_SPLASH: power 0, accuracy 0, 40 PP, MOVE_TARGET_USER
```

That is as complete an inert intervention as any code has ever contained. It has a route, it
consumes a finite supply, it has an animation, the game keeps a **running total of how many times
you have done it**, and the engine itself prints that nothing happened.

The counted statistic is the detail worth keeping. A system that records the administration of a
thing with no mechanism will accumulate a large and perfectly accurate dataset about it, and
nothing in that dataset is evidence of an effect. That is every uncontrolled before-and-after
series ever published.

## The printed description and the implementation disagreed, and the description won

`m035` is where this device belongs and it is worth restating here, because it is the cleanest
case of expectation surviving contact with the facts.

In Red and Blue, **Focus Energy** was described as raising the critical-hit rate.
`CriticalHitTest` in the first-generation disassembly carries the comment at exactly that branch:
using Focus Energy **shifts the wrong way**, so instead of improving the rate it produces a
quarter of the usual one. Players read the description, used the move, won some battles, lost some
battles, and attributed the wins to the move — for years, with the opposite effect running
underneath.

Nothing about that requires anyone to have been careless. The printed claim was plausible, the
outcome was noisy, and the number of trials any one player ran was far too small. By the third
generation the branch is corrected and `critChance` gets its `2 ×`, which is the table above.

## The control arm is in the same source file

```
   Cmd_damagecalc  (what actually happens)        AI_CalcDmg  (what the engine EXPECTS)
   ───────────────────────────────────────        ──────────────────────────────────────
   CalculateBaseDamage(...)                       CalculateBaseDamage(...)
   × gCritMultiplier × dmgMultiplier              × gCritMultiplier × dmgMultiplier
   charged-up and Helping Hand adjustments        charged-up and Helping Hand adjustments
   ... then, via adjustnormaldamage:              ... and that is ALL.
       ApplyRandomDmgMultiplier()                 NO random multiplier is applied.
```

Two routines, the same inputs, one difference: the realised value has the draw in it and the
expected value does not. That is a control arm, sitting in the same file, written for the
opponent's benefit rather than yours. The comparison between them is the only way to say what the
draw did, and it is exactly the comparison a trial without a comparator cannot make.

## And two battles where the designers deleted the variance

```
   ... && !(gBattleTypeFlags & (BATTLE_TYPE_WALLY_TUTORIAL | BATTLE_TYPE_FIRST_BATTLE))
```

`Cmd_critcalc` will not roll a critical hit at all in those two. The tutorial and the player's
first battle were made deterministic on purpose, so that the demonstration would demonstrate.

Which is the correct note to end the mechanism on. An outcome observed under conditions where the
variance has been engineered out is a **demonstration**, not a sample. It tells you what the
designers wanted you to see. A single impressive response to a treatment is in the same category
until something else establishes otherwise.

## Quick Claw, and why one turn settles nothing

```
   if (holdEffect == HOLD_EFFECT_QUICK_CLAW
       && gRandomTurnNumber < (0xFFFF * holdEffectParam) / 100)
       speedBattler = UINT_MAX;

   Quick Claw: holdEffectParam = 20     ──►  about one turn in five
   and gRandomTurnNumber is ONE draw for the turn, read by both sides.
```

When it fires it is absolute — the Speed figure becomes the maximum there is, so the whole
seven-factor pipeline `m066` works through is bypassed. When it does not fire it is nothing. Four
turns in five, a **Quick Claw** holder is indistinguishable from a **Quick Claw** holder that was
never given one, and the fifth turn is indistinguishable from being faster.

That is the attribution problem for an individual, and the game offers no way to solve it from
inside one battle. The technical twin describes the design that does solve it for a person: the
same intervention and an identical inert one, blinded, alternated, several times, with the outcome
recorded in each period.

## Where the metaphor stops

Everything above is mechanism. One thing in this topic is not, and it is the thing the word
"nocebo" is most often used to do damage with.

**A symptom produced by expectation is a real symptom.** The person is not lying, is not imagining
it, and has not failed a test of character. The physiology of a nocebo symptom is the physiology
of that symptom. So "it is probably nocebo" is never a reason to take a report less seriously, and
using the word to end a conversation is a misuse of it. The correct order is the reverse: take the
symptom at face value, and then test the attribution if the attribution matters.

The cost of getting that wrong runs in both directions. Someone whose reported symptoms are put
down to expectation and dismissed may stop reporting anything at all, which destroys the only
signal there was. Someone whose symptoms are attributed to a medicine without the attribution ever
being tested may lose a medicine that was helping and gain a lasting belief that they cannot
tolerate its whole class. Both are common, and both are avoided by the same move: believe the
symptom, interrogate the cause.

There is a second point, about information rather than about any one person. Honest public
information about medicines sometimes increases symptom reporting — that is a measured effect, and
it sits in real tension with the duty to tell people what a medicine may do. The answer is not to
withhold anything. It is to present risk in a form people can use: absolute numbers rather than
relative ones, what proportion do well alongside what proportion do not, the detail offered rather
than recited. Deciding not to tell someone something because they might then feel it is not an
available option.

And the ethical line, plainly: giving someone an inert preparation while implying it is active is
deception, and the mainstream professional position is that it is not acceptable. What is
acceptable, and is what good practice already consists of, is using the non-specific ingredients
**honestly** — explaining what is happening and why, saying what to expect and when, being the
same person next time, making a clear plan. Those are the real components of the effect and none
of them needs a tablet.

Nothing in this pair indicates whether any symptom anyone has is or is not caused by their
medicine, and nothing in it is a reason to continue or stop anything. That is a question for the
person's own prescriber or pharmacist, who can look at the timing, the drug and the alternatives,
and arrange a proper blinded re-challenge if one is warranted.

## What a Gym Leader is listening for

* Sixteen values, 85 to 100. Select the turns that rolled 85 and say what the next draw averages,
  and what that proves about the selection.
* **Scope Lens** against **Focus Energy** against both. Give the three rates from the table.
* Why does a single battle with a **Bright Powder** tell you nothing about whether it works?
* **Lucky Punch** on **Chansey** and **Lucky Punch** on **Blissey**. Same item, same line, two
  answers. Which is it, and why is the second one not "a weak effect"?
* Name the four things **Splash** does before printing that nothing happened, and say which of
  them a register would record.
* Where in the Emerald source is the control arm, and what single line is the difference?
* Why were critical hits switched off for the first battle and the tutorial, and what does that
  make an outcome observed there?
* **Quick Claw** fired. What can you conclude from that turn? (Nothing.)
* **Scope Lens** against a **Cloyster**. What is the effect, and what is the clinical word for an
  intervention in that position?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer, and to its technical twin:

* **A current clinical trials methodology textbook**, for the decomposition above, for regression
  to the mean, and for why control arms and blinding are constructed as they are. This is
  definitional material and a textbook is the right source for it.
* **The Cochrane Library's systematic reviews of placebo interventions**, which are
  the standard reference for what placebo arms do and do not show across conditions, and for the
  subjective-against-objective distinction. They are updated and their conclusions have been
  debated.
* **The primary literature**, for every quantitative claim in this topic without exception: the
  size of placebo responses by condition, the open-label placebo trials, adverse-event reporting
  in placebo arms, and the within-person re-challenge studies. Neither half of this pair states
  such a figure.
* **Your national professional regulator's and medical association's guidance on prescribing
  placebos and on honesty with patients**, for the ethical position where you practise. The
  position is broadly consistent between countries; the detail is not.
* **Your national body's guidance on communicating risk and benefit**, for absolute against
  relative presentation and for what is recommended about describing adverse effects.

The Pokémon figures are a different matter and were read directly from the public decompilations
rather than recalled. From the Game Boy Advance games: `ApplyRandomDmgMultiplier` as `100 -
(Random() % 16)`; `sCriticalHitChance[]` holding `16, 8, 4, 3, 2`, the clamp to index 4, and
`Cmd_critcalc`'s full list of contributing terms including the `2 ×` for Focus Energy, the `+1`
for a Scope Lens hold effect, and the `2 ×` conditioned on `SPECIES_CHANSEY` for a Lucky Punch and
on `SPECIES_FARFETCHD` for a Stick; the guard excluding `BATTLE_TYPE_WALLY_TUTORIAL` and
`BATTLE_TYPE_FIRST_BATTLE`, and the exemption for Battle Armor and Shell Armor holders; Shellder's
and Cloyster's `{Shell Armor}`, Armaldo's `{Battle Armor}` and Kabutops's `{Swift Swim, Battle
Armor}`; `HOLD_EFFECT_LEFTOVERS` restoring `maxHP / 16` floored to 1, only when the holder is
below full; Blissey's base HP of 255 and Shuckle's of 20; `gCritMultiplier` of 2; the accuracy
routine's `calc = calc × (100 - param) / 100` for `HOLD_EFFECT_EVASION_UP`, with Bright Powder's
`holdEffectParam` of 10 and Lax Incense's of 5; `Cmd_damagecalc` against `AI_CalcDmg`, the latter
omitting the random multiplier; `BattleScript_EffectSplash`'s `ppreduce`, `attackanimation`,
`incrementgamestat GAME_STAT_USED_SPLASH` and `printstring STRINGID_BUTNOTHINGHAPPENED`, and
Splash's data of power 0, accuracy 0, 40 PP and `MOVE_TARGET_USER`; Quick Claw's `holdEffectParam`
of 20 and the `gRandomTurnNumber < (0xFFFF * param) / 100` test setting the Speed figure to
`UINT_MAX`; and `Cmd_psywavedamageeffect`'s eleven multipliers. From the first-generation
disassembly: `CriticalHitTest` carrying, at the Focus Energy branch, the comment that using the
move shifts the wrong way and yields a quarter of the usual chance. The arithmetic in the blocks
above is recomputed from those figures.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in this pair are the Pokémon ones.** Neither half
states a figure for any placebo or nocebo response, deliberately: those are condition-specific and
contested, and a number of that kind lifted from a revision answer would be actively misleading.
**Nothing here indicates whether any symptom is or is not caused by a medicine, and nothing here
is a reason to start, continue or stop anything.** A symptom produced by expectation is a real
symptom, and "it might be nocebo" is not a conclusion anyone should draw about themselves or
anyone else from this page. Anyone who thinks a medicine may be causing them a problem should
raise it with their prescriber or pharmacist, who can assess the timing and the alternatives
properly.

## Where this stands, October 2026

The decomposition, regression to the mean and the logic of blinding are definitional and do not
date, and the game mechanics quoted are fixed in released software — pinned above to the Game Boy
Advance games except for the Focus Energy branch, which is explicitly the first-generation one and
is corrected by the third. Three clinical areas are moving. **Open-label placebo** is an active
research field and the size, durability and generalisability of the effect are unsettled, so any
statement stronger than "demonstrated in some symptom-defined conditions" runs ahead of the
evidence. **Nocebo and risk communication** is the subject of current guidance work in several
countries, prompted partly by disputed drug-intolerance syndromes, and the recommendations are not
uniform. And the **availability of blinded within-person re-challenge as a clinical service** is
new, uneven and expanding. Check the current reviews and your own professional body's guidance.
