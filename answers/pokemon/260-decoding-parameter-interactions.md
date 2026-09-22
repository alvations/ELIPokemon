---
id: "260"
slug: decoding-parameter-interactions
style: pokemon
category: optimization
difficulty: intermediate
question: "Walk me through temperature, top-k, top-p, min-p and the repetition penalties. Which of them interact badly, and why is a 'creative' preset not one dial?"
tags: [sampling, temperature, min-p, repetition-penalty, decoding]
---

# The encounter table is the distribution

Every patch of **Tall Grass**, every fishing spot and every surf tile in the game has a table
behind it: a list of species, each holding a share of the encounters, and the shares add to a
hundred. **Route 1** in Red and Blue has exactly two entries — **Pidgey** and **Rattata** — and
Pidgey is the commoner of the two. **Mt. Moon** is mostly **Zubat** and **Geodude** with
**Clefairy** as the rare row. **Viridian Forest** is **Caterpie**, **Weedle** and **Metapod**,
and somewhere down at the bottom of that table sits **Pikachu**. Those are probability
distributions you can actually look at, and every generation since has published more of them:
**Hoothoot** at night, **Ledyba** in the morning, different tables on the same tile.

Question 034 explains what each dial is. This one is about what they do to each other, and the
frame that makes it tractable is that they are three different operations, not five notches on one
knob:

1. **What you carry in your bag.** **Repel**, a Lure, **Safari Zone** Bait and Rocks. These change
   what you meet without changing what lives there.
2. **The shape of the table.** The shares themselves, stretched or squeezed.
3. **Which rows you will accept.** A cut across the table: the top few, the top ninety percent, or
   everything within reach of the commonest row.

The order they apply in is not a preference. It is written into the game.

```
  the table ─► bag effects: Repel, Lure, Bait, Rock        (before anything is reshaped)
            ─► rules of the zone: what is forbidden here
            ─► [ only if you are actually rolling ] ─────────────────────────┐
                 shape       stretch or squeeze every share                  │
                 entropy     take rows until the surprise budget is spent    │
                 top-k       the k commonest rows                            │
                 top-p       rows until the shares total 90                  │
                 min-p       every row at least a fifth as common as the top │
                 typical     rows whose rarity is nearest the route's average│
            ────────────────────────────────────────────────────────────────┘
            ─► you meet one

  each cut is laid over the last. Whatever survives all of them is re-totalled to 100,
  and that is the grass you are actually walking in.
```

## What each one does to the table

**Shape.** Squeeze the shares toward the top row and **Pidgey** takes almost everything; stretch
them and the 1% row climbs. What it never does is **reorder**: the rarest row is still the rarest
row, it is just no longer 1%. Nothing in your bag squeezes a table this way while leaving its
order untouched, and that is exactly the point — this is the one dial that edits the table rather
than filtering it.

**The k commonest rows.** A fixed count, blind to the route. Keep three in **Mt. Moon** and you
keep **Zubat** and **Geodude** and throw **Clefairy** away; keep three on **Route 1** and you have
kept a row that does not exist. Three is three whether the table has two rows or twelve.

**Rows until the shares total 90.** This one widens in **Viridian Forest**, where **Caterpie**,
**Weedle** and **Metapod** have to be counted before you are anywhere near ninety, and narrows to
almost nothing on **Route 1**. That is exactly what a fixed count cannot do — and note what it
costs either way: **Pikachu** is under the line in both.

**Every row at least a fifth as common as the top row.** This is the **Repel** trick, exactly.
Repel blocks any wild Pokémon whose level is below your lead's, so the bar is not a fixed number
and not a running total — **it is set by whoever is at the front of your party**. Change the
leader and the bar moves without a single row of the table changing. And because the bar is read
*after* the shares are reshaped, stretching the table lifts the small rows relative to the top row
and quietly lets more through. Reshaping moves this bar twice.

