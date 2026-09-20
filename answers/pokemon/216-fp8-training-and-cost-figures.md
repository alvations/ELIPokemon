---
id: "216"
slug: fp8-training-and-cost-figures
style: pokemon
category: open-weights
difficulty: intermediate
question: "A lab says it trained its model in FP8 for $5.576M. How do you read that figure?"
tags: [fp8, mixed-precision, training-cost, quantisation, deepseek]
---

# Four Effort Values buy one point. "I did it in 26 battles" buys nothing at all.

Two claims get made about a raised Pokémon and they are true in completely different ways.

The first is that **every four Effort Values buy exactly one point of a stat at level 100**, and
that 252 is the ceiling in any one stat with 510 across all six. That is a rule. You can go and
check it on your own **Machop** this afternoon.

The second is "I maxed his Attack in twenty-six battles." That is a receipt for the last leg of
a journey, quoted at an assumed exchange rate, with everything that went wrong left off.

## What working coarsely actually involves

You do not simply round everything off. A stat kept only to the nearest four points, with
everything else rounded the same way, comes out wrong. The real formula is three separate
protections:

```
   ┌─ what is kept coarse ───────┐   ┌─ what deliberately is NOT ───────────┐
   │  the EV contribution — one  │   │  HP, which has its own formula        │
   │  point per four, floored    │   │  the Nature multiplier, ×1.1 or ×0.9  │
   │  the running total you see  │   │  the level term                       │
   │  on the summary screen      │   │  the base stat itself                 │
   └─────────────────────────────┘   └───────────────────────────────────────┘

   keep the counting fine          multiply at the very end
   ┌────────────────────────┐      ┌───────────────────────────────────────┐
   │ every defeated Pidgey  │      │ Nature is applied LAST, to the whole  │
   │ is counted as itself,  │      │ number. Apply the ×1.1 early, to the  │
   │ one EV at a time, in   │      │ rounded pieces, and an Adamant        │
   │ its own stat — never   │      │ Machop ends up short. Round small     │
   │ rounded on the way in  │      │ amounts often and you lose the        │
   └────────────────────────┘      │ points you were counting for.         │
                                   └───────────────────────────────────────┘

   Done properly, the coarse version lands on the same stat the careful
   version would have given you, every time.
```

The lesson is general: **round the bulk, keep the counting and the fragile edges exact.** Every
training method that works looks like this, and every one that does not has either lost the
one-at-a-time counting or moved the Nature to the wrong end.

## How to read the receipt

```
   ┌──────────────── INSIDE "twenty-six battles" ────────────┐
   │  the battles themselves, with a Macho Brace held        │
   │  and Pokérus already caught — both doubling the         │
   │  haul, so four times the plain rate                     │
   │  a Power item pinning every point to one stat           │
   └─────────────────────────────────────────────────────────┘
   ┌──────────────── OUTSIDE it, every time ─────────────────┐
   │  the eggs · the Destiny Knot · the Everstone for the    │
   │  Nature · the discarded hatchlings · the Bottle Caps ·  │
   │  the Heart Scale at the Move Reminder · the hours at    │
   │  the Day Care · everything after the last battle        │
   └─────────────────────────────────────────────────────────┘
        ▲
        └ ask any serious breeder what the Pokémon really cost
          and the answer is in hundreds of eggs. That is not a
          contradiction of "twenty-six battles" — it is a
          different number, and quoting the small one as the
          price of a competitive Machop is the trick.
```

Four things to ask about any such receipt:

1. **Is it only the last leg?** Nearly always, and nearly always nobody says so.
2. **Was the rate real or assumed?** A **Macho Brace** doubles the haul and **halves Speed** while
   held. **Pokérus** doubles it again. Twenty-six battles at four times the rate is not
   twenty-six battles.
3. **Against what?** A **Chansey** hands over two points in one stat; a **Weedle** hands over
   one. The count does not travel to a different route unchanged.
4. **Does the arithmetic close?** 252 EVs at four per point is 63 stat points. If the summary
   screen does not move by roughly that, the claim is about something else.

And the one that matters most: **you cannot repeat it.** The battles are public. The eggs the
Trainer threw away are not.

## The version of this that is pure theatre

**Hyper Training** is the sharpest case. Hand over a **Bottle Cap** and the judge will tell you
the stat is "Best" — the top of the scale, 31. The stored value underneath **never moved**. Breed
that Pokémon and it passes on the old number, not the one on the screen. A **Gold Bottle Cap**
does it to all six at once.

Nothing is being faked: the Pokémon really does hit harder. But the readout and the underlying
value have come apart, and if you were reading the screen to decide what to breed from, you were
reading the wrong thing. Any claimed number about how a Pokémon was raised deserves exactly that
question — is this the value, or the display?

## What a Gym Leader is listening for

That you separate the rule from the receipt without being asked, and can say what makes coarse
training work — counting one at a time, multiplying at the end — rather than "he rounds it off".
On the receipt, the tell is whether you ask what it leaves out before you repeat it. The strongest
answers do the sum out loud: 252, divided by four, is 63 points, and here is what the screen
should say.

## Where this stands, September 2026

The EV rules and the Hyper Training behaviour come from published rulebooks and have not moved in
years. The newer claims — a coarser scheme again, a different training method, more than thirty
trillion battles' worth of experience — are **second-hand**: the sites holding the report and the
cards are blocked from where this was written, and no battle count or price for the newest one
turned up anywhere reachable. A rival Trainer's September claim to have matched it for a fraction
of the cost appears in coverage with two different multipliers, which tells you how carefully any
of it was copied. Treat it as an advertisement until someone else raises the Pokémon. The four
questions outlast every generation.
