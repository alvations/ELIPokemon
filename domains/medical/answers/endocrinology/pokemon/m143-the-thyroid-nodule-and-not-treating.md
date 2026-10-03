---
id: "m143"
slug: the-thyroid-nodule-and-not-treating
style: pokemon
category: endocrinology
difficulty: advanced
question: "A thyroid nodule is found. Why is most of the investigation that follows designed to stop rather than to proceed?"
tags: [thyroid, nodule, thyroid-cancer, overdiagnosis, cytology]
---

# Sweet Scent adds nothing to the encounter table, and almost every branch after it is written to make something unselectable

**Sweet Scent** is the right place to start and the reason is one argument in the source.
`SweetScentWildEncounter` calls `TryGenerateWildMon(gWildMonHeaders[headerId].landMonsInfo,
WILD_AREA_LAND, 0)` — and that third argument is the flags word, passed **0** (**mechanism**). An
ordinary step passes `WILD_CHECK_REPEL | WILD_CHECK_KEEN_EYE`; **Sweet Scent** passes nothing. No
**Repel** threshold, no **Keen Eye** check, no rate roll, no new-metatile test. m048 established
that in general practice as the open question bypassing every filter you had running, and here it
does a second job.

Because here is the part that matters: **Sweet Scent does not add a single entry to the table.**
It draws from `gWildMonHeaders[headerId].landMonsInfo`, the same table that was always there. It
guarantees you meet something that was already on the route. The table did not change; the
encounter did.

That is the whole overdiagnosis argument in one function call. Imaging a neck for an unrelated
reason reports what is in the field of view, with none of the filters a deliberate search would
have applied, out of a reservoir of common and mostly harmless findings that was there all along
(**consensus**). m084 argues overdiagnosis as a general mechanism and m013 argues what deliberate
searching costs; this answer is about what happens in the next forty minutes, which is a long
sequence of branches written to stop.

| In the battle | What it stands for |
| --- | --- |
| **Sweet Scent**'s `TryGenerateWildMon(..., 0)` | Incidental imaging: every filter off, nothing added |
| The `landMonsInfo` table, unchanged by **Sweet Scent** | The reservoir of common findings that was always there |
| **Repel** and **Keen Eye**, bypassed | The selection a deliberate search would have applied |
| **Flail** in its floor band at base power 20 | A suppressed reporter: read it first |
| **Grassy Terrain**, and **Tapu Bulu**'s **Grassy Surge** | Thyroid hormone, and the gland that normally sets it |
| `TryChangeBattleTerrain` returning FALSE on its own terrain | An autonomous second source, adding nothing and refreshing nothing |
| A **Terrain Extender**'s eight turns instead of five | A long half-life, so the field outlives the question |
| `GetConfig(B_HEAL_BLOCKING) >= GEN_5` at a decision point | Which rule applies is a property of the build, not the battler |
| `sSoundMovesTable`: ten moves and a sentinel, hand-kept | A risk-stratification list, and the feature nobody put on it |
| Pokédex **seen** set, **owned** clear | A result that documents encounter and not confirmation |
| `GetSetPokedexFlag` wiping four arrays and returning 0 | A contradictory result discarded, reading as a negative |
| `EFFECT_PLACEHOLDER` and `MOVE_LIMITATION_PLACEHOLDER` | A finding listed in the record and explicitly not for acting on |
| **Tapu Fini**'s **Misty Terrain**, set from the same place | A tumour in this gland reporting on the calcium channel |
| **Earthquake**: accuracy 100, `MOVE_TARGET_FOES_AND_ALLY` | Collateral written into the target field, not into the miss |
| **Flygon**'s **Levitate**, which **Earthquake** cannot reach | The adjacent structure that is out of the field |
| The **Move Deleter**: free, and irreversible | Removal that cannot be undone |
| The **Move Reminder**'s `gLevelUpLearnsets[species]` | What can be restored, and what cannot |
| **Silcoon** and **Cascoon**: one point of yield apart | Two lesions separated by a feature no sample contains |
| The **Move Deleter** in **Lilycove City**, charging nothing | Removal, free at the point of use |
| The **Move Reminder** in **Fallarbor Town**, one **Heart Scale** | Restoration, which costs and is restricted |
| **Shedinja**, deliberately not used | See the declining section |

