---
id: "182"
slug: vlm-distillation
style: pokemon
category: multimodal
difficulty: intermediate
question: "How do you make a small vision-language model that is actually useful?"
tags: [distillation, small-models, quantization, on-device, specialisation, evaluation]
---

# You cannot take Mewtwo everywhere

The question is never *"how small can the Pokémon be"*. It is **"how narrow can the job be"**.

A **Pidgeotto** that does exactly one thing beats a **Mewtwo** you cannot afford to bring out
thirty thousand times a day. And it beats it on the number that actually decides things: **what it
costs per correct answer** — not how good it is at its best.

**Blissey** has 255 HP and cannot hit anything. **Deoxys** hits like nothing else and folds to a
breeze. Neither is *the best Pokémon*; each is the best Pokémon **for something**, and that is the
whole of this page.

## Three ways to make it smaller ⚖️

* **🎓 Let the big one teach it.** Have Mewtwo work through **your** routes — not a generic training
  set — and drill the small one on what it produced. 📌 This is the strongest lever, because it
  passes on both the *ability* and **how the big one behaves on your particular problems**.
  ⚠️ With question 146's warning attached: **the teacher's mistakes become the student's facts.**
  Check a sample by hand.
* **📦 Compress it** (question 030). Cheap and nearly free of loss. ⚠️ And **check the eye
  separately** — a squashed eye feeds a slightly wrong tile into *everything* downstream, and a
  surprising number of setups never compress the eye at all, or compress it without checking.
* **✂️ Or make it hold less.** Fewer tiles (question 121), a smaller voice, a smaller eye. Remember
  the asymmetry from question 165: **cutting tiles saves a great deal; shrinking the voice saves
  less than its size suggests.**

## One job, done properly 🎯

A small Pokémon asked to cover every type is weak against all of them — a **Normal** type with no
resistances and no threats. A small Pokémon asked to do **one** thing can match Mewtwo at that one
thing, the way a **Shuckle** built entirely for Defence outlasts things far above its weight.

```
   Mewtwo ─► works through your real routes ─► a person checks a sample ─► drill the small one
                    │
              ⚠️ this is the expensive part, and it happens ONCE.
                 Everything afterwards is cheap, forever.
```

📌 The break-even is usually startlingly quick. At real volume, a day of Mewtwo's time plus a
training run pays for itself in weeks. ⚠️ Teams pay legendary prices for a narrow, high-volume chore
for **a year** because nobody sat down and did the arithmetic.

## What goes first when you shrink it 📉

Worth knowing **before** you meet it in the field:

* **📝 It gets fussy about how you ask.** Reword the instruction slightly and it does something else.
* **🖼️ Several pictures at once** (question 124) falls apart much faster than one picture does.
* **🔤 Reading small print** — ⚠️ **but check this one before blaming the size.** It is very often
  question 121's problem, not a capacity problem, and **walking closer fixes it** where a bigger
  Pokémon would not have.
* **🎚️ It is confidently wrong more often** — the **Confusion** problem from question 132, and it
  matters enormously if you were routing on how sure it said it was.
* **🚪 And its manners do not always come along.** Caution learned by the teacher transfers
  **unevenly** through the drilling, so **re-test the refusals** (question 139) rather than assuming
  they came in the package.

## Judging it 🏅

📌 **Report what it costs per correct answer, not how accurate it is.** A Pokémon that is right
ninety-two times in a hundred at a fiftieth of the price beats one that is right ninety-six times
for most purposes — and comparing accuracy alone **actively hides that**.

And test it on **your own routes**. Public leaderboards tell you about public leaderboards
(question 147). Two hundred examples from the traffic you actually see is worth more than all of
them put together for this one decision.
