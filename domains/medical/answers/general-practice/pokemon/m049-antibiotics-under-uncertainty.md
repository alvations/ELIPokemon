---
id: "m049"
slug: antibiotics-under-uncertainty
style: pokemon
category: general-practice
difficulty: advanced
question: "Why do the individual and the population optimum genuinely differ when an antibiotic is considered under diagnostic uncertainty?"
tags: [antibiotics, stewardship, resistance, externality, uncertainty]
---

# The Master Ball always succeeds, and there is one

The capture routine in **Red** and **Blue** carries a comment above the first instruction that
settles the individual case on its own. The routine generates a random byte and then runs a chain
of comparisons — a **Great Ball** keeps re-rolling until that byte comes out at 200 or below, an
**Ultra Ball** or a **Safari Ball** until it comes out at 150 or below, a **Poké Ball** accepts
anything — and only then does it reach the comparison against the species' catch rate.

The **Master Ball** does none of that. It jumps straight past every comparison to the captured
branch. No roll, no catch rate, no HP term, no status modifier. For the Pokémon in front of you,
right now, it is not the best option available; it is the only option with no failure mode at all.

And there is one of them in the game. One, handed over on the eleventh floor of **Silph Co.**
Throw it at the **Zubat** that just walked out of **Mt. Moon** — catch rate 255, the highest value
the field can hold, catchable with a ¥200 Poké Ball on a good roll — and the throw works
perfectly. The decision was individually optimal and it was the worst move in the whole game.

That is the structure, and it is worth being precise that nothing in it is a mistake. Both
calculations are correct. They are calculations over different things.

## You cannot tell from the rustle

The two optima would not conflict if you could see what was coming. You cannot. The slot is rolled
out of the table before the battle screen is drawn, and in an ordinary patch of grass the table
is overwhelmingly the common thing: on Mt. Moon 1F, Zubat holds six of the ten slots for 202/256
and **Clefairy** holds one for 3/256, so sixty-seven Zubat come out for every Clefairy. The
decision has to be made under exactly the uncertainty that makes reserving anything difficult.

## The shared counter, with the arithmetic done

The **Safari Zone** is the clearest statement of the problem the games contain, because it puts a
single visible budget on a whole excursion.

```
   EVERY NUMBER BELOW IS REAL, READ OUT OF THE CODE.

   entry fee                    ¥500
   Safari Balls issued          30
   step counter set to          502   (the gate worker says 500; the walk in spends two)
   centre area encounter rate   30/256 per eligible step — the highest in Kanto
   slot chances                 51 51 39 25 25 25 13 13 11 3 out of 256, in slot order

   the centre area's table, with each species' catch rate beside it:

     slot  /256   species (Red)      level   catch rate
     ────  ────   ────────────────   ─────   ──────────
       1     51   Nidoran♂             22       235
       2     51   Rhyhorn              25       120
       3     39   Venonat              22       190
       4     25   Exeggcute            24        90
       5     25   Nidorino             31       120
       6     25   Exeggcute            25        90
       7     13   Nidorina             31       120
       8     13   Parasect             30        75
       9     11   Scyther              23        45
      10      3   CHANSEY              23        30   ← rarest slot AND hardest catch

   WHAT THE BUDGET BUYS

      expected encounters in 502 steps   502 × 30/256   =  58.8
      balls available                                      30
      expected Chansey in the whole walk  58.8 × 3/256   =   0.69

   THROW AT EVERYTHING YOU MEET
      balls run out at encounter 30, which lands around step 256 — HALF THE WALK
      expected Chansey among the first 30 encounters   30 × 3/256  =  0.35

      every throw was locally sensible          ─  a free catch, in front of you
      the visit's yield of the thing it was for ▼  halved, 0.69 → 0.35
      and no single throw can be named as the one that did it

   RESERVE BY RULE
      throw only at slot 10            expected balls spent  ≈ 0.7 of 30
      and the walk completes, so the full 58.8 encounters are actually sampled
```

