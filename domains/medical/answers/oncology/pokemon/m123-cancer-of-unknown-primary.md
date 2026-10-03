---
id: "m123"
slug: cancer-of-unknown-primary
style: pokemon
category: oncology
difficulty: advanced
question: "When the primary site of a cancer cannot be identified, what in oncological reasoning stops working, and what carries the decision instead?"
tags: [unknown-primary, immunohistochemistry, diagnostic-reasoning, bounded-workup, favourable-subsets]
---

# Snorlax's Body Slam into a Wailmer is neutral, and nothing in the game found that out

Everyone thinks the type chart is a chart. It is not. In the third generation it is a hand-written
list of rows, and a great many of the squares you imagine on that grid have no row at all.

Count it. Leaving aside the unusable ninth slot, seventeen types take part in battle, which is two
hundred and eighty-nine ordered attacker-and-defender pairs. The list holds **one hundred and
ten**. The other one hundred and seventy-nine are not entered anywhere.

So here is **Snorlax**, pure Normal, using **Body Slam** — eighty-five base power, perfect
accuracy — against a **Wailmer**, pure Water. Normal against Water is not one of the hundred and
ten. The list is walked from the top, nothing matches, and **the match-up contributes nothing to
the number at all**. Then Wailmer answers with **Surf**, and Water against Normal is not in the
list either. Try **Gardevoir**'s **Psychic** into Snorlax: Psychic against Normal, also absent.
**Machamp**'s **Cross Chop** into a **Hariyama**: Fighting against Fighting, absent.

Four exchanges, four empty lookups. Each of those four attackers does get its same-type bonus,
because that is read off the attacker's own typing before the list is ever consulted — so the
damage is not *neutral*, it is **unmodified by the pair**, and those are different statements.
Nothing is printed. No flag is set. And what comes out is indistinguishable from what you would
get off a genuine row that happened to say *ordinary*. **A default and a lookup produce the same
output, and nothing downstream can tell them apart.**

That is cancer of unknown primary, and it is the whole answer. Oncology is lookup machinery keyed
on one field — the site of origin — and when the field is empty the machinery does not return an
error. It is never opened, and the decision gets made by whatever is left.

The house device of a type match-up as a hard zero belongs to the pharmacology and emergency
answers that established it, and this answer is not reusing it. **Nothing here is about a zero.**
It is about the squares with nothing in them at all, which is a different and quieter failure.

As elsewhere in this specialty, **the objects of study are tables, keys and defaults.** No Pokémon
in this answer stands in for a person, and the analogy is dropped entirely at the end.

Clinical claims carry the same marks as the rigorous half: (**mechanism**), (**definitional**),
(**consensus**), (**country-dependent**).

## What is keyed on the match-up, and what is not, drawn

```
   KEYED ON THE PAIR — the field that may be missing

      ┌─ the hand-written list of rows ───────────────────────────────────┐
      │  110 rows.  289 possible ordered pairs.  179 with NO ROW.         │
      │  Normal→Water, Water→Normal, Psychic→Normal, Fighting→Fighting,   │
      │  Ghost→Water, Dark→Water ... all absent, all silently ordinary    │
      │                                                                   │
      │  and one slot, the unusable ninth, that is NAMED and has no rows  │
      │  anywhere — the ??? type, counted in the total, used by nothing   │
      └───────────────────────────────────────────────────────────────────┘

   NOT KEYED ON IT — readable with the pair unknown

      the attacker's OWN typing    ─ Gengar is Ghost, so Shadow Ball gets the
                                     same-type bonus.  Read BEFORE any lookup.
      base power                   ─ Hydro Pump 120, Body Slam 85, Uproar 50
      accuracy                     ─ Thunder 70, Cross Chop 80, Blizzard 70
      PP                           ─ Cross Chop 5, Foresight 40
      who it hits                  ─ Surf both, Earthquake everything adjacent
      the flags                    ─ contact, protect, sound, King's Rock

   NAMED EXCEPTIONS, outside the list, written by hand

      Gengar's LEVITATE     tested in an `if` that REPLACES the whole walk
      Claydol and Baltoy    the same ability, same bypass
      Shedinja's WONDER GUARD  tested afterwards, on what the walk produced

   ═══════════════════════════════════════════════════════════════════════════

   THE FAILURE MODE

      the damage number carries no provenance.  Nothing in it says whether
      a row matched, no row existed, or Levitate fired instead of the walk.

      Clinically:  "metastatic adenocarcinoma, treated with ..." says
      nothing about whether the organ-first machinery was ever entered.
```

