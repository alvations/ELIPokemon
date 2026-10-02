---
id: "m091"
slug: pituitary-mass-effect-and-sequential-failure
style: pokemon
category: endocrinology
difficulty: advanced
question: "Why does a pituitary lesion cause trouble in two unrelated ways, and why do its hormone axes fail in a predictable order?"
tags: [pituitary, hypopituitarism, mass-effect, prolactin, apoplexy]
---

# Four move slots with four different printed PP, and an Earthquake that hits whoever is standing next to it

Nothing in this answer stands in for a person. The battler in the middle is a **gland**, the slots
either side of it are **structures**, and the whole picture is a diagram of plumbing.

Start with the four slots, because they are the hormonal half. **Gengar**'s Generation III
level-up learnset gives it **Hypnosis** at 20 PP, **Night Shade** at 15, **Confuse Ray** at 10 and
**Mean Look** at 5 — four slots, four different printed reserves, and nothing on the screen
telling you which is closest to empty *(mechanism)*. Put **Dusclops** on the other side and its
**Pressure** deducts one extra PP from every move used against it, turn after turn, equally,
caring nothing for which slot it is spending *(mechanism)*. A perfectly even drain, and the slots
still empty in a fixed order: **Mean Look** first, then **Confuse Ray**, then **Night Shade**,
then **Hypnosis**. The order is not about where the pressure is. It is about what each slot
started with.

Now the second, completely separate problem. **Earthquake** is written in the Generation III data
with `.target = MOVE_TARGET_FOES_AND_ALLY` — in a double battle it hits every adjacent battler
including the one on your own side, regardless of what it was aimed at *(mechanism)*. That is not
a hormonal fact about the user. It is a fact about **where things are standing**. One lesion, two
jobs, and neither predicts the other.

| In the battle | What it stands for |
| --- | --- |
| **Gengar**'s four slots: **Hypnosis** 20, **Night Shade** 15, **Confuse Ray** 10, **Mean Look** 5 | The anterior lobe's axes, and their reserve |
| **Dusclops**'s **Pressure**, one extra PP per use, evenly | Progressive compression of the lobe |
| The slot with the smallest printed PP going first | The order of axis failure, which is about margin |
| **Earthquake**, `MOVE_TARGET_FOES_AND_ALLY` | Mass effect: the lesion hits its neighbours |
| **Flygon**'s **Levitate**, an **Air Balloon** | An adjacent structure the mass does not reach |
| **Gravity**, an **Iron Ball**, **Ingrain**, **Smack Down** | What makes an unreached structure feel it |
| **Imprison**, tonic while its user is on the field | Dopamine down the stalk: the one brake |
| The sealed move freeing the instant that user leaves | The stalk effect, and the hormone that rises |
| **Grassy Terrain**, **Psychic Terrain**, **Misty Terrain**, **Electric Terrain** | The axis hormones, as in m056–m060 |
| A quiet **Flail** over a bare field | A low target hormone, reporter not raised |
| **Drizzle** persisting after **Kyogre** has left | The posterior lobe: a standing property, not a move |
| A **Leppa Berry**'s 10 PP, into one chosen slot | Replacement, one axis at a time |
| **Spite**, taking 2 to 5 PP from one slot at once | The sudden version — and only one slot |

**Three answers already hold ground this one needs, and it defers to all three.** m056 owns
**Flail** as the inverted reporter and the pattern table. m057 owns the two-column split and
`TryChangeBattleTerrain` refusing to refresh its own timer. m058 owns **Intimidate** against
**Clear Body** as the suppression test. None of them is re-derived here.

Claims are marked *(mechanism)*, *(definitional)*, *(consensus)* or *(country-dependent)* where it
matters.

## The field, drawn to scale, because the geometry is the argument

