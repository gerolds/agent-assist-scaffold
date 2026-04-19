# Agent-Assisted Project Scaffold

A drop-in coordination structure for long-running human + AI-agent projects. It gives agents persistent memory, navigable specs, and lightweight project management — so sessions stay productive instead of re-discovering context, drifting from goals, or drowning in stale docs.

## The Problem

AI coding agents are stateless. Every session starts from zero. In a long-running project this causes:

- **Discovery tax** — the agent re-reads everything to figure out where it left off.
- **Context overflow** — monolithic prompts bloat until they crowd out actual work.
- **Drift** — without persistent goals and checkpoints, work wanders between sessions.
- **Stale documentation** — plans and READMEs rot because nobody is accountable for them.
- **Churn** — lots of words, relatively little output. Decisions get revisited instead of closed.

## The Solution

A small set of files and conventions, split into two layers:

| Layer | Location | Contents | Mutability |
|-------|----------|----------|------------|
| **Instructions & Specs** | `.github/` | Agent roles, project specs, templates, reusable prompts | Stable — human-edited |
| **Living State** | `.agent/` | Checkpoint, backlog, thread registry, project index | Updated every session |

The agent reads only what the current task requires (via a specs index in `custom-instructions.md`), updates its checkpoint when done, and leaves a trail the next agent — or the same agent in a new session — can pick up without re-reading the whole project.

## Structure

```
.github/
  custom-instructions.md        ← Root prompt (created during migration, see below)
  agents/                       ← Agent role definitions
    custom-instructions.md      ← Pre-migration home (moved to parent after migration)
    big-picture.agent.md        ← Vision / product-level reasoning
    maintainer.agent.md         ← Coordination file upkeep
    gather-context.agent.md     ← Deep-read research subagent
    ...
  specs/                        ← Project-level specs (navigable, ≤200 lines each)
    project-facts.md            ← Stack, scenes, domain
    first-principles.md         ← Design philosophy
    architecture.md             ← Structural patterns
    system-contract.md          ← How systems are built
    runtime-code.md             ← Code style and rules
    workflow.md                 ← Document lifecycle and tracking
    templates/                  ← Thread, module, and context templates
  prompts/                      ← Reusable session-start prompts
    migrate.prompt.md           ← One-time migration (see below)
    health-check.prompt.md      ← Periodic project audit

.agent/                         ← Living coordination state
  index.md                      ← 1-page project overview (read first every session)
  checkpoint.md                 ← Last session: what was done, what's next, blockers
  backlog.md                    ← Prioritized deferred work
  thread-registry.md            ← Master index of all planning threads

PLANS~/                         ← Project-level discussion threads
<Module>/.plans~/               ← Module-scoped threads (Unity ~ convention)
<Module>/.agents~/context.md    ← Module-local agent context
```

## Key Concepts

### Specs, Not a Monolith

Instead of one giant prompt, project knowledge is split into focused spec files (≤200 lines each). The root `custom-instructions.md` is a navigation hub with a "when you are… read…" table. Agents load only what they need.

### Checkpoint Continuity

`.agent/checkpoint.md` is overwritten at session end with: what was done, what's next, and any blockers. The next session reads it first and picks up where the last one left off.

### Threads as Living Plans

Planning discussions live in `.plans~/` folders as markdown files with YAML frontmatter (parent, status, progress). They form a tree navigable from `.agent/thread-registry.md`. Status scores: `active` > `blocked` > `stale` > `good-enough` > `closed`.

### Health Checks

`health-check.prompt.md` is a periodic audit that surfaces ambiguity, drift, churn, and fragmentation — the main failure modes of long-running projects. It writes to `PLANS~/health-check.md`.

## How to Use This Template

### On a New Project

1. Copy this scaffold into your project.
2. Edit `.github/specs/project-facts.md` with your actual stack and domain.
3. Edit the project-specific references in `.github/agents/custom-instructions.md`.
4. Move `.github/agents/custom-instructions.md` → `.github/custom-instructions.md`.
5. Start working. The agent reads `index.md` → `checkpoint.md` and follows the specs index.

### On an Existing Project (Migration)

1. Drop the `.github/` folder into the project. **Do not** move `custom-instructions.md` yet.
2. Run `migrate.prompt.md` as a session prompt. It will:
   - Inventory existing modules and planning docs.
   - Create the `.agent/` coordination files.
   - Distribute any monolithic agent prompt into the spec files.
   - Convert existing planning docs into registered threads.
   - Verify nothing was lost.
3. After migration completes, move `.github/agents/custom-instructions.md` → `.github/custom-instructions.md`.

> **Why the two-step?** During migration the old project instructions should be disabled. The scaffold ships `custom-instructions.md` inside `agents/` so it doesn't activate as the root prompt until you explicitly move it.

## Design Principles

- **No information loss.** Migration copies content; it never paraphrases or discards.
- **One canonical location per fact.** Link, don't duplicate.
- **≤200 lines per document.** Split into linked children if longer.
- **Agents never modify `.github/`** without explicit human instruction.
- **Human approves direction.** Agents propose options with tradeoffs when unsure.

## What This Is Not

- Not a CI/CD pipeline or GitHub Actions setup.
- Not a code framework or library.
- Not tied to any specific language or engine (the included specs are Unity/C# examples — replace them with your own).