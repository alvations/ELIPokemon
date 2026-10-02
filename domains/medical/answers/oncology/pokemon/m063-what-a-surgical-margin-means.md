---
id: "m063"
slug: what-a-surgical-margin-means
style: pokemon
category: oncology
difficulty: intermediate
question: "What does a surgical margin actually mean, and in what sense is a clear margin a probability statement rather than a guarantee?"
tags: [surgery, margins, residual-disease, sampling, pathology]
---

# The Itemfinder says "nearby" and the window is not the shape you think

Read `HiddenItemNear` in the Red decompilation and the **Itemfinder** does three things, none of
which is what players believe it does.

It walks the table of hidden-item coordinates for the current map. It **skips anything already
collected**. And then it compares the item's position against a window around the player — five
tiles back and four forward in one axis, five back and five forward in the other — and returns a
single bit: something is in the window, or nothing is. No direction. No distance. No count. And
the window is **not symmetric**, which the source says and no in-game text mentions.

That is a margin report, in one subroutine. A bit returned from a window, where the window is
smaller than the area you care about, the shape of the window is a convention rather than a fact
about the world, and a negative result and *nothing there* are different propositions.

As elsewhere in this specialty: **the objects of study are instruments, thresholds, lookup tables
and accuracy fields.** No Pokémon in this answer stands in for a person with cancer, and the
analogy is dropped entirely at the end, where the subject changes.

Clinical claims carry the same marks as the rigorous half: **mechanism**, **definitional**,
**consensus**, **country-dependent**.

## The three reasons, drawn

```
   1. IT IS A SAMPLE OF A SURFACE          HiddenItemNear's window

      the resection surface is a            player
      three-dimensional AREA                  ●
                                        ┌───────────┐
      ┌──┐ ┌──┐ ┌──┐ ┌──┐               │     ●     │  ◄── returns ONE BIT
      │  │ │  │ │  │ │  │  sections     │   window  │      about THIS BOX
      └──┘ └──┘ └──┘ └──┘  read        └───────────┘
       ▲                                      ▲
       └── between them, surface               └── and the box is ASYMMETRIC
           NEVER LOOKED AT                         around the observer, which
                                                   the code says and the game
                                                   never tells you

   ────────────────────────────────────────────────────────────────────────────

   2. A CONTINUOUS NUMBER BECOMES A BAND     sFlailHpScaleToPowerTable

      HP is an exact integer.                 48ths of max HP  ──►  base power
      Flail does not read it.                        1                 200
      Cmd_remaininghptopower calls                   4                 150
      GetScaledHPFraction(hp, maxHP, 48)             9                 100
      FIRST — 48 steps — and then walks             16                  80
      a table of SIX THRESHOLDS.                    32                  40
                                                    48                  20
      exact → 48 steps → 6 bands.
      The thresholds are UNEVENLY SPACED and they are in the table because
      somebody put them there.  That is a margin convention exactly.

   ────────────────────────────────────────────────────────────────────────────

   3. THE NUMBER BELONGS TO THE MOVE, NOT TO THE OUTCOME

      Hydro Pump  .accuracy = 80      "it hit" does not make it 100.
      Fire Blast  .accuracy = 85      The field is a property of the MOVE.
      Thunder     .accuracy = 70      One result is a draw, not a revision
      Zap Cannon  .accuracy = 50      of the distribution it came from.
```

## Reason one: a bit returned from a window

The sampling argument is the strongest of the three and the one most often skipped, and the
Itemfinder is the whole of it (**mechanism**).

A resection surface is large. It is examined by cutting a finite number of blocks and reading
sections from them, chosen by protocol and by judgement to represent the surface and to cover what
worries the pathologist most. Between and within those blocks is surface that was not looked at.
So a clear margin is a **negative result from a sample**, and a negative from a sample bears on
the whole only as far as the sample represents it. Sample more and the evidence improves and the
cost rises, which is why sampling protocols are written per specimen type and are not left to
taste (**consensus**, **country-dependent** in the detail).

