---
id: "m059"
slug: calcium-and-the-parathyroid-loop
style: pokemon
category: endocrinology
difficulty: intermediate
question: "Why is calcium control the cleanest worked feedback loop in medicine, and how does the pair of calcium and parathyroid hormone locate the lesion?"
tags: [calcium, parathyroid, vitamin-d, phosphate, magnesium]
---

# Misty Terrain, one setter, and three answers on three different clocks

This is the loop to learn first, because every single part of it has a name you can point at.
**Misty Terrain** is the condition: while it is up, **grounded** Pokémon cannot be given a status
condition and cannot be confused, and Dragon-type moves aimed at grounded targets land for half
*(mechanism)*. **Tapu Fini** sets it with **Misty Surge** the instant it enters, for five turns,
or eight if it is holding a **Terrain Extender** *(mechanism)*. The reporter is **Flail**, whose
base power is read off the user's own remaining HP in six bands and counts **upward as the bar
falls** *(mechanism)* — the same reporter as the thyroid answer, because this is what these loops
look like.

And then three answers, which is the part that makes this the clean example. A priority move such
as **Aqua Jet** or **Mach Punch** resolves inside this turn, ahead of everything else
*(mechanism)*. **Leftovers** pays its sixteenth at the **end** of the turn *(mechanism)*. And
**Future Sight** is committed now and strikes **two turns later** *(mechanism)*. One controller,
three actuators, three clocks — this turn, end of turn, two turns out.

| In the battle | What it stands for |
| --- | --- |
| **Misty Terrain**: no status, no confusion, for grounded Pokémon | The controlled variable, held tight |
| **Tapu Fini**'s **Misty Surge**, on entry, five turns | The gland |
| **Flail**'s base power, 20 up to 200 as the bar falls | The controller's output, inverse |
| **Aqua Jet** or **Mach Punch**, resolving first, this turn | The fast actuator |
| **Leftovers**, a sixteenth at the end of every turn | The medium actuator |
| **Future Sight**, committed now, landing two turns later | The slow actuator |
| **Close Combat**: the user's Defence **and** Sp. Def each −1 | The paired opposite-direction readout |
| **PP**, and a **Leppa Berry** restoring 10 of it | The cofactor the reporter cannot work without |
| **Flygon**'s **Levitate**, which never feels terrain at all | A sensor out of the condition's reach |
| **Reflect**, halving what lands, changing nothing sent | The binding protein |

Claims are marked *(mechanism)*, *(definitional)*, *(consensus)* or *(country-dependent)* where it
matters.

## Why the tolerance is narrow at both ends

With **Misty Terrain** up, **Toxic** does not take, **Will-O-Wisp** does not take, **Stun Spore**
does not take, **Hypnosis** does not take and **Confuse Ray** does nothing, provided the target is
grounded *(mechanism)*. Lose it and all five land freely — which is the excitable end, where
anything at all can set the side off.

Over-supply is the other end, and here the analogy has to be honest about where it reaches. A side
that nothing can ever provoke is a side that nothing can stimulate either: it sits there,
unresponsive, and it is **the depression of excitability** that the real excess produces —
weakness, sluggishness, a system that will not fire. The real excess also produces confusion, and
that is exactly the thing **Misty Terrain** prevents, so the metaphor covers the excitability and
does not cover that *(mechanism)*. Said rather than glossed over.

## The loop, drawn with its clocks

```
                        ┌──────────────── MISTY TERRAIN ◄────────────────┐
                        │                 the controlled condition       │
                        ▼                                                │
              THE SENSOR: a grounded battler that feels it               │
              reads INVERSELY — the less it gets, the louder it is        │
                        │                                                │
                        ▼                                                │
              FLAIL   20 · 40 · 80 · 100 · 150 · 200                     │
              flat across the top third, steep at the bottom             │
                        │                                                │
      ┌─────────────────┼──────────────────────────┐                     │
      ▼                 ▼                          ▼                     │
   AQUA JET          LEFTOVERS                  FUTURE SIGHT             │
   priority: it      a sixteenth, paid at       committed this turn,     │
   resolves first    the end of the turn        LANDS TWO TURNS LATER    │
      │                 │                              │                 │
   THIS TURN         END OF TURN                  TWO TURNS OUT          │
      │                 │                              │                 │
      └─────────────────┴──────────────────────────────┴─────────────────┘

   And watch what the fast arm does to the OTHER number:
   CLOSE COMBAT lands for 120 and drops the USER'S Defence AND Sp. Def by one each.
   Neither drop alone tells you which move was used. The PAIR does.
```

