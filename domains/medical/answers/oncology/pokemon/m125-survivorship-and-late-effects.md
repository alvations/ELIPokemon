---
id: "m125"
slug: survivorship-and-late-effects
style: pokemon
category: oncology
difficulty: intermediate
question: "Why is a late effect of cancer treatment a different kind of clinical object from an acute toxicity, and what makes the record of the treatment the organising document for survivorship care?"
tags: [survivorship, late-effects, treatment-summary, surveillance, long-term-follow-up]
---

# The battle writes four kinds of thing into the permanent record, and the rest ends with it

Grep `src/battle_script_commands.c` for every `SetMonData` request the battle engine emits, and
the list is short:

```
   REQUEST_HP_BATTLE          hit points
   REQUEST_STATUS_BATTLE      status1 — the six persistent conditions
   REQUEST_PPMOVE1_BATTLE     the PP of one move slot
   REQUEST_MOVES_PP_BATTLE    the PP of all four
   REQUEST_HELDITEM_BATTLE    the held item
```

Four kinds of thing: HP, status, PP, item. Those are written through to `gPlayerParty[]`, the
structure that exists after the battle is over.

Now list what the battle also did. Stat stages, up and down to six either way. Confusion.
Infatuation. Leech Seed. Nightmare. The trapping states. Substitute's own HP. Reflect, Light
Screen, Mist, Safeguard, Spikes on either side. The weather. Disable, Taunt, Torment, Encore and
every timer in `gDisableStructs`. **Not one of those is written back.** They live in `status2`,
`gStatuses3`, `gSideStatuses`, `gSideTimers`, `gDisableStructs` and `gBattleWeather`, and when the
battle ends they are gone, having been as real as anything while it was running.

So the cartridge already distinguishes the two objects this answer is about. Something that
happened in the battle and something you still have afterwards are not the same kind of event, and
the difference is not severity. **It is which store it was written into.**

An acute toxicity and a late effect are not one phenomenon at two speeds. They are different
mechanisms with different reversibility and — the part that reorganises practice — a different
organising variable. An acute toxicity is predicted from the agent, the dose and the cycle. A late
effect is predicted from what somebody received, how much in total, where, and at what age: a
**record**, not an observation.

As elsewhere in this specialty, **the objects of study are stores, flags and probabilities.** No
Pokémon in this answer stands in for a person, nothing in it faints, and the analogy is dropped
entirely at the end where the subject changes.

Clinical claims carry the same marks as the rigorous half: (**mechanism**), (**definitional**),
(**consensus**), (**country-dependent**).

## What survives the battle, drawn

```
   WRITTEN BACK TO gPlayerParty[]            BATTLE-ONLY, DISCARDED

      hp                                       stat stages (±6)
      status1 (the six)                        confusion, infatuation
      pp[0..3]                                 Leech Seed, Nightmare, trapping
      heldItem                                 substituteHP
                                               Reflect / Light Screen / Mist /
                                                 Safeguard / Spikes
                                               the weather
                                               every gDisableStructs timer

      ►  five request constants ─────────┐    ►  no request exists for any
         covering four kinds of data     │       of these, so no store
                                         │       downstream ever sees them
                                         ▼
                              SAME SEVERITY DURING THE BATTLE.
                              Different store.  Different afterwards.

   ═══════════════════════════════════════════════════════════════════════════

   AND THE TWO THINGS WRITTEN BACK BEHAVE DIFFERENTLY

      hp   ── restored by Leftovers, Recover, Rest, Wish, a Sitrus Berry,
              a Potion, and by walking into any Pokémon Centre.
              A RENEWING compartment.

      pp   ── restored in battle by exactly one thing: a Leppa Berry,
              and its handler searches for a slot whose PP is ALREADY ZERO
              (`if (move && changedPP == 0) break;`) and writes to
              gPlayerParty[] directly.
              A NON-RENEWING compartment, and the only in-battle
              restorative operates on the permanent record.

      ►  and nothing on screen shows PP at all until you open the menu

   ═══════════════════════════════════════════════════════════════════════════

   THE THIRD SHAPE: A COST BILLED FOR COMPLETION

      Cmd_confuseifrepeatingattackends ──► MOVE_EFFECT_THRASH
                                            | MOVE_EFFECT_AFFECTS_USER

      Thrash and Outrage: .power = 90, and the cost arrives because the
      lock RAN TO THE END, is applied to the USER, and is a different
      kind of thing from the damage the move was for.

   ═══════════════════════════════════════════════════════════════════════════

   THE FOURTH SHAPE: A PROBABILITY BELONGING TO THE EXPOSURE

      percentChance = gBattleMoves[gCurrentMove].secondaryEffectChance;
      if (ability == ABILITY_SERENE_GRACE) percentChance *= 2;

      ►  the number is in the MOVE's data entry, not the target's
      ►  and it is re-rolled every use, so exposures ACCUMULATE
```

