---
id: "214"
slug: fine-grained-and-shared-experts
style: pokemon
category: open-weights
difficulty: advanced
question: "Why does DeepSeek use hundreds of small experts plus a shared one, and balance them without an auxiliary loss?"
tags: [mixture-of-experts, routing, load-balancing, deepseekmoe, deepseek]
---

# Narrow specialists multiply your answers. The centre stops them repeating each other.

In a Triple Battle the three slots are not equal. The one in the **centre can reach any of the
three opponents**; the two on the ends can only reach what is next to them. That is not a
metaphor, it is the rule, and it is exactly the shape of the thing being described.

Two moves, and they only work together. First, **go narrow**: rather than three broad Pokémon
that each cover a lot of ground, register hundreds that each cover almost nothing — a
**Pachirisu** that exists to answer one **Gyarados**, a **Ferrothorn** that exists to eat one
**Dragon Pulse** — and send out the same number of them. Second, **hold the middle**: one
Pokémon stands centre every single exchange, so whatever every fight needs is learned once
instead of separately by all three hundred.

## Why narrow beats broad at the same cost

```
   same bench weight, same slots filled, different grain

   broad    16 specialists, take 2     distinct line-ups =       120
   narrow  256 specialists, take 8     distinct line-ups ≈ 4.1e14
                                                             ▲
             far more answers, without one extra ────────────┘
             Pokémon on the field

   ┌─ one exchange ──────────────────────────────────────────────────────┐
   │                                                                      │
   │  threat ─► type chart ─► score ─► score + nudge ─► six called out    │
   │                │                       ▲              │              │
   │                │                       │              ▼              │
   │                │             the Rage Powder:    how hard each one   │
   │                │             changes WHO gets    hits is the plain   │
   │                │             called, nothing     score, never the    │
   │                │             about the damage    nudged one          │
   │                │                                      │              │
   │  threat ────────────► the centre slot, every exchange ─┴──► outcome  │
   └──────────────────────────────────────────────────────────────────────┘

     called too often  →  the powder thins  →  called less next time
     never called      →  the powder thickens →  called more next time
```

The count is the honest reason to go narrow. Cutting each specialist thinner and calling more of
them puts nothing extra on the field and multiplies the number of distinct answers you can give.
Each one then covers less, so it can cover it harder, and less of what it knows is already known
by the **Ferrothorn** beside it.

The centre slot exists because that overlap is otherwise unavoidable. Type advantage, **Stealth
Rock** on the opponent's side, knowing when to **Protect** — every exchange needs those, so
without a centre every one of the three hundred carries its own copy and you pay for the same
lesson three hundred times. Putting it in the middle frees the ends to be *unlike each other*,
which is the only reason to have them.

## Why the punishment had to go

Leave a roster alone and it collapses to a favourite: **Garchomp** wins early, gets the
experience, gets better, gets sent out more. The old fix is a **punishment** — dock yourself for
leaning on Garchomp. It works, and it is also a second goal pulling against the first, because
you are telling yourself to send out **Luvdisc** and its 330 total against something Garchomp and
its 600 would have beaten.

**Rage Powder** is the better instrument. **Amoonguss** does not weaken anything. It changes who
gets targeted this turn, and nothing else:

* the powder is added to **who gets picked**, and only to that;
* **how hard the picked one hits** is worked out as if the powder were not there;
* used too often and it thins; never used and it thickens back up.

And it is a nudge, not a law — **Grass** types ignore powder outright, and anything holding
**Safety Goggles** walks straight through it. That is the point: it steers the choice without
ever touching the damage roll, and it never becomes the thing you are optimising for. A very
light dose of the old punishment stays on top, purely to stop one battle going completely
one-sided.

## What it costs you

* **Traffic scales with how many you call, not how big they are.** Eight names per exchange means
  eight round trips. Keep half the bench in **Pokémon HOME** and the distance, not the Pokémon,
  sets your floor.
* **Narrower means scrappier.** Hundreds of one-answer Pokémon means hundreds of small, awkward
  calls, and the whole thing runs badly unless you group the threats by who answers them.
* **Even on the practice field is not even at the League.** The powder is a training-ground
  instrument. Walk into a circuit that is all **Steelix** and **Aggron** and your one
  **Machamp** is carrying everything while three hundred others sit in the box.
* **The rarely-called ones are the brittle ones.** They battle least, so they train worst — and
  they are the ones you registered for the strange matchups (question 207).

## What a Gym Leader is listening for

The count, said out loud: more and narrower multiplies the answers without putting anything extra
on the field. Then that the centre slot is about *not repeating yourself*, not about being
stronger. On balance, the sentence that matters is "the powder changes who is targeted, never the
damage" — say why that distinction is the entire trick and you have it. The strongest answers
bring up the circuit that is all Steel types without being asked, because no practice log will
show you that one.

## Where this stands, September 2026

The older roster — one in the centre, 256 on the bench, eight called — comes from published
rulebooks and has not moved. The newer one, 384 on the bench and six called, is **second-hand
only**: the sites holding the report and the cards are blocked from where this was written.
Bench counts are exactly the sort of number that gets garbled in retelling, so check them against
the card itself before you build a team around them.
