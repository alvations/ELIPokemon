---
id: "041"
slug: rag-vs-finetuning
style: pokemon
category: rag
difficulty: core
question: "What is RAG, and when should you use it instead of fine-tuning?"
tags: [rag, retrieval, grounding, fine-tuning, architecture]
---

# RAG is letting your Trainer consult the Pokédex mid-battle

Two ways to make a Trainer who knows your Gym's roster:

**🏕️ Train it in.** Months of study until every Pokémon on the roster is memorised.

**📖 Hand it the Pokédex.** It looks things up when it needs to.

The second one is RAG, and it's usually right — for a reason that isn't obvious.

## The insight 💡

Your Trainer is **unreliable at remembering** and **excellent at reading**.

Ask it to *recall* Flareon's ability and you get a confident guess. Hand it the Flareon page and ask
what the ability is, and you get the right answer, every time.

RAG doesn't make your Trainer smarter. It **converts the question from a memory question into a
reading question**, and reading is the thing it's actually good at.

## The lookup 🔍

```
   ❓ "What beats a Rain team?"
              │
              ▼
   ┌─────────────────────┐        ┌────────────────────────────┐
   │ 🔎 search the        │◄───────│ (offline) chop your        │
   │    Pokédex           │        │ scouting reports into      │
   └──────────┬───────────┘        │ pages and index them       │
              │ 50 candidate pages └────────────────────────────┘
              ▼
   ┌──────────────────────┐
   │ 📋 read them properly │   a slower, careful second pass
   │    and rank           │
   └──────────┬───────────┘
              │ the best 5
              ▼
   ┌──────────────────────────────────────┐
   │ 🧠 "Here are 5 pages. Now answer,     │
   │     and tell me which page you used." │
   └──────────────────────────────────────┘
```

Two passes matter: a **fast, broad** sweep to find candidates, then a **slow, careful** read to
rank them. Doing only the fast pass gets you roughly-relevant pages. Doing only the slow pass on
everything takes all day.

## Pokédex vs camp 📊

| | 📖 Pokédex | 🏕️ Camp |
| --- | --- | --- |
| Teaching it **facts** | ✅ the whole point | ❌ unreliable, breeds bluffing |
| Teaching it **style** | ❌ | ✅ the whole point |
| Roster changed today | ✅ reprint one page | ❌ retrain, wait days |
| "Where did that come from?" | ✅ page 47 | ❌ unanswerable |
| Different Trainers see different pages | ✅ hand out different books | ❌ impossible |
| Removing a leaked page | ✅ tear it out | ❌ retrain from scratch |
| Cost per battle | higher — carrying a book | unchanged |

**📌 Pokédex for what it should KNOW. Camp for how it should BEHAVE.**

They're not rivals. The best setup is usually both: a camp-trained Trainer with good habits, who
reads from a well-organised Pokédex.

## The underrated reasons 🔐

Three arguments for the Pokédex that nobody mentions until it's too late:

* 📌 **You can check its work.** "Page 47, line 3." Try auditing something a Trainer merely
  remembers.
* 🗑️ **You can take things back.** A page you shouldn't have published — tear it out, it's gone in
  seconds. Something trained into a Trainer's memory needs the whole Trainer rebuilt.
* 🔒 **Different people, different books.** Junior Trainers get the junior Pokédex. Once knowledge
  is *in* a Trainer, everyone who talks to it gets everything.

## Where the Pokédex fails 📉

* 🔍 **Bad search ruins everything.** If the right page isn't found, a Champion-level Trainer with a
  Pokédex is no better than one without. **Most "the Pokédex didn't help" stories are search
  failures**, not Trainer failures.
* 🌍 **Big-picture questions.** *"What are the overall trends across all 10,000 scouting reports?"*
  Five pages cannot answer that. You need summaries of summaries.
* 🔗 **Two-step questions.** *"Which of our opponents runs the Pokémon that just got banned?"* —
  that's two lookups chained. One lookup finds neither.
* 🌫️ **Too many pages is worse than a few.** Hand over twenty pages and it does *worse* than with
  five. More pages, more distraction, and the middle of a thick stack gets skimmed.
* ✂️ **The answer straddles a page break.** Half on page 12, half on page 13, and neither page
  alone says it.

## "But my Trainer can read a whole library now" 📚

True — modern Trainers can hold enormous amounts of text at once. So why look anything up?

Because carrying the *entire library* into every battle is slow, expensive, and — genuinely —
**often less accurate** than carrying five well-chosen pages. More text means more distraction, and
we know the middle of a thick stack gets skimmed.

Read the whole library when it's small and the question truly needs all of it. Otherwise: look it
up, then read carefully.
