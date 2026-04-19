---
name: "Migration — Verify"
description: "Phase 4 subagent. Validates migration completeness and reports to human."
tools: ['insert_edit_into_file', 'replace_string_in_file', 'create_file', 'apply_patch', 'show_content', 'open_file', 'list_dir', 'run_in_terminal', 'read_file', 'file_search', 'grep_search']
model: "GPT-5.4"
---

You are running Phase 4 of a project migration. Read `.github/prompts/migrate.prompt.md`
for full context.

Execute only the **Phase 4 — Verify** section. Check thread coverage, module coverage,
spec coverage, and registry consistency. Clean up the temporary inventory file.

Report to the human: what was migrated, what needs attention, what's ready.
Update `.agent/checkpoint.md` to "migration complete".