**This answer defers to five others.** m056 owns **Flail** as the inverted amplified reporter and
**Grassy Terrain** as thyroid hormone. m057, m058 and m059 own `TryChangeBattleTerrain`'s refusal
as autonomy. m095 owns the two-independent-questions structure of an incidental mass. m037 owns
Pokédex **seen** against **owned**. m073 owns the **Move Deleter** against the **Move Reminder**.
m048 owns **Sweet Scent**'s zero. All of them appear here; none is re-argued.

Clinical claims are marked (**mechanism**), (**definitional**), (**consensus**) or
(**country-dependent**). The Pokémon mechanics carry no clinical marker; the Sources section says
where each was read.

## What the pathway is actually shaped like

```
   SIX DECISION POINTS. FIVE OF THEM EXIT.

   Sweet Scent, flags = 0 ─── you have met something off the standing table
            │
            ▼
   [1] READ FLAIL           ─ floor band, power 20 ──► DIVERT
       the only diverting      something is already holding the field up:
       branch in the chart     the question is now WHAT IS SETTING IT
            │ Flail mid-table
            ▼
   [2] LOOK AT IT           ─ reassuring pattern ───► STOP
       features → a category   (do not sample)
            │ pattern of concern
            ▼
   [3] SAMPLE               ─ owned bit set, benign ► STOP
            │               ─ SEEN, NOT OWNED ─────► back to [3], or to [5]
            │ confirmed          the branch with no exit of its own
            ▼
   [4] IS ACTING BETTER     ─ sometimes not ───────► STOP
       THAN WATCHING?          (and this is a real answer, not a refusal)
            │
            ▼
   [5] ACT                  ─ and Earthquake has target FOES_AND_ALLY
            │
            ▼
   [6] AND THEN?            ─ the Move Deleter is free and permanent

   Every box except [1] and [5] is a brake. [1] is a signpost. [5] is the
   door, and it is the only one with a cost written into its own data entry.
```

## Read Flail first, because the floor band means something is already up

The thyroid answer reads this axis through **Flail**, whose base power is computed from the user's
own remaining HP in 48ths and walks a six-entry table: 200 at a sliver, then 150, 100, 80, 40, and
**20 across everything above two thirds of the bar** (**mechanism**). The move's own data entry
lists `.power = 1`; the number that matters is produced by `EFFECT_FLAIL`.

The reporter counts **upward as the bar falls**, so a *low* number means there is plenty.
**Flail** sitting in its floor band at 20 is the first branch of this pathway and it is the only
branch that redirects rather than stopping. A reporter at its floor means the field is already
being held up — and if you did not send the setter in, something else is setting it
(**mechanism**).

Clinically that is a suppressed pituitary reporter in somebody with a nodule, which points at
autonomous hormone production, and two things follow at once (**consensus**). The problem is now
hyperfunction rather than a structural unknown. And an autonomously hyperfunctioning nodule is
**very rarely** malignant, so the question you came in with largely answers itself.

And the floor is blind, which m056 already established and which does a job here: a full bar and a
two-thirds bar both give base power 20, so once **Flail** is at the floor you cannot tell how far
past the floor the situation is. That is why the next question is answered by **looking at the
field** rather than by reading the reporter harder.

## TryChangeBattleTerrain returns false, and that refusal is the autonomy

Send a second **Tapu Bulu** onto a field that already has **Grassy Terrain** and
`TryChangeBattleTerrain` begins:

```
   if (terrain == B_TERRAIN_NONE || terrain == gFieldTimers.terrain)
       return FALSE;
```

