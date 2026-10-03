---
id: "m109"
slug: continuous-versus-intermittent-observation
style: serious
category: nursing
difficulty: advanced
question: "What does continuous monitoring actually buy over intermittent observation, and why is detection not the limb that usually fails?"
tags: [monitoring, observations, alarm-fatigue, escalation, deterioration]
---

# An observation set is a sample, and what it buys depends on the interval against the event.

Three different activities are called observation and they do different work. A set of structured
bedside observations at a stated frequency is a **sample** of a continuous process. Continuous
physiological monitoring is a **high-rate sample of one or two channels and of nothing else**.
Continuous human presence is not primarily a measurement at all — it buys the ability to
*intervene* inside the duration of the event, which no monitor does.

Conflating the three produces the characteristic error in this subject: treating "more monitoring"
as an improvement in care, when the thing being improved is the front half of a chain whose
failures are mostly in the back half.

Markers used below. (**mechanism**) means it follows from the structure of the measurement;
(**definitional**) means it is what the word means; (**consensus**) means mainstream agreement
across major guidance; (**country-dependent**) means the reader's own policy decides. No interval,
no alarm limit and no monitoring threshold appears here; those are all local.

## The sampling argument, which is the whole mechanism

```
   event duration vs sampling interval        what an intermittent set of observations does
   ─────────────────────────────────────────  ───────────────────────────────────────────────
   change is SLOW compared with the interval  catches it, and catches the trend across several
   (hours to days — a developing infection,   sets. This is the common case and it is why
   a slowly falling haemoglobin)              intermittent observation works at all
   ─────────────────────────────────────────  ───────────────────────────────────────────────
   change is COMPARABLE to the interval       catches it late, and cannot tell you the rate.
                                              Two identical readings an interval apart are
                                              consistent with "stable" and with "fell and
                                              recovered"
   ─────────────────────────────────────────  ───────────────────────────────────────────────
   event is SHORTER than the interval         misses it entirely, and — the part that matters —
   (a paroxysmal arrhythmia, an apnoeic       MISSES IT SILENTLY. The chart shows a normal set
   episode, a nocturnal desaturation, a       of observations, which is a true record and a
   seizure, a fall)                            false reassurance
   ─────────────────────────────────────────────────────────────────────────────────────────────
   Nothing in an intermittent record distinguishes "did not happen" from "happened between
   samples". That is the same collapse m073 describes for the pertinent negative, arriving by a
   different route: a normal observation set is a negative finding about an INSTANT, and it is
   routinely read as a negative finding about an INTERVAL.
```

So what continuous monitoring genuinely buys is three things, and they are worth separating.
(**mechanism**)

* **Shorter detection latency** for a change on the monitored channel.
* **The derivative.** A rate of change is only available if the sampling is fast relative to the
  change, and the rate of change is frequently more informative than the value — which is also the
  argument for recording a trend rather than a single set, and for why m001's composite is read
  against the previous one.
* **Capture of transient events** that are shorter than any practicable observation interval.

## And four things it costs, none of which are incidental

**It narrows while it deepens.** A monitor watches one or two channels at high rate and nothing
else at all. The attention it attracts is attention moved away from everything not on the display,
including the person. The single best-attested independent signal of deterioration is a
clinician's or a relative's concern that someone does not look right — which is why concern-based
escalation exists in guidance alongside the numbers, and it is not a channel any monitor has.
(**consensus**)

**Alarms.** A threshold alarm on a noisy single channel produces non-actionable alarms at a rate
set by where the threshold sits, and in practice the majority of alarms in monitored clinical
areas are not actionable. The documented consequences are desensitisation, slower response, limits
widened to stop the noise, and alarms disabled; harm and deaths have been attributed to this, and
it has been the subject of national safety alerts in more than one country. (**consensus**; the
specific alerts are (**country-dependent**).) Alarm fatigue is therefore a property of the
system's design and not of the staff's attitude. (**mechanism**)

```
   where the threshold sits        non-actionable alarms      missed events
   ─────────────────────────────── ───────────────────────── ────────────────────────────────────
   tight                           many                       few — but the response degrades,
                                                               so the practical miss rate RISES
   loose                           few                         more, directly
   ─────────────────────────────────────────────────────────────────────────────────────────────
   The curve is not monotonic in either direction, which is why alarm limits are a clinical
   decision needing an owner and a review, and why a default limit applied to everybody is the
   worst of both. Where the local default sits, and who may change it, is institutional.
```

