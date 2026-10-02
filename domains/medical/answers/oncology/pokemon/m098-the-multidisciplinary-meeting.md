---
id: "m098"
slug: the-multidisciplinary-meeting
style: pokemon
category: oncology
difficulty: intermediate
question: "What is a cancer multidisciplinary meeting actually for, and what failure modes is it designed to prevent?"
tags: [multidisciplinary-team, decision-making, governance, pathways, documentation]
---

# Six hundred and forty trainers run one scoring script, and the Elite Four run four

Emerald does not decide an opponent's move with a clever function. It decides it with a
**committee whose membership is a field in a table**.

`gTrainers[]` gives every trainer an `aiFlags` word. `BattleAI_SetupAIData` sets all four of the
battler's move scores to **one hundred**, and `ChooseMoveOrAction_Singles` then runs this loop:

```
   while (AI_THINKING_STRUCT->aiFlags != 0)
   {
       if (AI_THINKING_STRUCT->aiFlags & 1) { ... BattleAI_DoAIProcessing(); }
       AI_THINKING_STRUCT->aiFlags >>= 1;
       AI_THINKING_STRUCT->aiLogicId++;
   }
```

One bit, one member. Each enabled script walks all four moves and adjusts their scores. The flag
word is consumed a bit at a time, so the members speak in a **fixed order given by bit position**
and not by who is loudest. And at the end the function does not return a decision; it collects
every move tied on the top score and returns `consideredMoveArray[Random() % numOfBestMoves]`.

Count the table and the distribution is the whole lesson. **Six hundred and forty** entries carry
`AI_SCRIPT_CHECK_BAD_MOVE` and nothing else — one member, who can only say *that move will not
work*. **One hundred and seventy-three** carry `CHECK_BAD_MOVE | TRY_TO_FAINT | CHECK_VIABILITY`:
**Roxanne**, **Brawly**, **Wattson** and **Norman** are all in that group, and so is **Wallace**.
**Sidney** has a fourth, `SETUP_FIRST_TURN`. And sixteen entries — placeholders and unused slots,
mostly — carry zero, which the loop handles by never running at all.

Sixteen zeroes is the interesting case, because the game still produces a move. Every usable
option kept its initial hundred, so they all tie, and the tie-break decides. **A process with
nobody in the room does not fail to produce an output. It produces one that looks exactly like
the others.**

As elsewhere in this specialty: **the objects of study are flag words, scoring scripts, a history
buffer and a tie-break.** No Pokémon in this answer stands in for a person with cancer, the thing
being decided about is a *move*, and the analogy is dropped entirely at the end, where the subject
changes.

Clinical claims carry the same marks as the rigorous half: **mechanism**, **definitional**,
(**consensus**, **country-dependent**).

## The structure, drawn against the failure it answers

```
   IN THE CODE                           WHAT IT PREVENTS
   ─────────────────────────────────────────────────────────────────────────────

   gTrainers[].aiFlags            ◄──    the option set being shaped by
   membership is a FIELD,                whoever happens to be looking.
   written before the battle             Six hundred and forty trainers
                                         have one member.  Guess what
                                         they are good at noticing.

   all four scores start at 100   ◄──    the referrer's plan starting
   BattleAI_SetupAIData,                 ahead of the alternatives.
   ALL_MOVES_MASK

   CheckMoveLimitations runs      ◄──    discussing options that are not
   BEFORE any script, and zeroes         available.  Eight named reasons:
   the unusable                          no move, no PP, Disable, Torment,
                                         Taunt, Imprison, Encore, and a
                                         Choice Band lock.

   aiFlags >>= 1 each pass        ◄──    order of speaking being set by
   — BIT POSITION is the agenda          force of personality.

   BATTLE_HISTORY — usedMoves,    ◄──    reasoning from what is true
   abilities, itemEffects,               rather than from what was
   trainerItems                          brought to the meeting.  Only
                                         OBSERVED facts are in there.

   the function returns a SCORE   ◄──    a score being mistaken for a
   and a tie-break, not a verdict        verdict.

   ─────────────────────────────────────────────────────────────────────────────

   AND THE PIECE WITH NO CODE IN IT AT ALL:

      THE MEETING                  THE CLINIC
      ┌──────────────────────┐     ┌──────────────────────────────────┐
      │ disease, imaging,    │ ──► │ the person: fitness, other       │
      │ histology, options,  │     │ conditions, priorities, what     │
      │ evidence, eligibility│     │ they want, what they will accept │
      └──────────────────────┘     └──────────────────────────────────┘
        produces a RECOMMENDATION    produces a DECISION

      Nothing in Pokémon models the right-hand box, and nothing here
      pretends to.
```

## Failure one: the option set shaped by the observer

