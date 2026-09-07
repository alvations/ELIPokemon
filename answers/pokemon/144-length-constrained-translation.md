---
id: "144"
slug: length-constrained-translation
style: pokemon
category: translation
difficulty: intermediate
question: "How do you translate when the output has a hard length limit?"
tags: [subtitles, length-control, ui-strings, expansion, line-breaking, compliance]
---

# Ten characters, and **Fletchinder** has eleven

The older games let you nickname a Pokémon in **ten characters**. Not "about ten". Ten. Type an
eleventh and nothing happens.

And then the roster kept growing, and the names kept getting longer — **Fletchinder**,
**Blacephalon**, **Centiskorch**, **Crabominable** — until the limit itself had to be raised to
twelve to fit them.

📌 **That is the whole lesson, and it is written into the games' own history.** A box sized around
the words you had is a box that breaks on the words you get later. And a name that does not fit is
not a slightly worse name. It is **a name you cannot enter**, and no scoring scheme from question
129 can see the difference between that and a perfectly good one.

## Everything gets longer 📏

Translating out of one region's language into another's almost always **expands**:

```
   into some regions:   +10% to +35%. compounds, longer words, more of them
   into others:         fewer characters — but each one takes more room on screen
   into others again:   the same length, written right-to-left, and now
                        every box you laid out is mirrored
```

⚠️ **Short things suffer worst**, because there is no slack anywhere. A ten-character name has
nowhere to give. A whole Pokédex entry can absorb a third more words and still fit the page; a
button that says **Fly** cannot absorb even one.

## Ways to make it fit 🎚️

* **🏷️ Ask for a length up front.** Mark every training example short / normal / long and prefix the
  request the same way — exactly the mechanism used for politeness in question 141.
* **💬 Just say the limit, then check.** Machines comply *approximately*. **Always measure. Never
  assume.**
* **🎲 Write several and keep one that fits.** Generate a handful, throw out the ones over budget,
  rank what remains. Unglamorous, reliable, and what most working systems actually do — it turns
  "obey a constraint" into "filter a list", which is a far easier problem.
* **✂️ Or cut it off at the limit.** Guaranteed to fit. Produces **Crabominabl**.
* **🔁 Or translate, measure, and ask again for a shorter one.** Costs a round trip, gives by far the
  best short versions, and it is exactly what a human does.

## Shortening is a skill, not a truncation 🎯

This is the part machines get wrong and professionals get right.

**Bad:** take **Crabominable** and chop the end off. **Good:** notice what is redundant and drop
*that*.

A battle message reading *"The wild Fletchinder used Quick Attack on your Charizard!"* can lose
"wild", can lose "on your Charizard" because there is only one Charizard on the field and everyone
can see it, and becomes *"Fletchinder used Quick Attack!"* — shorter, and **nothing was lost**,
because the dropped words were already on screen.

📌 That — dropping what is redundant, never clipping the ending — is what *"make it shorter"* should
mean to your system.

## The battle box has its own rules 📺

* **⏱️ It has to be readable in the time it is up.** A message can fit the box perfectly and still be
  gone before anyone finishes reading it. Fitting and readable are two separate limits, and you
  must hold both.
* **↩️ Break lines where the sentence breaks.** Never split **Quick Attack** across two lines, and
  never leave a word stranded alone on the second. A badly broken two-line message is measurably
  slower to read than a well-broken one **of exactly the same length**.
* **✌️ Two lines, maximum.** And do not let a message straddle the moment the scene changes.

## And the slots must survive 🧩

Game text is full of gaps waiting to be filled: *"{Pokémon} used {move}!"* Those markers must come
through **exactly** (question 133), because something is going to write **Gyarados** and
**Thunderbolt** into them at the last moment, and a translator that helpfully "translates" the
marker breaks the message for every Pokémon in the game.

⚠️ And the same word is often not the same word twice. **Fly** on a menu is a way of travelling.
**Fly** in the move list is an attack. One region will use one word for both; most will not. Send
the *context* along with each string — and almost nobody does.

## Reporting it 📊

**Always give the fit and the quality together.**

* how many came in under the limit;
* **how good the ones that fitted actually are**, so the damage from shortening is visible;
* and the curve — quality as you tighten the box.

⚠️ A system reported as *"95% fit"* with no quality figure is very probably producing
**Crabominabl**. A system reported with a glowing quality score and no fit figure is almost
certainly overflowing the box, and its score is **structurally incapable** of noticing.
