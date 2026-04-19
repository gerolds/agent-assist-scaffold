# Migrate to Agent Coordination Structure

> **One-time migration prompt.** Run this as the session-start prompt on a project that has
> existing code and planning documents but no `.agent/` or `.github/specs/` structure.
>
> The old project's custom-instructions should be **disabled** during migration.
> Only this prompt (and optional subagents) are active until migration completes.

## Your job

You are migrating an existing project to a human-in-the-loop agent coordination structure.
The target structure is defined in `.github/agents/custom-instructions.md` and `.github/specs/`.
You must not lose information. You must not break the project. You must not modify code files.

## Before you start

1. Read `.github/agents/custom-instructions.md` — this is the **target structure**.
2. Read `.github/specs/workflow.md` — document lifecycle rules.
3. Read `.github/specs/templates/` — thread, module, and context templates.
4. Confirm with the human: which file is the **existing agent prompt** (if any)?

## What is and isn't part of the project

**Project modules** are ONLY folders matching `Common.*` or `Game.*` at the project root.
These are the modules you migrate. Everything else is third-party, Unity, or infrastructure.

Ignore all of the following:
- `Packages/`, `Library/`, `ProjectSettings/`, `UserSettings/`, `Logs/`, `Temp/`, `obj/`
- Any folder under `Packages/` (these are Unity package manager packages — not yours)
- Any `.asmdef` outside of `Common.*` or `Game.*` root folders
- `Assets/Plugins/`, `Assets/TextMesh Pro/`, or any other third-party asset folder
- Assembly definitions belonging to packages (e.g. `com.unity.*`, `com.mycompany.packagename`)

When in doubt about whether a folder is a project module or third-party: **ask the human**.

## Handling pre-existing `.github/` and `.agent/`

The project may already have a `.github/` folder (renamed, obsolete). It may already have `.agent/` files from a template or partial migration.

- **Renamed/obsolete folders** (e.g. `.github_old/`, `OBSOLETE.github/`) — ignore entirely. Note their existence in the inventory but do not process them.

## Unity `~` folder convention

Unity's asset pipeline ignores any folder whose name ends in `~`. All planning and
agent-maintained folders inside the Unity project use this suffix:

- `Assets/<Module>/.plans~/` — module-scoped threads
- `Assets/<Module>/.agents~/` — module-local agent context
- `PLANS~/` — project-level threads (vision, meta-concerns, cross-module discussions)

Do NOT create `.plans/` or `.agents/` without the `~` suffix.

## Phases

Work through these in order. Update `.agent/checkpoint.md` after each phase.
You may delegate phases to subagents to conserve context.

### Phase 1 — Inventory

Produce a structured inventory. Do not create or modify any project files yet.

1. **Map modules** — find folders matching `Common.*` or `Game.*` at the project root.
   Only these are project modules. Ignore all other `.asmdef` files (packages, plugins, etc).
   Record: module name, path, whether it has Runtime/, Editor/, or both.
2. **Find planning docs** — search for markdown files that look like plans, discussions,
   TODOs, architecture decisions, meeting notes. Record: path, apparent type, rough length.
3. **Find the existing agent prompt** — read it fully. Note what content maps to which
   target spec file (runtime-code, system-contract, architecture, first-principles, project-facts).
4. **Identify existing READMEs** — per module and project-level.
5. **Report to human** — present the inventory. Ask: "Anything missing? Any docs I shouldn't
   touch? Any modules to skip?" Wait for confirmation before proceeding.

Output: write inventory to `.agent/migration-inventory.md` (temporary, deleted at end).

### Phase 2 — Scaffold

Create the coordination structure. Does not touch any existing files.

1. **Create `.agent/`** — `index.md`, `checkpoint.md`, `backlog.md`, `thread-registry.md`.
   If these files already exist, **overwrite them** (they are from a template or failed migration).
   - `index.md`: populate from inventory (modules, their status, what exists).
   - `checkpoint.md`: record "migration in progress, phase 2 complete".
   - `backlog.md`: empty.
   - `thread-registry.md`: empty (populated in phase 3).

