---
id: "222"
slug: open-weight-licence-patchwork
style: pokemon
category: open-weights
difficulty: advanced
question: "Two checkpoints from the same Qwen release carry different licences. How does that change what you are allowed to build?"
tags: [qwen, licensing, open-weights, compliance, procurement]
---

# Your Sceptile always listens. The traded Rayquaza has a ceiling.

The **Sceptile** you raised from a **Treecko** carries your **Original Trainer** name and your
**ID No.**, and it obeys at every level up to the cap of 100. Base stat total 530, and every point
of it is yours.

The **Rayquaza** somebody traded you is a **680**. It is enormously stronger and it comes with a
ceiling, because the games treat whose name is on it as load-bearing. A traded Pokémon obeys only
up to a level set by how many Badges you hold: **Roxanne**'s Stone Badge takes it to 20,
**Brawly**'s Knuckle Badge to 30, **Wattson**'s Dynamo Badge to 40, **Flannery**'s Heat Badge to
50, **Winona**'s Feather Badge to 70, and the eighth lifts the ceiling entirely. Under the
ceiling it is indistinguishable from one you raised. Over it, you call for **Dragon Claw** and it
uses something else, or turns round and takes a nap.

`Qwen3.8-2.4T-A95B` went out on **2026-08-12**. `Qwen3.8-27B` went out on **2026-08-14**. Same
family, same launch, same team. The 27B's card says **Apache 2.0** — that is your Sceptile. The
2.4T's card says `license: other`, and the slip in the **Poké Ball** is titled **Qwen3.8-Max
License** — that is the Rayquaza.

## What is written on the slip

The grant is generous. In its own words you may *"use, copy, modify, merge, publish, distribute,
sublicense, sell, deploy, host, fine-tune, and create derivative works from"* it. Then two
ceilings.

```
   ┌─ CEILING 1 — its Trainer's name stays on the summary screen ─────────┐
   │  If it is used for a commercial product or service with              │
   │        > 100,000,000  monthly active users     OR                    │
   │        > US$ 20,000,000  monthly revenue                             │
   │  the model's name must be PROMINENTLY DISPLAYED on that product.     │
   └──────────────────────────────────────────────────────────────────────┘

   ┌─ CEILING 2 — the eighth Badge is not yours to award ─────────────────┐
   │  If you or your affiliates run a                                     │
   │        "Model as a Service"    OR    "AI Work Assistant"  business   │
   │  and aggregate revenue tops US$ 50,000,000 over ANY consecutive      │
   │  twelve months, you must get a separate licence from Qwen before     │
   │  ANY commercial use of it or anything descended from it.             │
   │                                                                      │
   │  Carve-out: keeping it to yourself is exempt — provided it, its      │
   │  OUTPUTS, and its underlying CAPABILITIES never reach a third party. │
   └──────────────────────────────────────────────────────────────────────┘

        Model as a Service  = letting others battle with it, where THEY
                              pick the moves. Merely linking to a battle
                              someone else is running is explicitly NOT.

        AI Work Assistant   = a product built mainly for coding or office
                              work. NOT a single-purpose tool — the slip
                              names a translation tool as an example of
                              what falls outside — and not an AI feature
                              tucked inside something about anything else.
```

The ceiling is the point. Under it, the Rayquaza is a Rayquaza. There is even an upside: a traded
Pokémon earns **1.5×** experience, the same multiplier a **Lucky Egg** gives, and **1.7×** if it
came from a different-language game. The conditional deal is not the weaker deal — it is the
stronger Pokémon, on terms that change shape as you grow.

## Five ways that lands on a real decision

1. **It picks your Pokémon before the first ball is thrown.** Both are in the box. Only the
   Sceptile can become something you let other Trainers battle with at any size. If "we might rent
   it out" is on the plan, the slip has already chosen.
2. **Everything descended from it keeps the ID No.** Evolve a **Bagon** all the way to **Salamence**, train
   it to 100, **Hyper Training** it with a **Gold Bottle Cap**, teach it a forgotten move with a
   **Heart Scale** at the **Move Reminder** — the Original Trainer field never moves. A fine-tune,
   a trimmed copy, a community re-upload: still traded.
3. **The carve-outs are drawn by what it is *for*, and that is not a stat.** "Mainly for coding or
   office work" is a positioning question, not a **Pokédex** entry. A code-review bot is inside
   the named category. A translation tool is outside it by name. An AI feature inside a shop's app
   is outside it. Which one you are is settled by how you are sold.
4. **"Keeping it to yourself" is narrower than it sounds.** It holds only while the outputs and
   the capabilities never reach anyone else. An internal tool whose text goes out to customers has
   left the carve-out, and no **Everstone** you attach changes that.
5. **Linking is exempt, and that is a genuine fork.** Watching a **Battle Video** on the **Vs.
   Recorder** is not owning the **Garchomp** in it. If the Pokémon stays in their **PC box** and
   you only connect to the battle, no ceiling of yours is in question. Put it in your own party
   and every ceiling applies. That is a slip of paper pricing a build-or-buy decision.

## The rule underneath

**Read the slip that came in the ball, not the name of the species.** "Qwen is Apache" was a fair
sentence for the Qwen3 series — that repository's README said flatly that *"All our open-weight
models are licensed under Apache 2.0."* The Qwen3.8 repository says only *"Please find the license
file released with the model weights."* A guarantee that used to be stamped on the ball is now a
slip inside it, and that change shows up on no score table anywhere.

So in the box: which repository, which revision, what the card's `license:` field says, and a
stored copy of the file itself **at the revision you pulled**, compared on every swap. The **Name
Rater** is the honest reminder — he will not rename a Pokémon whose Original Trainer name and ID
No. are not yours, however long it has sat in your party. You hold the **Master Ball**. You still
cannot do everything with what is in it.

And holding it is not a free hand. This deal is wide in what it permits and conditional in when it
permits it, which is a different animal from no conditions at all.

## What a Gym Leader is listening for

That you read the slip *before* the **Type Chart**, not after. Then that you can name which
ceiling bites at which size of operation, instead of saying "it's restrictive". The strongest
answers notice that the Sceptile and the Rayquaza are not interchangeable even where the 530 and
the 680 would allow it — one is yours and one is traded — so "which is stronger" and "which can we
field" are two different questions with two different answers.

## Where this stands, September 2026

The clauses above are quoted from the licence file shipped with the weights, read through a
verbatim third-party copy because the card pages are behind an egress block here; two independent
copies agree word for word, and the file in the model repository is the authority. The card
`license:` fields and the two release dates come from that same evidence set and from the Qwen
team's own repository, read directly. **None of this is legal advice** — thresholds, definitions
and carve-outs are exactly the text a lawyer reads differently from a Trainer, and the slip prints
a contact address for that reason. Slips get rewritten. Read it again.
