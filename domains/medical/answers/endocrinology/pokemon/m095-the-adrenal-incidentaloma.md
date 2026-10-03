---
id: "m095"
slug: the-adrenal-incidentaloma
style: pokemon
category: endocrinology
difficulty: intermediate
question: "An adrenal mass is found on a scan done for something else. What two questions does that force, and why are they independent?"
tags: [adrenal, incidentaloma, overdiagnosis, phaeochromocytoma, imaging]
---

# The Itemfinder has already beeped, and the slot is occupied. Occupied is not the same as active

The Generation III device is the **Itemfinder**, and its own description in the item data is "A
device that signals an invisible item by sound" — one beep, nothing about what the item is
(**mechanism**). The **Dowsing Machine** is the same device after its Generation IV rename, which
is the name the cortisol answer uses.

That answer's point was that running the thing before you know what you are looking for is the
classic error. This answer is the harder case, and it is the commoner one: **it has already
beeped.** You were on this floor for something else entirely, the beep arrived, and you cannot
un-hear it. There is a buried item there and there always was.

So now there are exactly two questions, and the whole skill is noticing that they are two.

**Is it doing anything?** Plenty of real held items do nothing whatever in a battle. An
**Everstone**'s hold effect is `HOLD_EFFECT_PREVENT_EVOLVE` and that is all it is; an **Amulet
Coin** doubles prize money; an **Exp. Share** divides experience; a **Soothe Bell** modifies a
friendship increment (**mechanism**). Every one of those is a genuine item in a genuine slot, and
the battle in front of you proceeds exactly as though the slot were empty. **Leftovers** in the
same slot returns a sixteenth of maximum HP at the end of every turn. Same slot. Same look.
Nothing in common.

**And is it dangerous?** Which is a completely different question, answered by looking the item up
rather than by watching what it does. Neither question's answer tells you a thing about the
other's.

| In the battle | What it stands for |
| --- | --- |
| The **Itemfinder** beeping while you were here for something else | The scan you did not order for this |
| A buried item that was always there | The lesion's base rate, which is high |
| An **Everstone**, an **Amulet Coin**, an **Exp. Share**, a **Soothe Bell** | Occupied, and inert |
| **Leftovers** in the identical-looking slot | Occupied, and functioning |
| **Arbok**'s **Intimidate** against **Metagross**'s **Clear Body** | The push: does it give? |
| **Knock Off** against **Sticky Hold** | The other push: is it holding on? |
| An opposing Ability recorded **only when it fires** | Function cannot be looked up |
| `GetPokedexHeightWeight`, which **can** be looked up | Nature can. That is the asymmetry |
| A **Toxic Orb** or a **Flame Orb** | An item whose whole effect is on its holder |
| **Mt. Moon**'s encounter table against the route's | The same beep means different things by floor |
| **Zubat** on every floor; **Clefairy** only here | Base rate against the thing you were worried about |
| Both setters gone — no **Tapu Bulu**, no **Tapu Lele** | Bilateral: the question inverts to shortage |
| **Shedinja**'s 1 HP beside its **Wonder Guard** | Two properties, neither predicting the other |

**This answer defers to three others.** m058 owns the **Dowsing Machine** as imaging and
**Intimidate** against **Clear Body** as the push. m057 owns the two-setter split. m011 owns the
same rustle on a different floor. All three appear here; none is re-argued.

Claims are marked (**mechanism**), (**definitional**), (**consensus**) or (**country-dependent**)
where it matters.

## The grid, which is the whole structure

```
                           IS IT DOING ANYTHING?
                      no                        yes
                 ┌─────────────────────┬─────────────────────┐
                 │                     │                     │
            no   │  an Everstone.      │  Leftovers. Small,  │
                 │  The common cell    │  quiet, and acting  │
     IS IT       │  by a long way,     │  every single turn  │
     DANGEROUS?  │  and the battle     │                     │
                 │  never notices      │                     │
                 ├─────────────────────┼─────────────────────┤
                 │                     │                     │
            yes  │  something whose    │  both at once       │
                 │  harm is in the     │                     │
                 │  picking up, doing  │                     │
                 │  nothing in battle  │                     │
                 └─────────────────────┴─────────────────────┘

   ── WHY ALL FOUR CELLS ARE OCCUPIED ────────────────────────────────────────

   Shedinja is the cleanest proof available that two properties of one thing
   need not predict each other: exactly 1 maximum HP, and Wonder Guard. How
   much it has, and what can reach it. Independent fields. Neither readable
   from the other.

   ── AND THE TWO QUESTIONS TAKE DIFFERENT KINDS OF TEST ─────────────────────

   DOING ANYTHING   you PUSH. Send in Arbok. Try Knock Off. The game records
                    an opposing Ability only when it fires, so there is no
                    entry to look up until you have made it happen.

   DANGEROUS        you LOOK IT UP. Cmd_weightdamagecalculation reads
                    GetPokedexHeightWeight straight out of the dex. No push
                    required, and the number is there before you arrive.
```

