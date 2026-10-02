---
id: "m034"
slug: compensation-and-the-sick-patient
style: pokemon
category: emergency
difficulty: advanced
question: "Why is a patient holding normal observations by compensating closer to collapse than one with abnormal but stable numbers?"
tags: [compensation, deterioration, observations, early-warning, physiology]
---

# PP is the budget. The bar is not showing it, and the bar is all the game shows you.

**What is borrowed here is the observer's problem, not the thing observed.** Nothing in this
answer stands for a person — not a species, not a stat, not a bar. Pokémon is lent for one
structural fact about reading a system through a display: the display reports a value that
something is working to defend, and it does not report what the defending costs. The part of this
subject that is about people is in plain prose further down.

Start with what a battle screen genuinely withholds. The opposing side's HP is drawn as a **bar**
and never as a number, so even a full bar is a range. Its remaining **PP** is not shown at all.
Its **Held Item** is not shown until it does something. Its EVs and IVs are not shown ever. And
the counters running on the field are not shown as numbers anywhere: `Cmd_setreflect` writes
`reflectTimer = 5` and the Light Screen command writes `lightscreenTimer = 5`, and the five-turn
weather counter is set the same way — but the screen on turn one of **Rain Dance** and the screen
on turn five of Rain Dance are identical. A player reading the display is reading defended outputs
over hidden budgets, every single turn.

## The shape of the failure

```
   PP remaining on the     ████████████████▓▓▓▓▓▒▒▒░░
   move that matters       └──── spent steadily, and never displayed ────┘  └ empty

   what the screen shows   ────────────────────────────────────────╮
   (the bar)                                                       ╰──────────▼
                           looks the same … the same … the same … and then Struggle

   the cost of holding on  ▁▁▁▂▂▂▃▃▃▄▄▄▅▅▅▆▆▆▇▇▇█████
                           └── rising the whole time, and not on the screen either

   turn ──────────────────────────────────────────────────────────────────────►
                                                              ▲
                                                 nothing happened here. A budget
                                                 emptied, which is a different thing.
```

**Struggle** is the exact moment a budget empties, and the games model it honestly. In Emerald's
`GetWhoStrikesFirst` and again in the move-selection checks, the engine substitutes
`MOVE_STRUGGLE` whenever `noValidMoves` is set — the Pokémon does not stop acting, it acts outside
the normal rules. `Cmd_typecalc` returns immediately for Struggle, so Type Effectiveness does not
apply to it at all, and the user pays for the hit out of its own health. Still acting, now at a
cost to itself, and the bar gave no warning because the bar was never measuring the thing that ran
out.

Two asymmetries follow, and both are visible at the table.

* **The bar is a lagging indicator of trouble and a leading indicator of the end.** It is the last
  thing to move and the thing that moves just before everything resolves. A player watching only
  the bar learns at the latest possible moment.
* **The cheap signals move early and mean many things.** A **Protect** on a turn when nothing
  threatened, a switch for no visible reason, a worse move chosen than the obvious one: each is
  nearly nothing on its own, each has innocent explanations, and early-and-ambiguous is the only
  kind of early signal on offer.

## Where the information actually is

* **Effort, not value.** Two full bars are not the same position if one of them is full because
  **Leftovers** is paying for it every turn and the other is full because nothing has touched it.
  The display is identical. The state is not.
* **Something that reads the margin.** **Multiscale** only works at full health, so the turn it
  stops working is a reading of the margin rather than of the value. A **Sitrus Berry** eaten
  three turns ago leaves nothing on the screen saying so.
* **Conjunction.** Three weak oddities in one turn beat one dramatic one. This is the whole reason
  a good player tracks several cheap signals at once instead of waiting for the bar.
* **The derivative.** How far the bar moved *last* turn predicts the next turn better than where
  the bar is now. Two frames are a different instrument from one frame.
* **The display can be actively wrong, and only load reveals it.** **Zoroark**'s **Illusion**
  shows a different species entirely; **Mimikyu**'s **Disguise** absorbs one hit and only then
  shows the true form. Neither is defeated by looking harder at the screen. Both are revealed by
  loading the system — which is the sharpest statement available of why a defended reading stays
  normal right up until it cannot.
* **The invisible roll.** **Quick Claw** fires one turn in five, by the parameter in Emerald's
  item table, and nothing announces that it is held. It is learnable only across many turns, never
  from one.

## Three traps

* **The restored bar.** A **Hyper Potion** refills the bar and tells you nothing about the PP, the
  item that was already eaten, or the field counter running down. The value recovered; the budget
  did not. **Leppa Berry** restores exactly 10 PP in Emerald's item table — a reminder that the
  budget and the bar are topped up by completely different things, and that fixing one is not
  evidence about the other.
* **The deep reserve.** **Blissey** at base HP 255 holds a full-looking bar through far more than
  anything else does, which makes its bar the least informative bar on the field. The bigger the
  reserve, the longer the flat part, and the less a reassuring display is worth.