## Class one: a reserve that does not renew, and the only thing that restores it

HP and PP are both written back to the party. Watch how differently they behave.

HP has restoratives everywhere: Leftovers at a sixteenth per turn, Recover and Rest and Wish, a
Sitrus Berry's flat thirty in the third generation, a Potion from the bag, and a free full reset
at any Pokémon Centre. It is a renewing compartment and the game treats it as one.

PP has, inside a battle, one: `HOLD_EFFECT_RESTORE_PP`, the Leppa Berry. And read its handler,
because two details are doing work. It loops the four slots looking for one where `move &&
changedPP == 0` — **it fires only on a slot that is already completely exhausted**, not on a
depleted one. And it reads and writes `gPlayerParty[gBattlerPartyIndexes[battler]]` directly,
rather than `gBattleMons`, because PP is permanent-record data and the battle copy is not where it
lives.

That is class one, and the clinical version is the one that most reliably surprises people,
because for years there is nothing to find.

Some tissues have no meaningful progenitor pool, or one that is exhausted rather than replenished:
cardiac myocytes, nephrons, functional lung units, the ovarian follicle pool, and the endocrine
cells of an irradiated gland or pituitary, to varying degrees (**mechanism**, **consensus**). An
exposure that kills a proportion of them leaves the organ with less reserve, and reserve is by
definition the thing you are not currently using.

**It is silent until a demand arrives.** Resting function can be entirely normal in an organ with
substantially reduced reserve, because resting function is well below capacity. The clinical event
is the demand: a pregnancy, an intercurrent illness, an anaesthetic, another exposure on the same
organ, or ageing (**mechanism**). The emergency answer on compensation already owns the
observation that PP is the budget and the bar is not showing it; the point here is the other half
of it — the deficit **crosses the battle boundary**, and the next battle starts with it.

**Normal decline sums with it.** Every one of these compartments also declines with age in people
who were never treated, so a reduced starting reserve plus a normal rate of decline crosses the
symptomatic threshold earlier than either alone (**mechanism**). The arithmetic, not the biology,
is what makes these effects late.

**It is where the lifetime cumulative total comes from.** This specialty's answer on why toxicity
is predictable makes the point that a cumulative-dose-limited toxicity is a function of the total
received over a lifetime, and that lifetime totals are therefore carried forward across lines of
treatment and across years. The reason is this class: the tissue does not regenerate in the gap,
so the gap buys nothing (**mechanism**, **consensus**). A Leppa Berry that only fires at zero is
the right picture of a restorative that arrives too late to be prevention.

## Class two: the number is in the move's data entry, not the target's

`Cmd_seteffectwithchance` opens with two lines that place the probability exactly where this
answer needs it:

```
   if (gBattleMons[gBattlerAttacker].ability == ABILITY_SERENE_GRACE)
       percentChance = gBattleMoves[gCurrentMove].secondaryEffectChance * 2;
   else
       percentChance = gBattleMoves[gCurrentMove].secondaryEffectChance;
```

The chance is read from the **move**. Nothing about the target contributes to it. And the roll
happens on every use, so a move used many times has delivered many independent draws, no one of
which can be named as the one that mattered. **Serene Grace** — Togepi's and Togetic's ability in
the third generation — doubles it, which makes the modifier a property of the user and still not
of the target.

That is a second, independent malignancy arising years after treatment, and it is the clearest
case of a late effect that is not a severity at all but a probability.

Several of the things that treat cancer also damage DNA in cells that survive: radiation, and
among the systemic agents the alkylating agents and the topoisomerase inhibitors are the ones
conventionally named (**mechanism**, **consensus**). A surviving cell with a new mutation may do
nothing for a lifetime or may found a malignancy, and which happens is not a function of how much
anybody is looking.

Three features distinguish the class.

