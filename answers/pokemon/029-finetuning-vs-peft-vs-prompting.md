---
id: "029"
slug: finetuning-vs-peft-vs-prompting
style: pokemon
category: fine-tuning
difficulty: core
question: "When would you choose full fine-tuning vs PEFT vs prompting?"
tags: [fine-tuning, peft, prompting, rag, decision-framework]
---

# Four ways to fix a Pokémon, cheapest first

Your Pokémon isn't doing what you want. There's a ladder of fixes, and **most people climb too far
up it**.

```
  🗣️ 1. JUST TELL IT             seconds, free
        "Lead with Ferrothorn. Never switch it into Earthquake."
        ✅ instant  ✅ change your mind anytime  ✅ works on any Pokémon
        ❌ you must say it every single battle

  📋 2. HAND IT A SCOUTING REPORT   hours, cheap
        "Misty leads Starmie; her Politoed has Drizzle."
        ✅ updates in seconds  ✅ you can check where a fact came from
        ❌ now your scouting is the weak link

  🎒 3. GIVE IT A HELD ITEM        days, moderate
        Clip on a Mystic Water and train just that.
        ✅ cheap  ✅ swappable  ✅ Champion underneath is safe
        ❌ needs real training data

  🏕️ 4. SEND IT TO CAMP           weeks, expensive
        Rebuild the Pokémon.
        ✅ can change anything  ❌ it may come back having forgotten
        ❌ one whole Pokémon per specialism
```

## The one question that decides it ❓

**What's actually missing?**

| The problem | The fix |
| --- | --- |
| 📚 It doesn't **know** Toxapex got a new ability | Scouting report. **Never camp.** |
| 📐 It **formats** wrong | Just tell it. Item if you're repeating yourself constantly. |
| 🎭 Its **style/tone** is off | Mystic Water. This is precisely what items are for. |
| 🤷 It **can't do the task at all** | Item with real data — or get a better Pokémon. |
| 🌏 It needs a **whole new type** | Camp. Genuinely. |
| 💸 It's too **slow or expensive** | Train a *small* Pokémon to copy your big one. |

## The mistake everyone makes 🚨

Row one. It is *always* row one.

> *"Our Pokémon doesn't know Misty runs Politoed now. Let's send it to camp for a month."*

Here's what you get back. It still doesn't reliably know your roster — a month of camp is not how
facts stick. What it *has* learned is that **when asked about your Gym, one answers immediately
and with total confidence.**

You have trained a bluffer. Worse than before, because now it's wrong *confidently*, and you can't
tell when. And your roster changed last Tuesday anyway, so the whole month is stale.

**Facts go in the scouting report.** Every time.

## When camp is actually right 🏕️

**💰 You're repeating yourself constantly.** If you preface every single battle with the same
three-page briefing, and you battle ten million times a day, bake it in. Saying it once is free;
saying it ten million times is not.

**📐 You need format reliability.** Getting a Pokémon to produce *exactly* the right output shape
99.9% of the time is often easier with a thousand examples than with any amount of instruction.

**🐣 Shrinking a Champion.** The best use of training there is: have your expensive Cynthia-grade
Trainer play ten thousand battles, then train a **cheap little Pokémon to imitate it**. Ten times
cheaper, ten
times faster, nearly as good on your specific job. Highest return on effort in the whole game.

**🎨 Things you can't put into words.** House style. Domain judgement. The way *your* Gym does
things. Some behaviour is much easier to *demonstrate* than to *describe*, and that's exactly what
training is for.

## The order to do it in 📋

1. **🎯 Build your test battles first.** Before anything else. Without them you cannot tell whether
   any fix helped — you'll just have vibes and a bill.
2. **🗣️ Try telling it.** Measure.
3. **📋 Add a scouting report** if the gap is knowledge. Measure.
4. **🎒 Now** consider an item — and use your instruction-tuned version to *generate the training
   examples*.
5. **🏕️ Camp** only with a real reason and real data.

The classic expensive failure is jumping from step 1 straight to step 5, with no test battles, to
fix something that was a **scouting** problem all along.
