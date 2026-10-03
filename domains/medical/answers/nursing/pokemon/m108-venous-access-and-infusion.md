---
id: "m108"
slug: venous-access-and-infusion
style: pokemon
category: nursing
difficulty: advanced
question: "Why are the line, the rate and the fluid three separate decisions in intravenous therapy, and what goes wrong when they are made as one?"
tags: [intravenous, fluids, infusion-rate, vascular-access, prescribing]
---

# Nine levers set how often. A hand-written partition sets what is reachable.

m082 found the cleanest separation of these two questions in the cartridge and this answer borrows
it outright, because the clinical structure is identical. `WildEncounterCheck` is the **rate**
pipeline, and every line of it changes *how often* something happens: `encounterRate *= 16`, then
×80/100 on the **Mach Bike** or **Acro Bike**, then the **White Flute** and **Black Flute** mod,
then a **Cleanse Tag** at ×2/3, then six hand-written branches on the ability of party slot 0 —
**Stench** at ÷2 (×3/4 on the Battle Pyramid floor), **Illuminate** at ×2, **White Smoke** at ÷2,
**Arena Trap** at ×2, and **Sand Veil** at ÷2 in a sandstorm — and finally a hard cap of 2,880.
Nine levers on one number, and not one of them alters a single slot in the table. The **table**
decides *what*.

Fishing is where the engine states the second half as code, and the detail is worth having in
full:

```
   static u8 ChooseWildMonIndex_Fishing(u8 rod)
   {
       u8 rand = Random() % max(max(..._OLD_ROD_TOTAL, ..._GOOD_ROD_TOTAL),
                                ..._SUPER_ROD_TOTAL);
       switch (rod)
       {
       case OLD_ROD:    ... wildMonIndex = 0;  else 1;             // slots 0-1
       case GOOD_ROD:   ... 2, 3 or 4;                             // slots 2-4
       case SUPER_ROD:  ... 5, 6, 7, 8 or 9;                       // slots 5-9
   ──────────────────────────────────────────────────────────────────────────────────────────
   ONE random draw. THREE disjoint partitions of the same ten-slot table, hand-written, with
   no overlap at all. The number drawn is identical whichever rod is held; the rod decides
   which part of the table that number is allowed to mean. An **Old Rod** cast ten thousand
   times never once reaches slot 5.
```

Put real species in the slots and it stops being abstract. **Sootopolis City**'s fishing table
holds **Magikarp** in slots 0 through 6 and **Gyarados** in slots 7, 8 and 9. An Old Rod reads
slots 0 and 1. You can cast it in that water until the cartridge wears out and you will never once
meet a Gyarados — not rarely, never — while the **Super Rod** draws nothing else, and the **Good
Rod** in between, reading slots 2 to 4, draws Magikarp every time. **Route 118** makes the same
point with a different pair: slots 0 and 1 are a level 5-to-10 Magikarp and **Tentacool**, and
slot 5 is a **Sharpedo** at level 30 to 35. The rod is the whole difference between those
outcomes, and the water is identical.

That is the access decision, exactly. The conduit does not change what is in the water and does
not change how often you get a bite. It changes **what can be reached**, and it does so by a
hand-written rule that nothing about the fish can overcome. m030 and m013 use the same three rods
for probability and for the difference between sweeping on purpose and meeting something by
accident; this is the third job the same object does, and the slot ranges are m082's.

Markers used below, because this half carries clinical claims. (**mechanism**) means it follows
from physics or physiology; (**consensus**) is mainstream agreement across major guidance;
(**country-dependent**) means the reader's own policy decides. Code blocks carry no marker. No
rate, volume, concentration, gauge or dwell time appears anywhere here.

## What the line decides, and the fact everybody gets backwards

Peripheral veins tolerate solutions near physiological osmolarity and pH. Solutions well outside
that range, and agents that injure tissue if they escape the vein, need central access with the
tip in a high-flow vessel so that the infusate is diluted at the moment it arrives.
(**consensus**, **mechanism**) That is a Sharpedo in slot 5, and an Old Rod will not reach it,
however well the cannula is running.

