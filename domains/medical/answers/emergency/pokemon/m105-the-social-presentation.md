---
id: "m105"
slug: the-social-presentation
style: pokemon
category: emergency
difficulty: advanced
question: "Why is a presentation that looks social rather than medical still a clinical problem, and why is dismissing it a diagnostic error?"
tags: [function, attribution, environment, assessment, revision]
---

# Spikes are stored on the side, not on the Pokémon, and the message names the Pokémon anyway

`Cmd_trysetspikes` writes two things, and neither of them is on a Pokémon:

```
   gSideStatuses[targetSide] |= SIDE_STATUS_SPIKES;
   gSideTimers[targetSide].spikesAmount++;
```

`gSideStatuses` is indexed by **side**. `gSideTimers` is indexed by **side**. Nothing is written
into `gBattleMons`, nothing into `status1` or `status2`, and nothing anywhere that
`SwitchInClearSetData` will clear. A brand-new, completely untouched entrant loses HP the instant
it arrives, and the reason is a number held somewhere it has no access to.

Then the engine prints `STRINGID_PKMNHURTBYSPIKES`, which names the Pokémon.

## There is no indicator for it at all

`UpdateStatusIconInHealthbox` reads `MON_DATA_STATUS` and draws one of five graphics. There is no
graphic for a side status, no counter on screen for `spikesAmount`, and no way to read the field
except by remembering the message when it was set. So the only durable record of the cause is
`STRINGID_SPIKESSCATTERED`, printed once, several turns ago, possibly by somebody who has since
left the field — while the record of the *effect* is printed again, with a Pokémon's name attached
to it, on every single entry.

A player reviewing the log sees a sequence of entries about a series of Pokémon and nothing about
the ground they stepped onto. Question m037's distinction between what is documented as seen and
what is documented as confirmed is the same problem; this is the version where the thing that was
never documented is the cause.

## The damage is a product of two terms, and one of them is not about the entrant

```
   spikesDmg = (5 - gSideTimers[side].spikesAmount) * 2;
   gBattleMoveDamage = gBattleMons[battler].maxHP / spikesDmg;
```

Two inputs. The **layer count**, which belongs to the field and was set by someone else — one
layer gives maxHP/8, two gives maxHP/6, three gives maxHP/4, and `Cmd_trysetspikes` refuses a
fourth. And the **entrant's own maximum HP**, which converts that fraction into an absolute.

The same field costs a Blissey, base 255, and a Shuckle, base 20, the same fraction and nothing
like the same number — question m006's distinction again. And the two terms are not symmetrical in
what can be done about them: you can choose who enters, and you cannot change the layer count by
anything you do to the entrant. One term is in the Pokémon, one term is in the field, and only one
of them is modifiable from where you are standing.

## Whoever set it is not on the field

`Cmd_trysetspikes` writes to `BATTLE_OPPOSITE(GetBattlerSide(gBattlerAttacker))` — the *other*
side's slot in the array — and then that Pokémon's job is done. Skarmory learns Spikes at level
42, Cloyster at 33, Forretress at 49 and Qwilfish has it from level 1; any of them can set three
layers and leave. The damage then arrives entry after entry with **no agent present**, and nothing
on screen connects it to the Pokémon that caused it.

That is question m036's device in its original form: the hazard is on the ground, not on the
Pokémon, and whoever laid it has gone. Here it is doing a second job — the attribution problem.
The cause has no representation on screen and the effect has a name attached to it, so the obvious
reading of the log is the wrong one.

## Healing the entrant does not clear the field

A Full Restore brings the entrant back to full and leaves `spikesAmount` at 3. Switch out and back
in and the bill arrives again: `SIDE_STATUS_SPIKES_DAMAGED` is a per-entry guard, so the charge is
once per entry rather than once per battle, and the entries keep happening. Nothing about the
entrant's HP, its status, its stats or its item changes the field by one bit.

This is the whole structure in one sentence. Restoring the first term and sending the same Pokémon
back onto the same ground reproduces the result exactly, and the reproduction is arithmetic rather
than anybody's failure.

## Removal is third in a chain, and it costs somebody their whole turn

`Cmd_rapidspinfree` is the only thing in the game that clears Spikes, and question m102 reads it
for the same reason:

