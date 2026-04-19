# Module Template

> Copy this folder structure when creating a new module.
> Replace `_Template` with your domain name (e.g. `Game.Production`, `Common.Utils`).

## Folder Structure

```text
<Domain.Module>/
  README.md               # Module identity, primitives, scope, decisions
  Runtime/                # Runtime source — ships in builds
    <Module>.asmdef        # Assembly definition (references Runtime deps)
  Editor/                 # Editor source — editor-only
    <Module>.Editor.asmdef # Assembly definition (references Runtime + UnityEditor)
  .agents~/
    context.md            # Module-local agent context
  .plans~/                 # Thread documents
  Docs/                   # Durable documentation
```

## Assembly Definitions

Runtime `.asmdef` should reference:
- `Common.Utils` (shared runtime utilities)
- Other modules' Runtime assemblies as needed

Editor `.asmdef` should reference:
- This module's Runtime assembly
- `Common.Utils.Editor` (shared editor utilities)
- `UnityEditor` assemblies
- Other modules' **Runtime** assemblies (NOT their Editor assemblies)
