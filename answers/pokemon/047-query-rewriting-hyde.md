---
id: "047"
slug: query-rewriting-hyde
style: pokemon
category: rag
difficulty: advanced
question: "What are query rewriting and HyDE, and when do they help?"
tags: [hyde, query-expansion, multi-query, step-back, rag]
---

# Asking the Pokédex a better question

Your search only fails for one real reason: **you asked in your words, and the report was written in
someone else's.**

```
   😕 A trainer asks:   "my guy keeps dying"

   📄 The report says:  "Insufficient defensive investment leads to
                        premature knockouts against physical attackers."

   Words in common: zero. Nothing will be found.
```

The report is *right there*. Your search will never find it. So fix the question before you search.

## 1. 🔀 Ask it five ways

```
   "my guy keeps dying"
        ├─► "my Pokémon faints too easily"
        ├─► "how to improve survivability"
        ├─► "increasing bulk and defence"
        └─► "preventing knockouts"
```

Search for all of them. Combine the results. Simple, sturdy, and the **highest-value fix for most
systems** — you're just covering more of the ways a thing can be phrased.

## 2. 🎭 Write a fake answer, then search with THAT

The clever one, and the one worth understanding.

Don't search with your question. Ask your Trainer to **make up an answer first** — then search using
the made-up answer.

```
   ❓ "my guy keeps dying"
           │
           ▼  Trainer invents a plausible-sounding answer
   🎭 "Pokémon faint quickly when defensive stats are under-invested.
       Consider EV training in HP and Defence, and holding Leftovers
       for passive recovery."
           │
           ▼  search using THIS, and throw the text away
   📄 finds the real report — which reads exactly like this
```

Why does searching with a **made-up** answer work better than searching with the real question?

Because **questions and reports don't look alike.** Questions are short, worried, and casual.
Reports are long, calm, and technical. On the map they sit in completely different neighbourhoods —
so searching with a question means searching the wrong part of town.

A fake answer, however wrong, is *shaped like a report*. It lands in **report country**, surrounded
by actual reports. And that's all you needed.

📌 **The fake answer being factually wrong doesn't matter at all.** You threw the text away. You
only ever wanted its *shape*.

## 3. 🔭 Ask a broader question first

> ❌ *"What EV spread does Assault Vest Tapu Fini run in Regulation G?"*

Too specific. Nothing matches word for word.

> ✅ *"How is Tapu Fini built for competitive play?"*

Now you get real material. Read it, and the specific answer is usually in there.

## 4. 🔗 Break two-part questions apart

> *"Which of my Pokémon is weak to the type my rival's ace uses?"*

That's **two** lookups pretending to be one. No single search answers it:

1. *"What type is my rival's ace?"* → Dragon.
2. *"Which of my Pokémon are weak to Dragon?"* → these three.

One search finds neither half. Split it.

## 5. 🗣️ Fix the pronouns — non-negotiable

This is the one everybody forgets, and it breaks every conversation.

```
   Trainer: "Tell me about Gyarados."
   You:     [good answer]
   Trainer: "What about the other one?"
                     ▲
            Search for this exact phrase and you get NOTHING.
            "the other one" appears in no report ever written.
```

Before searching, rewrite it against the conversation: **"What about Milotic?"** Now it's findable.

📌 If you're building anything conversational, this isn't an optimisation. Without it, every
follow-up question fails, and follow-ups are most of a conversation.

## When to skip all this ⚠️

Every rewrite costs a Trainer call — a few hundred milliseconds, before the search even begins, on
the critical path.

* ✅ **Worth it:** vague questions, casual users searching technical reports, multi-turn chat,
  two-part questions.
* ❌ **Skip it:** the question was already precise; or you're looking up an exact code, where
  expanding *actively hurts* — `TM-4471` should stay `TM-4471`, not become "an error related to
  technical machines."

And here's the honest ordering, because people reach for this first and shouldn't:

> 📌 **Fix how you cut up the reports. Add a coach who reads properly. Search by words as well as by
> meaning. THEN rewrite queries.**

Query rewriting is a real win on genuinely hard questions, and a very popular way to add latency to
a system whose actual problem was somewhere else entirely.
