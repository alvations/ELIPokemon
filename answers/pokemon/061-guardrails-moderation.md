---
id: "061"
slug: guardrails-moderation
style: pokemon
category: safety
difficulty: intermediate
question: "How do you design guardrails and a moderation pipeline?"
tags: [guardrails, moderation, classifiers, defence-in-depth, over-refusal]
---

# Guardrails: the referees standing around the arena

You cannot rely on your Pokémon's own training to keep the match legal. You put **referees** at every
stage, each catching what the last one missed.

```
   🗣️ someone shouts an order
        │
   ┌────▼──────────────────┐  1️⃣ THE DOOR CHECK — instant
   │ Is this even a legal   │     Wrong format? Known-banned phrase?
   │ command? Too long?     │     Shouting forty times a minute?
   │ Obvious rule-break?    │     Milliseconds. Catches the obvious.
   └────┬──────────────────┘
   ┌────▼──────────────────┐  2️⃣ THE JUNIOR REF — reads the request
   │ Does this LOOK like    │     "Is this trying something dodgy?"
   │ trouble?               │     Quick. Sometimes wrong.
   └────┬──────────────────┘
   ┌────▼──────────────────┐  3️⃣ YOUR POKÉMON — with its own training
   │ It knows the rules     │
   └────┬──────────────────┘
   ┌────▼──────────────────┐  4️⃣ THE HEAD REF — watches the MOVE
   │ Was that move legal?   │     ⭐ usually the best referee here
   │ Did it reveal          │
   │ something private?     │
   └────┬──────────────────┘
   ┌────▼──────────────────┐  5️⃣ THE SCOREKEEPER — mechanical checks
   │ Valid move name? Real  │     No judgement. Just: does this
   │ target? Nothing leaked?│     check out?
   └────┬──────────────────┘
        ▼  the move happens      6️⃣ + everything logged for review
```

## Why the head ref matters most 👀

Here's the thing people get backwards. They pour all their effort into the **junior ref at the door**
and skimp on the one watching the actual move.

But judging a *request* is genuinely hard:

> *"How does Explosion work?"*

That's a kid learning the game. Or a competitive player planning a strategy. Or someone about to do
something stupid. **The words are identical in all three cases.** The junior ref is guessing.

Judging a *move* is easy:

> *"It just used a banned move."*

No ambiguity. Nothing to interpret. That's why layer 4️⃣ catches more, more reliably, than layer 2️⃣ —
and why skipping it in favour of an aggressive door policy is the standard mistake.

## Don't just allow or block 🚦

Blocking is blunt. Match the response to how sure you are:

| How confident? | What to do |
| --- | --- |
| 🔴 Certain | Block it. Log it. Explain briefly. |
| 🟠 Pretty sure | Block, and put it in the human review queue. |
| 🟡 Unsure | **Let it try again, with stricter instructions.** |
| 🟢 Probably fine | Allow, log for later analysis. |

That 🟡 row is badly under-used. A borderline move often just needs the Pokémon to **redo the turn
more carefully** — not a refusal.

## The failure nobody measures 🕵️

This is the one that quietly ruins products.

Every referee makes mistakes in **both** directions. And here's the asymmetry:

* ❌ **A banned move gets through** → incident. Alarms. Meeting. Everyone knows.
* 🤫 **A legitimate move gets blocked** → the Trainer shrugs and leaves. **You never find out.**

Refuse enough real requests and you have a Pokémon nobody can use — and a dashboard showing zero
incidents, which everyone reads as success.

📌 **Measure it deliberately.** Keep a list of requests that *sound* alarming but are completely
fine — a kid asking how Explosion works, a researcher asking about a known exploit, a historical
question about a violent tournament. Track how many get wrongly refused. **Report that number next
to your incident count.**

> A system with zero incidents and a 15% false-refusal rate isn't safe. It's broken.

## Running it in practice ⚙️

* ⏱️ **Referees cost time.** Five of them in sequence and every turn drags. Run the door checks
  **in parallel**, and check the output in chunks as it comes rather than waiting for all of it.
* 💰 **Referees cost money.** At scale, a referee per turn is a real bill. Use quick ones.
* 📅 **Version your rulebook.** Rules change. Log which version made each call, or you can never
  explain a decision from three months ago.
* 📢 **Let people appeal.** Wrongly blocked? There must be a way to say so, and it must reach the
  person who tunes the referees.
* 🤐 **Don't explain the block in detail.** *"Blocked — banned move, category 4, rule 12(b)"* tells
  the next person exactly what to work around. **A detailed refusal is a free map of your defences.**
