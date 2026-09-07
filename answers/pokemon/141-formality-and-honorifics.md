---
id: "141"
slug: formality-and-honorifics
style: pokemon
category: translation
difficulty: intermediate
question: "How do you control formality and honorifics in translation?"
tags: [formality, keigo, t-v-distinction, register, control-tokens, cocoa-mt]
---

# Every Trainer Class speaks differently, and the game tells you which one is talking

**Youngster Joey** rings you up to announce that his **Rattata** is in the top percentage of
Rattata. A **Gentleman** does not talk like that. Neither does an **Ace Trainer**, or a **Hiker**,
or **Nurse Joy**, or **Lance**.

The games are unusually explicit about this: the Trainer Class is printed **before** the battle
starts. You are told what register you are about to receive.

Most languages work the same way, except the marking is on **every single sentence** — and the
language you are translating *from* very often does not mark it at all.

## What has to be decided 🎩

| Where | What gets marked | What wrong sounds like |
| --- | --- | --- |
| 🇫🇷🇩🇪🇷🇺 Much of Europe | two ways to say "you" | insulting, or absurdly stiff |
| 🇯🇵 Japan | three separate axes of politeness at once | rude, or comically grovelling |
| 🇰🇷 Korea | several speech levels, plus respectful verb endings | socially unreadable |
| 🇮🇳🇹🇭 South and South-East Asia | respect built into pronouns and verbs | the wrong relationship implied |

📌 These are not decoration. In several of these, choosing the level is a **claim about the
relationship** between the two people, and every verb in the sentence repeats the claim.

## The source does not say 🤷

```
   what you are handed:  "Can you send me the badge case?"
                                    │
        ┌───────────────────────────┼───────────────────────────┐
   as Youngster Joey          as an Ace Trainer          as a Gentleman
   would say it               would say it               would say it

   all three are correct translations.
   exactly one is right for your situation.
   and NOTHING in the sentence tells you which.
```

So the machine guesses — and it guesses by habit, which means whatever it read the most of.
Trained mostly on League paperwork, everything comes out sounding like Lance addressing the Elite
Four. Trained mostly on route chatter, your legal notice comes out sounding like Youngster Joey.

⚠️ **There is no neutral setting.** Declining to choose is not neutrality; it is choosing by
accident and blaming the dice.

## How to actually control it 🎚️

* **🏷️ Stamp the Trainer Class on the front.** Mark every training example with its register and
  mark the request the same way. The classic approach, and it works — you need the archive labelled.
* **💬 Or just tell it.** *"Speak as a Gentleman would."* Works well, and ⚠️ **it drifts** — check
  entry two hundred, not entry one.
* **💿 Or keep a disc per register** (question 134) and swap.
* **✍️ Or translate first and restyle afterwards.** Costs an extra pass, and buys you one
  translation you can re-render at any politeness level you like.

And whichever you pick: **decide once for the whole document and hold it** (question 131). A letter
that opens as a Gentleman and closes as Youngster Joey reads as either careless or as somebody
deliberately changing their mind about you halfway down the page. Neither was intended.

## You already know the answer. Pass it along. 📮

Here is the part that gets skipped.

The right register depends on **who is speaking to whom, and in what setting** — a Gym Leader
addressing a challenger, a shop clerk in **Celadon Department Store**, a rival at the gate. Your
system nearly always knows this *before* translation starts. It is right there in whatever produced
the message.

📌 **Pass it in.** Working out the register by squinting at the sentence is guessing at something
you were already holding.

## Measuring it 🏅

* 🎯 **Hand it the same line and ask for each register in turn**, then check which one came back.
  This is the right instrument, and for exactly the reason from question 131: **the general quality
  score cannot see politeness at all.** A machine that gets *every single* register choice wrong
  loses almost nothing on it.
* 🔄 **Count the flips within one document.**
* 📉 **And test compliance at the end, not the start.** Ask for the register at line one and check
  it at line two hundred. Instructions fade, the average over the document hides it, and the last
  page is the one somebody signs.
