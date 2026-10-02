---
id: "m083"
slug: shared-decision-making
style: pokemon
category: general-practice
difficulty: advanced
question: "Why does a preference-sensitive decision have no single right answer, and what does that demand of the consultation?"
tags: [shared-decision-making, preference-sensitive, risk-communication, equipoise, decision-aids]
---

# Fire Blast against Flamethrower is a choice. Earthquake into a Taillow is not one.

Both of those are choices between two moves and they are not the same kind of choice, and the
cartridge is unusually clear about the difference. One of them has an answer printed in the type
chart. The other has two complete, correct, published data sets and no way to rank them without
something the data does not contain.

One thing to fix before the analogy starts, because it is what makes the analogy usable at all:
the decision-maker here is the **Trainer**, and the thing being decided is a *move* or an *item*.
Nothing in this answer puts a Pokémon in the position of the person whose values settle the
question. The weighting the data cannot supply belongs to whoever is holding the controller.

## The case where the chart decides, and offering a choice is offering a false one

**Earthquake** into a **Taillow** is ×0. Not weak, not unlucky — zero, because Taillow is
Normal/Flying and the Ground row of the chart holds 0.0 in the Flying column. No stat stage, no
**Choice Band**, no repetition and no amount of patience gets past a zero, which is the house
device m007 and m031 established and it is doing its ordinary job here. **Flygon** is the same
answer by a different route: Ground/Dragon, and Levitate as its only ability.

That is the shape of a decision where the evidence *has* settled it. There is no exchange rate to
find, because one option does not trade a worse outcome for a better one — it has no mechanism at
all. Laying the two out as equivalent options would not be respect for the Trainer. It would be
handing them a menu with a dead entry on it.

## The case where two correct data sets still do not rank

```
   EVERY NUMBER BELOW IS REAL, READ OUT OF THE EMERALD MOVE TABLE.

     move            power   accuracy   PP    other                power × accuracy
     ─────────────   ─────   ────────   ──    ─────────────────    ────────────────
     Flamethrower       95      100     15    10% burn                  95.0
     Fire Blast        120       85      5    10% burn                 102.0

     Surf               95      100     15    hits both foes            95.0
     Hydro Pump        120       80      5    one target                96.0

   Fire Blast is SEVEN PER CENT better on expected damage and carries a 15% chance
   of doing nothing at all, three times fewer uses, and the same burn chance. Nothing
   in those two rows ranks them. To rank them you need to know:

        how recoverable a miss is          ─ not in the move data
        how long the battle will run       ─ not in the move data
        whether the PP has to last a cave  ─ not in the move data
        how much a bad turn costs you      ─ not in the move data

   ┌──────────────────────────────────────────────────────────────────────────────┐
   │ Those four are held by the Trainer, they differ legitimately between two     │
   │ Trainers holding identical Pokémon, and neither of them is wrong. That is    │
   │ what a preference-sensitive decision is, and no further data closes it.      │
   └──────────────────────────────────────────────────────────────────────────────┘
```

## And the case whose class changes with the weather

**Thunder** and **Thunderbolt** are the pair that makes the classification itself the skill,
because which kind of decision they are depends on the state of the field.

```
   REAL MECHANICS. Thunderbolt: 95 power, 100 accuracy, 15 PP, 10% paralysis.
   Thunder: 120 power, 70 accuracy, 10 PP, 30% paralysis. And then the engine:

     the accuracy helper skips the accuracy check ENTIRELY for Thunder when rain
     is up and the weather has effect;  in harsh sun its accuracy is overwritten
     with 50.

     field        Thunder expected        Thunderbolt expected    which decision
     ──────────   ────────────────────    ────────────────────    ─────────────────
     clear        120 × 0.70 =  84        95 × 1.00 = 95          Thunderbolt wins
                                                                  on damage, Thunder
                                                                  on paralysis → a
                                                                  real trade-off
     Rain Dance   cannot miss  = 120      95 × 1.00 = 95          Thunder dominates
                                                                  → NOT a trade-off
     Sunny Day    120 × 0.50 =  60        95 × 1.00 = 95          Thunderbolt
                                                                  dominates → NOT a
                                                                  trade-off

   Same two moves, same Trainer, three different KINDS of decision. Reading the
   field before offering the choice is the whole of the technique.
```

## One item slot, four real items, and no ranking anywhere in the data

m014 owns the budget argument — four move slots, one held item, and the fourth addition is the one
that loses. This is the other half of that, and it is a different claim: even once the budget is
settled, the *ranking of the candidates* is not in the item data either.

| item | what it actually does, in Generation III | what it is bought with |
| --- | --- | --- |
| **Choice Band** | Attack × 150/100, and the engine stores the first move selected | the other three slots, immediately |
| **Leftovers** | restores maxHP/16 at the end of every turn, minimum 1 | nothing per turn, everything up front |
| **Lum Berry** | cures a status condition, once, and is then gone | the slot, for the rest of the battle |
| **Bright Powder** | an attack aimed at the holder has its accuracy × 90/100 | ten per cent of someone else's reliability |
| **Quick Claw** | 20 times in 100 it sets its holder's Speed to the maximum for that turn, which beats any Speed but no priority bracket | a benefit you cannot schedule |