**It tethers, and the tethering has its own harms.** Leads, probes, cables and a bed position;
disturbed sleep; reduced mobility, which is m072's deconditioning argument; and the device
pressure points, which are m004's. A continuously monitored person moves less, and moving less is
not neutral. (**consensus**)

**It does not act.** This is the one that matters and it gets its own section.

## The two limbs, and which one actually fails

The response to deterioration is conventionally split into an **afferent limb** — measure, record,
recognise, escalate — and an **efferent limb** — someone comes, assesses, and does something.
(**definitional**, from the rapid-response literature.)

```
   step                                      limb        where the documented failures are
   ───────────────────────────────────────── ─────────── ────────────────────────────────────────
   observations are due                       afferent    missed, or taken late
   observations are taken                     afferent    incomplete sets — respiratory rate is
                                                           the one most often omitted and the one
                                                           with the most predictive weight
   observations are recorded and scored       afferent    recorded without being summed, or
                                                           summed wrongly
   the threshold is recognised                afferent    recognised and not believed
   escalation is made                         ────────    THE BOUNDARY, and the commonest point
                                                           of total failure
   somebody answers                           efferent    delayed, or answered by someone without
                                                           the authority to act
   they attend and assess                     efferent    delayed
   a decision is made and carried out         efferent    made and not communicated; carried out
                                                           and not reviewed
   ─────────────────────────────────────────────────────────────────────────────────────────────
   Continuous monitoring improves the FIRST TWO ROWS and touches none of the others.
```

That is the answer to the question. The recurring finding in reviews of in-hospital deterioration
is that abnormal observations were frequently present and documented before the event, and that
the failure lay in recognition, escalation or response rather than in detection. (**consensus**)
Where the bottleneck is the efferent limb, improving the afferent limb produces a longer record of
a deterioration nobody acted on — and a continuous record that nobody read is **worse** than no
record, because it documents in detail that the information was available. (**mechanism**)

The corollary for practice is unglamorous and correct: the interventions that change outcomes in
this area are mostly about the back half — an escalation route that always answers, a threshold
that does not require permission to use, a response team with the authority to act, and a culture
in which escalating and being wrong is cheap.

## What good practice actually looks like, which is neither of the two options

The answer is not "continuous or intermittent". It is an **individualised monitoring plan**: what
is being watched, at what frequency, by whom, what change triggers what action, and when the plan
itself is reviewed. (**consensus**; the format and who may authorise it is
(**country-dependent**).) Most national early-warning guidance asks for exactly this and most
institutions have somewhere to write it, and the commonest defect is that the frequency is set by
the ward's routine rather than by the person's trajectory.

Two further specifics, stated as principles because the details are local. Continuous monitoring
is clearly indicated in defined settings — immediate post-anaesthetic recovery, critical care,
during certain infusions and after certain procedures — and the list is institutional and not
something to reason out from first principles. (**country-dependent**) And the limits of the
instrument matter as much as its presence: m102 holds the full argument on pulse oximetry, and
m107's version of it is the one that bites here, that a saturation inside a target range is fully
compatible with a rising carbon dioxide, so a continuously normal channel can accompany a
deterioration the monitor has no access to.

## Continuous human presence is a different intervention

Enhanced or one-to-one observation is frequently discussed as though it were the maximum setting
of the same dial. It is not. What it buys is the capacity to intervene inside the duration of the
event — a fall takes a fraction of a second, and no monitor shortens that — plus orientation,
reassurance, and the ability to notice everything that is not on a channel. (**mechanism**)

Its costs are real and are not the same costs. It is experienced as surveillance. It is frequently
allocated to the least experienced person available, which inverts the skill requirement. It is
expensive, so it is rationed by availability rather than by need. And it can substitute for
addressing the cause: continuous observation of someone who is falling because of a drug, a
delirium precipitant or an unmet need is a way of containing the consequence while the cause
continues. (**consensus**) It needs an indication, a review point and a plan for stopping, exactly
as m038 argues about a device.

## The human stakes, said plainly

Being watched is not a neutral experience, and the people most likely to be continuously observed
are the people least able to consent to it or to object. Someone who is confused, frightened,
withdrawn or very unwell is being observed because of a risk that is real — and from the inside it
can be experienced as being guarded rather than cared for. The difference between those two
experiences is made almost entirely by whether the person doing it talks to them, explains what is
happening, and treats the time as time with a person rather than a shift spent on a chair.