## What is keyed on the primary site, and how much of the specialty that is

Worth stating at full length, because the amount of machinery involved is what people
underestimate.

The staging classifications are written one per disease site. The guidelines are indexed by site.
The trials recruited by site. Many drug authorisations name a site. The multidisciplinary meetings
are constituted by site, with the pathologist, the radiologist and the surgeon who deal in that
organ. Screening programmes are per site. Even the vocabulary is per site: this specialty's answer
on staging against grading makes the point that a grade in one organ and the same number in
another are different statements (**definitional**).

Cancer of unknown primary is the situation where the key is absent: a malignancy confirmed on
histology, with evidence of spread, where the site of origin is not identified after an adequate
initial investigation (**definitional**, with what counts as adequate strongly
(**country-dependent**)).

And the list shows why that is harder than it sounds. One hundred and seventy-nine missing pairs,
and the engine is not embarrassed by one of them. A guideline keyed on a site you do not have does
not refuse to answer; it is never consulted, and the output looks ordinary.

## What is still readable when the pair is unknown

The walk through the list is not the only thing that happens when a move is used, and the parts
that do not consult it are where this answer's clinical content lives.

**The same-type bonus is read off the attacker, before the list is touched.** **Gengar** is Ghost
and Poison, so **Shadow Ball** — eighty base power, perfect accuracy — gets the one-and-a-half
multiplier the instant the move is declared, with no reference to what it is pointed at. That is a
property of the thing doing the acting. **Lineage is readable when the match-up is not.**

Clinically this is the first fork and the most consequential: whether the thing is a carcinoma, a
lymphoma, a melanoma, a sarcoma or a germ-cell tumour determines which treatment family is even
relevant, and several of those are highly treatable in a way the others are not (**mechanism**,
**consensus**). A panel of immunohistochemical stains is the instrument, read as a pattern rather
than as a set of independent yes-or-no results. And within carcinoma the subtype —
adenocarcinoma, squamous, neuroendocrine, poorly differentiated — is available from the specimen
and attracts different treatment (**definitional**, **consensus**).

**Every other field of the move is readable too.** **Hydro Pump** is a hundred and twenty base
power at eighty accuracy with five PP. **Thunder** is a hundred and twenty at seventy.
**Blizzard** is a hundred and twenty at seventy. **Cross Chop** is a hundred at eighty with five
PP. **Uproar** is fifty at perfect accuracy. **Foresight** has no power at all and forty PP. Not
one of those numbers depends on who is being hit. This specialty's answer on how the systemic
therapies differ built its whole argument on reading a move's own data and finding the cost
already in it, and all of that is still there with the match-up blank.

The clinical analogues, in order of how much they carry:

* **The distribution of disease.** This specialty's answer on how a cancer spreads derives
  organ-specific patterns from venous and lymphatic drainage, and the argument runs backwards: a
  pattern of involvement constrains the plausible origins, because whatever is first downstream of
  a site is where its cells arrive (**mechanism**). Squamous carcinoma in upper cervical nodes,
  adenocarcinoma confined to one axilla, disease confined to the peritoneum — each is a
  distribution before it is anything else. The game's version is which battlers a move can reach:
  **Surf** hits both opposing slots, **Earthquake** hits everything adjacent including your own
  partner, and **Spikes** reaches a side rather than a creature. Reach is a readable field.
* **Grade, and the rate of change.** Both readable, both relevant, neither keyed on a site.
* **Fitness**, which this specialty's answer on performance status places on an axis of its own,
  and which the missing field does not touch at all.
* **Specific molecular alterations**, where present — and this specialty's answer on
  biomarker-driven treatment selection describes the one place where the missing key costs nothing
  whatsoever (**consensus**, strongly (**country-dependent**) in what is available).

Two further things are easy to forget. **The specimen is a limited sample**, with the limitations
this specialty's answer on tumour heterogeneity and the single biopsy describes; a panel run on
too little material returns an equivocal pattern rather than a wrong one. And **the clinical
history** — previous excisions, a lesion removed years ago and not followed up, previous imaging —
occasionally supplies the field directly, which is why it is asked for before the panel is
extended (**consensus**).

