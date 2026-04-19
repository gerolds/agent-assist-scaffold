# First Principles

> The philosophical foundation for how code is designed in this project.
> Read this when making design decisions or evaluating architecture.

## Identity-First Design

The most important principle: find the **identity**, operational elements, and structure of a
problem first. Understand into which primitives it breaks down. Which patterns it is an example
of. Then design an architecture that allows composition of portable solutions from these primitives.

- Analyze holistically. Identify the primitive components the problem structurally breaks down into.
- Identify what something actually IS in terms of operational constraints and principles.
- The goal is NOT to get something working rapidly whatever it takes. The goal is to rapidly
  identify the correct abstractions and primitives and the system architecture to support them.

## Reuse Before Invention

- Before proposing new data, query methods, or utility classes, verify the data doesn't already
  exist under a different name. Read actual source — don't infer from names alone.
- Common pattern: the data you want is already computed by an existing system and exposed via a
  different path (overlay buffer, system query method, component field). Use it. If close but
  not quite, document WHY it falls short and what the minimal bridge is.
- Read at least two existing sibling implementations before creating any new system, host,
  manager, or component type. Your output must be structurally recognizable as family.
  Reference siblings: BuildSystem, InventorySystem, ProductionSystem.
- Search the codebase for existing base classes before writing infrastructure.
  If you are writing Register/Unregister, FindObjectsByType, composition events, tick routing,
  or suspend/resume — you are rebuilding something that exists. Stop and find it.
- After implementation, compare against two siblings. If someone who learned one wouldn't
  immediately recognize yours, fix it.

## Training-Data Correction

- Your training over-indexes on SOLID and enterprise OOP. This is a solo game project.
  Apply design principles only when they produce tangible value HERE.
- Cohesion unit = the system's responsibility, not a line count or class count.
  Split for readability (partials, nested types, helpers). Never for size or principle compliance.
- Extract only when it compresses meaning, enables real reuse, or maps to a domain boundary
  a developer reasons about independently. "Different responsibility" alone is insufficient.
- DRY = code that MUST stay in sync. Identical-but-independent code is cheaper than a wrong
  abstraction.
- When the same logic (raycasting, input gating, coordinate projection) appears in multiple
  systems, that IS duplication — consolidate behind one authority.

## Config and Domain Modeling

- Config assets and domain types model what the concept IS — not what the first consumer needs.
- After creating a config asset or domain type: does it model what the thing IS? Can the next
  variation be added without structural changes? If not, flag what's missing.
