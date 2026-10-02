---
id: "m048"
slug: the-consultation-and-premature-closure
style: pokemon
category: general-practice
difficulty: advanced
question: "Why does the opening question shape the diagnosis, and what does a hypothesis formed in the first minute actually cost?"
tags: [consultation, premature-closure, anchoring, agenda, diagnostic-error]
---

# Sweet Scent ignores your Repel, and that is the entire argument for the open question

Two ways to find out what is in a patch of grass, and they are not two speeds of the same thing.

Walk, and the engine rolls a slot, rolls a level, and *then* applies your filters: with a
**Repel** running it cancels the encounter outright if the level came out below your lead's, and
if your lead has **Keen Eye** or **Intimidate** it cancels, on a one-in-two coin flip, anything
five or more levels under your lead. Use **Sweet Scent** instead and the field routine is called
with its flag word set to zero. No rate roll, no Repel check, no ability check. One encounter,
immediately, drawn from the table exactly as the table is.

That is the difference between an opening that samples the problem and an opening that samples
your own expectations, and it is worth working out in numbers, because the cost is much larger
than it feels.

## The same grass, drawn twice

```
   EVERY NUMBER BELOW IS REAL, READ OUT OF THE CODE. Mt. Moon 1F: encounter rate 10/256,
   slot chances 51 51 39 25 25 25 13 13 11 3 out of 256 in slot order. The table, with
   the level printed in each slot:

     slot  1  Zubat  L8  (51)    slot  6  Zubat    L10 (25)
     slot  2  Zubat  L7  (51)    slot  7  Geodude  L10 (13)
     slot  3  Zubat  L9  (39)    slot  8  Paras    L8  (13)
     slot  4  Geodude L8 (25)    slot  9  Zubat    L11 (11)
     slot  5  Zubat  L6  (25)    slot 10  Clefairy L8  ( 3)   ← the Moon Stone

   WALKING, WITH A REPEL AND A LEVEL-10 LEAD. The filter cancels every slot whose level
   came out below 10, so what survives is slots 6, 7 and 9:

        survives     25 + 13 + 11  =  49 / 256  of rolls
        of which     Zubat         =  36 / 49   =  73.5 %
                     Geodude       =  13 / 49   =  26.5 %
                     Paras         =   0
                     Clefairy      =   0        ← IT IS LEVEL 8. IT CANNOT APPEAR.

        and the chance per step of meeting anything at all falls from
             10/256 = 3.91 %   to   10/256 × 49/256 = 0.75 %

   SWEET SCENT, STANDING IN THE SAME GRASS. Flag word zero: no rate roll, no Repel
   check, no ability check.

        the full table, unaltered      Zubat 202/256, Geodude 38/256,
                                       Paras 13/256, Clefairy 3/256
        cost                           one turn, and 1 PP out of 20

   A Trainer who walked that floor for a week with the Repel on would conclude, from real
   evidence, honestly gathered, that there is no Clefairy in Mt. Moon. The filter they set
   to save time is the thing that made the answer unreachable, and nothing downstream of
   it can recover what it excluded.
```

The Repel is the same object that stands in for a referral filter elsewhere in this specialty, and
for the same reason: it is a criterion applied to an already-rolled slot, which enriches what gets
through for whatever you specified and silently removes everything you did not. Used as a referral
filter that is exactly what you want. Used as an *opening question* it is the error.

## What a committed hypothesis does, in one line of code

```
   REAL MECHANICS. A Choice Band gives ×1.5 to physical damage, and the engine stores
   the FIRST move its holder selects. Afterwards:

      selecting any other move   ──►  blocked outright, it is not selectable
      a different move forced in ──►  gCurrentMove = the stored first choice
                                      the engine SUBSTITUTES your first answer for
                                      the one you just gave

      the only way out           ──►  leave the field, which spends the whole turn

   That is premature closure with the comment removed. Note which part is the error: not
   the first choice, which was probably right and came with a genuine ×1.5 attached. The
   error is that the slot is now the only slot, and the engine will keep answering with
   it while you believe you are choosing.
```