**Risk accrues with time since exposure rather than resolving** — the exposure is finished and the
hazard is not, the opposite of an acute toxicity's behaviour (**mechanism**).

**The latency differs by mechanism**, which is why the classes of second malignancy do not appear
on one timescale: the haematological ones attributed to particular systemic agents behave
differently in time from solid second cancers arising in a previously irradiated field
(**consensus**). The specific intervals belong to the literature and are deliberately not here.

**Nothing about the person's later state reports on it.** There is no reserve to measure and no
function to test, exactly as there is nothing in `gBattleMons` that records how many secondary
rolls a battler has been subjected to. The only thing that identifies somebody as being in the
at-risk group is the record of what they received, and in some settings the field it went to.

This specialty's answer on radiotherapy and fractionation names the mechanistic basis of
radiation-associated second malignancy as a **stochastic** late effect rather than a deterministic
one, and stochastic-against-deterministic is the cleanest available summary of the difference
between this class and the first.

## Class three: a cost billed for completion, and a structure that stays changed

`Cmd_confuseifrepeatingattackends` is three lines:

```
   if (!(gBattleMons[gBattlerAttacker].status2 & STATUS2_LOCK_CONFUSE))
       gBattleCommunication[MOVE_EFFECT_BYTE] = (MOVE_EFFECT_THRASH | MOVE_EFFECT_AFFECTS_USER);
```

Thrash and Outrage have `.power = 90` and `.secondaryEffectChance = 100`, and their handler sets
`STATUS2_MULTIPLETURNS`, stores the move in `gLockedMoves[]`, and writes
`STATUS2_LOCK_CONFUSE_TURN((Random() & 1) + 2)` — two or three turns, per the source's own
comment. When the counter runs out the confusion arrives.

Read what kind of cost that is. It is **billed for completion, not for failure**. The move did not
miss and was not countered; it worked, for its full duration, and the bill is a different kind of
thing from the damage it was for, applied to the user, flagged `MOVE_EFFECT_AFFECTS_USER` so that
the engine knows which side to charge.

That is class three's framing and it is the framing of the whole answer: these are consequences of
treatment that worked. The class itself is the least mysterious and the easiest to under-record.
Fibrosis in an irradiated field, lymphoedema after nodal surgery or radiotherapy, altered anatomy
after resection, stoma-related consequences and the functional results of all of them are changes
to the structure rather than to a reserve (**mechanism**). They do not recover because there is
nothing to recover: the tissue is now different tissue. Some progress slowly for years after
treatment, which is what puts them here rather than in the acute answer.

And there is a much larger version for anybody treated **before maturity**. A growth trajectory, a
skeletal trajectory, dentition, and neurocognitive and endocrine development were all processes
running at the time of treatment, and an intervention applied to a running process alters its
output rather than its current state (**mechanism**). The consequence appears when the process
would have delivered its result, years later. That is why dedicated long-term follow-up services
for people treated as children exist where they exist, and why age at treatment is one of the
dominant variables in any late-effect risk assessment (**consensus**, strongly
(**country-dependent**) in how such services are organised and resourced).

The honest limit, stated here rather than at the end: Thrash's counter is two or three turns and
nothing in Emerald has a latency measured in anything like the gap this clinical class needs.
`STATUS2_LOCK_CONFUSE_TURN` is a three-bit field. The *shape* of a cost billed for completion is
right and the *timescale* has no analogue at all, and the second half of that sentence matters as
much as the first.

## Six records of the last move, and not one of them is a history

So the risk belongs to the exposure. Which makes the record of the exposure the document that
organises everything afterwards — and here the cartridge has a fact that is better than an
analogy.

Emerald keeps **six** separate per-battler arrays about what just happened:

```
   EWRAM_DATA u16 gLastPrintedMoves[MAX_BATTLERS_COUNT]
   EWRAM_DATA u16 gLastMoves[MAX_BATTLERS_COUNT]
   EWRAM_DATA u16 gLastLandedMoves[MAX_BATTLERS_COUNT]
   EWRAM_DATA u16 gLastHitByType[MAX_BATTLERS_COUNT]
   EWRAM_DATA u16 gLastResultingMoves[MAX_BATTLERS_COUNT]
   EWRAM_DATA u8  gLastHitBy[MAX_BATTLERS_COUNT]
```

