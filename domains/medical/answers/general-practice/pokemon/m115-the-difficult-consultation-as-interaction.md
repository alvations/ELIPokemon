---
id: "m115"
slug: the-difficult-consultation-as-interaction
style: pokemon
category: general-practice
difficulty: advanced
question: "Why is a consultation that leaves the clinician feeling helpless better described as a property of the interaction than of the person, and what follows from that?"
tags: [consultation, attribution, diagnostic-error, continuity, clinician-factors]
---

# Not one of these four objects is a property of anybody on the field

**Nothing in this answer stands in for a patient, and a consultation is not a battle.** The four
objects used below were chosen because not one of them is a property of a participant: a *failure
readout* that erases its own cause, a *bitmask* of unusable options assembled from six different
stores, a *field condition* that belongs to neither side, and a *rate product* with nine terms and
no display. Every one of them is a fact about a situation. That is the entire reason they are the
right devices here, and the obvious adversarial mapping — the patient as the opponent — is wrong
on taste and also wrong on mechanism, because an opponent is a participant and the thing being
described is not.

## One label, ninety-five jumps, and five instructions

m101 found this in `data/battle_scripts_1.s` and used it for chest pain: a dozen unrelated
mechanisms producing one presenting complaint. The same object carries this question better,
because here the readout is the clinician's own.

```
   COUNTED IN data/battle_scripts_1.s. The identifier BattleScript_ButItFailed
   appears 96 times: once as the label definition, 95 times as a destination.

   BattleScript_ButItFailed::
        pause B_WAIT_TIME_SHORT
        orbyte gMoveResultFlags, MOVE_RESULT_FAILED
        resultmessage
        waitmessage B_WAIT_TIME_LONG
        goto BattleScript_MoveEnd

   FIVE INSTRUCTIONS. One bit set. Ninety-five places in the game's scripts arrive
   here, from effects that have nothing whatever to do with one another, and the
   player is shown a single sentence.

   AND THE MISS STRINGS ARE A SEPARATE SET. The engine distinguishes several ways
   of missing and offers exactly one way of failing. So the readout's resolution
   is not uniform: it is fine where the cause is mechanical and coarse where the
   cause is structural.
```

The lesson transfers exactly. A readout reached from ninety-five places cannot tell you which of
the ninety-five you are in, and a Trainer who concludes anything about *why* from the fact that
the message appeared has over-read a five-instruction label.

## Eight causes, six stores, and one of them is on the other side of the field

`CheckMoveLimitations` in `src/battle_util.c` is the second object, and it is better than the
first because its causes are enumerable. It walks the four move slots and ORs a bit into one
mask for each of **eight** conditions:

| | the condition | where it is stored |
| --- | --- | --- |
| 1 | the slot is empty | `gBattleMons[battler].moves[i]` |
| 2 | the slot has no PP | `gBattleMons[battler].pp[i]` |
| 3 | **Disable** names this move | `gDisableStructs[battler].disabledMove` |
| 4 | **Torment**, and this was the last move used | `status2` plus `gLastMoves[battler]` |
| 5 | **Taunt** is running and this move's power is 0 | `gDisableStructs[battler].tauntTimer` |
| 6 | **Imprison** — the move is known by somebody opposite | `gStatuses3` **on the other battlers** |
| 7 | **Encore** is running and this is not the encored move | `gDisableStructs[battler].encoreTimer` |
| 8 | a **Choice Band** has locked a different move | `gBattleStruct->choicedMove[battler]` |

Six separate stores, eight conditions, one bit per slot. The menu greys the slot out and says
nothing about which of the eight did it — which is m071 nursing's device, where it stood for a
treatment that has stalled for five possible reasons under one readout. Three further details
earn their place:

* **Condition 6 is not on your side of the field.** `GetImprisonedMovesCount` walks every battler,
  skips the ones on your own side, and checks `STATUS3_IMPRISONED_OTHERS` on the others. So a move
  can be unusable because of a bit set on somebody else, and there is no version of the fact that
  lives on you. That is a relational property in the strict sense: it is a fact about a pair.
* **Condition 8 is historical.** The Choice lock reads a move you yourself chose earlier. The
  block is you, one turn ago.
* **Condition 5 identifies its targets by `power == 0`.** Taunt does not consult a category flag;
  it greys out whatever has no attack power. A filter that works by a proxy field catches things
  nobody intended it to catch.

So of eight causes, one is relational, one is historical, and none of them is visible as itself.
A Trainer looking at four grey slots has exactly as much information as a clinician who knows only
that the consultation went badly.

## The condition is on the field, and the message names whoever walked in

The third object is **Spikes**, and m036 nursing established it while m105 emergency used it for
this precise failure. Spikes live in `gSideStatuses`, which is a property of a *side of the field*
and not of any battler, and the game provides **no screen indicator for them at all**. What it
does provide is a string:

