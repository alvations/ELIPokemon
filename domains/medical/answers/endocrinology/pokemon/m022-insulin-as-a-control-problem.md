---
id: "m022"
slug: insulin-as-a-control-problem
style: pokemon
category: endocrinology
difficulty: advanced
question: "Why is replacing insulin with injections intrinsically hard, and what do basal and bolus each do?"
tags: [insulin, basal-bolus, feedback, control-lag, hypoglycaemia]
---

# Leftovers every turn, or a Sitrus Berry at the threshold. The real thing is both, and neither is a move.

**Leftovers** restores a sixteenth of the holder's maximum HP at the end of every turn, costs no
turn, needs no decision, and never has to be told that the bar has moved. A **Sitrus Berry** does
nothing at all until HP drops to half or below, then fires once, restores its amount, and is
consumed. Those two items are the two halves of the job: continuous suppression in the background,
and a single sharp response to a load. The real system does both from inside the Pokémon, on its
own clock, with the sensor and the effector in the same body. Replacing it from the Trainer's side
turns a closed loop into an open one — you commit before you know what is coming, through a route
that cannot be recalled, reading a bar that is already out of date *(mechanism)*. That is the
whole difficulty.

| In the battle | What it stands for |
| --- | --- |
| **Leftovers**: 1/16 of max HP, every turn, unconditionally | Basal — continuous, proportional, suppressive |
| **Sitrus Berry**: fires at the half-HP threshold, then gone | Bolus — threshold-triggered, single-shot |
| The berry already in the item slot before the turn | Pre-made granules: the only way to act this turn |
| A held item resolving at the holder | Secretion into the portal vein, acting locally first |
| An item used from the bag, costing the whole turn | Replacement by a route the body never used |
| **Rain Dance**: 5 PP, five turns, cannot be recalled | A dose: committed the moment it is given |
| The HP bar animating toward the stored value | A measurement that trails the real one |

Claims are marked *(mechanism)*, *(consensus)* or *(guideline-dependent)* where it matters.

## The pattern, and why it has that shape

The background job is suppression. **Leftovers** is proportional to the holder's own maximum,
costs nothing, and runs whether or not anything is happening — which is exactly the shape a
background correction has to be, because its purpose is that nothing drifts while nobody is paying
attention *(mechanism)*.

The load job is different and needs to be fast, so the games solve it the way the body does: the
response is **already present before it is needed**. A Sitrus Berry that had to be fetched would
arrive a turn late; a Sitrus Berry sitting in the item slot resolves inside the turn the damage
landed *(mechanism)*. That is what pre-made, pre-docked stores are for, and it is the only way to
act faster than manufacture allows. Behind it, Leftovers keeps ticking — a sharp first response
and a sustained second one *(consensus)*.

Two things about the route have no counterpart in anything you do from the bag. A **held** item
resolves at its holder, in the holder's own end-of-turn slot, before the rest of the field has any
part in it. And the Trainer's version — a potion from the bag — costs the entire turn, so the
opponent acts first and the correction arrives after the damage it was meant to cover
*(mechanism)*. Worse, the held berry only learns about trouble from its own HP threshold, which is
downstream of the hit; a Trainer watching the opponent select a move knows *before* anything
lands. Replacement throws that early warning away *(mechanism)*.

## Where the lag enters, drawn to scale

```
   CLOSED LOOP (the Pokémon's own items and abilities)
   ──────────────────────────────────────────────────
   bar falls ──► threshold crossed ──► berry fires ──► holder ──► field sees it later
      ▲            same turn              same turn      instant      next turn
      │                                                                  │
      └─────────── bar recovers, the trigger un-trips ◄──────────────────┘
                   the correction begins while the damage is still landing

   OPEN LOOP (the Trainer, from outside)
   ────────────────────────────────────
   decision ──► turn spent ──► effect enters ──► resolves ──► still running later
      │           now           end of turn       one turn     several turns
      │                             ╎
      │                             ╎ ◄── Rain Dance is now committed for five
      │                             ╎     turns. It cannot be shortened, and it
      │                             ╎     FAILS if you try to re-use it in rain
      ▼
   what you read ◄──── the bar, animated over frames, in 48 pixels ──────┘

   one turn, in order (Generation III end-of-turn phase, in the real order)
   ───────────────────────────────────────────────────────────────────────
   Ingrain heals        ▲
   held items resolve   ▲   ← the corrections all pay out HERE
   Leech Seed drains        ▼
   poison damage            ▼   ← and the drains land AFTER them
   burn damage              ▼

   so every correction is calculated against the state BEFORE this turn's
   drains, and lands with the next turn's damage already selected
```

