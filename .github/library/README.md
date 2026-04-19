# Agent Library

> Pre-built agents that ship with the scaffold but are **not active by default**.
> Copilot only scans `.github/agents/` — files here are inert until you move them.

## How to Use

Copy (or symlink) any agent file into `.github/agents/` to activate it:

```sh
cp .github/library/critics/systems-design.critic.md .github/agents/
```

Remove it from `agents/` to deactivate. The library copy stays untouched.

## What's Here

### `critics/`

Opinionated reviewers. They read your project specs and evaluate work against them.
Domain-specific by nature — pick the ones that match your project, ignore the rest.

| File | Focus |
|------|-------|
| `colony-systems-critic.agent.md` | Colony-sim mechanics, feedback loops, systemic design |
| `colony-systems-critic-short.agent.md` | Same framework, hard ≤500 word limit |
| `lantern-reviewer.agent.md` | Implementation review: local conventions, sibling consistency, architecture fit |

### Writing Your Own

A critic is just an `.agent.md` file that:

1. Reads project specs (architecture, system-contract, runtime-code, etc.)
2. Evaluates a proposal or implementation against them
3. Produces structured feedback — not code changes

Name them `<domain>.critic.md` by convention so they're easy to identify, though any `.agent.md` name works in Copilot's `agents/` folder.
