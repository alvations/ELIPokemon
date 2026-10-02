---
id: "m087"
slug: hair-and-nail-as-a-timeline
style: pokemon
category: dermatology
difficulty: intermediate
question: "Why are the nail plate and the hair shaft records of events that happened months earlier, and what does that change about the history?"
tags: [nail, hair, alopecia, onychodystrophy, timeline]
---

# Yawn lands two turns later, and by then the Pokémon that used it has gone

**Yawn** does nothing on the turn it is used. The routine writes `STATUS3_YAWN_TURN(2)` onto the
target, the end-of-turn code subtracts one from that counter every turn, and when the counter
reaches zero the target falls asleep. By then the Pokémon that yawned may have switched out, the
weather may have changed, and the sleep arrives attached to a cause that is no longer on the
field.

That is a nail plate and a hair shaft. A nail plate is keratin extruded by the matrix under the
proximal fold; once it is out it is inert, it is never remodelled, and it travels distally at a
rate set by the matrix behind it. (**mechanism**) A hair shaft is the same: a column laid down by
the follicle, carrying what the follicle was doing when that segment was made and nothing at all
about what it is doing now.

So **examining a nail is not reading a status screen, it is reading a counter that was set
earlier.** A transverse abnormality is one event; the distance from the proximal fold is how long
ago; and the person consulting you is usually consulting about something that stopped being true a
season ago.

```
   THE NAIL PLATE AS A STRIP CHART
   ==================================================================================

   proximal fold                                                     free edge
   (made TODAY)                                                     (made LONGEST AGO)
        |                                                                  |
        v                                                                  v
   .....|=================|==========|=============================|........
        ^                 ^          ^                             ^
        |                 |          |                             |
   matrix, where       a transverse  a second one:    the oldest surviving
   the plate is        depression:   a second event   record this plate holds
   being produced      ONE systemic
                       event, at one
                       moment

   READ IT LIKE THIS
   ==================================================================================
   finding                     what it says                      the question to ask
   =========================   ===============================   ===================
   transverse groove or        ONE insult, at ONE time,          what happened about
   ridge at the same level     affecting the matrix of every     that long ago?
   across several nails        nail simultaneously
   =========================   ===============================   ===================
   complete separation of      a more severe version of the      same question, bigger
   the plate from the matrix   same thing -- the matrix          insult
   at one point in time        stopped altogether
   =========================   ===============================   ===================
   longitudinal band in ONE    something persisting in ONE       is it widening, is it
   nail, running the whole     part of ONE matrix, over time     changing, is the
   length                      rather than at one moment         cuticle involved?
   =========================   ===============================   ===================
   the whole plate is          the process is ongoing, not       what is still
   abnormal, from fold to      historical                        happening?
   free edge
   ==================================================================================
```

## Markers used in this answer

The clinical claims here carry the same inline markers as the serious half. **mechanism** —
follows from biology and is checkable by reasoning. (**definitional**) — a term's meaning.
(**consensus**) — standard across current textbooks and national guidance. (**country-dependent**)
— differs between countries or institutions, and yours is the authority. The Pokémon claims are
not marked this way; they are listed in the `## Sources` section with the file they were checked
against.

## The six growth curves are why a toenail answers a different question

The game does not store a level. It stores **experience**, and the level is derived from it
through one of six tables chosen by a per-species field. The formulas are in `experience_tables.h`
and they are not approximations:

```
   SAME NUMBER OF EXPERIENCE POINTS, DIFFERENT LEVEL REACHED
   ==================================================================================

   CURVE            FORMULA FOR LEVEL n            A SPECIES THAT USES IT
   ==============   ============================   =================================
   Medium Fast      n cubed                        Wurmple
   Fast             4 * n cubed / 5                Banette, Shuppet
   Slow             5 * n cubed / 4                Latios
   Medium Slow      6n cubed / 5 - 15n squared     Absol
                    + 100n - 140
   Erratic          piecewise -- four branches,    Lileep, Armaldo
                    breaking at 50, 68 and 98
   Fluctuating      piecewise -- three branches,   Gulpin, Swalot
                    breaking at 15 and 36
   ==================================================================================
   Feed Banette and Latios the identical number of experience points and they are at
   different levels, because the rate constant is a property of the species. And the
   last two curves are not even smooth: the rate changes at a hard boundary partway
   along, so the same input buys different progress depending on where you already
   are.
```

