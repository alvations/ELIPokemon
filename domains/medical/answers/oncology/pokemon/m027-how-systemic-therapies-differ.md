---
id: "m027"
slug: how-systemic-therapies-differ
style: pokemon
category: oncology
difficulty: intermediate
question: "Cytotoxic chemotherapy, targeted therapy, endocrine therapy and immunotherapy work by different mechanisms. What are those mechanisms, and how does each one's toxicity profile follow from it rather than being arbitrary?"
tags: [chemotherapy, targeted-therapy, endocrine-therapy, immunotherapy, mechanism]
---

# Read the move's own data and the cost is already written in it

Four classes of systemic anticancer therapy, four mechanisms, four toxicity profiles — and the
toxicity is not a separate list to learn. In each class it is a consequence of the mechanism, and
the games happen to contain four mechanics with exactly these four shapes, written into the data
as plainly as a field in a struct.

A warning about what is being compared, because it matters here more than anywhere else in this
repository. **The objects of study below are moves, items, abilities and weather — not anybody who
receives them.** Nothing in this answer stands in for a person with cancer, and nothing about an
outcome is being dressed up as a game. The analogy is for why a mechanism has the consequences it
has, and it is dropped the moment the subject changes.

Clinical claims carry the same marks as the rigorous half: **mechanism**, **definitional**,
**consensus**, **country-dependent**.

## The shape of the argument

```
  CLASS          THE MECHANIC            WHAT IT KEYS ON           SO THE COST FALLS WHERE
  ─────────────────────────────────────────────────────────────────────────────────────────
  cytotoxic      Earthquake + recoil     BEING GROUNDED, and       on everything adjacent,
  chemotherapy                           the damage dealt          and back on the user in
                                                                   proportion to it
  ─────────────────────────────────────────────────────────────────────────────────────────
  targeted       Dream Eater             THE TARGET BEING          nowhere, if the condition
  therapy                                 ASLEEP — a precondition   is absent. The PP is spent
                                          checked before anything   and nothing happens.
  ─────────────────────────────────────────────────────────────────────────────────────────
  endocrine      removing the rain       A DEPENDENCY on an        across the whole field,
  therapy        from under Swift Swim    external signal, not      because weather was never
                                          a weakness                a single target's property
  ─────────────────────────────────────────────────────────────────────────────────────────
  immuno-        Sandstorm               NOTHING ABOUT SIDES.      on every Pokémon that is
  therapy                                 Its code checks types     not Rock, Steel or Ground,
                                          and never asks whose      and it outlasts whoever
                                          side anyone is on         started it
  ─────────────────────────────────────────────────────────────────────────────────────────

          ▲                                        ▲
          │                                        │
   four genuinely different                 and the last column is a
   mechanics, not four skins                CONSEQUENCE of the middle
   on one                                   one. No extra fact needed.
```

## Cytotoxic chemotherapy: Earthquake, and the recoil that is computed from the damage

Two facts from the data, and between them they are the whole class.

**One. Earthquake cannot be aimed.** Its target field in the Emerald data reads *foes and ally*.
There is no version of it that hits one thing. What it keys on is a property — being on the ground
— and every Pokémon on the field holding that property is in scope. **Flygon**, whose only ability
in that data is **Levitate**, takes nothing. A holder of an **Air Balloon** takes nothing until
the balloon is gone. The exemption is a property, never an identity, and nothing about the move
inspects who is who.

That is cytotoxic selectivity exactly (**mechanism**). Alkylating agents, platinum compounds,
antimetabolites, topoisomerase inhibitors and the spindle agents all key on a property: *this cell
is replicating its DNA or separating it right now*. Nothing in the agent recognises a cancer cell.
Normal marrow, gut lining, hair follicles and gonadal tissue hold the same property, so they are
in scope, and the toxicity profile is therefore a list of the body's fastest-turning-over tissues
rather than an arbitrary catalogue of side effects.

**Two. Recoil is calculated from the damage that landed.** **Double-Edge** is 120 base power and
its recoil, in the code, is the HP actually dealt divided by three. **Take Down** and
**Submission** take a quarter of it. Not a quarter of the base power, not a flat charge — a
fraction of the harm delivered. One property of the move produces both numbers. And if the hit
does nothing, the recoil is nothing, because there is no damage to take a third of.

