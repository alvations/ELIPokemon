---
id: "m001"
slug: early-warning-scores
style: pokemon
category: nursing
difficulty: intermediate
question: "Why does a composite score built from simple bedside observations detect deterioration earlier than any single observation?"
tags: [observations, early-warning-score, deterioration, escalation, compensation]
---

# The HP bar is one field on the summary screen. Reading only the bar loses the battle.

A Pokémon's condition is not one number. It is a set of separate, small, cheap readings, every one
of them visible without any equipment: the HP bar, the single icon in the status slot, the stat
stages, the field condition, and the PP left on four moves. A composite early warning score is the
discipline of reading **all** of them and adding them up, rather than glancing at the bar.

The games make the case for the composite better than any argument could, because the status slot
holds **exactly one** condition at a time. **Burn**, poison, **Badly Poisoned**, paralysis, sleep
and freeze are mutually exclusive — land **Will-O-Wisp** on something already asleep and nothing
happens. One slot, one icon. And yet each of those six does something completely different to the
Pokémon, *and none of them touches the HP bar you were looking at*.

The sentence that matters: **the icon is not a diagnosis and the bar is not a severity index —
together they report the price the Pokémon is paying to stay on the field.** The slot is blind to
cause. A burn from **Will-O-Wisp**, a burn from a **Flame Orb** the Pokémon is holding on purpose,
and a burn from a **Scald** that was aimed at something else all print the same icon. That
blindness is the design. The reading gets someone to the field; working out why is the next job.

## What the readings are actually detecting

A Pokémon that is still standing and still swinging is not therefore fine. It is paying, every
turn, out of a reserve, and each condition charges differently:

```
   reading           what it is actually reporting              when it moves
   ────────────────  ─────────────────────────────────────────  ──────────────────────
   Burn              an eighth of maximum HP at the end of      immediately, and it
                     EVERY turn in the Advance games, and       never stops
                     physical damage halved
   Badly Poisoned    a sixteenth on the first turn, two         slowly, then fast; the
                     sixteenths on the second, three on the     counter IS the warning
                     third — a counter that only climbs
   paralysis         Speed cut to a quarter in the Advance      intermittently — easy
                     games, and one turn in four simply does    to call bad luck
                     not happen
   sleep             a length rolled the moment it lands;       all at once, and the
                     nothing at all happens until it ends       length is already set
   freeze            nothing happens until it thaws; a Fire-    all at once; Ice-types
                     type hit thaws it, and harsh sun stops     cannot take this at all
                     it landing in the first place
   HP bar            everything above, after the fact           LAST. A full bar is not
                                                                reassurance
   PP and stages     whether the Pokémon can still do the       quietly, and nobody is
                     thing you are counting on it for           looking
```

Three properties follow, and they are the whole argument for reading the screen rather than the
bar.

**Small deviations matter when they co-occur.** A Pokémon one stage down in Speed is nothing. A
Pokémon one stage down in Speed, **Badly Poisoned** at counter two, and holding a **Life Orb**
that costs it HP every time it attacks, is three small things in three different places — and
three small things is a pattern. Stat stages run only from −6 to +6, so each single stage looks
trivially small; the sum of several does not.

**One misread field does not ruin the read.** Mistake a **Pokérus** marker for an illness, or
misjudge how full a bar is at a glance, and a composite read loses a little. A plan that hangs
entirely on that one field loses everything.

**A composite travels.** The whole point of the summary screen is that it can be handed to someone
else. "Level 36, **Badly Poisoned**, counter at four, Speed down two" is a thing another Trainer
can act on. "It looks a bit rough" is not.

## The failure modes, which matter more than the readings

### The one that reads fine and is one turn from the floor

**Dragonite** with its hidden ability, **Multiscale**, takes half damage from everything *while
its HP is full*. Full bar, clean status slot, nothing to score. The moment the bar moves off full
by a single point the protection is gone, and the next hit lands at double what the last one did.
The reading was flat, flat, flat, then catastrophic — and nothing in the flat part was wrong.

A **Focus Sash** is the same story with the reserve already spent. The bar says 1. There is no
second **Focus Sash**. A reading of "1 HP, no status" scores almost nothing and means almost
everything, and whether it is early or terminal depends entirely on whether anyone watched it get
there. This is why a **Battle Video** beats a screenshot: the shape between two readings is the
measurement, and a single frame is not an observation about the trajectory at all.

Reference ranges also depend on which Pokémon is in front of you. **Eviolite** raises both
defences by half — but *only* for a Pokémon that can still evolve. A rule that is correct for one
category and wrong for the next is exactly why the games keep separate rules per category instead
of one chart for everything.

### The chronically abnormal baseline

