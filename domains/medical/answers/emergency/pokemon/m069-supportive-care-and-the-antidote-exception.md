---
id: "m069"
slug: supportive-care-and-the-antidote-exception
style: pokemon
category: emergency
difficulty: advanced
question: "Why is the management of most poisonings supportive rather than antidotal, and what has to be true before a specific antidote is worth reaching for?"
tags: [toxicology, supportive-care, antidotes, final-common-pathway, revision]
---

# Forty-one effect scripts end up in the same pipeline, and a special case is a four-line prologue

Emerald's `gBattleMoves` has 355 entries, one of which is the empty `MOVE_NONE`, and 198 distinct
values appear in the `.effect` field. That sounds like 198 pieces of machinery. It is not. Open
`data/battle_scripts_1.s` and count the jumps into `BattleScript_EffectHit`: forty-one distinct
effect scripts reach it, by forty-five separate jumps, and what they all run once they arrive is
one sequence.

```
   BattleScript_EffectHit ── the shared pipeline, in order
   ─────────────────────────────────────────────────────────────────────
     attackcanceler              ◄── BattleScript_HitFromAtkCanceler
     accuracycheck               ◄── BattleScript_HitFromAccCheck
     attackstring
     ppreduce                    ◄── BattleScript_HitFromAtkString
     critcalc                    ◄── BattleScript_HitFromCritCalc
     damagecalc
     typecalc
     adjustnormaldamage
     attackanimation             ◄── BattleScript_HitFromAtkAnimation
     waitanimation / effectivenesssound / hitanimation
     healthbarupdate
     datahpupdate
     critmessage / resultmessage
     seteffectwithchance
     tryfaintmon
     moveend
   ─────────────────────────────────────────────────────────────────────
   five labelled entry points.  A special case does its own few lines and
   then re-enters the common path at whichever label is correct for it.
```

Those five labels are the detail that makes this the right analogy rather than a loose one. A move
with something particular to do does not get its own pipeline. It gets a short prologue and then
joins the shared one at the right point — `BattleScript_EffectTwister` is three instructions and a
`goto`; `BattleScript_EffectGust` is three and a `goto`; the Surf special case is four lines at
the very head of `EffectHit` itself. The common path is where the work happens. The specific
branch is small, cheap and bolted on the front.

## What a specific counter costs: exactly one bit

Now the other half, and it is the sharper half. Open `src/data/pokemon/item_effects.h` and read
what a single-purpose item actually contains.

```
   one bit, one flag                                        the flag it is aimed at
   ──────────────────────────────────────────────────────────────────────────────────
   gItemEffect_Antidote[6]    = { [3] = ITEM3_POISON };     poison, and nothing else
   gItemEffect_BurnHeal[6]    = { [3] = ITEM3_BURN };       burn
   gItemEffect_IceHeal[6]     = { [3] = ITEM3_FREEZE };     freeze
   gItemEffect_ParalyzeHeal[6]= { [3] = ITEM3_PARALYSIS };  paralysis
   gItemEffect_Awakening[6]   = { [3] = ITEM3_SLEEP };      sleep
   gItemEffect_CheriBerry[6]  = { [3] = ITEM3_PARALYSIS };  paralysis
   gItemEffect_ChestoBerry[6] = { [3] = ITEM3_SLEEP };      sleep
   gItemEffect_PechaBerry[6]  = { [3] = ITEM3_POISON };     poison
   gItemEffect_RawstBerry[6]  = { [3] = ITEM3_BURN };       burn
   gItemEffect_AspearBerry[6] = { [3] = ITEM3_FREEZE };     freeze
   gItemEffect_PersimBerry[6] = { [3] = ITEM3_CONFUSION };  confusion
   ──────────────────────────────────────────────────────────────────────────────────
   the whole mask                                           everything in the table
   gItemEffect_FullHeal[6]    = { [3] = ITEM3_STATUS_ALL };
   gItemEffect_LumBerry[6]    = { [3] = ITEM3_STATUS_ALL };
```

A single-purpose item is six bytes with **one bit** set, at index 3, and that bit is matched
against one flag. The general-purpose items carry the whole mask. And the game prices this
honestly, from `src/data/items.h`: Antidote 100, Parlyz Heal 200, Burn Heal 250, Ice Heal 250,
Awakening 250, **Full Heal 600**, **Full Restore 3000**. The broad entry is the expensive one. You
pay, in the game's own currency, for not having to be right about which bit it is.