```
                        THE SLOT DIRECTLY ABOVE
          what is standing there is reached first by anything that grows
                                    │
                                    │   it is reached because of WHERE it is,
                                    │   not because of what the gland secretes.
                                    ▼
        ┌───────────────────────────────────────────────────────┐
        │                  THE LEVEL ABOVE                      │
        │              Helping Hand · Imprison                  │
        │                         │                             │
        │                   THE CHANNEL                         │
        │       the moves go down here ──┼── the Ability does not │
        └─────────────────────────┼─────────────────────────────┘
                                  │
   THE SLOT TO THE LEFT           ▼            THE SLOT TO THE RIGHT
   adjacent, so Earthquake    ┌─────────┐      adjacent, so Earthquake
   reaches it                 │ GENGAR  │      reaches it
                              │ 4 slots │
                              └─────────┘

   ── WHO FEELS WHAT, AND IT IS ONE CHECK ────────────────────────────────────

   IsBattlerGroundedInverseCheck reads, in this order:
       Iron Ball        → grounded
       Gravity          → grounded
       Ingrain          → grounded
       Smack Down       → grounded
       Telekinesis / Magnet Rise            → NOT grounded
       Air Balloon / Levitate               → NOT grounded
       Flying type                          → NOT grounded

   The overrides are tested BEFORE the exemptions. Gravity beats Levitate.

   And it is the SAME function that decides who feels the terrain. One check,
   two layers: a hormone reaching a tissue, and a mass reaching a structure.
```

That shared check is the thing worth carrying away. In the thyroid and calcium answers, grounded
meant *has the receptor*; **Flygon** never felt the terrain however much of it there was. Here
grounded means *is in the way*. The code does not distinguish them, and neither does the anatomy:
a thing is either reachable or it is not, and the exemptions lose to the overrides either way
*(mechanism)*.

Two separate deliveries sit either side of that channel. The four **moves** need the channel: they
cost PP, they can be sealed, and cutting the channel strands them even though the slots are
intact. The **Ability** does not. **Drizzle** keeps raining after **Kyogre** has left the field —
the house asymmetry from the pharmacology answers — and that is the posterior lobe: made upstream,
delivered down the nerve, and untouched by a lesion sitting inside the box *(mechanism)*. Sever
the channel and you lose both. Fill the box and you usually lose only the moves.

## The channel, and the one move that gets *easier* when you cut it

**Imprison** is the mechanic that makes this topic land. Its Generation III implementation seals
moves on the other side for as long as its user stays on the field, and — this is the part people
misremember — **it fails outright unless the sealer and the sealed share a move**:

```
   for each foe:
       for each of MY four moves:
           if that move is also in the foe's four → seal
   if no foe shares a single move → Imprison FAILS
```

The comment in the decompilation says so in as many words *(mechanism)*. The brake only works
because both ends speak the same language. Take away the shared move and the brake does not exist.

Now cut the channel. Every move that was coming *down* it stops arriving — and the one move that
was being held *shut* by **Imprison** is free the moment its user is off the field. So one output
goes **up** while every other output goes down, and it goes up for a reason that has nothing to do
with the gland having decided to make more of it *(consensus)*.

That is why a loud readout on that one output does not establish that the lesion is making it. It
is equally the signature of a lesion that is merely leaning on the channel. How loud is loud
enough to separate the two is a local matter and the figures belong in the laboratory handbook,
not here *(country-dependent)*.

And it is why this is the one lesion that can be made smaller by **reapplying its own brake**. The
slot still holds the receiving end. Put the inhibition back from outside and the thing shrinks
*(consensus)*. **Disable** is the contrast that proves the point: four turns, on whatever move was
last used, no shared-move requirement and no choosing. Tonic and targeted is a different mechanic
from brief and arbitrary, and only the first one can be reapplied on purpose.

## The slots empty in printed order, and the order is about reserve

Run **Dusclops** opposite **Gengar** and the sequence is forced: **Mean Look** at 5 PP is the
first slot to go dark, and **Hypnosis** at 20 is the last. Nobody chose that. The drain was
identical across all four.

