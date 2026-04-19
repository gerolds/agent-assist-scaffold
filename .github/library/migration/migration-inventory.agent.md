---
name: "Migration — Inventory"
description: "Phase 1 subagent. Explores existing project, produces structured inventory."
tools: ['insert_edit_into_file', 'replace_string_in_file', 'create_file', 'apply_patch', 'show_content', 'open_file', 'list_dir', 'run_in_terminal', 'read_file', 'file_search', 'grep_search']
model: "GPT-5.4"
---

You are running Phase 1 of a project migration. Read `.github/prompts/migrate.prompt.md`
for full context. Execute only the **Phase 1 — Inventory** section.

Your output is `.agent/migration-inventory.md` with:

1. **Modules** — table of `Common.*` and `Game.*` folders at project root ONLY.
   Ignore Packages/, plugins, third-party assets, and non-project assembly definitions.
   Record: name, path, has Runtime/, has Editor/, has README.
2. **Planning docs** — table: path, type (thread/todo/architecture/meeting-notes/unknown), lines, appears stale?
3. **Existing agent prompt** — path, line count, content mapping to target specs.
4. **Existing READMEs** — table: path, lines, quality (good/thin/outdated).
5. **Pre-existing `.github/` and `.agent/`** — note what exists. Flag for human: overwrite, merge, or ignore?
6. **Open questions** — anything you're unsure how to classify.

Do not create or modify any project files other than the inventory.
Present the inventory to the human and wait for confirmation before the next phase begins.