Six, because six different consumers need six different definitions of *what just happened*:
chosen against used, used against landed, landed against the type that landed, the resulting move
after a redirection, the one that was printed. Mirror Move, Encore, Counter and Mirror Coat,
Mimic, and the message system each read a different one, and reading the wrong one gives a wrong
answer rather than no answer.

And now the fact that matters: **every one of them holds only the most recent value.** There is no
array anywhere that holds the sequence. Each is overwritten on the next event and each is cleared
to `MOVE_NONE` on switch-in, at the site the emergency answer on handover already documents for
what survives a switch and what does not.

That is the clinical argument exactly (**mechanism**):

* class one risk depends on which organ-toxic agent, how much in total, and what else acted on the
  same organ;
* class two risk depends on which mutagenic exposure, how much, and to which field;
* class three risk depends on what was removed or irradiated, and on the age at which it happened.

Not one of those is the name of the cancer. Two people with the same diagnosis treated in
different eras or on different protocols have different late-effect risks; two with unrelated
diagnoses who received the same agent share one. **Survivorship care is organised by exposure, not
by diagnosis.**

So the document is a **treatment summary**: the agents with their cumulative totals, the radiation
fields and the delivered dose, the operations, the age at treatment, and any acute toxicity that
occurred and might predict a late one (**consensus**). Where it is given to the person and to
their general practitioner at the end of treatment, the surveillance that follows can be aimed;
where it is not, nobody downstream can tell what to look for or what a later symptom might mean
(**mechanism**).

Which is a records problem, and it fails the way records problems fail. The nursing answer on the
clinical record makes the general case that a record is an instrument other people act on and that
a pertinent negative is worth writing down. Survivorship sits at the worst possible transfer: out
of a specialist service, into primary care, years before the thing being guarded against appears,
with the people who know least about the exposure being the ones present when it declares
(**consensus**). Six arrays, each correct for its own reader, none of them a history — and the
thing a survivorship clinic needs is the history.

## Why surveillance is justified only where an action follows

`moveDmgs[]` in the opponent's thinking routine exists only because the next instruction compares
it against the other three. This specialty's answer on treatment intent makes the point at length:
a reading with nothing downstream that consumes it is not information, it is overhead.

**Surveillance is justified where detection changes what happens** (**mechanism**). For several
late effects there is a real pathway: a surveillance test, an abnormality defined on it, and an
intervention that improves the outcome. For others there is a test and no intervention, and
performing it generates diagnoses without benefit.

Three harms, all already in this corpus. This specialty's answer on screening and overdiagnosis
sets out that finding more is not automatically better and that overdiagnosis is a real harm
rather than a technicality. The general-practice answer on overdiagnosis adds that labelling
outlives what it labelled — `GetSetPokedexFlag` with no case that clears a bit. And the emergency
answer on imaging sets out that a test has a harm of its own. All three apply to a population
that is, by construction, well.

A fourth harm is specific to this setting and is worth naming on its own: a surveillance programme
tells somebody that they remain a person at risk, every time it runs. For some people that is
reassuring and for some it is the opposite, and it is not a neutral act (**consensus**).

Which late effects have an established surveillance pathway, and what each consists of, is set out
in national guidance and in the long-term follow-up protocols of the services that run them, and
it differs substantially between countries and between adult and paediatric practice
(**consensus**, strongly **country-dependent**). It also changes, which is why a protocol is the
place to read it and a revision note is not.

## Attribution, and why it gets harder with time

One more structural point, because this is where reasoning about late effects goes wrong in both
directions.

As time passes since treatment the base rate of ordinary disease in the same person rises. A
cardiac problem twenty years after an anthracycline may be a late effect, may be ordinary
cardiovascular disease, and is frequently both acting together (**mechanism**). Two symmetrical
errors follow and both are common:

* **attributing everything to the treatment**, which aims investigation at the wrong mechanism and
  leaves ordinary modifiable risk alone;
* **attributing nothing to it**, which is the default when nobody has the treatment summary, and
  which assesses a known-at-risk organ as though it were an average one.

The resolution is not to decide but to hold both, which requires knowing the exposure. So this
section is the previous one restated: the record is what makes the question askable. Six arrays
that each hold one value cannot answer *what has this battler been subjected to*, and the game
does not pretend otherwise.

## Where the metaphor stops

Everything above is stores, write-backs and probabilities, and the cartridge is a good place to
see them because the list of things written back to the permanent record is five lines you can
grep for. What follows is about people, so the analogy stops and nothing below leans on it.

