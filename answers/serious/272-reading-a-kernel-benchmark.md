---
id: "272"
slug: reading-a-kernel-benchmark
style: serious
category: optimization
difficulty: intermediate
question: "Someone shows you a kernel benchmark with a 12x speedup. What do you check before you believe it?"
tags: [benchmarks, warm-up, autotuning, determinism, scepticism]
---

# A kernel multiplier is a ratio, and almost nobody states the denominator.

[212](212-reading-model-announcements.md) sorts model claims into four tiers before arguing with
them. Kernel claims take the same treatment, and they sort *better*, because the benchmark script
is usually in the repository. Most of what follows is checkable in ten minutes with `git clone`,
which puts it in tier one — and almost nobody does it.

```
  ┌────────────────────┬────────────────────────────────────────────────────────┐
  │ 1. CHECKABLE NOW   │ What is the baseline class? What shape? Autotune on?   │
  │    (ten minutes)   │ Is warm-up excluded? Read benchmark/*.py. Never argue. │
  ├────────────────────┼────────────────────────────────────────────────────────┤
  │ 2. CHECKABLE WITH  │ Re-run it. Needs the same GPU, the same torch and      │
  │    WORK            │ triton, the same autotune budget. Usually reproduces.  │
  ├────────────────────┼────────────────────────────────────────────────────────┤
  │ 3. ONLY ON YOUR    │ "2× faster fine-tuning." "12× faster MoE." Your model, │
  │    OWN TRAFFIC     │ your shapes, your batch, your phase mix.               │
  ├────────────────────┼────────────────────────────────────────────────────────┤
  │ 4. NOT CHECKABLE   │ A multiplier with no script, no shape and no baseline. │
  └────────────────────┴────────────────────────────────────────────────────────┘
```

## The eight questions, with evidence for each

**1. Against what, exactly?** Open the benchmark. Unsloth's MoE benchmark runs
`benchmark_fused_moe.py --model qwen3 --mode forward --seqlen 1024 --permute_x --permute_y
--autotune`, and the baseline it constructs is Hugging Face's `Qwen3MoeSparseMoeBlock`. That is a
reference implementation with a Python `for expert_idx in expert_hit:` loop in it. Beating it by
12× is a true statement about a reference loop, not about the best available MoE kernel.

**2. Does the repo itself say the baseline is weak?** The same README: *"The Llama4 reference
layer is still highly under-optimized as there are many low-hanging opportunities."* When the
author tells you the denominator is slow, believe them, and adjust the numerator's fame
accordingly.

**3. Was the *winner* tuned and the loser not — or the other way round?** Also from that README:
*"Running with autotuning turned off with the default manual kernel config will result is
**highly** sub-optimal performance as it is only meant for testing / debugging purposes."* The
same kernel, with and without its autotuner, differs enough that the author warns you in bold. A
comparison is only meaningful if both sides got the same tuning effort, and they almost never do.

**4. Warm-up.** Three independent projects treat first-call cost as a shipping problem:

```
   FlashInfer   compiles or downloads kernels on first use; ships flashinfer-cubin
                and flashinfer-jit-cache wheels plus `install-cubin-wheel` and
                `download-kernels` CLIs purely to avoid it
   vLLM         persists torch.compile artifacts under VLLM_CACHE_ROOT, and offers
                VLLM_FORCE_AOT_LOAD=1 to FAIL LOUDLY rather than silently recompile
   Triton       autotune sweeps configs on first call — the MoE block alone needs
                2 configs for the forward and 4 for the backward
```