## Question one: occupied is not active, and you only learn it by pushing

Two pushes, both established in this specialty, and they ask different things.

**Send in Arbok.** Its **Intimidate** lowers every opposing battler's Attack by one stage on
entry. If the stage drops, the stat obeys the ordinary rules. If **Metagross** is out with **Clear
Body**, or **Torkoal** with **White Smoke**, nothing moves at all (**mechanism**). You measured
nothing; you pushed, and the answer is in whether it gave. That is the cortisol answer's device
and it arrives here unchanged, which is the point — autonomy is the claim, not amount.

**Or try to take the item.** **Knock Off** removes it; **Sticky Hold** stops the removal and fires
a message when it does (**mechanism**). And here is the fact that makes it the right device for an
incidental find: the game records an opposing Ability **only when it fires**. Until you push, the
field holds no entry for it whatsoever. Function is not a property you can read off the screen; it
is a property you have to provoke.

One discipline that follows, and it is the reason a short targeted list beats a broad sweep. If
the holder has no item at all, the **Sticky Hold** branch simply advances and nothing is recorded
(**mechanism**). The push returns a blank. A blank is not a negative, and a floor full of blanks
is how a sweep turns into a sequence of things you now have to go back and check.

## Question two: what it is, which you look up rather than provoke

`Cmd_weightdamagecalculation` sets **Low Kick**'s base power by walking a weight table against
`GetPokedexHeightWeight(...)` — the **Pokédex** entry's figure, which is there before you ever
meet the thing and is identical for every individual of the species (**mechanism**).

That is the whole asymmetry between the two questions. One of them has an entry you can consult.
The other has no entry until you have made something happen. A reasoning process that treats them
as one question will use the wrong kind of test for one of them, and the usual direction of that
error is to try to answer "is it dangerous" by watching what it does.

## The find you do not dig up

There is a class of item whose entire effect is on **whoever is holding it**. A **Toxic Orb**
badly poisons its own holder in battle; a **Flame Orb** burns its own holder (**mechanism**). Both
are Generation IV items rather than Generation III ones, and that is worth pinning rather than
smoothing over.

The point they make is the one the real version makes about a needle. For most buried items,
digging it up is how you find out what it is, and the cost is a few steps. For this class, **the
acquisition is the event** — and the harm has nothing to do with whether you learn anything. So
there is one question you settle *before* you dig, and settling it first is mechanical rather than
procedural (**consensus**).

And the second reason not to dig is that for the hardest case it does not work. Two cortical
lesions are made of the same cells, and a small sample cannot separate them — which in these terms
is a dig that comes back with "an item" and no entry (**mechanism**). You paid the cost and the
beep is still unexplained.

**And the same beep on a different floor is a different beep.** The general-practice answers own
this device and it belongs here without alteration: **the same
rustle on a different floor.** **Zubat** is on every floor of **Mt. Moon** and **Clefairy** is
not, so an identical rustle carries a different expectation in the two places, and the expectation
comes from the encounter table rather than from the rustle (**mechanism**).

A beep in a cave you are walking through for no particular reason is one thing. The identical beep
in a cave you are in **because you already know something is wrong** is another, and the
difference is entirely outside the sound. Nothing about the beep changed. The table did.

## Two slots occupied, which inverts the question

If **both** of a side's setters are gone — no **Tapu Bulu** holding up **Grassy Terrain**, no
**Tapu Lele** holding up **Psychic Terrain** — the adrenal-insufficiency answer's two-column
diagram is what applies, and the question is no longer whether something is making too much. It is
whether anything is making enough (**mechanism**). **Flail** pinned loud over a bare field is the
pattern to recognise, and it is the opposite of the pattern this answer started from.

That is not a doubling of the one-slot question. It is a different question, with a different
differential, reached by noticing that there are two.

## The harm the pathway does, and the order you cannot have

The cortisol answer's error was running the **Dowsing Machine** first. Here you do not get that
choice: the beep has happened, and an un-hearing mechanic does not exist in any generation.

What is available is to reconstruct the order on purpose. Decide what the encounter table on
**this** floor says you should expect, and only then decide what the beep means. **Flail** loud
says the fault is at the level above and a find there matters. **Flail** at 20 says the setter is
autonomous and the same find at the level above means nothing (**mechanism**). Identical beep,
opposite meaning, decided entirely by what you established first — and you can still establish it
afterwards, which is the one piece of good news in the whole topic.

How many times you walk the floor again afterwards, and for how many years, is local
(**country-dependent**), and the direction of travel has been towards fewer walks.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

Everything above is a picture of two independent properties of one finding, of the different kinds
of test each one needs, and of why an identical observation carries a different meaning depending
on why you were looking. The picture is fair. Nothing above stands in for a person — the buried
item is a finding on a scan, not somebody.

