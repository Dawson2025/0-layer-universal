# Tree of Needs

This folder contains the hierarchical organization of all requirements for the Better AI System.

**Version**: 1.4.0 (see [_meta/VERSION.md](./_meta/VERSION.md))

---

## Structure

```
tree_of_needs/
├── _meta/                               Meta-documentation
│   ├── CHANGELOG.md                     Version history
│   ├── DEPENDENCIES.md                  Need dependency map (+ shared needs)
│   ├── EXTENSION_GUIDE.md               How to extend the tree
│   ├── PRINCIPLES.md                    Guiding principles
│   └── VERSION.md                       Versioning policy
│
└── 00_seamless_ai_collaboration/        ← ROOT NEED
    │
    ├── 01_capable/                      "Can AI do the work?"
    │   ├── need_01_persistent_knowledge
    │   ├── need_02_scalable_context
    │   ├── need_03_discoverable
    │   └── need_04_multimodal ⟷         (shared with 05_engaging)
    │
    ├── 02_continuous/                   "Does work keep going?"
    │   ├── need_01_tool_portable
    │   ├── need_02_session_resilient
    │   ├── need_03_failure_recoverable
    │   ├── need_04_evolvable
    │   └── need_05_cross_platform
    │
    ├── 03_trustworthy/                  "Can I trust AI?"
    │   ├── need_01_rule_compliant
    │   ├── need_02_predictable
    │   └── need_03_bounded
    │
    ├── 04_observable/                   "Can I see what's happening?"
    │   ├── need_01_transparent
    │   ├── need_02_debuggable
    │   └── need_03_auditable
    │
    └── 05_engaging/                     "Is it enjoyable?"
        └── need_01_multimodal ⟷         (shared with 01_capable)
```

⟷ = Shared need (appears in multiple branches)

---

## The Graph (DAG)

```
                              Seamless AI Collaboration
                                         │
       ┌───────────┬───────────┬─────────┴─────────┬───────────┬───────────┐
       │           │           │                   │           │           │
   CAPABLE    CONTINUOUS   TRUSTWORTHY        OBSERVABLE   ENGAGING       │
    /|\ \       /|\ \          /|\                /|\          |          │
   / | \ \     / | \ \        / | \              / | \         |          │
  n1 n2 n3 n4 n1 n2 n3 n4 n5 n1 n2 n3          n1 n2 n3       n1         │
           \_______________________________________________/
                              multimodal (shared)
```

Note: `multimodal` has two parents (01_capable and 05_engaging), making this a DAG.

---

## Why "Tree" (Actually a DAG)?

While called "Tree of Needs," this is technically a **Directed Acyclic Graph (DAG)** - some needs have multiple parents.

1. **Single Root** - All requirements trace to one goal: Seamless AI Collaboration
2. **Clear Branches** - Five concerns: Capable, Continuous, Trustworthy, Observable, Engaging
3. **Specific Leaves** - Each need is focused and actionable
4. **Inheritance** - Child needs inherit context from parents (via CLAUDE.md cascade)
5. **Navigation** - AI can traverse up/down to find relevant context
6. **Shared Needs** - Some needs belong to multiple branches (marked with ⟷)

### Shared Needs Example
`multimodal` belongs to both:
- **01_capable**: "Can AI do voice/visuals?" (capability)
- **05_engaging**: "Is using voice/visuals enjoyable?" (experience)

See [_meta/DEPENDENCIES.md](./_meta/DEPENDENCIES.md#shared-needs) for details.

---

## Future-Proofing

This tree is designed to evolve:

| Document | Purpose |
|----------|---------|
| [RATIONALE.md](./_meta/RATIONALE.md) | Why hierarchical/DAG structure (research-backed) |
| [PRINCIPLES.md](./_meta/PRINCIPLES.md) | Guiding principles for all needs |
| [EXTENSION_GUIDE.md](./_meta/EXTENSION_GUIDE.md) | How to add branches/needs |
| [DEPENDENCIES.md](./_meta/DEPENDENCIES.md) | Which needs depend on which |
| [CHANGELOG.md](./_meta/CHANGELOG.md) | What changed and when |
| [VERSION.md](./_meta/VERSION.md) | Versioning policy |

---

## Reading Order

1. [_meta/PRINCIPLES.md](./_meta/PRINCIPLES.md) - Understand guiding principles
2. [00_seamless_ai_collaboration](./00_seamless_ai_collaboration/) - Start with the root
3. Read each branch README to understand the five concerns
4. Dive into specific needs as relevant
5. Check [_meta/DEPENDENCIES.md](./_meta/DEPENDENCIES.md) for implementation order
