---
id: "m070"
slug: handover-and-what-crosses-the-boundary
style: serious
category: emergency
difficulty: intermediate
question: "Why is the handover from pre-hospital to hospital the point at which information loss costs most, and what is it that actually gets lost?"
tags: [handover, information-loss, pertinent-negatives, human-factors, revision]
---

# A handover is a boundary with a field list, and everything without a field is deleted

A handover is a transfer of state across a boundary, and like every such transfer it has a
**schema**: an implicit or explicit set of fields that cross. Numbers, times, interventions and
identifiers cross easily, because they have fields. What has no field does not degrade gracefully;
it is simply not there on the other side, and nobody on the receiving side can see that it is
missing. **(Mechanism** — this is a property of any bounded transfer and is checkable by
reasoning.**)**

The pre-hospital-to-hospital boundary is where that costs most, for a reason that is specific to
it rather than general to handovers. It is the point at which **the only people who saw the scene
stop being present**, and the scene cannot be re-examined. Every other handover in a patient's
journey transfers information that the receiving team could, in principle, go and obtain again.
This one does not. The information is not merely being passed; some of it is being passed for the
last time.

## What crosses, and what does not

```
   crosses readily (it has a field)        does not cross (no field, and no trace of the gap)
   ──────────────────────────────────────────────────────────────────────────────────────────────
   age, name, identifiers                 the scene: position, surroundings, what was around them
   times: event, call, arrival             the deformation, the height, the distances
   recorded observations                   the TRAJECTORY: improving or worsening, and how fast
   interventions given                     how much support those observations were obtained on
   the problem, in a few words             what was actively checked and found ABSENT
   a named category or label               the sender's impression, and what it is based on
                                           what has already been tried that did not work
                                           what the patient said before they stopped saying it
                                           who else was there, and what they described
   ──────────────────────────────────────────────────────────────────────────────────────────────
                                            ▲
                                            └── all of it irreplaceable: nobody can go back
```

Read the right-hand column and a pattern appears. What fails to cross is disproportionately
**contextual, comparative and negative** — the three kinds of information that do not fit a field
on a form. Trajectory is comparative: it needs two points, and a handover that reports the latest
set of observations has thrown away the comparison that made them meaningful. Pertinent negatives
are negative: a careful examination that found nothing produces no entry, and a careless one that
looked at nothing produces exactly the same no entry. And impression is contextual: it is an
aggregation over a large number of weak signals, many of which have no name, which is why it has
to be asked for explicitly or it will not volunteer itself. This is question m034's point about a
worried clinician, at the moment the worry has to survive a boundary.

## Why the loss costs more here than elsewhere

* **Priors are set by the first framing, and this is the first framing.** Whatever the receiving
  team hears in the first sentences becomes the frame everything afterwards is fitted into.
  Anchoring is strongest at the start, and the handover is the start. A mislabelled problem is
  therefore not merely an error passed on; it is an error with leverage.
* **The information is non-recoverable.** A missing result can be repeated. A missing scene
  cannot.
* **The receiving team is being asked to receive and to act simultaneously.** Attention is divided
  at precisely the moment the transfer needs it undivided, and the sender is often still
  physically managing the patient. This is a structural problem, not a discipline problem.
* **The two sides have different models and different vocabularies.** They were trained
  differently, work to different guidance, and use some of the same words for different things. A
  term that is precise on one side of the boundary can be ambiguous on the other, and neither side
  observes the ambiguity happening.
* **Everyone is in motion.** The physical choreography of an arrival actively works against a
  verbal transfer, and the information most at risk is the part that comes last — which, in an
  unstructured handover, is usually the impression.

## The structural remedies, and what each one actually fixes

Each of the following exists against a specific failure above, and naming the pairing is more
useful than listing them.

**A declared format.** Structured handover formats are in widespread use; several exist, they
differ between services and countries, and this answer names none, because naming one as the
standard would be wrong and because a half-remembered format is worse than the local one.
**(Consensus** that a declared structure improves transfer; (**country-dependent**) in which
structure, and strongly service-dependent.**)** What a format fixes is the schema problem: it
creates a field for the things that otherwise have none. Which fields it has is therefore the
whole design question, and the reason the good ones have a slot for mechanism, for trajectory and
for the sender's concern is that those are the items that disappear without one.

**A convention that one person speaks and the others stop.** This fixes the divided-attention
problem, and it only works if it is agreed in advance, because nobody can negotiate it in the
moment.

**Read-back, or a repeated summary.** This fixes the different-vocabularies problem, because the
only way to detect that a term was understood differently is to hear it come back.

**The written record arriving with the patient.** This fixes the last-item problem, by removing
the dependence on a verbal transfer completing without interruption.

**Asking for the impression as a question.** This fixes the aggregation problem. The question is
closed — what is the single thing that concerns you most — because an open invitation at the end
of a handover is reliably declined.