Three clocks is the design, not an accident. You answer a problem first with something that
resolves inside the turn, then with something that pays at the end of it, and only then with
something you have to commit to and wait for *(mechanism)*. Cheap and fast first; slow and
committed last. Which is why the **time course** of a disturbance tells you which arm is carrying
it.

## The slow arm has no authority without its substrate

**Future Sight** is committed two turns before it lands, which means it is useless to you if the
battle will not still be there — and it is useless if you have no **PP** left in it. It is not a
fourth hormone and it is not an alternative to the fast arms; it is the arm with the longest reach
and the longest delay *(mechanism)*.

Take the slow arm away and the controller does not go quiet. It runs the fast arms harder, so
**Flail climbs while the terrain still looks adequate** *(mechanism)*. The loop is working. It is
working hard, and the loud reporter is reporting the effort, not a failure.

## The pair, which is the whole diagnostic move

| The terrain | Flail | What it means |
| --- | --- | --- |
| Plainly over-long | Loud, or quietly at 40 | The **setter** is not listening to the sensor |
| Plainly over-long | Pinned at 20 | The loop is working and **overridden** — someone else set it |
| Gone | 200 | The loop is **trying**: no substrate, no reach, no slow arm |
| Gone | 20 | The **controller** is gone — or has no PP left to report with |

The second row is worth its own sentence, because the mechanic is verified and it is the sharpest
thing in this answer: `TryChangeBattleTerrain` returns false when the terrain is already the one
being set, so your own **Tapu Fini** entering onto an opponent's Misty Terrain does nothing,
announces nothing, and refreshes no timer *(mechanism)*. The condition is up. Your loop is
correct. Your loop has simply been made redundant.

And the phrase that carries the whole skill is **"quietly at 40"**. Flail at 40 is an ordinary
number. Flail at 40 while the terrain is plainly over-long is **wrong**, because a working sensor
would have taken it to 20. A reading can be entirely ordinary and still be the wrong answer to the
question it was asked.

## The sensor that is out of reach, which is the cleanest case of all

Terrain reaches **grounded** battlers only. **Flygon** has **Levitate** as its only ability and
never feels Misty Terrain at all; the same goes for **Claydol**, for a Flying type, and for anyone
holding an **Air Balloon** until it pops *(mechanism)*.

Now put the **sensor** out of reach while the rest of the side is grounded. The sensor is
perfectly content at a level the rest of the side is not, so the controller settles at a new,
stable, **wrong** value and sits there quite happily. Nothing is diseased. Nothing is broken. The
thermostat is simply out of the room. **Gravity**, an **Iron Ball**, or **Ingrain** rooting it
would put it back in the room, and then the same sensor would read the same terrain completely
differently *(mechanism)*.

That is a set-point problem rather than a gland problem, and telling it apart from a gland problem
matters because the two get handled differently *(consensus)*.

## The cofactor, which is the thing everybody forgets

**Flail** has PP. Run it to zero and the reporter cannot report, however hard the condition pushes
— and the bar is exactly where it was, and the terrain is exactly where it was *(mechanism)*. A
**Leppa Berry** restores 10 PP, an **Ether** does the same *(mechanism)*, and the whole loop comes
back at once, because nothing was ever wrong with the sensor, the setter or any of the three
actuators.

A condition that will not come back no matter what you do to the actuators is the specific
situation in which the reporter's PP is what has been forgotten *(consensus)*.

## What was sent is not what lands

**Reflect** halves incoming physical damage for five turns, eight while the setter holds **Light
Clay**, and changes nothing whatsoever about the attacker *(mechanism)*. **Flail** at 200 into
Reflect lands like Flail at 100, and if you are grading the attacker by what the defender felt,
you are wrong about the attacker and nothing about the attacker moved.

Third answer in this specialty where that trap applies, with the same shape each time. One error,
three axes.

## Why losing the setter has the time course it has

Take **Tapu Fini** off the field and all three actuators are still there while the controller is
suddenly absent. The fast arm goes first, because priority moves are the ones being chosen turn by
turn. **Leftovers** keeps paying its sixteenth. And **Future Sight**, already committed, still
lands two turns later, after the controller that ordered it has gone *(mechanism)*. Fast arm out
first, slow arm out last — and the recovery runs the other way round. That ordering is readable
straight off the diagram, which is why the diagram is drawn with the clocks on it.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