Two of the Itemfinder's quirks carry straight across.

* **It skips what has already been dealt with.** `wObtainedHiddenItemsFlags` is tested and
  collected items are passed over, so a negative can mean *nothing is there* or *the thing that
  was there is no longer in scope*. A margin report is read the same way: it is a statement about
  this specimen, after this operation, and not about the site.
* **A bit is not a location.** The Itemfinder will not tell you which way to walk. A specimen has
  to be oriented and inked so that an involved margin can be localised to a face — otherwise the
  result is true and nearly unusable, which is the same complaint players have about this item.

And intraoperative assessment is the Itemfinder rather than the full examination: a faster,
coarser instrument whose job is to inform a decision while the operation is still happening, not
to replace the definitive reading (**consensus**).

## Reason two: Flail reads the bar, not the number

The second reason is in `Cmd_remaininghptopower`, and it is exact.

**Flail** and **Reversal** both get stronger as the user's HP falls. Neither reads the user's HP.
The routine calls `GetScaledHPFraction` with a scale of **48** — the same forty-eight steps the
health bar is drawn in, which this specialty has already used once — and then walks
`sFlailHpScaleToPowerTable`, six threshold-and-power pairs: 1 gives 200 base power, 4 gives 150, 9
gives 100, 16 gives 80, 32 gives 40, and 48 gives 20.

So an exact integer becomes 48 steps and then six bands, at thresholds that are **unevenly
spaced** and that are in the table because somebody chose them. There is no point in a Pokémon's
physiology at which 9/48 is different in kind from 10/48. The table says there is, because a table
has to say something.

That is margin reporting (**definitional**). Local recurrence risk varies smoothly with margin
width; the report is a small number of categories separated by thresholds. The thresholds are
conventions chosen to be reproducible between observers and to map onto decisions, they are
**site-specific** — breast, rectum, skin, head and neck and sarcoma are maintained separately by
different bodies — and they are revisable. Several have been revised, generally downwards, as
evidence accumulated (**consensus**, **country-dependent** in adoption).

One band genuinely is different in kind rather than in degree, and the table has that too: the
entry at 1. Tumour reaching the inked surface is not a small distance. It is the absence of one.

And the measurement is taken on altered tissue. Specimens shrink and deform on removal and in
fixation, so the recorded distance is a distance on the fixed specimen (**mechanism**). The table
is read after the scaling, not before.

## Reason three: there is no clearance move, and the data says so twice

Now the part people most want to be false. Look at the four moves in the games that are named as
though they end things: **Guillotine**, **Horn Drill**, **Fissure** and **Sheer Cold**. Every one
of them has `.effect = EFFECT_OHKO`, `.power = 1`, `.pp = 5` and — the number that matters —
`.accuracy = 30`. **Rhydon** learns Horn Drill at level 38 on its own level-up list, so this is
not an exotic option somebody has to go looking for; it is the move a player is handed, and it is
accuracy 30.

And `Cmd_tryKO` then refuses them twice over, before accuracy is even consulted:

* **If the target has Sturdy, the move misses outright.** The routine jumps to
  `BattleScript_SturdyPreventsOHKO` and there is no roll at all. Point it at an **Onix**, whose
  ability list is Rock Head and Sturdy, and the accuracy field is never consulted.
* **If the target's level exceeds the user's, it cannot succeed**, because the condition requires
  the user's level to be at least the target's — and the chance itself is the move's accuracy plus
  the level difference, so the whole thing is contingent on circumstances the move does not
  control.

That is the honest shape of a margin (**mechanism**). There is no excision that converts a
probability into a certainty, and the two hard refusals have clinical counterparts: a tumour that
does not grow as a single expanding front defeats a plane-based description of its edge
altogether. **Discontinuous and multifocal growth** puts tumour beyond apparently uninvolved
tissue. **Lymphovascular and perineural extension** travels along structures rather than through
the plane. **Field change** in some sites means the surrounding epithelium is abnormal rather than
normal, so a margin is clear of tumour and not of risk.

