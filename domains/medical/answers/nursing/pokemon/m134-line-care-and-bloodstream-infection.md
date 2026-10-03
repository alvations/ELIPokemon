---
id: "m134"
slug: line-care-and-bloodstream-infection
style: pokemon
category: nursing
difficulty: advanced
question: "What is the dressing on a vascular access device actually protecting, and why is a care bundle measured as all-or-none rather than element by element?"
tags: [vascular-access, care-bundles, infection-prevention, dressings, surveillance]
---

# Two routes in, one barrier, and the second is covered only where someone wrote a check.

Emerald has a side-wide barrier against status, and the exact text of its checks — plural, and
that is the point — is the best short statement in the cartridge of what a line dressing is and is
not. It protects a side. One shared condition covers one class of arrival. Everything else it
covers, it covers because somebody wrote the check again by hand, ten times, in ten separate
places. And what it misses is not a stronger version of the same thing but a different route in,
which is why pushing harder on the barrier does not close it.

m038 holds the argument that duration is the dominant term for any indwelling device, and it hands
this answer the duration term and the daily review of whether the device is still wanted. What is
left is what happens while it is still justified.

Markers used below, because this half carries clinical claims. (**mechanism**) means it follows
from the structure; (**definitional**) is what the word means; (**consensus**) is mainstream
agreement across major guidance; (**country-dependent**) means the reader's own national guidance
or local policy decides, which here covers every number. Code blocks carry no marker. No dwell
time, dressing interval, antiseptic agent or concentration, scrub duration or infection rate
appears anywhere here.

## One barrier, two routes, and the condition that decides which is covered

```
   // src/battle_script_commands.c — the ONE shared site, where BOTH protections are tested:
   if (... ability == ABILITY_SHIELD_DUST && !(gHitMarker & HITMARKER_STATUS_ABILITY_EFFECT)
       && !primary && gBattleCommunication[MOVE_EFFECT_BYTE] <= 9)
       INCREMENT_RESET_RETURN

   if (gSideStatuses[...] & SIDE_STATUS_SAFEGUARD && !(gHitMarker & HITMARKER_STATUS_ABILITY_EFFECT)
       && !primary && gBattleCommunication[MOVE_EFFECT_BYTE] <= 7)
       INCREMENT_RESET_RETURN
   ──────────────────────────────────────────────────────────────────────────────────────────
   Read the conditions, because the usual summary of this pair is wrong. BOTH clauses carry
   `!primary` and both are excused by HITMARKER_STATUS_ABILITY_EFFECT; they differ only in an
   effect-byte ceiling, 9 against 7 — m103's figures. So at this site neither protection
   covers a status applied as a move's PRIMARY effect, and neither covers one sourced from an
   Ability: Effect Spore, Poison Point and Flame Body walk through both, intact and working
   exactly as written.
```

So how does **Safeguard** stop **Will-O-Wisp**, which it does? Not here. It stops it because
somebody wrote the check again, by hand, inside that move's own script:

```
   BattleScript_EffectWillOWisp::
       ...
       accuracycheck BattleScript_ButItFailed, ACC_CURR_MOVE
       jumpifsideaffecting BS_TARGET, SIDE_STATUS_SAFEGUARD, BattleScript_SafeguardProtected
       attackanimation
       setmoveeffect MOVE_EFFECT_BURN
       seteffectprimary                 ◄── and by here the shared `!primary` test is useless
   ──────────────────────────────────────────────────────────────────────────────────────────
   There are TEN such hand-written jumps in data/battle_scripts_1.s, and here is the whole
   list: the Sleep, Toxic, Confuse, Poison and Paralyze effect scripts, Swagger's and
   Flatter's confusion branches, Will-O-Wisp, Yawn, and Teeter Dance — which gets its own
   label, BattleScript_TeeterDanceSafeguardProtected. Shield Dust has ZERO sites in the
   scripts. Its only existence is the shared `!primary` clause above.
```

Which turns the device into something sharper than "one barrier, one route". **The barrier's
coverage of the second route exists only where someone wrote the check by hand, act by act** —
it is a hand-maintained list, which is m075's `sSoundMovesTable` shape, and the eleventh entry
nobody added is simply not covered. m103's reading of these same ten sites is the
prevention-as-refusal-at-entry argument; this is the same ten sites read as a coverage map.