The two halves of that last block are the entire clinical problem. The corrections resolve first
and are sized against information that is already one phase stale; the drains resolve afterwards.
Both are consequences of dead time, not of carelessness *(mechanism)*.

## Why controlling this from outside is hard

1. **Dead time, with an actuator you cannot take back.** **Rain Dance** commits five turns the
   instant it is clicked. It cannot be cut short, and it cannot be topped up — used while it is
   already raining it simply fails, with five PP and a wasted turn gone *(mechanism)*. A
   controller that cannot withdraw its last action has to predict *and* stay conservative.
2. **The disturbances are not visible.** The opponent's held item, their ability, whether they
   switch, a **Quick Claw** going off, a **Critical Hit**, and the damage roll itself — spread
   over sixteen values between 85% and 100% — are all decided after you have committed
   *(consensus)*. A controller blind to its disturbances cannot be tight.
3. **The two directions of error are not equal, and here the battle analogy stops.** Overshooting
   a correction in Pokémon wastes HP you could not use. Overshooting insulin causes hypoglycaemia,
   which does harm within minutes, and severe hypoglycaemia can cause seizure, loss of
   consciousness and death *(consensus)*. That is not a battle outcome and it is not material for
   a metaphor. It is the reason a rational controller biases toward running high and accepts a
   worse average: the two failures are not symmetrical, and only one of them is fast.
4. **The arm that should rescue an overshoot is also broken.** The field conditions are reciprocal
   — **Dry Skin** gains an eighth per turn in rain and loses an eighth per turn in harsh sunlight,
   so a working pair of setters is what keeps the bar inside a band *(mechanism)*. With no
   **Groudon** left to put sun back up, nothing pulls the bar the other way. Plainly, in the
   clinic: in long-standing type 1 diabetes the glucagon response to a falling glucose is lost and
   the adrenergic warning symptoms blunt, and repeated lows lower the threshold at which any
   warning appears at all *(consensus)*. The system that should rescue an overshoot degrades with
   every overshoot.
5. **What you read is not what you are controlling.** The HP bar is drawn in forty-eight pixels
   and animated toward the stored value over several frames, so the bar you are looking at trails
   the number the game is holding, and it is quantised on the way *(mechanism)*. Controlling a
   lagged, coarsened estimate through a lagged actuator is the textbook recipe for oscillation.

## What the two items actually are

They are not two sizes of one thing. **Leftovers** is a *fraction of the holder's own maximum*, so
it scales with the Pokémon: a **Blissey**, with the highest base HP in the games at 255, banks a
large absolute amount, while a **Shedinja**, whose maximum is 1, gets the one-point floor. The
**Sitrus Berry** in Generation III was a *flat* 30 HP whatever it was attached to — nearly all of
it wasted on Shedinja, a rounding error on Blissey — and the **Oran Berry** is a flat 10 on the
same half-HP trigger to this day *(mechanism)*. The games eventually changed Sitrus to a quarter
of maximum HP, and that change is the whole argument: a fixed absolute amount against a variable
size is wrong in both directions, which is why the background correction is the proportional one.

Getting the background wrong shows as the bar drifting when nothing is happening. Getting the
threshold response wrong shows as a spike or a crash tied to one specific hit. Telling those two
apart from a battle log — by looking at the quiet turns separately from the loud ones — is the
actual skill, and it is why a log is read by period and not as an average *(mechanism)*.

