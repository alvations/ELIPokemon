---
id: "m053"
slug: acne-mechanism-and-sequence
style: pokemon
category: dermatology
difficulty: intermediate
question: "What are the mechanisms of acne, and why does the order in which treatments are added follow from them?"
tags: [acne, pilosebaceous, retinoid, stewardship, scarring]
---

# You cannot Surf before Koga, and no amount of base power moves the boulder

Kanto's field moves do not unlock in order of how hard they hit. They unlock in order of badge,
and the check is written into the menu code as a single bit test that refuses with *a new badge is
required* if the bit is clear:

```
   THE ORDER IS A DEPENDENCY GRAPH, NOT A DIFFICULTY CURVE
   ==================================================================================

   BADGE             FROM             THE FIELD MOVE IT PERMITS
   ===============   ==============   ====================================
   Boulder Badge     Brock            FLASH
   Cascade Badge     Misty            CUT
   Thunder Badge     Lt. Surge        FLY
   Rainbow Badge     Erika            STRENGTH
   Soul Badge        Koga             SURF
   ===============   ==============   ====================================
   A level-100 Gyarados that knows Surf cannot use it on the overworld
   before Koga. Not "it is hard". The game refuses.
   And the boulder in the way needs STRENGTH specifically -- Hyper Beam has
   150 base power and does nothing whatsoever to a boulder.
   ==================================================================================
```

Acne's treatment sequence is that kind of ordering. Four mechanisms interact in the pilosebaceous
unit, one of them sits upstream of the other three, and an agent that does not touch the upstream
one cannot hold a result no matter how hard it hits. The boulder needs Strength.

## The four mechanisms, and the one that is the boulder

**One: altered follicular keratinisation.** Corneocytes lining the follicular duct stop shedding
properly and plug it. The resulting **microcomedo** is the primary lesion and the precursor of
everything you can see. This is the upstream step.

**Two: sebum.** Sebaceous glands enlarge and output rises under androgen drive — which is why the
condition starts around adrenarche and puberty and not before. Composition changes as well as
quantity. Sebum is substrate.

**Three: the follicular microbiome.** *Cutibacterium acnes*, formerly *Propionibacterium acnes*,
proliferates in the lipid-rich, relatively anaerobic plugged duct. It is a commensal, present on
everybody, and the modern account is about strain differences and biofilm rather than simple
overgrowth. Acne is not an infection, and the stewardship problem below starts with people
treating it as one.

**Four: inflammation.** Innate immune activation around the follicle, neutrophils, and eventually
rupture of the follicular wall into the dermis, which produces the deep slow lesions. The old
teaching put inflammation after the comedo; the current position is that inflammatory change is
detectable early, in skin that looks clinically normal. That revision is the argument for treating
early rather than waiting.

## The four-move limit is the reason combination therapy exists

A Pokémon carries at most **four** moves, and the limit is not a suggestion — the slots are fixed
and learning a fifth means deleting one. Anyone who has built a team knows what follows: no single
Pokémon covers everything, so coverage is assembled across the party.

```
   THE DEPENDENCY GRAPH
   ==================================================================================

   AGENT CLASS              1 KERATIN   2 SEBUM   3 C. ACNES   4 INFLAMMATION
   ======================   =========   =======   ==========   ==============
   topical retinoid           YES         no          no          partial
   benzoyl peroxide           partial     no         YES          partial
   topical antibiotic          no         no         YES            YES
   oral antibiotic             no         no         YES            YES
   azelaic acid               partial     no         YES          partial
   combined oral              partial    YES       indirect      indirect
     contraceptive /
     anti-androgen
   oral isotretinoin          YES        YES       indirect        YES
   ======================   =========   =======   ==========   ==============
   Read the FIRST column downwards. Two rows carry a YES, and one of them is the
   oral agent with the most requirements attached to it in the whole specialty.
   That is why a topical retinoid is the foundation of almost every regimen and
   almost every maintenance plan, and not a thing somebody graduates to.
   STRENGTH is in that column. Hyper Beam is not.
   ==================================================================================
```

## PP is the stewardship argument, and it is already in the game

Every move has a **PP** count and the counts are small. **Toxic** has 10. **Thunder** has 10.
**Fissure** has 5. Spend them and they are gone, and when the last one on the last move is gone
the Pokémon is reduced to **Struggle** — 50 base power, 1 PP, typed as the recoil effect, which is
to say it damages the user as well. The shared resource ran out, and the fallback hurts the thing
using it.