## The walk is bounded, and it is bounded by a marker somebody wrote

Here is the part people do not expect. The walk does not stop when it finds the answer.

It cannot, because **Shedinja** is Bug and Ghost, **Sableye** is Dark and Ghost, **Claydol** is
Ground and Psychic, and a dual-typed target needs two separate matches that may sit anywhere in
the list. So the engine walks every row of all one hundred and twelve, every time, for every
damaging move in every battle, and it stops because the last row is a hand-written end marker.
**The search terminates because somebody wrote a terminator, not because the search succeeded.**

That is the discipline of the bounded workup, and the bound is not a resource argument.

**Further investigation is justified only where its result would change management**
(**mechanism**). If the treatment offered would be the same whichever of three candidate origins
is correct, establishing which one costs time and buys nothing. The emergency-medicine answer on
imaging as a test with a harm of its own makes the general version; this specialty's and general
practice's answers on overdiagnosis make the version about what additional looking generates.

**The search has its own harms.** Repeated cross-sectional imaging and endoscopy carry procedural
risk and radiation exposure, they generate incidental findings that demand their own
investigation, and all of it takes time during which no treatment is happening (**mechanism**,
**consensus**).

**So the recognised framing is a defined initial workup, after which the diagnosis is made.**
Cancer of unknown primary is a diagnosis reached after an adequate investigation rather than a
label for an incomplete one, and that distinction is the entire clinical content of the definition
(**definitional**). What counts as adequate differs between countries and is set out in national
guidance — typically histology with an immunohistochemical panel, cross-sectional imaging, and
investigation directed by the pattern and the lineage, with further tests added only where a named
hypothesis predicts their result (**consensus**, **country-dependent**). A test ordered because
the primary has not been found yet, rather than because a hypothesis predicts what it will show,
is the characteristic error of this presentation.

## The ??? type: a slot with a number and nothing behind it

The cartridge has a name for the unclassifiable, and gives it nothing to do.

Between Steel and Fire, in the middle of the type enumeration, sits the unused ninth slot — the
one the games have never shown a player and the fan community calls the **??? type**. It is
counted in the total number of types. It has a constant of its own. And it has **not one row in
the list**. A move of that type would be walked against all one hundred and twelve rows, match
nothing, and emerge exactly ordinary with no message printed.

It is also actively stepped over. This specialty's answer on performance status found the same
slot from the other side: **Hidden Power**, whose type is computed at the moment of use rather
than stored, increments past the ninth value when its arithmetic lands there, because the result
is not usable as a battle type. Somebody had to write that skip.

So the cartridge is in precisely the clinical position. It has a category for *not one of the
recognised ones*. The category is formally defined, it occupies a slot in the classification, and
every instrument downstream treats it as the default rather than as a distinct thing. Naming the
category did not make the machinery handle it.

## The named exceptions, and what a favourable subset actually is

Two things sit outside the list entirely, handled by identity, and both are instructive.

**Levitate replaces the walk.** If the target has it and the move is Ground-typed, the engine
never looks at the list at all: it jumps straight to its own message and its own result.
**Gengar** has Levitate in the third generation, and so do **Claydol** and **Baltoy**. That is not
a row. It is a hand-written branch sitting in front of the general machinery because somebody
decided this case deserved its own path.

**Wonder Guard is the mirror image**, tested after the walk rather than before it, reading what
the walk produced. **Shedinja** is its only holder, and the device is used here purely as a
type-override with nobody's resilience as the subject — the use this corpus's conventions permit.

That is what a **favourable subset** is. A minority of unknown-primary presentations are not
undifferentiated problems at all; they are recognisable patterns that behave like a known disease
and are managed as that disease despite the absent field (**consensus**). This is the part of the
topic most worth learning, because management and outlook differ substantially from the general
case. The mainstream list, as a current textbook would give it:

* squamous carcinoma confined to cervical nodes, managed along the lines of a head and neck
  primary;
* adenocarcinoma confined to axillary nodes in a woman, managed along the lines of a breast
  primary;
