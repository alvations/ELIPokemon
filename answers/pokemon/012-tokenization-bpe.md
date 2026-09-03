---
id: "012"
slug: tokenization-bpe
style: pokemon
category: nlp
difficulty: core
question: "What is tokenization? Explain BPE and why token boundaries cause weird model behaviour."
tags: [tokenization, bpe, sentencepiece, vocabulary, unicode]
---

# Tokenization is how you write Pokémon names on a scoreboard

Your stadium scoreboard has a limited set of tiles, and every Pokémon name has to be spelled out
of them. What tiles do you stock?

## The two bad answers 🎫

**One tile per letter.** A–Z, 26 tiles, done. Any Pokémon, any language, any nickname spells
fine. But `CHARIZARD` eats nine tiles, a full team eats sixty, and the scoreboard operator is
exhausted before the match starts.

**One tile per Pokémon.** `[CHARIZARD]` — one tile, instant. Beautiful, until a challenger shows
up with a Charizard nicknamed **"Big Steve"** and you have no tile for it. You put up `[???]`
and the crowd has no idea what's happening.

## The real answer: tiles for common chunks 🧩

Stock tiles for whatever shows up a lot.

`[CHAR]` `[IZARD]` `[SAUR]` `[MON]` `[ITE]` `[MEGA]` `[▁a]` `[▁the]` `[ing]` — plus every single
letter as a backstop, so **nothing is ever unspellable**.

Now `CHARIZARD` is `[CHAR][IZARD]` — two tiles. `BULBASAUR` is `[BULBA][SAUR]`. And "Big Steve"
is `[Big][▁Ste][ve]`, which is clumsy but *works*, because you kept the letters around.

## How you pick the tiles: BPE 🔨

You don't guess. You read a giant pile of Pokémon text and merge greedily:

```
  Start with letters only.
  Then repeatedly: find the most common adjacent pair, and fuse it into a new tile.

  round 1:  "s"+"a" appears constantly  →  make [sa]
  round 2:  [sa]+"u"                    →  make [sau]
  round 3:  [sau]+"r"                   →  make [saur]     ← BULBASAUR, IVYSAUR, VENUSAUR
  round 4:  "c"+"h"                     →  make [ch]
  round 5:  [ch]+"a"                    →  make [cha]
  ...
  stop at 50,000 tiles.
```

Frequent things end up as single tiles. Rare things stay as fragments. The merge list is
**ordered**, and you replay it in that exact order every time — which is why the same name always
spells identically.

## Why your Trainer is strangely bad at some things 🤔

This one design choice explains almost every embarrassing model failure.

**"How many R's in CHARIZARD?"** 🅁
Your Trainer never saw letters. They saw `[CHAR][IZARD]` — two tiles. Asking them to count R's is
like asking someone who reads Chinese characters how many strokes are in a word they only ever
recognised as a whole shape. They'll guess. They'll be wrong. It is *not* a reasoning failure.

**Adding up damage numbers** 🔢
`1234` might be tiled as `[12][34]` in one place and `[1][234]` in another. The columns don't
line up, so carrying is a nightmare. Models that tile digits one at a time do noticeably better
arithmetic — same brain, better scoreboard.

**Spelling names backwards** — same problem as counting.

**The trailing space trap** ␣
`[Pikachu]` and `[▁Pikachu]` (with the leading space) are **different tiles**. End your prompt
with a stray space and you've handed the Trainer a tile they almost never see in that position.
They get visibly worse for no reason you can see. This is why battle formats are so fussy about
exact spacing.

**Cursed tiles** 👻
Somewhere in the tile set is `[SolidGoldMagikarp]` — it made the cut when counting tiles, but the
Trainer then barely encountered it in actual training. It's a tile with **nothing behind it**.
Play it and the Trainer starts babbling. Every large tile set has a few of these haunted tiles.

**The language tax** 🌏
The tile set was chosen from mostly-English text. So `[Pikachu]` is one tile, but the same name
in Thai or Hindi might take six, because no common chunks were ever learned for those scripts.
Those Trainers pay several times more per sentence — more time, more cost, less room on the
board. That's a real unfairness baked into the tile set, not a quirk.

## Two rules to remember 📌

1. **You can never restock the tiles mid-career.** Change the tile set and every Pokémon's name
   means something different — you'd have to retrain the Trainer from the ground up.
2. **You're billed in tiles, not words.** Code, JSON and non-English text all spell out much
   longer than plain English prose, and cost accordingly.
