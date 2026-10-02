---
id: "m058"
slug: cortisol-excess-and-the-shape-of-the-tests
style: pokemon
category: endocrinology
difficulty: advanced
question: "Why do the tests for cortisol excess have the shape they do, and why is imaging the wrong first step?"
tags: [cushings, cortisol, dynamic-testing, suppression, incidentaloma]
---

# Send in Arbok and watch. If Attack does not fall, something is holding it, and that is the whole test.

You cannot read a Pokémon's Attack stat off the screen. What you can do is send in **Arbok**,
whose **Intimidate** lowers every opposing battler's Attack by one stage the moment it enters
*(mechanism)*. If Attack drops, the stat was being held in the ordinary way, by the ordinary
rules, and it obeys. If **Metagross** is out with **Clear Body**, or **Torkoal** with **White
Smoke**, nothing moves at all — the ability simply does not take *(mechanism)*. You never measured
anything. You pushed, and the answer was in whether it gave.

That is the shape of the test for too much of a field condition, and there are only three shapes
available:

1. **Push it the way it should give.** Send in the Intimidate user. Obedient systems drop a stage;
  autonomous ones do not.
2. **Read the integral.** Friendship is a stored 0–255 that the games never show you, and
  **Return**'s base power is friendship × 10 ÷ 25, topping out at 102 — one figure for the whole
  run, carried over unchanged from the glycation answer *(mechanism)*.
3. **Read it at the right time of day.** Evolve an **Eevee** at high friendship and you get
  **Espeon** if it is not night and **Umbreon** if it is *(mechanism)*. Identical stored value.
  Two different outcomes. **A number without the clock is not a reading.**

And underneath all three, the house rule: **push the loop in the direction it should resist.** Too
much is tested by pushing down. Too little is tested by pushing up. One sentence, every axis.

| In the battle | What it stands for |
| --- | --- |
| **Psychic Terrain**, blocking priority moves at grounded targets | Cortisol: permission, and proportion |
| **Arbok**'s or **Salamence**'s **Intimidate**, −1 Attack on entry | The suppression test |
| **Metagross**'s **Clear Body**, **Torkoal**'s **White Smoke** | Autonomy: the push does not take |
| Setting the condition from outside and watching | The stimulation test, the other way round |
| Friendship, 0–255, stored and never displayed | The integrated total |
| **Return**'s base power — friendship × 10 ÷ 25, max 102 | The integral, read out as one figure |
| **Eevee** → **Espeon** by day, **Umbreon** at night | The same value, read at two times |
| **Reflect**, halving what lands, changing nothing sent | The binding protein |
| The **Dowsing Machine**, beeping at everything buried | Imaging: it finds what was always there |
| **Belly Drum** — bar halved, Attack straight to +6 | A signature only one cause produces |

Claims are marked *(mechanism)*, *(definitional)*, *(consensus)* or *(country-dependent)* where it
matters.

## Before any test: look at who else set the terrain

The commonest reason a field condition is up too much is that **somebody else has been setting
it** *(consensus)*. You find that by looking at the last twenty turns, not by measuring this one.
And there is a mechanic that makes the finding unmistakable once you know it: a Surge ability
entering onto its own terrain does nothing, announces nothing, and refreshes no timer, because
`TryChangeBattleTerrain` returns false when the terrain is already the one being set
*(mechanism)*.

So the picture is inverted from the one that gets taught. The condition is plainly up. Your side's
setter has not fired in twenty turns. Your reporter is quiet. Everything says "too much", and
every part of your own loop reads "too little", because the supply is from outside it.

## Who to push on, which is an arithmetic question

The tells divide sharply, and the division is the most useful thing on this page.

| Common, says almost nothing | Rare, says one thing |
| --- | --- |
| The bar drifting down | A Pokémon that cannot act at all on the turn it is asked to |
| Chip damage at end of turn | A defensive stat that has quietly fallen several stages |
| A side that feels slow | Damage landing that the matchup says should not land |
| One stat a stage below where you expected | **Belly Drum**'s +6 Attack beside a halved bar |

The left column happens in every battle for a dozen reasons. The right column happens when
something has been **taken apart**, and very little takes a side apart that way *(mechanism)*.
Push on the right column and a positive answer means something. Push on the left column and you
will get far more spurious answers than real ones, however good the push is — because a test's
behaviour in use is a property of who you point it at, not of the test *(mechanism)*.