* adenocarcinoma confined to the peritoneum in a woman, managed along the lines of a tubal or
  ovarian primary;
* poorly differentiated carcinoma with a midline distribution in a younger person, where a
  germ-cell origin is considered and treatment follows that family;
* neuroendocrine neoplasms, which have their own treatment family independent of site;
* adenocarcinoma with bone metastases in a man, where a prostatic origin is considered and the
  relevant immunohistochemical and serum markers are checked;
* a single site of disease that is resectable or treatable with local therapy, where the local
  treatment is offered on its own merits.

Every entry is **a distribution combined with a lineage** — exactly the two things the earlier
section established are still readable. The subsets are not exceptions to the reasoning; they are
what the reasoning produces when the distribution is distinctive enough to substitute for the
missing field (**mechanism**). And Gengar's Levitate makes the organisational point too: that
branch exists because a person wrote it. Nothing *finds* a favourable subset automatically.
Somebody has to ask the question.

Outside those subsets, treatment is empirical and chosen on lineage and fitness, and that is where
practice varies most and the evidence is weakest (**consensus**, **country-dependent**).

## One barrier you can remove, and one you cannot

The list has one more structure worth reading, and it is the same shape this specialty's answer on
how a cancer spreads found in the table of moves Mimic may not copy: a conditional marker sitting
in the middle of a hand-written list, so that the rows after it are read only sometimes.

The rows after that marker are the two that make Ghost-types untouchable by Normal and Fighting
moves. **Foresight** and **Odor Sleuth** — no power, perfect accuracy, forty PP each, the same
effect under two names — set a flag that makes the walk stop at the marker, so those two rows are
never reached. Use Foresight on a Gengar and **Machamp**'s Cross Chop connects.

And the mirror row sits *before* the marker: Ghost against Normal. **Shadow Ball** off a Gengar
into a Snorlax is zero whatever anybody does, because no flag reaches a row read unconditionally.

Two barriers, one list, and the only difference is which side of a hand-written marker the row
landed on. Clinically that is the difference between a feature of the disease you cannot change
and a state you can alter before you start — and in this topic it is the difference between the
subsets where a lineage result opens a door and the ones where it closes one.

## The default that does not announce itself

The damage number is a number. It carries no field saying whether a row matched, whether no row
existed, or whether Levitate fired instead of the walk. The next step consumes it either way.

Clinically the record reads: a histological description, a pattern of spread, and a treatment.
**Nothing in that sentence distinguishes a decision made with the key from one made without it**
(**mechanism**). Three failure modes follow, all documented in practice:

* **An assumed origin hardens into a stated one.** A plausible hypothesis recorded once as a
  possibility reappears in the next letter without its hedge, and three letters later it is the
  diagnosis. This is the nursing answer's documentation argument in its most consequential form.
* **The favourable subsets are missed**, because recognising one needs somebody to ask whether
  this distribution plus this lineage is a pattern, and nothing in the pathway asks.
* **The limits of the workup are not carried forward.** A later clinician cannot tell from the
  record whether the primary was looked for thoroughly and not found, or looked for briefly — two
  different situations with different implications for repeating anything.

The remedies all consist of writing things down: record that the primary is unidentified rather
than naming a presumed one; record what was done to look; record the panel and what it did and did
not support; and record whether the presentation was assessed against the favourable subsets
(**consensus**).

## Where tissue-of-origin profiling has and has not changed this

Honest statement of an unsettled area, because asserting either side would be wrong — and the
cartridge supplies no device for it, which is worth saying rather than inventing one.

Molecular classifiers — gene-expression and methylation profiling — can assign a predicted tissue
of origin from a specimen, and are used in some services (**consensus**, (**country-dependent**)).
Whether directing treatment according to that prediction improves outcomes compared with empirical
treatment chosen on lineage has been tested, and the results have not settled the question;
practice differs substantially between countries and centres (**consensus**,
**country-dependent**).

What has changed the reasoning more is the other route. Where a treatment is indicated by a
molecular alteration irrespective of the tissue it arose in, the missing field stops mattering for
that decision entirely — the inversion this specialty's answer on biomarker-driven treatment
selection describes. For a subset of these presentations, broad molecular profiling is not an
attempt to recover the key but a route that does not need one (**consensus**, strongly
(**country-dependent**)).

