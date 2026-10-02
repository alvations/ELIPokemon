---
id: "m043"
slug: adherence-and-regimen-design
style: pokemon
category: pharmacology
difficulty: intermediate
question: "What makes a regimen hard to take, why does the timing of a side effect matter more than its severity, and why is calling someone non-compliant a statement about the prescription?"
tags: [adherence, regimen-design, side-effect-timing, deprescribing, measurement-bias]
---

# Snorlax learns Rest at 28 and Snore at 28. The games hand you the cost and the fix together.

**Rest** fills the whole bar and wipes every status condition off it, and the Game Boy Advance
code charges for that in a way worth looking at closely. It refuses outright if HP is already
full. And then it writes the sleep counter to exactly **3** — not a roll, a constant — where every
other way of falling asleep in those games sets `(Random() & 3) + 2`, a roll of two to five turns.

So Rest is the trade every maintenance regimen is: an **immediate, certain, exactly-known** cost
in exchange for a benefit you only collect if you are still standing afterwards. Three turns is
not severe. Three turns is *badly timed*, which is a different thing and the more important one.

And **Snorlax** learns **Rest** at level 28 and **Snore** — 40 base power, usable only while
asleep — at level 28 as well. The same level. The games put the problem and one of its answers in
the same learnset entry, which is as close as a cartridge gets to saying *this is a design
question*.

## The four slots are the whole budget

The **Four-Move Limit** is a hard four. Not a soft four, not four plus an exception: four. So
every slot you spend making a plan survivable is a slot not doing the job the plan was for.

| The slot is spent on | And what it buys | What it costs |
| --- | --- | --- |
| **Rest** | The bar, and every status off it | Three turns asleep, immediately |
| **Snore** | 40 power while asleep, so the turns are not wasted | A whole slot, to patch another slot |
| **Sleep Talk** | A random one of your other moves while asleep | A slot, and no control over which |
| **Swords Dance** | Attack up two stages | A turn before anything happens |
| the fourth | the actual attack | — |

Four slots, and in that column three of them exist to make one of them tolerable. The equivalent
on a prescription is a drug for the side effect of a drug, and the point is not that it is wrong —
sometimes it is exactly right — but that it is a cost being paid in the same currency as the
benefit.

**And the item slot is a second, separate budget**, which is where the cheap fix lives. A **Chesto
Berry** carries `HOLD_EFFECT_CURE_SLP` and a **Lum Berry** carries `HOLD_EFFECT_CURE_STATUS`:
either of them removes Rest's three turns the instant they arrive, without touching the full heal
at all. That is the entire lesson of this answer. The move did not change. The Snorlax did not
change. **The set changed**, and whoever wrote the set is the one who can change it.

## The arithmetic of a plan with steps

The printed accuracies in the Game Boy Advance move data are honest numbers, and multiplying them
is the only honest way to read a plan that needs all of them.

```
   A FOUR-STEP PLAN, each number straight off the move data

   step               move              printed accuracy     running product
   ──────────────────────────────────────────────────────────────────────────
    1   lay the hazard   Spikes          no accuracy check        1.000
    2   burn it          Will-O-Wisp            75                0.750
    3   poison it        Toxic                  85                0.638
    4   drain it         Leech Seed             90                0.574
   ──────────────────────────────────────────────────────────────────────────
    and if the plan also wanted a sleep:
    5   Hypnosis                               60                0.344
   ──────────────────────────────────────────────────────────────────────────

   NOT ONE of those numbers looks bad. Seventy-five, eighty-five, ninety: you would
   accept every one of them on its own without a second thought. The plan that needs
   all four is a coin flip, and the plan that needs five works one time in three.

   ┌──────────────────────────────────────────────────────────────────────────────┐
   │  Nothing in that table is anybody failing at anything. The product of        │
   │  several good numbers is a bad number, and the only lever that moves it is   │
   │  HOW MANY STEPS THERE ARE. That lever is held by whoever wrote the plan.     │
   └──────────────────────────────────────────────────────────────────────────────┘

   And Spikes is the instructive row twice over: it cannot miss, and it also pays
   NOTHING until the opponent switches something in. Up to three layers in these
   games, at maxHP/8, maxHP/6 then maxHP/4 -- so three guaranteed turns spent on a
   benefit that may never be collected at all.
```

