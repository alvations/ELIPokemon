---
id: "m039"
slug: nutrition-and-swallowing
style: pokemon
category: nursing
difficulty: intermediate
question: "What does a nutrition and swallowing assessment actually protect against, and what goes wrong when it is skipped?"
tags: [nutrition, dysphagia, aspiration, refeeding, screening]
---

# Swallow is a real move, and it fails outright if nothing has been stockpiled.

The games contain a three-move family that is almost absurdly well suited to this question, and it
is worth laying out exactly as the Advance code implements it.

**Stockpile** charges. It can be used up to **three** times and a fourth attempt is refused
outright. **Swallow** converts whatever has been stockpiled into HP: at one charge a **quarter**
of maximum HP, at two charges a **half**, at three charges **all of it** — and with **zero**
charges it **fails**, with its own failure message, doing nothing whatsoever. **Spit Up** takes
the identical store and fires it **outward** as damage, scaled by the same counter, and also fails
at zero.

One store. Two destinations. One of them is not nutrition.

```
   THREE SEPARATE QUESTIONS, and a Pokémon can fail any one while passing the others
   ──────────────────────────────────────────────────────────────────────────────────
   1  IS THERE A STORE?            Swallow with the counter at zero fails. There is
                                    nothing wrong with the move. There is nothing in it
   2  CAN IT GET THROUGH?          the store is fine, the move is fine, and something
                                    outside the Pokémon is blocking the route entirely
   3  DID IT GO THE RIGHT WAY?     Spit Up. Same charge, same counter, same Pokémon,
                                    and it comes out as damage instead of going in
   ──────────────────────────────────────────────────────────────────────────────────
   Collapse the three into one question — "is this Pokémon eating?" — and you get the
   classic failures: a full store nobody can reach, an empty store nobody noticed, and
   the one that went outward while the screen said a move had been used successfully.
```

## The store is fine and the route is shut

The games have at least four separate mechanics that produce an identical screen — the item
present, the effect absent — and they are not interchangeable:

```
   mechanic        the game's own printed text               what it actually blocks
   ──────────────  ────────────────────────────────────────  ──────────────────────────
   Unnerve         "Foes can't eat Berries."                 the act of eating. The
                                                              Berry is right there, it
                                                              is the correct Berry, and
                                                              it cannot be consumed
   Embargo         "Prevents the foe from using any items."   the whole route, for five
                                                              turns, from outside
   Magic Room      "Held items lose their effects for 5       the EFFECT, while leaving
                   turns."                                    the item visibly in place
   Heal Block      "Prevents the foes from recovering HP      the destination, not the
                   for 5 turns."                              supply
   ──────────────────────────────────────────────────────────────────────────────────────
   Four mechanisms. One appearance. "The right thing was prescribed" and "the right
   thing arrived" are different claims, and the item slot answers only the first.
```

**Unnerve** is the sharpest of the four and the most worth holding onto, because it is the one
where absolutely nothing is wrong with the supply. The Berry is in the slot. It is the right
Berry. The Pokémon cannot eat it, and the only thing on screen is a Pokémon that did not get
better.

## The confirmation that confirms nothing

**Zoroark** has **Illusion**, and the implementation is precise about both halves. On switching in
it displays the species of the **last conscious Pokémon in your party** — so the screen tells you,
confidently and in the normal place, that something is what it is not. And the disguise ends
**when the Pokémon takes damage**. Not when you look at the screen again. Not when you check
twice. Not when it does something plausible.

That is the entire problem with a bedside confirmation that is not a confirmation. A thing that is
in the wrong place can produce a completely reassuring display, and the only tests that break the
disguise are the ones that are actually a test. The absence of anything going visibly wrong is not
evidence, and the games will show you a Zoroark labelled as a **Blissey** for as long as you let
them.

**And the thing that already happened will not announce itself either.** **Future Sight** strikes
at the end of the second turn *after* it was used, and in between the field looks untouched — no
animation, no message, nothing on the HP bar. Harm that is already in motion and has not yet
appeared on the screen is the normal case rather than the exception.

## The move checks the precondition before it acts, and the refusal is the safety feature

Here is the part of the Swallow implementation that is easiest to skim past and is the most
important. The move does not simply run and produce a small result when the store is empty. It
**refuses**, with its own message, and it also refuses when the HP bar is already **full**. Two
preconditions, checked before anything happens.

**Belly Drum** is the same discipline on a much bigger action: it maximises Attack at the cost of
**half** the holder's maximum HP, and the code requires HP **strictly greater than half the
maximum** and Attack **not already at +6**. Fail either precondition and the move does not go
ahead at all.

A large intervention, gated on a state check made **before** it starts rather than after. The
games treat the refusal as the feature, not the inconvenience — and the moment that most needs a
check is the one that looks like progress, because that is the moment nobody is looking for a
reason to stop.

## The tiers, and the sixteenth nobody is getting

The route escalates in named steps, exactly as the healing items do: in the Advance games a
**Potion** restores 20, a **Super Potion** 50, a **Hyper Potion** 200, a **Max Potion** all of it,
and a **Full Restore** does HP and the status slot together. Each is a different route to the same
place, each has its own indication, and reaching for the biggest one is not the same as reaching
for the right one.

