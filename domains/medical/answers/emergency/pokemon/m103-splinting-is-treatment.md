---
id: "m103"
slug: splinting-is-treatment
style: pokemon
category: emergency
difficulty: intermediate
question: "Why is immobilising a fracture treatment in its own right rather than packaging for transport?"
tags: [fractures, immobilisation, prevention, counterfactual, revision]
---

# Safeguard costs a turn and a move slot, prints nothing, and is the entire intervention

`Cmd_setsafeguard` in `src/battle_script_commands.c` is eighteen lines long and, on the turn it
runs, changes nothing you can see. It sets one bit in `gSideStatuses`, writes 5 into
`gSideTimers[side].safeguardTimer`, and prints a message. No damage, no stat change, no HP
movement, nothing on the health box. A player watching that turn and a player watching a wasted
turn are watching the same screen.

It is nevertheless one of the strongest things that side can do, and the reason is that the harm
it refuses is **per-turn and cumulative**, not a one-off. Question m102's table has the
arithmetic: once a status is written into `status1` it bills `maxHP / 8` every turn until
something specific clears it, and almost nothing clears it. Refusing the write once is worth more
than clearing it later, which is the argument question m069 makes about where in a pipeline a
refusal belongs.

## Four shields, and four different cut-offs

The engine has several of these, they are not interchangeable, and each one is written to cover
one route.

```
   the shield           what it refuses                      what still gets through
   ───────────────────────────────────────────────────────────────────────────────────────────────
   Safeguard, 5 turns,  move effect bytes 1 to 7: sleep,     a status arriving from an ABILITY:
   one side             poison, burn, freeze, paralysis,     Parasect's Effect Spore, Poison Point
                        Toxic, confusion — and only as a     on Qwilfish, Flame Body — the check
                        SECONDARY effect                     is skipped when
                                                             HITMARKER_STATUS_ABILITY_EFFECT is
                                                             set
   Shield Dust, on      the same bytes plus 8 and 9, flinch  all damage. It stops the extra and
   Dustox, Caterpie,    and Tri Attack, and only when the    never the hit
   Wurmple              effect is not the move's primary
                        purpose
   Mist, 5 turns, one   stat reductions only                 a reduction flagged "certain", and
   side                                                      Curse, exempted by name
   Clear Body, White    stat reductions, with no timer at    the same two exceptions, and anything
   Smoke                all: an Ability holds while its      that is not a stat reduction
                        holder is on the field
   Keen Eye             accuracy reductions only             every other stat
   Hyper Cutter         Attack reductions only               every other stat
   ───────────────────────────────────────────────────────────────────────────────────────────────
     NONE of them cures anything. Every one is a refusal at the point of entry,
     and each cut-off is written as a numeric range or a named exception in code.
```

The Safeguard clause is worth reading as written, because the three conditions are the whole
design: the side must hold the bit, the effect byte must be 7 or lower, and the effect must not be
primary — and the separate `HITMARKER_STATUS_ABILITY_EFFECT` test means a status arriving by
Ability is not covered at all. A shield against one route is not a shield. Question m009's
distinction between an Ability and a move is the reason the exemption exists.

## It is invisible exactly when it works

Search `data/battle_scripts_1.s` for `SIDE_STATUS_SAFEGUARD` and you find **ten** check sites, one
each in Sleep, Toxic, Poison, Paralyze, Confuse, Will-O-Wisp and Yawn, and one each in Swagger,
Flatter and Teeter Dance's confusion branches. Somebody wrote that line ten times. Nine of them
jump to the same four-instruction script:

```
BattleScript_SafeguardProtected::
	pause B_WAIT_TIME_SHORT
	printstring STRINGID_PKMNUSEDSAFEGUARD
	waitmessage B_WAIT_TIME_LONG
	end2
```

That message is the **only** evidence Safeguard ever produces, and it appears only when the other
side attempts something it blocks. On a turn where nothing is attempted, the bit is set, the timer
ticks down in `ENDTURN_SAFEGUARD`, and the screen is identical to a screen with no Safeguard on
it. The successful case has no visible content; it has a message about something that did not
happen, or it has nothing.

A player reviewing a Battle Video cannot distinguish a turn in which Safeguard prevented nothing
from a turn in which there was nothing to prevent. Question m036's Spikes have the same problem
from the other end.

