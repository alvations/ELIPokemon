---
id: "m092"
slug: sodium-as-a-statement-about-water
style: pokemon
category: endocrinology
difficulty: advanced
question: "Why is the serum sodium concentration a statement about water rather than about salt?"
tags: [sodium, water, vasopressin, hyponatraemia, osmolality]
---

# Four readouts in this game, one quotient underneath, and everybody watches the wrong half of it

Here is the function the whole answer turns on, copied out of the Generation III source:

```
   u8 GetScaledHPFraction(s16 hp, s16 maxhp, u8 scale)
   {
       u8 result = hp * scale / maxhp;
       if (result == 0 && hp > 0)
           return 1;
       return result;
   }
```

Two arguments. A division. One guard at the bottom that refuses to report zero *(mechanism)*.

Four different things in the game are that quotient wearing different clothes. The health bar is
it at `scale = 48`. The bar's **colour** is it banded, green above half the pixels, yellow above a
fifth, and `HP_BAR_FULL` only on a strict `hp == maxhp`. **Flail**'s base power is it walked
against a six-entry table — thresholds at 1, 4, 9, 16, 32 and 48 giving 200, 150, 100, 80, 40 and
20, so it counts *upward* as the quotient falls, and **Reversal** carries `EFFECT_FLAIL` in the
data, which is to say it is not a similar move but literally the same table. And **Water Spout**
is the same division with the move's own power as the scale — `hp * power / maxHP`, with its own
forced floor of 1, which is why **Eruption** behaves identically *(mechanism)*.

Five readouts. One division. And every battler alive watches the **numerator** move, because
damage, a **Potion**, **Recover**, **Soft-Boiled**, **Leftovers**' sixteenth and **Leech Seed**'s
eighth are the only things that touch it mid-battle — so everybody learns, wrongly, that the
readout is a statement about the numerator.

| In the battle | What it stands for |
| --- | --- |
| `hp`, the numerator | Total exchangeable cation: sodium with potassium |
| `maxHP`, the denominator | Total body water |
| The 48-pixel bar, its colour bands, **Flail**, **Reversal**, **Water Spout** | Five readouts of the one concentration |
| Damage, a **Potion**, **Recover**, **Leftovers**, **Leech Seed**, **Super Fang**'s half | What moves the numerator |
| **HP Up**, a **Pomeg Berry**, a **Rare Candy**, **Effort Values** | What moves the denominator, up and down |
| **Pain Split**, setting both bars to their average | Osmotic equilibration across a membrane |
| **Pain Split** failing outright against a **Substitute** | The uncounted compartment blocks it too |
| `currentHP += newMaxHP - oldMaxHP` | The body's rule for coupling the two |
| Scaling both arguments by one factor | A volume change with no change in concentration |
| **Blissey**'s base 255 HP, **Chansey**'s 250, **Shuckle**'s 20 | Same quotient, nothing like the same amounts |
| **Shedinja**'s denominator of exactly 1 | A quotient with no resolution left in it |
| **Substitute**'s separate `substituteHP` | Something in the sample the method does not count |
| **Endeavor**, which fails unless the target is above you | Urine against plasma: a directional compare |
| **Sticky Hold** against **Knock Off** and **Thief** | Is it holding on, or letting it go |
| **Haze**, which clears every stage and no `substituteHP` | Clearing the readout is not clearing the state |

**This answer defers to two others.** m057 owns the two-setter split and what a missing reserve
costs. m059 owns the pair-reading move that **Endeavor** and **Sticky Hold** are put to here.
Neither is re-derived.

Claims are marked *(mechanism)*, *(definitional)*, *(consensus)* or *(country-dependent)* where it
matters.

## Two inputs, drawn with what each one actually controls