Antibiotic monotherapy in acne, topical or oral, selects resistant *C. acnes* and resistant
commensals including staphylococci and streptococci, and that resistance is transmissible and
persists. The standard answer is to pair every antibiotic with benzoyl peroxide or a retinoid, to
cap the duration of oral courses, and not to run a topical and an oral antibiotic of the same
class together. Benzoyl peroxide is the partner of choice specifically because it kills by
oxidation and acquired resistance to it is not described — which in this register is a move with
no PP cost at all. The duration caps and the preferred agents are **country-dependent**.

## Choice Band, which is what monotherapy actually buys you

A **Choice Band** raises the holder's Attack to one and a half times, and the in-game description
tells you the price in nine words: *raises a move's power, but permits only that move*. The
implementation enforces it — the code stores the chosen move and refuses every other slot for as
long as the item is held.

That is monotherapy. A single agent, used harder, with the other three columns of the table locked
out. It is a trade with a known cost and not a free upgrade, and it is the shape of the regimen
that quietly fails at month four.

## The things that look like escalation and are not

**Adequate duration before judging.** Follicular keratinisation normalises over weeks, so a
regimen gets a real trial — of the order of two to three months — before it is called a failure.
Early irritation from a retinoid is expected, is related to how much and how often, and is the
commonest reason a regimen is dropped in week two. Establishing what was actually applied comes
before escalating; the sibling answer in this set on topical quantity is the general case.

**Maintenance is its own phase.** Clearing the visible lesions does not touch mechanism one.
Continuing a topical retinoid after clearance is what stops the microcomedones re-accumulating. An
**Everstone** is the right image for this one: it does not do anything you can see, it holds a
state in place, and taking it off has consequences later rather than immediately.

**Treat early where scarring is in prospect.** Nodulocystic disease, truncal disease, a family
history of scarring, existing scars and significant psychological impact all shorten the
observation period, because the endpoint being avoided does not resolve. Which of those is a
referral threshold is **country-dependent**.

And on irreversibility, the games are unusually clean. Evolution runs one way. There is an item
that prevents it — the **Everstone**, whose hold effect in the code is literally named as
preventing evolution — and there is no item, move, ability or machine anywhere in the series that
reverses it. Atrophic scarring is that box: ice-pick, boxcar and rolling scars, plus
post-inflammatory pigmentation and erythema. Everything upstream of it is treatable. Nothing
downstream of it is.

## The Master Ball, and why having one is not a reason to throw it on Route 1

**The Master Ball always succeeds.** The catch routine in Pokémon Red does not compute anything
for it — it compares the item against MASTER_BALL and jumps straight to the captured branch. There
is exactly one in a standard playthrough, everybody knows where it is, and nobody spends it on a
Route 1 **Rattata**.

Oral isotretinoin is the bottom row of the table: it acts on sebaceous gland size and output,
normalises follicular keratinisation, reduces *C. acnes* as a consequence of removing its
environment, and is anti-inflammatory. Every column. That is the mechanistic reason it is the most
effective agent available, and the reason it is not simply used first is everything attached to it
rather than anything about its effect.

The attachments are real and they are not reproduced here. It is a potent human teratogen, and
every country that licenses it runs a pregnancy prevention framework around it — contraception
requirements, pregnancy testing before, during and after, and limits on the quantity dispensed.
Mucocutaneous effects are near-universal. Baseline and on-treatment monitoring is required and the
panel differs by country. Prescribing is usually restricted to specialists. Your national
regulator is the authority on all of it. [country-dependent]

## Where the metaphor stops

This section carries no Pokémon, because the mechanism is over and the consequences are not
something to be cute about.

The psychiatric question around isotretinoin has to be stated without hedging in either direction.
Depression, mood change and suicidality have been reviewed repeatedly by national regulators, and
the position in several countries is that a causal link is not established but that the signal is
taken seriously enough to require counselling and mental-health monitoring before and during
treatment. That is where it stands: not settled, not dismissed, actively under review. People
taking it are asked about their mood because mood matters. Anyone taking it who notices a change
in how they feel should be able to say so to their prescriber and be taken seriously, and anyone
having thoughts of self-harm needs help from a person, now, rather than a page about mechanisms.

Acne is routinely described as trivial by people who do not have it, and that description is part
of the harm. It happens on the face, at the age when a person's face matters most to them, for
years, in full view, and it is one of the few medical conditions strangers feel entitled to
comment on. It is reliably associated with reduced quality of life, social withdrawal, and with
depression and anxiety. The association is strong and it does not track the severity grade a
clinician assigns — a person with mild acne by any scoring system can be severely affected by it,
and that is not a misperception to be corrected.

