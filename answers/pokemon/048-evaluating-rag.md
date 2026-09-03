---
id: "048"
slug: evaluating-rag
style: pokemon
category: rag
difficulty: intermediate
question: "How do you evaluate a RAG system?"
tags: [rag-evaluation, recall, faithfulness, ragas, component-eval]
---

# Was it the scout or the Trainer?

Your Pokédex system gave a bad answer. **Whose fault?**

```
   ❓ question ──► 🔍 SCOUT ──► 📄 reports ──► 🧠 TRAINER ──► 💬 answer
                      │                            │              │
                "did you fetch          "did you actually    "was the
                 the right one?"         READ them?"          answer right?"
```

Three completely different failures, and they need three completely different fixes:

* 🔍 The scout fetched the **wrong reports**.
* 🧠 The scout fetched the right ones and the Trainer **ignored them**.
* 💬 Both did their job and the answer is still wrong.

📌 If you only measure the final answer, you know something's broken and **nothing about what.**
Teams burn weeks polishing the Trainer's instructions when the scout was never fetching the right
page.

## 🔍 Grading the scout

You need a list: *"for this question, report #47 is the right one."*

**Was the right report in the fetched pile?** ← **the single most important number you have.**

Because it's a **hard ceiling**. If report #47 wasn't fetched, no Trainer alive can use it. Not a
better prompt, not a better model, not a bigger context. It wasn't there.

Also worth tracking: how much **junk** came with it (distractions make the Trainer worse), and
**how high up** the right report ranked — because a thick stack gets skimmed in the middle.

Measure this **before and after the coach's pass**, so you can see which stage is losing things.

## 🧠 Grading the Trainer

Now assume the right reports *were* fetched. Did the Trainer use them?

**📌 Did it stick to the reports?** The RAG-specific question. Break the answer into individual
claims and check each one against the reports. This catches the maddening failure where the scout did
everything right and the Trainer answered from memory anyway.

**🎯 Did it answer the actual question?** It can be perfectly grounded in the reports and still not
address what was asked.

**🔗 Do its citations hold up?** Different from the above! It can say something true and *cite the
wrong page for it*. Check the cited line actually says the thing.

**📊 How many reports did it use?** If you handed over twenty and it used three, you're handing over
too many and diluting its attention.

## 💬 Grading the whole thing

**✅ Was the answer right?** The obvious one.

**🤷 Does it admit when the answer ISN'T in the reports?** — and this is the most under-tested thing
in the entire field.

> Ask something **not in your reports at all.** Watch what happens.

A system scoring 90% on answerable questions and **0% on unanswerable ones** is dangerous, because
it invents an answer every time you stray outside the archive — and you have no idea, because nobody
tested it.

**⏱️ How long and how much**, broken down by stage.

## Building your test set 🛠️

1. 📋 **Use real questions** from real Trainers. Not the ones you imagined. Yours are cleaner,
   better-spelled and more reasonable than anything a real person types.
2. 🌶️ **Deliberately include the nasty ones:** two-part questions, unanswerable ones, ambiguous ones,
   ones needing today's data, ones phrased adversarially.
3. 🏷️ **Label which report is correct — not just the answer.** Without this you cannot measure the
   scout, and the scout is the stage that's usually broken.
4. 🔒 **Freeze it and version it.** Recut your reports and every label needs rechecking, because the
   pages moved.
5. 📊 **Watch a dashboard per stage**, never one number.

## The question that tests whether you get it 🎓

> *"The scout finds the right report 95% of the time, and the answers are still wrong. Now what?"*

It's the scout's job, done. So it's downstream: the Trainer is ignoring the reports, or drowning in
twenty when it needed five, or the right report is buried at position 18 where nobody reads, or the
answer is *in* the reports but split across two pages and neither has it whole.

**Different problem, different fix** — and you only know that because you measured the stages
separately.
