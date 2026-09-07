---
id: "160"
slug: multimodal-chain-of-thought
style: pokemon
category: multimodal
difficulty: advanced
question: "Does chain-of-thought reasoning help vision-language models?"
tags: [multimodal-cot, visual-reasoning, test-time-compute, cropping, verification, tools]
---

# Thinking harder about a Pokémon you cannot see properly

Thinking step by step works marvellously when the difficulty is **working something out**. Applied
to *looking*, it often does nothing — and sometimes makes things **worse**. The reason is the whole
lesson.

## Two failures that look identical from outside 🔍

```
   IT COULD NOT SEE                          IT COULD NOT WORK IT OUT
   ────────────────                          ────────────────────────
   the label on TM26 was four tiles           it read Blissey's 255 HP and
   wide and is simply gone (q121, q127)       Shuckle's 230 Defence correctly
                                              and subtracted them wrong

   think harder ►  it now produces a          think harder ►  genuinely fixes it
   beautifully argued paragraph about
   a TM it never read. Longer. More
   fluent. Still wrong — and now the
   mistake comes with reasoning attached.
```

📌 **Most "it cannot reason about pictures" is "it could not see."** Extra thinking does not add
tiles. A Trainer who cannot make out whether that shape has wings does not settle it by thinking
harder about **Charmeleon**; they settle it by walking closer.

And worse: a long chain of reasoning **drifts off the picture** exactly the way a long Pokédex
entry does (question 122) — every step listens to the previous step and less and less to the thing
in front of it. Eight steps in, it is reasoning about its own third sentence.

⚠️ **The test that settles it:** hand the Pokédex a perfect written description of the picture. If
the answer becomes right, it never had a thinking problem. It had an **eyesight** problem, and no
amount of deliberating will touch it.

## What does work: keep going back and looking 👁️

* **🔭 Let it walk closer.** Give it the ability to say *"show me that corner, bigger"* and look
  again. This attacks the actual bottleneck (question 121) instead of narrating around it, and it
  is **by far the most effective thing on this list.**
* **📋 Write down what it sees, then reason over the writing.** The six stats first, the subtraction
  second (question 127). Splits eyesight from arithmetic and makes it obvious which one failed.
* **👉 Make every step point at something.** A claim that has to name the tile it came from is far
  harder to invent (questions 122, 128).
* **🧰 Or bring specialists.** Something that reads small print, something that counts, something
  that traces outlines. The Pokédex directs; the specialists look. This is a **Double Battle** team
  — **Togekiss** doing one job and **Amoonguss** another — rather than one **Arceus** trying to
  cover every type at once, and it is reliably better.
* **✅ Then check the answer against the picture.** A second pass, purely to verify. Cheap, and it
  works because **checking is easier than answering** — the same reason it is easier to confirm a
  Pokémon is a **Gyarados** than to name it from a silhouette in question 120's lineup.

## Where the extra effort pays 💰

| What you are asking | Does thinking longer help? |
| --- | --- |
| 📊 Comparing **Blissey**'s hexagon with **Shuckle**'s | **Yes**, substantially |
| 🔢 Counting **Zubat** that overlap each other in **Mt. Moon** | **Yes** — especially if it may look again |
| 🦎 *"Is that a **Charmeleon** or a **Charizard**?"* | **No.** It either saw the wings or it did not |
| 🔤 Reading the label on **TM26** | **No.** Walk closer instead |

📌 And here is the instinct to unlearn: with text, more effort means **more thinking**. With
pictures, more effort should usually mean **more looking** — another crop, a closer pass, a second
glance. Spending the whole budget on deliberation is spending it in the wrong place.

## Judging it 🏅

* 🔀 **Report with and without, broken down by type.** ⚠️ An overall gain hides that the thinking
  helped with charts and actively **hurt** at naming Pokémon — and you will roll that out
  everywhere.
* 🧾 **Read the working, not just the answer.** Right answer by wrong reasoning is common, and it
  does not survive contact with a slightly different question. Sample a few and actually read them.
* 💸 **And count the cost.** Three points for six times the effort and four extra close-up looks is
  a **trade**, not a free win. Say what it cost.