Nothing happens. The terrain is not re-set, the message is not printed, and — the detail this
specialty has used three times — **`terrainTimer` is not refreshed** (**mechanism**). It keeps
counting down on the clock the first setter started, five turns, or eight if that setter was
holding a **Terrain Extender**.

m057, m058 and m059 all use that refusal for the same structural idea: a supply that is already
being provided from somewhere means the thing you just introduced accomplishes nothing, and the
original clock continues underneath. Here it carries a sharper point. **The interesting property
of a nodule that makes hormone is not how much it makes. It is that it makes it without being
asked** (**mechanism**). The field is up; the level above is not driving it; the refusal of a
second **Grassy Surge** is what tells you the field already has a source.

And where it is available, a scan that shows which tissue is taking up iodine is the test that
localises the source — the equivalent of looking at who is actually standing there rather than
inferring it from the field. Its availability and where it sits in the sequence differ by country
(**country-dependent**).

## Looking, and a configuration flag that decides what looking means

Everything after the diverting branch is answered by looking at physical properties rather than by
measuring a hormone: what the nodule is made of, how it reflects, what its margins and shape are,
what bright specks are inside it (**mechanism**). Several published systems turn those features
into a category, and the category carries a recommendation about whether to sample
(**consensus**).

The games give me two devices for that and they go together.

**A hand-maintained list fails for whatever is not on it.** `sSoundMovesTable` is ten moves and a
terminator, written out by hand, and anything audible that nobody added to it is simply not a
sound move as far as the code is concerned (**mechanism**). m075 used that in nursing for a
transmission route encoded as a list. A risk-stratification system is exactly such a list: a set
of features somebody chose, combined in a way somebody specified, and a nodule's features are
classified by whichever list the department holds.

**And which rule applies is read from a configuration flag at the decision point.** The expansion
is full of lines like `GetConfig(B_HEAL_BLOCKING) >= GEN_5` and `GetConfig(B_TAUNT_ME_FIRST) <
GEN_5` sitting *inside* the branch they govern (**mechanism**). The same mechanic behaves
differently depending on which generation's rule the build is configured to, and nothing about the
battler changes.

That is the cleanest expression of country-dependence this specialty has found. Several
sonographic systems are in use, they use different feature sets and different size thresholds, and
the same nodule can attract different recommendations under different systems (**consensus**).
Which one applies is a property of the department, not of the nodule (**country-dependent**). And
the design intent of every one of them is to **reduce sampling**, which is to say they were
written to make the next branch not fire.

No thresholds from any of them appear here, deliberately, and the scope section says why.

## Seen without Own, and the four arrays that have to agree

Now the sample, and the Pokédex is the right structure for it because it keeps **two separate bit
arrays**.

`GetSetPokedexFlag` holds `seen` and `owned` independently, and its caught case is strict: the
`owned` bit must agree with the `seen` bit **and** with `seen1` **and** with `seen2`, and if any
of the four disagrees it clears all four and returns 0 (**mechanism**). m037 used **seen** against
**owned** in nursing for documented-as-encountered against documented-as-confirmed, and that is
the indeterminate cytology category precisely.

An indeterminate result is not a negative and not a positive. The `seen` bit is set. The `owned`
bit is not. The question has not been answered (**definitional**, **consensus**). And because it
has not been answered, it generates further action — repeat sampling, molecular testing where it
is available, or an operation performed in order to find out (**consensus**). An operation done to
obtain a diagnosis carries the surgical costs of one done to treat a cancer, and most of the
people having it do not have one.

The four-array wipe does a second job. An **inadequate** specimen is a different failure from an
indeterminate one — one is a problem with the sample and the other with what the sample showed —
and `GetSetPokedexFlag` discarding a contradictory record and returning 0 is the shape of the
first: a result that cannot be trusted, zeroed, reading on the screen exactly like a result that
was clear (**mechanism**). m073 made the same observation about `FlagGet` returning FALSE for both
a failed lookup and a genuine clear bit. A confident zero is the most expensive thing a storage
class can give you.