A clinician's assessment of what is possible is conditioned by what they can do, and that is
neither dishonesty nor incompetence — it is what expertise does to a problem (**mechanism**).

`AI_SCRIPT_CHECK_BAD_MOVE` is that, drawn. It is a genuinely useful member: it notices that a move
has no mechanism against this target, which this repository's **Type Effectiveness** zero already
establishes as a different statement from *weak against*. But it is **one** member, and a trainer
carrying only that bit never asks whether a move is viable or whether anything can finish the
battle this turn, because nobody in the room asks those questions. Six hundred and forty entries
are in exactly that position.

Declaring the membership in advance is the control. The option set presented includes surgery,
systemic therapy, radiation therapy and, where relevant, treating neither the tumour nor a symptom
yet — regardless of which specialty referred the case. In several countries the required
membership is written into a national standard rather than left to local custom
(**country-dependent**, (**consensus**) in principle). It is a field in a table, not a habit.

## Failure two: deciding from the summary rather than the material

`BATTLE_HISTORY` has four arrays — `usedMoves` per battler, `abilities`, `itemEffects` and
`trainerItems` — and every one of them is a record of what has been **observed**.
`RecordLastUsedMoveByTarget` appends the target's last move only if it is not already listed, and
the dermatology answer on assessment before intervention already uses the companion fact that the
game records an opponent's ability only when it fires. The panel scores against the record, and
the record is not the world.

Which is the argument for the meeting reviewing **primary material**: the images on a screen with
a radiologist driving, the slides with a pathologist describing them, rather than the reports of
either. The justification is empirical. Specialist re-review of imaging and of histology changes
the assessment, and changes staging and diagnosis, often enough that it is done as a matter of
course — a statement about measured discrepancy rates rather than about anybody's competence
(**consensus**; those rates are disease-specific and are not quoted here). It is also why a case
arriving with its reports but without its images and blocks is frequently not reviewable at all.

## Failure three: the meeting that must produce something

`CheckMoveLimitations` runs before any script and zeroes the score of every move that cannot be
used, for eight separately-tested reasons: the slot is empty, the PP is gone, the move is the one
**Disable** named, **Torment** forbids repeating the last one, **Taunt** forbids anything with
zero power, **Imprison** forbids anything the opponent also knows, **Encore** forbids anything
except the encored move, and a **Choice Band** lock forbids anything but the chosen one. Striking
unavailable options off the agenda *before* discussion is a procedural act, and the game does it
first.

Then `AreAllMovesUnusable` is the honest corner. When every option is struck off, the battler does
not stall — it uses **Struggle**, which is what a process looks like when it is obliged to output
something and has nothing to output.

The clinical countermeasures are procedural (**consensus**): a list prepared in advance so the
missing results are known to be missing, and an explicit culture that **deferring is a legitimate
output**. "Insufficient information to recommend; proceed to these investigations and return" is a
complete and useful outcome. A guess recorded in the same field as a recommendation is
indistinguishable from a recommendation to everybody who reads it later — which is Struggle
recorded as a move choice.

## Failure four: the agenda, and who sets it

Two details about order, both exact.

`aiFlags >>= 1` on every pass means the scripts run in the order their **bits** sit in the word,
and `aiLogicId` indexes `gBattleAI_ScriptsTable` with that count. Nothing about the strength of a
member's opinion changes when it is heard.

And in one venue the agenda itself is restricted. In the **Battle Palace**, `BattleAI_SetupAIData`
is called with `gBattleStruct->palaceFlags >> MAX_BATTLERS_COUNT` instead of `ALL_MOVES_MASK`, so
only some of the four moves are given a starting score of a hundred and the rest start at zero and
are never seriously considered. A venue where the list is pre-filtered before anybody scores
anything is a real design, with real consequences, and a service that triages its meeting list is
making the same trade.

## Failure five: the record, and what happens between steps

The durable product of a meeting is the record: who was present, what was recommended, what
alternatives were considered, what was uncertain, and what would change the recommendation —
because the people who act on it were mostly not in the room (**mechanism**). A good record states
its **basis**, so a later reader can tell a recommendation that follows guidance from one that
departs from it, and records when a recommendation was **not** followed and why, which is the only
way the meeting learns anything about itself (**consensus**).

The other underrated function is that the list is a **register**. A named coordinator tracking
which cases have been discussed, which await results, which were referred onward and which have
not yet had their recommendation communicated turns the meeting into a tracking instrument as well
as a decision process (**consensus**, strongly (**country-dependent**) in how it is resourced). It
is the same mechanism that makes it the natural place to check open studies against, which is why
trial accrual tracks how the meeting is run and not only what is available (**consensus**).

## The piece the game is good at: a contribution with no value alone

