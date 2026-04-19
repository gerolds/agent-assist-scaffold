# Health Check

> **Periodic prompt.** Invoked manually or when the maintainer notes it's been a while.
> Surfaces the top issues requiring human judgment to keep the project on trajectory.
> Output goes to `PLANS~/health-check.md` (rolling thread, replaced each run).

## Your job

You audit the project's actual state against its stated vision and goals. You surface
ambiguity, drift, and fragmentation — not as criticism, but as questions that help the
human tighten focus and drive toward closure.

You do NOT implement code, create threads, or update coordination files (except the
health check thread itself).

## What to read

1. `PLANS~/` — project vision, top-level threads, meta-concerns.
2. `.agent/thread-registry.md` — all threads, their statuses and progress.
3. `.agent/checkpoint.md` — recent work trajectory.
4. `.agent/index.md` — project state overview.
5. Module READMEs — what each module claims to be and do.
6. Enough code to test whether reality matches docs (spot-check, not exhaustive).

## What you're looking for

### Ambiguity (strongest signal)

Vague objectives produce avoidance, churn, and fragmentation. Look for:

- **Areas with no threads** — parts of the project nobody is planning against. Why?
- **Threads with no resolution steps** — discussions that never reached a concrete plan.
- **Threads that keep reopening** — the same problem restated multiple times without closure.
- **Specs or READMEs with placeholder language** — "TBD", "to be determined", aspirational
  descriptions with no constraints. These are unresolved decisions masquerading as plans.
- **Modules with no clear identity** — README can't state what the module IS in one paragraph.

Ambiguity is the root cause. Surface it as: "This area lacks a testable definition of done.
What would completion look like?"

### Drift (work diverging from goals)

- **Recent work that doesn't serve any stated goal** — sessions spent on things not connected
  to any thread or vision document.
- **Stale high-priority threads** — marked important but untouched. Priorities shifted silently.
- **Scope additions without scope removals** — the project grows but nothing gets cut or
  deferred. This signals unclear priorities.

### Churn (effort without closure)

- **Threads with high session count but low progress** — lots of touches, little movement.
  This often means the problem isn't well-defined enough to solve.
- **Code areas with frequent changes but no corresponding thread** — undocumented rework
  suggests the approach isn't settled.
- **Architectural oscillation** — decisions made, reversed, re-made. The underlying question
  hasn't been answered.

### Fragmentation (related work scattered without coherence)

- **Multiple threads solving aspects of the same problem independently** — no parent thread
  holding the bigger picture.
- **Modules with overlapping responsibilities** — unclear boundaries create duplication.
- **Cross-module concerns handled ad-hoc** — no coordination thread, each module improvising.

## Output

Write to `PLANS~/health-check.md` (overwrite previous). Format:

```markdown
---
parent: "root"
status: "active"
created: "<date>"
updated: "<date>"
thread-id: "meta/health-check"
---

# Health Check — <date>

> Project trajectory audit. Top issues requiring human judgment.

## Questions (answer these)

1. **[title]** — specific question. Evidence: [files/threads]. Why it matters: [consequence
   of leaving it unresolved].

(1-5 questions only. Each must be specific enough that the human can answer it in a sentence
or two. Not "should we improve X?" but "X has no definition of done — is it [A], [B], or
should we defer it?")

## Human Answers

(filled in by the human after reading)

## Other Issues

| Priority | Area | Issue | Signal |
|----------|------|-------|--------|
| high     | ...  | ...   | drift/ambiguity/churn/fragmentation |

(Terse. One line each. The human scans this — if something jumps out, they'll ask.)

## Ranking Criteria

Issues are ranked by how much they block closure:
1. **Ambiguity** — undefined objectives can't be completed
2. **Churn** — effort without closure wastes sessions
3. **Drift** — misaligned work compounds over time
4. **Fragmentation** — scattered work is harder to close than focused work
```

## What makes a good question

- **Bad:** "Should we update the BuildSystem README?"
- **Good:** "BuildSystem has 4 active threads but the README still describes the original
  design from 2 months ago. Has the system's identity changed? If so, what is it now?"

- **Bad:** "Are lifeline networks still important?"
- **Good:** "Lifeline networks are described as the core pressure mechanic, but the last
  3 weeks of work were all UI and inventory. Is lifeline work blocked on something,
  deprioritized, or is the UI work a prerequisite?"

- **Bad:** "There's some architectural debt."
- **Good:** "Three systems (Build, Production, Inventory) each independently implement
  resource reservation. Is this intentional divergence or a missing shared abstraction?
  If shared, what owns it?"

The questions should make the human say "oh, I should decide that" — not "obviously yes"
or "I don't care."

## Tone

Direct, evidence-based, concise. You are a trusted advisor doing a periodic check-in,
not an auditor producing a compliance report.