A fingernail replaces itself over a matter of months. A toenail takes considerably longer and may
approach a year or more. (**consensus**) Same organ, different rate constant, so the toenail holds
a longer history and answers a question about a more distant past. And the operational consequence
is the one worth carrying away: **the assessment interval is set by the structure's own growth
rate, not by the clinic's diary.** Judging a nail treatment before a full plate has grown out is
judging it before the evidence exists — reading the level before the experience has accumulated.

The two piecewise curves have a job here too. The hair follicle cycles through a long growth
phase, a brief transitional one, and a resting phase that ends in the shaft being released, and
the rate is not one constant along that cycle. **Erratic** and **Fluctuating** are what a rate
with hard boundaries in it looks like when somebody writes it down.

## Yawn is telogen effluvium and the counter is why the history misses it

At any moment the great majority of scalp follicles are in the growth phase and they are not
synchronised, so the ordinary daily shed is unremarkable. Telogen effluvium is what happens when
that independence breaks: a systemic insult — a febrile illness, surgery, a major physiological
event, significant weight loss, a new medicine, severe iron deficiency — pushes a large cohort of
growing follicles into the resting phase at once. The shedding cannot begin until that phase ends,
so it starts roughly two to three months after the event, by which time the person has usually
recovered from it. (**consensus**)

That is `STATUS3_YAWN_TURN(2)` exactly. The consequence was written at the moment of the insult,
the counter ran down out of sight, and the arrival looks causeless. The history that explains it
is the history of a season ago, which is why the useful question is what was happening two or
three months back and not what is happening today.

The contrasting mechanism has a contrasting timescale, and the timescale alone is diagnostic.
Anagen effluvium — classically cytotoxic chemotherapy — damages the matrix while it is actively
making the shaft, so loss happens within days to weeks. That is not a counter at all: it is damage
to the thing doing the writing. If you want the stored-at-the-moment-of-use device in its purest
form, **Future Sight** and **Doom Desire** are it, and m086 and m068 both use them; the point here
is the delay, not the frozen value.

## The Move Deleter is the scarring alopecia, and the game has the guard written in

In Lilycove City there is a man who will make a Pokémon forget a move. Down the road in Fallarbor
Town there is a tutor who will teach one back — for a **Heart Scale**, and `removeitem` takes the
scale whether you come back tomorrow or never.

The asymmetry between those two services is the whole distinction between non-scarring and
scarring alopecia:

```
   WHAT CAN BE REFILLED, AND WHAT CANNOT
   ==================================================================================

   NON-SCARRING                           SCARRING (CICATRICIAL)
   ====================================   ===========================================
   follicular openings still visible      follicular openings LOST -- smooth, shiny,
   within the patch                       featureless scalp within the patch
   ====================================   ===========================================
   the slot is still there and the        the slot is gone, and the Move Reminder's
   Move Reminder can refill it, because   script has a branch for exactly this: no
   the move is in the species' own        relearnable move, nothing to teach, come
   level-up list                          back another time
   ====================================   ===========================================
   alopecia areata, telogen effluvium,    lichen planopilaris, frontal fibrosing
   androgenetic, traction (early)         alopecia, discoid lupus, central
                                          centrifugal cicatricial alopecia,
                                          folliculitis decalvans
   ====================================   ===========================================
   regrowth is possible                   that area will not regrow
   ====================================   ===========================================
   look at pattern and shedding           look at the ACTIVE EDGE -- scale, redness,
                                          pustules, tenderness at the margin
   ====================================   ===========================================
   time pressure: low                     time pressure: HIGH -- treatment protects
                                          what is still there and recovers nothing
   ==================================================================================
   Sustained traction is the bridge between the columns: reversible early, scarring
   if it continues. The question about how the hair is styled, and for how long, is
   a clinical question and not small talk.
```

