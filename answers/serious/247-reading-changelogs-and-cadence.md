---
id: "247"
slug: reading-changelogs-and-cadence
style: serious
category: open-weights
difficulty: intermediate
question: "How do you read a library's changelog and release cadence to tell a real capability change from a repackaging?"
tags: [semver, changelogs, release-engineering, deepspeed, dependencies]
---

# Read the release script before the release notes. It says what the number may mean.

A version number is only as informative as the scheme behind it, and the scheme is almost never
in the release notes — it is in the repository, usually in twenty lines of shell nobody reads.
DeepSpeed is a good subject because its scheme is unusually legible, so I read it rather than
assuming.

```
   release/release.sh, in order                       what it tells you
   ──────────────────────────────────────────────────────────────────────────────
   1. refuse unless $1 == contents of version.txt  ── the file is the source
   2. check_release_version.py: parse and compare  ──   of truth, not the tag
   3. python -m build --sdist                      ── sdist only
   4. twine upload dist/deepspeed-$1.tar.gz        ── PyPI is the artefact
   5. git tag v$1 ; git push origin v$1            ── the tag comes AFTER
   6. bump_patch_version.py --current_version $1   ──────────────────┐
   ──────────────────────────────────────────────────────────────────┘
        │
        └─ writes f'{major}.{minor}.{micro + 1}'  ← unconditionally

   CONSEQUENCE: the patch number is a COUNTER that advances after every
   release, automatically. A minor bump only happens when a human edits
   version.txt by hand. So the patch digit tells you a release happened.
   It tells you NOTHING about how big it was.
```

And the project sits on `0.x`. Under semver's own text a zero major means anything may change at
any time — so in 132 PyPI releases since `0.3.1.dev1` on 22 October 2020, DeepSpeed has never
made a compatibility promise through its version number. That is not a criticism. It is
information, and it is the opposite of what most dependency policies assume.

## Two patch releases that were not patches

Both of these I read out of the repository, and both are the reason "it's only a patch" is not a
risk assessment.

**0.18.3, 9 December 2025.** Shipped a PyTorch-compatible `backward` API — `loss.backward()`
instead of `engine.backward(loss)`, including non-scalar outputs — and low-precision master
params, gradients and optimizer states, so you can keep everything in bf16 and skip the fp32
copies entirely. A new public API surface *and* a new numerical regime, in a patch.

**0.19.5, 10 August 2026.** Changed `pin_memory` to default **`true`** for both `offload_param`
and `offload_optimizer`, where it had defaulted to `false`. The configuration docs carry the
warning themselves: this can produce out-of-memory errors after upgrading, especially on hosts
with a low `ulimit -l`. A default flip, in a patch, that breaks a job that was working, with
nothing in your own diff to explain it.

## The five diffs, in order of how often they bite

```
   1. CONFIG DEFAULTS       grep the diff for `default=` and for default
                            columns in the config docs. A changed default is
                            a change to code you did not write and did not
                            deploy. This is number one for a reason.

   2. PUBLIC API SURFACE    new kwargs, removed kwargs, renamed modules,
                            anything that was private and is now public
                            (or the reverse — that one is the outage).

   3. THE PRs BEHIND THE    a changelog line is a summary of a diff. The
      HEADLINES             diff is the artefact. Open the two or three PRs
                            the line points at and read the tests.

   4. WHAT CI ACTUALLY      DeepSpeed's README publishes a build matrix:
      COVERS                NVIDIA, AMD MI200, CPU, Gaudi2, Intel XPU,
                            Ascend NPU — and a "contributed hardware" table
                            marking which accelerators are contributor-
                            validated but NOT upstream-validated. If your
                            hardware is in the second column, a green badge
                            is not about you.

   5. DID version.txt MOVE  a re-tag with no version change is a re-cut, not
      AT ALL?               a release. Nothing shipped.
```

**Repackaging versus capability**, stated as a test you can apply mechanically: a repackaging
moves files, renames a module, adds a wheel target, or changes packaging metadata — the set of
reachable behaviours is unchanged. A capability change adds a config key, changes a default, or
changes what an existing number means. If the diff touches a default or a unit, it is a
capability change however the note is phrased.

## Reading the cadence

```
   0.19.0  2026-05-06  ┐
   0.19.1  2026-05-30  │
   0.19.2  2026-06-16  │  seven patch releases in 133 days
   0.19.3  2026-07-23  │  ≈ one every 19 days
   0.19.4  2026-08-06  │
   0.19.5  2026-08-10  │  ← the pin_memory default lives here
   0.19.6  2026-08-27  │
   0.19.7  2026-09-16  ┘  (version.txt on master already reads 0.19.8)

   minors:  0.17.0  2025-06-02   →  0.18.0  2025-10-07   (127 days)
            0.18.0  2025-10-07   →  0.19.0  2026-05-06   (211 days)
```

A three-week patch cadence with a four-to-seven-month minor cadence is the project telling you
where its churn is. The correct posture is **pin exactly, upgrade deliberately, and test the
upgrade rather than reading about it** — on a project that never promised you compatibility,
a floating `>=` constraint is a decision to be surprised on somebody else's schedule.

## And the contrast that matters

A library version is enforced. `deepspeed==0.19.7` resolves through an installer to a specific
immutable artefact with a hash, today and in five years, and a lockfile makes that reproducible
for everyone on the team. A model's version — see question 246 — is a product name. No tool
resolves it, no registry guarantees immutability behind a friendly alias, and nothing stops the
weights behind it being replaced. When someone proposes treating the two the same way in a
dependency policy, that is the difference to put on the table.

## What an interviewer digs into next

* You upgraded a patch version and throughput fell 15%. Where do you look first?
* What is the difference between a `0.x` project's minor bump and a `1.x` project's major?
* Which is riskier: a changed default or a removed function, and why is it the first one?
* How would you detect a changed default automatically in CI?
* What would make you *not* pin exactly?

## Where this stands, September 2026

Everything about DeepSpeed here is **primary**, read from a clone of `deepspeedai/DeepSpeed` at
commit `1eb56d2` — `release/release.sh`, `release/bump_patch_version.py`,
`release/check_release_version.py`, `version.txt` (0.19.8), `README.md`'s build matrix and
contributed-hardware table, `docs/_pages/config-json.md` for the `pin_memory` note, and
`blogs/core_api_update/README.md` for the 0.18.3 additions — with the release dates taken from
PyPI's JSON API. The two PRs named in that blog, #7665 and #7700, were located in the git history
and both carry `version.txt` = 0.18.3, which is how the release attribution above was made rather
than guessed. Cadences change. Reading the release script first does not.