2. **Create `.github/specs/`** — copy the template spec files from this structure.
   If the project already has a `.github/specs/`, merge carefully — don't overwrite.

3. **Populate spec files from existing agent prompt** — if the project has a monolithic agent
   prompt, distribute its content:
   - Stack, scenes, domain facts → `project-facts.md`
   - Code patterns, hot-path rules, naming → `runtime-code.md`
   - System base classes, registration, extension points → `system-contract.md`
   - State ownership, cross-cutting, Unity-native → `architecture.md`
   - Design philosophy, reuse-before-invention, training corrections → `first-principles.md`
   - Content that doesn't fit any spec → flag for human decision.

   **Rule:** copy content, don't paraphrase. Preserve the original author's phrasing. Trim
   only obvious redundancy. When unsure whether something is load-bearing, keep it.

4. **Create module-level files** — for each discovered module:
   - `.agents~/context.md` from template (populate dependencies and key files from inventory).
   - `.plans~/` directory (empty, populated in phase 3).
   - Skip `README.md` if one already exists — don't overwrite.
   - If no README exists, create one from the MODULE_README template with what you know.

5. **Create `custom-instructions.md`** — use the template from this structure. Update the
   project facts section and specs index to match what was actually created.

6. **Create `PLANS~/`** — project-level planning surface for vision, meta-concerns, and
   cross-module threads. Add a brief README.

### Phase 3 — Convert threads

Transform existing planning documents into the thread structure.

For each planning doc found in inventory:

1. **Classify**: thread (discussion/plan), backlog item (TODO/deferred), spec content
   (architecture decision), or archive (meeting notes, outdated).
2. **Route**:
   - **Thread (module-scoped)** → copy to `<Module>/.plans~/`, add frontmatter, register.
   - **Thread (project-level)** → copy to `PLANS~/`, add frontmatter, register.
     Vision docs, meta-concerns, and cross-module discussions go here.
   - **Backlog item** → add to `.agent/backlog.md`.
   - **Spec content** → merge into the appropriate spec file or module README.
   - **Archive** → leave in place. Note in inventory as "not migrated — archive".
3. **Add frontmatter** to threads: parent (root unless clearly a child), status (infer from
   content — active if unresolved, closed if done, stale if outdated), created/updated dates.
4. **Respect the ≤200 line rule.** If a doc exceeds 200 lines, split into parent + children.
5. **Wire parent pointers** — if docs reference each other, reflect that in parent/child.
6. **Don't rewrite content.** Add frontmatter and move. Preserve the original text.

After converting: populate `thread-registry.md` with all discovered threads.

### Phase 4 — Verify

1. **Thread coverage** — every planning doc from inventory is either in thread-registry,
   backlog, a spec file, or flagged as archive. None lost.
2. **Module coverage** — every module has README.md, `.agents~/context.md`, `.plans~/`.
3. **Spec coverage** — every spec file has content (not just template headers).
   If a spec is empty, flag it — the project may not need it.
4. **Registry consistency** — every path in thread-registry points to a real file.
5. **Checkpoint** — update to "migration complete" with summary of what was done.
6. **Clean up** — delete `.agent/migration-inventory.md`.
7. **Report to human** — summary: modules migrated, threads created, specs populated,
   anything that needs human attention.

## Rules

- **Never modify code files** (`.cs`, `.shader`, `.asmdef`, scenes, prefabs, SOs).
- **Never delete existing planning docs** — copy into new structure, leave originals until
  the human confirms they can be removed.
- **Never paraphrase** — when moving content between files, preserve original wording.
- **Always wait for human confirmation** after the inventory phase.
- **Update checkpoint** after every phase so the migration can be resumed if interrupted.
- **Flag ambiguity** — when you're unsure how to classify a doc or where content belongs,
  list it as an open question for the human rather than guessing.
