---
id: "097"
slug: serving-cost-latency
style: pokemon
category: mlops
difficulty: intermediate
question: "How do you reduce LLM serving cost and latency in production?"
tags: [serving, latency, throughput, batching, caching, routing]
---

# Running a Gym: making battles fast and cheap

Two completely different costs, with completely different fixes:

```
   📖 READING THE TEAM SHEET           ⚔️ PLAYING THE TURNS
   ─────────────────────────           ────────────────────
   Scout everything at once.           One turn at a time, in order.
   Busy, focused, productive.          Flipping through your notebook
                                       before every single turn.

   → how long before you MOVE          → how long between moves
   → costs scale with sheet length     → costs scale with match length
```

📌 This is why **long matches cost far more than long team sheets.** Reading is efficient; playing
is a grind, and every turn re-reads everything.

## The fixes, biggest wins first 🏆

**1. ✂️ Play shorter matches. ← the most ignored fix**

Every turn costs. So **stop your Trainer monologuing.**

> ❌ *"Let me consider all six of my Pokémon and their matchups against each of their six, taking
> weather into account, and then explain my reasoning at length before finally..."*
>
> ✅ *"Thunderbolt."*

Same decision. A fraction of the cost. **Asking for brevity is free**, and it directly cuts the
expensive half of the bill.

**2. 📋 Photocopy the standard briefing.**

Every match starts with the same twelve-page rulebook? **Scout it once. Staple a copy into every
notebook.** Never read it twice.

Cuts your time-to-first-move enormously, and the briefing becomes nearly free.

📌 Requires the unchanging part to be **at the top** — reorder it and you lose the whole benefit.

**3. 🎯 Don't send the Champion to every match. ← usually the biggest saving**

Most challengers are ordinary. **A journeyman Trainer handles them fine.**

Put something quick at the door that asks *"is this hard?"* — route the routine matches to the cheap
Trainer, escalate the tricky ones.

This is often the single largest cost reduction available, and it's an **architecture** decision, not
a tuning knob.

**4. 🔄 Never let a table sit idle.**

Naïvely, you run ten matches, wait for **all ten** to finish, then start ten more. So nine tables sit
empty while one long match drags on.

**Instead: the moment a table frees up, seat the next challenger.** Several times the throughput.
This is table stakes for running your own Gym.

**5. ✏️ Write your notes smaller.** Half the notebook, half the page-flipping, half the time per turn.

**6. 📄 Stop wasting desk space.** Don't hand every match a 500-page binder when most end in twelve
turns. Loose pages, handed out as needed.

**7. 🐣 Let a rookie guess ahead, and have the Champion check.** Two to three times faster per match —
**but only when the Gym is quiet.** During a packed tournament it makes things *worse*, because
there's no idle capacity to spend.

**8. 🎓 Train your own specialist.** Have your Champion play ten thousand of *your* matches, then
train a small cheap Trainer to copy it. **Ten times cheaper on your specific job.** Highest return of
anything here, and it takes real effort.

**9. 🗂️ Remember answers to repeated questions.** *"What beats Water?"* gets asked forty times a day.
Answer it once, keep the answer.

⚠️ **Dangerous** for anything personal or time-sensitive. *"How's MY team doing?"* must never come out
of a shared cache.

**10. 📺 Show the moves as they happen.** Doesn't make anything faster. **Transforms how fast it
feels** — a Trainer who starts moving immediately feels quick even in a long match. Cheap. Should be
your default.

## What to measure 📊

| | What it means |
| --- | --- |
| ⏱️ **Time to first move** | how responsive it feels |
| 🔁 **Time between moves** | how it feels once underway |
| 📈 **Matches per hour** | your total capacity |
| 💰 **Cost per match** | what the business cares about |
| ✅ **Matches per hour AT AN ACCEPTABLE SPEED** | ⭐ **the honest number** |

That last row is the one to report.

You can *always* raise matches-per-hour by seating more challengers — and every one of them waits
longer. Push it far enough and you have spectacular throughput and a queue nobody will tolerate.

📌 **Throughput at unacceptable speed is not capacity.** Report the number that includes both.