The real axis ordering has the same character — the usual teaching is growth hormone and the
gonadotrophins first, then thyrotropin, then corticotropin, and prolactin behaving separately for
the reason above *(consensus)*. Like the PP table it is a tendency rather than a law, and
individual battles depart from it.

What the mapping gets right is the **reason**. The order is not a statement about how hard the
drain is pressing, because the drain is even. It is a statement about the printed reserve
*(mechanism)*. And the honest limit of the mapping is that **Gengar**'s PP figures are printed in
the data where you can read them, and the real reserves are not — the mechanistic account of why
those particular axes have the least margin is not fully settled, and I am not going to invent
one.

Two readings fall out. One dark slot should send you to look at the other three, because the gland
fails as a gland. And the slot that survives longest here is the one whose loss matters most,
which turns the usual relationship between *late* and *urgent* upside down.

## Reading it: the pair, and the reporter that fails to shout

Same move as every other answer in this specialty. Read the terrain **and** the reporter, as a
pair, and ask whether the reporter is behaving appropriately for the field it is standing on
*(mechanism)*.

**Flail** at 200 over a bare field puts the fault at the setter. **Flail** sitting quietly at 20
over a bare field puts the fault at the level above — and that is the dangerous pattern, because
nothing is complaining. An ordinary reading next to an obviously empty field is not a reassurance;
it is the finding. The reporter that should be shouting and is not has told you where the lesion
is *(mechanism)*.

For the axes whose output arrives in bursts, one basal pair settles nothing and the test becomes a
push: supply the condition from outside, or send the setter in deliberately, and watch. Which
push, how, and what counts as a response differ by country and by laboratory and are not on this
page *(country-dependent)*.

## Why you refill one slot before another

A **Leppa Berry** restores 10 PP, and its `holdEffectParam` in the Generation III data is
literally the number 10 — one berry, one slot, your choice of which *(mechanism)*.

The choice is not free. Refilling one particular slot raises the rate at which a *different*
slot's supply is consumed, so topping up the wrong one first can turn a side that was just about
coping into one that is not *(consensus)*. The mechanism is a clearance interaction and it is the
reason the order is fixed rather than a matter of preference. Which preparation, how much and in
what sequence is formulary and protocol, differs between countries, and is deliberately not here.

## The sudden version, and where the games give me nothing

**Spite** takes 2 to 5 PP in one hit — `(Random() & 3) + 2`, and only if the slot has more than 1
PP left — from whichever move was last used *(mechanism)*. One slot. One event. Large.

The acute pituitary syndrome is all four slots and both neighbouring structures in the same
instant, and Generation III has no mechanic that does that. I could dress one up. I am not going
to: the games give me a sudden bite out of **one** slot and nothing more, and the honest thing is
to name the gap and hand the rest to the plain-prose section below, the way the reproductive-axis
answer did when the games had no picture for an oscillator's phase.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

Everything above is a picture of two independent failure modes of one structure — what it
secretes, and the room it occupies — and of why an evenly applied insult still produces an ordered
sequence of losses. The picture is fair. A gland is not a battler and a visual field is not an
adjacent slot.

Pituitary disease is slow, and the things it takes first are the things people are routinely told
to expect from ordinary life: tiredness, loss of libido, mood change, less tolerance of exercise.
Several years between the first symptom and the diagnosis is common and documented, and it is
usually nobody's single mistake. Saying that is more useful than presenting the diagnosis as
straightforward.

Visual field loss from chiasmal compression is often not noticed by the person who has it, because
perception fills the gap in and each eye covers for the other. That is a fact about how vision
works, not about how carefully someone is paying attention, and it is why formal field testing
exists instead of asking.

And a note about who is reading. Someone reading this may have a pituitary adenoma, or be waiting
for a scan or a surgical opinion about one. If that is you: nothing above is a threshold, a dose,
a plan or a prognosis. Replacement arrangements, cover for illness and surgery, and what any one
result means in the sequence it was taken in all belong to the team holding the case. The plan you
already have is the one that applies, and it is not something to re-derive from an analogy about
move slots.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md)
for the standing documents of this specialty. Specific to this answer:

