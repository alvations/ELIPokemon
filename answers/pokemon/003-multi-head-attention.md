---
id: "003"
slug: multi-head-attention
style: pokemon
category: transformers
difficulty: core
question: "What is multi-head attention and why use more than one head?"
tags: [attention, multi-head, subspaces, induction-heads]
---

# Multi-head attention, or: the coaching box at Nationals

One head of attention is a Trainer who only knows the type chart — Electric beats Water, done. Good! Better than nothing!
Also completely exploitable, because a Sturdy Golem or a Focus Sash will ruin their day and
they will never see it coming.

Multi-head attention is the **coaching box**: several specialists watching the same battle at
the same time, each one paid to notice a different thing, all whispering at once.

## The box

```
                        THE BATTLE (one field, everyone sees it)
                                     │
   ┌──────────┬──────────┬───────────┼───────────┬──────────┬──────────┐
   ▼          ▼          ▼           ▼           ▼          ▼          ▼
 🧪 TYPE    🛡️ ABILITY  🌧️ WEATHER  🎽 ITEM    📊 STATS   🧠 MEMORY  😴 BENCH
 EXPERT     SCOUT      TRACKER     WATCHER    ANALYST    KEEPER     WARMER

 "Water/    "That may   "Rain is    "Focus     "It's at   "They led  "...nothing
  Flying,    have        up — Thunder Sash, it   +2 Speed  with this  to report,
  hit it"    Sturdy"     can't miss"  survives"  already"  last game" boss"
   │          │           │            │           │          │          │
   └──────────┴──────────┴───────────┬┴───────────┴──────────┴──────────┘
                                     ▼
                            HEAD COACH combines it all
                                     ▼
                              ONE decision this turn
```

Every coach watches the *whole* field. Every coach ranks the field differently. The head coach
(that's the output projection `W_O`) listens to all of them simultaneously and makes a single
call.

## Why not just hire one really good coach?

Because a coach speaks in exactly one ranking. "Gyarados 90%, Golem 10%" is *one* opinion. It
cannot also say "but watch Golem's ability" — that would be a different ranking, and a coach
only gets one voice per turn.

If you want to track type advantage **and** abilities **and** weather **and** items, you need
that many coaches. This is the entire argument.

## The catch: the budget is fixed 💰

You don't get to hire eight coaches at full salary. You have a fixed budget and you **split**
it. Eight coaches means each one is a part-timer who only ever looks at their one narrow
thing. That's fine — a specialist who only watches the weather is genuinely useful.

But split too far and you get 64 interns who each know one fact and can barely form an
opinion. The sweet spot is enough coaches to cover the important angles, each still competent
enough to actually read the field.

## The coaches nobody assigned 🎭

Nobody sat down and handed out job titles. You hired eight people, sat them in the box, and
they *organically* divided the work — because two coaches shouting the same thing is wasted
salary and the ones who found an unwatched angle became indispensable.

A few types show up in every coaching box ever assembled:

* 👈 **The "who went last?" coach** — just tracks the previous switch. Boring, load-bearing.
* 🔁 **The Battle Memory coach** — *"They pulled this exact lead in game one, and followed it
  with Trick Room. Expect Trick Room."* This one is the reason a Trainer can adapt mid-set
  without ever having trained against this specific team.
* 😐 **The bench warmer** — genuinely has nothing to say most turns, so it stares at the
  scoreboard. Every box has one. It turns out the *option* to say nothing is itself useful,
  because someone has to absorb the pressure when nothing interesting is happening.

## The bill comes at tournament time 💸

Every coach keeps their own notebook on every Pokémon that has appeared. Eight coaches, six
Pokémon, ten turns — that's a filing cabinet, and lugging it between rounds is slower than
the actual thinking.

So the modern move is: keep all eight coaches (you want the *opinions*), but have them
**share one set of notebooks** instead of each keeping their own. Same tactical coverage,
a fraction of the luggage.