**Helping Hand** has `.power = 0`, `.target = MOVE_TARGET_USER`, and `.priority = 5` — it goes
before almost everything. And `Cmd_trysethelpinghand` refuses it outright unless the battle is a
double battle, the partner is not absent, **and** neither battler already carries the flag.

So: a move whose entire function is to improve what a colleague is about to do, which fails if
there is no colleague, which must arrive **before** the colleague acts, and which cannot be
stacked. That is the specialist nurse's contribution, the radiologist's re-read, the pharmacist's
check: worth a great deal inside the meeting, worth exactly nothing outside it, and worth nothing
at all if it arrives after the decision.

## What the meeting cannot do

The meeting has the disease. It frequently does not have the person (**mechanism**). Fitness,
other conditions, what matters to the individual, what they would accept and what they have
already declined are often absent or second-hand; a performance status recorded weeks ago by
somebody else is a weak input routinely treated as a strong one, which is the next answer in this
specialty.

Three things follow (**consensus**). The output is a **recommendation**, taken to the person by
somebody who can discuss it, and the decision is made there. A recommendation can be declined, and
a documented decision not to follow it is a normal outcome rather than a deviation. And where the
recommendation depends on something the meeting does not know, it should be **conditional** —
recommending one thing if the person is fit for it and another if not is more honest than picking
one and hoping.

## The meeting's own failure modes

Stated plainly, because an uncritical account of this topic is useless (**consensus**).
**Volume**: time per case falls as the list grows, and many brief discussions can be a worse
instrument than few real ones. **Dominance**: one voice setting the frame gives the structure of a
multidisciplinary meeting without the function. **Rubber-stamping**: confirming the referrer's
plan is the default failure, and it is invisible, because the record of a rubber-stamp and the
record of a review look identical — a one-bit `aiFlags` word and a four-bit one produce output in
the same format. **Absent disciplines**: a recommendation made without radiology or pathology
present is a different kind of output and should be recorded as one. **Everything-by-default**:
equal depth for every case spends on the easy ones the time the difficult ones needed. And **the
evidence base**: that multidisciplinary review improves outcomes rests largely on observational
and audit evidence with the mechanisms above as the reasoning. It is a widely accepted model of
care rather than a randomised finding, and saying so is more useful than overstating it.

## Where the metaphor stops

Everything above is flag words, scoring scripts and a tie-break, and code is a good place to see
them because the order of operations is written down. What follows is about people, so it is said
plainly and without the analogy.

Being discussed at a meeting one is not present at, by people one has mostly not met, is a strange
thing to be told about and a stranger thing to find out about afterwards. People are sometimes
told that their case is going to the meeting with no account of what that is, and then wait —
often over a weekend — for a recommendation whose timing nobody has explained. Two things follow
that cost nothing: saying what the meeting is and when it sits, and saying who will make contact
afterwards and roughly when.

And the recommendation-versus-decision distinction is not administrative. It is the difference
between being told what has been decided about you and being offered what has been recommended for
you, and only the second leaves room for a person to say they want something else, or nothing yet,
or more time. Where a recommendation is presented as settled, that room disappears without anybody
intending it to. No mechanic in this game models the clinic, and none of the above was derived
from one.

## What a Gym Leader is listening for

* Six hundred and forty entries carry one scoring script. Which clinical failure is that, and what
  is the structural answer to it?
* All four scores start at one hundred. What would be different if the referrer's option started
  higher?
* `CheckMoveLimitations` runs before any script. Name the procedural act that corresponds to, and
  the eight reasons it uses.
* `AreAllMovesUnusable` leads to Struggle. What is Struggle, in a meeting?
* `BATTLE_HISTORY` holds what was observed. Which failure does that illustrate, and what is the
  countermeasure?
* Helping Hand fails when there is no partner and must land before the partner moves. Name both
  halves of what that models.
* The sixteen zero-flag entries still produce a move. Why is that the most uncomfortable fact in
  this answer?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific
to this answer:

* Your national or regional standard for multidisciplinary cancer care, published by the body that
  sets it — for required membership, quorum, what must be recorded and which cases must be
  discussed. The single most useful document here, and it differs substantially between countries.
* Your own institution's terms of reference for the meeting in your disease, which governs who
  chairs it, how the list is prepared and how a recommendation is communicated.
* Your service's audit of the meeting — attendance, quorum, proportion of recommendations
  implemented and the reasons recorded for non-implementation. That audit, not this answer, is the
  evidence about your meeting.
* The tumour–node–metastasis classification published by the Union for International Cancer
  Control, for the staging language the meeting is conducted in.
* The primary literature, for the effect of multidisciplinary review on management and outcome and
  for specialist re-review discrepancy rates, both of which rest on observational studies.

The Pokémon side is in the opposite position and is sourced file by file in the closing note.

## Scope and safety