```
   sText_PkmnHurtBySpikes[] = "{B_SCR_ACTIVE_NAME_WITH_PREFIX} is hurt
                               by SPIKES!"

   The cause is stored where nothing displays it. The message names the entrant,
   every single time something enters. And whoever set the layer may have left the
   field long ago — their own Pokémon is not required to be present for the hazard
   to keep working.
```

Attribution follows the name in the string. Four entrants in a row take damage, the string names
four different Pokémon, and the shared cause is never named at all. That is exactly the error the
serious half calls attribution: the consistent element is in the environment, the readout names
whoever is currently in it, and the environment has no indicator.

## When nothing is usable the engine still acts, and it bills the actor

The fourth object is the one that makes the whole thing uncomfortable in the right way.
`AreAllMovesUnusable` checks whether the mask has come back as `ALL_MOVES_MASK`. If it has, it
sets `noValidMoves`, and the selection script prints `STRINGID_PKMNHASNOMOVESLEFT`. Then, on the
actor's turn:

```
   if (gProtectStructs[gBattlerAttacker].noValidMoves)
   {
       gProtectStructs[gBattlerAttacker].noValidMoves = FALSE;
       gCurrentMove = gChosenMove = MOVE_STRUGGLE;
       gHitMarker |= HITMARKER_NO_PPDEDUCT;
       ...
   }
```

The engine does not permit a null turn. With nothing usable it substitutes **Struggle**, and
Struggle is implemented as the ordinary recoil script with one extra line.
`BattleScript_EffectRecoil` sets `MOVE_EFFECT_RECOIL_25 | MOVE_EFFECT_AFFECTS_USER |
MOVE_EFFECT_CERTAIN`, the same recoil effect byte as **Take Down**, and then jumps past an
`incrementgamestat` unless the move actually is Struggle. A quarter of the damage dealt, billed
back to the user. That fraction is pinned to the third generation on purpose: the basis changed to
maximum HP from the fourth generation, and an unqualified figure here would be wrong somewhere.

And then the detail that ought to be read twice:

```
   BattleScript_MoveEffectRecoil::
        jumpifmove MOVE_STRUGGLE, BattleScript_DoRecoil
        jumpifability BS_ATTACKER, ABILITY_ROCK_HEAD, BattleScript_RecoilEnd
   BattleScript_DoRecoil::
        ...
```

**Rock Head** waives recoil. It does not waive Struggle's, because the Struggle check jumps
*over* the ability check. The one cost that was never chosen is the one cost that nothing protects
against. An actor out of usable options is made to act anyway, and the protection that exists for
the costs of chosen acts is unreachable for this one.

That is not whimsy about anybody's suffering and it is not meant as one. It is a precise statement
about a system that forbids a null action: the cost of having no good option falls on whoever has
to act, and it falls outside every mechanism built to absorb the costs of acting.

## Nine levers, one product, and no readout

Last, the specialty's own object, from m082. The encounter rate a Trainer actually experiences is
the table rate times 16, then times 80/100 on either bike, then halved or raised by half by the
**Black Flute** or the **White Flute**, then two thirds with a **Cleanse Tag** on the lead, then
halved or doubled by **Stench**, **White Smoke**, **Illuminate**, **Arena Trap** or **Sand Veil**
in slot 0, then clamped to `MAX_ENCOUNTER_RATE 2880`. Nine levers. One product. Nothing anywhere
on screen displays the result.

Two consequences, and they are the ones that matter for choosing what to change:

* **The last lever you touched is not the explanation.** A Trainer who put on a Cleanse Tag and
  then had a quiet walk has one data point against a nine-term product and a clamp, and the clamp
  in particular can make a lever do nothing at all.
* **The levers are not equal and are not all yours.** The bike multiplier is a choice; the lead's
  ability is a party-composition decision made long before; the table rate is the route's and
  cannot be touched from inside the walk. Three different classes of term, and only one of them is
  adjustable in the moment.

Which is the honest answer to *what should I change*: find out which term is actually large.
m082's separation holds — the levers move how often you are asked, and not one of them touches a
slot.

## Where the metaphor stops

The person in the chair is usually having a worse time than the clinician. People who consult
repeatedly without resolution are often in distress, often unwell in ways nobody has named, and
often aware — accurately — that they are experienced as a burden. Knowing that about yourself, in
a room you came to for help, is its own harm, and it is a harm the consultation produces rather
than one it inherits.

It falls unequally. The categorisation attaches most readily to people whose symptoms are not
visible, whose conditions fluctuate, who have no diagnosis yet, whose first language is not the
system's, who are poor, or who already have a psychiatric diagnosis in the record. That is m050's
mechanism arriving as a social process inside a consultation, and better intentions do not fix it.
Only the discipline of describing the interaction rather than the person does, and imperfectly.

The clinician's side, without self-pity and without dismissal: repeated consultations in which
nothing is achieved are a real occupational load, they contribute to burnout, and the feelings
that come with them — irritation, dread, guilt about the irritation — are ordinary and are not
evidence of a defect of character. They are also not private, because a clinician carrying them
alone is more likely to make the attribution error above. The route out is collegial and
structural, which is why case discussion and supervision belong on a list of interventions rather
than on a list of kindnesses.