And one limit of the test that is architectural rather than operational: cytology cannot separate
a follicular adenoma from a follicular carcinoma, because the distinction rests on invasion, which
is an architectural feature a cell sample does not contain (**mechanism**). That is m095's
adrenal-biopsy argument arriving at another gland: the test that looks like the direct route to
the answer sometimes cannot produce one.

**Silcoon** and **Cascoon** are the species for that, and m086 found them in dermatology. They are
identical in every base stat, in typing, in ability and in effort yield, and differ in body colour
and in **one point of experience yield — 71 against 72** (**mechanism**). The fork that decided
which one a **Wurmple** became is `(personality >> 16) % 10 <= 4`, fixed at creation and visible
nowhere. Two things that look the same, separable only by a measurement nobody takes by eye — and
in a follicular lesion the measurement is invasion, which lives in the architecture and not in the
cells.

## A slot that is listed, and has a branch written to stop you using it

Here is the mechanic that carries indolence, and it is better than anything I expected to find.

`EFFECT_PLACEHOLDER` is a real move effect in the expansion. A move carrying it occupies a slot,
appears in the moveset, and has a **dedicated branch in `CheckMoveLimitations`**:

```
   else if (check & MOVE_LIMITATION_PLACEHOLDER && moveEffect == EFFECT_PLACEHOLDER)
       unusableMoves |= 1u << i;
```

Somebody wrote a condition whose only purpose is to grey out a thing that is present, listed, and
not to be acted on (**mechanism**). Not deleted — deleting it would lose the record. Not hidden.
Present, recorded, and explicitly unselectable.

That is active surveillance. A substantial share of what this pathway finds would never have gone
on to cause harm, in several countries recorded incidence rose for decades without a matching
change in mortality, and the consequence is that **active surveillance of a small low-risk
papillary cancer is an accepted option in some systems rather than a refusal of treatment**
(**consensus**, **country-dependent**). The code's own answer to a thing it does not want acted on
is a branch, not a deletion, and that is the right shape.

## Misty Terrain from inside the thyroid, which means a different cell

This is where the established vocabulary earns the most and where I am extending it rather than
adding to it.

The four terrains in this specialty are assigned: **Grassy Terrain** is thyroid hormone with
**Tapu Bulu** as the gland, **Psychic Terrain** is cortisol with **Tapu Lele**, **Misty Terrain**
is calcium with **Tapu Fini**, and **Electric Terrain** is the reproductive clock with **Tapu
Koko**. m094 declined to invent a fifth and built on a clock and a counter instead, which was
right.

I am not inventing one either. What I am doing is pointing out that **a tumour in this gland can
belong to a different layer**. Medullary thyroid carcinoma arises from the parafollicular cells
rather than the follicular epithelium: it makes no thyroid hormone, takes up no iodine, and is
**not monitored on the thyroid axis at all** — its circulating marker is calcitonin, which belongs
to the calcium story (**mechanism**). So the setter standing inside **Tapu Bulu**'s gland is
putting up **Misty Terrain**, and **Flail** — the thyroid reporter — has nothing to say about it,
because **Flail** reads the bar that **Grassy Terrain** was holding up and this thing is not
touching that bar.

And one consequence with no counterpart in the rest of the answer. Medullary disease has a
hereditary form, occurring as part of a multiple endocrine neoplasia syndrome, so family history
and genetic assessment are part of its management (**consensus**). m045's distinction fits:
**Sketch** copies horizontally, within one encounter, and an **Egg Move** arrives vertically, from
the generation before. This is the vertical one, and nothing else in this gland is.

## Earthquake has accuracy 100 and still hits your own side

The treatment branch, and the mechanic is in the move's data entry rather than in anything that
happens at run time:

