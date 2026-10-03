---
id: "m138"
slug: the-practice-as-a-coupled-system
style: serious
category: general-practice
difficulty: advanced
question: "Why are list size, appointment length and continuity one set of coupled constraints rather than three separate decisions, and what happens to the slack?"
tags: [capacity, list-size, consultation-length, continuity, workload]
---

# The three decisions are denominated in the same resource, so there are not three decisions

A practice appears to make several independent choices: how many people are registered, how long
an appointment is, how hard it tries to send somebody back to the clinician they saw last time.
They are not independent. All three are expressed in the same currency — clinician time — and that
currency is fixed in the short run by the number of clinicians and the length of a working week.
Fix any three terms of the identity and the fourth is determined; it is not available to be chosen
as well (**mechanism**).

This is a structural answer, not an operational one. No list size, consultation length, staffing
ratio or waiting target appears here: every one of them is contractual or local, they differ
enormously between health systems, and an invented figure would be worse than none. m082 holds the
access-and-demand argument and m015 holds the case for continuity as a clinical intervention; what
this answer adds is the coupling between them.

Load-bearing claims below are marked with what they rest on: **mechanism**, **definitional**,
(**consensus**) or (**country-dependent**).

## The identity, and the fact that it is an identity

```
   AN ACCOUNTING IDENTITY, NOT A MODEL. No figures are attached; it holds for any.

      clinician time available
         =  ( list size  x  contacts per person per year )  x  time per contact
            +  all the work that is not a contact

   and the second line is not small:

      results to review          letters and discharge summaries to action
      prescriptions to authorise referrals to write and chase
      visits, and the travel     meetings, supervision, teaching, appraisal
      care-home rounds           the inbox that arrives whether anyone is free

   FOUR TERMS. CHOOSE THREE AND THE FOURTH IS DETERMINED. There is no arrangement
   of the three in which the fourth is also chosen - which is the entire content
   of this answer, and the part most often argued around.

   WHAT EACH CHOICE DOES TO THE OTHERS

   raise LIST SIZE, staffing fixed
      -> contacts per session must rise  (time per contact falls)
      -> or the wait lengthens           (access falls)
      -> or work moves into non-contact time, which nobody counts

   lengthen TIME PER CONTACT, staffing fixed
      -> contacts per session falls      (access falls)
      -> and demand does not fall to match, because demand is not set by supply

   tighten CONTINUITY, staffing fixed
      -> the schedule loses degrees of freedom: this person needs THAT clinician's
         appointments, not any appointment
      -> so the same capacity delivers either more waiting or more held-back slots

   ─────────────────────────────────────────────────────────────────────────────────
   THE COUPLING IS NOT A METAPHOR. It is that all four terms are measured in the
   same resource, and that the demand side responds to each change.
```

The last clause is what makes this harder than arithmetic. If demand were exogenous, the identity
would be a simple trade and a practice could pick a point on it. Demand is not exogenous: it
responds to what the service does, and some of the responses push total workload in the opposite
direction from the intention (**mechanism**).

## Three feedback loops, and each one can reverse a sensible change

* **The re-consultation loop.** A contact too short to settle the problem produces another
  contact. The second contact consumes the capacity that shortening was supposed to release, and
  it arrives attached to a person who has now had to ask twice. Whether a shorter appointment
  raises or lowers total contacts is an empirical question with setting-dependent answers, but the
  mechanism is not in doubt and the direction of the risk is one-way (**consensus** that the loop
  exists, magnitude contested).
* **The investigation and referral loop.** Discontinuity makes the cheap resolution — *I know this
  person, and this is different* — unavailable, and the substitute is a test or a referral. m015
  is the full argument. Each substitution consumes capacity elsewhere in the system and some of it
  returns as a result to review, which lands back in the non-contact term.
* **The displacement loop.** Need that cannot enter here enters somewhere else, or enters later in
  a worse state. m082 states this as the central property of a hard door, and it matters for the
  identity because displaced demand does not disappear from the practice's own workload: much of
  it returns as a discharge letter, an out-of-hours contact to reconcile, or a presentation that
  is now more complicated.

The practical consequence is that the three dials cannot be set by optimising each one in turn. A
change that is locally sensible on one dial can raise the total load through a loop that runs
through another.

## Where the slack actually goes

An identity with four terms and fixed capacity has to balance somewhere. In practice the residual
lands in a small number of places, and the two that absorb most of it are the two nobody measures.

1. **Non-contact time outside sessions.** The inbox, the letters, the results and the
   prescriptions are done, and when there is no room inside the session they are done outside it.
   This term is almost never counted in any workload measure, which means a service can be
   substantially over capacity and look balanced in its own data.
2. **Waiting.** Visible, measured, politically costly, and therefore the term that gets managed —
   often by moving it rather than reducing it.
3. **Task shifting.** Work moves to a different member of the team. This genuinely relaxes the
   constraint when the receiving role has capacity and the right scope; it relocates the
   constraint when it does not, and it adds a coordination cost that lands in the non-contact term
   either way.
4. **Rationing by endurance.** When appointments are scarce and access is first-come, the sort key
   becomes persistence, which is not a clinical quantity and correlates with the attributes m082
   lists.
5. **Attrition.** Hours reduced, roles left, retirement brought forward. This is the slowest term
   and the most expensive, and like the first it is invisible until it has already happened
   (**consensus**).

The generalisable point: **the residual of an identity goes into whichever term is unmeasured**,
and a system whose data looks balanced may be one whose balancing term is simply not in the data
(**mechanism**). That is the single most useful thing to know about reading a practice's own
activity statistics.

## Why activity counts are the wrong output measure