## What the push is actually asking

```
   AN ORDINARY SIDE, FACED WITH INTIMIDATE
   ───────────────────────────────────────
   Arbok enters ──► Intimidate fires ──► every opposing battler: Attack −1
                                               │
                                               ▼
                                   the stat MOVED → ordinary rules apply

   A SIDE HOLDING IT AUTONOMOUSLY, FACED WITH THE SAME THING
   ─────────────────────────────────────────────────────────
   Arbok enters ──► Intimidate fires ──► Metagross has CLEAR BODY
                                               │
                                               ▼
                                   nothing happens at all. Not a stage.
                                   → the stat was never on the hook

   ── you did not read the stat. You asked whether the stat OBEYS ──

   AND THE SAME LOGIC BACKWARDS IS THE TEST FOR A SHORTAGE
   ───────────────────────────────────────────────────────
   suspected shortage ──► set the condition from outside ──► does anything respond?
                          a side with the ability shows it; a side without does not
```

**Clear Body**, **White Smoke** and **Full Metal Body** all prevent stat loss caused by another
battler, and **Hyper Cutter** blocks the Attack drop specifically *(mechanism)*. Autonomy is not a
number. That is why no single observed stat, however extreme, settles it, and why a stat sitting
at its ordinary value does not rule it out.

## Why the clock, and why the integral

The thing a running total cannot show you is the **shape** of the run, and the thing a single
glance cannot show you is the total. **Return** at base power 102 tells you the whole stretch went
well and nothing about this turn. The **Eevee** branch tells you that the same stored 220-or-above
— 160 from Generation VIII *(mechanism)* — sends you to two different species depending only on
whether the clock says night.

Each shape has its own failure mode, which is why you use two and care about whether they agree
*(consensus)*:

* The **push** fails when the pusher never gets to push: **Mawile** can carry **Hyper Cutter**
  instead, and in later generations several abilities block **Intimidate** outright *(mechanism)*.
* The **integral** fails for the reasons the glycation answer sets out — a **Luxury Ball**, a met
  location, a trade resetting the carrier to a flat 70 — things that move the number without
  moving the truth *(mechanism)*.
* The **clock** fails when the clock itself is wrong, which is exactly as mundane as it sounds.
* And **all three** fail against **Reflect**, which halves what lands for five turns, eight while
  the setter holds **Light Clay**, and changes nothing about the attacker *(mechanism)*. Grade the
  attacker by what the defender felt and Reflect has made you wrong without anything about the
  attacker having changed.

## Then, and only then, where it is coming from

The order is **confirm, classify, localise**, and each step asks something different
*(consensus)*:

* **Confirm** that the condition really is up and really is not obeying, with two of the three
  shapes agreeing.
* **Classify** by the reporter. **Flail** loud beside a condition that is plainly up means the
  level above is still driving it. **Flail** pinned at 20 beside the same condition means the
  setter is doing it on its own and nobody is asking *(mechanism)*.
* **Localise** last.

## Why the Dowsing Machine first is the classic error

The **Dowsing Machine** beeps at every buried item on the floor you are standing on. Walk any
route with it and you will find things — and every single one of them was there before you arrived
and has nothing to do with what you came for *(mechanism)*.

Use it before you know what you are looking for and the beep arrives with no context, and the pull
to attribute the whole situation to the thing you dug up is overwhelming. The error is not that
the machine lied. There really is an item there. The error is **attribution**: an ordinary buried
item has been promoted to an explanation by the order you did things in. Downstream, that means
digging in the wrong place, and sometimes digging up a floor that was never the problem.

Run it the other way round and the beep means something, because the reporter has already told you
what kind of thing you should be finding. **Flail** loud says the fault is at the level above, and
a find there matters. **Flail** at 20 says the setter is autonomous, and the same find at the
level above means nothing at all. Identical beep. Opposite meaning, decided entirely by what you
established first.

## Where it strains, said honestly

Two caveats, because the structure above is tidier than reality. A condition can be up **in
bursts**, with ordinary turns in between, so one round of pushes that all come back obedient does
not close the question when the rest of the battle plainly says otherwise *(consensus)*. And at
the mild end, "slightly more than it should be" and "exactly as much as this situation warrants"
are genuinely hard to separate — the push's reliability was worked out against obvious cases and
does not transfer to borderline ones *(consensus)*. The right answer to a borderline case is to
watch it over more turns, not to read the same numbers more confidently.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