There is no dominant row. Which one is right depends on what the Trainer is trying to avoid, and
"what you are trying to avoid" is not a property of the Pokémon.

## The information exists, and it is not where the decision is

Here is the part that transfers most directly. In Generation III the type chart is in the
cartridge, complete, exact and consulted on every hit — and nothing in the move menu shows you
any of it. The verdict arrives *after* the move, as a message. The Trainer chooses in front of a
list of four names and finds out what the chart said once it is too late to choose again.

That is the gap a decision aid closes. Not new evidence, not a better chart: the same numbers,
moved to the moment where the choice is actually made, in a form somebody can hold while making
it. **Sweet Scent**'s one turn and 1 PP buys the same thing a step earlier, which is m048's point
about looking before committing rather than after.

## Where the metaphor stops

Two things make this hard in a way no framework fixes, and neither of them belongs inside an
analogy.

The first is that a person can decide well, with good information and sound reasoning, and have it
turn out badly — and the reasoning was still sound. That is what a probability is. A consultation
that implies otherwise, in either direction, leaves somebody feeling at fault for an outcome they
were honestly told was possible.

The second is distributive. Done well, sharing a decision redistributes power. Done badly it
rewards confidence, articulacy, familiarity with the system and willingness to disagree with a
professional — all unequally distributed, none of them clinical. The people who most need a
decision made with them are frequently the least likely to be offered one, and the remedy is
structural rather than attitudinal: the same offer, the same aid, the same check that it was
understood, the same interpreter, every time, rather than according to who looks interested.

And the part usually left out of a teaching account: there are consultations where the honest
answer to being asked what you would do is useful, and asking for it is not a failure of
autonomy. Giving a recommendation, labelled as a recommendation, after the person's own weighting
has been heard, is part of the method and not a lapse from it.

## What a Gym Leader is listening for

Whether the Trainer classifies the choice before discussing it — chart-decided, genuinely traded,
or state-dependent — and says which, out loud. Then the four things the move data does not
contain, from memory. Then the weather case, and what it means that the same two moves change
class. Then the item table, and why there is no best row. Then where the information was at the
moment of the decision rather than afterwards. Then the hard one: what they would do if the
Trainer asked them to just pick, and why that is allowed.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The shared decision making guidance issued by the national body for clinical guidelines in the
  reader's own country, which sets out what is expected of the consultation locally
  (**country-dependent**).
* The consent and capacity law and professional guidance applying in the reader's jurisdiction,
  which is the authority on what information must be given and on how a refusal is handled. This
  differs materially between countries and has shifted in several over the last decade
  (**country-dependent**).
* The published decision aids maintained for the specific decision in question, together with the
  inventory criteria used to appraise them, for whether an aid is fit to use.
* Any systematic review of patient decision aids, for the effects on knowledge, decisional
  conflict and value-choice concordance, and for the weaker and more variable effects on which
  option is chosen.
* The risk-communication literature on framing, denominator neglect and absolute against relative
  presentation, for why format changes decisions.

The Pokémon figures are a separate matter and are not covered by the line above. The Generation
III power, accuracy and PP values for Flamethrower, Fire Blast, Surf, Hydro Pump, Thunder and
Thunderbolt with their secondary-effect chances, Surf's both-opponents target, the accuracy helper
skipping the check for Thunder in rain and the overwrite to 50 in sun, the Ground row of the type
chart holding zero against Flying, Taillow's Normal/Flying typing, Flygon's Ground/Dragon typing
with Levitate as its only ability, Choice Band multiplying Attack by 150/100 and storing the first
move selected, Leftovers restoring maxHP/16 with a floor of 1, the Lum Berry curing one status
once, Bright Powder's hold-effect parameter of 10 applied as a 90/100 multiplier to incoming
accuracy, Quick Claw's parameter of 20 applied as a per-turn roll that sets its holder's Speed to
the unsigned maximum, and Sweet Scent's 20 PP, were all read directly from the
pret and rh-hideout decompilation projects, which this environment can reach.

## Scope and safety

This is revision material about the structure of a consultation, written for someone already
training in or qualified for the field. It is not a clinical reference, not a decision aid, and
nothing here is guidance to any individual about a decision of their own — that belongs with the
clinician who has assessed them, with local guidance, and with the consent law of their
jurisdiction. No condition, treatment, benefit figure or harm figure is named here on purpose:
the arithmetic of a specific decision is local, several of the numbers are contested, and all of
them are revised. The move and item figures above are real and stand in for a mechanism; none of
them is a clinical probability and no clinical figure should be read out of them. If someone is
unwell right now, the relevant action is to contact local urgent care or the local emergency
number, not to read this.

## Where this stands, October 2026

The core distinction — that preference-sensitive decisions require a weighting the evidence does
not contain, and that effectiveness-sensitive ones do not — is mainstream and stable. The
expectations placed on the consultation are not: consent law, professional guidance and national
shared-decision-making policy differ by country and have moved substantially in several over the
last decade, generally toward a stronger requirement to discuss reasonable alternatives. The
evidence on decision aids continues to accumulate, and the open questions are about
implementation and equity of delivery rather than about whether the aids inform people. The
Generation III figures are stable because the games are finished, and the later-generation values
for these moves differ, which is why the generation is named. Take the legal and professional
requirements from the reader's own jurisdiction rather than from here, as of October 2026.