**Shedinja** has a maximum HP of **1**. Not low — one, at every level, with any training, forever,
because its base HP stat really is 1. A reading of "1 HP" on a Shedinja is a full bar. Treat it as
an emergency and the time is wasted; treat every Pokémon's 1 as a Shedinja's and someone dies. Its
**Wonder Guard** is the rest of the story: the only damaging moves that affect it at all are
super-effective ones, so the usual relationship between what is thrown and what lands does not
hold either.

**Slaking** is the other shape. Base stats of 150/160/100 — enormous — and **Truant**, which means
it moves only every other turn. A Slaking that does nothing this turn is not deteriorating. That
is Tuesday. A reading that is permanently abnormal stops being read at all, which is its own
hazard, and the fix is not to adjust the screen quietly but to write down, where the readings are
written, that this Pokémon's normal is not the normal.

**Pokérus** is the trap in the other direction. It puts a marker on the status screen that looks
like something has gone wrong, cannot be cleared at a **Pokémon Center**, and is in fact doubling
what the Pokémon gains from every battle. An abnormal reading that needs no response at all.

### The measurement itself

The HP bar is a picture. The exact number is on the summary screen, one button away, and almost
nobody looks. Every estimate rounds toward the halves and the thirds of a bar, because that is
what a bar is for. The single most informative reading in the set is also the one that takes
deliberate effort to obtain properly, and a read built on a glance is weaker than its arithmetic
suggests.

### The read that is taken and not acted on

Noticing is not an intervention. **Full Heal** clears the icon and restores no HP; **Full
Restore** does both; a **Lum Berry** does it automatically the moment the condition lands. Some
Pokémon fix themselves — **Shed Skin** gets a one-in-three chance every turn, **Natural Cure**
clears the slot on switching out. None of that happens because the icon was observed. It happens
because somebody did something, and the useful question about any reading is what it triggers.

And the override matters as much as the ladder. A Trainer who switches out because something is
wrong before the screen says so is not being unscientific; they are using the one instrument the
screen does not contain.

## Where the metaphor stops

The paragraphs above are about a mechanism, so a game is a fair way to explain them. What the
mechanism is attached to is not a game.

A patient who is compensating is a person doing silent, expensive work to stay level, and the
reason anyone cares about the shape of a chart is that the collapse at the end of it is sudden,
frightening, and sometimes irreversible. The apparatus — the chart, the sum, the trigger, the
ladder, the phone call — exists for one purpose, which is that somebody more experienced arrives
while there is still reserve left to work with. Every part of it is a way of making that arrival
happen on time and not depend on who is on shift, how confident they feel, or whether they want to
risk waking a senior colleague. That is the whole value, and it is worth saying plainly rather
than through an analogy.

## What Nurse Joy is listening for

That the bar is the last thing to move and not the first. What the screen cannot show — what is in
the bag, what the opponent has set up, whether this Pokémon has ever been like this before. Why a
full bar on something tachycardic and cold is a worse combination than the number suggests. What
the response ladder at this particular Center actually is, who comes, and how fast. And how a
Shedinja's baseline gets written down so the next Trainer does not panic at a 1.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* The current observation chart and early warning score in use in the reader's own institution,
  together with the escalation policy printed on or alongside it — the only authority for
  parameter sets, points, trigger values and the response at each band.
* The national early warning score specification published by the reader's national body for
  clinical standards, where their country runs one, and its accompanying implementation guidance.
* The obstetric early warning tool and the paediatric age-banded tool issued for the reader's
  country, for the two populations whose reference ranges differ.
* The reader's national guidance on recognising and responding to acute deterioration in hospital,
  for the concern-based escalation route and for individualised monitoring plans.
* A standard physiology textbook, for the compensation mechanisms the second section is about,
  which are not guideline claims at all.
* The reader's institutional audit of observation completeness and respiratory-rate recording, if
  one exists, for the measurement-quality claim.

Separately, and unlike the above: the Pokémon mechanics in this answer were checked directly
against the public disassemblies of the games, which this environment could reach.

## Scope and safety

This explains the reasoning behind a class of tool, for someone already training in or qualified
for clinical practice. It is not a protocol, not a decision aid, and deliberately contains no
trigger values, because the parameter ranges, the points and the response ladder differ between
countries and between institutions and are revised. The chart and escalation policy in use where
someone works is the authority; this is not, and it has had no clinical review. Nothing here is
for use in an emergency or for a decision about any person's care. If someone is unwell right now,
the local emergency number is the correct response.

## Where this stands, October 2026

The physiology is stable and the composite-score architecture has been mainstream for two decades.
What dates quickly is everything numerical: parameter sets, weightings, trigger values,
oxygen-target handling, the obstetric and paediatric variants, and the response ladder attached to
each band. Those live in the chart and the escalation policy of the institution, which are
periodically reissued — the national score a reader was taught may not be the one on the ward they
move to. The status slot, unlike the chart, has held exactly one condition since Kanto.