Everything above is a picture of a feedback loop with one inverse sensor, three actuators on three
clocks, and a paired readout. The picture is fair, and it is the cleanest such picture in the
subject. What an abnormal result means for a person is not a battle.

Primary hyperparathyroidism is often found by accident, on a blood test taken for something else,
in someone who feels perfectly well. What happens next is genuinely contested — it depends on age,
on bone density, on kidney function and on how high the calcium is, and the guideline bodies that
publish on it do not agree. "Your calcium is high" is neither a diagnosis nor a plan, and a great
deal of avoidable fear lives in the gap between an abnormal number and a conversation about it.

Chronic hypoparathyroidism after neck surgery is a condition people live with permanently,
supplying from outside something the body normally regulates minute by minute, where being
slightly under-replaced and slightly over-replaced are both unpleasant and both common. People
living with it frequently say it is under-recognised, and that is worth taking at face value
rather than explaining.

And a note about who is reading. Someone reading this may have been told their calcium is
abnormal. If that is you: nothing above is a threshold, a target or a plan. A calcium result is
read alongside albumin, phosphate, kidney function, the hormone and the rest of the picture, by
the team that ordered it. Reading one number against a table — which is precisely the error this
answer is about — is not something to do from an analogy about terrain.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md)
for the standing documents of this specialty. Specific to this answer:

* Your national guideline on hyperparathyroidism and on investigating hypercalcaemia, for referral
  and intervention criteria, which differ between countries.
* Your national or regional guidance on chronic kidney disease mineral and bone disorder, which is
  a separate document and governs that whole situation.
* **Your own laboratory's handbook**, for its reference intervals, the albumin-adjustment formula
  it applies, whether directly measured ionised calcium is available, and the assays it runs.
* Your national formulary, for anything about calcium, vitamin D or active vitamin D analogue
  preparations and the monitoring they need.
* A current endocrinology or renal textbook, for calcium-sensing receptor biology, the inverse
  secretion curve, and the renal handling of phosphate.

The Pokémon side is different and is sourced properly. **Misty Terrain**'s status and confusion
protection and its grounded-only condition, the five-turn and eight-turn terrain timers, **Misty
Surge** on **Tapu Fini**, **Flail**'s six-band power table, **Future Sight** striking two turns
later, **Close Combat**'s 120 power with the user's Defence and Special Defence each dropping one
stage, the **Leppa Berry**'s 10 PP, **Levitate** on **Flygon** and **Claydol**, the grounding
effects of **Gravity**, an **Iron Ball** and **Ingrain**, **Reflect** with **Light Clay**, and the
fact that a Surge ability does nothing and refreshes no timer on its own terrain were all read
from the pokeemerald and pokeemerald-expansion decompilations rather than from memory.

## Scope and safety

The Pokémon here is doing one job: making a feedback loop with one inverse sensor, three actuators
on three clocks and a paired readout concrete. It is not a clinical reference, not a decision aid,
and not about any individual's care. **No reference intervals, thresholds, doses, adjustment
formulae or intervention criteria appear here on purpose** — they differ between laboratories,
countries and guideline bodies, they are revised, and the units calcium is reported in differ too.
Your laboratory and your local guidance are the authority and this page is not. Severe
hypocalcaemia and severe hypercalcaemia are both medical emergencies and neither is described
here. Nothing here has had clinical review. If someone is unwell now, contact local emergency
services.

## What a Gym Leader digs into next

* Why is **Flail** at 40 sometimes the abnormal reading?
* Why does **Close Combat** identify itself through a pair of drops that neither drop makes alone?
* Why does a **Levitate** sensor settle the whole side at the wrong value without anything being
  broken?
* Why does a reporter with no PP look exactly like a reporter with nothing to report?
* Why does **Future Sight** still land after the controller that ordered it has gone?

## Where this stands, October 2026

The loop, its inverse sensor, the three clocks and the paired readout are mechanism and do not
date. What dates on the Pokémon side is the constants and the cast: terrains arrived in Generation
VI and the **Surge** abilities in Generation VII, **Future Sight**'s power and PP have both
changed across generations and only its two-turn delay has held, and **Rillaboom**, **Pincurchin**
and **Indeedee** carry their Surge as a **Hidden Ability**. Check the current generation's data.
On the clinical side everything numeric and procedural moves — reference intervals, adjustment
formulae, which vitamin D metabolite is measured, intervention criteria and the whole of the
kidney-disease mineral guidance — so check current local guidance and your own laboratory's
handbook.