And then the part that is the opposite of the intuition. For laminar flow down a given pressure
gradient, flow rises with the **fourth power of the radius** and falls with the **length**.
(**mechanism**) A short wide peripheral cannula therefore delivers volume *faster* than a long
narrow central catheter. Central access is not fast access, and the time spent obtaining it is
itself a cost in someone who is bleeding.

## The conduit has its own capacity, and it is not the contents' capacity

```
   u8 CalculatePPWithBonus(u16 move, u8 ppBonuses, u8 moveIndex)
   {
       u8 basePP = gBattleMoves[move].pp;
       return basePP + ((basePP * 20 * ((gPPUpGetMask[moveIndex] & ppBonuses) >> (2 * moveIndex)))
                        / 100);
   }
   ──────────────────────────────────────────────────────────────────────────────────────────
   Read the three arguments. The capacity of a slot is computed from the OCCUPANT's base PP
   and from a bonus stored against the SLOT INDEX — two bits per slot, in one byte, for the
   whole moveset. And there is a dedicated `RemoveMonPPBonus(mon, moveIndex)` whose entire job
   is to clear those two bits when the occupant changes.
```

Two facts in one function: the conduit has a finite working life of its own, and that life is a
joint property of the conduit and what is running through it. m034's argument is that PP is the
budget the health bar is not showing; here it is the device-day. m038 holds the full version — the
infection hazard of any indwelling device accrues per device-day, duration is the dominant term,
and the insertion decision is made once while the cost accrues daily. (**consensus**) Expected
duration is therefore a device-selection input, which is why a short cannula, a longer peripheral
catheter, a centrally or peripherally inserted central catheter and a tunnelled device all exist.

The complications belong to the line even when the fluid caused them, which is precisely why these
two decisions get merged. Phlebitis is mechanical, chemical or infective — and the chemical kind
is caused by the contents and recorded against the device. Infiltration is leakage of a
non-vesicant; **extravasation** is leakage of a vesicant, it is a tissue-injury emergency with a
time-critical local management, and it is usually a line decision presenting as a fluid
complication. (**consensus**) The local extravasation policy is the one document in this subject
worth knowing the location of before it is needed.

Here the games have nothing, and saying so is better than inventing something. **No mechanic
models a conduit being damaged by what passes through it.** A move slot is not degraded by the
move in it; PP falls and nothing else happens. The nearest thing is recoil, which m104 uses
properly and which bills the *user* rather than the channel. The chemical-phlebitis and
extravasation mechanisms have no analogue in the cartridge, and they are the half of this topic
that most needs one.

## The rate: the same total, delivered differently, is a different intervention

This is the house device and it is the oldest one in the domain. **Leftovers** restores `maxHP/16`
at the **end of every turn**; a **Sitrus Berry** restores a flat **30** in one instant. m002 and
m005 both turn on the difference, and m005's whole argument is that a ledger of per-turn ticks is
not the same object as a number read off a screen.

```
   delivery          what the engine does                   what the recipient experiences
   ───────────────── ────────────────────────────────────── ────────────────────────────────────
   Leftovers         maxHP/16, end of turn, every turn,     a continuous input, invisible per
                     indefinitely, no announcement          turn, decisive over many
   Sitrus Berry      +30, once, the instant hp <= maxHP/2   a single step, announced, and the
                                                             item is gone
   Sandstorm         maxHP/16, end of turn — the SAME        exactly cancels Leftovers. The net
                     denominator with the sign reversed      is zero and nothing is fine
   ─────────────────────────────────────────────────────────────────────────────────────────────
   Same quantity of HP can arrive three ways. The engine treats them as three different objects
   with three different stores, three different timings and three different messages, because
   they are.
```

The clinical content maps term for term. The body's capacity to accommodate a volume is
rate-limited, so circulatory overload is a **rate** complication rather than a volume one — the
same total can be absorbed uneventfully over hours and cause pulmonary oedema over minutes.
(**mechanism**) The reverse failure is just as real: an inadequate rate in genuine hypovolaemia is
not caution, it is slower treatment of shock. And some agents have harms that are entirely
rate-dependent, with potassium-containing infusions the standard teaching example, which is why
pre-mixed bags exist and why adding concentrated electrolyte at the bedside is restricted or
prohibited in many institutions. (**consensus**; the restrictions are (**country-dependent**).)