Which is why the residual-disease question is its own axis: whether tumour remains after the
resection, and whether what remains is macroscopic or only microscopic, is recorded separately
from the stage group, because it is an assessment of the operation's result and not of the
disease's extent (**definitional**).

And a margin addresses the plane only. It says nothing whatever about disease that has already
left — the earlier answers in this specialty put systemic therapy in the weather, with no declared
target, for exactly this reason. Adjuvant systemic therapy is a separate question with separate
evidence.

## Why the answer is not "take more", and the gate that says so

**Substitute** costs a quarter of maximum HP, and `Cmd_setsubstitute` checks first: if current HP
is not **above** that quarter, the move fails and you get nothing. The protection is real, the
price is fixed, and the game refuses the trade rather than letting you overdraw.

The two ends of that are worth naming. A quarter of **Blissey**'s bar is a large absolute number
and Blissey can spend it, because the bar is large. **Shedinja**'s base HP is 1: a quarter of 1 is
0, the code floors that to 1, and the gate then requires current HP strictly above 1 — which
Shedinja can never have. Substitute is not a bad idea for Shedinja. It is **unavailable**, for
arithmetic reasons, permanently.

Margin width is that trade and not a quantity to maximise (**mechanism**, **consensus**). More
tissue means more loss of function, worse cosmesis, higher operative morbidity, and in several
sites a reconstruction that would not otherwise be needed. In many locations a wider margin is
simply not available, because the structure beyond the tumour is one that cannot be removed —
which is the move failing outright rather than costing more. And beyond a certain width the gain
in local control flattens while the costs do not, which is the empirical finding behind every
threshold revision that reduced a recommended margin.

So the things that genuinely buy certainty are **different mechanics**, not bigger ones.
**Lock-On** and **Mind Reader** set `STATUS3_ALWAYS_HITS`, and `Cmd_accuracycheck` tests that flag
*before* it calculates anything — a different instrument inserted ahead of the roll, not a
stronger version of the roll. Clinically: better preoperative imaging and localisation,
intraoperative assessment, specimen radiography, and techniques that map the margin as the
excision proceeds in the sites where they are established (**consensus**, strongly
**country-dependent** in availability).

## Where the metaphor stops

Everything above is sampling, thresholds and lookup tables, and code with a readable window
calculation is a good place to see them. What follows is about people, so it is said plainly and
without the analogy.

Being told that a margin is involved, or close, means being told that an operation that was
supposed to be over may not be — that there may be more surgery, or radiotherapy, or both. That is
a hard thing to hear while still recovering from the first operation, and the fact that it is a
probability statement rather than a verdict does not make it easier to hear. The reverse matters
too: a clear margin is genuinely good news, and it is routinely delivered with qualifications that
are accurate and land as doubt.

And the trade in the section above is somebody's body. A wider excision is not an abstract cost.
It is function, appearance, sensation, continence or speech, depending on the site, and the person
whose body it is has a legitimate view about where that trade should sit — a view that belongs in
the decision rather than after it. No threshold described here determines what happens to any
individual, and no figure of any kind appears in either half of this answer for that reason.

## What a Gym Leader is listening for

* The Itemfinder returns one bit about a window. Name the three things that makes a clear margin,
  and say which of them is the strongest.
* Flail reads 48ths and then a table of six. Which half of that is the pathologist and which half
  is the reporting standard?
* The OHKO moves are accuracy 30 and Sturdy refuses them outright. What is each of those two facts
  an analogy for?
* Why is tumour at the inked surface the entry at 1 rather than a very small margin?
* Substitute fails if you do not have the quarter to spend. Which clinical situation is that?
* Lock-On is checked before the accuracy roll. What does that say about how certainty is actually
  bought?
* Why does a clear margin say nothing about adjuvant systemic therapy?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific
to this answer:

* The dataset or minimum reporting standard your pathology service reports that specimen type
  against, published by the body that maintains it — for what is sampled, how, and which margins
  are reported. It is site-specific and it is the single most useful document here.
