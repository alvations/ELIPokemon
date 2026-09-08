---
id: "187"
slug: mt-in-regulated-domains
style: serious
category: translation
difficulty: advanced
question: "What changes when translation is used in medical, legal or financial contexts?"
tags: [regulated, liability, validation, audit-trail, human-in-the-loop, critical-errors]
---

# Translation where being wrong has consequences

Everything technical in this dataset still applies. What changes is that **the acceptable failure
rate is not set by you**, the failures have named consequences, and somebody will eventually ask you
to demonstrate — with records — why you believed the system was fit for use.

## The shift in what you optimise

```
   ORDINARY MT                        REGULATED MT
   ───────────                        ────────────
   maximise average quality           minimise CATASTROPHIC failures
   ship at "better than before"       ship at "validated against a defined protocol"
   metrics: COMET, chrF               metrics: critical error recall, at a stated
                                               operating point (question 132)
   a bad segment is a bad segment     a bad segment is a dosage, a deadline,
                                      a liability cap, an allergy
```

A system with excellent average quality and 3% undetected critical errors is worse here than one
with mediocre average quality and 0.1%. The whole calculus inverts, and teams carrying habits from
consumer MT get this wrong in a way that is invisible until it is not.

## What a defensible deployment includes

* **A written intended-use statement.** What content, which language pairs, which audience, what
  the output may and may not be used for. Everything else is judged against this.
* **Validation against a protocol**, not a benchmark: a defined test set built for the domain, a
  defined acceptance threshold, defined error categories with severity (MQM, question 171), and
  sign-off by a qualified person.
* **Human review in the loop where the risk requires it.** For patient-facing instructions, legal
  filings and financial disclosures, "MT plus QE" is generally not sufficient; the standard is MT
  plus **qualified human review**, with the reviewer's identity recorded.
* **An audit trail.** For every segment: source, model and version, glossary version, QE score,
  reviewer, timestamp. If you cannot reconstruct why a particular translation was produced, you
  cannot answer the question that will be asked.
* **Version pinning and change control.** A model upgrade is a change to a validated system and
  requires re-validation. "We upgraded to the latest model" is not a neutral act here.
* **Defined failure handling.** What happens when QE flags a segment, when the service is down, when
  a translation is later found to be wrong. Including recall procedures.

## The specific technical requirements

* **Critical error detection as a first-class classifier** (question 132), with its own recall
  target on a purpose-built test set: negation flips, number and unit changes, entity swaps, omitted
  clauses, added content.
* **Terminology enforced and verified**, not requested (question 133). In medicine and law the term
  *is* the meaning.
* **No silent length truncation** (question 144) — a truncated legal sentence can invert it.
* **Data residency and confidentiality.** Patient and client data crossing a border or entering a
  third-party API is often the binding constraint, ahead of quality. Check before you architect.
* **Provenance labelling.** Machine-translated content should be identifiable as such to the reader,
  and in several jurisdictions must be.

## The honest position

For high-risk content, the value of MT is usually **speed and cost in the drafting step**, not the
removal of the human. Systems sold as replacing qualified review in these domains are making a claim
their evaluation does not support, and the gap between the average-case metric and the
worst-case consequence is exactly where that claim fails.

## What an interviewer digs into next

* Why can a system with better average quality be the wrong choice here?
* What is in an audit trail, and what question is it there to answer?
* Why is a model upgrade a regulated change?
* Where does MT genuinely add value in a high-risk workflow?