The delivery device is a fourth object people forget is in the chain — a gravity set's rate
depends on bag height, limb position and tubing, a volumetric pump delivers the number entered,
and a syringe driver is the wrong instrument for a large volume. Wrong-rate entry and free-flow
are documented harms, and the defence is m003's: double-checking at the point of programming and a
design that makes the dangerous entry hard, not individual carefulness. (**consensus**)

## The bag: three items, one shelf, one price, and a different resource inside

```
   item            price   holdEffect                 holdEffectParam   what it restores
   ─────────────── ─────── ────────────────────────── ───────────────── ────────────────────────
   Oran Berry      20      HOLD_EFFECT_RESTORE_HP     10                HP, flat
   Sitrus Berry    20      HOLD_EFFECT_RESTORE_HP     30                HP, flat
   Leppa Berry     20      HOLD_EFFECT_RESTORE_PP     10                PP — a different
                                                                         resource entirely
   ─────────────────────────────────────────────────────────────────────────────────────────────
   Same price. Same `ITEM_USE_PARTY_MENU`. Same `ITEM_B_USE_MEDICINE` battle usage. Adjacent
   entries in `src/data/items.h`. One of them does not act on the quantity you were watching
   at all.
```

And the params are **flat**, not fractions, which is the m006 and m041 device in one line: a
Sitrus Berry restores the same 30 to **Blissey**, whose base HP is **255**, and to **Shedinja**,
whose base HP is **1**. Identical bag, identical number, completely different meaning.

That is why a litre is not a litre. Tonicity and composition decide which compartment the contents
reach: isotonic crystalloid distributes to the extracellular space, so only a fraction stays
intravascular and the resuscitation volume exceeds the deficit; a glucose solution distributes to
total body water once the glucose is metabolised and is therefore a poor intravascular expander;
balanced crystalloid and isotonic saline occupy the same space with different chloride and buffer
loads, and which is preferable is an active trial literature rather than a settled answer.
(**mechanism**, **consensus**)

The indications are different objects too. A widely used framework separates resuscitation,
routine maintenance, replacement of ongoing losses, redistribution and reassessment — five Rs,
whose wording differs by country. (**consensus**, **country-dependent**) It exists to prevent the
error with the worst history: hypotonic maintenance fluid given at a volume suited to replacement
produces hyponatraemia, the harm is neurological, and in children this has been the subject of
national safety alerts in several countries. (**consensus**)

## The error is almost always a borrowed answer

```
   the question asked          the answer actually used                 the harm
   ─────────────────────────── ──────────────────────────────────────── ───────────────────────
   which line?                 whichever is already in                  extravasation of an
                                                                         agent that needed a
                                                                         slot the rod cannot
                                                                         reach
   how fast?                   whatever the last bag ran at             overload, or
                                                                         under-resuscitation
                                                                         recorded as caution
   which bag?                  whatever is in the cupboard              the wrong compartment,
                                                                         and the hyponatraemia
                                                                         story above
   how fast, for a central      "it's central, so it's fast"            the fourth-power
   line?                                                                 relationship says
                                                                         otherwise
   when do we stop?            nobody owns this one                     an infusion still
                                                                         running after the
                                                                         person started drinking
   ─────────────────────────────────────────────────────────────────────────────────────────────
   Every row is one decision's answer used for a different decision's question. The last row is
   m038's structure again: started once for a good reason, and nothing afterwards asks.
```

## Where the metaphor stops

Cannulation hurts, and it hurts most for the people who need it most. The person with difficult
veins — oedematous, dehydrated, previously treated with chemotherapy, a long-term intravenous drug
user, a child — is the person who gets attempted repeatedly, and the number of attempts is almost
never recorded anywhere. People describe repeated attempts as one of the worst parts of an
admission, and some decline treatment rather than face them again. Most institutions set a limit
on attempts before escalating to someone more skilled or to a different device; knowing the local
one is both a kindness and a clinical competence.

A drip also tethers. It makes walking to the toilet a two-object manoeuvre, makes washing and
dressing awkward, wakes people when the pump alarms, and connects directly to the continence and
falls arguments elsewhere in this specialty — an infusion running overnight is a reason somebody
gets up in the dark holding a stand. None of that appears in the prescribing decision and all of
it is real.

