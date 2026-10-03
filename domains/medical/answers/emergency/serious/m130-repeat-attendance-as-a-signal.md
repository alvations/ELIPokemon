---
id: "m130"
slug: repeat-attendance-as-a-signal
style: serious
category: emergency
difficulty: intermediate
question: "Why is repeat attendance a clinical signal rather than a nuisance, and what makes the pattern the finding?"
tags: [reattendance, pattern, records, diagnosis, revision]
---

# The count is thrown away at the moment each attendance is recorded, and the count is the finding

Somebody comes back. The previous episode was assessed, nothing requiring admission was found,
advice was given, and now they are here again — third time this month, or second time this week,
or fourth time since the spring.

The clinical content of that sentence is almost entirely in the **number and the spacing**, and
almost nothing about the way the information is stored makes the number and the spacing available.
Each attendance is recorded as an episode. The episode has a presenting complaint, an assessment
and an outcome. What it does not have is a field that says *this is the fourth*, and the system
that would compute it is usually a different system from the one in front of the person doing the
assessment. (**Mechanism** — this is a property of how the information is held, not a claim about
anybody's diligence.)

So the first move in this topic is to separate two claims that get fused. *This person has
attended repeatedly* is a datum. *This person is attending unnecessarily* is a conclusion, and it
is the conclusion the word *frequent* is routinely heard as containing. The second does not follow
from the first, and the assessment that would test it is exactly the one the fused reading
prevents.

## What a reattendance actually discriminates between

The useful question is not whether the attendance is justified. It is: **given that someone has
come back, which of a small number of structurally different things is happening?**

```
   the person came back
        │
        ├── the original problem was correctly characterised and has PROGRESSED
        │      → the reattendance is the safety-net working exactly as designed
        │
        ├── the original problem was MIS-characterised
        │      → the reattendance is the only mechanism that will ever correct it,
        │        and the previous assessment is now a source of anchoring rather
        │        than of reassurance
        │
        ├── a SEPARATE new problem
        │      → and the record of the old one is now actively misleading
        │
        ├── the problem was characterised correctly and the PLAN FAILED
        │      → could not get the medicine, could not get the follow-up, could not
        │        afford it, did not understand it, nobody was free to bring them
        │
        ├── the underlying condition is one that RELAPSES, and the interval between
        │   relapses is itself the clinical measure
        │      → the count IS the severity marker, and no single visit shows it
        │
        └── the need being presented is real and is not the one the department treats
               → still a clinical problem; question m105's argument about a label
                 that names where a cause is and gets read as naming its absence
```

Six branches, and the branch cannot be determined from the current visit alone. That is what makes
the pattern a finding rather than a context: *the pattern is the only observation that
discriminates between them*, and the alternative to using it is not a neutral assessment but a
repeat of the previous one. (**Mechanism.**)

Two of those branches deserve separate statements because they are the ones most often collapsed
into the others.

* **For a relapsing condition, the frequency is the measure.** There are conditions in which *how
  often* is the primary index of control, and a clinician who treats each episode as a
  self-contained event and never counts has not measured the thing the condition is graded by. The
  specific conditions, their control measures and their escalation steps are guideline material
  and are not described here. (**Consensus.**)
* **A failed plan looks identical to a failed patient from inside a single consultation.** The two
  are distinguished only by asking what happened after the last visit, and that question is cheap,
  is rarely asked, and is the one that separates a dispensing problem or a transport problem from
  a disease problem. (**Mechanism.**)

## Why the previous assessment is a liability as well as an asset

The previous record is the best information available about this person and simultaneously the
main threat to the current assessment, which is an uncomfortable pair of facts to hold at once.

* **It anchors.** A documented conclusion is read before the person is seen, and every subsequent
  observation is interpreted against it. Question m068 describes this mechanism under the name
  anchoring and question m048 as premature closure; the only unusual feature here is that the
  anchor arrives with the authority of a colleague's signature. (**Consensus.**)
* **"Nothing found" is not a negative finding unless somebody wrote down what was looked for.** An
  episode recorded as *no acute pathology* with no account of the search cannot be distinguished
  from an episode in which little was looked for, and the two have completely different
  implications for the current visit. This is question m070's missing pertinent negative and
  question m037's distinction between what was documented as seen and what was documented as
  confirmed. (**Mechanism.**)
* **The record of a *different* problem is misleading in a specific direction.** A person known to
  the department for one thing is at structural risk of having the next thing attributed to it,
  because the prior is doing work that the new presentation has not earned. (**Mechanism.**)
* **And the reassurance compounds.** Each visit at which nothing was found raises the subjective
  prior that nothing will be found, in the clinician and in the person, and that movement is not
  Bayesian updating on new evidence — it is the same evidence counted repeatedly. (**Mechanism.**)

The practical consequence is not *ignore the previous record*, which would be absurd. It is that
the previous record should be read for **what was looked for** rather than for **what was
concluded**, and that where the search is not recorded, the conclusion carries much less weight
than its wording suggests.

## What makes the pattern usable rather than merely present

The pattern is almost always present in the data and almost never present in the consultation, so
the gap is structural and the remedies are structural too. (**Country-dependent** in every
particular, since what exists depends entirely on the system.)

* **It has to be computed and surfaced, not remembered.** A count that requires somebody to notice
  is a count that is noticed on quiet shifts. Where systems flag reattendance within a defined
  window, the flag is doing the arithmetic nobody has time to do.
* **The window matters and is a clinical choice.** Reattendance within hours, within days and
  within months mean different things, and a single flag with a single interval conflates them.
  The intervals used in local and national measurement are set for audit purposes as much as
  clinical ones, and they differ.
* **It has to be routed somewhere that can act on the pattern rather than on the episode.** A flag
  that reaches only the person assessing the current episode gets a better single assessment; a
  flag that reaches someone who can review the sequence gets the diagnosis. Which of those exists
  is institutional.
* **A record answers *now* and *ever* and has no field for *how often*.** A clinical record is
  built to say what the current problem is and what has happened before; the structured items
  it carries are a problem list and a past history, and neither of those is a frequency. So the
  distinction the system makes cheaply is between a current and a past problem, and the one it
  makes expensively is between twice and nine times. (**Mechanism.**)
* **And the count is fragmented across providers, because it belongs to the service and not to
  the person.** Someone who attends three different departments, or a department and two
  out-of-hours services, has three small counts and no large one, and each service sees a first
  or second attendance. The pattern is a property of the *person's* trajectory and the records
  are organised by *place*, which is why a shared record changes this topic more than any
  clinical insight does. (**Mechanism**; whether such a record exists at all is
  (**country-dependent**).)
* **Reattendance measured as a quality indicator is not the same quantity as reattendance used as
  a clinical signal**, and conflating them has a predictable failure mode: once the count is a
  performance measure, the incentive attached to it points away from treating it as information.
  (**Consensus** that this tension exists; its handling is local.)

Nothing above names an interval, a threshold, a flagging system or a care-planning process,
because those are local, they are revised, and the reader's own guidance is the authority.

## The human stakes, said plainly

The word in use for this, in most departments, is one of a small set of informal labels, and every
one of them is a judgement about the person wearing the clothes of a description. People know.
Someone who has attended six times knows precisely how they are being read, often before anybody
speaks, and that knowledge changes what they tell you — which means the label degrades the quality
of the history that would resolve the question it is standing in for.

Four things follow, and none is a mechanism.

The first is that coming back is frequently the exact behaviour that was asked for. The safety-net
advice at the previous visit said *come back if it gets worse, or if you are worried*, and
somebody who follows that instruction and is then treated as a nuisance has been punished for
compliance. That is both unjust and self-defeating, because the next time they need to come back
they will weigh it against this experience.

The second is that the people most likely to attend repeatedly are, in aggregate, the people with
the least of everything else: the fewest alternatives, the least ability to wait, the least access
to a regular clinician, the most unstable housing, the worst health. The inverse care law is a
mechanism rather than a complaint — question m050's argument — and reattendance is one of the
places where it is most visible and most often mistaken for a behavioural trait.

The third is that the frustration in a department under pressure is real and is not a reason. The
resources that would change the pattern are usually elsewhere, the problem is genuinely one the
department cannot solve on its own, and the correct response to a problem whose solution lies
elsewhere is to characterise it accurately and refer it. Attaching a structural problem to the
person standing in front of you is the failure mode, not the diagnosis.

The fourth is about what to say. A person who expects to be dismissed is disarmed by being told,
plainly, that coming back was right, and that the fact that this is the fourth time is itself a
reason to look at the whole sequence rather than just today. That sentence costs nothing, it is
true, and it changes the consultation.

And the honest closing point: a proportion of reattendances genuinely are for problems the
department cannot help with, and pretending otherwise is not kindness. The argument here is not
that every return is a missed diagnosis. It is that the number and the spacing are information,
that they are routinely discarded, and that the discarding happens at the point of recording
rather than at the point of judgement — which is why it is a design problem and not a character
problem.

## What an examiner digs into next

* Which part of *third time this month* carries the clinical content, and what happens to it in
  the record?
* Separate the datum from the conclusion, and say which assessment the fused reading prevents.
* Give six structurally different things a reattendance can represent.
* For which kind of condition is the frequency itself the measure, and what does a clinician who
  never counts fail to measure?
* A failed plan and a failed patient look identical from inside one consultation. What
  distinguishes them?
* Why is the previous record simultaneously the best information and the main threat?
* Why is *nothing found* not a negative finding, and what would make it one?
* Why is repeated reassurance not Bayesian updating?
* Should the previous record be read for its conclusion or for its search? Why?
* A record answers *now* and *ever* cheaply. Which question does it answer expensively, and why?
* Why is the count fragmented, and what does that imply about who sees a pattern?
* Why does a count have to be computed rather than remembered, and why does the window matter?
* What goes wrong when reattendance is used both as a quality indicator and as a clinical signal?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-emergency.md`](../../../for-agents/SOURCES-emergency.md), and they
apply here. Specific to this answer:

* The current standards for emergency department assessment, documentation and reattendance issued
  by **the reader's national emergency medicine college**. This is where the expectation about
  recording what was looked for actually sits, and where any reattendance interval used in
  measurement is defined; both differ between countries.
* **The reader's own employing organisation's** policy on reattendance flagging, on individual
  care planning for people who attend frequently, and on referral to community and specialist
  services. This governs what is possible where they work and outranks every general account
  including this one.
* The current national definitions used for measuring unplanned reattendance, issued by **the
  reader's national body for health service statistics or performance measurement**, which is a
  different document from the clinical standards and is written for a different purpose.
* A current standard textbook of **emergency medicine**, and the literature on **diagnostic
  error**, for anchoring, premature closure and the handling of a previous diagnostic conclusion.
* **The primary literature**, for the characteristics of populations who attend frequently and for
  the evidence on interventions aimed at them. No proportion, rate or effect size is quoted here.

Markers used above: (**mechanism**) (follows from the structure of the problem or of the record
and is checkable by reasoning), (**consensus**) (agreed across mainstream sources as of writing),
(**country-dependent**) (genuinely differs between countries, services or institutions). No
interval, threshold, flagging system, care-planning process or statistic is named above, and
nothing is quoted, because none of these documents was opened.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *how a pattern across episodes becomes a clinical finding and why
it is usually lost*, written for someone already trained. It is deliberately not a protocol and
not a decision aid: it names no reattendance interval, no threshold, no flagging system, no
care-planning process and no statistic, and it is not something to consult while assessing anyone.
It contains no account of capacity, consent, or the protection of adults or children at risk,
because those are matters of law that differ by jurisdiction and the reader's own legislation and
statutory guidance are the only acceptable source. Record systems, reattendance definitions,
flagging arrangements and the availability of community and specialist services differ enormously
between countries and institutions. The reader's own national guidance and local policy are the
authority; this is not, and it has had no clinical review. Nothing here describes any real person
or any real case.

## Where this stands, October 2026

The argument is stable and the implementation is not. That the clinical content of a reattendance
lies in the number and the spacing, that episode-based records discard the count at the point of
recording, that the datum and the conclusion are different claims, that a reattendance
discriminates between a small number of structurally different states and that the current visit
alone cannot identify which, that for relapsing conditions the frequency is the control measure,
that a documented conclusion anchors, that an unrecorded search makes *nothing found*
unfalsifiable, and that repeated reassurance is the same evidence counted repeatedly are all
long-standing and follow from the structure of the problem rather than from any single document.
What moves is everything else. Record systems and what they surface change with each procurement;
the intervals used to define unplanned reattendance are set nationally for measurement purposes
and are revised; individual care planning for people who attend frequently exists in some systems
and not others and is contested where it exists; the evidence on interventions aimed at frequent
attendance keeps being restudied with mixed results; and the availability of the community
services that would change the pattern is a political variable rather than a clinical one. The law
on the protection of adults and children at risk differs by jurisdiction and is not described here
at all. Treat this as an explanation of a principle dated October 2026, and read the current
guidance from the college and institution that govern where the reader actually works for anything
beyond the principle.
