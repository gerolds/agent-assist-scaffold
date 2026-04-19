# Workflow

> How work is tracked and documents are maintained across sessions.

## Coordination Files

| File                        | Purpose                          | Lifecycle      |
| --------------------------- | -------------------------------- | -------------- |
| `.agent/checkpoint.md`      | Ephemeral current task state     | Overwrite      |
| `.agent/backlog.md`         | Persistent deferred-work queue   | Add/remove     |
| `.agent/thread-registry.md` | Master thread index              | Maintained     |

No item lives in two places. Checkpoint = ephemeral. Backlog = persistent. Threads = discussions.
Active work and completion are tracked via thread status in the registry.

## Module README Quality Test

A good README:
- Can the module be reconstructed from it and companions alone?
- Does it preserve only durable information that constrains implementation or review?
- Does each section answer a specific retrieval question?

## Document Rules

1. **≤200 lines.** Split into linked children if longer.
2. **YAML frontmatter** on every `.plans~/` document: parent, status, created, updated, progress.
3. **2-3 sentence summary** at the top of every document.
4. **No orphans.** Every document is reachable from the thread registry or a parent.
5. **No duplicates.** One canonical location per fact. Link, don't copy.

## Progress Reporting

Every thread has a `## Progress Log` (reverse-chronological) and a `progress: "N/M"` frontmatter
field. Update both whenever you touch a thread. The registry mirrors the frontmatter field so
humans can scan progress at a glance without opening each thread.

## ADR Headers

For substantive changes to a file, keep a tiny ADR header above usings.
File-native comment syntax. Consolidate, don't append.
