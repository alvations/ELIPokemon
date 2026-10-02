---
id: "m032"
slug: why-protocols-exist
style: serious
category: emergency
difficulty: intermediate
question: "Why are time-critical decisions written down as protocols instead of left to individual clinical judgement?"
tags: [protocols, cognitive-load, variance, standardisation, human-factors]
---

# Because variance is the harm, and a rare decision is where variance is widest

A protocol exists where three conditions hold at once: the decision is **time-critical**, so there
is no opportunity to look anything up or think it through; the consequences are **high-stakes**,
so the cost of being wrong is not recoverable; and the event is **low-frequency**, so no
individual accumulates enough personal experience of it to have a well-calibrated judgement. Any
two of those without the third does not need a protocol. All three together, and individual
judgement is the wrong instrument — not because individuals are bad at deciding, but because the
*spread* of their decisions is wide and the tail of that spread is where the harm lives.
**(Mechanism** — this is an argument about distributions, and it stands or falls on its own
logic.**)**

The honest version of the argument is unflattering and worth saying plainly: a protocol usually
encodes more pooled experience than the person following it has. It was written by a group with
access to aggregate outcomes that no single clinician sees, and revised against evidence that
accumulated across populations. So deviating because *I have done a lot of these* is a bad reason.
Deviating because *this is not the situation the protocol is for* is a good one, and telling those
two apart is the actual skill that the existence of protocols demands.

## The three things a protocol buys

**It externalises the sequence so it does not have to be held in mind.** Working memory is small
and it degrades under threat, noise, time pressure and sleep deprivation. A written sequence turns
recall into reading, and reading is far more robust. More importantly it frees the capacity that
was holding the sequence for the thing a protocol cannot do, which is noticing that the situation
has changed.

**It compresses the distribution.** This is the part most often skipped, and it is the strongest
argument.

```
   a rare, high-stakes decision, over many clinicians facing it
   ─────────────────────────────────────────────────────────────────────────────────

   individual judgement        ░░▒▒▓▓███▓▓▒▒░░░░░░░░░░░░░░░        wide
                              └─── a few are better than any protocol
                                        and the left tail is the harm ───┘

   protocol-governed           ░░░░▒▓████▓▒░░░░                    narrow
                                   └─ ceiling slightly lower,
                                      floor very much higher

   ─────────────────────────────────────────────────────────────────────────────────
   the trade: give up some of the best case to delete most of the worst case
```

A protocol is a deliberate reduction in **expected peak performance** in exchange for a large
reduction in **variance**. That trade is correct whenever the loss function is asymmetric —
whenever being badly wrong costs far more than being slightly suboptimal costs. In a time-critical
resuscitation it is overwhelmingly asymmetric, which is why this is the one area of practice most
heavily proceduralised.

**It is a shared schema, so strangers can interleave.** A team assembled from whoever was nearby
has no shared history. A protocol lets each member predict what the others will do next without
asking, which means hands can be in several places at once without negotiation. This is why the
written form matters as much as the content: a protocol that everyone knows but which is worded
differently in two departments loses most of this benefit.

## The four things it gives up

* **It is wrong at the edges by construction.** A protocol is fitted to the central mass of cases.
  The atypical case is where it performs worst, and that is also where a clinician is least likely
  to notice, because the protocol is running and feels like progress.
* **It can crowd out the recognition that this is not that situation.** The failure is not
  following the protocol badly; it is following the correct protocol for the wrong problem,
  fluently and to completion.
* **It manufactures a feeling of completion.** Finishing the steps is not the same as having
  solved anything, which is why structured approaches are explicitly built to be repeated.
* **It moves the error upstream and makes it systematic.** One clinician's misjudgement harms the
  people in front of them. A badly written protocol harms everyone who follows it, everywhere,
  until it is revised. That is the price of removing variance: the remaining error is no longer
  random, so it does not average out.

## Why the written form, specifically

Writing a decision down does three things that agreeing on it does not.

```
   agreed informally                     written down
   ───────────────────────────────────────────────────────────────────
   drifts, silently                      drifts visibly, in revisions
   cannot be audited against             can be audited against
   cannot be taught identically twice    can
   cannot be extended by a stranger      can
   fails open under stress               fails closed under stress
   ───────────────────────────────────────────────────────────────────
```

The last row is the subtle one. An informal agreement under stress collapses toward whatever each
individual thinks best, which is exactly the wide distribution the protocol existed to remove. A
written protocol under stress collapses toward the document.

## What an examiner digs into next

* What are the three conditions, and what happens if only two of them hold?
* Why is variance reduction worth a lower ceiling, and when is it not?
* What distinguishes a legitimate deviation from an illegitimate one?
* Why does a protocol make errors systematic rather than random, and why is that sometimes an
  improvement and sometimes much worse?
* What is lost when two neighbouring departments use differently worded versions of the same
  protocol?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* The current life support guidelines issued by **the national resuscitation council for the
  country the reader practises in**, which are the clearest worked example of a protocol with all
  three conditions present. The councils differ from one another and each revises on its own
  cycle.
* The current consensus on science with treatment recommendations issued by **the International
  Liaison Committee on Resuscitation**, which is the evidence synthesis the national councils
  write from, and which is also the place to see how a protocol is argued for rather than
  asserted.
* **The reader's own employing organisation's** clinical policy and standard operating procedures,
  which are the documents that actually bind practice and which outrank every general account
  including this one.
* The human-factors and crew-resource-management literature as taught on **the reader's own
  institution's** mandatory training, which is where the cognitive-load argument is usually set
  out in a form specific to that institution's protocols.

Claims here are marked **mechanism** (an argument about distributions and about working memory,
checkable by reasoning), **consensus** (agreed across the major councils as of writing), or
**council-dependent** (genuinely different between councils). Nothing is quoted from any of these
documents, and no guideline number, document title or identifier is given, because none was
opened.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *why protocols are built the way they are*, written for someone
already trained. It is deliberately not a protocol and contains none: no sequence of actions, no
rates, no depths, no ratios, no doses, no settings. It is not a reference to be consulted while
acting. Resuscitation guidance **differs between national councils and is revised on a cycle**,
and the differences land precisely on the specifics this answer declines to state. The reader's
own national council and local policy are the authority; this is not, and it has had no clinical
review. Nothing here describes any real person, case or institution.

## Where this stands, October 2026

The three-conditions framing, the variance argument and the shared-schema argument are the
standard justifications and are not controversial as reasoning; they are **mechanism**, and a
reader can check them by thinking rather than by looking anything up. What is
**council-dependent** is every particular: which decisions are proceduralised, how prescriptive
each protocol is, how deviation is documented and reviewed, and how often the document is revised.
Several national councils publish on multi-year cycles that are not synchronised with each other,
so two readers in different countries can both be correct and disagree. Dated October 2026; the
current document from the reader's own council is the authority on everything specific.