Two details in the code sharpen it. A **TM** in the third generation is consumed the moment the
move is learned — `RemoveBagItem(item, 1)`, with an explicit exemption so that **HM**s are not —
so a move learned from a TM and then deleted may have no route back at all, while an HM move
always has one. And the Move Deleter's script calls `IsLastMonThatKnowsSurf` and refuses: the game
will not let you delete the one record you cannot rebuild. **Somebody wrote a guard against
irreversible loss into a man in a house in Lilycove, and the clinical equivalent is identifying an
active scarring process while there are still follicles to protect.** The referral routes and
timescales for that are (**country-dependent**).

## Rare Candy moves the readout and throws the history away

The level-up item does not add experience. It looks up `gExperienceTables[growthRate][level + 1]`
and **writes that value into the experience field**, discarding whatever surplus progress was
there. The number on the screen goes up by one and the record of how the Pokémon got there is
gone.

Keep that in view whenever a hair or nail complaint is managed as a cosmetic one. The appearance
can be changed without the process being touched, and the record that would have dated the process
is the appearance.

## What the nail says about the rest of the body

Nail findings are often the readout of something that is not a nail problem, which is **Kyogre**'s
**Drizzle** from m052 pointed at a different organ: one upstream setter, several downstream
readouts, and the nail is one of them. Pitting, onycholysis, subungual hyperkeratosis and the
salmon-coloured patch point to psoriasis, and nail involvement is associated with psoriatic
arthritis — so a nail examination is part of an arthritis assessment and not a cosmetic aside.
Ragged cuticles, nail fold erythema and abnormal nail fold capillaries point to connective tissue
disease. Clubbing, koilonychia and transverse grooves each carry their own differential.
Separation of the plate from the matrix some weeks after a febrile illness is a recognised
sequence and settles on its own.

Two findings carry a different kind of weight, and they belong with the recognition question
rather than this one. A **longitudinal pigmented band in a single nail** — particularly one
widening, with irregular pigmentation, involving the cuticle or proximal fold, or arising in a
single digit in an adult — is a reason for specialist assessment of the nail apparatus rather than
observation. And a **solitary chronically abnormal nail unit** that does not behave like its label
is assessed rather than re-treated, which is the discipline m055 applies to a non-healing ulcer.
The staging and spread reasoning lives in the oncology answers m061 to m065 and is not re-derived
here. **Spinda**'s spots are the m016 device for variation between individuals; nothing in this
answer uses variation to excuse a single lesion behaving differently from its neighbours.

## Where the metaphor stops

No Pokémon in this section.

Hair and nail disease is visible, permanent in some of its forms, and routinely dismissed. The
dismissal is itself a clinical problem rather than a matter of manners: a scarring alopecia called
cosmetic is a scarring alopecia that is not treated during the only period in which treatment can
protect anything, and the tissue lost in that interval does not come back.

People with these conditions commonly arrive having been told there is nothing to be done, and
having already spent substantial sums on products. Some have changed how they dress, stopped
swimming, stopped having their hair cut by a stranger, or stopped going to work events. That is
not vanity, and it is not the reason to treat; it is the reason the consultation deserves the same
seriousness as any other.

Two specific things are worth naming. First, several scarring alopecias are much more commonly
seen in particular populations — central centrifugal cicatricial alopecia above all — and the
teaching images, as m018 argues at length, under-represent exactly those populations, which delays
recognition in the people most affected. Second, hair loss during cancer treatment and hair loss
from a scarring disease are different problems with different trajectories, and conflating them in
a conversation is both unkind and inaccurate.

Without softening: nothing here is for any reader's own use, and no treatment, interval or
referral route named here is a recommendation. Anyone with hair loss that is spreading, scarring,
painful, itchy or associated with redness and scale around the hair openings, or with a new or
changing pigmented band in a nail, needs assessing in person — and a patch of scalp becoming
smooth and shiny is a reason to be seen sooner rather than later.

## What a Gym Leader is listening for