## Timing: it goes up before, and it cannot be refreshed

Two mechanics, both exact.

**It must already be up.** The check sits at the point of infliction, so a Safeguard set on the
turn after Thunder Wave landed does nothing about the paralysis now sitting in `status1`. The ten
check sites are all in the attacker's script, evaluated when the status is about to be written.

**The attempt is wasted if it is already up.** `Cmd_setsafeguard` opens by testing the bit, and if
it is set it does this:

```
   gMoveResultFlags |= MOVE_RESULT_MISSED;
   gBattleCommunication[MULTISTRING_CHOOSER] = B_MSG_SIDE_STATUS_FAILED;
```

The timer is not refreshed and the turn is gone. `Cmd_setmist` does the same thing on `mistTimer`.
This is the mechanic questions m057 to m059 are built on: a setter that returns a failure when its
own effect is already running, and does not extend the clock. The window is five turns, it lapses
in `ENDTURN_SAFEGUARD` whether or not anything was blocked, and it cannot be topped up early — so
the thing to watch is the clock, not the bit.

## Specific, bounded, and not a cure

Three limits, each of which is the design rather than a defect.

* **It does not clear what is already there.** Safeguard is silent about an existing burn. The
  clearing instruments are different objects entirely: a single-purpose item, question m003's
  Antidote; `Refresh`, which fails outright when there is nothing to cure; `Heal Bell` and
  `Aromatherapy` across the party. **Haze** is the matching case on the stat side — it clears
  every stage and restores not one point of anything else, which is question m051's device.
* **It is silent about damage.** A Pokémon behind Safeguard takes exactly as much from Hyper
  Beam's 150 base power as it would have without it. The shield covers the status route and no
  other.
* **It is one bit in one variable, and the variable belongs to the side.** It does not travel with
  the Pokémon that set it; `gSideTimers` is indexed by side, so switching out leaves it running
  for whoever comes in, and question m070's `SwitchInClearSetData` never touches it.

## Why the engine calls it a move

`EFFECT_SAFEGUARD` and `EFFECT_MIST` are two entries in the same jump table as `EFFECT_EXPLOSION`
and `EFFECT_HIT`, one `.4byte` each, in the same file, read by the same dispatcher. Safeguard
occupies one of four move slots — question m014's budget — costs PP like anything else, and takes
the whole turn. Lapras learns Mist at level 7 and Safeguard at 43; Articuno gets Mist at 13;
Shuckle gets Safeguard at 23; Ninetales has it from level 1.

Nowhere does the data model distinguish an act that does something from an act that prevents
something. There is no "preparation" category, no discount on the turn, and no second-class slot
for it. The engine's accounting treats a refusal as an action, because in the only currency it has
— turns, PP and slots — it costs exactly as much as one.

## Where the metaphor stops

Plain prose from here, with no game in it, because the subject is a person with a broken limb.

An unsupported fracture is not a fixed state. The bone ends move whenever the limb moves, and each
movement produces further soft-tissue injury, further bleeding from the fracture surfaces and torn
vessels, further traction on the vessels and nerves running alongside, and severe pain, which has
physiological consequences of its own. **(Mechanism.)** The injury therefore has a rate, and the
rate is largely a function of movement, so immobilisation is treatment of an ongoing process.
Restoring length and alignment also reduces the space available to bleed into, most clearly in the
large long-bone and pelvic injuries. **(Consensus;** the device used and whether realignment or
traction forms part of it are (**country-dependent**) and are not described here.**)** Of its four
effects — less soft-tissue damage, less blood loss, much less pain, and making movement possible
at all — only the last is transport.

Three further points, and none is a caveat. Prevention is measured in what did not happen, so a
splint applied early produces a course of events with no notable content and gets no credit, while
omission produces harms that appear later, elsewhere, and are attributed to the injury: the same
structural problem as pressure-area care and infection prevention. It has to be in place before
the movement it prevents, which is routinely lost when immobilisation is sequenced as the last
step of preparing to go. And a correctly applied device can become a source of harm as the limb
swells, so application is the start of a period of reassessment rather than the end of a task.
**(Consensus** that immobilisation reduces pain, that immobilised limbs are reassessed, and that a
splint can contribute to pressure injury and can mask or worsen a developing compartment problem;
intervals, findings recorded and escalation thresholds are **country-dependent.)**

