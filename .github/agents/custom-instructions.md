# Custom Instructions — Passed With Every Session

> Root prompt fragment for every agent session. Navigation hub + operating rules.
> **Read only what your current task requires.**

## Who You Are

You are a coding agent on a human-supervised project. Sessions may be interrupted, resumed
by a different agent, or redirected at any time. The human approves direction and reviews output.

## Project Facts

**Unity 6000.4** colony-sim (URP 17, C# 9, InputSystem, nullable enabled).
Full stack, scenes, domain: → `.github/specs/project-facts.md`

## Project Structure

Modules: `Common.*` (shared), `Game.*` (features), `Game.Core` (orchestration).
Each module has `Runtime/` and `Editor/` — different compilation domains with different rules.

```text
.github/                      # STABLE — instructions and specs
  agents/                     # Agent role definitions
  specs/                      # Project-level specs (index below)

.agent/                       # LIVING — changes every session
  index.md                    # Current project state (start here)
  checkpoint.md               # Last session state, next steps, blockers
  backlog.md                  # Prioritized work items
  thread-registry.md          # Master thread index

Assets/PLANS~/                # Project-level discussions, vision, meta-concerns
                              # Top-level threads that don't belong to a single module

Assets/<Domain.Module>/              # e.g. Common.Utils, Game.Production
  README.md                   # Module identity, primitives, scope, decisions
  Runtime/                    # Ships in builds. No UnityEditor namespace.
  Editor/                     # Editor-only. Can reference Runtime.
  .agents~/context.md         # Module-local agent context
  .plans~/                    # Module-scoped discussion and planning threads
```

> **`~` suffix**: folders ending in `~` are ignored by Unity's asset pipeline.
> All planning and agent-maintained folders inside the Unity project use this convention.

## Specs Index

| When you are...                               | Read                                       |
| --------------------------------------------- | ------------------------------------------ |
| Starting any session                          | `.agent/index.md` → `.agent/checkpoint.md` |
| Writing or reviewing code                     | `.github/specs/runtime-code.md`            |
| Creating a new system, component, or host     | `.github/specs/system-contract.md`         |
| Making architecture or design decisions       | `.github/specs/architecture.md`            |
| Understanding first principles                | `.github/specs/first-principles.md`        |
| Tracking work or document lifecycle           | `.github/specs/workflow.md`                |
| Looking for project facts and stack info      | `.github/specs/project-facts.md`           |
| Creating a thread or planning document        | `.github/specs/templates/thread.md`        |
| Setting up a new module                       | `.github/specs/templates/module/`          |

## Core Rules

1. **Never assume context from a prior session.** Re-read `.agent/index.md` and `checkpoint.md`.
2. **Never modify `.github/`** without explicit human instruction.
3. **Update `.agent/checkpoint.md`** at session end or before a major pivot.
4. **When a task surfaces a wider issue**, tell the human. Create a thread if instructed.
5. **Prefer local code search** before MCP lookups. No temporary asset fixup scripts.
6. **Do not modify scenes, prefabs, or SOs** unless the task explicitly requires it.
7. **If unsure about direction**, propose 2-3 options with tradeoffs. Don't guess and implement.

## Planning Mode

Any agent can produce a planning thread. Use `.github/specs/templates/thread.md`.
Register in `.agent/thread-registry.md`. Thread rules are in `.github/specs/workflow.md`.

## Threads

A `.plans~/` document capturing a discussion, decision, or plan. Threads form a tree:
every thread has a `parent:` pointer (or `root`). Navigate: registry → branch → leaf.
Status scores: `active` > `blocked` > `stale` > `good-enough` > `closed`.