That is the single sentence a cytotoxic agent is (**mechanism**): harm to the target and harm to
the host come out of the *same* property, so they cannot be separated by trying harder. A more
aggressive schedule does not buy selectivity; it buys more of both.

**Why there is a gap between cycles.** Put **Leftovers** on a Pokémon and it regains a sixteenth
of its maximum HP at the end of every turn. A side that recovers between exposures tolerates a
repeated hit that a side without recovery does not, and the interval is doing all the work. That
is the mechanistic basis of cycling (**mechanism**): normal proliferating compartments recover on
a known schedule, the tumour recovers less completely if the therapy is working, and the gap is
where the therapeutic window lives. It is not a scheduling convenience.

**And the part the analogy does not cover.** Several cytotoxics carry organ damage that
proliferation does not explain at all — cardiac, renal, auditory, nerve and pulmonary — and some
of it depends on the *total lifetime amount received* rather than on any one cycle, so it is
tracked cumulatively and does not recover in the gap (**consensus**). The games' nearest
equivalent is a **Life Orb**, which takes its tenth of maximum HP every time, regardless of how
much the attack achieved: a flat charge per exposure, which adds up. Dose-intensity-limited
against cumulative-dose-limited is the most useful distinction in this section, and the two items
make it concrete — a fraction of what you delivered, against a fixed charge for having delivered
anything.

## Targeted therapy: Dream Eater checks first, and does nothing if the answer is no

**Dream Eater**'s battle script is two instructions long before it decides anything. It jumps to
the working branch only if the target carries the sleep status. Otherwise it falls straight
through to *it had no effect* — and the PP has already been spent. The move is 100 base power and
against an awake target it is worth exactly zero.

That is the defining property of a targeted agent, and it is why biomarker testing is a
prerequisite rather than a refinement (**mechanism**, **consensus**). A targeted drug inhibits a
specific molecule the malignant cell has become dependent on: a kinase binding site, a surface
receptor, or a repair pathway whose loss is survivable for a normal cell and lethal for one that
has already lost another. Without the dependency the agent keeps every bit of its toxicity and has
lost its only route to benefit. Given blind, it is pure cost — a mechanistic statement, not a
rhetorical one. **Sucker Punch** is the same shape and fails for the same reason: the condition is
checked, and when it is absent the turn is gone.

**And the toxicity follows the target's day job** (**mechanism**). The reason this class has
narrow, characteristic profiles rather than the broad one above is that it is aimed at a molecule
— and the molecule has normal work elsewhere. A receptor that normal skin and gut epithelium also
use gives rash and diarrhoea. A pathway maintaining vascular tone and endothelial integrity gives
hypertension, proteinuria and impaired wound healing. A receptor the myocardium uses makes cardiac
function the thing to watch. Knowing where the target normally lives derives most of the list.

**Resistance is the target changing out from under you.** **Terastallizing** gives a Pokémon a
declared type that need not be either of its original two, and the careful matchup you chose stops
holding — the Pokémon is the same Pokémon and your reasoning about it is now wrong. Or the hit is
converted rather than resisted: **Flash Fire**, **Volt Absorb** and **Water Absorb** each take the
matching element and turn it into nothing or into a gain. Clinically: a secondary mutation at the
binding site, amplification of the target, a parallel pathway restoring the signal, or a phenotype
change that dissolves the dependency (**consensus**).

## Endocrine therapy: take the rain away and the multiplier goes back to one

**Ludicolo** has **Swift Swim**. In the rain its Speed is doubled — and in the turn-order code
that doubling is one multiplier, set to 2 while rain is up and 1 when it is not. **Chlorophyll**
does the same thing in harsh sunlight. **Kyogre** brings the rain with **Drizzle** and **Groudon**
the sun with **Drought**; take the weather away and the multiplier is 1 again.

Note what did *not* happen. Nothing hit **Ludicolo**. It is unharmed, unchanged, and exactly as
fast as it ever was on its own. What was removed was its dependence on something outside it — and
the moment rain returns, so does the multiplier.

