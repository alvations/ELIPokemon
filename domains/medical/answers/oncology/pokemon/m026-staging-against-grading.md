---
id: "m026"
slug: staging-against-grading
style: pokemon
category: oncology
difficulty: intermediate
question: "Staging and grading are two different axes. What does each describe, why are both needed, and in what sense is a staging system a communication protocol rather than a biological description?"
tags: [staging, grading, classification, communication, orthogonality]
---

# For three generations, the category was computed from the type

Open the data for any attack and you find two separate columns. One is its **type** — Fire, Water,
Steel. The other is its **category** — whether the calculation runs against the defender's Defense
or its Special Defense. Two columns. Two different questions. Neither is derivable from the other.

Except that for three generations, one *was* derived from the other, by a single integer
comparison, and the derivation got individual moves wrong. That is the whole of staging against
grading: two orthogonal descriptors, a long habit of reading one off the other, and a pile of
specific errors that habit produced.

Clinical claims below carry the same marks as the rigorous half: **mechanism**, **definitional**,
(**consensus**, **country-dependent**). Every Pokémon fact is read from the games' own data, and
the closing note says which file.

## The two columns, drawn

```
                        CATEGORY  (which defensive stat the maths uses)

                      PHYSICAL                 SPECIAL
                 ┌──────────────────────┬──────────────────────┐
     Fire        │  Fire Punch          │  Flamethrower        │
                 ├──────────────────────┼──────────────────────┤
  T  Water       │  Waterfall           │  Hydro Pump          │
  Y              ├──────────────────────┼──────────────────────┤
  P  Fighting    │  Close Combat        │  Focus Blast         │
  E              ├──────────────────────┼──────────────────────┤
     Steel       │  Iron Head           │  Flash Cannon        │
                 └──────────────────────┴──────────────────────┘

   Every row has both columns filled.  Every column has every row.
   Name the type and you still cannot name the category.  Name the
   category and you still cannot name the type.

   And they are consumed by DIFFERENT PARTS OF THE GAME.  The type
   is read by the Type Chart, against the defender's own types.  The
   category is read by the damage formula, to pick which of the two
   defensive stats to divide by.  Different reader, different table,
   different question.
```

## What the type encodes

The type answers *where this lands*. It is read against the defender's own types through the Type
Chart, it decides whether a hit is resisted, doubled or ignored outright, and it is what **STAB**
keys on. Alongside it, and recorded separately, sit **Base Power** and accuracy. Three fields, not
interchangeable and never summed into one, for the same reason that nodal involvement and distant
spread are recorded separately rather than added together (**definitional**) — they are different
statements and collapsing them destroys information.

Two features of the notation matter more than people expect.

* **A label has to say what registry it belongs to.** The same species carries a Hoenn number and
  a National number, and Emerald ships explicit conversion tables in both directions because a
  bare number is not a statement until you know which list it indexes. A clinical stage carries a
  prefix for the same reason: assessment before surgery, assessment from the resected specimen,
  and assessment after pre-operative systemic therapy are different measurements and are notated
  differently so they cannot be pooled (**definitional**).
* **The generation must be stated.** The Type Chart is not a constant. Two types did not exist in
  the first generation, one did not exist until the sixth, and Steel's resistances were trimmed on
  the way. The same move against the same defender is a different multiplier depending on which
  chart is in force. A clinical stage without its edition is the same kind of incomplete statement
  (**definitional**).

And some moves are not described by this scheme at all. In the Emerald data, Curse's type field is
**TYPE_MYSTERY** — index 9, sitting outside the eighteen battle types, because the thing it does
is not a typed hit and the scheme was never built to describe it. The lymphomas, the myelomas and
the chronic lymphocytic leukaemias sit outside the anatomical staging scheme in exactly that way:
a disease distributed through marrow and lymphatics does not carry the information an anatomical
map was designed to carry, so it is given its own framework instead of a forced slot in this one
(**consensus**).

## What the category encodes

The category answers *what kind of thing this is*, not where it lands. It picks which of the
defender's two defensive stats the calculation divides by — nothing else. It is a statement about
the character of the move, read from the move itself.

And like a grade, it is only meaningful against the thing it is being read against. The same
category label is a different statement depending on the defender's spread: **Special** means one
thing aimed at **Skarmory** and another aimed at **Blissey**, and no amount of staring at the
label tells you which. A grade is organ-specific in the same way — the schemes for prostate,
breast, central nervous system tumours and soft-tissue sarcomas are separate, maintained by
separate bodies, and a number in one is not the same statement as that number in another
(**definitional**, **consensus**).

## Why the Type Chart is a protocol and not a theory

This is the part usually skipped, and it is the point.

The Type Chart is **optimised for agreement, not for fidelity**. Nobody believes Fire is exactly
twice as effective on Steel as a matter of physics. The chart exists so that two players who have
never met mean the same thing by the same word, and every design choice follows from that
(**mechanism**):

* **The multipliers are discrete** — nothing, a half, one, two — although resistance is
  conceptually continuous. Discrete values can be agreed between two people; continuous ones
  cannot. A clinical staging system chops continuous extent into discrete groups for precisely
  this reason.
* **The inputs are observable at the time.** The game prints the result on the screen. The
  anatomical staging scheme is anatomical in origin rather than molecular for the same reason: it
  was built from what could be seen when the assessment was made.
