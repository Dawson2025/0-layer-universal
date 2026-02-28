# Request Dependencies

**Project**: Better AI System
**Date**: 2026-01-25

## Dependency Graph

```
                    ┌─────────────────────┐
                    │ REQ-01              │
                    │ Layer-Stage System  │
                    │ (Foundation)        │
                    └──────────┬──────────┘
                               │
           ┌───────────────────┼───────────────────┐
           │                   │                   │
           ▼                   ▼                   ▼
┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
│ REQ-05           │ │ REQ-06           │ │ REQ-07           │
│ Documentation    │ │ Context System   │ │ Rules System     │
│ System           │ │                  │ │                  │
└────────┬─────────┘ └────────┬─────────┘ └────────┬─────────┘
         │                    │                    │
         └────────────────────┼────────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │ REQ-08              │
                    │ Automation System   │
                    │ (Enforcement)       │
                    └──────────┬──────────┘
                               │
           ┌───────────────────┼───────────────────┐
           │                   │                   │
           ▼                   ▼                   ▼
┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
│ REQ-02           │ │ REQ-03           │ │ REQ-04           │
│ Setup System     │ │ Manager          │ │ Memory System    │
│                  │ │ Hierarchy        │ │ (Research)       │
└──────────────────┘ └──────────────────┘ └──────────────────┘
```

## Dependency Matrix

| Request | Depends On | Blocks |
|---------|------------|--------|
| 01 - Layer-Stage | (none) | 02, 03, 04, 05, 06, 07, 08 |
| 02 - Setup | 01, 08 | - |
| 03 - Manager Hierarchy | 01, 06, 08 | 04 |
| 04 - Memory | 01, 03, 06 | - |
| 05 - Documentation | 01 | 08 |
| 06 - Context | 01 | 03, 04, 08 |
| 07 - Rules | 01 | 08 |
| 08 - Automation | 01, 05, 06, 07 | 02, 03 |

## Detailed Dependencies

### REQ-01: Layer-Stage System
**Depends on**: Nothing (foundation)
**Blocks**: Everything else

*Rationale*: All other requests assume consistent naming, stage numbering, and registries. This must be complete first.

---

### REQ-02: Better Setup System
**Depends on**:
- REQ-01: Needs consistent structure to configure
- REQ-08: Needs validation to verify setup correctness

**Blocks**: Nothing (end-user feature)

*Rationale*: Setup scripts must know the expected structure (REQ-01) and validate their results (REQ-08).

---

### REQ-03: AI Manager Hierarchy System
**Depends on**:
- REQ-01: Needs layer/stage structure for scope definitions
- REQ-06: Needs context rules for context loading per role
- REQ-08: Needs entity scaffolding for creating agent configs

**Blocks**:
- REQ-04: Memory system needs hierarchy for scope decisions

*Rationale*: Manager hierarchy defines roles that interact with layers/stages, load context, and may need automated creation.

---

### REQ-04: AI Dynamic Memory System
**Depends on**:
- REQ-01: Needs structure for memory scope hierarchy
- REQ-03: Needs agent roles for memory ownership
- REQ-06: Needs context rules for what to remember

**Blocks**: Nothing (research/future)

*Rationale*: Memory system is built on top of existing infrastructure. It's the most advanced feature and depends on most others.

---

### REQ-05: AI Documentation System
**Depends on**:
- REQ-01: Needs consistent paths to validate

**Blocks**:
- REQ-08: Automation needs doc validation tools

*Rationale*: Documentation validation is core to the automation suite. Must know structure first.

---

### REQ-06: AI Context System
**Depends on**:
- REQ-01: Needs layer/stage structure for context chains

**Blocks**:
- REQ-03: Manager roles need context loading rules
- REQ-04: Memory needs to know what context to persist
- REQ-08: Automation needs context rules to validate

*Rationale*: Context gathering is fundamental to how agents operate within the structure.

---

### REQ-07: AI Rules System
**Depends on**:
- REQ-01: Needs structure for rule scope definitions

**Blocks**:
- REQ-08: Automation enforces rules

*Rationale*: Rules define what automation enforces.

---

### REQ-08: AI Automation System
**Depends on**:
- REQ-01: Needs structure to validate
- REQ-05: Needs doc system for path validation
- REQ-06: Needs context rules to validate
- REQ-07: Needs rules to enforce

**Blocks**:
- REQ-02: Setup uses entity scaffolding
- REQ-03: Hierarchy uses agent config scaffolding

*Rationale*: Automation is the enforcement layer. It needs to know what to enforce before it can enforce it.

---

## Implementation Order

Based on dependencies, the optimal implementation order is:

1. **REQ-01** (Layer-Stage) - No dependencies, blocks everything
2. **REQ-05** (Documentation) - Depends only on REQ-01
3. **REQ-06** (Context) - Depends only on REQ-01
4. **REQ-07** (Rules) - Depends only on REQ-01
5. **REQ-08** (Automation) - Depends on 01, 05, 06, 07
6. **REQ-03** (Manager) - Depends on 01, 06, 08
7. **REQ-02** (Setup) - Depends on 01, 08
8. **REQ-04** (Memory) - Depends on 01, 03, 06 (research phase)

## Parallel Opportunities

Some requests can be worked in parallel:

**Parallel Group A** (after REQ-01):
- REQ-05 (Documentation)
- REQ-06 (Context)
- REQ-07 (Rules)

**Parallel Group B** (after REQ-08):
- REQ-02 (Setup)
- REQ-03 (Manager Hierarchy)

## Critical Path

```
REQ-01 → REQ-06 → REQ-08 → REQ-03 → REQ-04
         (most dependencies flow through context and automation)
```