That is endocrine therapy (**mechanism**). For a disease driven through a hormone receptor, the
strategy is to interrupt the signal rather than poison the cell: block the receptor, degrade it,
or cut off the ligand by suppressing the gland that makes it or the enzyme that synthesises it, in
combinations that depend on the disease and the physiological setting (**consensus**,
**country-dependent** in regimen choice). Three consequences, all mechanical:

* **It is largely cytostatic, so it is slower.** The effect accrues over longer periods, and in
  the post-operative setting treatment runs for years rather than weeks.
* **The toxicity is the physiology of the withdrawn hormone.** Weather was never one Pokémon's
  property — it is a field condition, and removing it changes the field. A hormone acts
  systemically, so withdrawing it is felt systemically: vasomotor symptoms, bone density loss,
  joint and musculoskeletal symptoms, effects on sexual function, metabolic and cardiovascular
  effects.
* **A modulator is not a pure antagonist.** Something that blocks a receptor in one tissue can
  partially activate it in another, which is why certain agents have tissue-specific effects a
  clean blocker does not (**mechanism**).

**And therefore adherence is a first-order lever**, in a way it is not for an infused agent given
in a day unit (**consensus**). A tablet taken daily for years is worth what its continuation is
worth, and the symptoms above are why continuation is hard.

## Immunotherapy: Sandstorm's code never asks whose side you are on

Read the sandstorm routine and the mechanism is unmistakable. At the end of every turn it takes a
sixteenth of maximum HP from each Pokémon on the field — unless that Pokémon is Rock, Steel or
Ground, or holds the one ability that exempts it. **Tyranitar**, which sets the weather with
**Sand Stream**, is Rock and takes nothing. Everything else is charged.

And here is the line that matters: **there is no check of which side anyone is on.** Not an
exception, not a special case. The condition is a field condition, the exemption list is a list of
types, and the question of ownership is never asked. The weather also keeps running after whoever
set it is no longer on the field.

That is why immune-related adverse events look like autoimmunity: **they are autoimmunity**
(**mechanism**). Checkpoint inhibitors are antibodies that block inhibitory signalling on T cells.
They are not cytotoxic; they remove a restraint and the immune system does the work. But the
restraint they remove is one that exists to hold back self-reactive T cells, so releasing it
systemically puts every organ in scope — colon, liver, lung, thyroid and pituitary and the other
endocrine organs, skin, joints, myocardium, nervous system. Three consequences follow from the
mechanism and not from a list:

* **It is not dose-proportional**, because the drug is not the thing doing the damage.
  **Trick Room** makes the same point from the other side: it reverses the order of action for
  everything on the field for several turns, and there is no smaller amount of it available — you
  changed the rules, not a target.
* **The latency is variable**, and an event can begin after treatment has finished — the weather
  outlasts the Pokémon that set it.
* **Some of it does not resolve**, endocrine organs in particular, which can need lifelong
  replacement (**consensus**).

**So the management is different in kind** (**mechanism**, **country-dependent** in protocol). The
answer to an immune-related adverse event is immunosuppression, and in some cases stopping for
good — not the dose reduction that answers a cytotoxic toxicity. You do not clear a sandstorm by
attacking less. Engineered cell therapies and T-cell-engaging antibodies add two further
mechanism-derived syndromes, from cytokine release and from neurological effects, each with its
own graded pathway.

One honest note on the mapping: **Magic Guard**, which Clefairy was given from the fourth
generation onwards, blocks indirect damage without touching the move's power — which is the shape
of supportive care, something that intercepts a cost without blunting the agent. It is a real
mechanic and a real principle, and it is not a promise that every cost has such an interceptor.
Most do not.

## Where the four categories leak

A teaching scheme, not a taxonomy of nature (**consensus**).

* **Antibody–drug conjugates** aim like a targeted agent and deliver a cytotoxic payload. The
  nearest thing in the games is **Sucker Punch** held by something wearing a **Life Orb**: the
  aiming is conditional and fails outright without its precondition, while the charge belongs to
  the item and not to the aiming. Clinically the toxicity has a target-dependent component and a
  payload-dependent component, and the payload part looks like chemotherapy because it is
  chemotherapy.