```
                                 hp  ×  scale
   what every readout reads  =  ──────────────
                                    maxHP

   ── THE NUMERATOR ────────────────────┬── THE DENOMINATOR ────────────────────
                                        │
   moved IN BATTLE by                   │   moved by CalculateMonStats only
     damage                      (down) │     HP Up        → HP Effort Values up
     a Potion, Recover, Soft-Boiled (up)│     Pomeg Berry  → HP Effort Values down
     Leftovers, maxHP/16 a turn    (up) │     Rare Candy   → a level
     Leech Seed, maxHP/8 a turn  (down) │     and nothing in Generation III
     Super Fang, half of CURRENT (down) │     touches it mid-battle at all
   what it sets                         │
     how much there IS                  │   what it sets
                                        │     THE READING
   Blissey 255 · Chansey 250 · Shuckle  │   and every readout above reads the
   20: three denominators, one band      │   ratio, never either argument
   ── AND HERE IS THE PART NOBODY WATCHES ─────────────────────────────────────

   Scale BOTH arguments by the same factor and GetScaledHPFraction returns the
   identical number. Blissey's 255 and Shuckle's 20 can sit on the same band.
   So a change in how much there is of everything is INVISIBLE to the bar, to
   its colour, to Flail, to Reversal and to Water Spout alike — which is the
   whole reason the readout is not a statement about amount.

   ── AND THE OVERRIDE THAT BEATS EVERY OTHER INPUT ───────────────────────────

   CalculateMonStats tests  species == SPECIES_SHEDINJA  FIRST and sets
   newMaxHP = 1, and no IV, no EV and no level downstream gets to argue.
   One branch read before the arithmetic. Nothing after it can win.
```

That override is worth sitting with, because the real system has one in the same position. There
are two sensed signals, and when they disagree, the one read first wins and the arithmetic
downstream does not get a vote *(consensus)*. A body in a low-volume state will hold water it does
not osmotically need, every time, and the readout falls. The controller is behaving exactly as
written. The number is still wrong.

And the denominator case is the one the games make vivid. **Shedinja** carries a denominator of
exactly 1, so `GetScaledHPFraction(1, 1, 48)` hands back 48 and there is no second value available
anywhere between. Four readouts, no resolution in any of them *(mechanism)*. A quotient is only as
informative as its denominator permits, and nothing you do to the numerator fixes that.

## Before anything else: is the number a quotient of what you think it is?

Two cases where the reading is low and the state is not, and both are mechanical rather than
clinical.

**There is something in the count that is not what you are counting.** **Substitute** costs
maxHP/4 and stores that amount in `substituteHP`, a separate field the bar never draws — and
**Haze** clears every stat stage on the field and restores not one point of it *(mechanism)*. So
there is a real quantity, sitting in the same battler, that the readout's two arguments do not
include. Read the bar and you have measured something; it is simply not the thing you wanted.

**The floor lies.** `GetScaledHPFraction` returns 1 whenever the true quotient rounds to 0 and
`hp` is above 0, and **Water Spout**'s scaling does the same — two routines in one game refusing
to report a zero *(mechanism)*. A reading sitting on the floor is consistent with an enormous
range of states, and the one thing it definitely is not is a measurement.

Which is why you establish the denominator first. A low band with a denominator you have checked
is a different problem from a low band with a denominator nobody looked at, and they have nothing
in common except the band.

## If it really is low, two readouts answer two separate questions

**Question one: is the denominator being held?** The readout for that is **Endeavor**, and the
reason it works is the failure condition. Its Generation III implementation is three lines:

```
   if (target.hp <= attacker.hp)   → the move FAILS outright
   else                            → damage = target.hp - attacker.hp
```

It is a **directional comparison between two bars**, not a measurement of either *(mechanism)*.
The answer is in which way the inequality runs, and the move tells you by whether it does anything
at all. One bar against another, and the direction is the finding.

**Question two: if it is being held, is there a reason?** The readout is **Sticky Hold**. Try to
take the item — **Knock Off**, or **Thief** — and watch. If the item moves, nothing was holding
it. If **Sticky Hold** fires, the holder is keeping what it has *(mechanism)*. And here is the
part that makes it the right device: the game records an opposing Ability **only when it fires**,
so until you push, the field has no entry for it at all. You learn that something is holding on by
trying to take it away.

The two go together and neither answers the other's question. That is the same pairing move the
calcium answer makes, for the same structural reason.

There is a third move that reads two bars, and it is worth naming because of what stops it. **Pain
Split** sets both battlers' HP to `(attacker.hp + target.hp) / 2` — it does not measure either
bar, it **equilibrates** them, which is what water does across a membrane when the two sides
disagree *(mechanism)*. And its Generation III implementation refuses to run at all if the target
has a **Substitute** up: the first thing `Cmd_painsplitdmgcalc` tests is `STATUS2_SUBSTITUTE`, and
if the flag is set it jumps straight to the failure branch. So the compartment the bar does not
count is also the compartment that blocks equilibration — one hidden quantity, two separate
consequences, and **Haze** will not clear it either.