## Why the timing beats the size: Curse

**Curse** is the sharpest mechanic in the games for this, because the code splits it down the
middle. The battle script's very first instruction is `jumpiftype2 BS_ATTACKER, TYPE_GHOST` — so
the *same move* does two unrelated things depending on who used it. A non-Ghost gets a stat change
that costs nothing: Attack and Defence up, Speed down. A **Ghost** gets the real one.

```
   GENGAR, which learns Curse at level 16, against ALAKAZAM.
   Level 100, perfect HP stat, the full 252 effort points, from the HP formula:

        Gengar    base HP 60  →  ( 120 + 31 + 63 ) + 110  =  324
        Alakazam  base HP 55  →  ( 110 + 31 + 63 ) + 110  =  314

   THE COST, paid the instant it lands:        maxHP / 2  of the USER   =  162
   THE RETURN, at the end of each turn:        maxHP / 4  of the TARGET =   78

   end of turn        1       2       3       4
   returned so far    78     156     234     312
   still behind?     yes     yes      NO      no
                                      ▲
                      THREE turns before the trade is worth making

   And Alakazam does not have to stay. STATUS2_CURSED lives in volatile status, and
   the switch-in routine zeroes volatile status outright -- so Alakazam walking away
   on turn one ends the curse and Gengar has spent half its bar on nothing.
```

Read that against **Belly Drum** from `m008`. Belly Drum states its gate and **refuses outright**
below it — it will not let you pay unless the payment is survivable. Curse does not refuse. It
takes the 162 and then the return depends on something you do not control.

A move that fails loudly is kinder than one that charges you up front and disappoints quietly. A
player who looks at the bar one turn after Curse and concludes Curse is bad has gathered honest
evidence and drawn the wrong conclusion from it, and the reason is purely that the cost arrived
first.

## Reading whether the plan is being followed

Your own Pokémon shows HP as a number. The opponent's shows a bar and nothing else — `m008`'s
asymmetry — so for one side you have a measurement and for the other an impression, and you cannot
tell a missed **Leftovers** turn from a flat drain by looking. `m041` is the same problem one
level up: a single reading of Speed is consistent with several different Pokémon, and no amount of
staring at it resolves which.

The honest move in both is to name which instrument you are holding before quoting what it said.

## The thing nobody writes on a team sheet

Nobody has ever written *uncooperative Snorlax* in the notes.

The sheet has four moves, an item, an ability, a nature and an effort-point spread, and a trainer
chose every one of them. When a Snorlax keeps falling over to the three turns of **Rest** it was
given, nothing on that sheet is a fact about the Snorlax's character. It is a fact about the four
slots. The **Chesto Berry** costs twenty in a **Poké Mart** and it is sitting right there.

And the other direction matters as much: sometimes the right edit is to take the move **off**. A
plan that needs five things to land, in a format where it will get three turns, is a plan to
abandon rather than a plan to execute harder. `m014` is where deliberately removing something is
treated as the clinical act it is.

## Where the metaphor stops

Everything above is mechanism, and mechanism is what the analogy is for. The language is not a
mechanism, and here the Pokémon framing stops entirely, because this is the one question in the
specialty where the words themselves do the damage.

"Non-compliant" written in a record follows a person. It changes how the next clinician reads
them, it invites less explanation rather than more, and it is applied unevenly — more readily to
people who are poor, who do not share the clinician's first language, who have a mental health
diagnosis, or who have already been labelled difficult once. The clinical consequence runs the
wrong way: someone who expects to be blamed says less, so there is less to work with, so the next
prescription is written on worse information.

There is real risk on the other side too, and it should be said plainly rather than softened.
Stopping some medicines abruptly causes rebound, withdrawal, or loss of control of a condition,
and that is a genuine danger. That makes it *more* important, not less, that a person feels able
to say they have stopped — because a consultation where the honest answer is punished produces a
record that is wrong, and the decisions then rest on a fiction.