No Pokémon stands for a patient anywhere in this answer, nothing in the game represents a person,
a limb, an injury or an outcome, and no part of it is a sequence of actions. The game is carrying
one idea: that an intervention whose entire effect is a refusal at the point of entry is still an
intervention, costs exactly what an action costs, and is invisible precisely when it has worked.
What is at stake when the limb belongs to a person — the pain, the handling, and the
organisational habit of filing immobilisation under logistics and doing it last — is stated here
without ornament, and it is not a mechanic.

## What a Gym Leader is listening for

* Safeguard changes nothing visible on the turn it is used. Why is it nevertheless worth a turn?
* Name the three conditions in the Safeguard clause, and the route that is not covered by any of
  them.
* Shield Dust stops effect bytes up to 9 and never stops damage. What does that tell you about
  what a shield is for?
* Somebody wrote the Safeguard check ten times. What does the number ten represent?
* What does `Cmd_setsafeguard` do when Safeguard is already up, and what is the general lesson
  about topping up a prevention?
* Which objects in the game clear a status, as opposed to refusing one?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md), and they
apply here. Specific to this answer:

* The current fracture and major trauma guidance issued by **the national body for clinical
  guidelines in the country the reader practises in**, for immobilisation, pain management and
  every threshold and interval.
* The current pre-hospital care guidance issued by **the reader's national ambulance service or
  pre-hospital care body**, for which devices are carried and how immobilisation is sequenced.
* A current standard textbook of **emergency medicine** or of **orthopaedic trauma**, for the
  local pathophysiology of fracture and for compartment syndrome.
* **The reader's own employing organisation's** trauma and limb-injury policy, which governs
  practice where they work and outranks every general account including this one.

No guideline number, document title or identifier is given, and nothing is quoted, because none of
these was opened. The Pokémon side is in the opposite position and is sourced file by file in the
closing note.

## Scope and safety

**If someone is unwell or injured right now, call your local emergency number.** This is not for
use during an emergency, and reading this instead of calling for help would be worse than doing
nothing at all.

This is revision material about *why an intervention counts as treatment*, written for someone
already trained, and the Pokémon framing covers the structure of a preventive intervention and
nothing else. It is deliberately not a protocol: no device, no technique, no sequence of actions,
no interval, no agent, no dose, and nothing to consult while treating anyone. Immobilisation
practice, available devices and standards for timing and reassessment differ between countries,
ambulance services and hospitals, and they are revised. The reader's own national guidance,
service guidance and local policy are the authority; this is not, and it has had no clinical
review. Nothing here describes any real person.

## Where this stands, October 2026

The Pokémon facts are pinned to source and are stable. `Cmd_setsafeguard`'s five-turn write, its
failure branch setting `MOVE_RESULT_MISSED` without refreshing the timer, `Cmd_setmist`'s
identical behaviour on `mistTimer`, the Safeguard clause in `Cmd_seteffectwithchance` with its
effect-byte cut-off of 7, its not-primary condition and its `HITMARKER_STATUS_ABILITY_EFFECT`
exemption, Shield Dust's cut-off of 9, Mist's exemptions for a certain reduction and for Curse,
and the Clear Body, White Smoke, Keen Eye and Hyper Cutter checks in the stat-change routine are
all read from `src/battle_script_commands.c`; the `ENDTURN_SAFEGUARD` and `ENDTURN_MIST` lapse
cases from `src/battle_util.c`; the ten Safeguard check sites, their owning scripts and the four
instructions of `BattleScript_SafeguardProtected` from `data/battle_scripts_1.s`; Hyper Beam's 150
base power from `src/data/battle_moves.h`; Dustox, Caterpie and Wurmple having Shield Dust,
Parasect having Effect Spore and Qwilfish having Poison Point from
`src/data/pokemon/species_info.h`; and Lapras learning Mist at 7 and Safeguard at 43, Articuno
Mist at 13, Shuckle Safeguard at 23 and Ninetales Safeguard at 1 from
`src/data/pokemon/level_up_learnsets.h`. Those are Generation III behaviours and later generations
change several of them, so a reader checking today's game should read today's game. On the
clinical side the argument is long-standing and the operational detail is not: devices carried,
whether traction is applied, reassessment intervals, the analgesic approach and the standards
against which timing is audited all differ between countries and services and move with each
revision. Principle dated October 2026; read the current guidance for anything past the principle.
