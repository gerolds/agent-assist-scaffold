# Runtime Code

> Rules for code in `<Module>/Runtime/`. This code ships in player builds.
> No `UnityEditor` namespace. Lean, tested, stable.

## What Belongs Here

- Domain logic, systems, components, data types
- ScriptableObject definitions for config and symbols
- MonoBehaviours that exist in the game
- Pure C# utilities used at runtime
- Interfaces and contracts

## What Does NOT Belong Here

- Anything referencing `UnityEditor`
- Custom inspectors, property drawers, editor windows
- Asset import/processing code
- Debug-only tooling (use `#if UNITY_EDITOR` sparingly and only for hooks, not logic)

## Code Patterns

- `[SerializeField] private` fields over public mutable
- Try* methods return `bool` + `out` param. Avoid null returns.
- Early returns. Explicit data flow. No stringly-typed APIs.
- Hot paths: no LINQ, no boxing, no closures, no uncached GetComponent
- Explicit data flow and cached references over implicit discovery
- Cancel async work on scene-object destruction
- Events for public API boundaries and decoupled observation only

## When Runtime Work Affects Editor

When you add or change:

- A `[SerializeField]` field → check if a custom drawer exists in `Editor/` that needs updating
- A ScriptableObject → check for custom editors or creation wizards in `Editor/`
- A component's public API → check if editor tools reference it
- Serialization shape → editor migration code may be needed

**Flag these to the human if unsure.** Don't silently break editor tooling.

## Naming

- `*System` = host (SystemBase-derived)
- `*ComponentBase` = abstract family
- `*Presenter` = observer and UI routing
- `*Display` = prefab refs
- `*Host` / `*Authoring` = system entry point

## Comments

- Explain intent, constraints, tradeoffs — not obvious code
- File-level ADR header above usings for substantive changes (file-native comment syntax)
- Consolidate ADR headers, don't append

## IInfoProvider Rule

Any IInfoProvider that emits a percentage, ratio, ETA, or threshold as text must also
provide a visual Meter or Badge for that same fact. Text-only scalar representation is a defect.

## Editor Code (`<Module>/Editor/`)

Editor code is a **consumer and author** of runtime types. It runs only in the Unity Editor,
can reference `Runtime/` types and `UnityEditor` APIs.

**Editor code must understand the runtime types it touches.** When runtime types change,
corresponding editor code is likely stale.

- Odin Inspector attributes where they simplify inspector code
- LINQ is fine — no hot-path concerns
- `SerializedObject`/`SerializedProperty` for undo-safe inspector code
- No game logic in Editor (even "just for testing")
- Don't duplicate runtime validation — call it and surface results
- Don't assume editor state persists across domain reloads
- Don't reference other modules' Editor assemblies (prefer runtime interfaces)

Each module's `Editor/` `.asmdef` references its own Runtime assembly, `UnityEditor`,
and other modules' **Runtime** assemblies (not their Editor assemblies).
