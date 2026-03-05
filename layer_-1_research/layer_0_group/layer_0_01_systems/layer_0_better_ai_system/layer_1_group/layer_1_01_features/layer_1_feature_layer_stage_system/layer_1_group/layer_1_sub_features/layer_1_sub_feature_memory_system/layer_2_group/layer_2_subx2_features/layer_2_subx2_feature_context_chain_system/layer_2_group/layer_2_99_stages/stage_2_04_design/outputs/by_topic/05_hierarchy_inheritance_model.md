---
resource_id: "245a5166-cc7d-451b-a821-c7eec6556768"
resource_type: "output"
resource_name: "05_hierarchy_inheritance_model"
---
# Hierarchy Inheritance Model

**Date**: 2026-02-23
**Status**: Approved, partially enforced
**Scope**: What context propagates across hierarchy levels, what doesn't, and enforcement gaps

---

## Overview

The layer-stage hierarchy forms an inheritance chain. Parent context flows DOWN to children. Children inherit, extend, and can override — but cannot remove parent context. This document defines what propagates, how, and where enforcement gaps remain.

---

## Inheritance Model

```
Parent context flows DOWN to children
Children INHERIT from parents (can extend, can override)
Children CANNOT remove parent context
```

This is analogous to object-oriented inheritance: a child entity inherits all parent rules and knowledge, can add its own, and can specialize behavior — but cannot delete a parent rule.

---

## What Propagates

### Always Propagates (Inherited by ALL children)

| Context | Source | Mechanism | Status |
|---------|--------|-----------|--------|
| Universal rules | `.0agnostic/02_rules/` at root | CLAUDE.md cascade (filesystem walk) | Enforced |
| Safety governance | `.0agnostic/02_rules/static/` | CLAUDE.md cascade | Enforced |
| Modification protocol | Root CLAUDE.md | CLAUDE.md cascade | Enforced |
| Commit/push rules | Root CLAUDE.md | CLAUDE.md cascade | Enforced |
| Stage Completeness Rule | Root CLAUDE.md | CLAUDE.md cascade | Enforced |

These propagate because Claude Code auto-loads every CLAUDE.md in the filesystem path from root to working directory. The CLAUDE.md cascade is the primary enforcement mechanism for universal context.

### Propagates to Immediate Children

| Context | Source | Mechanism | Status |
|---------|--------|-----------|--------|
| `conventions.childNaming` | Parent 0AGNOSTIC.md / index.jsonld | Agent reads parent before creating child | **Not enforced** — agent must explicitly check |
| Layer number (parent + 1) | Parent entity's layer field | Agent calculates during entity creation | **Not enforced** — agent must manually calculate |
| Triggers | Parent 0AGNOSTIC.md | Inherited unless overridden | **Defined but not enforced** |
| Parent reference | Convention: `**Parent**: path` in child 0AGNOSTIC.md | Agent writes during entity creation | Enforced by chain validation |

### Optional Propagation

| Context | Source | Mechanism | Status |
|---------|--------|-----------|--------|
| `rel:treeOfNeedsBranch` | Parent feature | Guides child organization | Optional |
| Design decisions | Parent stage_04 outputs | Referenced by child research/design | Convention only |
| Episodic memory | Parent .0agnostic/04_episodic_memory/ | Cross-session by convention | Not automated |

---

## Propagation Mechanisms

### 1. CLAUDE.md Cascade (Static, Always-Loaded)

```
~/CLAUDE.md
  └── dawson-workspace/CLAUDE.md
        └── code/CLAUDE.md
              └── 0_layer_universal/CLAUDE.md
                    └── layer_-1_research/CLAUDE.md
                          └── ...down to working directory
```

Claude Code auto-loads every CLAUDE.md from root to working directory at session start. This is the most reliable propagation mechanism — it cannot be bypassed.

**What it carries**: Identity, critical rules, triggers, navigation pointers
**What it doesn't carry**: Detailed knowledge, protocols, episodic memory (too large)

### 2. 0AGNOSTIC Parent Chain (Dynamic, On-Demand)

```
context_chain_system/0AGNOSTIC.md
  ↑ Parent: ../../../0AGNOSTIC.md
memory_system/0AGNOSTIC.md
  ↑ Parent: ../../../0AGNOSTIC.md
...up to root
```

Each 0AGNOSTIC.md has a `**Parent**:` reference. Agents can traverse upward to load broader scope. This is on-demand — the agent must explicitly follow the chain.

