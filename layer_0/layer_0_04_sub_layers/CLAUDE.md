# Sub-layers (layer_0_04_sub_layers)

## Identity

| Property | Value |
|----------|-------|
| **Layer** | 0 (Universal) |
| **Position** | `layer_0/layer_0_04_sub_layers/` |
| **Role** | **SUB-LAYERS MANAGER** - Foundational content organized by type |

## Purpose

This directory contains universal content that applies across all projects, organized by content type (knowledge, principles, rules, protocols, setup).

---

## Directory Structure

```
layer_0_04_sub_layers/
├── CLAUDE.md                              ← You are here
├── layer_0_00_sub_layer_registry/         ← Registry and metadata
├── sub_layer_0_01_knowledge_system/       ← Domain knowledge
├── sub_layer_0_02_principles/             ← Guiding principles
├── sub_layer_0_03_rules/                  ← Mandatory rules
├── sub_layer_0_04_protocols/              ← Standard protocols
└── sub_layer_0_05+_setup_dependant_hierarchy/  ← Setup-specific content
```

---

## Sub-layers

| Number | Name | Purpose |
|--------|------|---------|
| 00 | `sub_layer_registry` | Sub-layer definitions and metadata |
| 01 | `knowledge_system` | Domain knowledge, reference materials |
| 02 | `principles` | Guiding principles for decisions |
| 03 | `rules` | Mandatory rules (modification protocol, commit rule, etc.) |
| 04 | `protocols` | Session init protocols, context protocols |
| 05+ | `setup_dependant_hierarchy` | OS/tool specific configuration |

---

## Note on Reorganization

The AI system and context agents have been moved to their own directories:

| Content | Old Location | New Location |
|---------|--------------|--------------|
| AALang/GAB | `sub_layer_0_01_ai_system/` | `layer_0/layer_0_01_ai_manager_system/professor/` |
| Context Loading Agent | `sub_layer_0_02_context_agents/` | `layer_0/layer_0_03_context_agents/` |
| Orchestrator | `sub_layer_0_02_context_agents/` | `layer_0/layer_0_01_ai_manager_system/personal/` |

---

## Key Content

| Sub-layer | Key Files |
|-----------|-----------|
| `knowledge_system` | Reference documentation, domain knowledge |
| `principles` | `guiding_principles.md` |
| `rules` | `AI_CONTEXT_MODIFICATION_PROTOCOL.md`, `safety_governance.md` |
| `protocols` | `context_loading_protocol.md`, `universal_init_prompt.md` |
| `setup_dependant_hierarchy` | OS-specific, tool-specific configuration |

---

## Context Chain Position

- **Parent**: `layer_0/CLAUDE.md`
- **Siblings**:
  - `layer_0_01_ai_manager_system/` (AI system)
  - `layer_0_02_manager_handoff_documents/` (IPC)
  - `layer_0_03_context_agents/` (Context loading)

---

## AALang Integration

@agent ctx:ContextLoadingAgent

### On Load

When this file is loaded, update state actors:
- `ctx:ContextLoadingStateActor.loadedFiles` += layer_0_04_sub_layers/CLAUDE.md
- `ctx:NavigationStateActor.inSubLayers` = true

### Available Resources

After loading sub-layers context:
1. Knowledge at `sub_layer_0_01_knowledge_system/`
2. Principles at `sub_layer_0_02_principles/`
3. Rules at `sub_layer_0_03_rules/`
4. Protocols at `sub_layer_0_04_protocols/`