The end of treatment is widely assumed to be the good part and frequently is not. People describe
the withdrawal of a structure — appointments, a team, a plan, something to do — at exactly the
point when everybody around them expects relief and celebration, and the mismatch between what is
expected of them and what they feel is itself part of the difficulty. Fear that the cancer will
come back is close to universal and does not indicate that anything has gone wrong with the
person; it is a reasonable response to a real uncertainty, it is well described, and there are
services and approaches for it. Anybody struggling with it should be talking to their clinical
team or their general practitioner, who can say what is available where they are. That is as far
as either half of this answer goes on it, deliberately, and neither half goes into anybody's
outlook at all.

The practical things that help are unglamorous. People are entitled to a written summary of what
they received, in language they can use, because they will be the one carrying it to clinicians
who have never seen their oncology notes — and they are frequently the only reliable route by
which that information travels. They are entitled to know which symptoms matter enough to report
and to whom, specifically enough to act on rather than as a general instruction to be vigilant.
And they are entitled to have their ordinary health looked after: somebody treated for cancer
years ago is still a person who needs their blood pressure checked and their vaccinations offered,
and attention disproportionately focused on the cancer history is its own kind of neglect.

Nothing in either half says anything about what will happen to any individual, and no clinical
figure of any kind appears in either half. Both omissions are deliberate. And nothing in the game
stands in for a person anywhere in this: the subject throughout has been which store a consequence
was written into.

## What a Gym Leader is listening for

* The engine emits five `SetMonData` request constants covering four kinds of data, and no more.
  What clinical distinction is that list, and why is it not a distinction of severity?
* HP has a dozen restoratives and PP has one. Which late-effect class is that, and what is the
  clinical event when the deficit declares?
* The Leppa Berry fires only on a slot whose PP is already zero. What does that say about a
  restorative arriving after the reserve is spent?
* `secondaryEffectChance` is read from the move and not the target. Which late-effect class is
  that, and what identifies somebody as being in the at-risk group?
* Serene Grace doubles the chance and is a property of the user. What does that add to the
  argument?
* `MOVE_EFFECT_THRASH | MOVE_EFFECT_AFFECTS_USER` bills a cost for completion. Why is that the
  right framing for the whole of survivorship?
* Where does this analogy break on timescale, and why does saying so matter as much as the device?
* Six `gLast...` arrays, each correct for its own reader, none of them a history. What does a
  survivorship clinic need that none of them is?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific to
this answer:

* Your national guidance on cancer survivorship or long-term follow-up, from the body that issues
  it where you work. It says what a treatment summary must contain and who holds the follow-up,
  and it differs between countries and between adult and paediatric practice.
* The long-term follow-up protocols of the service that runs them locally, for which late effects
  are surveyed, with what test, at what interval, and what an abnormality triggers. These are the
  only place a surveillance schedule should be read.
* The published guidance for people treated for cancer in childhood, adolescence or young
  adulthood from the group that issues it in your region. That population's late-effect profile
  and surveillance recommendations are substantially different and are maintained separately.
* Your national formulary and the product information for any agent concerned, for its recognised
  long-term and cumulative-dose toxicities and whatever monitoring is advised.
* A current standard textbook of the specialty, for the mechanisms of each class, for which organs
  have renewing and non-renewing compartments, and for the recognised late effects of radiotherapy
  by site.
* The primary literature, for the latency and magnitude of second-malignancy risk by exposure, and
  for the evidence that any particular surveillance pathway improves outcomes. The second is the
  claim here most worth checking.

The Pokémon side is in the opposite position and is sourced file by file in the closing note.

## Scope and safety

This is revision material about the mechanisms of late effects and about why the treatment record
organises the care that follows, dressed in a game so that the question of which store a
consequence lands in stays visible. It has had no clinical review. **No agent, cumulative dose,
radiation dose, surveillance test, interval or risk figure appears here, and none should be
inferred** — the surveillance schedules belong to the long-term follow-up protocol in force where
you work, they differ between countries, between services and between adult and paediatric
practice, and they are revised; that protocol is the authority and this is not. It says nothing
about what will happen to any individual, it is not a decision aid, and it describes no
individual's situation. Anyone affected by cancer — their own treatment or someone else's —
should be talking to the clinical team or general practitioner looking after that person, who have
the treatment record and the examination, neither of which is here. Anybody struggling with the
end of treatment or with fear of recurrence should raise it with that team; this is a note about
mechanism and is not support. The analogy carries stores and probabilities only: no part of it
stands in for a person, nothing in it faints, and no creature's situation is the subject of any
sentence in it.