For people on long-term intravenous treatment, the device becomes part of their body and part of
how they manage their life, and they usually know more about its care than the person in front of
them. Asking is not a formality.

And the structural point, because individuals get blamed for it: fluids are prescribed badly
mostly because the three decisions live in three places — a chart, a pump and a bag — and nobody
owns the fourth, which is when to stop. Changing where the review is recorded is the fix.
Retraining individuals is not.

## What Nurse Joy is listening for

The three decisions, and an example of each being right while the combination is wrong. Why
osmolarity, pH and vesicant potential drive the access decision, and why tip position is part of
the prescription rather than a radiological detail. The fourth-power relationship, and why central
access is not fast access. Infiltration against extravasation, and why the second is
time-critical. Why circulatory overload is a rate complication. Why potassium-containing infusions
are a rate-safety problem. Where each class of fluid distributes and what that makes it for. The
hypotonic-maintenance hyponatraemia story. And the local answers: who may cannulate, who may
access a central device, how tip position is confirmed, what the phlebitis tool is, what the
attempt limit is, and who reviews the infusion daily.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to
this answer:

* The reader's **national clinical guideline on intravenous fluid therapy in adults**, and the
  separate paediatric one.
* The reader's institutional vascular access policy and its phlebitis assessment tool, including
  who may insert and access each device class and how central tip position is confirmed.
* The reader's institutional extravasation policy, which is agent-specific and time-critical.
* The reader's national patient safety body's alerts on intravenous potassium and on hypotonic
  maintenance fluid in children.
* The reader's national formulary, for any statement about a particular drug's route, diluent,
  rate or compatibility.
* A current textbook of applied physiology, for compartment distribution and the flow
  relationship.
* The published trial literature comparing balanced crystalloids with isotonic saline, which is
  active and unsettled.

The Pokémon material is from the **pret/pokeemerald** decompilation of Pokémon Emerald:
`WildEncounterCheck` and `ChooseWildMonIndex_Fishing` in `src/wild_encounter.c`;
`CalculatePPWithBonus` and `RemoveMonPPBonus` in `src/pokemon.c`; the Oran, Sitrus and Leppa
entries in `src/data/items.h`; Blissey's and Shedinja's base HP in
`src/data/pokemon/species_info.h`; and the Sootopolis City and Route 118 fishing tables in
`src/data/wild_encounters.json`. The nine encounter-rate levers and the slot partition are m082's,
checked against the same file. The per-rod slot **probabilities** are deliberately **not** quoted
here: the named constants `ChooseWildMonIndex_Fishing` compares against are not present at the
header path this answer's other citations come from, so they were not verified, and an unverified
mechanical figure is the defect this directory is least able to catch.

## Scope and safety

This explains the structure of an intravenous prescribing decision through a game's access and
delivery mechanics, at the level of someone already training in or qualified for clinical
practice. It is not a fluid prescribing guide, not a cannulation procedure and not a drug
administration reference. It states **no volume, no rate, no concentration, no catheter gauge, no
dwell time and no compatibility** — all of which are set by the reader's formulary, national
guidance and local policy, which are the authority. Nothing here has had clinical review. Nothing
here is for use in an emergency or for any decision about any person's care; suspected
extravasation in particular needs the local policy and the local team immediately. If someone is
unwell right now, the local emergency number is the correct response.

## Where this stands, October 2026

The mechanical material is fixed and the physics does not date: distribution follows tonicity,
flow follows radius and length. The three-decision structure and the fluid-is-a-drug framing are
standard in national guidance and unlikely to reverse. What dates is the detail. The
balanced-crystalloid against saline question is active and the balance has moved within the last
decade. Device selection has shifted toward longer peripheral catheters and peripherally inserted
central catheters where duration justifies them, at different speeds in different countries. The
restrictions on concentrated electrolytes, the rules on peripheral cannula dwell and replacement —
including whether routine replacement is recommended at all, which has changed — and the phlebitis
tools in use are institutional and differ. The reader's national fluid guideline, formulary and
local vascular access policy are the authority throughout.
