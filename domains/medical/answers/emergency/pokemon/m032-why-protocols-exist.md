---
id: "m032"
slug: why-protocols-exist
style: pokemon
category: emergency
difficulty: intermediate
question: "Why are time-critical decisions written down as protocols instead of left to individual clinical judgement?"
tags: [protocols, cognitive-load, variance, standardisation, human-factors]
---

# Red and Blue decided turn order with two if-statements. Emerald wrote it in a table.

In Red and Blue there is no priority system. `engine/battle/core.asm` asks, by name, whether the
selected move is **Quick Attack**; if it is and the other side's is not, that side moves first.
Then it asks, by name, whether the move is **Counter**; if it is and the other side's is not, that
side moves *last*. Then it falls through to comparing Speed, and on an exact tie it calls
`BattleRandom` and flips a coin. Two hand-written special cases in the middle of the battle loop,
and the ordering of every other move in the game is an accident of what the code happened to do
next.

By Emerald every entry in `gBattleMoves` carries a declared `.priority`, and `GetWhoStrikesFirst`
reads that field instead of asking about any move by name. That is the whole move from
case-by-case judgement in the moment to a written-down rule consulted the same way every time, and
it was made for the same three reasons a protocol gets written. The decision is **time-critical**
— it has to resolve inside the turn, with no opportunity to work it out. It is **high-stakes** —
getting the order wrong loses the battle, and the battle does not rewind. And the awkward cases
are **low-frequency** — nobody playing Red encountered a Quick Attack against a Counter often
enough to build a reliable sense of what should happen.

## The three things the table buys

**The sequence stops having to be held anywhere.** Red's rule lives inside the loop that executes
the turn, so understanding the ordering means reading the loop. Emerald's lives on the move. A
player can learn that **Whirlwind** is -6 without knowing anything about how a turn executes, and
the game can add **Trick Room** at the bottom of the table later without anyone relearning the
machinery. Reading beats recalling, and it frees attention for the thing the table cannot do,
which is noticing that the matchup is not the one the plan was built for.

**It compresses the spread.** This is the strongest argument, and it is the one standardised
formats are built around. Both games quietly cheat for the player, and both stop the moment the
result has to mean something to somebody else. In Red and Blue `ApplyBadgeStatBoosts` multiplies a
stat by 1.125 for each of four badges — the **Boulder Badge** raises Attack, the **Thunder Badge**
raises Defence, the **Soul Badge** raises Speed and the **Volcano Badge** raises Special — so a
player holding Brock's, Lt. Surge's, Koga's and Blaine's badges is running numbers that nobody
else's save file agrees with. The very first instruction in that routine is a check for a link
battle, and it returns without doing anything. Emerald does the same thing with the **Dynamo
Badge**, Wattson's, the third in Hoenn: a 10% Speed boost inside `GetWhoStrikesFirst`, suppressed
in link battles, recorded link battles and **Battle Frontier** battles alike. It is not that the
badges are unfair. It is that a result you cannot reproduce in someone else's save file is not a
result.

```
   the same matchup, many players running it
   ────────────────────────────────────────────────────────────────────────────────

   Red and Blue, no table       ░░▒▒▓▓███▓▓▒▒░░░░░░░░░░░░░░░        wide
                               └── a few players knew the loop's quirks cold,
                                   and everyone else was guessing ───┘

   Flat Rules, declared table   ░░░░▒▓████▓▒░░░░                    narrow
                                    └─ the clever edge cases are gone,
                                       and so is every disaster

   ────────────────────────────────────────────────────────────────────────────────
   the trade: give up the best case to delete most of the worst case
```

The **Battle Frontier** pushes this much further than a badge boost, and its seven facilities are
a scale of how much judgement a written ruleset can take away. Frontier singles fix the party at
three rather than six. **Flat Rules** level every Pokémon to a common cap. A **Species Clause**
forbids duplicates and an **Item Clause** forbids two of the same **Held Item**. The **Battle
Factory** goes further still and hands over rental Pokémon, so the team is not the player's choice
either. And the **Battle Palace** goes furthest of all: in `PlayerHandleChooseMove`, a Palace
battle never calls the routine that draws the four move names, the PP and the move type. The menu
is not shown. The player is not asked. `ChooseMoveAndTargetInBattlePalace` picks instead, and the
player watches. Seven facilities, seven **Frontier Brain** rulesets, each removing a different
degree of freedom — and not one of them makes any individual player better. They make the
*distribution* narrower, which is a different and more valuable thing.

**It is a shared schema, so strangers can play each other.** Two players who have never met can
battle because both know the same declared table. That is the only reason a link battle works at
all. A table that everyone knows but which two cartridges implement differently loses almost all
of this — which is why the same ruleset has to be worded identically on both sides of the cable.

## The four things it gives up

* **The table is wrong at the edges by construction.** It is fitted to the cases the designers
  thought about. **Prankster** had to be added later to lift an entire class of move up a bracket,
  which is an admission that the per-move numbers had not captured something real.
* **Following the table perfectly is not the same as reading the battle.** The characteristic
  failure is not misapplying a bracket. It is applying the correct bracket fluently in a matchup
  where Type Effectiveness had already decided the outcome two turns ago.
