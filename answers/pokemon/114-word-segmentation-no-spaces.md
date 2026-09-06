---
id: "114"
slug: word-segmentation-no-spaces
style: pokemon
category: multilingual
difficulty: intermediate
question: "How do you handle languages that do not put spaces between words?"
tags: [segmentation, chinese, thai, sacrebleu, tokenization, evaluation]
---

# The order comes out as one long shout

Most Trainers give orders in neat pieces. *"Pikachu. Thunderbolt. Now."* Three clean chunks with
gaps you can hear.

Then there is Exploud. One continuous roar, start to finish, and somewhere inside it is an
instruction. Where one word stops and the next begins is something **you** decide, from context,
every time. Nobody put the gaps in, because in Exploud's language there were never any gaps to
put in. Whismur and Loudred are the same; a Chatot playing back a recorded phrase gives you one
unbroken stretch of sound and no punctuation whatsoever.

Braille on the Sealed Chamber wall is the written version: an unbroken run of bumps under the
Hoenn stone. The instruction is in there — Registeel is behind it. The spaces are not.

## The good news: your Pokémon never needed the gaps 🎉

This looks like a crisis and mostly is not. A Pokémon listening to a continuous shout can learn
the useful chunks straight from the sound, without anyone marking them first — and it will pick
chunks that are useful to *it*, which is all that was ever required.

The old approach was to keep a specialist — the sort of researcher who sits in the Ruins of
Alph all day sorting Unown into words — whose only job was inserting gaps before your Pokémon
was allowed to listen. That specialist is now mostly unemployed. A Pokémon fed the raw roar
does better than one fed a pre-chopped version, if only because nothing gets mangled on the
way in.

And note how shaky the specialists always were: **two researchers in the same Alph chamber will
break the same inscription into different words and both be right.** There is no fact of the
matter waiting to be uncovered here.

## The bad news: the scoreboard still counts words ⚖️

Here is where it genuinely bites.

The Pokémon League scores a translated battle report by counting how many **words** match the
official version. Fine in Kanto. For an Exploud transcript, somebody has to insert the gaps
before anything can be counted — and who inserts them changes the score.

```
   ONE ROAR, TWO REFEREES
   ─────────────────────────────────────────────────
   Goldenrod hears:  [use][Thunderbolt][now]      ► 2 of 3 match ► 67%
   Ecruteak hears:   [use Thunder][bolt now]      ► 1 of 2 match ► 50%

   Same battle. Same translation. Same official version.
   Two scores. Neither referee did anything wrong.
```

Whitney's Gym publishes 67%. Morty's publishes 50%. Same battle, same translation, and **those
numbers were never comparable** — nothing in either report says so.

## How the League fixes it 🏅

* 📝 **Name the referee on the scorecard.** Every score is published with exactly who inserted
  the gaps and which rulebook they used. A number without that is not a result, it is a rumour.
* 🔤 **Or count letters instead of words.** No gaps needed, no referee needed, no argument.
  Which is why character-counting has quietly become the sensible default for these regions.

## Three other things calibrated on gaps that quietly break 🧨

* ✂️ **Chopping a long Pokédex entry into pages.** "Break at the gaps" gives you one enormous
  page for Exploud and a tidy one for Pikachu. "Break every N letters" cuts a word in half.
  Break on punctuation and line structure instead, and go and look at what came out.
* 📏 **Any rule that counts words.** *Reject reports over 200 words. Average words per battle.
  Trim to the first 50 words.* Every one of those does something different — and silently
  different — in a region with no gaps.
* 🖥️ **Where the text wraps on the Pokédex screen.** A Rotom Pokédex that only breaks lines at
  gaps renders the whole Sealed Chamber inscription as one line running off the edge of the
  screen, with Registeel's instructions somewhere past the right-hand margin.