* **Some agents sit in two boxes**, because an antibody can recruit the immune system as part of
  how it works.
* **The word chemotherapy** is used colloquially for all of it, which is worth knowing when a
  conversation is plainly at cross purposes.

## Where the metaphor stops

Everything above is about mechanism, and the analogy earns its place there. What follows is about
people, so it is said plainly.

Mechanism predicts the shape of a toxicity profile. It does not predict what any one person will
experience, in what combination, or how much it will matter to them — and the things in that last
clause are not minor. The choice between these classes for a particular person turns on the
biology of their disease, on what is available and funded where they live, on everything else
going on in their body, and on what they themselves want from treatment. That is a different kind
of reasoning from this answer, done by people who have the information, and none of it is a puzzle
with a clean mechanical answer. Nothing here describes anyone's situation, and no part of a game
is a model of it.

## What a Gym Leader is listening for

* Derive a cytotoxic toxicity profile from first principles, then name an effect the
  dividing-tissue rule does not explain.
* Why does a gap between cycles help, mechanically?
* Why is a targeted agent without its target pure cost, in mechanistic rather than regulatory
  terms?
* Why is dose reduction the wrong instinct for an immune-related adverse event?
* Why does adherence matter more in endocrine therapy than in infused therapy?
* An antibody–drug conjugate has two sources of toxicity. Which is which?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md).
Specific to this answer:

* The summary of product characteristics, or equivalent national prescribing information, for any
  specific agent — the authority for its mechanism, its licensed indications and its
  adverse-effect profile.
* Your national formulary and your centre's own systemic anticancer therapy protocols, for
  regimens, cycle structures and local toxicity-management pathways.
* The published management guidance for immune-related adverse events issued by your national or
  regional oncology professional body, and your centre's local version of it.
* The pharmacology section of a current standard oncology textbook, for the class-level mechanisms
  described above.

## Scope and safety

This is revision material about mechanism, dressed in a game so the four mechanisms stay distinct.
It has had no clinical review. No dose, regimen, schedule or monitoring interval appears here, and
none should be inferred; the formulary and the local protocol are the authority, and this is not.
Regimen choice, availability and toxicity-management pathways differ by country, region and
institution, and they change. Nothing here describes any individual's situation. Anyone affected
by cancer — their own diagnosis or someone else's — should be talking to the clinical team looking
after that person, who know the disease, the treatment and the history, none of which are here.
The analogy covers mechanism and stops there: no Pokémon in it stands in for a person, and nothing
in it says anything about what happens to anybody.

## Where this stands, October 2026

The Pokémon facts are read from the games' own source. Earthquake's target field is *foes and
ally* and its base power is 100; Double-Edge is 120 with recoil set to the HP actually dealt
divided by three, and Take Down and Submission to a quarter of it; Sandstorm charges a sixteenth
of maximum HP at the end of each turn, exempts Rock, Steel and Ground and one ability, and its
routine contains no test of which side a Pokémon is on; Dream Eater's script jumps to its working
branch only on the sleep status and otherwise reports no effect; the Swift Swim and Chlorophyll
speed multiplier is set to 2 only while the matching weather holds; Flygon's ability is Levitate
in both slots, Tyranitar's is Sand Stream, Kyogre's is Drizzle, Groudon's is Drought and
Ludicolo's is Swift Swim. Life Orb, Air Balloon, Magic Guard, Trick Room and Terastallization are
later-generation additions described from working knowledge of those games rather than from code
opened here, and the note about Clefairy gaining Magic Guard in the fourth generation is flagged
for the same reason.

The clinical side — four mechanisms, each toxicity profile derived from its mechanism — is
long-standing and is the part of this answer that will still be true in ten years. The contents of
each box are not: new targets, new conjugate payloads and new cell therapies arrive continuously,
and what is available and funded differs sharply by country. No agent is named, no trial is cited
and no number appears, deliberately. Those facts date, and they belong to the prescribing
information and the local protocol rather than to a revision note like this one.