Three more real mechanics make the same point from different sides, and each has a turn count
attached, which is what makes them arguable rather than atmospheric:

* **Encore** forces repetition of the last move used — in Generation III for a random 2 to 6
  turns, in Generation IV for 3 to 7, and from Generation V for 3. It costs 5 PP and it does not
  need the target to agree. Whatever was said first is what keeps being said.
* **Taunt** removes every status move from the menu, leaving only attacking moves selectable: in
  Generation III for exactly 2 turns, in Generation IV for a random 3 to 5, and from Generation V
  for 3. That is a conversation in which only closed questions are available, and it is imposed
  rather than chosen.
* **Disable** takes the last move used away entirely. The thing most recently mentioned becomes
  the thing that cannot be mentioned again.

## And the first turn sets conditions that outlast the first turn

```
   REAL MECHANICS, in the order the engine runs them on arrival.

   something enters the field
        │
        ├── Intimidate fires HERE, before either side has selected anything, and drops
        │   the opposing Attack by one stage. The first exchange is already conditioned.
        │
        ├── Fake Out is selectable ONLY on a battler's first turn out — priority +3 from
        │   Generation V, +1 before it, 40 power. One turn, and then the option is gone
        │   from the menu for the rest of the battle.
        │
        └── Rain Dance or Sunny Day set on turn one run for 5 turns — 8 with a Damp Rock
            or a Heat Rock — so the conditions chosen in the first moments are still
            running long after the moment is over.

   Nothing in that list is recoverable later. Which is the whole claim: the opening is
   not the polite part before the real part. It is the part that constrains the rest.
```

## Why committing early is adaptive, which is why it is hard to drop

Most of the time the first slot is the right slot. On **Route 1** the table is exactly half
**Pidgey** and half **Rattata** and nothing else exists at all, so a Trainer who decides what is
coming before it arrives is right every single time and faster every single time. The **Choice
Band**'s ×1.5 is the same bargain made explicit: real power, bought with the loss of the other
three slots.

Three consequences follow, and the third is the one Trainers skip:

* **The benefit is spread over every encounter and the cost lands in a few.** From inside, the
  practice feels excellent. The floors where it fails are rare, and the failures do not announce
  themselves as failures of method.
* **The error is the stopping, not the guess.** A Trainer who forms a view in the first frame and
  keeps sampling has not made the mistake. The mistake is the stored move.
* **The commitment is partly made for you.** Once the stored move exists, the menu itself changes
  — the other three are greyed out. Nobody experiences that as a choice to confirm. They
  experience it as the obvious thing to press.

## What actually reduces the cost

* **A second pass, deliberately.** Sweet Scent costs one turn and 1 PP, and it is the only
  instrument in the game that draws the real table with every filter switched off. It is cheap and
  it is almost never used, because walking feels like progress.
* **Switch out while the stored move is still cheap.** Leaving the field clears the lock, and it
  costs one turn. Later it costs the battle.
* **Say the alternative out loud.** Naming the slot you do not believe in converts a private
  impression into a thing somebody can argue with — including you, one turn later.
* **Check the filters you forgot were running.** A Repel has a step counter and the game tells you
  when it expires; Keen Eye and Intimidate do not announce themselves at all, and a Trainer who
  does not know what is in their lead slot does not know what is being culled from their evidence.
* **And the structural fix is the net.** An opening pass does not have to be right when the plan
  behind it has a named trigger and a route back — the **Max Repel** with 250 counted steps and
  the **Escape Rope** in a known bag slot. Getting the first answer wrong is survivable by design,
  which is exactly what takes the pressure off getting it right.

## Where the metaphor stops

Being interrupted while describing something frightening is not a minor procedural failure. It
tells someone that what they are saying is not what the room is for, and people do not generally
try twice. A great many consultations end with the person having not said the thing, and almost
none of those are recorded as anything at all.