* Your national or specialty-society guidance on pituitary adenomas and on hypopituitarism, for
  the diagnostic sequence, the dynamic tests in use and the follow-up intervals.
* Your national or specialty-society guidance on prolactin-secreting tumours, for how a raised
  prolactin is attributed and for the place of medical therapy.
* **Your own institution's protocol** for suspected pituitary apoplexy and for perioperative cover
  in pituitary surgery. It overrides a national document where the two differ.
* Your laboratory's handbook, for the assays it runs and how it reports them.
* A current neuroanatomy text, for the chiasmal decussation, the cavernous sinus and the
  hypophyseal portal circulation.
* A current endocrinology textbook, for the anterior lobe's cell lineages and the usual order of
  axis loss.

The Pokémon side is different and is sourced properly. **Gengar**'s Generation III level-up
learnset, the printed PP of **Hypnosis**, **Night Shade**, **Confuse Ray** and **Mean Look**,
**Dusclops**'s **Pressure** and its one-extra-PP deduction, **Earthquake**'s
`MOVE_TARGET_FOES_AND_ALLY`, **Imprison**'s shared-move failure condition, **Disable**'s
Generation III duration and 55 accuracy, **Spite**'s `(Random() & 3) + 2` and its
more-than-1-PP guard, the **Leppa Berry**'s `holdEffectParam` of 10, and the order in which the
grounding check tests **Iron Ball**, **Gravity**, **Ingrain** and **Smack Down** before
**Telekinesis**, **Magnet Rise**, an **Air Balloon**, **Levitate** and the Flying type were all
read from the pokeemerald and pokeemerald-expansion decompilations rather than from memory. Two
notes on what was **not** read from code. **Surf** does not hit an ally in Generation III — its
target is written as `MOVE_TARGET_BOTH`, the two foes only, which is why **Earthquake** is doing
this job here and **Surf** is not. And the *size* of the spread-damage reduction that later
generations apply to a move like **Earthquake** in a double battle is not stated here, because the
Generation III source shows only its absence and the later figure was not read from a
decompilation reachable from this environment.

## Scope and safety

The Pokémon here is doing one job: making two independent failure modes of a single structure, and
an ordered sequence of losses under an even insult, concrete. It is not a clinical reference, not
a decision aid, and not about any individual's care. No doses, thresholds, assay cut-offs, test
protocols or replacement regimens appear here on purpose — they differ between countries,
institutions and laboratories and are revised, and a revision page is the wrong place to get them
from. Check the formulary and your local protocol. Nothing here has had clinical review. The
metaphor covers mechanism and stops at outcome: the acute pituitary syndrome is an emergency and
is not material for a battle analogy. If someone is unwell now, contact local emergency services.

## What a Gym Leader digs into next

* Why does an even drain still empty the slots in a fixed order?
* Why does **Imprison** fail unless the two sides share a move, and what does that say about why a
  brake can be reapplied from outside?
* Why does cutting the channel send one output up while every other output goes down?
* Why is a quiet **Flail** over a bare field worse news than a loud one?
* Why does **Gravity** beat **Levitate**, and why is it the same check that decides who feels the
  terrain?

## Where this stands, October 2026

The two-independent-problems structure, the reserve argument behind the ordering and the
tonic-brake asymmetry are mechanism and do not date. What dates on the Pokémon side is the
constants and the cast: **Disable** runs four to seven turns in Generation IV and two to five
before that, **Spite** became a flat deduction from Generation IV, **Earthquake** takes no
spread-damage reduction in a double battle in Generation III and takes one in later generations,
**Gravity** and **Smack Down** are Generation IV moves and an **Air Balloon** a Generation V item,
and the terrains arrived in Generation VI with the **Surge** abilities in Generation VII. Check
the current generation's data. On the clinical side everything procedural and numeric moves —
dynamic tests, assays, size conventions, imaging and surveillance intervals, surgical indications
and the drug classes named in guidance — so check current local guidance and your own
institution's protocol.
