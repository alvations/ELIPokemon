---
id: "255"
slug: tree-drafting-and-verification
style: serious
category: optimization
difficulty: advanced
question: "What does verifying a tree of candidates instead of a single chain buy you?"
tags: [speculative-decoding, tree-attention, medusa, eagle, acceptance-rate]
---

# It buys depth: a chain dies at the first token the drafter gets wrong, and a tree does not.

A chain draft commits to one continuation, so the expected accepted length is `Σ α^i` and it
collapses as soon as `α` sags. A tree draft offers `k` candidates at each position and verifies
all of them in the **same** forward pass, using an attention mask that lets every node see only
its own ancestors. The per-position acceptance is no longer the probability that the drafter's top
guess is right; it is the probability that the target's token is **anywhere in the offered set** —
the top-`k` mass. That is a much larger number, and it compounds over depth in your favour instead
of against you.

The cost is that the tree's nodes all ride in the token dimension of the verification pass, which
is precisely the resource that [256](256-speculative-decoding-at-high-batch.md) shows you run out
of. Tree width is the cleanest way to convert spare compute into accepted tokens, and it is
worthless once there is no spare compute.

## The mask is the whole trick

```
   chain draft, γ = 3                 tree draft, k = 2 at each of 3 depths
   ──────────────────                 ────────────────────────────────────
   [prefix] A  B  C                                  [prefix]
                                                     /        \
   one continuation                                A            D
   4 tokens in the pass                          /   \        /   \
                                                B     E      F     G
                                               / \   / \    / \   / \
                                              C   H I   J  K   L M   N

                                     14 tree tokens in ONE forward pass

   attention mask over the tree tokens (1 = may attend)

           pfx  A  D  B  E  F  G  C  H ...
      A     1   1  .  .  .  .  .  .  .       every node attends to the prefix
      D     1   .  1  .  .  .  .  .  .       and to its own ancestors only
      B     1   1  .  1  .  .  .  .  .
      E     1   1  .  .  1  .  .  .  .       B and E share ancestor A
      F     1   .  1  .  .  1  .  .  .       F and G share ancestor D
      C     1   1  .  1  .  .  .  1  .       position_id = depth, not index
```

Two things follow from that picture. The mask is `T × T` for `T` tree tokens, so the attention
backend has to accept an arbitrary mask rather than a plain causal one — this is why tree support
is a kernel feature, not a scheduler feature. And `position_ids` are the node's **depth**, not its
index in the flattened buffer, or RoPE puts sibling branches at different distances from the
prefix.

## The arithmetic, and why full trees are impossible

Expected accepted length is a sum over nodes of the probability that the target's own continuation
follows that node's path:

```
   E[accepted]  =  Σ          P(path to v)          root excluded
                  v ∈ tree
```

Take a genuinely heavy-tailed next-token distribution — twelve outcomes with mass `20 20 10 10 10
10 5 5 4 4 1 1` percent. Its top-`k` coverage is `20, 40, 60, 80, 90, 98, 100` at `k = 1, 2, 4, 6,
8, 10, 12`. Now price a full `k`-ary tree of depth 4:

```
    k   top-k coverage   full-tree nodes   E[accepted]        note
   ──────────────────────────────────────────────────────────────────────────────
    1       0.20                 4            0.250     this is the chain
    2       0.40                30            0.650
    4       0.60               340            1.306
    6       0.80             1,554            2.362
    8       0.90             4,680            3.095
   10       0.98            11,110            3.804
   12       1.00            22,620            4.000     accept everything, always
   ──────────────────────────────────────────────────────────────────────────────
```

Twelve times the accepted length for five thousand times the tokens per pass. Nobody can pay that,
which is why every real system **prunes**: keep the highest-path-probability nodes until a fixed
node budget is spent. Doing that greedily on the same distribution:

```
   node budget      4      8     16     32     64    128    256
   E[accepted]   0.600  0.900  1.180  1.480  1.784  2.088  2.394
```

Read the first column against the chain's 0.250. With exactly four tree tokens — the same four the
chain used — the pruned tree scores 0.600, because it spends all four on **width at depth 1**
rather than depth it will never reach. That is the single most counter-intuitive result here, and
it is why static tree shapes are broad at the top and narrow at the bottom.

Now the same exercise on a *narrow* distribution — two outcomes at 60/40, which is what
schema-constrained output and repetitive code actually look like:

```
   node budget      4      8     16     32     64
   E[accepted]   1.600  2.360  3.238  4.000  4.000      chain would give 1.306
```

It saturates at 32 nodes: a complete binary tree of depth 4 is 30 nodes, coverage is 1.0 at every
depth, and you accept the entire draft every single time. The width you should buy is set by the
tail of your token distribution, and it differs by endpoint by an order of magnitude.

## Verifying a tree without losing exactness

Greedily this is easy: walk from the root, and at each depth keep the child that equals the
target's argmax. With sampling it needs care, because "accept whichever child matches" is not the
rule from [253](253-speculative-decoding-exactness.md). The SpecInfer-style ([Miao et
al.](https://arxiv.org/abs/2305.09781)) multi-round version is: try child 1 with `min(1, p/q₁)`;
on rejection, subtract what child 1 already accounted for, renormalise, and try child 2 against
the residual; continue; if all `k` fail, sample from what is left. The result is still exactly
`p`. Medusa's *typical acceptance* is the shortcut that does not preserve it — worth knowing which
one your stack runs before you quote the exactness guarantee.

## What the serving stacks actually do

Read these from the trees rather than the papers, because the gap is large. SGLang builds an
explicit candidate tree: `build_tree_kernel_efficient`, a `speculative_eagle_topk` width, and a
`TreeMaskMode` with a `FULL_MASK` setting (primary). Its adaptive controller, which tunes the
number of draft steps at runtime from observed acceptance lengths, **refuses to run unless
`speculative_eagle_topk == 1`** — that is, tree drafting and adaptive depth are currently mutually
exclusive there, and you pick one (primary). vLLM's V1 path is chain-first; its EAGLE proposer
carries a literal `FIXME: when using tree-based specdec, adjust number of forward-passes according
to the depth of the tree`, and its `use_local_argmax_reduction` optimisation is documented as
applying only to "non-tree speculation" (primary). Trees are well established in the literature
and unevenly established in production.

## What an interviewer digs into next

* Why does a four-node tree beat a four-token chain, and what does that say about tree shape?
* Why must position ids be tree depth?
* How do you verify a tree without breaking the distributional guarantee?

## Where this stands, September 2026

The arithmetic is durable — `E[accepted] = Σ P(path)`, the collapse of full trees under
exponentiation, and the fact that optimal width tracks the tail of the token distribution will
survive every framework in this answer. The framework details are a September 2026 snapshot read
first-hand from the SGLang and vLLM repositories, and the constraint that adaptive depth excludes
tree width is exactly the kind of thing that gets fixed in a point release. Re-read those two
files before you plan around either. The SpecInfer multi-round verification description is
coverage.

**Citation note.** The arXiv identifiers linked above are given from working knowledge.
`arxiv.org` is blocked from the environment this was written in, so **not one of them was resolved
while writing**. Resolve every identifier before you cite it.