This is revision material about how a decision process is constructed, dressed in a game so that
the difference between a declared membership and an ad hoc one stays concrete. It has had no
clinical review. **No membership requirement, quorum, discrepancy rate, timescale or target
appears here, and none should be inferred** — those are set nationally and locally, differ between
countries and institutions, and are revised; the standard and terms of reference in force where
you work are the authority, and this is not. It is not a governance document and not a decision
aid, and it describes no individual's case. Anyone affected by cancer — their own diagnosis or
someone else's — should be talking to the clinical team looking after that person, who have the
images, the histology and the history, none of which are here. The analogy carries membership,
agenda, order and output format only: the thing being decided about is a move, no part of it
stands in for a person, and nothing in the game models the clinic conversation.

## Where this stands, October 2026

The Pokémon facts are read from Emerald's own source. `include/constants/battle_ai.h` defines the
script bits, of which `CHECK_BAD_MOVE`, `TRY_TO_FAINT`, `CHECK_VIABILITY`, `SETUP_FIRST_TURN`,
`RISKY`, `PREFER_POWER_EXTREMES`, `PREFER_BATON_PASS`, `DOUBLE_BATTLE`, `HP_AWARE` and
`TRY_SUNNY_DAY_START` are the low ten, with `ROAMING`, `SAFARI` and `FIRST_BATTLE` at the top end
and bits ten to twenty-eight marked unused in the file's own comment. `BattleAI_SetupAIData` in
`src/battle_ai_script_commands.c` sets each of the four move scores to one hundred when the
matching bit of `defaultScoreMoves` is set, is called with `ALL_MOVES_MASK` in ordinary battles
and with `gBattleStruct->palaceFlags >> MAX_BATTLERS_COUNT` in the Battle Palace, and zeroes the
score of any move flagged by `CheckMoveLimitations`. That routine, in `src/battle_util.c`, tests
in order for an empty slot, zero PP, the Disabled move, Torment against `gLastMoves`, Taunt
against a zero `power` field, Imprison via `GetImprisonedMovesCount`, an Encore lock, and a Choice
Band lock against `gBattleStruct->choicedMove`; `AreAllMovesUnusable` routes to
`BattleScript_NoMovesLeft` when all four are flagged. `ChooseMoveOrAction_Singles` consumes
`aiFlags` one bit at a time, incrementing `aiLogicId`, which indexes `gBattleAI_ScriptsTable`, and
returns `consideredMoveArray[Random() % numOfBestMoves]`. `BATTLE_HISTORY` is declared in
`include/battle.h` as `usedMoves` per battler plus `abilities`, `itemEffects` and `trainerItems`,
and `RecordLastUsedMoveByTarget` appends `gLastMoves[target]` only into the first empty slot and
only if it is not already present. The counts quoted are from `src/data/trainers.h` as it stands:
six hundred and forty entries with `AI_SCRIPT_CHECK_BAD_MOVE` alone, one hundred and seventy-three
with `CHECK_BAD_MOVE | TRY_TO_FAINT | CHECK_VIABILITY`, thirteen with `CHECK_BAD_MOVE |
TRY_TO_FAINT | SETUP_FIRST_TURN`, seven with `CHECK_BAD_MOVE | TRY_TO_FAINT`, five with the three
plus `RISKY`, one with the three plus `SETUP_FIRST_TURN`, and sixteen with zero — the last group
being `TRAINER_NONE`, the Brendan and May placeholders, the Red and Leaf entries and a run of
apprentice entries, so it is a statement about the table and not about sixteen trainers a player
meets. Roxanne, Brawly, Wattson, Norman and Wallace carry the three-script set and Sidney carries
it plus `SETUP_FIRST_TURN`; Youngster Calvin and Youngster Allen carry one script. Frontier,
e-Reader, Trainer Hill and Secret Base battles override the trainer's own word with exactly
`CHECK_BAD_MOVE | CHECK_VIABILITY | TRY_TO_FAINT`. Helping Hand's move data is `.power = 0`,
`.accuracy = 100`, `.pp = 20`, `.target = MOVE_TARGET_USER`, `.priority = 5`, and
`Cmd_trysethelpinghand` requires `BATTLE_TYPE_DOUBLE`, a non-absent partner and neither battler
already flagged. Later generations replaced this AI wholesale and nothing here is claimed about
them.

The clinical reasoning is structural and should age well: a declared membership, review of source
material, a written record, a register that tracks people between steps, and an output that is a
recommendation rather than a decision are answers to failures that do not go away. What moves is
the regulation and the format — required membership, quorum rules, which cases must be discussed,
what must be recorded and how fast a recommendation must reach the person are all set nationally
and revised; remote and hybrid meetings are now ordinary in many services; triage of the list is
adopted unevenly; and automated preparation and summarisation of the list is active with no
settled position. No requirement, interval or clinical figure is quoted here, deliberately.
