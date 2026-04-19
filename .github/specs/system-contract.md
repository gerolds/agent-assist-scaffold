# System Contract

> How systems (hosts + components) are built. Read before creating any new system.
> **Read `Common.Utils/Runtime/Patterns/System/SystemBase.cs` before starting.**

## Base Classes

- `*System` with components → `SystemBase<TC, TS>` or `PackableSystemBase<TC, TS>`. No exceptions.
- Component base is abstract. Concrete subtypes = different roles (tool, user, sensor, handler).
- `OnRegistered`/`OnUnregistered` route by subtype into specialized sub-collections.
  Reference: `BuildSystem.OnRegistered` and `InventorySystem.OnRegistered`.

## Anti-Patterns (You Are Rebuilding SystemBase If...)

- You're writing `HashSet<T>` of components
- You're writing `Register()`/`UnRegister()` methods
- You're using `FindObjectsByType` in Start
- You're writing `event Action<T> CompositionChanged`

→ Use SystemBase instead.

## Service Resolution

- `Services.Get<T>()` for cross-system resolution in `Start()`.

## Naming

- `*System` = host
- `*ComponentBase` = abstract family
- `*Presenter` = observer and UI routing
- `*Display` = prefab refs
- `*Host` / `*Authoring` = system entry point

## Modifiability Convention

Systems that compute values or gate decisions expose injectable extension points.
Four shapes across the entire codebase:

| Shape        | Signature                        | Composition                               |
| ------------ | -------------------------------- | ----------------------------------------- |
| **Filter**   | `(context) → bool`              | Conjunction (AND)                         |
| **Modifier** | `(baseValue, context) → value`  | Pipeline (each sees previous output)      |
| **Scorer**   | `(context) → float`             | Aggregation (sum/max/weighted by system)  |
| **Observer** | `(event) → void`               | Broadcast (no veto)                       |

- The system's own default logic is the first implementation of each shape.
- External concerns compose via `AddFilter`/`AddModifier`/`AddScorer`/`AddObserver` at init.
- Implementations: interface or delegate — plain C# class, ScriptableObject, delegate, or test
  mock. NOT assumed MonoBehaviour. The carrier is whatever the registering site owns.

## Naming Rule for Extension Points

`I{System}{Noun}{Shape}` — e.g. `IBuildCommandFilter`, `IWorkSpeedModifier`,
`IPlacementScorer`, `IInventoryMutationObserver`.

Never use interceptor, validator, evaluator, gate, or handler as shape synonyms.
