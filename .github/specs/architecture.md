# Architecture

> Structural principles and patterns. Read when making design decisions.

## State Ownership

- Validate at boundaries; trust validated internal state; fail loudly on invariant violations.
- Immutable data and pure domain logic where possible. Mutation lives in host objects.
- State belongs where it's owned:
  - Runtime state → `*System` hosts
  - Config → ScriptableObjects
  - View state → presenters
  - Persistent state → mementos on the host that saves/restores it

## System Design

- Systems are engines that drive variations within contracts. Inspector config and scripting
  against system contracts should both be natural. A system that forces workarounds for obvious
  variations is too narrow.
- Narrow, deep APIs for plumbing. Generous, expressive APIs for domain primitives.
- Before creating a new mechanism, check whether an existing abstraction already covers the
  category. Reference: inventory absorbs items/resources/currency; SystemBase absorbs all
  component-owning hosts; Producer/Recipe absorbs all crafting; persistence absorbs all saveable
  state. The unifying principle IS the design — find it before building a one-off.

## Cross-Cutting Concerns

- When multiple systems independently compensate for the same cross-cutting concern →
  coordinating system or boundary is missing. One authority per invariant; delete the scattered
  checks.
- Cross-system wiring lives in one orchestration init point in `Game.Core`, not in per-pair
  Bridge/Adapter files. If you're creating a `*Bridge` or `*Adapter`, the orchestration layer
  is missing — add the wiring there instead.

## Use Unity's Strengths

Colliders for spatial queries, physics layers for filtering, GameObjects for identity and
hierarchy, Inspector for runtime debugging, ScriptableObjects for config and symbols, prefab
composition for behavior assembly, scenes as composition roots. C# data structures own
simulation state. Don't reimplement what Unity provides.

## Types and APIs

- Avoid stringly typed, untyped, and dynamic APIs. Encode intent in types.
- Keep data passing simple. Favor early returns.
- When touching event handling and mutable data, always consider state persistence and object
  lifecycle, including edge cases.
- Verify any new MonoBehaviour provides real modularity: different GameObject, different scope
  (view/data/logic), or pluggable specialization.