The clinical structure is identical and it is the thing most often lost. Organisms reach the
bloodstream **along the outside of the catheter**, from the patient's own skin flora tracking down
the device surface through the subcutaneous track, or **along the inside of the lumen**, from the
hub, the connector, the administration set, the infusate and the hands at access
(**mechanism**). Extraluminal arrival generally predominates with short dwell and intraluminal
arrival as dwell lengthens and access events accumulate (**consensus**, from observational and
microbiological evidence rather than from mechanism alone).

```
   route                     what the dressing does about it     what acts on it instead
   ───────────────────────── ─────────────────────────────────── ──────────────────────────────
   EXTRALUMINAL               everything it does. This is its     skin antisepsis at insertion,
                              entire job                          securement, site selection
   ───────────────────────── ─────────────────────────────────── ──────────────────────────────
   INTRALUMINAL               NOTHING. The hub is outside the     hub decontamination before
                              dressing and outside its reach      every access, aseptic
                                                                   technique, set management,
                                                                   fewer access events
   ─────────────────────────────────────────────────────────────────────────────────────────────
   So an institution with immaculate insertion practice and a rising rate is auditing the
   covered route. Safeguard is up. The status is arriving from an Ability.
```

That last line is mechanism rather than guidance: a barrier that covers one route cannot be made
to cover the other by being applied more carefully, and no amount of auditing the covered route
closes the uncovered one (**mechanism**).

## `Cmd_setsafeguard` fails rather than refreshing, which is exactly what a lifted dressing is

```
   static void Cmd_setsafeguard(void)
   {
       if (gSideStatuses[GET_BATTLER_SIDE(gBattlerAttacker)] & SIDE_STATUS_SAFEGUARD)
       {
           gMoveResultFlags |= MOVE_RESULT_MISSED;              ◄── it FAILS
           gBattleCommunication[MULTISTRING_CHOOSER] = B_MSG_SIDE_STATUS_FAILED;
       }
       else
       {
           gSideStatuses[...] |= SIDE_STATUS_SAFEGUARD;
           gSideTimers[...].safeguardTimer = 5;
           gSideTimers[...].safeguardBattlerId = gBattlerAttacker;
       }
   }
   ──────────────────────────────────────────────────────────────────────────────────────────
      Using it again while it is up does NOT top up the timer. The timer stays wherever it was,
   the turn is spent, and the only output is a failure string. `Cmd_setreflect` is written
   identically, and m090 found the same shape in the same function family. A barrier is up or
   it is not; there is no partial state and no reinforcement.
```

That is the single most useful thing to take from this answer to a bedside. **A lifted dressing is
not a partial dressing.** The barrier is intact or it is not, and taping over a loose edge
restores the appearance and not the function — because what makes the dressing work is a
continuous seal over a wound, and the seal is a binary (**mechanism**). Worse, moisture trapped
under an occlusive dressing is more dangerous than the same moisture in the open, since the
occlusion is precisely what turns it into a culture medium (**mechanism**).

Which is why **integrity rather than the calendar** is what makes a dressing need changing, with
the scheduled change as a backstop for one that has stayed intact (**consensus**; the schedule
itself is (**country-dependent**)). And why the usual choice is a transparent semipermeable
dressing: the skin at the site is the thing being inspected, and the whole design requirement is
to make looking at it cheap enough that it happens (**consensus**). The dressing's third and
least-taught job is **securement** — micromotion at the site disrupts the track and draws
organisms along it, so a device that moves is a device being inoculated (**mechanism**).

## Insertion is an Ability. Maintenance is a check that runs at every access.

Part I's device, and it is the right one, because the asymmetry it names is the whole difference
between the two halves of a line bundle.