```
   [MOVE_EARTHQUAKE] = { .power = 100, .accuracy = 100, .type = TYPE_GROUND,
                         .target = MOVE_TARGET_FOES_AND_ALLY, ... }
```

Accuracy 100. It does not miss. In a double battle it hits your own partner, and it does so
**because the target field says so** (**mechanism**). That is not a failure of execution; it is
the move's declared reach.

The parathyroid glands sit on or near the posterior thyroid capsule and the recurrent laryngeal
nerves run in the groove beside it, so hypoparathyroidism and voice change after thyroid surgery
are consequences of where things are rather than accidents of technique (**mechanism**,
**consensus**). m059 is where the time course of post-surgical hypocalcaemia is worked through and
m091 is where a mass affecting what is next to it is argued; the target field is the same idea
stated as data.

**Flygon** is the counterpart and it is the useful half of the comparison. **Earthquake** cannot
touch it, because **Levitate** is its only ability in both slots and a Ground move has no reach to
something that is not grounded (**mechanism**). Something adjacent is at risk and something
adjacent is not, and which is which is a property of the anatomy and not of how carefully anybody
works.

## The Move Deleter is free, and the Move Reminder's list is fixed

The last branch, and m073 found it in nursing. The **Move Deleter** stands in a house in
**Lilycove City** and his script takes no item at all: removal is free at the point of use and it
is permanent. The **Move Reminder** in **Fallarbor Town** will put a move back, and her script
runs `checkitem ITEM_HEART_SCALE` and then `removeitem ITEM_HEART_SCALE` — restoration costs a
**Heart Scale**, and the list she works from is `gLevelUpLearnsets[species]`, so a move that
arrived by any other route is gone for good (**mechanism**). Free to remove, paid for and
restricted to put back.

Taking the whole gland out commits a person to lifelong replacement, and m056's closing argument
is the one that applies: replacement supplies the hormone and does not restore the loop, so the
amount is set from outside and adjusted by measurement rather than regulated (**mechanism**). The
**Move Reminder** can restore the hormone. It cannot restore the thing that decided how much.

And the surveillance that follows is the other cost nobody writes down as one. Repeated imaging,
repeated sampling and a cancer label carried for decades have effects on insurance, on employment
and on how somebody thinks about themselves, and none of those appears in a complication list
(**consensus**).

## The mapping I am declining

Three refusals, and the first two are about taste rather than inventory.

**I am not using Shedinja for anaplastic carcinoma.** It is the obvious device — the case where
every argument collapses because one parameter is 1 — and the specialty's conventions allow
**Shedinja** for a parameter-collapse point with nobody attached. This is not that. Anaplastic
thyroid carcinoma is rare, aggressive, and the thing a person has; making the joke species stand
in for it would be whimsy about an outcome, which is the one thing this register does not do. It
is named in the serious half, with the single necessary statement that none of this answer's
braking argument transfers to it (**consensus**), and it gets no mechanic here.

**I am not mapping the sampling decision to a Poké Ball.** It is the shape the Pokédex device
invites: `seen` becomes `owned` by catching, so the act in between would be a throw. The
specialty's conventions rule catching out as a mapping for diagnosis — it is acquisitive and
non-consensual and reads badly however it is framed — and the ball mechanics are reserved for
probability. So I used **seen** and **owned** as *states* and left the transition between them
unmapped, which is the right trade and cost this answer its neatest paragraph.

**And I am not building a fifth terrain for a tumour.** A nodule is not a hormone. What it does,
when it does anything, is set one of the four that already exist — which is why the **Misty
Terrain** section above works by *reassigning* a setter rather than by adding a field condition.
m094 set that precedent and this answer follows it: extend the layer, do not add to it.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

Everything above is a picture of a reservoir that was always there, an encounter forced with the
filters off, and a chain of branches most of which exist to make the next thing unselectable. The
picture is fair, and the conclusion it supports is the right one: in this pathway, stopping is
usually the correct output and not a failure to find anything.