## Where the metaphor stops

Everything above is lists, keys, end markers and hand-written exceptions, and the cartridge is a
good place to see them because you can count the missing rows. What follows is about people, so
the analogy stops and nothing below leans on it.

Being told that you have cancer and that nobody can say where it started is a specific and
unusually hard thing to be told. Almost everything a person has ever heard about cancer is
organised by organ: the word is the handle for everything else — what to read, which charity,
which support group, which question to ask. Without it people are left holding a diagnosis they
cannot look up, and the commonest reaction is to assume the not-knowing is a failure of effort,
either theirs or the team's. It is usually neither.

Two things help and both are about language. The first is saying explicitly that this is a
recognised situation with a name and a pathway, rather than an unfinished investigation — people
frequently believe tests are still pending when the diagnosis has in fact been reached. The second
is saying what the search was, what it ruled out, and why it stopped, because *we stopped looking*
sounds like giving up and *further tests would not change what we would offer* does not, and the
second is the accurate one when it is true.

The repeated biopsies and scans are their own burden, and so is the number of different clinicians
a person meets when no single site-specific team owns the problem. Where a named unknown-primary
or acute oncology service exists, having one team is the main thing it provides, and it matters
more than its diagnostic yield.

Nothing in either half of this answer says anything about what will happen to any individual, and
no clinical figure of any kind appears in either half. Both omissions are deliberate. And nothing
in the game stands in for a person: the subject throughout has been a lookup with a missing key.

## What a Gym Leader is listening for

* Snorlax's Body Slam into a Wailmer comes back ordinary. Why is *how* it came back ordinary the
  whole clinical point?
* One hundred and ten rows, two hundred and eighty-nine possible pairs. Why is the gap worse than
  a wrong answer?
* Gengar's Shadow Ball gets the same-type bonus before the list is consulted. Which clinical step
  is that, and why is it the first fork?
* The walk runs to the end marker every time rather than stopping at a match. What does that say
  about how a diagnostic search should terminate?
* The ??? type is counted in the total and has no rows. What does naming a category and giving it
  no behaviour cost?
* Levitate is a branch in front of the walk rather than a row inside it. What is the clinical
  version, and what has to happen for one to be recognised?
* Foresight reaches the Fighting-into-Ghost row and nothing reaches the Ghost-into-Normal one.
  What is the clinical difference between those two barriers?
* The damage number carries no provenance. Name the three failure modes that follow clinically.
* Where does the cartridge supply no device at all here, and why is saying so better than
  inventing one?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific to
this answer:

* Your national guideline on metastatic malignancy of unknown primary origin, from the body that
  issues guidelines where you work. It defines what counts as an adequate initial workup in your
  system, and that definition is the clinical content of the diagnosis. It differs between
  countries.
* Your own service's pathway for this presentation, including whether a named team or an acute
  oncology service holds it, and which multidisciplinary meeting discusses it.
* The published guidance on immunohistochemical panels for the undifferentiated malignancy from
  the pathology body that issues it in your region. The panels and their interpretation are the
  pathologist's territory.
* A current standard textbook of the specialty, for the favourable subsets. The list above is the
  textbook list and the textbook is where the management of each belongs.
* Your national guidance on molecular profiling and on access to treatments indicated by an
  alteration irrespective of tissue of origin, which determines what is available to offer and
  differs sharply between countries.
* The primary literature, for the trials of treatment directed by a predicted tissue of origin
  against empirical treatment. This is the claim here most likely to have moved.

The Pokémon side is in the opposite position and is sourced file by file in the closing note.

## Scope and safety

This is revision material about diagnostic reasoning when the organising fact is missing, dressed
in a game so that a silent default stays visible. It has had no clinical review. **It is not a
diagnostic algorithm and must not be used as one**, and no immunohistochemical panel, marker,
threshold, imaging protocol or treatment regimen appears here, deliberately — the panels belong to
the pathology standard, the adequate workup is defined nationally and differs between countries,
and both are revised; the guideline and pathway in force where you work are the authority and this
is not. It says nothing about what will happen to any individual and describes no individual's
situation. Anyone affected by cancer — their own diagnosis or someone else's — should be talking
to the clinical team looking after that person, who have the histology, the imaging and the
history, none of which is here. The analogy carries table lookups and defaults only: no part of it
stands in for a person, and no creature's situation is the subject of any sentence in it.