Everything above is a picture of dynamic testing: why you push a loop rather than read it, why a
rhythm has to be sampled at the right point, and why the order of investigation determines what a
finding means. The picture is fair. What this diagnosis is to live through is not a battle.

Cortisol excess is typically diagnosed years after it began, and the features noticed first —
weight gain, mood change, poor sleep — are features people are routinely blamed for. Someone told
for three years that they need to try harder, who then turns out to have had an adenoma, has
usually absorbed the blame along the way. That is a harm the diagnostic process caused, and it is
worth naming as one rather than treating the delay as an interesting statistic.

The opposite harm is real too, and it comes from testing the common features in everybody: a
borderline result, then a scan, then an incidental finding, then more tests, and sometimes an
operation on a gland that was never the problem. Both harms exist and they pull against each
other, which is why **whom to test** is the serious clinical question rather than a preliminary to
it.

And a note about who is reading. Someone reading this may be in the middle of this investigation,
or may suspect they should be. If that is you: nothing above is a threshold, a protocol or a
reassurance. A result means something only in the sequence it was taken in and alongside the rest
of the picture, and that reading belongs to the team that ordered it — not to an analogy about
Intimidate.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../for-agents/SOURCES-endocrinology.md`](../../for-agents/SOURCES-endocrinology.md) for
the standing documents of this specialty. Specific to this answer:

* The specialty society guidance on diagnosing cortisol excess issued in your country, for which
  tests are recommended, in what combination, and in whom.
* Your national guidance on incidentally discovered adrenal and pituitary lesions, which governs
  what happens to a finding made out of sequence.
* **Your own laboratory's handbook**, for the assays it runs, whether a salivary assay is
  available, the collection conditions each needs and the thresholds it reports against.
* Your national formulary, for the synthetic glucocorticoid used in a suppression test and the
  interactions that alter its clearance.
* A current endocrinology textbook, for the diurnal rhythm, the catabolic actions of
  glucocorticoid and the binding globulin.

The Pokémon side is different and is sourced properly. **Intimidate**'s single-stage drop on
entry, the list of abilities that prevent stat loss, **Clear Body** on the **Metagross** line and
on the three Regis, **White Smoke** on **Torkoal**, **Hyper Cutter** beside **Intimidate** on
**Mawile**, **Flail**'s band table, **Reflect** with **Light Clay**, the **Eevee** branch on time
of day, the friendship evolution threshold of 220 falling to 160 in Generation VIII, and the fact
that a Surge ability does nothing on its own terrain were all read from the pokeemerald and
pokeemerald-expansion decompilations rather than from memory. **Return**'s formula is carried over
from the glycation answer, which sourced it the same way.

## Scope and safety

The Pokémon here is doing one job: making the logic of dynamic testing concrete — why you push a
loop instead of reading it, and why order of investigation decides meaning. It is not a clinical
reference, not a decision aid, and not about any individual's care. **No thresholds, doses,
collection protocols or test performance figures appear here on purpose** — they differ between
laboratories, countries and guideline bodies, they are revised, and a suppression test read
against the wrong threshold is worse than no test at all. Your laboratory and your local guidance
are the authority and this page is not. The specialist procedures that separate a pituitary from
an ectopic source are not described. Nothing here has had clinical review. If someone is unwell
now, contact local emergency services.

## What a Gym Leader digs into next

* Why does sending in **Arbok** tell you something no amount of watching the stat would?
* Why does **Clear Body** make the push informative rather than useless?
* Why does the same stored friendship value send an **Eevee** to two different species?
* Why does using the **Dowsing Machine** first change what the beep means?

## Where this stands, October 2026

The test logic — push against the direction the loop should give, integrate to cancel a rhythm,
sample at the right point in the clock, and only then go looking — is mechanism and does not date.
What dates on the Pokémon side is the constants and the cast: the set of abilities that block
**Intimidate** has grown across generations, the friendship evolution threshold changed in
Generation VIII, **Reflect** with **Light Clay** and **Disable** have both been retuned, and
terrains and the **Surge** abilities only exist from Generation VI and VII. Check the current
generation's data. On the clinical side everything numeric and procedural moves — first-line
tests, thresholds, assay platforms, salivary availability and the incidental-lesion guidance — so
check current local guidance and your own laboratory's handbook.