**And a protected moment for it.** The reason this is structural rather than polite is that
everything above fails if the transfer is attempted during the physical move. Services that do
this well treat the handover as an event with a boundary of its own.

## What a structured handover still cannot do

* **A field list is a prediction about what will matter.** It was written in advance, by people
  who did not know about this patient, and the unusual case is where its fields fit worst.
* **It can manufacture a sense of completion.** Having been through the format is not the same as
  having transferred understanding, and a fluent handover of the wrong frame is the failure mode
  that a format makes more likely rather than less.
* **It cannot create information that was never recorded.** If the trajectory was not observed, no
  format recovers it.
* **The absence of a field is still invisible.** This is the irreducible part: the receiving side
  cannot distinguish *not examined* from *examined and normal*, or *no concern* from *concern not
  asked for*, unless the format forces the distinction. Every improvement in handover is, at
  bottom, an attempt to make a gap visible.

## The human stakes, said plainly

Two people are in this, and the patient is only one of them.

What is being handed over is a person who, a short time ago, was somewhere else, with people who
knew them, in circumstances that will never be reconstructable. The information that fails to
cross is frequently the information that would have changed what happened next, and failures of
handover are a well-described and much-studied source of avoidable harm across the whole of
healthcare — which is why this is a subject with a literature, rather than a matter of being
conscientious. **(Consensus.)** The patient, meanwhile, is listening. A handover happens over the
person it is about, in the third person, and that is worth remembering: the content does not
change, and the way it is said can.

The other person is the one handing over. They have often been working alone or in a pair, under
pressure, sometimes for a long time, with decisions they had to make without the resources the
receiving team has. Their impression is the most information-dense thing they carry and the
hardest for them to articulate quickly, and it is the item most often not asked for. Treating a
handover as a download from a less-qualified source to a more-qualified one loses exactly that
item, and the loss is not symmetrical: the receiving team can obtain almost everything else by
other means.

This answer names no structured format, no mnemonic, no fields and no sequence, deliberately.
Formats differ between ambulance services, between hospitals and between countries, and the one
the reader is held to is the one agreed where they work. That is also the one worth learning.

## What an examiner digs into next

* Why does a handover have a schema, and what happens to information with no field?
* What makes this particular boundary different from every other handover in a patient's journey?
* Why do contextual, comparative and negative information fail to cross disproportionately?
* Why is a missing pertinent negative indistinguishable from an examination that was never done?
* Match each structural remedy to the specific failure it addresses.
* Why can a fluent handover be worse than a halting one?
* Why is the sender's impression both the densest item and the one most often lost?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md), and they
apply here. Specific to this answer:

* **The handover standard agreed between the reader's own emergency department and the ambulance
  service that brings patients to it.** This is the document that actually governs the transfer
  and it is local by nature; there is no national or international handover format that can
  substitute for it.
* The current clinical practice guidelines issued by **the ambulance service or national paramedic
  body for the country the reader practises in**, for how the sending side is trained to structure
  what it says.
* The current guidance on safe transfer of care issued by **the reader's own national body for
  clinical guidelines or national patient-safety body**, for the evidence that handover is a
  high-risk transition.
* **The human-factors and team-communication material taught on the reader's own resuscitation or
  trauma course**, which is where read-back, the single-speaker convention and the protected
  handover moment are taught.

Markers used above: **mechanism** (follows from the structure of a bounded transfer or from
cognitive psychology and is checkable by reasoning), (**consensus**) (agreed across mainstream
sources as of writing), (**country-dependent**) (genuinely differs between countries, services or
institutions). No format, mnemonic or field list is stated, and nothing is quoted, because none of
these documents was opened.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *why a transition loses information and what kind*, written for
someone already trained. It is deliberately not a protocol: it names no handover format, no
mnemonic, no field list, no sequence of actions, no thresholds, no doses and no settings, and it
is not something to consult while acting. Handover formats and the standards attached to them
differ between ambulance services, between hospitals and between countries, and they are revised.
The agreed local standard where the reader works is the authority; this is not, and it has had no
clinical review. Nothing here describes any real person, any real case or any real handover.

## Where this stands, October 2026

The analysis is stable and uncontroversial: that a handover transfers only what it has fields for,
that contextual, comparative and negative information is lost preferentially, and that this
particular boundary is where loss is least recoverable are all long-standing and follow from the
structure of the problem rather than from any single document. That handover is a high-risk
transition is settled across patient-safety literature. What is not settled is any specific: which
structured format is used, what its fields are, how long a protected handover period is, whether
read-back is mandated, and how the standard is audited all differ between services and countries
and are revised — and several widely taught formats have been introduced, modified and replaced
within the last two decades. Treat this as an explanation of a principle dated October 2026, and
read the agreed local standard between the reader's own department and its ambulance service for
anything beyond the principle.