* The tumour–node–metastasis classification published by the Union for International Cancer
  Control, for the residual-disease classification and how it relates to the stage group.
* Your national or regional guidance for the specific disease, for the margin width currently
  regarded as adequate there and for what is recommended when a margin is involved. These differ
  between countries and have been revised.
* Your own institution's protocol for specimen orientation, intraoperative assessment and
  re-excision, which governs local practice.
* The primary literature, for the trials behind any particular threshold, which is where the
  revisions described in general terms above were settled.

The Pokémon side is in the opposite position and is sourced file by file in the closing note.

## Scope and safety

This is revision material about what a margin report means, dressed in a game so that the
difference between a sample and a surface stays concrete. It has had no clinical review. **No
margin width, threshold, sampling interval or recurrence figure appears here, and none should be
inferred** — those are site-specific, differ between countries and institutions, and have been
revised; the reporting standard and local protocol in force where you work are the authority, and
this is not. It is not a reporting guide and not a surgical decision aid, and it describes no
individual's specimen or situation. Anyone affected by cancer — their own diagnosis or someone
else's — should be talking to the clinical team looking after that person, who have the specimen,
the report and the history, none of which are here. The analogy carries measurement and reporting
only: no part of it stands in for a person, and none of it says anything about what happens to
anybody.

## Where this stands, October 2026

The Pokémon facts are read from the projects' own source. `HiddenItemNear` in the Red
decompilation walks the hidden-item coordinate table for the current map, tests the obtained-items
flags and skips anything already collected, and then compares the item's coordinates against a
window built by subtracting 5 with a clamp at 0 and adding 4 in one axis and 5 in the other — so
the window is asymmetric, and the source's own comment describes it as four to five tiles
depending on direction. `Cmd_remaininghptopower` in Emerald calls `GetScaledHPFraction` with a
scale of 48 and then walks `sFlailHpScaleToPowerTable`, whose six pairs are 1→200, 4→150, 9→100,
16→80, 32→40 and 48→20. Guillotine, Horn Drill, Fissure and Sheer Cold all carry `EFFECT_OHKO`,
power 1, accuracy 30 and 5 PP in Emerald's move data; `Cmd_tryKO` jumps to
`BattleScript_SturdyPreventsOHKO` when the target has Sturdy, and otherwise computes the chance as
the move's accuracy plus the level difference and requires the user's level to be at least the
target's. The accuracies quoted are Emerald's: Hydro Pump 80, Fire Blast 85, Thunder 70, Zap
Cannon 50. Rhydon learning Horn Drill at level 38 is from Emerald's level-up learnsets, and
Shedinja's base HP of 1 from its species data; Onix's ability list of Rock Head and Sturdy, and
its base HP of 35 against base Defense 160, are from Emerald's own species info. Blissey's bar
being the largest in the games is established in the pharmacology answer on pharmacokinetics in
this repository and is not re-derived here. `Cmd_setsubstitute` takes a quarter of maximum HP and
fails unless current HP exceeds that quarter, and `Cmd_accuracycheck` tests `STATUS3_ALWAYS_HITS`,
which Lock-On and Mind Reader set, before calculating accuracy. Sturdy's behaviour in later
generations is different and no later behaviour is claimed here.

The clinical reasoning is structural and will not date: a margin has always been a sampled,
converted, plane-bound measurement, and the three reasons it is probabilistic follow from how the
examination is done rather than from any current convention. The conventions themselves are the
only part that moves. Recommended widths have been revised in several diseases, generally
downwards as evidence accumulated that the local-control gain from additional tissue flattens, and
which revisions have been adopted differs by country and institution. The instruments are also
changing — intraoperative margin assessment, specimen imaging, and computational pathology applied
to margin reading are all active and unevenly available. No width, threshold or performance figure
is quoted here, deliberately. Those are the facts that date, and they belong to the current
reporting standard rather than to a revision note like this one.
