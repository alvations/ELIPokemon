---
id: "m035"
slug: first-aid-for-untrained-bystanders
style: serious
category: emergency
difficulty: intermediate
question: "Why is first-aid guidance for untrained bystanders different in kind from clinical guidance, rather than just simpler?"
tags: [first-aid, bystander, guidance-design, simplification, dispatcher]
---

# A different reader means a different objective, which means a different document

Clinical guidance and bystander first-aid guidance are not the same document written at two
reading levels. They optimise different quantities over different populations, and that is why one
is conditional and detailed while the other is short and flat. **(Mechanism** — the argument is
about what each document can assume about its reader, and it is checkable by reasoning.**)**

Clinical guidance can assume a reader who recognises which branch of the guidance they are in, who
can tell when they have taken the wrong branch, and who can recover from having done so. Under
those assumptions conditionality is cheap and it buys accuracy, so adding a branch is close to
free and almost always worth it.

Bystander guidance has a different reader: untrained, frightened, acting once in a lifetime, with
no feedback, no supervision, and — the decisive point — **no way to detect that the branch they
chose was the wrong one**. The quantity being optimised is therefore not the outcome achievable by
a reader who applies the document correctly. It is the **expected outcome across everybody who
will attempt it**, including everyone who misreads it, remembers it imperfectly, and applies it to
a situation it was not written for. A different objective function produces a genuinely different
document, not an abridged one.

## Four consequences of that objective

```
   assumption about the reader          clinical guidance    bystander guidance
   ───────────────────────────────────────────────────────────────────────────────
   can identify which branch applies    yes                  no
   can detect a wrong branch            yes                  no
   can recover from a wrong branch      usually              no
   will act more than once              yes                  probably never again
   has supervision or feedback          yes                  no
   ───────────────────────────────────────────────────────────────────────────────
   therefore: branches are              cheap, so add them   expensive, so remove them
              the optimisation target   best case            whole distribution
```

* **Minimise branching, even at a real cost in accuracy.** Every decision point is a place the
  reader can go wrong and not know it. A branch that improves the outcome for the minority who
  identify it correctly and worsens it for the majority who do not is a net harm, however good the
  branch is on its own terms. Branches therefore get collapsed, and the accuracy lost is accepted
  on purpose.
* **Prefer actions whose failure mode is benign.** The selection criterion is not *best if done
  correctly*, it is *least bad across the distribution of how it will actually be done*. An action
  that is somewhat less effective but almost impossible to make worse beats a more effective one
  with a bad tail.
* **Accept a lower ceiling to raise the floor.** This is question m032's variance argument at its
  most extreme, because a bystander population has the widest variance of any population of
  readers. The document's job is to truncate the left tail.
* **Bias the recognition step toward acting.** Recognition is where untrained readers fail most
  and it is also where the stakes concentrate, and the costs are wildly asymmetric: not starting
  when something was needed is far worse than starting when it was not. So the guidance is
  deliberately written to err toward acting, and that asymmetry — rather than any claim that
  recognition is easy — is its justification. Clinical guidance can afford to be more
  discriminating because its reader can afford to be wrong and notice.

## Advice that was removed, and the shape they share

The strongest evidence that this is a design discipline rather than condescension is the list of
things that were taken out. All of these are mainstream removals, and the reader's own national
council and poisons service are the authority on the current wording.

* Putting butter, oil, or ice directly onto a burn.
* Inducing vomiting after a swallowed poison.
* Cutting, applying heat to, or attempting to suck venom out of a snake bite.
* Tilting the head backwards during a nosebleed.
* Giving alcohol, or anything else, as a stimulant to someone cold or collapsed.
* The lay pulse check, removed because a pulse check is unreliable even among trained rescuers and
  the delay it causes costs more than the error it was meant to prevent. **(Consensus** that it
  was removed; **council-dependent** in how each council now words the recognition step.**)**

Every one has the same shape. A plausible mechanism, a failure mode that sounded benign and was
not, and a reader with no way to tell the difference. The test for inclusion was never whether the
advice helps when applied correctly — it is whether the distribution of *attempts*, botched ones
included, comes out better than the distribution with no advice at all.

And one in the other direction, which matters because it keeps the discipline honest: guidance on
tourniquets has changed direction more than once, moving away from lay use and then substantially
back toward it for life-threatening limb bleeding as evidence accumulated. *Removed* does not mean
*wrong forever*. It means the balance of harms, as understood at that revision, went the other
way.

## Where the branching went

```
   where the conditionality lives
   ──────────────────────────────────────────────────────────────────────────────────
   clinical guidance     reader ──► branch ──► branch ──► branch ──► act
                                     ▲          ▲          ▲
                                     └──────────┴──────────┘  reader evaluates these

   bystander guidance    reader ─────────────────────────────► act
                            │                                   ▲
                            └──► call handler ──► branch ───────┘
                                   ▲
                                   └── someone who can see which branch this is,
                                       correct it, and change it mid-attempt
   ──────────────────────────────────────────────────────────────────────────────────
   the branches did not get deleted. They got moved to a reader who can run them.
```

The branching that written guidance could not safely carry did not disappear. It moved to a person
on the telephone. An emergency call handler can assess, adapt, correct and re-decide in real time,
which is exactly the capability the printed document lacks, and dispatcher-assisted instruction is
now a central part of how bystander care is delivered rather than an extra.

This reframes the first line of every bystander-facing document. **Calling the local emergency
number is not merely a request for an ambulance.** It is how the reader acquires the branch logic
that the written guidance had to leave out, from someone who can see the branch they are actually
in. It is the single most important instruction in first aid for precisely that reason.