And one thing is deliberately set aside. Where the distress in the room is a mental-health crisis,
or where there is risk to the person, none of the analysis above is the relevant frame and none of
the analogy reaches it at all. The applicable local urgent mental-health pathway is the authority
there, and no mechanic in any video game has anything to say about it.

## What a Gym Leader is listening for

Whether the Trainer starts from the readout rather than from the opponent — and notices,
unprompted, that none of the four objects is a property of a participant. Then the count: 96
appearances of one identifier, 95 of them destinations, five instructions inside, against a
separate set of miss strings. Then the eight conditions and six stores, with **Imprison** singled
out as stored on the other side of the field and the **Choice Band** as stored one turn ago. Then
**Taunt** catching things by `power == 0`, offered as a proxy-field problem. Then **Spikes**: the
cause in `gSideStatuses` with no indicator and the string naming the entrant, with the point that
whoever laid it need not still be present. Then Struggle, with `HITMARKER_NO_PPDEDUCT` and the
recoil fraction pinned to the generation, and then **Rock Head** failing to cover it because the
jump goes over the ability check. Then the nine levers and the clamp, and the hardest one: which
term they would try to measure first, given that nothing displays the product.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* A current textbook of the general practice consultation, for the consultation models, for
  agenda-setting and for the clinician's emotional response treated as clinical data.
* The published literature on frequent attendance and on the clinician's response to it, read
  with attention to framing, since the framing has shifted substantially and the older
  terminology is now widely rejected.
* The national or regional guidance on persistent physical symptoms applying where the reader
  works, which differs between systems and has been revised (**country-dependent**).
* The published literature on diagnostic error, and on attribution error in particular, for how
  an existing label changes the assessment of a new symptom.
* The local urgent mental-health pathway and local safeguarding procedure applying where the
  reader works, for the situations the plain-prose section sets aside (**country-dependent**).
* Whatever case-discussion, supervision or reflective-practice structure the reader's own
  organisation provides.

The Pokémon facts are a separate matter and are not covered by the line above. The 96 appearances
of `BattleScript_ButItFailed` in `data/battle_scripts_1.s` and its five-instruction body setting
`MOVE_RESULT_FAILED`; the eight conditions of `CheckMoveLimitations` and the stores each reads,
including `GetImprisonedMovesCount` walking the opposing battlers for `STATUS3_IMPRISONED_OTHERS`
and **Taunt** selecting on `gBattleMoves[move].power == 0`; `AreAllMovesUnusable` comparing the
mask against `ALL_MOVES_MASK`, setting `noValidMoves` and queueing
`STRINGID_PKMNHASNOMOVESLEFT`; the substitution of **Struggle** with `HITMARKER_NO_PPDEDUCT`;
`BattleScript_EffectRecoil` setting `MOVE_EFFECT_RECOIL_25 | MOVE_EFFECT_AFFECTS_USER |
MOVE_EFFECT_CERTAIN` for both **Take Down** and Struggle, with the quarter being of damage dealt
in the third generation and the basis changing to maximum HP from the fourth;
`BattleScript_MoveEffectRecoil` jumping to `BattleScript_DoRecoil` on Struggle *before* the
**Rock Head** check; **Spikes** residing in `gSideStatuses` with no screen indicator while
`sText_PkmnHurtBySpikes` names the entering Pokémon; and the nine encounter-rate levers with
their multipliers and the clamp at `MAX_ENCOUNTER_RATE 2880`, were all read directly from the pret
decompilation projects, which this environment can reach. These are Emerald's.

## Scope and safety

This is revision material about the structure of a consultation, written for someone already
training in or qualified for the field. It is not a clinical reference, not a decision aid, and
nothing here should inform the assessment or management of any individual — that belongs with the
clinician who knows them. Nothing here describes any real person or consultation; every scenario
is constructed. This answer is not about mental-health crisis, risk of self-harm or safeguarding,
and neither the reasoning nor the analogy applies to any of those: where any is in question the
local urgent pathway or safeguarding procedure is the authority and takes precedence. No
diagnostic label, criterion or attendance threshold is named here on purpose. The jump counts,
bitmask conditions, recoil fraction and rate multipliers above are real properties of a video
game and stand in for a mechanism; none is a clinical quantity and no clinical figure should be
read out of them. If someone is unwell or in crisis right now, the relevant action is to contact
local urgent care, the local urgent mental-health service or the local emergency number, not to
read this.

## Where this stands, October 2026

The structural claim — that the readout has several unrelated generators and is therefore a poor
guide to its own cause — is mechanism and will not move. The framing has moved a great deal and
continues to: the older clinician-centred terminology has been substantially abandoned in teaching
and in published guidance over the last two decades, the management framing for persistent
physical symptoms has been revised more than once and differs by country, and the literature on
diagnostic error and attribution has grown rapidly. Terminology here is itself contested, so the
words a reader meets locally will differ from the words used above and should be taken from
current local sources. The Emerald scripts are stable because the games are finished, as of
October 2026.