* **It is versioned, and the version travels with the label.** Competitive play states its
  **Regulation** set in the invitation, because a team legal under one is illegal under the next.

Now the failure mode, which this game demonstrates better than any clinical example.

For three generations the category was not recorded. It was *computed*, by one comparison:
anything whose type index sat below TYPE_MYSTERY was physical, anything above it was special.
Which means **Fire Punch** — a punch, flagged in the data as making contact — ran off Special
Attack, because Fire's index is above the line. And **Shadow Ball**, a thrown ball of shadow, ran
off Attack, because Ghost's index is below it. The fourth generation gave every move its own
category field, and those moves were reassigned without one thing about them changing.

That is stage migration, exactly (**mechanism**). When the *investigation* improves — a more
sensitive scan, a more thorough nodal examination — people move into higher stage groups while
their disease stands still, and both the group they left and the group they joined look better
afterwards, because the group they left has lost its most advanced members and the group they
joined has gained its least advanced ones. Comparing **Blaziken**'s **Blaze Kick** across the
split is comparing two different numbers under one name, and comparing stage-for-stage figures
across an era of changing imaging is the same error with higher stakes.

## Where the axes are deliberately mixed

The games then went and blurred their own distinction, on purpose and usefully. **Body Press** is
a Fighting move whose damage is calculated from the user's Defense. **Psyshock** is a Special move
that divides by the defender's Defense. Both deliberately cross the columns, both are good design,
and both need to be *named* as the hybrids they are rather than filed under either heading.

Some current clinical schemes fold grade and tissue-based biomarkers into the stage group itself
for particular diseases (**consensus**, with (**country-dependent**) uptake). Same move. It is a
reasonable answer to anatomy under-predicting behaviour, it does blur the orthogonality this
answer opened with, and the honest position is that the result is a third thing — a prognostic
grouping, neither a stage nor a grade — which should be reported under its own name.

## Where the metaphor stops

A stage group and a grade describe a disease. They are not a forecast about a person, and nothing
in a game is a useful picture of that, so this part is said plainly and without the analogy.

A group statistic is an average over a large and varied population, assembled at some point in the
past, treated with the drugs and imaged with the scanners of that time. It does not contain the
information needed to say what will happen to any one person inside it. Any individual differs
from the average of their group in ways the average has no way to express, and those differences
are the things that actually matter — everything else going on in that person's body, what
treatment is available where they are, what they choose. That is a statement about what the
arithmetic can and cannot do. It is why no survival figure appears anywhere in either half of this
answer, and the absence is deliberate rather than an omission.

## What a Gym Leader is listening for

* Name a Fire move in each category, and a physical move in two different types. If either is
  hard, the two columns are still fused.
* Why is Base Power recorded separately from type instead of folded into one number?
* What broke when the category stopped being computed and started being recorded?
* Why does Curse's type field sit outside the eighteen battle types, and what is the clinical
  equivalent?
* What is lost by merging grade into a stage group, as well as what is gained?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md).
Specific to this answer:

* The current tumour–node–metastasis classification published by the Union for International
  Cancer Control, and the parallel staging manual published by the American Joint Committee on
  Cancer — for the category definitions, the prefixes, and the stage-grouping rules for a given
  disease site.
* The disease-specific grading scheme your pathology service reports against, as published by the
  body that maintains it — including the World Health Organization's classification series for the
  organ in question.
* Your national or regional cancer network's published staging and reporting standards, for which
  edition is in force locally and from when.
* The pathology report in front of you, for which prefix applies and therefore what the stage on
  it is a statement about.

## Scope and safety

This is revision material about how two classification axes are constructed, dressed in a game so
the orthogonality is concrete. It has had no clinical review. It is not a staging manual, it is
not a decision aid, and it describes no individual's situation. Staging and grading systems differ
between countries and institutions and are revised; the edition in force where you work is the
authority, and this is not. Anyone affected by cancer — their own diagnosis or someone else's —
should be talking to the clinical team looking after that person, who have the specimen, the
images and the history, none of which are here. And the analogy is for the shape of a
classification only: no part of this game stands in for a person, and none of it says anything
about what happens to anybody.

## Where this stands, October 2026

The Pokémon facts are from the games' own source. The macro that decided the category for three
generations is one line in Emerald's battle header — physical if the type index is below
TYPE_MYSTERY, special if above — and TYPE_MYSTERY is index 9 of eighteen in the type constants,
with Curse's own type field set to it. Fire Punch's and Shadow Ball's entries carry the types and
the contact flag quoted above, and the Hoenn-to-National conversion tables are in the same tree.
The fourth generation's split, the sixth generation's new type, and Terastallization are later
additions and are described from working knowledge of those games, not from code I opened.

The clinical structure — extent recorded separately from cellular appearance, combined into stage
groups by site-specific rules, versioned, with prefixes marking where the information came from —
is stable and has been for decades. The content moves: editions are revised, groups are redrawn,
and folding grade and biomarkers into prognostic groups is an active direction rather than a
settled one. No edition number, threshold or disease-specific rule is quoted here, deliberately.
Those are the facts that go out of date, and they belong to the classification currently in force
rather than to a revision note like this one.