## Why a number is specified, without that number appearing here

Some first-aid instructions carry a specified rate rather than an instruction to use judgement,
and the reason is worth separating from the number itself. An untrained rescuer left to their own
sense of urgency performs far too fast or far too slow, and both lose effectiveness; the
distribution of self-paced attempts is wide in a way that directly costs outcomes. Naming a target
converts an unbounded judgement into something that can be coached over the telephone, rehearsed
in a class, counted along with, and corrected mid-attempt. The *existence* of the number is doing
the work.

**The number is not stated in this answer, and that is deliberate.** It differs between national
councils, it is revised on a cycle, and a misremembered number acted on is exactly the harm this
whole discipline exists to prevent. It belongs in the reader's own council's current document,
read there, and nowhere else.

## What the approach gives up

It is wrong for the atypical case, by construction. It under-serves a reader who does have
training and reads the public version anyway. It can be mistaken for the whole of care rather than
its first minutes. And the simplification has to be re-argued at every revision, because the
reader population itself changes: a document written for a public with no training and no
telephone is not the right document for a public where many people have had some training and
almost everyone is holding a phone with a call handler on the other end.

## The human stakes, said plainly

The removals listed above were not corrections of carelessness. Every one of them was taught in
good faith, by people who believed it helped, to readers who then did it to someone they cared
about. Butter or ice onto a burn. Vomiting induced after a swallowed poison. A snake bite cut,
heated or sucked. A head tilted back for a nosebleed. Alcohol given to someone cold or collapsed.
The lay pulse check, which cost more in delay than it ever recovered in accuracy. **(Consensus**
that each was removed from mainstream lay guidance; (**country-dependent**) in how each council
words its current position.**)** The honest summary is that advice given with good intentions
caused harm, that this was found out, and that the advice was withdrawn. That sequence is the
discipline working — and it is also why a forty-year-old leaflet is not a safe thing to act from.

Three consequences are about the reader rather than the document. The reader of bystander guidance
is usually frightened and often knows the person in front of them, which is the hardest set of
conditions in which to read anything, and is exactly why the written instruction is blunt, short
and nearly branchless. A bystander who tries and does it imperfectly has not done the wrong thing:
across everyone who attempts it, attempting is better than not attempting, and that is the
principle the document is built around rather than a reassurance added to the end of it
**(consensus)**. And the people most affected afterwards are frequently the ones who were there
and acted; support after an event of this kind exists, through the ambulance service that attended
and through primary care, and using it is an ordinary thing to do.

One instruction carries all of this. **Calling the local emergency number is how a bystander
obtains the branch logic the document had to leave out**, from a call handler who can assess and
correct in real time. Where such a handler is giving instructions, those are the instructions that
apply, and they are current in a way no written account including this one can be.

## What an examiner digs into next

* State the objective function for each document and name the difference in one sentence.
* Why is a branch that helps a minority and harms a majority a net harm even when the branch is
  correct?
* What do the removed items have in common, mechanically?
* Why does the tourniquet reversal strengthen rather than weaken the argument?
* Why is calling the emergency number the most important instruction, in terms of information
  rather than transport?
* Why specify a rate at all, and why would stating it here be a mistake?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md).
Specific to this answer:

* The current first-aid and basic life support guidance for the public issued by **the national
  resuscitation council for the country the reader is in**. This is the authority on every
  specific the answer above declines to state, including any rate. The councils differ from one
  another and each revises on its own cycle.
* The current consensus on science with treatment recommendations issued by **the International
  Liaison Committee on Resuscitation**, including its first-aid material, which is the evidence
  synthesis the national councils write their public guidance from and where removals are argued
  rather than announced.
* **The reader's national or regional poisons information service**, which is the authority on
  ingestion and envenomation advice and on why the older advice was withdrawn.
* **The reader's own national ambulance service or equivalent**, for how dispatcher-assisted
  instruction is actually delivered where they are, which varies considerably.
* The first-aid manual published by **whichever voluntary first-aid organisation runs training in
  the reader's country**, for the public-facing wording as that country's trainers teach it.

Claims here are marked **mechanism** (an argument about what a document can assume about its
reader), (**consensus**) (agreed across mainstream guidance as of writing), or
**council-dependent** (genuinely different between councils). No rate, depth, ratio, dose or
setting is stated anywhere in this answer; nothing is quoted; and no guideline number, document
title or identifier is given, because none was opened.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all. If a call handler is giving instructions, those instructions are the ones to follow — they
come from someone who can assess the actual situation, which no written document can.

This is revision material about *how bystander guidance is designed and why*, written for someone
already trained. It is deliberately not first-aid guidance and is not usable as any: it contains
no sequence of actions, no rates, no depths, no ratios, no doses and no settings, and the removed
items listed above are named as history rather than as instruction. First-aid and resuscitation
guidance **differs between national councils and is revised on a cycle**. The reader's own
national council, poisons service and ambulance service are the authority; this is not, and it has
had no clinical review. Nothing here describes any real person, case or institution.

## Where this stands, October 2026

The design argument — different reader, different objective, therefore a structurally different
document — is (**mechanism**) and is stable. That each item in the removals list was removed is
(**consensus**) as of writing and has been for years in every case. Everything else is
**council-dependent** and moves: the exact current wording of every item, which recognition cues
are given, every number, and how prominently dispatcher-assisted instruction is foregrounded all
differ between national councils, which publish on multi-year cycles that are not synchronised
with one another. The tourniquet example is included specifically because it is the clearest
demonstration that this material changes direction, and a reader who takes the direction of travel
from this answer rather than from their own council's current document has misread it. Dated
October 2026.