**Rows whose rarity is nearest the route's average.** The odd one, and the reason "the top
something" is a bad way to think about all of them. It is not a cut from the top: a row that is
*far less surprising* than the route's average is as atypical as a row that is far more
surprising, so this rule can throw out **Pidgey** itself, and **Zubat** with it. If you were
picturing another nucleus, you had the wrong shape in mind.

**Bait and Rocks are two different things wearing one name.** In the **Safari Zone** — whose table
runs from **Nidoran** and **Exeggcute** up through **Scyther** and **Pinsir** to **Chansey** and
**Tauros** — you get thirty **Safari Balls** and five hundred steps, and two ways to interfere.
A Rock makes the
Pokémon easier to catch **and** likelier to flee. Bait makes it stay **and** harder to catch. Both
are called "throwing something", both buy one property and pay in another, and the number that
works for one is meaningless for the other. Do not port it across.

## The interactions that bite

* **The Master Ball ignores every one of them.** It never fails. Every catch modifier you stacked
  so carefully does nothing at all, and the game never warns you. A config that sets a temperature
  and then decodes greedily is a Master Ball: the settings are in the bag and no roll happens.
* **Reshaping the table reweights the Rock.** The Rock is thrown against the raw table and the
  shares are stretched afterwards, so the same Rock is worth less on a flattened table and more on
  a sharpened one. Tune the shape after the Rock and you have untuned the Rock.
* **Repel reads the lead you walked in with.** The bar comes from your own party, not the route —
  so the same item behaves differently depending on what you brought, and a long party history
  makes it stronger. Penalties count the prompt by default for exactly this reason.
* **On a two-row route, banning repeats bans walking.** **Route 1** has **Pidgey** and **Rattata**
  and nothing else. Forbid meeting the same species twice and you cannot cross it. That is what a
  repetition penalty does to structured output, where the same brace and the same key must come
  back again and again — use a grammar (question 262) and leave the penalties alone.
* **Three cuts stacked become one row.** Top-three, top-ninety-percent and a fifth-of-the-top all
  laid over a lopsided table leave **Pidgey**, every time, and only a floor rule stops the table
  from emptying entirely.
* **The rules have been rewritten between generations.** The same items in the same bag do not
  behave identically in two different games. Pin the game before you pin the numbers.

## Why "creative" is not one dial

Ask any shiny hunter. The base odds are 1 in 4,096 in the modern games and were 1 in 8,192 before
that, and there are at least three separate ways to move them, which are **not** the same knob:

| What it changes | The real mechanism | What you get if that is all you do |
| --- | --- | --- |
| Which rows are eligible at all | the cuts across the table | rare rows that do not belong on this route |
| How flat the shares are | the shape of the table | a different **Pidgey**, not a different species |
| Pressure away from what you met already | Bait, Rocks, **Repel** | churn: new names, same walk |

The **Masuda Method** (leaving a parent from a foreign-language game in the **Day Care**), the
**Shiny Charm** from a completed **Pokédex**, and a **PokéRadar** chain in **Sinnoh**'s grass are
three entirely different mechanisms that people
discuss as one number. Decoding presets are the same mistake. And none of the three touches what
people usually mean by creative — the *plan* — which lives in what you asked for, in walking the
route several times and choosing, or in giving it more turns to think.

**How to tune.** Move one thing, hold the rest, and judge on a real outcome instead of three
encounters. Prefer one cut, not three.

## What a Gym Leader is listening for

Whether you know which of these edits the table and which merely filters it — and whether you
noticed that the bar the **Repel** sets moves every time the table is reshaped underneath it.

## Where this stands, September 2026

The pipeline order, the sign-dependent penalty, the silent skip when nothing is being rolled, the
bar being read after the reshape, and the entropy-budget cut are all **primary**: read straight
out of the current serving sources during this write-up. Everything about other engines is
coverage — check the order in the one you actually battle on. The arithmetic behind the table will
outlive every default here.
