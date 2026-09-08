---
id: "183"
slug: multimodal-accessibility
style: pokemon
category: multimodal
difficulty: intermediate
question: "How should multimodal models be used for accessibility?"
tags: [alt-text, audio-description, captioning, wcag, user-testing, autonomy]
---

# Describing a battle to somebody who cannot watch it

This is the oldest genuinely useful thing a Pokédex does. Not winning anything — **telling somebody
what is there** when they cannot see it for themselves.

And it is the application where being subtly wrong does the **most** harm, for one reason:

📌 **The listener cannot check you against the picture.**

A Trainer looking at the field spots an invented **Charmeleon** wing instantly (question 122).
Somebody relying on your description has **only your description** — and a confident wrong one is
worse than saying nothing at all.

## The same picture, three different right answers 🖼️

Describing is not captioning. **What counts as a good description depends on why somebody is
looking.**

```
   the same photograph of a route, three situations:

   a report on a Sandstorm    ─► "Sand blowing across Route 111, visibility low,
                                  two Trainers sheltering by the rock face."
   a listing for a held item  ─► "A Leftovers, the item the Snorlax is holding."
   a decorative header        ─► say nothing. Announcing it is NOISE.
```

So a system needs **the surrounding page**, not just the picture. It needs to be **short by
default** and detailed on request. And — the two everybody omits — **a way to say "this is
decorative"** and **a way to say "I cannot tell."**

⚠️ And where there is **writing** in the picture, **read it out**. Do not describe it. *"A sign"* is
useless; the sign said which way **Cerulean City** is. Same for a chart: give the **numbers**, not
the shape (question 127).

## Describing a battle as it happens 🎙️

* 🗣️ **The description has to fit in the gaps.** Between the commands, between the moves — a
  length-constrained job (question 144) with the same timing discipline as a dub (question 154).
* 👥 **And say who is speaking, and what the noise was.** A transcript that is right about the words
  and silent about **which Trainer said them** is far less usable than its accuracy suggests
  (question 125). *"An Onix collapses"* is information.

## The rules that make this responsible 🧭

* **🤷 Say when you are unsure.** *"A Pokémon, possibly a Growlithe"* is more useful than a confident
  invention. This is question 151's abstention argument — and here **the listener has no way to
  catch you**, which makes it obligatory rather than merely good practice.
* **🚫 Never state things about a person you cannot possibly know.** Reading somebody's age, their
  background, their mood, or whether they are disabled off a photograph **and stating it as fact**
  is a documented harm, not a feature. ⚠️ **Describe what is visible. Attribute nothing.**
* **➕ This adds to human description. It does not replace it** where the content matters. The same
  argument as the signing avatars in question 155, and it fails the same way: **deployed as a saving
  rather than as extra coverage.**
* **👥 Test it with the people who will rely on it, and pay them.** A system judged only by people
  who can see it, scoring well on caption metrics, will pass every test and be **unusable**.
* **🚪 And do not remove the path that already worked.** The point is *more* access, not a cheaper
  substitute for the access somebody already had.

## Judging it 🏅

⚠️ Comparing your description against a reference description is close to irrelevant here.

Measure whether it **worked**: could the listener answer questions about the picture, follow the
battle, find the item? Then measure **invention** (question 122) — weighted far more heavily than
you would anywhere else — and how often it admitted uncertainty.

📌 And say **who did the judging.** In this application, that single line tells a reader more than
any score you could print beside it.