**What it carries**: Full entity identity, behaviors, triggers, status, navigation
**What it doesn't carry**: Only what's in 0AGNOSTIC.md — not .0agnostic/ content

### 3. .0agnostic/ Resource Inheritance (Convention)

Children don't literally inherit parent .0agnostic/ content. Instead:
- Children reference parent knowledge by relative path (e.g., `../../.0agnostic/01_knowledge/`)
- Universal artifacts are placed at the root .0agnostic/ level
- Per-entity artifacts stay at the entity level

**What it carries**: Whatever the agent explicitly loads
**What it doesn't carry**: Nothing auto-propagates

### 4. Hot Rule Promotion (agnostic-sync.sh)

Rules with `promote: hot` frontmatter get a summary pointer injected into ALL generated tool files at that entity level. This ensures agents always see critical rules without reading .0agnostic/ directly.

```yaml
---
promote: hot
hot_trigger: "When this condition is met"
hot_summary: "Do this thing. Full rule: path/to/rule.md"
---
```

**What it carries**: 1-line summary + path pointer per promoted rule
**What it doesn't carry**: Full rule content (stays cold; agent reads on demand)

---

## Propagation Gaps (Known Issues)

### Gap 1: conventions.childNaming not enforced

```
DEFINED IN: parent/index.jsonld or 0AGNOSTIC.md
  → "conventions": { "childNaming": { "pattern": "layer_{N+1}_*" } }

SHOULD FLOW TO: Agent creating child entity

ACTUALLY FLOWS TO: Nothing — agent doesn't read it unless explicitly told

RESULT: Agent creates wrong naming (e.g., "subfeature_*" instead of "layer_1_subx2_feature_*")
```

**Mitigation**: The `/entity-creation` skill reads entity_structure.md which defines naming conventions. Using the skill prevents this gap.

### Gap 2: Layer number not calculated automatically

```
PARENT HAS: "layer": 0
CHILD SHOULD HAVE: "layer": 1 (0 + 1)
ACTUALLY: Agent must manually calculate and set
```

**Mitigation**: The `/entity-creation` skill handles this. Also documented in NESTED_DEPTH_NAMING.md.

### Gap 3: No visibility into inherited context

```
QUESTION: "What context does this entity have access to?"
ANSWER: Unknown without manually tracing ancestry
NEED: Tool to show inherited context at any point
```

**Mitigation**: The `/chain-validate` skill traverses the chain and reports. The chain_visualization child entity (layer 4) is designed to address this.

### Gap 4: Dynamic rules don't inherit across entities

Parent dynamic rules (e.g., `sync_after_agnostic_edit.md`) don't automatically apply to children. Each entity must define its own dynamic rules or explicitly reference parent rules.

**Mitigation**: Universal rules that must apply everywhere should use hot promotion or be placed in the root .0agnostic/02_rules/static/ with `promote: hot` frontmatter.

---

## Propagation Rules Summary

| Context | Source | Should Propagate | Actually Propagates | Enforcement |
|---------|--------|------------------|---------------------|-------------|
| Universal rules | root .0agnostic/02_rules/ | Always | Yes (CLAUDE.md cascade) | Automatic |
| Modification protocol | Root CLAUDE.md | Always | Yes (CLAUDE.md cascade) | Automatic |
| Parent reference | Convention in 0AGNOSTIC.md | Always | Yes (if agent follows convention) | Chain validation skill |
| conventions.childNaming | Parent 0AGNOSTIC.md | On child creation | Only if agent reads parent | `/entity-creation` skill |
| Layer number | Parent layer + 1 | On child creation | Only if agent calculates | `/entity-creation` skill |
| Triggers | Parent 0AGNOSTIC.md | Inherited | Not enforced | Convention |
| Hot-promoted rules | `promote: hot` frontmatter | Always at entity level | Yes (agnostic-sync.sh) | Automatic |
| Detailed knowledge | .0agnostic/01_knowledge/ | On demand | Only if agent reads | Convention |

---

## Related Documents

- **Chain structure**: `.0agnostic/01_knowledge/context_chain_architecture.md`
- **Chain validation**: `.0agnostic/03_protocols/chain_validation_protocol.md`
- **Entity creation**: `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`
- **Discovery temperatures**: `08_discovery_temperature_model.md`
- **Propagation chain**: `03_propagation_chain_architecture.md`