And one entry sits between the two, which is the most useful row in the table. **Refresh** is not
an item but a move, 20 PP, and `Cmd_cureifburnedparalyzedorpoisoned` — the command its script runs
— tests `STATUS1_POISON | STATUS1_BURN | STATUS1_PARALYSIS | STATUS1_TOXIC_POISON` and nothing
else. Three of the five, by name, written into one opcode. A **partial** mask is what most real
interventions look like: broader than one bit, narrower than everything, and you still have to
know which side of its boundary you are on. **Heal Bell** and **Aromatherapy**, 5 PP each, are
broader again and act across a whole party rather than one slot.

That price is the whole argument. A one-bit answer requires a one-bit question to have been
answered correctly first, and if it has not, the bit lands on nothing and the turn is gone. The
mask requires no such answer. And the engine reports the failure plainly: `PokemonUseItemEffects`
in `src/pokemon.c` opens with `bool8 retVal = TRUE` and only sets it `FALSE` where a bit matched
something and the corresponding `HealStatusConditions` call did work. A bit aimed at a flag that
is not set changes nothing and the function says so.

## Refusing the flag beats clearing it, and the engine says so by where it puts the check

The cheapest entries in the whole system are not in the item table at all. They are abilities, and
what they do is refuse the flag rather than clear it afterwards. **Immunity** on **Snorlax**
refuses poison. **Limber** on **Persian** refuses paralysis. **Water Veil** on **Wailord** refuses
burn. **Insomnia** on **Hypno** and **Vital Spirit** on **Primeape** refuse sleep. **Magma Armor**
on **Magcargo** refuses freeze. **Own Tempo** on **Spinda** refuses confusion. **Oblivious** on
**Slowpoke** refuses infatuation. **Shield Dust** on **Dustox** refuses the secondary effect
outright. Every one of these is a check inside `SetMoveEffect` that fires *before* the flag is
written, and none of them costs a turn or an item.

Two more sit between prevention and cure. **Safeguard**, 25 PP, blocks the flag being set across a
whole side for a limited number of turns — a declared barrier rather than a property of an
individual. And **Natural Cure**, which **Blissey**, **Starmie** and **Roselia** carry, is the
strangest and most instructive: `Cmd_switchoutabilities` has exactly one case in its entire switch
statement, and that case sets `status1 = 0` when the holder leaves the field. The condition is not
treated; the Pokémon simply stops being where the condition applies, and the flag goes with it.

None of that makes the item table redundant. It makes the point that the ordering of the options
is not cure-first: refusing the flag, then removing the thing from the situation, then a broad
mask, then a single bit, in roughly that order of robustness and roughly the reverse order of
specificity.

## The specific branch has to be in the right place, not just present

The five entry labels in the pipeline are not decoration — they encode *where* a special case
legitimately differs. Consider what each one means for a branch that joins there.

* **Joining at `HitFromAtkCanceler`** means the prologue ran before anything else was checked. The
  Surf special case sits there, because the state it reads — whether the target is mid-Dive — has
  to be read before accuracy is evaluated.
* **Joining at `HitFromAccCheck`** skips the cancel step because the caller already did it.
  `BattleScript_EffectEarthquake` works this way: it runs `attackcanceler`, `attackstring` and
  `ppreduce` itself, once, and then loops per target into the damage part only.
* **Joining at `HitFromCritCalc`** skips the strings and the PP, which is what a multi-hit or a
  repeated-target case needs so it does not charge PP five times or print the message five times.

A branch inserted at the wrong label either repeats work that was already done or skips work that
was not. The shared pipeline is doing the vast majority of the work in every case; the skill is
entirely in knowing where a particular special case correctly attaches.

## What the generic path can and cannot do

* **It does not need to know which move it is.** Every command in the list operates on
  `gCurrentMove` and the battlers' current state. The pipeline is correct for a move it has never
  seen, which is why a hundred moves added later needed no new pipeline.
* **It handles the thing that actually ends battles.** `datahpupdate`, `tryfaintmon` and `moveend`
  — the structural consequences — are in the shared path, not in any branch. The branches handle
  flavour; the common path handles what matters.