* **Resolving every action is not winning.** Reaching the bottom of the bracket list ends the turn
  and settles nothing.
* **A bad entry is bad everywhere at once.** One player misjudging a turn costs that player a
  battle. A wrong number in `gBattleMoves` is wrong in every copy of the game, in every battle,
  until a later generation revises it. Taking the variance out means the error that is left is no
  longer random, so it does not cancel out across players.

## Why the written form, specifically

```
   Red and Blue, in the loop            Emerald, in the table
   ──────────────────────────────────────────────────────────────────────
   drifts silently between versions     drifts visibly, in revisions
   cannot be checked against            can be read off and checked
   cannot be taught twice the same      can
   a new move needs the loop edited     a new move needs one number
   an unnamed move falls through        every move has a declared answer
     to the default, silently
   ──────────────────────────────────────────────────────────────────────
```

The last row is the one that matters. Red's two checks have no opinion about any move they do not
name, so an unanticipated case quietly becomes a Speed comparison and nobody is told. Emerald has
an opinion about all of them, and when the opinion is wrong it is wrong in public, in a table
someone can point at.

And the variance that is genuinely irreducible stays. On an exact Speed tie, in the same bracket,
both games call a random number and flip a coin. No table removes that. A protocol narrows the
spread; it does not promise a single answer where the situation does not contain one.

## Where the game stops

Plainly, without the metaphor, because this part is not a mechanic.

The reason time-critical clinical decisions are written down is that human working memory is small
and gets smaller under fear, noise, exhaustion and time pressure, and that a rare high-stakes
decision is exactly where an individual's judgement is least calibrated, because nobody sees
enough of them. A written protocol usually encodes more pooled experience than the person
following it has. That is **mechanism**: an argument about distributions and about how people
think when frightened, checkable by reasoning. It is also the reason the honest ground for
deviating is *this is not the situation the document was written for*, and never *I have done a
lot of these*. No Pokémon stands for a patient anywhere in this answer, and the game is carrying
one idea only: that a declared rule beats a judgement made fresh each time, when the time is short
and the spread is wide.

## What a Gym Leader is listening for

* The Battle Palace never draws the move menu. Which of the three reasons for writing a protocol
  down does that illustrate, and which one does it abandon?
* What exactly did Red and Blue do instead of a priority table, and what happened to every move
  the two checks did not name?
* Why does a standardised format switch the Dynamo Badge boost off, when the badge is available to
  every player?
* Which is the narrower claim — that the table makes any one player better, or that it makes the
  spread of outcomes tighter? Why does the second one matter more?
* What does the Speed-tie coin flip say about the limits of writing a rule down?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* The current life support guidelines issued by **the national resuscitation council for the
  country the reader practises in**, which are the clearest worked example of a protocol with all
  three conditions present. The councils differ from one another and each revises on its own
  cycle.
* The current consensus on science with treatment recommendations issued by **the International
  Liaison Committee on Resuscitation**, which is the evidence synthesis the national councils
  write from, and where a protocol is argued for rather than simply asserted.
* **The reader's own employing organisation's** clinical policy and standard operating procedures,
  which actually bind practice and outrank every general account including this one.
* The human-factors and crew-resource-management material taught on **the reader's own
  institution's** mandatory training, where the cognitive-load argument is set out against that
  institution's own protocols.

Nothing is quoted from any of these, and no guideline number, document title or identifier is
given, because none was opened. The Pokémon side is in the opposite position and is sourced file
by file in the closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *why protocols are built the way they are*, written for someone
already trained, and the Pokémon framing covers the shape of the rule and nothing else. It is
deliberately not a protocol and contains none: no sequence of actions, no rates, no depths, no
ratios, no doses, no settings, and nothing to consult while acting. Resuscitation guidance
**differs between national councils and is revised on a cycle**. The reader's own council and
local policy are the authority; this is not, and it has had no clinical review. Nothing here
describes any real person, case or institution.

## Where this stands, October 2026

The Pokémon facts are pinned to source: Red and Blue's two special cases and the 50/50 tie are
from `engine/battle/core.asm` in the Red decompilation, and the four badge boosts, the 1.125
multiplier and the link-battle early return are from `ApplyBadgeStatBoosts` in that same file,
whose own comment names which badge raises which stat. The declared `.priority` field is from
`src/data/battle_moves.h`; the Dynamo Badge boost, its suppression in link, recorded-link and
Frontier battles, and the tie coin flip are from `GetWhoStrikesFirst` in `src/battle_main.c`; and
the Battle Palace never drawing the move menu is from `PlayerHandleChooseMove` in
`src/battle_controller_player.c` — all three in the Emerald decompilation. The party-size and
move-slot limits are from the same project's `include/constants/global.h`. Prankster and Trick
Room are from working knowledge of later generations, not read from either project. The Palace is
described only as far as the code path goes — the menu is not drawn and the player is not asked —
and deliberately says nothing about *how* the game then chooses, because that table was not read.
On the clinical side the reasoning is **mechanism** and stable; everything specific is
**council-dependent** and moves on cycles that the councils do not synchronise with one another,
so two readers in different countries can both be right and disagree. Dated October 2026.