Why a nail plate records an event rather than a state. How you convert the position of a
transverse groove into a date. Why a toenail answers a question about a more distant past than a
fingernail — the per-species rate constant, not a difference in the organ. Why telogen effluvium
presents after the person has recovered, and why that makes the two-to-three-month question the
useful one. What distinguishes anagen from telogen effluvium on timescale alone. The single
examination finding that separates scarring from non-scarring alopecia, and why it dictates
urgency. Where you biopsy a scarring alopecia, and why not the centre. Which nail changes point
outside the nail. And why a nail treatment cannot be assessed before a plate has grown out.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-dermatology.md`](../../../for-agents/SOURCES-dermatology.md),
and they are the authority for everything procedural or quantitative here. Specific to this
answer:

* For nail and hair growth rates, the phases of the hair cycle and their durations, and the named
  nail signs: a current standard textbook of dermatology. The rates here are stated as orders of
  magnitude on purpose and the textbook figure is the one to use.
* For the classification of the alopecias, the scarring entities and their management: the
  specialist guidance of your national dermatology body, and your regional referral pathway for
  suspected scarring alopecia, which sets the timescale.
* For any systemic agent used in hair or nail disease, including the antifungals with their
  interactions and monitoring: your national formulary.
* For a pigmented nail band and when it needs specialist assessment: your region's
  suspected-skin-cancer referral guideline, and the oncology answers in this domain for the
  staging and spread reasoning this answer deliberately does not restate.
* For nail disease as a marker of psoriatic arthritis and of connective tissue disease: your
  national rheumatology and dermatology guidance.

The Pokémon claims were checked separately against source. Yawn writing `STATUS3_YAWN_TURN(2)`,
the end-of-turn code decrementing it and the sleep landing when it reaches zero; a switch clearing
`gStatuses3` entirely; the six experience curves and their formulas — n cubed for Medium Fast,
four fifths of n cubed for Fast, five quarters for Slow, the quartic-looking Medium Slow
expression, and the four-branch Erratic and three-branch Fluctuating piecewise definitions
breaking at levels 50, 68 and 98 and at 15 and 36; Wurmple being Medium Fast, Banette and Shuppet
Fast, Latios Slow, Absol Medium Slow, Lileep and Armaldo Erratic, and Gulpin and Swalot
Fluctuating; the level-up item writing `gExperienceTables[growthRate][level + 1]` straight into
the experience field rather than adding to it; Future Sight and Doom Desire computing their damage
at the moment of use; the Move Deleter living in a house in Lilycove City and his script calling
`IsLastMonThatKnowsSurf` and refusing; the Move Reminder in Fallarbor Town taking a Heart Scale
with `removeitem` and having an explicit branch for a Pokémon with no relearnable move; and a TM
being consumed by `RemoveBagItem(item, 1)` on learning while HMs are exempted — all from the pret
decompilation of Pokémon Emerald.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

**No growth rate, interval, treatment or referral timescale named here is an instruction, and none
of it addresses any reader's own treatment.** The rates are given as orders of magnitude to
explain why the examination works the way it does; the textbook and the formulary where you
practise are the authority, and referral routes and timescales differ by country.

Anyone with hair loss associated with redness, scale, pustules or tenderness around the hair
openings, with a patch of scalp becoming smooth and featureless, or with a new, changing or
pigmented band in a single nail, needs to be assessed in person. A rapidly spreading scalp
process, or one with systemic symptoms, needs assessing urgently.

Local guidance and the policy where you practise are the authority on all of this, and they differ
by country and by institution.

## Where this stands, October 2026

The biology is settled and is the part worth memorising: inert keratin, a rate set behind it, and
position as elapsed time. What moves is classification and treatment. The nomenclature of the
scarring alopecias has been revised repeatedly over the last two decades and the groupings differ
between texts. Frontal fibrosing alopecia has been reported in rising numbers internationally and
the cause of that rise is not settled. Treatment of alopecia areata changed substantially with the
arrival of oral Janus kinase inhibitors, and which of them is licensed, for which severity, at
what age, and whether it is funded, is firmly (**country-dependent**) and has moved more than
once. Trichoscopy has become a routine part of the hair examination rather than a specialist
extra. The nail signs and their differentials are stable — rather more stable than the experience
curves, two of which the series has quietly rewritten between generations. Current as of October
2026.