Here is what it cannot carry.

The word is the problem. Somebody told they have a thyroid nodule has usually heard "we need to
check it is not cancer", and from that moment they are a person waiting to find out, through a
sequence of appointments, for weeks. The great majority will be told it is nothing. The waiting
happened anyway, and it is a genuine cost of a pathway built to stop — paid by many so that a few
are found. No diagram above contains it.

Somebody told they have a small low-risk thyroid cancer and offered surveillance is being asked
for something genuinely hard: to live alongside a diagnosis with the word cancer in it and
deliberately not act on it. That this is often the better option does not make it easy, and
somebody who chooses surgery instead is not making a mistake. Both are reasonable and the choice
belongs to the person, with time and a conversation rather than a leaflet.

The harms on the treatment side are lived rather than listed. Hypoparathyroidism after surgery can
be permanent and is unpleasant to live with. A changed voice is a changed identity for some
people. Lifelong replacement is a daily reminder and a schedule of appointments. None of that
argues against treating a cancer that needs treating. It argues for being honest about what is
being traded.

A note about who is reading. Somebody reading this may be partway through exactly this pathway. If
that is you: there are deliberately no sizes, categories or numbers anywhere here to match against
your own report, because a feature means something only inside the system your department uses and
alongside everything else about you. The team that ordered the scan is the only place that reading
exists — not an analogy about encounter tables. And a nodule growing quickly, a new change in your
voice, or new difficulty swallowing or breathing is a reason to contact them rather than to keep
reading.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md)
for the standing documents of this specialty. Specific to this answer:

* Your national or specialty-society guidance on thyroid nodules and on differentiated thyroid
  cancer, for the sequence of investigation, the sonographic risk-stratification system used where
  you work, its size thresholds and the criteria for active surveillance.
* **Your radiology department's protocol**, for which risk-stratification system it reports
  against. Different systems recommend differently for the same nodule and the department's choice
  is the one that applies.
* **Your cytopathology service's reporting scheme**, for its categories and for how it reports
  inadequate against indeterminate specimens.
* Your national or specialty-society guidance on medullary thyroid carcinoma, for its marker, its
  genetic assessment and the syndromes it occurs in.
* Your national or specialty-society guidance on anaplastic thyroid carcinoma, because nothing in
  this answer's braking argument applies to it.
* **The primary literature**, for the incidence-against-mortality evidence behind the
  overdiagnosis argument in this disease and for the active-surveillance series.
* A current endocrinology or head-and-neck surgery textbook, for the position of the parathyroid
  glands and the recurrent laryngeal nerves relative to the thyroid capsule, and for each tumour's
  cell of origin.