The line that matters is the last one in the middle block. **No individual throw can be labelled
as the wasteful one.** Every Nidoran♂ caught really was a Nidoran♂; the throw worked; the catch is
correct. The waste exists only when you count the whole visit, which is why it is so hard to
argue about one throw at a time: the honest statement is about a rate, and what is in front of you
is not a rate. This is the same shape as over-sweeping a floor, and recognising the shape is worth
more than memorising either case.

## The replenishment is capped, and the empty state costs you

```
   REAL NUMBERS. PP falls by one per use. What puts it back:

      Ether          +10 PP to one move
      Max Ether      that move back to full
      PP Up          raises a move's MAXIMUM by (base PP ÷ 5), capped at 7 per use,
                     and the use count lives in two bits — so THREE USES, EVER

      base PP   ÷5   per PP Up   maximum after three
      ───────   ──   ─────────   ───────────────────
      Hydro Pump  5    1    +1          8
      Surf       15    3    +3         24
      Tackle     35    7    +7         56
      Splash     40    8    +7 (cap)   61

   And the empty state. From Generation II onward Struggle itself has 1 PP, carries 50
   power, is used when nothing else can be, and hurts the user every time.

      the pool falls      one use at a time, from any direction
      the pool rises      in capped increments, three times, and never again
      the floor           is not zero. It is a move that damages whoever uses it.
```

That asymmetry is the whole reason the shared resource behaves like a stock rather than a flow.
Nothing about spending is hard; everything about putting it back is bounded.

## What narrows the gap, in order of how much it buys

1. **Anything that tells you which slot came up.** This is the only lever that improves both
   ledgers at once, which is why it dominates. Everything else trades one cost for another.
2. **Match the ball to the catch rate instead of reaching for the scarcest one.** An Ultra Ball
   caps the random byte at 150 rather than 255; against Chansey's catch rate of 30 that is a real
   improvement, and against Zubat's 255 it is ¥1 000 spent for nothing a Poké Ball would not have
   done. The right instrument is the cheapest one that clears the job.
3. **Make the throw conditional.** Decide the rule at the gate, before the first rustle, and write
   it as *which slots* rather than *how many balls*. A rule about slots survives contact with the
   grass; a quota does not.
4. **Instruments above the individual throw.** The Zone issues 30 and no more, replaces the bag so
   no Master Ball can be smuggled in, and ends the visit when the counter runs out. None of that
   asks the Trainer to weigh anything. It removes the choice from where it could not be weighed.

## The counterweight, stated as strongly as the argument

A Trainer who walks out of the Safari Zone with 30 unused balls having met a Chansey and not
thrown has also failed, and has paid ¥500 to do it. The argument above is not for throwing less.
It is for a rule about *which* encounters — because a quota pushes the loss onto whichever
encounter happens to come after the quota is spent, and which slot comes up last is not something
anybody chose.

And the counter is local. The centre area runs at 30/256 and Mt. Moon runs at 10/256; Clefairy is
3/256 on the first floor, 11/256 on the second and 16/256 on the third. A rule written for one
floor is not a rule for another, and a Trainer who carries one across has read neither table.

## Where the metaphor stops

Two people stand behind this decision and only one of them is in the room. The person present has
a reasonable question — they feel unwell, there is a treatment, and they are being told the
reasons for not using it involve people they will never meet. Treating that as unreasonable, or as
something to be managed with a leaflet, is both unkind and ineffective. The honest version of the
conversation includes the part that is genuinely uncomfortable: that the clinician is weighing a
cost the person is not being asked to bear, and that this is why the decision does not feel like
it is entirely about them.

The other person is real too. A resistant infection in someone who has run out of options is not
an abstraction, and it arrives at the end of a chain in which every individual link was
defensible. Nobody in that chain did anything they could be blamed for, which is precisely why
the failure has to be designed against rather than moralised about.

And the part that is easy to leave out of a stewardship argument. The person who was not treated,
followed the advice, got worse, and came back — or did not come back — has been harmed by a
correct decision. Holding that alongside the population case, without softening either, is the
actual skill. It is also why the conversation at the point of not prescribing has to leave the
door genuinely open rather than closing it politely.