One caution, and it is mechanical. If the holder has no item, the **Sticky Hold** branch simply
advances and nothing is recorded *(mechanism)*. The push returns a blank, and a blank is not a
negative. Anything already emptying the slot — anything that has made the holder let go for
reasons of its own — destroys the test, and the test does not announce that it has been destroyed.

## The rule can be right while the result is not

Now the coupling, which is the best thing in this answer, because the game's authors had to
legislate it and you can read what they chose. When `maxHP` moves, something has to happen to
`hp`, and `CalculateMonStats` decides:

```
   currentHP += newMaxHP - oldMaxHP;
```

The **absolute gap** is conserved. Not the ratio *(mechanism)*. Which means that moving the
denominator moves the numerator by the same number of points, and the quotient — every one of the
four readouts — lands somewhere new. One line of code, and it is the entire reason the reading can
change without anybody adding or removing a single point of the thing being read.

Nobody made a mistake. The rule is consistent, deliberate and applied the same way every time. It
is simply a rule about the gap, and all four readouts are about the ratio.

## Read the other way: the denominator falling

A **Pomeg Berry** takes HP effort points away, which lowers `maxHP`, which runs the same line in
reverse *(mechanism)*. The band moves the opposite way for the mirror-image reason, and the thing
that would have to be true for it to keep moving is that something is removing the denominator and
nothing is putting it back. Two conditions, not one.

## Why fixing the number by moving the denominator has its own failure mode

The decompilation's own comment, left in by the people who wrote it down:

```
   // BUG: currentHP is unintentionally able to become <= 0 after the
   // instruction below. This causes the pomeg berry glitch.
   currentHP += newMaxHP - oldMaxHP;
```

Drive the denominator down far enough, by the rule the code uses to keep the quotient honest, and
the numerator is carried somewhere that is not a state at all *(mechanism)*. The guard that would
catch it sits behind a `BUGFIX` flag that the shipped cartridge does not set. The failure is not
in the measurement and not in the intention; it is in **the correction**, and it is the correction
that has to be done carefully.

And here the games give me nothing, so I will say so rather than dress something up. Nothing in
Generation III models a battler that has **reorganised itself** around an abnormal field such that
restoring the normal field is itself the injury. That is the actual reason the speed of a
correction matters, it is the single most consequential thing on this topic, and it is in the
plain-prose section below with no analogy on it at all.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

Everything above is a picture of one arithmetic fact: that a concentration is a quotient, that its
two inputs are set by different controllers answering different questions, and that a rule
coupling them can be perfectly consistent and still move the reading. The picture is fair. Nothing
above stands in for a person — the quantities are quantities.

Hyponatraemia is the commonest electrolyte abnormality in hospital practice, and a large share of
the harm attributed to it comes from two directions that pull against each other: leaving a
genuinely symptomatic acute case uncorrected, and correcting a chronic one too fast. Brain cells
defend their volume against a fall in extracellular osmolality by giving away potassium and then
organic osmolytes, over hours to days. A chronically low sodium is therefore accompanied by a
brain that has already adapted to it, and restoring the outside quickly draws water out of cells
that no longer have the osmolytes to hold their own. The resulting injury is demyelinating, it has
a recognisable clinical picture, and it is caused by treatment rather than by disease. It is worth
naming as an iatrogenic injury rather than as an unavoidable complication.

There is a diagnostic trap here with human consequences too. A low sodium is often recorded,
attributed to a medicine or to age, and not worked through — and two of the things it can mean are
cortisol deficiency and an occult malignancy. Neither is common. Both are costly to miss.

And a note about who is reading. Someone reading this may have been told their sodium is low, or
may be on a fluid restriction. If that is you: nothing above is a threshold, a target, a rate or a
plan. What is done about a low sodium is set against its cause and against how long it has been
there in a particular person, and that assessment belongs to the team that ordered the test — not
to an analogy about a division.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md)
for the standing documents of this specialty. Specific to this answer:

* Your national or specialty-society guidance on the investigation and management of
  hyponatraemia, for the diagnostic sequence, the correction limits and the monitoring intervals.
  European and North American documents differ in emphasis and in some figures, so open the one
  that applies where you work.
* **Your own institution's protocol** for severe or symptomatic hyponatraemia and for managing an
  over-rapid correction. It overrides a national document where the two differ.
* **Your laboratory's handbook**, for whether its sodium assay measures a diluted or an undiluted
  sample, and for how it reports measured and calculated osmolality.
* The joint international society statement that renamed central and nephrogenic diabetes
  insipidus as vasopressin deficiency and vasopressin resistance.
* A current textbook of renal physiology, for the relationship between the serum sodium and total
  body exchangeable cation and water, and for the cerebral osmolyte response to chronic
  hypotonicity.

The Pokémon side is different and is sourced properly. `GetScaledHPFraction`'s three lines and its
forced 1, `B_HEALTHBAR_PIXELS` being defined as 48, `GetHPBarLevel`'s bands at 50 and 20 per cent
and its strict `hp == maxhp` test for a full bar, **Flail**'s six-entry threshold table, **Flail**
and **Reversal** sharing one `EFFECT_FLAIL`, **Water Spout**'s `hp * power / maxHP` and its own
forced 1 (shared with **Eruption**), **Pain Split**'s averaging and its `STATUS2_SUBSTITUTE`
failure branch, **Leech Seed**'s eighth, **Chansey**'s base 250, **Endeavor**'s `target.hp <=
attacker.hp` failure branch, **Sticky Hold** blocking **Knock Off** and the fact that an Ability
is recorded only when it fires, **Substitute**'s separate `substituteHP` field, **HP Up** adding
and a **Pomeg Berry** subtracting HP effort points, **Blissey**'s base 255 and **Shuckle**'s base
20, the **Shedinja** branch in `CalculateMonStats`, and the `currentHP += newMaxHP - oldMaxHP`
line together with the comment naming the Pomeg berry glitch were all read from the pokeemerald
and pokeemerald-expansion decompilations rather than from memory. One note on what is **not**
claimed: whether **Sticky Hold** blocks **Trick** in Generation III is not asserted here, because
only the **Knock Off** and **Thief** branches were read.

## Scope and safety

The Pokémon here is doing one job: making it concrete that a concentration is a quotient with two
independently driven inputs, and that the rule coupling them is where the surprises live. It is
not a clinical reference, not a decision aid, and not about any individual's care. **No correction
limits, infusion rates, fluid regimens, thresholds or assay cut-offs appear here on purpose** —
they differ between countries and institutions, they are revised, and the speed at which a sodium
is corrected is one of the places where taking a figure from a revision page would do real harm.
Check your local protocol and the formulary. Nothing here has had clinical review. The metaphor
covers mechanism and stops at outcome: severe symptomatic hyponatraemia and severe hypernatraemia
are emergencies and are not material for a battle analogy. If someone is unwell now, contact local
emergency services.

## What a Gym Leader digs into next

* Why do all five readouts miss a change that scales both arguments at once?
* Why does **Pain Split** fail against a **Substitute**, and why is that the same fact twice?
* Why is a reading sitting on `GetScaledHPFraction`'s forced 1 not a measurement?
* Why does **Endeavor** tell you something by failing?
* Why is a blank from **Sticky Hold** not a negative result?
* Why does `currentHP += newMaxHP - oldMaxHP` move every readout without anything adding or
  removing a point of what is being read?

## Where this stands, October 2026

The arithmetic of the quotient, the two-controller split and the coupling argument are mechanism
and do not date. What dates on the Pokémon side is the constants and the implementation: 48 pixels
is a Generation III figure and the expansion makes it a configurable constant, **Water Spout** and
**Eruption** arrived in Generation III and **Pain Split** in Generation II, **Thief** and **Knock
Off** have had their power and secondary behaviour revised more than once, **Sticky Hold**'s
coverage was widened in later generations, and the `BUGFIX` guard that would close the Pomeg berry
glitch is a decompilation option and not something the cartridge does. Check the current
generation's data. On the clinical side the terminology is moving — the vasopressin deficiency and
resistance names are recent and adoption is uneven — and everything procedural and numeric moves
with it, so check current local guidance, your own institution's protocol and your laboratory's
handbook.