A microbenchmark that includes the first call measures a compiler. One that excludes it and does
not say how many iterations it warmed for is unreadable either way. The convention to look for is
the explicit one — the maximum-achievable-matmul numbers in
[stas00/ml-engineering](https://github.com/stas00/ml-engineering) state "a mean of 100 iterations
after 50 warmup iterations", and that sentence is what makes the table usable.

**5. Shape — and this is the biggest one.** The same source's measured H100 BF16 peak of 794.5
TFLOP/s comes from `2048x2048x13312`, found by what it openly calls "a brute-force search of a
non-exhaustive sub-space of various shapes". No layer in any transformer has that shape. Worse,
shape can choose the *regime*: from [271](271-training-kernels-and-fusion.md), a grouped MoE
GEMM's arithmetic intensity is exactly the average tokens per expert, so

```
   seqlen 1024 → 64 tokens/expert  → far below the ridge → memory-bound → fusion wins big
   seqlen 8192 → 512 tokens/expert → above the ridge     → compute-bound → fusion wins little
```

The benchmark's `--seqlen 1024` is the regime where the result is largest. That is not fraud. It
is a choice, made by everyone, and it is why you re-run at your own sequence length.

**6. Which phase?** [268](268-roofline-decode-and-prefill.md): prefill sits 29× above the ridge
point and decode at batch 1 sits 261× below it. A bytes optimisation is transformative on one and
invisible on the other. "2× faster attention" with no phase named is not a result.

**7. Was the launch overhead in or out?** A decode kernel timed at batch 1 in a Python loop
without CUDA graphs is substantially measuring Python. Turn graphs on
([270](270-serving-stack-around-the-kernel.md)) and the per-launch cost the new kernel was
"saving" disappears from both sides, and the margin with it.

**8. Did the output change?** Fused and split-reduction kernels are reduction-order dependent, and
two separate projects ship switches that say so:

```
   FlashInfer plan(): fixed_split_size … "will lead to deterministic softmax score
     reduction in the merge_states kernel, and therefore batch-size invariant outputs"
     disable_split_kv … "for determinism in CUDA Graph"

   Unsloth MoE README, TODO: "TMA store: implemented but not enabled currently due to
     non-determinism arising from triton pipelining bug"
```

Read the first one carefully: **by default, the answer depends on the batch size.** Not
catastrophically — a last-bit difference in a softmax denominator — but enough that a greedy
decode can diverge on a long generation, and enough that "we changed nothing but the kernel" is
not quite true.

## The trap that catches good engineers

**Bundled claims.** Unsloth's own release note reads: *"New RoPE & MLP Triton Kernels & Padding
Free + Packing: 3× faster training & 30% less VRAM."* Everything in it is true. But padding-free
packing is a **data** change, not a kernel change — if your batches were half padding, removing
the padding is most of a 2× on its own and would be there with no Triton at all. Two
interventions, one number. The same applies to any "70% less VRAM" that silently includes gradient
checkpointing, which trades about a third more compute for the memory and is older than every
library in this arc.

## What to do instead

Write the measurement before you read the claim. Fix a token budget, not a wall-clock budget. Run
your own shapes, your own phase mix, your own batch distribution, warm up explicitly and say how
much, and report **tokens per second and p99 inter-token latency together** — a kernel that wins
throughput by degrading tail latency has not won. Then diff the logits against the old path on a
fixed prompt set, so that question 8 has an answer rather than a shrug. An afternoon of that
converts every future kernel release from an argument into a measurement.

## Where this stands, September 2026

Every quotation above is primary: I read them in the repositories, not in coverage of them. The
specific flags, wheel names and TODO lines will move — check the version you have pinned.

The durable part is the shape of the error, and it is not dishonesty. **A kernel benchmark is a
ratio between two configurations, and the author controls both.** Every knob in this answer —
baseline choice, tuning budget, warm-up, shape, phase, launch overhead, tolerance — has a
defensible setting that makes the number larger, and a defensible setting that makes it smaller.
Nobody has to lie for a 12× and a 1.2× to describe the same kernel. The only defence that has ever
worked is measuring the thing you are actually going to run, and the only reason not to is that
you have not written the harness yet.

## What an interviewer digs into next

* Name three ways to make an honest kernel benchmark twice as impressive.
* Why can the same MoE kernel be a 12× win and a 1.3× win on the same GPU?
* Two kernels, identical maths. Why might greedy decoding diverge between them?