* **It cannot express a mechanism it has no command for.** That is the real limit, and it is why
  bespoke commands exist at all: `trysetfutureattack`, `trysetroots`, `tryimprison`,
  `trysetmagiccoat`. Each is a hand-written opcode added because the pipeline had no way to say
  that thing, and each one is a small, specific, separately maintained piece of machinery —
  precisely the cost structure of a specific intervention.
* **And a bespoke command can fail on its own terms.** `Cmd_trysetfutureattack` opens by checking
  whether a future attack is already pending on that target and jumps to
  `BattleScript_ButItFailed` if it is. The specific branch has preconditions the generic path does
  not have, which is the general rule rather than a quirk.

## The engine never remembers which script to run; it looks it up every time

One more structural point, and it is the one that matters most in practice. The engine does not
decide what to do by recognising the move. At `src/battle_script_commands.c` the line is
`gBattlescriptCurrInstr = gBattleScriptsForMoveEffects[gBattleMoves[gCurrentMove].effect];` — a
jump through a table of 214 entries, indexed by the move's `.effect` byte, consulted fresh on
every single use.

Nothing is cached. There is no shortcut for a move the engine has already seen this battle. The
cost of the lookup is one indirection and the benefit is that the engine is never wrong about a
move it has never met, including the hundred-odd that were added after the table was written. A
system that handles a very large catalogue of rare cases correctly does it by looking each one up,
not by knowing them — and the design decision that makes that affordable is keeping the number of
*scripts* small while the number of *entries* stays large.

## Where the metaphor stops

Plain prose from here, with no game in it, because this is a subject where the metaphor would be
in the way.

Almost everything a poison does to a person that could kill them, it does through a small number
of final common pathways: loss of the airway, failure of ventilation, failure of the circulation,
seizure, a disturbance of cardiac rhythm or conduction, a derangement of temperature, and a
derangement of the internal chemical environment. There are a very large number of agents and very
few ways out. Supporting those pathways is therefore **agent-independent** — it does not require
knowing what was taken, which matters because in a large share of real presentations the agent,
the amount and the timing are uncertain or unknown — and it buys the time in which the body's own
elimination reduces the exposure. Supportive care is the treatment in the great majority of cases,
not the fallback, and *waiting while supporting* is an active, skilled, demanding thing to do
rather than an absence of intervention. That is **mechanism**, checkable by reasoning.

A specific antidote has to clear four conditions at once, and most agents fail at least one: a
mechanism specific enough to interfere with; a window of benefit that overlaps when people
actually present; enough diagnostic confidence, because a specific agent aimed at the wrong
mechanism consumes time and belief and sometimes carries its own harm; and availability in the
building when it is needed. The absence of an antidote is usually a fact about the agent rather
than a gap in the pharmacopoeia. **(Consensus** for the general shape; **country-dependent** for
which antidotes are considered worthwhile, which are stocked and where, and for everything about
decontamination, whose role has narrowed and differs between national bodies.**)** Most countries
run a poisons information service with a clinician line and a maintained database, and consulting
it is the standard of care rather than an admission of ignorance.

A substantial share of poisoning presentations involve self-harm, intentional overdose, or an
exposure in the context of a mental-health crisis. None of that is in the analogy above and none
of it would be improved by being put there. The assessment of risk to a person, capacity,
safeguarding and the involvement of mental-health services run alongside the physiology and matter
at least as much; they are specialist domains with their own guidance and their own legal
framework in every country. Anyone having thoughts of harming themselves needs their local crisis
service, their own clinician or the local emergency number now, rather than a revision page.
Children arriving after an exploratory exposure and older people arriving after an error with
regular medicines are both common and both accidental, and neither is served by a framing built
around intentional overdose.

No Pokémon stands for a patient anywhere in this answer. Nothing in the game represents a person,
a poisoning, a treatment given to anyone, or any outcome; the items above are discussed as entries
in a lookup table and as bits in a mask, which is what they are in the code. The Revive and Max
Revive entries sit in that same table and are deliberately not used here or anywhere in this
directory, because nothing in Pokémon may stand in for resuscitating a person. The game is
carrying two ideas only: that a shared pipeline does most of the work in almost every case, and
that a one-bit answer requires a one-bit question to have been answered correctly first.