**Ingrain** is as close as the games get to closing the loop: the Pokémon roots itself, restores a
sixteenth of its maximum every turn with no turn spent and no decision taken, and keeps doing it.
It also cannot switch out, it still only pays at the end of the turn, and it cannot act faster
than its own clock *(mechanism)*. Automated insulin delivery sits in the same place — it
measurably improves time spent in range *(consensus)* and it does not remove the lag, which is why
rapid change is still where the remaining failures cluster.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it. Point 3 above already dropped
the analogy; this is the full version of why.

Hypoglycaemia is the limiting factor in insulin therapy, and it is the reason the loop is
deliberately run loose rather than tight. Mild episodes are unpleasant, disruptive and
frightening. Severe episodes cause seizure, loss of consciousness and death. Impaired awareness of
hypoglycaemia removes the warning that would otherwise allow someone to treat it themselves, and
it is caused by the very thing it makes more dangerous. Fear of hypoglycaemia is a rational
response to a real hazard, not non-adherence, and it is routinely recorded as the latter.

The daily burden is the part the diagram hides, and the part the items in it trivialise. Leftovers
requires no decision. Replacing a continuously regulated hormone by hand means dozens of decisions
a day, every day, with no days off, under an asymmetric penalty, against disturbances nobody can
measure. Numbers that look poor on a printout are usually not a failure of effort — the problem is
not solvable with the available actuator, in the strict sense set out above. Someone who has been
managing it for twenty years has been doing something genuinely difficult for twenty years.

A note about who is reading. Someone reading about insulin is more likely to be living with it
than revising it. If that is you: nothing here is about your regimen, there are deliberately no
doses or ratios anywhere on this page, and the only people who can change anything about it are
you together with your own clinical team. If hypoglycaemia is happening now, treat it the way your
own team has agreed with you, and if someone cannot be roused, call emergency services.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md).
Specific to this answer:

* Your national formulary — in the United Kingdom the British National Formulary, elsewhere the
  equivalent national formulary — for every insulin preparation's onset, profile, duration and
  warnings. It is the authority on anything quantitative about insulin.
* The summary of product characteristics, or equivalent approved product information, for the
  specific preparation concerned.
* Your national diabetes guideline's sections on insulin therapy in type 1 diabetes and on
  hypoglycaemia, from the body that issues it.
* Your local hospital's or trust's insulin safety policy and insulin prescription chart guidance.
* A diabetes or endocrinology textbook chapter on beta-cell secretory physiology, the incretin
  effect and first-pass hepatic extraction.
* The consensus statements of the Advanced Technologies and Treatments for Diabetes meetings, for
  how continuous-glucose metrics and automated delivery are currently assessed.

## Scope and safety

The Pokémon is here to make a control loop with a lag concrete, and it stops at mechanism: point 3
above drops the analogy entirely, because hypoglycaemia is not a battle outcome. This is not a
guide to giving insulin and not about any individual's care. **There are no doses, ratios,
correction factors or rates anywhere on this page, and that is deliberate** — every number here is
a quantity of HP in a video game, none of it converts to anything, and nothing should permit a
dose to be calculated. Insulin is a high-risk medicine; the formulary, the product information and
local insulin safety policy are the authorities. Nothing here has had clinical review. If someone
is unwell now, or hypoglycaemia is suspected and they cannot be roused, contact local emergency
services.

## What a Gym Leader digs into next

* Why does the berry have to be in the slot already, rather than fetched?
* What does using an item from the bag cost that a held item does not?
* Why is a fraction of maximum HP the right shape for a background correction and a flat amount
  the wrong one?

## Where this stands, October 2026

The control argument is mechanism and does not date. The cast does: the Sitrus Berry's flat 30 HP
became a quarter of maximum in Generation IV, weather durations changed, and held-item behaviour
has been revised more than once — check the current generation's data rather than a remembered
table. On the clinical side, sensor accuracy, algorithm behaviour and available preparations move
fastest of all; treat any figure you remember as out of date until the formulary confirms it.
