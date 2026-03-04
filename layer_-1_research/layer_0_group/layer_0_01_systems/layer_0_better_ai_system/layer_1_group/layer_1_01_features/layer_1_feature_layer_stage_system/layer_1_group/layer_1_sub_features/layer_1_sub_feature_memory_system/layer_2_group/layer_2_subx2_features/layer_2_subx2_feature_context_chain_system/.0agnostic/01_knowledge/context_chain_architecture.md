# Context Chain Architecture

**Layer**: layer_2 (Research Sub-Feature)
**Stage**: 02_research → 05_design
**Date**: 2026-02-17
**Topic**: How context flows through the layer-stage hierarchy via parent chains

---

## Overview

A **context chain** is the sequence of `0AGNOSTIC.md` files linked by `Parent:` references that forms the inheritance path from any entity to the system root. Every entity in the layer-stage system participates in exactly one chain.

The chain serves two purposes:
1. **Inheritance**: context, rules, and knowledge flow downward from parent to child
2. **Navigation**: agents can traverse upward to find broader scope or escalate

---

## Chain Structure

### The 0AGNOSTIC Parent Chain

Each `0AGNOSTIC.md` contains a `**Parent**: \`../path/0AGNOSTIC.md\`` reference. Following these links produces a chain:

```
context_chain_system/0AGNOSTIC.md
  ↑ Parent: ../../../0AGNOSTIC.md
memory_system/0AGNOSTIC.md
  ↑ Parent: ../../../0AGNOSTIC.md
layer_stage_system/0AGNOSTIC.md
  ↑ Parent: ../0AGNOSTIC.md
layer_0_features/0AGNOSTIC.md
  ↑ Parent: ../0AGNOSTIC.md
layer_0_group/0AGNOSTIC.md
  ↑ Parent: ../0AGNOSTIC.md
better_ai_system/0AGNOSTIC.md
  ↑ Parent: ../0AGNOSTIC.md
layer_-1_research/0AGNOSTIC.md
  ↑ (no parent — root reached)
```

**Depth**: 7 levels for the context_chain_system entity.

### Chain vs CLAUDE.md Cascade

These are two **independent** chain mechanisms:

| Aspect | 0AGNOSTIC Chain | CLAUDE.md Cascade |
|--------|----------------|-------------------|
| **Direction** | Explicit upward via Parent refs | Implicit upward via filesystem walk |
| **Trigger** | Agent reads 0AGNOSTIC.md and follows Parent | Claude Code auto-loads at session start |
| **Timing** | Dynamic (on-demand) | Static (always loaded) |
| **Scope** | Layer-stage hierarchy only | Any filesystem directory |
| **Content** | Source of truth (Identity, Triggers, Pointers) | Generated summaries (from agnostic-sync.sh) |

Both mechanisms produce context inheritance but serve different roles. The 0AGNOSTIC chain is the **canonical** path; the CLAUDE.md cascade is the **delivery** mechanism for Claude Code specifically.

---

## Chain Construction Rules

### Relative Path Convention

Parent references use **relative paths**, not absolute:
- `**Parent**: \`../0AGNOSTIC.md\`` — parent is one directory up
- `**Parent**: \`../../../0AGNOSTIC.md\`` — parent is three directories up (through group/sub-features/feature structure)

### Depth Calculation

Depth varies by entity type in the layer-stage system:

| Entity Depth | Structure Pattern | Typical `../` Count |
|--------------|-------------------|---------------------|
| Research project | `layer_-1_research/project/` | 1 (`../`) |
| Feature (layer 0) | `.../layer_0_features/feature/` | 1 (`../`) |
| Sub-feature (layer 1) | `.../layer_1_subx2_features/sub_feature/` | 3 (`../../../`) |
| Sub-sub-feature (layer 2) | `.../layer_2_subx2_features/sub_feature/` | 3 (`../../../`) |

The extra `../` levels traverse the `layer_N_group/layer_N_*_features/` container structure.

### Container vs Entity Nodes

Not every directory in the chain is a full entity:

| Type | Has stages? | Has orchestrator? | Chain role |
|------|------------|-------------------|------------|
| Entity | Yes (11 stages) | Full GAB (5 modes) | Research/work node |
| Container | No | Lightweight GAB (3 modes) | Routing/registry node |

Containers (like `layer_0_group/`, `layer_0_features/`) exist for organizational routing. Entities (like `layer_stage_system`, `memory_system`) are where actual research work happens.

---

## Chain Traversal Algorithm

```
function traverse_chain(entity_path):
    current = entity_path + "/0AGNOSTIC.md"
    chain = []

    while current exists:
        content = read(current)
        chain.append({path: current, identity: extract_identity(content)})

        parent_ref = extract_parent(content)
        if parent_ref is None:
            break  # root reached

        current = resolve_relative(dirname(current), parent_ref)

    return chain  # ordered leaf → root
```

### Traversal Uses

| Use Case | Direction | When |
|----------|-----------|------|
| Context loading | Leaf → Root | Before starting work (gather full context) |
| Escalation | Leaf → Root | When task exceeds current scope |
| Delegation | Root → Leaf | When routing task to specific entity |
| Validation | Both | Testing chain integrity |

---

## Related Documents

- Chain visualization: `layer_3_group/.../chain_visualization/diagrams/current/context_chain/`
- Context loading: `sub_layer_2_01_knowledge_system/overview/production_context_system/HOW_CONTEXT_WORKS.md`
- Avenue redundancy: `./avenue_web_architecture.md`