## Where this stands, October 2026

The Pokémon facts are read from Emerald's own source and nothing here is claimed about any
generation but the third. `gTypeEffectiveness` in `src/battle_main.c` is declared `const u8
gTypeEffectiveness[336]` — one hundred and twelve three-byte rows, of which one is
`TYPE_FORESIGHT, TYPE_FORESIGHT, TYPE_MUL_NO_EFFECT` and the last is `TYPE_ENDTABLE,
TYPE_ENDTABLE, TYPE_MUL_NO_EFFECT`, leaving one hundred and ten data rows.
`include/constants/pokemon.h` gives `TYPE_MYSTERY` as nine and `NUMBER_OF_MON_TYPES` as eighteen,
so seventeen types take part in battle and two hundred and eighty-nine ordered pairs are possible;
`TYPE_MYSTERY` appears nowhere in the table. Enumerating the rows and subtracting gives one
hundred and seventy-nine absent pairs, among them Normal into Water, Water into Normal, Psychic
into Normal, Fighting into Fighting, Ghost into Water and Dark into Water. `Cmd_typecalc` in
`src/battle_script_commands.c` returns early for Struggle, applies the same-type one-and-a-half
multiplier from `IS_BATTLER_OF_TYPE(gBattlerAttacker, moveType)` before any lookup, handles
`ABILITY_LEVITATE` against a Ground-typed move in an `if` whose `else` is the entire walk, walks
to `TYPE_ENDTABLE` calling `ModulateDmgByType` once per matching defending type, breaks out at the
`TYPE_FORESIGHT` marker when the target carries `STATUS2_FORESIGHT` and otherwise steps over it,
and tests `ABILITY_WONDER_GUARD` afterwards against the flags the walk set. `ModulateDmgByType` is
reached only on a matching row, so an absent pair leaves the damage and the result flags
untouched. `TYPE_GHOST, TYPE_NORMAL` sits before the marker; `TYPE_NORMAL, TYPE_GHOST` and
`TYPE_FIGHTING, TYPE_GHOST` sit after it. The mid-list conditional marker is the same structure
this specialty's answer on how a cancer spreads found in `sMovesForbiddenToCopy`, and it is named
here rather than re-derived. From `src/data/battle_moves.h`: Body Slam eighty-five power, Normal,
accuracy one hundred; Surf ninety-five power, Water, hitting both opposing slots; Psychic ninety
power; Cross Chop a hundred power at eighty accuracy with five PP; Shadow Ball eighty power,
Ghost, accuracy one hundred; Hydro Pump a hundred and twenty at eighty with five PP; Thunder a
hundred and twenty at seventy; Blizzard a hundred and twenty at seventy; Uproar fifty at one
hundred; Earthquake a hundred power reaching foes and ally; Spikes no power, no accuracy,
targeting the opponents' field; and Foresight and Odor Sleuth both `EFFECT_FORESIGHT`, no power,
accuracy one hundred, forty PP. From `src/data/pokemon/species_info.h`: Snorlax Normal with
Immunity and Thick Fat, Wailmer pure Water, Gardevoir pure Psychic, Machamp pure Fighting,
Hariyama pure Fighting, Gengar Ghost and Poison with Levitate, Claydol and Baltoy Ground and
Psychic with Levitate, Shedinja Bug and Ghost with Wonder Guard, Sableye Dark and Ghost. The ???
name for the unused ninth slot is community usage and is not a string in the source.

The clinical reasoning will not date in its structural half: a specialty organised by one field
behaves differently when that field is empty, the instruments downstream fail silently rather than
loudly, a pattern of spread plus a lineage is what remains readable, and a test that cannot change
management is not worth doing. Two things are moving. The adequate initial workup is being revised
as imaging and pathology change, and national definitions of it have never agreed with each other.
And the place of molecular profiling is unsettled in both of its forms — as a route to a predicted
tissue of origin, where the evidence has not settled the question, and as a route to a treatment
indicated irrespective of tissue, which is expanding and depends strongly on what is reimbursed
where you are. The favourable subsets are the stable part of the topic. No panel, marker or
regimen is quoted here, deliberately.
