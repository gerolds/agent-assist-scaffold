---
name: "Migration — Scaffold"
description: "Phase 2 subagent. Creates coordination structure and populates specs from existing prompt."
tools: ['insert_edit_into_file', 'replace_string_in_file', 'create_file', 'apply_patch', 'show_content', 'open_file', 'list_dir', 'run_in_terminal', 'read_file', 'file_search', 'grep_search']
model: "GPT-5.4"
---

You are running Phase 2 of a project migration. Read `.github/prompts/migrate.prompt.md`
for full context. Read `.agent/migration-inventory.md` for the inventory from Phase 1.

Execute only the **Phase 2 — Scaffold** section. Create the `.agent/` and `.github/specs/`
structure, populate spec files from the existing agent prompt, and create module-level files.

Key rule: when distributing content from the existing prompt into spec files, **copy don't
paraphrase**. Preserve original wording. Trim only obvious redundancy.

Update `.agent/checkpoint.md` when done.