The distribution of that harm is not even. The people most likely to be interrupted, and least
likely to re-raise an item once it is passed over, are those whose speech the system finds
hardest to accommodate: anyone working through an interpreter, anyone with a communication
disability, anyone in distress, anyone who has previously not been believed, and anyone who has
learned that the appointment is short and they should not take up space in it. A consultation
style built around a confident, fluent, available person is not a consultation style for them,
and the fix is structural rather than attitudinal — time, interpreters booked properly, and not
making the person compete with the clock.

And the part that is not about diagnosis. For the clinician the consultation is one of many; for
the person it is an event they will remember and repeat to their family. Both of those are true
at once, and the second one is not a sentimental addition to the first. How the opening went is
most of what determines whether the person comes back, which means it is also a safety mechanism.

## What a Gym Leader is listening for

Whether the Trainer treats the opening as the draw rather than as courtesy, and can say what the
Repel removed. Then the Clefairy line, out loud: level 8, lead level 10, filter on, zero. Then the
distinction between committing early and stopping early, with the stored move as the example of
the second. Then the turn counts — Encore, Taunt, the weather — because a claim with a number on
it can be checked and a claim about atmosphere cannot. Then the honest benefit of the ×1.5. Then
the hard one: a battle lost without a single incorrect inference in it, and exactly which press of
the button did the damage.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The consultation-skills and communication sections of the curriculum and assessment guidance
  issued by the reader's own college or training body for general practice, which is the document
  that defines what is formally expected and marked.
* Any of the published consultation models taught in the reader's own training programme, read in
  its primary form rather than in summary, for how each handles agenda-setting.
* The primary literature on agenda-setting and on the length of the uninterrupted opening
  statement — several groups have published on this, their estimates differ, and the differences
  are informative rather than embarrassing.
* Any systematic review of diagnostic error in primary care, in the patient-safety literature, for
  how often premature closure appears among the contributory factors and how it was identified.
* The literature on cognitive bias and debiasing in clinical reasoning, including the papers
  reporting that debiasing interventions are harder to demonstrate than to describe.
* The reader's own organisation's interpreter and reasonable-adjustment policy, which determines
  what is actually achievable in the consultations where this matters most.

The Pokémon figures are a separate matter and are not covered by the line above. The ten slot
chances, the Mt. Moon 1F and Route 1 encounter tables with their printed levels, the encounter
rate of 10/256, the order in which the engine rolls a slot and a level before applying a filter,
the Repel cancelling an encounter whose level is below the lead's, the one-in-two Keen Eye and
Intimidate cull of anything five or more levels under the lead, Sweet Scent calling the field
routine with its flag word set to zero and its 20 PP, the Choice Band's ×1.5 and the engine
substituting the stored first move, the generation-by-generation turn counts for Encore and Taunt,
Disable removing the last move used, Intimidate firing on entry for one stage, Fake Out being
selectable only on a battler's first turn out with priority +3 from Generation V, weather lasting
5 turns or 8 with the matching rock, and the Max Repel's 250 steps, were all read directly from
the pret and rh-hideout decompilation projects, which this environment can reach.

## Scope and safety

This is revision material about clinical reasoning and consultation structure, written for someone
already training in or qualified for the field. It is not a clinical reference, not a decision
aid, and not for use in making a decision about any person's care. No published average for the
length of an opening statement, and no diagnostic-error rate, is reproduced here, because the
figures differ between studies and settings and the principle does not depend on any of them. The
encounter and battle numbers are real, they stand in for a mechanism, and no clinical figure
should be read out of them. If someone is unwell right now, the relevant action is to contact
local urgent care or the local emergency number, not to read this.

## Where this stands, October 2026

The reasoning here — that the opening determines what is sampled, and that premature closure is a
failure of stopping rather than of hypothesis generation — is long settled and is not expected to
move. What is moving is the context. Remote, telephone and asynchronous consulting change the
opening in ways that are only partly understood, and text-based first contact in particular
changes who is able to state an agenda at all. Automated history-taking and summarisation tools
are being introduced into first contact in several systems; their effect on what gets sampled and
on whose words survive into the record is an open question and should be treated as one. The
Pokémon mechanics are generation-pinned where they differ and are otherwise stable because the
games are finished. Take local consultation-model teaching and local access arrangements from
current sources rather than from here, as of October 2026.