And the quietest failure in the set: **Leftovers** restores **a sixteenth** of maximum HP at the
end of every turn, and a Pokémon holding **nothing** gets nothing. There is no message for that.
No icon, no animation, no entry in any ledger — just a continuous input that is absent, on a
screen whose job is to report events. Food served and not eaten is a zero that nothing on the
summary page is designed to print.

## Where the picture runs out, before the part where it stops entirely

Two honest admissions, because the alternative is forcing a mapping.

The games have no mouth. There is nothing in them that corresponds to oral care, and the clinical
fact has to be said flat: what gets aspirated matters as much as whether aspiration happens, risk
is strongly associated with oral hygiene and with dependency for mouth care, and mouth care is
therefore a respiratory intervention rather than a cosmetic one. It is also among the first things
dropped on a busy shift. No analogy improves that sentence.

And there is no mechanic in which restarting something after a gap is itself the hazard. The
precondition checks above are the closest the games come, and they are a decent picture of *why*
you check first. They are not a picture of the physiology.

## Where the metaphor stops

Eating is not a clinical input. It is one of the ordinary pleasures and one of the most social
things people do, and it is tied to dignity and to identity. Nil by mouth is experienced as
deprivation, thickened fluids are widely disliked by the people drinking them, and being fed by
someone else is for many people the hardest part of being ill. None of that is a reason to take
risks with an unsafe swallow. All of it is a reason to treat the decision as being about a person
rather than about a route, to keep a restriction no longer than it has to be, and to take
seriously that someone may weigh the pleasure of eating against the risk differently than a
clinician would.

And the decisions about starting, continuing or withdrawing artificial nutrition and hydration in
advanced illness belong to the person whose life it is, with those close to them and the clinical
team, inside the law where they live. That is a legal and ethical matter, not a nursing task and
not a protocol. Nothing in this answer is guidance on it, there is no game in it, and a reader
facing one needs the relevant legal framework and the people involved rather than a revision note.

## What Nurse Joy is listening for

Which of the three questions a given finding actually answers. Why a move can be present, correct
and completely blocked from outside — and which of the four mechanisms that looks like. Why the
absence of anything visibly going wrong is not a confirmation, and what kind of test breaks the
disguise. Why the precondition check happens before the action and not after. What the local
escalation of routes actually is, and who decides. And where in the record the sixteenth that
nobody is getting would be written down, if anywhere.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to
this answer:

* The reader's national guidance on nutrition support in adults, for the screening requirement,
  the refeeding risk criteria and the starting-rate and monitoring recommendations — none of which
  is reproduced here.
* The reader's institutional nutrition and hydration policy, its screening tool, and its
  nil-by-mouth and nasogastric tube policies, including the confirmation method and who may
  confirm placement.
* The reader's national patient safety body's alerts on nasogastric tube misplacement, for the
  list of invalid confirmation methods and for the current confirmation standard.
* The international framework of standardised terminology and definitions for texture-modified
  foods and thickened liquids, for the descriptor levels.
* The reader's national stroke guideline, for the swallow screening requirement and its timing
  after stroke, which is where most screening practice originates.
* A standard anatomy and physiology textbook, for the phases of swallowing and for the refeeding
  mechanism, which are mechanism rather than guideline material.
* The primary literature and systematic reviews on thickened fluids and on oral care in pneumonia
  prevention — the two claims here most worth reading directly, because both are contested in
  magnitude.
* The capacity, best-interests and end-of-life legal framework of the reader's own jurisdiction,
  for decisions about artificial nutrition and hydration. This differs profoundly between
  countries and nothing here substitutes for it.

Separately, and unlike the above: the Stockpile cap, the Swallow fractions and both of its failure
conditions, the Spit Up scaling, the Belly Drum preconditions, the Illusion display and trigger,
the Future Sight timing, the Potion tiers and the Leftovers fraction were all read directly out of
the public disassemblies of the games and their expansion, which this environment could reach.
Every move and ability text in quotation marks above is the game's own printed description.

## Scope and safety

This explains what three assessments are for and how they fail, for someone already training in or
qualified for clinical practice. It is not a protocol, not a decision aid, and it deliberately
contains no screening thresholds, no feeding rates, no electrolyte values and no aspirate test
values — the only numbers in it belong to a video game. Those clinical values are set by national
and local guidance, they differ, and they are revised; the policy where someone works is the
authority and this is not. It has had no clinical review. Nothing here is for use in an emergency
or for a decision about any person's care, including any decision about what anyone should eat or
drink or about whether artificial nutrition should be started, continued or stopped. If someone is
unwell right now, the local emergency number is the correct response.

## Where this stands, October 2026

The anatomy and the refeeding mechanism do not move. Everything procedural does: screening tools
and their scoring, the refeeding risk criteria and starting rates, the texture descriptor
framework and its editions, the nasogastric confirmation standard, and the swallow screening
timings in stroke guidance. The evidence on thickened fluids and on oral care has continued to
accumulate without settling. And the legal framework governing decisions about artificial
nutrition differs by country and changes with case law, which is the part of this pair most likely
to be out of date first. Swallow, by contrast, has refused to work on an empty counter since
Hoenn.