A team sheet can be rewritten in a menu. A person is not a set, their reasons are not a design
flaw to be engineered around, and nothing in this answer or its technical twin is advice to anyone
about their own medicines — in particular, nothing here suggests starting, stopping or changing
anything. Anyone finding a medicine hard to take, or who has already stopped one, has a reason
worth hearing, and the person to tell is their own prescriber or pharmacist, who can change the
design.

## What a Gym Leader is listening for

* Why is three turns of **Rest** a timing problem rather than a severity problem?
* Four moves at 100, 75, 85 and 90 accuracy. What is the plan's number, and who can change it?
* Why does **Gengar**'s **Curse** cost half a bar when **Snorlax**'s costs nothing?
* **Alakazam** switches out on turn one. What did the 162 buy? (Nothing.)
* Why is **Belly Drum** refusing outright a kinder design than **Curse** charging you first?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer, and to its technical twin:

* **Your national guideline body's guidance on medicines adherence and on medicines
  optimisation**, for the terminology, the intentional and unintentional distinction, and what is
  expected in a review consultation. Country-dependent and revised on a cycle.
* **Your national formulary's monograph** for any drug whose early adverse effects or titration
  schedule are at issue, and for the modified-release preparations a frequency reduction depends
  on.
* **Your institution's policy on medicines reconciliation at admission and discharge**, which is
  where the largest avoidable losses in this topic happen.
* **The primary literature** for anything quantitative — adherence rates, intervention effect
  sizes, the performance of the measurement methods. The technical twin deliberately states no
  adherence figure, because a number quoted without its method is not informative.

The Pokémon figures are a different matter and were checked against the public decompilation of
the Game Boy Advance games, read directly: Rest restoring the full bar, clearing status, failing
at full HP, and setting the sleep counter to exactly 3, against `(Random() & 3) + 2` for every
other route into sleep; Snorlax learning Rest and Snore at level 28 and Belly Drum at 15; Snore at
40 base power and usable only while asleep; the Chesto Berry's and Lum Berry's hold effects and
the Chesto Berry's price of twenty; the Four-Move Limit; the printed accuracies of Will-O-Wisp at
75, Toxic at 85, Leech Seed at 90, Hypnosis at 60, Sleep Powder at 75, Sing at 55 and Spore at
100; the Spikes battle script containing no accuracy check at all, a maximum of three layers, and
damage of `maxHP / ((5 − layers) × 2)`; the Curse script branching on whether the user is
Ghost-type before anything else, the Ghost branch costing the user half of maximum HP and removing
a quarter of the target's maximum HP at the end of each turn, and the non-Ghost branch being a
stat change instead; Gengar learning Curse at level 16 and Dusclops at 34; volatile status being
zeroed on switch-in; and the base HP of Gengar and Alakazam with the HP formula. Every arithmetic
result in the blocks above is recomputed from those rules rather than recalled.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in this pair are the Pokémon ones.** The
probabilities in the technical twin are illustrative figures chosen to make an exponent legible;
none is an observed adherence rate and none describes any real population. Nothing here is advice
about anyone's own medicines, and nothing in either half suggests starting, stopping or changing
any treatment — stopping some medicines abruptly is itself harmful, and that decision belongs with
a prescriber who has the records. Practice, terminology and the system barriers described differ
by country. Anyone finding a medicine hard to take should raise it with their own prescriber or
pharmacist. A set can be rewritten from a menu. A person cannot, and is not asking to be.

## Where this stands, October 2026

The arithmetic and the harm-before-benefit asymmetry are mechanism and do not date, and the game
mechanics cited are fixed in released software — though the series has changed several of them
between generations, and this answer pins the ones it uses to the Game Boy Advance games. The
terminology does date: "compliance" gave way to "adherence" and in several places to "concordance"
and then to plainer language about what a person decided, and the preferred term differs by
country and by specialty. So does the evidence for specific interventions — reminder systems,
compliance aids, pharmacist-led review, digital adherence monitoring — where the literature has
moved repeatedly and effect sizes have generally come in smaller than early enthusiasm suggested.
Check the current guidance from your own national body.
