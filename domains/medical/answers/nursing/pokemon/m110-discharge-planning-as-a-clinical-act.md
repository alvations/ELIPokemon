---
id: "m110"
slug: discharge-planning-as-a-clinical-act
style: pokemon
category: nursing
difficulty: intermediate
question: "Why is discharge planning a clinical act, and what has to be true before someone can leave safely?"
tags: [discharge, transitions-of-care, medicines-reconciliation, follow-up, readmission]
---

# `Wish` lands on whoever is in the slot two turns later, and names the one who set it.

The third generation has exactly one move that arranges something to happen after the arranger may
be gone, and every detail of how it is implemented is the discharge argument.

```
   case 0: // use wish
       if (gWishFutureKnock.wishCounter[gBattlerAttacker] == 0)
       {
           gWishFutureKnock.wishCounter[gBattlerAttacker] = 2;
           gWishFutureKnock.wishMonId[gBattlerAttacker] = gBattlerPartyIndexes[gBattlerAttacker];
   ...
   case 1: // heal effect
       PREPARE_MON_NICK_WITH_PREFIX_BUFFER(gBattleTextBuff1, gBattlerTarget,
                                           gWishFutureKnock.wishMonId[gBattlerTarget])
       gBattleMoveDamage = gBattleMons[gBattlerTarget].maxHP / 2;
   ──────────────────────────────────────────────────────────────────────────────────────────
   Read the two lines in `case 1` together. `wishMonId` — the party index of whoever made the
   arrangement — is used for ONE THING: printing a name in a message. The size of the benefit
   is `gBattleMons[gBattlerTarget].maxHP / 2`, which is half the maximum HP of WHOEVER IS IN
   THAT SLOT WHEN IT RESOLVES. The counter is indexed by POSITION, not by individual.
```