```
   if      (status2 & STATUS2_WRAPPED)          -> free from Wrap, and stop
   else if (gStatuses3 & STATUS3_LEECHSEED)     -> clear Leech Seed, and stop
   else if (gSideStatuses & SIDE_STATUS_SPIKES) -> clear ALL layers, and stop
```

Spikes are **third**, so a Pokémon that is also wrapped clears the wrap and leaves the field
exactly as it was. The clearing also has to be planned long before it is needed: Rapid Spin has to
be on a team member in advance — Starmie has it from level 1, Staryu learns it at 10, Forretress
at 22, Hitmontop at 25, Donphan at 41 — that member has to still be alive, has to come in, and has
to spend a turn on an action that does nothing to the opponent at all. Question m103's point about
prevention applies to removal too: the turn is spent and the screen shows almost nothing for it.

And when it works it clears all three layers at once, which is the most hopeful mechanic in this
answer: the field problem is not graded down one step at a time, it is either addressed or it is
not.

## Who the field hurts is a category, not an effort

One more mechanic, because it is the part people get backwards. `Cmd_weatherdamage` exempts from
sandstorm every battler whose first or second type is Rock, Steel or Ground, and anything with
Sand Veil; hail exempts Ice. The exemption list is **types and abilities** — question m028's
convention — properties of the entrant that were fixed before it arrived and that nothing it does
in the battle can alter. Tyranitar in its own sandstorm takes nothing; Jolteon takes maxHP/16
every turn for being an Electric-type in weather it did not set.

Nothing in that is about how hard anything is trying, and reading the damage as a property of the
battler rather than of the pairing is the error. Question m050 is built on the same observation
from the other side.

## Where the metaphor stops

Plain prose from here, with no game in it, because the subject is a person whose life has stopped
working.

Someone arrives and the presenting problem is not a symptom: the arrangement they were living
under has stopped working. The word usually attached is *social*, and it is doing two jobs. As a
statement about **where** the cause is, it can be accurate; as a statement about urgency, severity
or whether a disease is present, it is not a statement at all, and it is read as one constantly.
**(Definitional.)**

Function is a margin between two quantities: what a person can do, and what they are being asked
to do. A small decrement in the first — a new infection, a medicine's effect, pain, a night
without sleep — or a small increase in the second — a helper who is no longer available, a cold
house, a hospital stay that changed nothing at home — takes the margin below zero, and what
presents is the arrangement failing rather than the decrement itself. Because the margin may
always have been small, the size of the presenting event carries almost no information about the
size of the cause. **(Mechanism.)** Much of the modifiable risk sits in the second term, so
treating the first and returning someone to an unchanged second reproduces the presentation; that
is an arithmetic identity rather than anybody failing to cope. And the hazard is often
environmental and was set by something that has since gone: a deconditioning admission, a medicine
started elsewhere, a service withdrawn.

Dismissal is a diagnostic error of a specific shape — a label naming the location of a cause used
as though it named the absence of one, after which it suppresses the search that would test it.
Three things give that teeth: acute illness in older people frequently presents as a change in
function rather than as the classic features of the disease; a label applied before any history of
the change is applied before the evidence that would refute it; and "no medical cause found" is
unfalsifiable unless somebody recorded what was looked for, since an absent observation is not a
negative one. **(Consensus;** the proportion of such presentations with an identifiable acute
problem is a matter of published series and is not quantified here.**)** The recognised response
is a multidisciplinary assessment of both terms, because the two terms are assessed by different
professions and the second cannot be changed by a prescription — its name, composition and funding
are (**country-dependent**). Capacity, consent and the protection of adults at risk are
deliberately absent from this answer: they are matters of law that differ by jurisdiction and the
reader's own legislation is the only acceptable source.

No Pokémon stands for a patient anywhere in this answer, and that constraint shaped it. Nothing in
the game represents a person, a frailty, a home, a carer or an outcome; no entrant stands for
anybody arriving anywhere. The game is carrying two ideas and no others: that a cause can be
stored somewhere the thing taking the damage has no access to, while every record of the effect
carries that thing's name; and that an effect which is a product of two terms cannot be fixed by
addressing the term that happens to be in front of you. What is at stake when the arrangement
belongs to a person — being described as an administrative problem in their own hearing, the
account of the people nobody asked, and a carer's own exhaustion being a clinical fact about
somebody who is not the patient — is stated above without ornament, and it is not a mechanic.