Scarring is permanent, and the fact that it is permanent is what makes delay expensive. Someone
who was told for two years to grow out of it and who now has atrophic scars has been let down in a
way that cannot be put right afterwards. That is a stronger argument for treating properly and
early than any of the mechanism above.

A few presentations are not acne and need saying plainly: an abrupt monomorphic papulopustular
eruption **without comedones** is an acneiform drug eruption; acne fulminans is abrupt, ulcerating
and systemically unwell, and is urgent; and acne of abrupt onset in an adult woman with hirsutism,
menstrual irregularity or features suggesting virilisation prompts endocrine assessment rather
than only dermatological treatment.

Without softening: no agent, combination, duration or monitoring requirement in this answer is for
any reader's own use. Anyone with acne that is scarring, not responding, or affecting how they
live needs their own clinician.

## What a Gym Leader is listening for

Why a topical retinoid is the foundation of a regimen rather than an escalation, in terms of the
four mechanisms — which in this register is why the boulder needs **Strength** and not **Hyper
Beam**. Why benzoyl peroxide is the partner chosen for an antibiotic rather than a second
antibiotic. What you would check before concluding a regimen has failed at six weeks. Why
clearance is not the end of treatment. What the absence of comedones tells you. And what in a
presentation would shorten your observation period before escalating.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in the dermatology sources file in the
writers' directory for this domain, and they are the authority for everything procedural or
quantitative here. Specific to this answer:

* For the agents, the combinations, the duration limits on oral antibiotics and the monitoring:
  the acne section of your national formulary, and the acne guideline issued by the national body
  that sets guidance where you practise.
* For isotretinoin — the pregnancy prevention framework, the dispensing limits, the monitoring
  panel and the mental-health counselling requirements: the materials issued by your national
  medicines regulator for that drug, and the summary of product characteristics. These are the
  authority, they differ between countries, they have been revised, and nothing here reproduces
  them.
* For antimicrobial stewardship in acne: your national stewardship guidance and your local
  microbiology policy, which set the duration caps and the preferred agents.
* For the pathogenesis, the lesion types and the scarring morphologies: a current standard
  textbook of dermatology.
* For the early-inflammation revision and the strain-level microbiome work: the primary
  literature.

The Pokémon claims were checked separately against source. The badge gating of the field moves —
Flash behind the Boulder Badge, Cut behind the Cascade Badge, Fly behind the Thunder Badge,
Strength behind the Rainbow Badge and Surf behind the Soul Badge, each as a bit test that refuses
with a new-badge message — and the Master Ball's catch routine jumping straight to the captured
branch without computing anything are from the pret decompilation of Pokémon Red. Hyper Beam's 150
base power, Toxic's and Thunder's 10 PP, Fissure's 5 PP, Struggle's 50 base power and 1 PP and
recoil effect, the four-move limit, the Choice Band's one-and-a-half multiplier on Attack with its
stored chosen move enforced in code, its in-game description, and the Everstone's hold effect
being named as preventing evolution are from the pret decompilation of Pokémon Emerald. That no
item, move or machine anywhere in the series reverses an evolution is an observation about the
games rather than a line of code, and is stated as such.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

**No agent, combination, course length or monitoring requirement named here is a prescribing
instruction, and none of it addresses any reader's own treatment.** Isotretinoin in particular is
discussed only to explain why its mechanism makes it effective and why its risks make it
restricted; its contraception, testing, dispensing and monitoring requirements are set by national
regulators, differ between countries, and have deliberately not been reproduced. An answer here
agreeing with your memory is not confirmation.

Anyone with acne that is scarring, painful, rapidly worsening, or accompanied by systemic symptoms
needs to be seen rather than to read about it. Anyone whose mood is affected — by the condition or
by a treatment for it — needs to be able to say so to a clinician, and anyone having thoughts of
self-harm needs urgent help from a person rather than information from a revision page.

Local guidance and the formulary where you practise are the authority on all of this, and they
differ by country and by institution.

## Where this stands, October 2026

The four-mechanism model is stable and is what the sequencing rests on. Two parts of it have
shifted in the last decade and are worth knowing as shifts rather than as facts: inflammation as
an early rather than a late event, which strengthened the case for early treatment, and the move
away from *C. acnes* as an overgrowing pathogen towards strain-level and biofilm accounts. The
genus name itself changed, from *Propionibacterium* to *Cutibacterium*, so older material reads
differently — the same problem as quoting a **Super Potion** figure without naming its generation.
What moves fastest here is regulatory: isotretinoin's pregnancy prevention and mental-health
monitoring requirements have been revised more than once and differ between countries, and the
duration caps on oral antibiotics are tightening as stewardship guidance is rewritten. Check the
current documents rather than this one. Current as of October 2026.
