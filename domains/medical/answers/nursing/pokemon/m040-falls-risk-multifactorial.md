---
id: "m040"
slug: falls-risk-multifactorial
style: pokemon
category: nursing
difficulty: advanced
question: "Why do multifactorial falls risks resist single-intervention fixes, and why can preventing falls cause harm?"
tags: [falls, multifactorial-assessment, deconditioning, restraint, risk-scores]
---

# Speed is one number on the summary screen, and at least seven separate things multiply it.

This is not an analogy. It is the order of operations, and the games compute it in exactly this
sequence, each step applied to the output of the last:

```
   start with the Pokémon's Speed stat
     × the STAT STAGE ratio                  from −6 to +6, nothing beyond
     × a weather ABILITY                     Swift Swim, Chlorophyll, Sand Rush — each
                                              DOUBLES it, in the right weather
     × another ability                       Slow Start HALVES it while its timer runs;
                                              Unburden DOUBLES it once the item is gone;
                                              Quick Feet adds half — but only to a
                                              Pokémon that HAS a status condition
     × the player's own BADGES               in Emerald, holding the DYNAMO BADGE from
                                              Mauville City adds a tenth, to your side
                                              only
     × the held ITEM                         Macho Brace halves. Iron Ball halves.
                                              Choice Scarf adds half
     × TAILWIND                              doubles it, side-wide, for a few turns
     ÷ PARALYSIS                             by FOUR in the Advance games, by TWO from
                                              the seventh generation — the code carries
                                              both behind a configuration switch
   ──────────────────────────────────────────────────────────────────────────────────────
   They MULTIPLY. Every one of them is applied to whatever the last one produced, which
   is why no single term tells you where a slow Pokémon's Speed went.
```

Take a case. One stage down in Speed, which is the smallest stat change the game permits.
Paralysed. Holding an **Iron Ball** that somebody equipped on purpose. On a side where the
opponent has laid a **Sticky Web**, which drops the Speed of every grounded Pokémon by another
stage as it arrives. Four channels, every one of them individually trivial, and nothing in the
game will tell you that the result is the product of four trivial things rather than one serious
one.

**Now remove any single factor.** Clear the paralysis: the stage is still down, the Ball is still
on, the Web is still on the ground. Remove the Ball: the paralysis is still dividing by four. You
have divided the product by one of its terms, which is exactly the effect size a
single-intervention trial reports, and it is exactly as small as the arithmetic says it should be.

## Every protection in the games covers one channel. Read them side by side.

This is the part that makes the point unanswerable, because the games supply a whole cupboard of
single-channel defences and not one of them covers the field:

```
   protection        the game's own text                   what it does NOT touch
   ────────────────  ────────────────────────────────────  ───────────────────────────
   Clear Body        "Stats can't be lowered."             the item, the paralysis, the
   White Smoke       the same text, different species       Web already on the ground —
                     and the code gates it on the drop      and any drop the Pokémon
                     coming from OUTSIDE                    inflicts on ITSELF
   Keen Eye          "Accuracy can't be lowered."          Speed. At all. One stat
   Hyper Cutter      "Attack can't be lowered."            Speed. At all. One stat
   Mist              "Creates a mist that stops lowering   the item, the paralysis; it
                     of allies' stats."                     runs five turns and DEFOG
                                                            clears it
   Safeguard         "Protects allies from status          the stat stages, the item,
                     problems for 5 turns."                 the Web — and INFILTRATOR
                     so it blocks the PARALYSIS channel     walks straight through it
                     and precisely nothing else
   Heavy-Duty Boots  "Protects from the effects of traps   the Web, which stays exactly
                     set on the field."                     where it is for whoever
                                                            comes in without Boots
   ────────────────────────────────────────────────────────────────────────────────────
   Six protections. Each blocks ONE term in a product of seven. And none of them does
   anything at all about the Iron Ball, because the Iron Ball was equipped deliberately
   and the game has no opinion about your own decisions.
```

## Why the score is worth less than the list

The composite read off a summary screen works beautifully for one thing — the early-warning
problem, where several small readings are **added** up because each is a separate report on one
underlying state. It fails here, and the reason is structural rather than a matter of tuning.

A composite score of these channels gives you a number. The number tells you the Pokémon is slow,
which you could see. What it cannot tell you is **which factor to attack**, because a product of
seven terms has no single largest term in general and the score throws away the decomposition that
was the only useful part of the measurement. Score every Pokémon on a frail team and they all come
back high, which separates nobody from anybody.

What is worth having is not the number. It is **the list, with a name against each line**: which
stage, which item, which ability, which hazard, whose decision. That list divides. The score does
not.

The one reading worth keeping is the history. The shape between two readings beats any single
frame — a record of what happened last time is the strongest instrument in the set, and it is
strongest precisely because it is a summary of every other channel at once rather than a channel
of its own.

## Why preventing the fall can be the injury

The binding moves — **Wrap**, **Bind**, **Fire Spin**, **Clamp**, **Whirlpool** — take a share of
HP every turn and, crucially, **prevent the target switching out**. The second clause is the
injury, not the first: it is not the damage, it is the inability to get away from it.

And the games have the pure form, with no damage attached at all. **Mean Look** — *"Fixes the foe
with a mean look that prevents escape."* **Block** — *"Blocks the foe's way to prevent escape."*
**Spider Web** — *"Ensnares the foe to stop it from fleeing or switching."* Three moves, zero
damage, one effect: the Pokémon cannot leave. A Pokémon that cannot be switched out is perfectly
safe from everything on the bench and completely exposed to everything on the field, and nothing
on the screen scores that as harm.