Being told there is something on your adrenal gland, when you went for a scan about something else
entirely, is a specific kind of distressing, and the distress is not proportional to the risk. A
large part of what the work-up is for is ending the uncertainty rather than finding disease, and
saying that plainly to the person is usually more use than a description of the statistics.

There is an equity dimension too. Incidental findings arrive in proportion to how much imaging
someone has had, and that tracks how much contact they have had with healthcare for other reasons.
So the pathway is entered unevenly, and the burden of years of surveillance ends up distributed by
something other than risk.

And a note about who is reading. Someone reading this may have been told they have an adrenal
nodule and be waiting for tests. If that is you: nothing above is a threshold, a protocol, a
timescale or a reassurance. A result means something only alongside the rest of the picture and in
the sequence it was taken in, and that reading belongs to the team that ordered it — not to an
analogy about buried items.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md)
for the standing documents of this specialty. Specific to this answer:

* Your national or specialty-society guidance on the management of adrenal incidentalomas, for the
  investigations recommended, the imaging criteria, the surgical indications and the follow-up
  policy. European and North American guidance differ and recent revisions have reduced the
  surveillance advised, so the current version of the one that applies where you work is the
  authority.
* Your national or specialty-society guidance on primary aldosteronism, and on phaeochromocytoma
  and paraganglioma, for the sampling preparation and the sequence around any intervention.
* **Your radiology department's protocol**, for the unenhanced attenuation criteria it uses and
  how it words a report.
* **Your laboratory's handbook**, for the cortisol, aldosterone, renin and metanephrine assays it
  runs and their sample handling.
* A current endocrinology or pathology textbook, for the lipid content of cortical adenomas, the
  limits of needle biopsy in cortical lesions, and the differential for bilateral adrenal
  enlargement.

The Pokémon side is different and is sourced properly. The Generation III item being named
**ITEMFINDER** with the description "A device that signals an invisible item by sound"; the
**Everstone**'s `HOLD_EFFECT_PREVENT_EVOLVE`, the **Amulet Coin**'s `HOLD_EFFECT_DOUBLE_PRIZE` and
the **Exp. Share**'s and **Soothe Bell**'s hold effects, none of which touches a battle;
**Leftovers**' `HOLD_EFFECT_LEFTOVERS`; **Sticky Hold** blocking **Knock Off** and the fact that
an opposing Ability is recorded only when it fires; **Shedinja**'s maximum HP being forced to 1 in
`CalculateMonStats` independently of its Ability; and `Cmd_weightdamagecalculation` reading
`GetPokedexHeightWeight` were all read from the pokeemerald and pokeemerald-expansion
decompilations rather than from memory. Two notes on provenance. The **Dowsing Machine** name does
not exist in Generation III at all — the string in the data is **ITEMFINDER** — so that name is
pinned to Generation IV onward here rather than used loosely. And a **Toxic Orb** and a **Flame
Orb** are Generation IV items: their holder-poisoning and holder-burning hold effects were read
from the expansion's item data, and they are not in the Generation III table.

## Scope and safety

The Pokémon here is doing one job: making it concrete that an incidental finding forces two
independent questions, that they need different kinds of test, and that the same observation means
different things depending on why you were looking. It is not a clinical reference, not a decision
aid, and not about any individual's care. **No size thresholds, attenuation values, biochemical
cut-offs, ratios or surveillance intervals appear here on purpose** — they differ between
countries, institutions and radiology departments, they have been revised recently and in one
direction, and a revision page is the wrong place to get them from. Check your local guidance,
your radiology protocol and your laboratory's handbook. Nothing here has had clinical review. The
metaphor covers mechanism and stops at outcome: a catecholamine-secreting tumour can produce a
cardiovascular emergency and that is not material for a battle analogy. If someone is unwell now,
contact local emergency services.

## What a Gym Leader digs into next

* Why does knowing what the item is tell you nothing about whether it is doing anything?
* Why is a blank from **Sticky Hold** not a negative result?
* Why can **Low Kick**'s power be looked up when an Ability cannot?
* Why is there one question you settle before you dig rather than by digging?
* Why does losing **both** setters turn the question from too much into not enough?

## Where this stands, October 2026

The independence of the two questions, the different kinds of test each one takes, the
look-it-up-against-provoke-it asymmetry and the prior-from-context argument are mechanism and do
not date. What dates on the Pokémon side is the names and the constants: the Generation III item
is the **ITEMFINDER** and only becomes the **Dowsing Machine** from Generation IV, a **Toxic Orb**
and a **Flame Orb** are Generation IV items, **Sticky Hold**'s coverage was widened after
Generation III, **Knock Off**'s power and secondary behaviour have been revised more than once,
and the terrains and **Surge** abilities arrived in Generations VI and VII. Check the current
generation's data. On the clinical side the surveillance policy has moved recently and
substantially, and so have the thresholds, attenuation criteria, cut-offs and surgical indications
— so check current local guidance, your radiology department's protocol and your laboratory's
handbook.