* **The signal that cannot be generated.** **Substitute** does not show up as its own bar, so a
  side standing behind one does not produce the readings a player is watching for at all, and the
  absence of them is not good news. **Focus Sash** is silent in the same way once it has been
  consumed: the slot is simply empty now, and no part of the screen reports an empty slot.

## Where the metaphor stops

Plain prose from here, with no metaphor at all, because this is the part that is about people.

A recorded observation is the output of a control loop that is actively holding that output in
range, and holding it costs something. A person maintaining normal values by working hard has
already spent reserve to buy those values, so the margin left is smaller than it was. A person
sitting with abnormal values that are not moving has reached a position the loop can hold without
further expenditure. The first has a worse number hidden behind a better one. The second has a
worse number on display and a budget intact. That is **mechanism** — control theory applied to
physiology, and checkable by reasoning rather than by citation.

What that makes readable is the cost rather than the value: the work being done to hold a number
rather than the number; gradients between a defended centre and a periphery supply has been
withdrawn from; the conjunction of several variables each slightly displaced, which is exactly
what aggregated early warning scores exist to make visible; the trend across repeated observations
rather than any single set; and change in alertness or in how a person interacts, which is often
the earliest thing of all. The documented fact that an experienced clinician is worried performs
comparatively well, and its weakness is only that it does not survive a handover unless it is
written down.

Three consequences are worth holding on to, and none of them is a mechanic. A value that
normalises after an intervention is ambiguous between the problem being resolved and the reserve
being spent again. Greater physiological reserve means a longer flat phase and a steeper collapse,
so normal numbers are least reliable as reassurance in the people whose deterioration is most
abrupt. And where the compensatory response is limited — by age, by comorbidity, or by medicines
acting on the effectors — the expected change never appears, and its absence is not reassurance,
because a signal that could not be generated is not a signal that was sought and not found.

## What a Gym Leader is listening for

* What does the battle screen show about the other side, and what does it withhold?
* What is Struggle, mechanically, and why is it the right illustration of a budget emptying rather
  than of a bar emptying?
* Why is a full bar maintained by Leftovers a different position from an untouched full bar?
* Why do Illusion and Disguise need load rather than attention to break them?
* Why is Blissey's bar the least informative bar on the field?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* **The reader's own employing organisation's** observation, escalation and deteriorating-patient
  policy, which names the early warning score actually in use there, its thresholds and its
  escalation routes. That is the governing document, and it is the one this answer deliberately
  does not reproduce.
* The national guidance on recognising and responding to acute deterioration issued by **the
  relevant national health-service body or clinical-standards agency for the country the reader
  practises in**. These differ by country, and so do the scores they endorse.
* The current life support guidelines issued by **the national resuscitation council for the
  country the reader practises in**, for the point at which recognition becomes resuscitation. The
  councils differ from one another and each revises on its own cycle.
* A current physiology textbook of the reader's own choosing, for the control-loop account of
  cardiovascular and respiratory compensation, which is standard material rather than guidance.

No score is named, no thresholds, cut-offs, rates or values are given, nothing is quoted, and no
guideline number or document title is given, because none was opened. The Pokémon side is in the
opposite position and is sourced file by file in the closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *why compensation masks severity*, written for someone already
trained, and the Pokémon framing covers the observer's problem and nothing else — no Pokémon, stat
or bar here stands for a person. It is deliberately not a protocol and is not usable as one: it
names no early warning score, states no thresholds, cut-offs or normal ranges, and contains no
sequence of actions, rates, depths, ratios, doses or settings. Observation and escalation policies
**differ between institutions**, and resuscitation guidance **differs between national councils
and is revised on a cycle**. The reader's own organisational policy and national council are the
authority; this is not, and it has had no clinical review. Nothing here describes any real person,
case or institution.

## Where this stands, October 2026

The Pokémon facts pinned to source are: the five-turn screen and weather counters from
`Cmd_setreflect` and its neighbours in `src/battle_script_commands.c`; Struggle being substituted
when no valid move remains, from `src/battle_main.c`; Struggle bypassing the type calculation,
from `Cmd_typecalc` in `src/battle_script_commands.c`; Quick Claw's one-in-five parameter and
Leppa Berry's 10 PP from `src/data/items.h`; and Blissey's base HP of 255 from
`src/data/pokemon/species_info.h` — all in the Emerald decompilation. **Multiscale, Focus Sash,
Illusion and Disguise all postdate Emerald and were not read from either decompilation available
here**; they are stated from working knowledge of later generations. A reader who wants those
exact should check the generation they are playing. On the clinical side the control-loop account
and the three traps are mainstream **mechanism** and have not changed in a long time; every
specific — which score, what thresholds, how often, escalating to whom — is
**institution-dependent**, differs between organisations in the same city, and is revised. Dated
October 2026.