**And the cost of being built up is paid in the present.** **Macho Brace** — *"Promotes growth,
but reduces Speed in battle."* The item that makes a Pokémon stronger over time makes it slower
right now, and a Trainer optimising only for this turn takes it off and gets a faster Pokémon that
never improves. The trade between present safety and future capability is written into an item
description, and it has a right answer only once you have decided which of the two you are being
measured on.

Which is the whole of the incentive problem. A Pokémon that is knocked around on the field
produces a visible event. A Pokémon that was never let out and therefore never grew produces
nothing — no message, no entry, nobody asking. The pressure runs one way, and any plan that does
not explicitly protect the growing will drift toward the box, because that is where the incentives
point.

## Where the metaphor stops

The arithmetic above is arithmetic, and a game is a fair way to show it. What it is attached to is
not, and both harms are real.

For a frail older person a fall in hospital can be the event that ends independent living, and the
fracture is only part of it. The fear afterwards is itself disabling, and the activity restriction
it produces makes the next fall more likely — so the psychological consequence is also a
physiological one. People describe losing confidence in their own body, and that is not a soft
outcome.

The second thing is said less often. The person who was never allowed out of the chair also lost
something, and nobody filled in a form about it. Deconditioning in an older person is measurable
within days, not weeks, and is slower to rebuild than to lose. Both harms pull in opposite
directions and the resolution is not to pick one: it is to attack the modifiable channels so that
someone can move with less risk, rather than to reduce the risk by reducing the moving.

And restriction is not a nursing preference. Whether a restriction is lawful depends on capacity,
on best-interests determination, and on the deprivation-of-liberty framework of the jurisdiction.
That is law, it differs profoundly between countries, and nothing in this answer — or in any
revision note — substitutes for it.

Finally: a staff member present when someone falls often carries it personally, and an institution
that responds by looking for the individual who was insufficiently vigilant produces exactly the
restrictive, defensive practice that harms the next patient.

## What Nurse Joy is listening for

Why a product of terms behaves differently from a sum, and what that predicts about any trial that
removes one term. Which channel on this particular Pokémon is the one somebody equipped on
purpose. Why six different protections can all be in place and the Pokémon still be slow. What the
list looks like when the score has been thrown away. Why a Pokémon that cannot be switched out is
in a worse position than the screen says. And what the local law says about preventing something
from leaving, and who decides that.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../for-agents/SOURCES-nursing.md`](../../for-agents/SOURCES-nursing.md). Specific to this
answer:

* The reader's national guidance on falls assessment and prevention in older people, for the
  multifactorial assessment components and for whether numerical risk scoring is recommended in
  inpatient settings — the recommendation that differs most between countries.
* The reader's institutional falls prevention policy, its assessment documentation and its
  post-fall procedure, including the observation schedule and the imaging criteria for someone
  taking an anticoagulant.
* The reader's national guidance on head injury, for the anticoagulation and imaging thresholds
  this answer deliberately does not state.
* The reader's national guidance on delirium, for the bidirectional relationship with falls.
* The reader's national guidance on medicines optimisation, deprescribing and polypharmacy review,
  for the medicines channel.
* The capacity, best-interests and deprivation-of-liberty legal framework of the reader's own
  jurisdiction, for anything about restriction or restraint. This is law, it differs by country,
  and nothing here substitutes for it.
* The systematic review literature on falls interventions — exercise, vitamin D, hip protectors,
  flooring, bed and chair alarms, and multifactorial programmes in hospital. These rest on trial
  evidence rather than on mechanism, and the contested ones are flagged as such in the rigorous
  half.
* A standard geriatric medicine textbook, for sarcopenia and for the rate of deconditioning with
  bed rest.

Separately, and unlike the above: the Speed calculation order, the paralysis divisor in both its
generational forms, the Dynamo Badge multiplier, the item and ability multipliers, the stat-stage
limits, the Sticky Web effect and the self-inflicted-drop exemption on Clear Body were all read
directly out of the public disassemblies of the games and their expansion, which this environment
could reach. Every ability, move and item text in quotation marks above is the game's own printed
description.

## Scope and safety

This explains why a class of risk resists a class of intervention, for someone already training in
or qualified for clinical practice. It is not a protocol, not a decision aid, not a risk
assessment tool, and it names no clinical score, threshold, observation interval or imaging
criterion, deliberately — the only numbers in it belong to a video game. It is explicitly **not**
guidance on restriction or restraint, which is a legal and capacity matter governed by the law
where the reader works. The falls policy and the legal framework where someone works are the
authority; this is not, and it has had no clinical review. Nothing here is for use in an emergency
or for a decision about any person's care, including any decision about whether a particular
person should walk. If someone is unwell right now, the local emergency number is the correct
response.

## Where this stands, October 2026

The arithmetic and the physiology are stable: multiplicative channels, and deconditioning that
starts within days. What has moved, and is still moving, is the guidance layer — the retreat from
numerical falls risk scoring in inpatient settings, the evidence on bed and chair alarms, the
vitamin D recommendations, and the legal framework governing restriction, which changes with
legislation and case law rather than with evidence. The local policy and the local law are the
authority for all of it, and the legal half will date first. The Speed calculation, by contrast,
has multiplied its terms in the same order since the Advance games, and the only thing that
changed was the paralysis divisor.