Where observation is in place because of risk to the person themselves — self-harm, severe
distress, a mental-health crisis — the whole subject sits inside a legal and ethical framework
about capacity, consent, restriction of liberty and least restrictive practice. That framework
differs profoundly between countries, it is not a nursing judgement made at the bedside, and
nothing in a revision answer should be used to reason about it. The reader's own legal framework
and safeguarding route are the only authority. It is named here, not explained here, because
leaving it out would misrepresent what the word "observation" covers.

Two further things belong to real people rather than to mechanism. Alarms are experienced, not
just responded to: continuous audible alarms are a documented cause of sleep deprivation in
hospital, sleep deprivation is a delirium precipitant, and the person in the next bed is also
awake. And being monitored is frequently understood by patients and families as being *watched
over* — so the removal of a monitor, which is usually good news, is often heard as being
abandoned. Saying why it is coming off takes a sentence and is routinely omitted.

Finally, the context. Observation frequency is set by staffing at least as much as by clinical
need, and an institution that responds to a missed deterioration by increasing the required
frequency without changing the staffing has made the records worse and the care no better. That is
not cynicism; it is the same identification-of-the-wrong-variable argument this specialty makes
about hand hygiene, documentation and fatigue.

## What an examiner digs into next

The sampling argument, with an example of each of the three relations between event duration and
interval. Why a normal observation set is a statement about an instant and is read as a statement
about an interval. The three things continuous monitoring buys and the four it costs. Why alarm
fatigue is a design property. The afferent and efferent limbs, and the evidence about which one
fails. Why a continuous record nobody reads is worse than none. What an individualised monitoring
plan contains and who authorises it locally. Why enhanced human observation is a different
intervention rather than a higher setting. And the local answers: where the monitoring plan is
written, who sets alarm limits, what the escalation route is when nobody answers, and what the
legal framework is for observation imposed for someone's own safety.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to
this answer:

* The reader's **national guidance on recognising and responding to acute deterioration**, which
  is where the individualised monitoring plan requirement and the escalation structure live, and
  which differs by country.
* The reader's institutional policy on physiological monitoring and on alarm management, including
  default alarm limits, who may change them, and the escalation route when an alarm is not
  answered.
* The reader's national patient safety body's alerts on clinical alarms and alarm fatigue.
* The published literature on afferent and efferent limb failure in rapid-response systems, which
  rests on observational and audit evidence rather than on mechanism, and on the trials of
  continuous ward monitoring, whose results are mixed.
* The reader's institutional policy on enhanced, constant or one-to-one observation, including its
  indications, authorisation and review.
* The reader's own legal framework on capacity, consent and deprivation of liberty, and the local
  safeguarding route, for observation imposed for someone's own safety. This is law and differs
  profoundly between countries.
* A current textbook of clinical measurement, for the sampling and artefact arguments.

## Scope and safety

This explains what intermittent and continuous observation each measure and where the chain they
sit in actually fails, at the level of someone already training in or qualified for clinical
practice. It is not a monitoring policy, not an escalation protocol and not guidance on enhanced
observation. It states no observation interval, no alarm limit and no monitoring threshold,
because all of those are set by the reader's national guidance and local policy, which are the
authority. It is explicitly **not** a basis for any decision about observation imposed for a
person's own safety: that involves capacity, consent and restriction of liberty, and belongs to
the reader's own legal framework and safeguarding route. Nothing here has had clinical review, and
nothing here is for use in an emergency or for a decision about any person's care. If someone is
unwell right now, the local emergency number is the correct response.

## Where this stands, October 2026

The sampling argument is mathematics and does not date. The afferent-and-efferent-limb framing has
been stable for two decades and the finding that the back half is the usual failure point has been
reproduced many times. What is genuinely unsettled is whether continuous monitoring of general
ward patients improves outcomes: wearable and contactless continuous monitoring has moved quickly,
the trial evidence is mixed, and the plausible mechanism for the mixed result is the one this
answer gives — that it improves a limb that was not the bottleneck. Expect that literature to look
different in a few years, and expect the direction of travel in alarm management to continue
toward fewer, better-targeted alarms. Everything procedural — intervals, default limits, who
authorises what, and the whole framework around observation for a person's own safety — is local
and legal and moves independently. The reader's national deterioration guidance, institutional
policy and legal framework are the authority throughout.
