---
id: "m013"
slug: screening-and-its-harms
style: serious
category: general-practice
difficulty: advanced
question: "Why is a screening programme not simply more testing, and what do lead-time bias, length bias and overdiagnosis each do to its apparent benefit?"
tags: [screening, overdiagnosis, lead-time-bias, length-bias, public-health]
---

# Screening is an offer made to people who have not complained

Everything difficult about screening follows from that one structural fact. A diagnostic test is
requested by someone with a problem, and the default — doing nothing — is already failing them. A
screening test is offered by a system to a population that is, overwhelmingly, well, and the
default is genuinely acceptable. That inverts the burden of proof: the programme has to show it
does more good than harm, because the harms land on people who had nothing wrong with them and
would otherwise have had an uneventful year *[consensus]*.

So "more testing is better" is not a conservative position. It is a strong claim, and three
specific statistical artefacts make a programme look as though it has justified that claim when it
has not.

## Lead-time bias

```
   ILLUSTRATIVE ONLY — round numbers to show the mechanism, not any real disease.
   One disease, one fixed date of death, two detection points.

   biological onset       becomes detectable       symptoms appear        death
        │                        │                       │                 │
   year 0 ───────────────────── 4 ───────────────────── 8 ─────────────── 10
                                │                       │
          screen-detected ──────┘                       └────── symptom-detected
          survival from diagnosis:  6 years                     survival:  2 years
          counted as a 5-year survivor:  YES                    counted:   NO

   Five-year survival moved from 0 % to 100 %. The date of death did not move at all.
```

Survival measured from the date of diagnosis is not a measure of benefit, because screening moves
the date of diagnosis by construction. The only measure that cannot be gamed this way is
disease-specific mortality — ideally all-cause mortality — in the whole *invited* population,
compared with a whole uninvited population, counted from the moment of invitation regardless of
who attended *[consensus]*. Stage-shift, survival rates and case fatality are all compatible with
zero benefit.

## Length bias, and overdiagnosis as its limiting case

```
   ILLUSTRATIVE ONLY. Two subtypes of one disease, identical incidence, different
   sojourn time (the period in which it is detectable but silent).

   subtype        new cases / yr    sojourn (yrs)    detectable pool at any instant
   ───────────    ──────────────    ─────────────    ──────────────────────────────
   slow   (S)            100              10              100 × 10   =  1 000
   fast   (F)            100               0.5            100 ×  0.5 =     50

   A screening round samples the POOL, not the incidence. It returns twenty slow cases
   for every fast one, though the two are equally common as new cases.

   Consequence: the screen-detected group has a better outcome than the
   symptom-detected group even if screening changed nothing for anybody, because it is
   made of different disease.

   OVERDIAGNOSIS is the same mechanism at its limit — sojourn longer than the person's
   remaining life, so the disease would never have surfaced at all.

   Population signature of overdiagnosis:
        incidence of the diagnosis     ▲  rises, and stays risen
        disease-specific mortality     ─  flat
        late-stage incidence           ─  flat, when a working screen should lower it
```

Three things about overdiagnosis are worth saying precisely because they are counter-intuitive.

* **It is not a false positive.** The disease meets the pathological definition. The test was
  right. The diagnosis is correct and the person still did not need it.
* **It cannot be identified in any individual.** Once found, it is treated, and a person treated
  for something that would never have harmed them is indistinguishable from a person whose life
  was saved. The quantity only exists at population level. This is why the conversation in a
  single consultation is so hard: the honest statement is about a rate, and the person is not a
  rate.
* **Its harms are the full harms of the diagnosis.** Investigation, treatment and its
  complications, the change in how someone understands their own body, and the downstream effects
  on insurance and employment in some systems *[country-dependent]*.

## Why the decision is population-level even though the consultation is not

A programme's arithmetic is a balance of counts over a whole invited cohort: how many are invited,
how many attend, how many are recalled, how many are investigated, how many are harmed by the
investigation, how many are overdiagnosed, and how many deaths are averted. Expressed per person
it is almost always a small benefit and a small harm spread over a very large number of people, so
the aggregate decision is a public-health judgement made with data no single clinician sees.

The consultation is the opposite. It is one person asking whether to attend, and the honest answer
involves a benefit they probably will not get and a harm they probably will not suffer. Two things
make that tractable without being misleading: presenting both directions in the same units over
the same denominator and the same time horizon, and being explicit that the recommendation is a
population judgement which an individual is entitled to decline.

Classical conditions for a worthwhile programme were set out decades ago by the World Health
Organization and have been revised repeatedly since; they remain the standard frame, and the
revisions have mostly been about adding the harms side and the requirement for an organised
programme rather than opportunistic testing *[consensus]*.

**Which programmes exist, at what ages, and at what intervals differs substantially between
countries** — including between countries with similar wealth and similar disease burden, because
the judgement depends on local incidence, local capacity, local treatment pathways and local
tolerance of overdiagnosis *[country-dependent]*. For that reason no interval, age range or
threshold appears in this answer. A reader comparing two countries' programmes and concluding that
one must be wrong has usually not read either one's published rationale.

## What an examiner digs into next

Whether the candidate rejects survival-from-diagnosis as evidence without being prompted. Then
whether they can separate length bias from overdiagnosis rather than treating them as one thing.
Then the signature of overdiagnosis in routine data, and why it takes a long follow-up to see.
Then the consultation itself: how to describe a small absolute benefit and a small absolute harm
over the same denominator, and what to do when someone asks for the recommendation rather than the
numbers.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* The World Health Organization's published principles for screening, in its original form and in
  the later revisions issued by the same organisation, for the conditions a programme must meet.
* The published rationale, age range and interval for each programme operating in the reader's own
  country, issued by that country's national screening body or equivalent committee
  *[country-dependent]*.
* The information leaflet that the reader's own national programme sends with its invitations,
  which is the document that actually states the benefits and harms to the public in that country.
* Any standard textbook of epidemiology or public health, for the derivations of lead-time bias,
  length-biased sampling and the relationship between incidence, prevalence and sojourn time.
* The methods chapter of any randomised trial of a screening programme, for why outcomes are
  analysed by invitation rather than by attendance.
* Any systematic review of overdiagnosis for the specific disease in question, in the
  epidemiological literature, for the estimated magnitude — which is contested, and the range
  between estimates is wide.

## Scope and safety

This is revision material about how a public-health intervention is evaluated, written for someone
already training in or qualified for the field. It is not a clinical reference, not a decision
aid, and nothing here should inform whether any individual attends a screening appointment — that
conversation belongs with the person's own clinician and with the information their national
programme publishes. No age range, interval or threshold appears here on purpose, because those
figures differ by country and are revised. All worked numbers are hypothetical round figures
illustrating a mechanism and describe no real disease. If someone is unwell right now, the
relevant action is to contact local urgent care or the local emergency number, not to read this.

## Where this stands, October 2026

Lead-time bias, length-biased sampling and overdiagnosis are long-settled statistical facts and
are not in dispute. What is actively contested, and moving, is the *magnitude* of overdiagnosis
for several specific programmes, and the resulting decisions about whom to invite and how often.
Those decisions are being revised in several countries, in both directions, and in some cases risk
stratification is replacing a single population-wide interval. Anyone relying on a specific
interval or age range should take it from their own national programme's current publication
rather than from here. Correct as a description of consensus in October 2026.
