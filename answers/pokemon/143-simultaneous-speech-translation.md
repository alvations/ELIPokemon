---
id: "143"
slug: simultaneous-speech-translation
style: pokemon
category: translation
difficulty: advanced
question: "How does simultaneous speech translation work, and why is it hard?"
tags: [speech-translation, simultaneous, wait-k, latency, word-order, re-translation]
---

# "Pikachu, use Thunder—"

Stop there. **What was the command?**

```
   "Thunder"        110 power. might miss.
   "Thunderbolt"     90 power. will not miss.
   "Thunder Wave"   no damage at all — it PARALYSES
   "Thunder Punch"  physical, gets in close
   "Thunder Fang"   different again
```

Five moves. Identical opening. And one of them is not an attack in any sense — **Thunder Wave**
does no damage whatsoever, and a Pokémon that throws a Thunderbolt when it was told to paralyse has
lost the turn and possibly the match.

Now translate that command for a Trainer who does not speak the language, **while it is still being
shouted**, in a battle where the turn is already resolving.

That is simultaneous translation. It stops being a quality problem and becomes a **quality-versus-
delay** problem, and there is no point on that curve where you get both.

## Sometimes waiting is not optional ⏳

Some languages put the important part **last**. The whole sentence has been built and the thing it
is actually about arrives at the very end — like a Trainer who describes the situation, the
weather, the type matchup, and *then* names the move.

📌 You cannot begin translating that. Not because the machine is slow — because **the information
has not arrived yet**. Guess, and you may have to take it back.

⚠️ This is the fundamental obstacle and **no clever policy removes it.** It can only be traded
against delay, or against the risk of being wrong.

## Deciding when to speak 🎚️

The whole system is one alternation: **listen more**, or **commit and say something**.

* **⏱️ Wait a fixed amount, then keep pace.** Hear a few words, then say one for every one you hear.
  Almost embarrassingly simple, needs no training, and it is a genuinely strong baseline. How long
  you wait *is* the dial.
* **🧠 Or wait longer only where it is actually ambiguous.** Hold at "Thunder—", run freely
  everywhere else. Better on the curve, more machinery.
* **🔄 Or say something and correct it.** Retranslate the whole thing every time more arrives, and
  overwrite what you already put up.

That last one deserves its own warning. **On a scoreboard it is fine** — the text rewrites itself,
the audience barely notices, and the final quality is near-perfect. **In a battle it is
impossible.** Once Pikachu has thrown the Thunderbolt, there is no version of shouting *"sorry, I
meant Thunder Wave"* that puts the electricity back. You cannot un-throw a move.

So measure the rewriting, not just the delay. How often did the display change **after** somebody
had already read it?

## Two machines or one 🔗

Writing the cry down and then translating the writing (question 138) is easy to assemble and stacks
three problems: mishearings arrive downstream as **confident** nonsense, the delay adds up across
both stages, and somebody has to decide where one command ends and the next begins — in real time,
with no idea what is coming.

That last one is badly underrated. A Trainer mid-battle does not speak in tidy sentences. They
shout continuously, they restart, they say *"use Thunder— no, Quick Attack!"* **Putting the
boundary in the wrong place is a mistranslation that nothing downstream can repair.**

## Always report two numbers 📊

Quality alone means nothing here.

* ⏲️ **How far behind the speaker you are**, in words or in milliseconds.
* ⚙️ **And count the thinking time.** A policy that looks instant on paper and then runs an enormous
  Pokédex for every word is not instant. **Extreme Speed** is only fast if the Pokémon using it is.

📌 A system reported with a quality score and no delay figure should be assumed to have **waited
for the Trainer to finish talking**, which is the one thing it was built not to do.

## Where it actually breaks 💥

* 🎙️ **Real Trainers stumble.** Restarts, "er", corrections mid-word. A machine drilled on clean
  recorded commands falls apart on a live Gym battle.
* 🏷️ **Names must be right the first time.** There is no second pass (question 133). **Quick Attack**
  and **Quick Claw** are not the same thing, and nobody is going to fix it afterwards.
* 🔢 **Numbers are the classic catastrophe.** *"Twenty-five"* arrives in pieces and changes meaning
  as it completes. Commit at *"twenty"* and you are simply wrong — which is survivable in a battle
  and is not survivable when the number is a dose.
* 🧑‍🏫 **And no human does this either.** A real interpreter chunks, compresses, and **predicts from
  knowing the subject** — the way a veteran Trainer hears "Pikachu, use Thunder—" against a
  **Gyarados** and already knows it is Thunderbolt, because nobody paralyses a Pokémon that is about
  to take quadruple damage. Expecting word-perfect fidelity at zero delay is expecting something no
  professional has ever delivered.