```
   how the weather got there        when it acts                   the clinical counterpart
   ──────────────────────────────── ────────────────────────────── ───────────────────────────
   Drizzle, on Kyogre's switch-in    ONCE, and the rain PERSISTS    the INSERTION bundle: hand
                                     after Kyogre has left the      hygiene, maximal barrier
                                     field entirely                 precautions, an alcoholic
                                                                     antiseptic preparation,
                                                                     site selection, a sterile
                                                                     field. Performed once; its
                                                                     effect runs for the whole
                                                                     dwell
   ──────────────────────────────── ────────────────────────────── ───────────────────────────
   Rain Dance, as a move             every use, with its own        the MAINTENANCE bundle: hub
                                     timer, by whoever is in        decontamination before every
                                     front of you now               access, aseptic technique,
                                                                     dressing integrity, set
                                                                     management, fewer accesses
   ─────────────────────────────────────────────────────────────────────────────────────────────
   One is an event performed by a small number of identifiable people under observation. The
   other is a habit distributed across everyone who touches the device, on every shift, for
   weeks. Compliance with the first is easy to audit and comparatively easy to improve.
```

The asymmetry is structural: an act performed once by identifiable people under observation and an
act repeated indefinitely by everyone on every shift have different failure rates whatever either
bundle contains (**mechanism**).

And the reason the second is genuinely harder is m067's finding doing a second job that fits:
`AtkCanceler_UnableToUseMove` re-runs its whole fourteen-case chain **every turn**, and a pass on
one turn is not evidence about the next. Hub decontamination has that structure exactly: each
access is an independent event, and a hub that was clean this morning is not a statement about
this access (**mechanism**). The failure mode is that staff reason from the state of the device
rather than from the state of this particular act.

## All-or-none, in `Rock Slide`'s accuracy — and the engine's own silent version

A bundle is a small set of evidence-based elements applied together and measured as **all-or-none
compliance**: an episode counts only if every element was performed (**definitional**). The
arithmetic is the entire argument, and `Rock Slide` supplies a concrete number to do it with.

```
   Rock Slide: .power = 75, .accuracy = 90, .target = MOVE_TARGET_BOTH
   The accuracy check is  (Random() % 100 + 1) > calc  →  a miss.

   five independent checks, each at Rock Slide's accuracy:
       one            0.9
       two            0.81
       three          0.729
       four           0.656
       FIVE           0.59        ◄── a little under three in five
   ─────────────────────────────────────────────────────────────────────────────────────────────
   Five elements, each individually respectable, and the product is nothing like the average.
   This arithmetic is about the game's number, not anybody's audit figure. What transfers is
   the shape: the patient experiences the PRODUCT, so element-by-element reporting hides
   exactly the thing a bundle exists to deliver, and the gap widens with every element added.
```

The product-not-the-average point is mechanism, and it is the whole case for the measure
(**mechanism**).

And the engine has its own all-or-none, which fails in the way that matters most — silently:

```
   static void CreateShedinja(u16 preEvoSpecies, struct Pokemon *mon)
   {
       if (gEvolutionTable[preEvoSpecies][0].method == EVO_LEVEL_NINJASK
           && gPlayerPartyCount < PARTY_SIZE)
       {
           ... the whole Shedinja is built here ...
       }
   }                        ◄── and if either condition is false: NOTHING. No message, no
                                failure string, no record that anything was supposed to happen
   ──────────────────────────────────────────────────────────────────────────────────────────
   Two conditions, both required, and one of them — a free party slot — is a property of the
   CONTEXT rather than of the act being performed. The evolution proceeds, the player sees
   Ninjask, and the second outcome simply does not occur.

   Checked in src/evolution_scene.c rather than recalled, because the spare Poké Ball that
   everyone remembers is a LATER generation's requirement: Emerald's version tests the
   evolution method and the party count, and nothing else.
```

Two further things the all-or-none measure is doing, which the arithmetic alone does not show. It
makes the absence of an element **visible as a defect** rather than as a difference of opinion —
some elements are weakly evidenced on their own, and the point is that the set is applied
consistently and that deviation becomes something to explain (**consensus**). And it is a measure
of a **system**, not a grade for a person: used punitively it produces documentation compliance,
which is the one failure mode the measure cannot detect from its own data (**mechanism**).

## Five fields in `struct SideTimer` record who set it. The sixth does not.