The Pokémon side is different and is sourced properly. `SweetScentWildEncounter` calling
`TryGenerateWildMon(gWildMonHeaders[headerId].landMonsInfo, WILD_AREA_LAND, 0)` with the flags
argument passed as zero, against an ordinary step's `WILD_CHECK_REPEL | WILD_CHECK_KEEN_EYE`;
`TryChangeBattleTerrain`'s first line returning FALSE when the requested terrain equals
`gFieldTimers.terrain`, and its `terrainTimer` of 8 with a **Terrain Extender** and 5 without;
**Flail**'s six-band table computed on 48ths of the user's own bar with a listed `.power` of 1;
**Earthquake**'s data entry carrying `.power = 100`, `.accuracy = 100` and `.target =
MOVE_TARGET_FOES_AND_ALLY`; **Flygon** being Ground and Dragon with `abilities =
{ABILITY_LEVITATE, ABILITY_LEVITATE}`; `GetSetPokedexFlag` holding `seen` and `owned` as separate
bit arrays and requiring `owned`, `seen`, `seen1` and `seen2` to agree in its caught case,
clearing all four and returning 0 otherwise; `EFFECT_PLACEHOLDER` existing as a move effect with
its own `MOVE_LIMITATION_PLACEHOLDER` branch in `CheckMoveLimitations`; and the expansion's
generation-configuration tests such as `GetConfig(B_HEAL_BLOCKING) >= GEN_5` sitting inside the
branches they govern were all read from the pokeemerald and pokeemerald-expansion decompilations
rather than from memory. `sSoundMovesTable`'s ten entries and a sentinel and the **Move Deleter**
against the **Move Reminder**'s `gLevelUpLearnsets[species]` are m075's and m073's findings
respectively and are reused on their authority. The terrains, their **Tapu** setters and the
**Terrain Extender** are Generation VII and VIII material used throughout this specialty;
`EFFECT_PLACEHOLDER` and `GetConfig` are properties of the expansion and not of any retail
cartridge, which is stated because it matters.

## Scope and safety

The Pokémon here is doing one job: making it concrete that a pathway can be a chain of branches
whose purpose is to stop, that a reservoir of common findings is not changed by the act of finding
one, and that a result which documents an encounter without confirming anything is structurally
worse than a negative. It is not a clinical reference, not a decision aid, and not about any
individual's care. **No nodule sizes, sonographic category definitions, cytology category numbers,
test performance figures, radioiodine activities or surveillance intervals appear here on
purpose** — those differ most between systems, and a number lifted from a revision page and
matched against somebody's own report is the specific harm this section exists to prevent. Check
your own national guidance, your radiology department's protocol and your cytopathology service's
scheme. Nothing here has had clinical review. No Pokémon in this answer stands in for a person,
for a tumour somebody has, or for an outcome.

## What a Gym Leader digs into next

* Why does **Sweet Scent** adding nothing to `landMonsInfo` settle the overdiagnosis argument?
* Why is reading **Flail** first a *diverting* branch rather than a preliminary one?
* Why is `TryChangeBattleTerrain` returning FALSE a statement about autonomy rather than about
  amount?
* Why does `GetConfig(... ) >= GEN_5` sitting inside a branch express country-dependence better
  than any amount of hedging?
* Why is a set **seen** bit with a clear **owned** bit worse than both bits clear?
* Why does `GetSetPokedexFlag` wiping four arrays and returning 0 model the *other* kind of failed
  sample?
* Why is `EFFECT_PLACEHOLDER`'s dedicated branch the right shape for active surveillance, and why
  is deletion the wrong one?
* Why is the setter inside **Tapu Bulu**'s gland putting up **Misty Terrain**, and why has
  **Flail** nothing to say about it?
* Why does **Earthquake**'s accuracy of 100 make its collateral worse to think about rather than
  better?

## Where this stands, October 2026

The structure of the pathway as a chain of brakes, the reservoir argument, the reason the axis is
read first, the physical basis of the looking step, the difference between an unanswered result
and a negative one, the structural limit of cytology in follicular lesions, the different cell of
origin and different marker of medullary carcinoma, and the anatomical basis of the surgical harms
are mechanism and consensus and do not date. What dates on the Pokémon side is the cast and the
provenance: the terrains and the **Tapu** setters are Generation VII and VIII, a **Terrain
Extender** Generation VII, and `EFFECT_PLACEHOLDER`, `GetConfig` and `MOVE_LIMITATION_PLACEHOLDER`
are expansion constructs rather than retail ones — check the current source.
`CheckMoveLimitations` has grown from eight ORed conditions in the Advance code to eighteen
branches and will grow again. On the clinical side this is one of the fastest-moving subjects in
the specialty: sonographic risk systems and their thresholds, cytology reporting schemes, the
availability and role of molecular testing, active-surveillance criteria, the extent of surgery
recommended for low-risk disease and the use of radioiodine have all been de-escalated in several
countries over recent cycles and continue to move. Check current local guidance, your radiology
department's protocol and your cytopathology service's scheme.