## What a Gym Leader is listening for

* Forty-one effect scripts jump into one pipeline. What does that tell you about where the work
  is, and what does it tell you about where the skill is?
* Why does `BattleScript_EffectHit` have five labelled entry points rather than one?
* `gItemEffect_Antidote` is six bytes with one bit set. What has to be true before that bit is
  worth spending a turn on?
* Full Heal costs 600 and Antidote costs 100. What is the extra 500 buying?
* Refresh's opcode names three status bits out of five. Why is a partial mask the realistic case?
* The engine indexes a 214-entry table on every use rather than remembering. What is that buying,
  and what is it costing?
* Why are Immunity, Limber and Water Veil cheaper than anything in the item table, and what is
  Natural Cure doing that is different again?
* `Cmd_trysetfutureattack` can fail on a precondition the shared pipeline does not have. What is
  the general principle?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../for-agents/SOURCES-emergency.md`](../../for-agents/SOURCES-emergency.md), and they apply
here. Specific to this answer:

* **The poisons information service for the country the reader practises in**, including its
  clinical database and its telephone service. This is the authority for anything agent-specific
  and no general account including this one substitutes for it.
* **The reader's national formulary**, for anything about an antidote as a medicine.
* The current guidance on acute poisoning issued by **the reader's own national body for clinical
  guidelines**, for decontamination, risk assessment and common presentations.
* The current guidance on the assessment and care of people presenting after self-harm, issued by
  **the reader's own national body for clinical guidelines**, which governs the half of this
  subject the analogy deliberately does not touch.
* **The reader's own employing organisation's** antidote stock list and poisoning policy.

No guideline number, document title or identifier is given, and nothing is quoted, because none of
these was opened. The Pokémon side is in the opposite position and is sourced file by file in the
closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all. **If anyone may have been poisoned, the local emergency number and the local poisons
information service are the route, immediately.** Anyone having thoughts of harming themselves
needs their local crisis service, their own clinician or the local emergency number now, rather
than this page.

This is revision material about *why a field is organised the way it is*, written for someone
already trained, and the Pokémon framing covers two ideas only: a shared pipeline, and the cost of
a one-bit answer. It is deliberately not a protocol and not a decision aid — it names no agent, no
antidote, no dose, no threshold, no decontamination indication and no sequence of actions, and it
is not something to consult while acting. Agent-specific management, antidote stocking and
decontamination guidance differ by country and institution and are revised. The reader's poisons
information service, national guidance and local policy are the authority; this is not, and it has
had no clinical review. Nothing here describes any real person.

## Where this stands, October 2026

The Pokémon facts are pinned to source and are stable. The 355 entries in `gBattleMoves` and the
198 distinct `.effect` values are counted from `src/data/battle_moves.h`; the shared pipeline, its
five labelled entry points, the forty-one scripts and forty-five jumps that reach it, the Surf
special case at its head and the Earthquake and Twister prologues are read from
`data/battle_scripts_1.s`; the one-bit item effect arrays and the `ITEM3_STATUS_ALL` masks are
`src/data/pokemon/item_effects.h`; the prices of 100, 200, 250, 600 and 3000 are from
`src/data/items.h`. Refresh's three-bit test is `Cmd_cureifburnedparalyzedorpoisoned`, Natural
Cure's single case is `Cmd_switchoutabilities`, the status-refusing abilities are checked in
`SetMoveEffect`, and `Cmd_trysetfutureattack`'s precondition check is in the same file — all
`src/battle_script_commands.c`. The ability holders named above are from
`src/data/pokemon/species_info.h`, the PP values from `src/data/battle_moves.h`, the 214-entry
`gBattleScriptsForMoveEffects` table from `data/battle_scripts_1.s`, and the `retVal` convention
in `PokemonUseItemEffects` from `src/pokemon.c`. Those are Generation III figures — the move
count, the effect table, the item list and the prices have all changed in later games — so a
reader checking today's values should read today's game. On the clinical side the structural
argument is long-standing and every specific is not: which antidotes are worthwhile, what is
stocked and where, and the role of decontamination all differ by country and have been revised
repeatedly. Principle dated October 2026; use the poisons information service and local policy for
anything past the principle.