## Where this stands, October 2026

The Pokémon facts are read from Emerald's own source and nothing here is claimed about any
generation but the third. The `BtlController_EmitSetMonData` requests appearing in
`src/battle_script_commands.c` are `REQUEST_HP_BATTLE`, `REQUEST_STATUS_BATTLE`,
`REQUEST_PPMOVE1_BATTLE`, `REQUEST_MOVES_PP_BATTLE` and `REQUEST_HELDITEM_BATTLE`;
`REQUEST_ALL_BATTLE` appears in that file only in `BtlController_EmitGetMonData`, which reads
rather than writes. Stat stages, `status2`, `gStatuses3`, `gSideStatuses`, `gSideTimers`,
`gDisableStructs` and `gBattleWeather` have no write-back request. In `src/battle_util.c` the
`HOLD_EFFECT_RESTORE_PP` case loops the four slots with `if (move && changedPP == 0) break;` and
reads and writes `gPlayerParty[gBattlerPartyIndexes[battler]]` or the enemy equivalent through
`GetMonData` and `SetMonData`, using `CalculatePPWithBonus(move, ppBonuses, i)` for the ceiling.
`Cmd_seteffectwithchance` in `src/battle_script_commands.c` reads
`gBattleMoves[gCurrentMove].secondaryEffectChance` and doubles it for `ABILITY_SERENE_GRACE`.
`Cmd_confuseifrepeatingattackends` sets `gBattleCommunication[MOVE_EFFECT_BYTE] =
(MOVE_EFFECT_THRASH | MOVE_EFFECT_AFFECTS_USER)` unless `STATUS2_LOCK_CONFUSE` is already set;
`sStatusFlagsForMoveEffects[MOVE_EFFECT_THRASH]` is `STATUS2_LOCK_CONFUSE`, and the
`MOVE_EFFECT_THRASH` case of `SetMoveEffect` sets `STATUS2_MULTIPLETURNS`, writes `gLockedMoves`
and applies `STATUS2_LOCK_CONFUSE_TURN((Random() & 1) + 2)` under the comment `// thrash for 2-3
turns`. `src/data/battle_moves.h` gives Thrash `.effect = EFFECT_RAMPAGE`, `.power = 90`, `.type =
TYPE_NORMAL`, `.accuracy = 100`, `.pp = 20`, `.secondaryEffectChance = 100`, `.target =
MOVE_TARGET_RANDOM`, and Outrage the same with Dragon type and `.pp = 15`. The six arrays —
`gLastPrintedMoves`, `gLastMoves`, `gLastLandedMoves`, `gLastHitByType`, `gLastResultingMoves` and
`gLastHitBy` — are declared in `src/battle_main.c` over `MAX_BATTLERS_COUNT` and are each reset at
battle start and on switch-in. Serene Grace is Togepi's and Togetic's ability in the third
generation; the Sitrus Berry's flat thirty is a third-generation figure and the percentage version
is later; the Leftovers fraction is a sixteenth of maximum HP.

The clinical reasoning will not date in its mechanistic half: a compartment that does not renew
loses reserve and declares when a demand arrives, a mutagenic exposure leaves a probability that
accrues with time, an altered structure stays altered, and a process interrupted while running
delivers an altered result later. Nor will the organisational conclusion that follows — the risk
belongs to the exposure, so the record of the exposure organises everything afterwards. Almost
everything operational is moving: who holds long-term follow-up, whether a treatment summary is
routinely issued, and which late effects have a surveillance pathway are set nationally and
locally and are being revised, with the direction of travel towards risk-stratified rather than
uniform review. The genuinely unsettled part is the late-effect profile of the newer treatment
classes — the immune checkpoint inhibitors and the targeted agents have not been in use long
enough to be characterised the way the cytotoxics and radiotherapy have, and persistent endocrine
consequences of checkpoint inhibition are already recognised while the full picture is not. Any
list of late effects written now is a list about the treatments of the past, which is worth saying
plainly. No agent, dose, interval or figure is quoted here, deliberately.