This is the difference between the two definitions of a line infection, and it is sitting in one
struct in `include/battle.h`.

```
   struct SideTimer
   {
       u8 reflectTimer;      u8 reflectBattlerId;        ◄── attributed
       u8 lightscreenTimer;  u8 lightscreenBattlerId;    ◄── attributed
       u8 mistTimer;         u8 mistBattlerId;           ◄── attributed
       u8 safeguardTimer;    u8 safeguardBattlerId;      ◄── attributed
       u8 followmeTimer;     u8 followmeTarget;          ◄── attributed
       u8 spikesAmount;                                  ◄── NO id. NO timer. Just a count.
   };
   ──────────────────────────────────────────────────────────────────────────────────────────
   Five side effects store a battler id so the engine can say WHO. Spikes stores a number so
   the engine can say HOW MANY, and nothing else — which is m036's and m105's point arriving
   in a place you can read it as one line of a header file.
```

```
   the definition                    which field it is            what it is designed for
   ───────────────────────────────── ───────────────────────────── ─────────────────────────────
   CATHETER-RELATED bloodstream       safeguardBattlerId. It        deciding what is wrong with
   infection — a clinical and         demands attribution: the      this patient and what to do
   microbiological diagnosis          infection is tied to the      about the device
                                      device by evidence
   ───────────────────────────────── ───────────────────────────── ─────────────────────────────
   CENTRAL LINE ASSOCIATED            spikesAmount. It counts       counting comparably across
   bloodstream infection — a          qualifying events in          wards, hospitals and
   surveillance definition            patients who have a line,     countries, applied by people
                                      without requiring the device  who were not there
                                      to be proven the source
   ─────────────────────────────────────────────────────────────────────────────────────────────
   Two different objects answering two different questions, and they do not produce the same
   number. The surveillance definition is deliberately mechanical, which
   means it includes infections the device did not cause and excludes some it did. A rate
   therefore moves when the DEFINITION changes, when ascertainment changes, and when blood
   culturing practice changes — none of which is a change in how well lines are cared for.
```

Two definitions of one event producing two different numbers follows from what each was built for
(**definitional**); that a rate moves when the definition, the ascertainment or the culturing
practice moves is mechanism (**mechanism**); and both definitions, with the national programme
that uses them, are set locally and revised (**country-dependent**).

So a falling rate is evidence of something and proof of nothing, and a rate compared between two
institutions compares two ascertainment systems at least as much as two sets of practice. The
third device worth naming here is m101's: `MOVE_RESULT_NO_EFFECT` is a composite bit that erases
three unrelated causes, and one reported figure covering both routes into a bloodstream behaves
the same way.

## Where the metaphor stops

A line infection is a serious event and nothing in a game stands for it. It means bacteraemia in
somebody who is usually already unwell; it often means removing and replacing access that was
difficult to obtain in the first place; it means a prolonged course of treatment and a longer
stay. It is also substantially preventable, and that combination is what gives this subject its
weight.

The person at the other end is frequently someone whose life depends on that access continuing to
work: someone on long-term parenteral nutrition, someone having chemotherapy, someone on dialysis,
a child who has had many lines and is running out of sites. For them a central line is not a
clinical object. It is a part of their body that they live with, protect, travel with, sleep
awkwardly because of, and know a great deal about — commonly more than whoever is accessing it on
a given shift knows. The most useful practical habit in the whole subject is to ask how their line
is usually handled, and the commonest insult is to override the answer. People with long-term
access also carry a reasonable fear of losing it, and that fear is a clinical fact about the
consultation rather than a personality trait.

Two things about how this is discussed. Zero-tolerance framing has driven real improvement and it
has a cost: where a rate is a performance measure, pressure falls on ascertainment as well as on
practice, and the person who orders the blood culture that finds an infection is the person who
creates the number. And when an infection does occur, treating it as an individual failure in a
distributed, interruption-driven process is both unjust and ineffective — the maintenance half is
spread across everyone on every shift, which is exactly why blame cannot locate the defect.

And the context, because it governs everything above. Hub decontamination before every access,
aseptic technique and the time to do a dressing properly are time-dependent tasks performed under
interruption. An institution that answers its line infection rate with a teaching session, having
changed neither the staffing nor the number of access events a patient receives, has identified
the wrong variable.

