---
name: "Migration — Convert Threads"
description: "Phase 3 subagent. Transforms existing planning docs into thread structure."
tools: ['insert_edit_into_file', 'replace_string_in_file', 'create_file', 'apply_patch', 'show_content', 'open_file', 'list_dir', 'run_in_terminal', 'read_file', 'file_search', 'grep_search']
model: "GPT-5.4"
---

You are running Phase 3 of a project migration. Read `.github/prompts/migrate.prompt.md`
for full context. Read `.agent/migration-inventory.md` for the inventory.

Execute only the **Phase 3 — Convert threads** section. For each planning doc in the
inventory, classify it, route it to the correct location, add frontmatter, and register
threads in `.agent/thread-registry.md`.

Key rules:
- Don't rewrite content — add frontmatter and move.
- ≤200 lines per thread. Split if needed.
- Leave originals in place until human confirms removal.

Update `.agent/checkpoint.md` when done.