## What a Gym Leader is listening for

* Which array are Spikes stored in, and what does that mean for switching?
* The damage has two inputs. Name them and say which one you can do anything about.
* Who set the layers, and where are they now? What does the log name instead?
* A Full Restore on the entrant: what exactly has changed about the field?
* Rapid Spin is third in `Cmd_rapidspinfree`. Give two ways the removal fails to happen even when
  the team has it.
* Sandstorm exempts Rock, Steel and Ground types and Sand Veil. What kind of fact is an exemption
  list?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md), and they
apply here. Specific to this answer:

* The current guidance on the care of older people with frailty in acute settings issued by **the
  national geriatric medicine society or college for the country the reader practises in**, for
  the structure of comprehensive assessment.
* The current standards for emergency department assessment issued by **the reader's national
  emergency medicine college**, which is where the expectations for this presentation sit.
* A current standard textbook of **geriatric medicine**, for the atypical presentation of acute
  illness and for the evidence on comprehensive assessment.
* **The reader's own employing organisation's** policy on assessment, discharge planning and
  referral to community services, which governs what is possible where they work.
* For anything touching capacity, consent or the protection of adults at risk: **the governing
  legislation and statutory guidance of the reader's own jurisdiction**, and nothing else.

No guideline number, document title or identifier is given, and nothing is quoted, because none of
these was opened. The Pokémon side is in the opposite position and is sourced file by file in the
closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *how a presentation is categorised and why the categorisation
misleads*, written for someone already trained, and the Pokémon framing covers only where a cause
is stored and how an effect is attributed. It is deliberately not a protocol: no assessment tool,
no score, no threshold, no pathway, and nothing to consult while assessing anyone. It contains no
account of capacity, consent, substitute decision-making or the protection of adults at risk,
because those are matters of law that differ by jurisdiction and the reader's own legislation and
statutory guidance are the only acceptable source. Services and team composition differ enormously
between countries and institutions. The reader's own national guidance and local policy are the
authority; this is not, and it has had no clinical review. Nothing here describes any real person.

## Where this stands, October 2026

The Pokémon facts are pinned to source and are stable. `Cmd_trysetspikes` writing to
`gSideStatuses` and `gSideTimers` on the opposite side and refusing a fourth layer, the damage
formula `maxHP / ((5 - layers) * 2)` giving maxHP/8, /6 and /4, the `SIDE_STATUS_SPIKES_DAMAGED`
per-entry guard, `Cmd_rapidspinfree`'s three-branch chain with Spikes third and all layers cleared
at once, and `Cmd_weatherdamage`'s exemptions for Rock, Steel and Ground types, Sand Veil and Ice
in hail are read from `src/battle_script_commands.c`; the side-status bit definitions from
`include/constants/battle.h`; the five status graphics and their single source in
`MON_DATA_STATUS` from `src/battle_interface.c`; `STRINGID_PKMNHURTBYSPIKES` and
`STRINGID_SPIKESSCATTERED` from `data/battle_scripts_1.s`; Blissey's base 255 and Shuckle's base
20 from `src/data/pokemon/species_info.h`; and Skarmory learning Spikes at 42, Cloyster at 33,
Forretress at 49, Qwilfish at 1, Starmie's Rapid Spin at 1, Staryu's at 10, Forretress's at 22,
Hitmontop's at 25 and Donphan's at 41 from `src/data/pokemon/level_up_learnsets.h`. Spikes
layering is a **third** generation feature — Generation II has one layer — and later generations
change the clearing rules, so a reader checking today's game should read today's game. On the
clinical side the argument is long-standing and the delivery is not: what comprehensive assessment
is called, who is in the team, whether it exists at the front door, and what community services
can be arranged differ sharply between countries and institutions and move with each
reorganisation; the law on capacity and on the protection of adults at risk differs by
jurisdiction and is not described here at all. Principle dated October 2026; read the current
guidance for anything past the principle.
