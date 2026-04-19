# Project Facts

> Concrete facts about the project. Stack, scenes, content layout, domain.

## Stack

- **Engine:** Unity 6000.4
- **Render Pipeline:** URP 17
- **Language:** C# 9, nullable reference types enabled
- **Input:** InputSystem
- **Async:** UniTask (not coroutines). `-Async` suffix. `CancellationToken` where practical.
- **UI Animation:** DOTween + UniTask for UGUI flows
- **Debug Drawing:** ALINE
- **Editor Ergonomics:** Odin Inspector
- **No `record` types.**

## Scenes

- Main menu: `Assets/Game.Content/Scenes/Start__SYSTEM.scene`
- Root game: `Assets/Game.Content/Scenes/Game__SYSTEM.scene`

## Content Layout

- All game-specific content assets: `Assets/Game.Content/*`
- Subfolders organized by feature/domain
- Inspect `Library/PackageCache/*` when you need package or cached source

## Domain

Colony sim. Top-down-ish perspective, grid-based building and pathfinding.
The core resource and pressure mechanic is a **lifeline network**.
Solo project with agentic help — all code supports the workflows this implies.

## Module Naming

Modules follow a domain hierarchy at the project root:

- `Common.*` — shared utilities and infrastructure (e.g. `Common.Utils`)
- `Game.*` — feature/system modules (e.g. `Game.Production`, `Game.Build`)
- `Game.Core` — orchestration, cross-system wiring, bootstrap
- `Game.Content` — assets, not code

Each module is a Unity assembly definition. Runtime code in `Runtime/`, editor code in `Editor/`.