Contacts are an intermediate quantity, not an output. Counting them has a predictable effect:
shortening a contact raises the count, so a measure built on contacts rewards exactly the move
most likely to trigger the re-consultation loop. The same applies to any measure that counts an
act rather than a resolution.

Measures that are informative here are the ones that **span two terms at once** — for example, the
proportion of contacts that are with the person's usual clinician, read alongside how long it
takes to get one; or the proportion of problems resolved without a further contact, read alongside
the length of the contact that resolved them. A measure confined to one term cannot see a trade
between terms, which is why single-term dashboards can all be green while the system is
deteriorating (**mechanism**).

Two honest limits. First, continuity is not one thing: being seen by the same clinician, being
seen by the same small team, and having a coherent record are three different goods with different
costs, and measures rarely distinguish them. Second, none of these measures is a quality measure;
they describe the shape of the service, not whether the clinical work in it is any good.

## The counterweight, stated as strongly as the argument

The coupling is real but it is not a reason for fatalism, because one assumption in the identity
is false and that is where the slack is. **Uniform appointment length is a design choice, and a
crude one.** Need is not uniformly distributed: a large share of contacts are brief and
conclusive, and a small share need much more time than the standard allowance. Allocating one
length to all of them guarantees that the brief ones waste capacity and the complex ones do not
get enough.

Differentiating length is the one lever that genuinely relaxes the coupling rather than moving it,
and it is the reason a system of mixed appointment types exists at all. It also carries exactly
one serious cost, and it is a familiar one: the allocation has to be made *before* the
consultation, which is the point of least information. m112's argument applies — the decision does
not disappear by being moved earlier, and whoever makes it is making a clinical judgement on a
fraction of the data. Segmentation done well relaxes the constraint; segmentation done on a crude
proxy reproduces the inverse care law inside the appointment book, because the people least able
to describe a problem on a form get sorted into the shortest slot.

And the structural counterweight that belongs in the same place: more of this is determined above
the practice than inside it. Staffing, premises, funding formulae, list closure rules and
contractual access requirements are set elsewhere, and a practice optimising within them is
choosing between arrangements of the same constraint rather than removing it
(**country-dependent**).

## The human stakes, said plainly

The person who needs the most time is usually the person least able to ask for it. That is the
whole of the equity argument about appointment length, and it is not solved by anybody working
harder: it is a property of how the time is allocated and of who finds it easy to operate an
allocation system.

The second thing is that the invisible term in the identity is somebody's evening. When the
residual lands in non-contact work, it lands on named people, outside the hours anybody counts,
and it is the term that gets drawn on first precisely because drawing on it never shows up as a
failure. Nursing m074 makes the argument that fatigue is a safety factor and not a personal
failing, and it applies with full force here: a system that balances itself on unmeasured goodwill
is a system whose safety margin is somebody's tiredness.

And the honest statement about continuity. It is a clinical good with evidence behind it and it is
also, concretely, a constraint that takes options away from a timetable. Pretending it is free
makes it the first thing cut when access is under pressure, because the case for it is never made
as a resource case. Both halves are true, they pull against each other, and a practice that says
out loud which it is choosing — and for whom — is doing something better than one that implies it
has chosen neither.

## What an examiner digs into next

Whether the candidate writes the identity down and recognises it as an identity rather than a
trade-off to be balanced. Then the non-contact term, offered unprompted, with at least four of its
components. Then what each of the three dials does to the other two, in both directions. Then the
loops: re-consultation, investigation and referral, displacement — and which of them can reverse
the intended effect of a change. Then where the residual goes, with the point that it goes into
whatever is unmeasured. Then why activity counts reward shortening. Then the counterweight, with
uniform length identified as the false assumption and the before-the-consultation cost of fixing
it stated. Then the hard one — which single measure their own practice could add that spans two
terms, and what it would make visible that is currently not.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The contract or regulation that governs registration, list closure, access requirements and
  funding in the reader's own system, which determines which of these terms a practice may
  actually change (**country-dependent**).
* The reader's own organisation's workforce and activity data, including whatever it records about
  work done outside booked sessions — the absence of that record is itself the finding this answer
  predicts.
* The published literature on consultation length, read for what longer consultations are
  associated with and for the limits of the causal claim, which is argued about and confounded by
  who books longer appointments.
* The published literature on continuity of care, for its associations with hospitalisation,
  investigation and satisfaction, and for the distinction between relational, team and
  informational continuity.
* A current textbook of health services research or operations management in healthcare, for
  queueing behaviour, variation, and why utilisation close to capacity produces disproportionate
  waiting.
* Any national review of primary care workload in the reader's system, read as a description of
  one country's arrangement rather than as a general finding.

## Scope and safety

This is revision material about how the capacity of a general practice behaves as a system,
written for someone already training in or qualified for the field. It is not a clinical
reference, not a decision aid, and nothing here should inform a decision about any individual's
care, appointment or referral. No list size, consultation length, staffing ratio, waiting-time
target or workload threshold is named here on purpose: all are local, several are contractual, and
all are revised. Nothing here is a statement about how any particular practice should be
organised, and nothing in it is a measure of anybody's performance. If someone is unwell right
now, the relevant action is to contact local urgent care or the local emergency number, not to
read this.

## Where this stands, October 2026

The identity is arithmetic and will not move. The loops, the residual going into the unmeasured
term, and the equity consequence of uniform appointment length are mechanism and mainstream. What
moves is everything numerical and contractual: list sizes, standard appointment lengths, staffing
models, the scope of other professional roles, access requirements and the balance between booked
and same-day work. The expansion of multidisciplinary teams and of remote and asynchronous contact
has changed where the residual lands rather than removing it, and the evidence on total workload
under those models is arriving rather than settled. Take anything operational from current local
requirements rather than from here, as of October 2026.
