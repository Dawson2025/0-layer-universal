# Need Dependencies

How needs relate to and depend on each other.

---

## Structure: DAG (Not Strict Tree)

While called "Tree of Needs," the structure is actually a **Directed Acyclic Graph (DAG)**. Some needs have multiple parents (shared needs).

### Why a DAG?

Some needs genuinely belong to multiple branches:
- **Multimodal** belongs to both 01_capable (can AI do it?) AND 05_engaging (is it enjoyable?)

This is natural - real requirements often serve multiple concerns.

### Shared Needs

| Need | Primary Branch | Also In | Reason |
|------|----------------|---------|--------|
| `multimodal` | 05_engaging | 01_capable | Capability + Experience |

Shared needs have:
- **Primary location**: Full requirements.md
- **Reference location**: Cross-reference pointing to primary

Symbol: `⟷` indicates a shared need in documentation.

---

## Dependency Types

| Type | Symbol | Meaning |
|------|--------|---------|
| **Enables** | `→` | Must be satisfied before the other can work |
| **Enhances** | `~>` | Makes the other more effective (not required) |
| **Related** | `<->` | Share concepts, should be considered together |
| **Shared** | `⟷` | Same need appears in multiple branches |

---

## Dependency Map

```
                    ┌─────────────────────────────────────────────┐
                    │     00_seamless_ai_collaboration            │
                    │              (ROOT NEED)                    │
                    └─────────────────────────────────────────────┘
                                        │
    ┌───────────┬───────────┬───────────┼───────────┬───────────┐
    ▼           ▼           ▼           ▼           ▼           │
01_capable  02_continuous  03_trustworthy  04_observable  05_engaging
    │           │           │               │           │       │
    │           │           │               │           │       │
    ▼           ▼           ▼               ▼           ▼       │
 Foundation  Depends on  Depends on    Supports all  Enhances  │
 (build      01_capable  01_capable    (cross-cut)   experience│
  first)                                                        │
```

---

## Cross-Branch Dependencies

### 01_capable → 02_continuous
The CONTINUOUS branch depends on CAPABLE foundations:
- `tool_portable` needs `persistent_knowledge` (agnostic system prompts)
- `session_resilient` needs `discoverable` (self-describing structure)
- `failure_recoverable` needs `discoverable` (can find what broke)

### 01_capable → 03_trustworthy
The TRUSTWORTHY branch depends on CAPABLE foundations:
- `rule_compliant` needs `discoverable` (rules must be findable)
- `predictable` needs `persistent_knowledge` (consistent context loading)
- `bounded` needs `scalable_context` (scope defined by agent hierarchy)

### 01_capable → 04_observable
The OBSERVABLE branch depends on CAPABLE foundations:
- `transparent` needs `discoverable` (can see where you are)
- `debuggable` needs `discoverable` (can trace to source)
- `auditable` needs `persistent_knowledge` (history persists)

### 04_observable → All
OBSERVABLE supports debugging all other branches:
- Validation tools check 01_capable structure
- Debugging tools diagnose 02_continuous failures
- Audit trails verify 03_trustworthy compliance
- Debugging tools help tune 05_engaging experiences

### 05_engaging → User Experience
ENGAGING enhances the experience of all other branches:
- `multimodal` needs `discoverable` (must find things to interact with)
- `multimodal` enhances all branches (voice/visuals make everything better)

---

## Intra-Branch Dependencies

### 01_capable (internal)
```
persistent_knowledge
        │
        ├──→ scalable_context (delegation uses knowledge hierarchy)
        │
        └──→ discoverable (navigation requires knowing structure)
```

### 02_continuous (internal)
```
tool_portable
        │
        ├──→ session_resilient (cross-tool uses same mechanisms)
        │       │
        │       └──→ failure_recoverable (recovery after session issues)
        │
        ├──→ evolvable (portability enables evolution)
        │       │
        │       └──~> all other needs (evolution future-proofs everything)
        │
        └──→ cross_platform (portability extends to OS/machines)
```

**Notes**:
- `evolvable` enhances ALL other needs by ensuring they remain viable as technology changes
- `cross_platform` extends tool portability to OS and machine portability

### 03_trustworthy (internal)
```
rule_compliant
        │
        ├──→ predictable (following rules → consistent behavior)
        │
        └──→ bounded (rules define boundaries)
```

### 04_observable (internal)
```
transparent
        │
        ├──→ debuggable (visibility enables diagnosis)
        │
        └──→ auditable (transparency enables review)
```

### 05_engaging (internal)
```
multimodal
        │
        └──~> future needs (conversational, adaptive, delightful)
```

**Note**: `multimodal` is the foundation for engagement - future needs build on it.

---

## Implementation Priority

Based on dependencies, recommended implementation order:

### Phase 1: Foundation (01_capable)
1. `need_01_persistent_knowledge` - System prompt hierarchy
2. `need_03_discoverable` - Layer-stage structure, registries
3. `need_02_scalable_context` - Agent delegation

### Phase 2: Continuity (02_continuous)
4. `need_01_tool_portable` - Agnostic architecture
5. `need_02_session_resilient` - Handoff documents
6. `need_03_failure_recoverable` - Idempotent setup
7. `need_04_evolvable` - Modular, forward-compatible design
8. `need_05_cross_platform` - OS and machine portability

### Phase 3: Trust (03_trustworthy)
9. `need_01_rule_compliant` - Rule hierarchy
10. `need_02_predictable` - Consistent behavior
11. `need_03_bounded` - Scope definitions

### Phase 4: Observability (04_observable)
12. `need_02_debuggable` - Validation suite
13. `need_01_transparent` - State visibility
14. `need_03_auditable` - Change tracking

### Phase 5: Engagement (05_engaging)
15. `need_01_multimodal` - Voice, visuals, rich interaction

---

## Adding New Dependencies

When adding a new need, document:
1. What existing needs it depends on (prerequisites)
2. What existing needs depend on it (dependents)
3. What needs are related but not dependent (related)

Update this file and the dependency diagram accordingly.
