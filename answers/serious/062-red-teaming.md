---
id: "062"
slug: red-teaming
style: serious
category: safety
difficulty: intermediate
question: "What is red teaming for LLMs, and how do you do it systematically?"
tags: [red-teaming, adversarial-testing, automated-red-teaming, coverage]
---

# Red teaming

Adversarially probing a system to find failures **before** users or attackers do. Distinct from
evaluation: evaluation measures typical performance on a representative distribution; red teaming
searches for worst cases, and is explicitly not representative.

## Doing it systematically

Ad-hoc "let's try to break it" produces a scattered list of the same few jailbreaks. A systematic
programme has four parts.

**1. A threat model.** Who is attacking, with what capability and motive?

| Actor | Capability | Motive |
| --- | --- | --- |
| Curious user | prompting only | fun, boundary-testing |
| Motivated individual | published jailbreaks, persistence | specific content |
| Third party via content | indirect injection | exfiltration, action hijacking |
| Sophisticated attacker | automated search, model access | scale, systematic extraction |

Different actors need different defences. Systems built only against actor 1 fail against actor 3.

**2. A taxonomy of harms**, so you can measure coverage rather than counting anecdotes. Typically:
content harms (violence, CSAM, weapons, self-harm), factual harm (medical, legal, financial advice),
privacy (PII extraction, training-data memorisation), security (injection, tool misuse, exfiltration),
integrity (bias, manipulation), and product-specific harms — for a support bot, promising a refund
that policy forbids.

**3. Methods.**

```
   MANUAL                   AUTOMATED                 HYBRID
   ──────                   ─────────                 ──────
   experts probe by hand    a red-team LLM generates  humans find a novel
   ✅ creative, finds novel  thousands of attacks      class; automation
      classes               ✅ scale, reproducible,    expands and regresses
   ❌ slow, doesn't scale       regression-testable    it. The pattern that
   ❌ coverage is uneven     ❌ tends to rediscover     works.
                               known classes
```

Also: **domain experts** (a chemist finds failures a generalist cannot evaluate), **crowdsourcing**
for breadth, and **bug bounties** for adversarial diversity you cannot hire.

**4. A feedback loop.** Findings must become: a fixed behaviour, a regression test in a permanent
suite, and a class-level generalisation. Fixing one prompt and moving on is the classic failure —
attackers vary phrasing, so you need to fix the *class*.

## Metrics

* **Attack success rate** per harm category, tracked over releases.
* **Attack cost** — attempts needed to succeed. A jailbreak needing 200 attempts is meaningfully
  different from one needing 2, even at the same eventual success rate.
* **Coverage** — categories probed vs categories in the taxonomy. Guards against measuring only
  where you looked.
* **Time to discovery** for a newly introduced flaw.
* **Over-refusal**, always reported alongside — a red team optimising only for fewer successful
  attacks will drive the system into refusing everything.

## Practical notes

* **Red team the whole system, not the model.** Failures live in retrieval, tool permissions, and
  orchestration at least as often as in the model.
* **Test multi-turn.** Most real attacks are gradual escalation; single-turn testing misses them
  entirely.
* **Rotate the team.** Fresh people find different things; a stale team converges on its own habits.
* **Protect the red teamers.** Sustained exposure to harmful content has real psychological cost —
  rotation, support, and limits are an ethical requirement, and are also why automation matters
  beyond throughput.

## What an interviewer digs into next

* How is red teaming different from evaluation?
* Why is attack *cost* a better metric than a binary "was it broken"?
* How do you generalise from one successful attack to a class?
* How would you red team a RAG system specifically?