## What a Gym Leader is listening for

Whether the Trainer can state why the two sums disagree without being told, rather than asserting
that Master Balls are precious. Then the attribution point: that no throw can be named as the
wasteful one, and what that implies about relying on judgement in the moment. Then the budget
arithmetic — 58.8 expected encounters against 30 balls, and what throwing as you go does to 0.69.
Then the replenishment table, and why three PP Ups is the whole story. Then the counterweight,
offered unprompted. Then the hard one: how the rule should differ between a Trainer who can pay
another ¥500 and walk back in, and one who cannot.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The reader's national antimicrobial prescribing guidance and local microbiology formulary, which
  together are the only authority on agent, spectrum and duration for any specific condition, and
  which differ substantially between countries and between regions (**country-dependent**).
* The World Health Organization's published global action plan on antimicrobial resistance, and
  its classification of antibiotics into access, watch and reserve groups, for the
  population-level framing and the reserved-agent concept.
* The reader's own country's national action plan or surveillance report on antimicrobial
  resistance, which carries the local resistance rates that determine where the local balance
  point sits (**country-dependent**).
* Any systematic review of delayed or back-up antibiotic prescribing in primary care, for the
  evidence on symptom outcomes and on reconsultation.
* Any systematic review of audit-and-feedback or of behavioural interventions on antibiotic
  prescribing, for how much the population-level instruments actually move prescribing and for how
  long the effect lasts.
* The published literature on short-course versus standard-course duration for the specific
  infection in question, which is where the duration argument is settled or still contested.

The Pokémon figures are a separate matter and are not covered by the line above. The capture
routine's unconditional branch for the Master Ball, the re-roll ceilings of 200 for a Great Ball
and 150 for an Ultra or Safari Ball, the Poké Ball and Ultra Ball prices, the single Master Ball
from Silph Co., the Safari Zone's ¥500 fee, its 30 Safari Balls and its step counter being set to
502, the centre area's 30/256 rate and its full ten-slot table with levels, the catch rates of
Chansey, Scyther, Parasect, Exeggcute, Nidoran♂, Nidorino, Nidorina, Rhyhorn, Venonat and Zubat,
the Mt. Moon Clefairy slot chances on all three floors, the ten slot chances, Ether restoring 10
PP, PP Up adding base PP ÷ 5 capped at 7 and being limited to three uses by a two-bit counter, the
base PP of Hydro Pump, Surf, Tackle and Splash, and Struggle having 1 PP and 50 power from
Generation II onward and damaging its user, were all read directly from the pret and rh-hideout
decompilation projects, which this environment can reach.

## Scope and safety

This is revision material about the structure of a prescribing decision, written for someone
already training in or qualified for the field. It is not a clinical reference, not a decision
aid, and nothing here should inform what any individual is given or not given — that belongs with
the prescriber who has examined them and with local microbiology guidance. No antibiotic, class,
dose, duration, spectrum, scoring rule, prevalence or resistance rate is named here on purpose,
because all of them are local, several are contested, and all are revised. The catch rates and
budgets above are real and stand in for a mechanism; none of them is a clinical probability and no
clinical figure should be read out of them. The local formulary and the local antimicrobial
guidance are the authority and must be checked before anything reaches a patient. If someone is
unwell right now, the relevant action is to contact local urgent care or the local emergency
number, not to read this.

## Where this stands, October 2026

The structural claim — that the individual and population optima diverge because the benefit is
private and part of the cost is shared and unattributable — is settled and will not move. What
moves continuously is everything operational: resistance rates, which agents are classified as
reserved, recommended durations for specific infections, and which near-patient tests are
available and funded in primary care. Short-course regimens have displaced longer ones in several
indications over the last decade and that process is ongoing in both directions. Near-patient
testing and host-response markers at first contact are the area where the lever that improves both
ledgers would come from, and the evidence on them is arriving rather than settled. The Red and
Blue numbers are stable because the games are finished. Take agents, durations and local
resistance data from current local guidance rather than from here, as of October 2026.
