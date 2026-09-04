---
id: "100"
slug: fairness-bias-privacy
style: pokemon
category: responsible-ai
difficulty: intermediate
question: "How do you think about fairness, bias, and privacy in an ML system?"
tags: [fairness, bias, privacy, differential-privacy, impossibility, memorisation]
---

# Fairness and privacy: judging Trainers, and keeping their secrets

You've built a system that predicts **which Trainers will make it to the Indigo Plateau.** Gyms use
it to decide who gets sponsorship.

You need it to be **fair.** Which sounds simple, and is the hardest thing on this page.

## "Fair" means at least five incompatible things ⚖️

| What "fair" could mean | What it demands |
| --- | --- |
| 🎯 **Equal sponsorship rates** | The same *proportion* from Kanto, Johto, Hoenn and Alola. |
| ✅ **Equal chances for the good ones** | A Trainer who *would* make it is equally likely to be spotted, wherever they're from. |
| ❌ **Equal error rates** | Wrongly rejecting equally often across regions. |
| 📊 **Honest numbers** | "70% likely" means 70% for a Kanto Trainer *and* a Johto Trainer. |
| 👥 **Similar Trainers, similar treatment** | Two comparable Trainers get comparable scores. |

**Now the part that matters:**

> 🚨 **These are mathematically impossible to satisfy at once.**

Not "hard." Not "expensive." **Proven impossible** — unless every region has an identical underlying
success rate, or your system is literally perfect. Neither will ever be true.

📌 So *"make it fair"* is **not a well-posed request.** Somebody has to choose **which** fairness you
mean, and that is a decision about **values**, not a decision about code.

There was a famous public argument where one side said a system was unfair (unequal wrong-rejection
rates) and the other said it was fair (honest numbers). **Both were correct.** They were measuring
different things, and no amount of engineering reconciles them.

The right move is to ask: **what does a mistake actually cost here?**

* 💼 **Wrongly denied sponsorship** → a career that never happens.
* 🏥 **Wrongly flagged for a health check** → an inconvenient afternoon.

Different harms. Different fairness. Choose deliberately, write down why.

## Where the unfairness gets in 🕳️

```
   1️⃣ 📜 HISTORY   Kanto has had more Champions — because Kanto has
                    had Brock, Misty and eight funded Gyms for fifty
                    years. Your data records this faithfully.

   2️⃣ 📊 SAMPLING  You have ten thousand Kanto records and two
                    hundred from Alola.

   3️⃣ 🏷️ LABELS    You're predicting "made it to the League" — but
                    that's really "got through a system that already
                    favoured Kanto."

   4️⃣ 🔍 PROXIES   You removed "region." But you kept hometown, whether
                    their starter was Bulbasaur or Rowlet, and which
                    academy they attended.
                    You removed the label, not the information.

   5️⃣ ⚖️ TRAINING  Optimising overall accuracy means happily being
                    terrible for Alola — it's 2% of your data.

   6️⃣ 🚪 USE       The threshold, who gets seen, and the feedback loop.
```

**📌 Deleting "region" does NOT fix this.**

Two reasons. The proxies remain — hometown alone reconstructs it. And worse: **you've destroyed your
ability to check.** You can no longer measure whether you're being unfair to Alola, because you threw
away the field that would tell you.

📌 You usually need the attribute **to audit**, even when the model doesn't use it.

## Privacy: your Trainer memorises things 🔐

This is not theoretical. **Trainers reproduce their training footage verbatim.**

Show a Trainer someone's private team sheet enough times and it will recite it back to a stranger who
asks the right question.

**The single biggest fix is the dullest: 🗑️ remove duplicates.**

Things that appear **once** get blurred into general knowledge. Things that appear **five hundred
times** get memorised word for word. Deduplicating your footage:

* ✅ dramatically reduces memorisation, **and**
* ✅ makes the Trainer better anyway.

Highest-value privacy work there is, and it's tidying.

**🎲 The rigorous version: add deliberate noise.**

Train in a way where **any single Trainer's data could be removed and the result would look
essentially the same.** That's a real, provable guarantee — nobody can determine whether a specific
Trainer was in your footage, because their presence genuinely didn't change anything.

⚠️ And it **costs accuracy.** Genuinely. Turn the guarantee up and quality goes down.

📌 And here's the uncomfortable interaction between this page's two halves: **the noise hurts
under-represented groups most.** Alola has two hundred records; drown them in noise and there's
nothing left. Your privacy protection just made your fairness problem worse.

## The practice that matters most 📊

Above every technique on this page:

> **Report your numbers broken down by group. Never in aggregate.**

```
   😊 "Overall accuracy: 91%."          ← tells you nothing
   😰 "Kanto: 94%. Johto: 92%.
       Alola: 61%."                      ← THERE it is
```

The aggregate is where every failure hides, because the under-represented group is by definition too
small to move it.

**Break it down. Publish it. Look at it.** That one habit catches more real harm than every clever
technique combined.