## What Nurse Joy is listening for

The two routes, their separate interventions, and which predominates when. Why perfect insertion
practice with a rising rate means you are auditing the covered route. The three jobs of the
dressing and the one thing it does nothing whatever about. Why a lifted dressing is not a partial
one, and why occluded moisture is worse than open moisture. Securement, and the micromotion
mechanism behind it. The insertion bundle and the maintenance bundle as different objects, and
which is harder and for what structural reason. The arithmetic of all-or-none compliance, and the
two further things the measure is doing. The difference between the clinical and the surveillance
definition, and the three ways a rate moves with no change in practice. Why a culture drawn
through the device answers a different question — m132 is the argument. And the local answers:
which antiseptic, which dressing, which intervals, who may access what, and which surveillance
definition is currently in force.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to
this answer:

* The reader's **national guidance on preventing infection associated with intravascular
  devices**, which sets the insertion and maintenance elements, the antiseptic preparation, the
  dressing choice and the review requirements. It differs by country and is revised.
* The reader's **institutional vascular access policy**: which devices may be inserted and
  accessed by whom, the local dressing and administration set intervals, and the escalation route
  for a suspected line infection.
* The reader's **national healthcare-associated infection surveillance programme's definitions and
  protocol** — the document that says what is counted and how, and therefore what the local rate
  means. It is the authority on the surveillance definition and it changes.
* The reader's national microbiology guidance on investigating suspected device-related
  bacteraemia, for what is required of the cultures and how a result is interpreted.
* The published literature on central line bundles and their implementation, including the
  collaborative improvement programmes, whose results and the debate about attributing them are
  both worth reading.
* A current textbook of infection prevention and control, for the route mechanisms and the
  definitional material.

The Pokémon material is from the **pret/pokeemerald** decompilation of Pokémon Emerald: the
Safeguard check site with its `HITMARKER_STATUS_ABILITY_EFFECT` condition, the Shield Dust clause
behind `!primary`, `Cmd_setsafeguard`, and `Rock Slide`'s accuracy check in
`src/battle_script_commands.c`; `Rock Slide`'s data in `src/data/battle_moves.h`;
`AtkCanceler_UnableToUseMove` in `src/battle_util.c`; `struct SideTimer` in `include/battle.h`;
and `CreateShedinja` in `src/evolution_scene.c`. The Shedinja conditions and the Safeguard /
Shield Dust pair were read in the source rather than recalled — the first because the Poké Ball
requirement people remember belongs to a later generation, the second because both halves of it
are counter-intuitive.

## Scope and safety

This explains what a vascular access dressing protects and why bundles are measured as
all-or-none, through a game's status-barrier and evolution code, at the level of someone already
training in or qualified for clinical practice. It is not a vascular access policy, not an
insertion or dressing procedure, and not a guide to diagnosing or managing any infection. It
deliberately states no dwell time, dressing change interval, antiseptic agent or concentration,
scrub duration, administration set interval or infection rate, because every one of those is set
by the reader's national guidance and institutional policy, which are the authority. It is not a
basis for any decision about whether a device should be removed, nor for starting, changing or
withholding any treatment. Nothing here has had clinical or microbiological review. Nothing here
is for use in an emergency or for a decision about any person's care. If someone is unwell right
now, the local emergency number is the correct response.

## Where this stands, October 2026

The mechanical material is fixed, and the route distinction and the all-or-none arithmetic are
structural and do not date. What moves often is everything procedural: antiseptic preparations,
dressing types including antimicrobial-impregnated ones, needleless connector design and
disinfection method, administration set intervals and the evidence for locking solutions are all
active areas, and the recommendations differ by country at any given moment. The surveillance
definitions move too, and a rate reported under a revised definition is not comparable with the
one before it — which is why neither is named here. The one durable direction of travel is the
shift of attention from insertion, where practice is now generally good, toward maintenance and
toward reducing the number of access events a device receives, which is the term this answer's
structure predicts should matter most. The reader's national guidance, institutional policy and
surveillance programme are the authority throughout.