So: the plan is made by one party member, sized to a different one, delivered to whoever happens
to occupy that place two turns later, and the only trace of the person who set it up is their name
on the paperwork. (This is also the Advance-generation behaviour specifically. The later games
compute the heal from the *wisher's* maximum HP instead, which is the version most people remember
— the generation matters and the code above is Emerald's.)

Put real bars in the slot and the consequence is stark. **Blissey**'s base HP is **255** and
**Magikarp**'s is **20**. A **Wish** set by Blissey that resolves onto a **Magikarp** heals half
of Magikarp's maximum, because `gBattlerTarget` is the slot and not the wisher — the arrangement
was made by the one with the resources and is delivered at the scale of whoever receives it.
Reverse the pair and a Wish set by a Magikarp restores half of Blissey's enormous bar. Neither is
what the one setting it up had in mind, and nothing in the message distinguishes the two cases:
the string names the setter either way, because `wishMonId` is read only to print it.

Markers used below, because this half carries clinical claims. (**mechanism**) follows from the
structure of the transition; (**definitional**) is what the word means; (**consensus**) is
mainstream agreement across major guidance; (**country-dependent**) means the reader's own system
decides. Code blocks carry no marker. No timescale, interval or criterion appears anywhere here.

## The plan resolves after you have gone, and it can arrive at a full bar

Two more conditions in the same pair of functions:

```
   // the end-of-turn check, in TurnBasedEffects
   if (gWishFutureKnock.wishCounter[gActiveBattler] != 0
    && --gWishFutureKnock.wishCounter[gActiveBattler] == 0
    && gBattleMons[gActiveBattler].hp != 0)

   // and in case 1, before the heal lands
   if (gBattleMons[gBattlerTarget].hp == gBattleMons[gBattlerTarget].maxHP)
       gBattlescriptCurrInstr = T1_READ_PTR(gBattlescriptCurrInstr + 2);   // jump: nothing
   ──────────────────────────────────────────────────────────────────────────────────────────
   The arrangement is silently void if the slot's occupant has nothing left to receive it, and
   it is silently void if they need nothing. Neither outcome is reported to the one who set it
   up, because by then the turn belongs to somebody else.
```

That is a follow-up appointment, and it is also an outstanding result. A pending investigation at
discharge is an open loop that closes only if a **specific person** is named with a **specific
action**, because the team that ordered it has dispersed, the receiving clinician did not order it
and may not know it exists, and the filing system does not distinguish "seen and normal" from
"never opened". (**consensus**) Unowned results are a repeatedly reported source of serious harm,
including missed malignancies, and the mechanism is structural rather than careless. It is m073's
collapse again, relocated to a results inbox.

The engine's own answer to this problem is worth noticing, because it is the right one:

```
   struct WishFutureKnock
   {
       u8  futureSightCounter[MAX_BATTLERS_COUNT];
       u8  futureSightAttacker[MAX_BATTLERS_COUNT];
       s32 futureSightDmg[MAX_BATTLERS_COUNT];
       u16 futureSightMove[MAX_BATTLERS_COUNT];
       u8  wishCounter[MAX_BATTLERS_COUNT];
       u8  wishMonId[MAX_BATTLERS_COUNT];
       u8  weatherDuration;
       u8  knockedOffMons[NUM_BATTLE_SIDES];
   };
   ──────────────────────────────────────────────────────────────────────────────────────────
   Every deferred consequence in the battle lives in ONE named structure: **Future Sight** and
   **Doom Desire**, the pair whose damage is computed at the instant of use — m044's and m068's
   device — each with its own attacker and move recorded; the **Wish**; the field clock m107 is
   built on; and **Knock Off**'s record of what has been taken. Nothing deferred is stored
   anywhere else in the engine. That struct is a discharge summary, and it works because there
   is exactly one of it and every field says who set the thing and what it was for.
```

And one species carries the whole struct. **Jirachi** learns **Wish** at level **1**, **Future
Sight** at **40** and **Doom Desire** at **50** — every move in `WishFutureKnock` except the
weather clock, on one level-up learnset. A kit made entirely of consequences that arrive after the
turn they were arranged in.

A summary that reaches the receiving team after the first community contact has failed however
good it is, and the content and deadline are specified in most systems and differ in both.
(**country-dependent**)

## Three ways out, three stored destinations, none of them chosen at the door

This is the part the games model better than anything else in the subject. Where you end up when
you leave is not a decision made as you leave. It is a value that was written earlier, by an event
you may not have noticed.

```
   the exit          where it sends you                       who wrote that destination, and when
   ───────────────── ──────────────────────────────────────── ──────────────────────────────────
   Teleport          SetWarpDestinationToLastHealLocation()   SetLastHealLocationWarp, the last
   (the field move)  = gSaveBlock1Ptr->lastHealLocation       time you were looked after
   ───────────────── ──────────────────────────────────────── ──────────────────────────────────
   Escape Rope,      SetWarpDestinationToEscapeWarp()         UpdateEscapeWarp — and ONLY when
   and Dig           = gSaveBlock1Ptr->escapeWarp             you stepped from an OUTDOOR map
                                                              into a non-outdoor one
   ───────────────── ──────────────────────────────────────── ──────────────────────────────────
   Fly               SetWarpDestinationToHealLocation(        a FLAG_VISITED_* flag, set when
                     sMapHealLocations[mapSecId][2])          you first arrived there on foot
   ─────────────────────────────────────────────────────────────────────────────────────────────
   Three exits. Three different stored values. Not one of them is computed from the situation
   you are in when you use it.
```

Each of the three carries a clinical point and they are different points.

**Teleport goes to the last place that looked after you**, whatever has happened since, and it is
refused outright unless the current map type is one of exactly four — `MAP_TYPE_ROUTE`,
`MAP_TYPE_TOWN`, `MAP_TYPE_OCEAN_ROUTE`, `MAP_TYPE_CITY`, in
`Overworld_MapTypeAllowsTeleportAndFly`. The route out is a property of where you are standing,
not of your ability to take it.

**Escape Rope goes to the door you came in by** — and `UpdateEscapeWarp` only rewrites that value
on an outdoor-to-indoor step. Enter one building from inside another and nothing updates it, so
the rope delivers you to an entrance belonging to somewhere you left a while ago. That is the
discharge address recorded on admission and never revised, and it is why the function is gated on
`gMapHeader.allowEscaping`, a per-map boolean: `CanUseDigOrEscapeRopeOnCurMap()` returns that flag
and nothing else, and the refusal when it is clear is the game's generic can't-use-it message,
which tells you nothing about why.

**Fly cannot send you anywhere you have never been.** `GetMapsecType` has sixteen hand-written
cases, every one of them `FlagGet(FLAG_VISITED_<town>) ? MAPSECTYPE_CITY_CANFLY :
MAPSECTYPE_CITY_CANTFLY`. The destination has to have been established first, by a separate
earlier act, or it is simply not selectable. And when it is selectable, the row it indexes is a
heal location rather than a map coordinate. **Lilycove City**'s row reads
`HEAL_LOCATION_LILYCOVE_CITY`, **Fallarbor Town**'s reads `HEAL_LOCATION_FALLARBOR_TOWN`, and
**Sootopolis City**'s reads `HEAL_LOCATION_SOOTOPOLIS_CITY` — each town pointing at its own
healing point — while **Littleroot Town**'s reads
`HEAL_LOCATION_LITTLEROOT_TOWN_BRENDANS_HOUSE_2F`: a named bedroom on the first floor of a named
house. **You arrive at the place that provides the care, and the array says which place that is.**

That whole table is the fourth condition of a safe discharge: the destination exists, is agreed,
and is ready **before** departure. A referral made on the day of discharge is not a destination.
(**consensus**) And it is the time-constant argument for starting on admission: arranging a
package of care, equipment, an adaptation or a placement takes longer than an acute illness
resolves, and the steps are sequential and belong to other organisations — so a plan begun after
the clinical problem is settled makes the stay the illness *plus* the arrangement, with every
extra day carrying its own hazards: deconditioning (m072), hospital-acquired infection (m036), a
device nobody reviewed (m038), delirium, and a falls risk in an unfamiliar room (m040).
(**mechanism**, **consensus**) An early expected date of discharge is not a prediction. It is a
device for making the arrangement run in parallel with the treatment.

## What the save file does not model, and it is most of the plan

Six functions are withdrawn simultaneously at the door, and the cartridge has an object for one of
them.

```
   function withdrawn at discharge    the engine's nearest equivalent
   ─────────────────────────────────  ────────────────────────────────────────────────────────
   continuous observation             nothing. m109 is the argument; the monitor simply stops
   medicines, administered by        nothing. A held item is in the slot or it is not, and no
   someone else                       mechanic models somebody else putting it there
   an escalation route that answers   nothing
   mobility and personal care         nothing
   nutrition                          nothing — m039 makes the same observation about Leftovers
                                      and a Pokémon holding nothing
   results pending                    `gWishFutureKnock`, and only this one
   ─────────────────────────────────────────────────────────────────────────────────────────
   One of six. The analogy carries the deferred-consequence half of discharge planning well and
   carries the rest not at all, which is worth stating here rather than at the end.
```

So the remaining conditions have to be said flat. The medicines have to be reconciled against what
the person took before, every change explained with its reason recorded, the supply has to exist,
and there has to be an honest answer to whether this person or their carer can actually administer
it — because admission and discharge are the points where medication discrepancies cluster, and
the list changes *and* the administrator changes at the same moment. (**consensus**) m003 holds
the systems argument and m043 the adherence one. Function has to be assessed against the person's
own stairs and their own chair rather than a flat ward floor. Follow-up has to be booked with its
purpose understood, with explicit safety-netting — what to look out for, what to do, who to
contact — and m012 is the full argument on what separates a safety-net that works from reassurance
that sounds like one.

And three structural failure modes, because they are not errors of carefulness. **"Medically fit
for discharge"** does real work and also quietly reclassifies mobility, continence, cognition, who
is at home and whether there is food as *not clinical* — and those are the terms that determine
whether the person comes back. (**mechanism**) **Timing**: discharges late in the day and at the
end of the week are associated with worse outcomes in several systems, because pharmacy,
equipment, transport, community services and the person's own general practice are variously
closed. (**consensus**) **Readmission as a metric** is a genuine signal of planning failure and is
also confounded by severity, by local access and by coding, so a low rate may mean good planning
or a community service that cannot admit anyone. (**consensus**) It generates questions; it does
not answer them.

## Where the metaphor stops

Discharge is a day with an enormous amount riding on it and no clinical drama at all, which is
exactly why it gets delegated downward and compressed into an afternoon. None of what follows has
a mechanic and none of it should.

Most people want to go home, and want it strongly enough to understate how they will manage. "I'll
be fine" is said sincerely by people who will not be fine, because home is where they want to be
and because being a burden is something most people will accept real risk to avoid. Taking that at
face value is not respect for autonomy; it is declining to do the assessment. Taking it seriously
means asking about specifics — the stairs, the bathroom, the shopping, who is actually there on a
Tuesday — which produces a different and far more useful answer.

Families and carers are frequently the plan without having agreed to be. A relative told what has
been arranged, rather than asked what they can do, often says yes in the room and cannot sustain
it, and that is where arrangements break down in the first fortnight. In many systems carers are
entitled to an assessment of their own, and the proportion who receive one is low.

There is distress in both directions. Being kept in when you are ready is its own harm and is
experienced as being trapped. Being sent home before the support exists is frightening and is
commonly experienced as having been pushed out. And people are discharged to residential care
after an admission that began as something small — a permanent change to someone's life, decided
in a week, by people they met a fortnight ago. That is a reason to involve them properly and
early, not a reason to avoid the decision.

Where someone wishes to leave against advice, or where there is a question about whether they can
make that decision, the subject moves into capacity, consent and sometimes safeguarding. That is a
legal framework, it differs profoundly between countries, it is not settled at a bedside, and
nothing built out of a video game should be used to reason about it — the reader's own law and
local safeguarding route are the only authority. One practical point does generalise: someone
leaving against advice still needs the plan, the medicines and the safety-netting, and withholding
them as a consequence of the decision is indefensible.

And the context: discharge planning fails mostly for structural reasons. The plan lives in several
systems, community services are commissioned separately, the summary is written by the person with
the least time, and nobody owns the week afterwards. An institution that answers a readmission by
asking ward staff to plan better, without changing any of that, has identified the wrong variable.

## What Nurse Joy is listening for

What changes at the door, function by function. The time-constant argument for starting on
admission, and why an early expected date is a parallelism device and not a prediction. The seven
conditions, with medicines reconciliation and outstanding results expanded. Why an unowned result
is an open loop and what closes it. Why "medically fit" is necessary and not sufficient. Why
late-in-the-day and end-of-week discharges carry extra risk. Why readmission is a confounded
metric. What a usable summary contains and when it has to arrive. Who the plan assumes will do
things, and whether they were asked. And the local answers: who coordinates discharge, what the
documentation is, how outstanding results are owned, what a carer is entitled to, and what the
legal framework is for someone leaving against advice.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to
this answer:

* The reader's **national guidance on transition between inpatient care and community or care-home
  settings**, which is among the most country-specific documents in this directory.
* The reader's institutional discharge policy, including who coordinates, the documentation, any
  criteria-led discharge arrangements, and the process for outstanding results.
* The reader's national standards for the content and timeliness of a discharge summary.
* The reader's institutional policy on medicines reconciliation at discharge, and the national
  formulary for anything about a specific medicine.
* The reader's own legal framework on capacity and consent, and the local safeguarding route, for
  discharge against advice and for decisions about where someone will live. This is law.
* The published literature on unowned test results and on post-discharge adverse events, which
  rests on audit and observational evidence.
* The literature on readmission as a quality indicator, for the confounding argument.
* The reader's local carers' assessment provisions, which are statutory in some countries and
  absent in others.

The Pokémon material is from the **pret/pokeemerald** decompilation of Pokémon Emerald:
`Cmd_trywish`, whose two cases are quoted above, is in `src/battle_script_commands.c`; the
end-of-turn Wish check and `TurnBasedEffects` are in `src/battle_util.c`, `struct WishFutureKnock`
is in `include/battle.h`, `SetWarpDestinationToLastHealLocation`,
`SetWarpDestinationToEscapeWarp`, `SetWarpDestinationToHealLocation`, `UpdateEscapeWarp` and
`Overworld_MapTypeAllowsTeleportAndFly` are in `src/overworld.c`, `SetUpFieldMove_Teleport` is in
`src/fldeff_teleport.c`, `CanUseDigOrEscapeRopeOnCurMap` and `ItemUseOutOfBattle_EscapeRope` are
in `src/item_use.c`, and `GetMapsecType` with `sMapHealLocations` are in `src/region_map.c`, and
Jirachi's and Blissey's and Magikarp's entries are in `src/data/pokemon/level_up_learnsets.h` and
`src/data/pokemon/species_info.h`. The statement that later generations compute Wish from the
wisher's maximum HP is **not** from this code and is named as a generational difference rather
than quoted from a source.

## Scope and safety

This explains why discharge is a clinical decision and what has to be true before it is safe,
using a game's deferred-effect and exit mechanics, at the level of someone already training in or
qualified for clinical practice. It is not a discharge checklist, not a local process and not a
basis for deciding whether any particular person is ready to leave. It states no timescale, no
interval and no criterion, because discharge processes, documentation standards and the roles
involved differ more between countries than almost anything else in this directory. Nothing here
has had clinical review. Decisions about capacity, about discharge against advice and about where
someone will live belong to the reader's own legal framework and local safeguarding route, and are
named here rather than explained. Nothing here is for use in an emergency or for a decision about
any person's care. If someone is unwell right now, the local emergency number is the correct
response.

## Where this stands, October 2026

The mechanical material is fixed, and so is the structural argument: six functions are withdrawn
at once, the time constant of arranging support exceeds that of an acute illness, and an unowned
result is an open loop. Almost everything else moves, and moves differently by country — where the
boundary between hospital and community sits, who commissions and pays for post-discharge support,
whether discharge-to-assess or similar models are in use, the standards for summary content and
timeliness, and the role titles of the people who coordinate it have all changed repeatedly in the
last decade. The electronic layer — shared records, automated summaries and
results-acknowledgement systems — is moving fastest, and its failure modes are not yet as well
characterised as the paper ones were. The reader's national transitions guidance, institutional
discharge policy and legal framework are the authority throughout.
