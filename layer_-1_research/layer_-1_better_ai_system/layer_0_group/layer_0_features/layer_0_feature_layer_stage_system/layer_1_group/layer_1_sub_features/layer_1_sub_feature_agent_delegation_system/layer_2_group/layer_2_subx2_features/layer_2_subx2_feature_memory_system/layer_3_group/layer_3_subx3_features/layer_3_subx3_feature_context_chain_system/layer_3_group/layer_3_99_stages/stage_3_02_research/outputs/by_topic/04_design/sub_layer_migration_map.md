# Design — Sub-Layer Migration Map

## Purpose

Detailed mapping of every directory and file category in the current sub-layer hierarchy to its new location inside `.0agnostic/`. This document serves as the execution reference for the migration.

---

## Migration Overview

```
BEFORE                                          AFTER
──────                                          ─────
layer_0/layer_0_04_sub_layers/                  layer_0/.0agnostic/
├── sub_layer_0_01_knowledge_system/    ──→     ├── knowledge/
│   └── principles/                     ──→     │   └── principles/
├── sub_layer_0_02_rules/               ──→     ├── rules/
│   ├── static/ (0_every_api_request/)  ──→     │   ├── static/
│   └── dynamic/ (1_scenario_based/)    ──→     │   └── dynamic/
├── sub_layer_0_03_protocols/           ──→     ├── protocols/
└── sub_layer_0_04+_setup_dependant/    ──→     └── knowledge/setup/
                                                     + .1merge/ (OS-specific)
```

---

## sub_layer_0_01_knowledge_system/ → .0agnostic/knowledge/

### aalang_gab_system/ → knowledge/aalang_gab_system/

| File | Action | Rationale |
|------|--------|-----------|
| `agent_patterns.md` | Move | AALang reference doc |
| `gab_compiler.md` | Move | GAB compiler reference |
| `jsonld_design_vs_runtime.md` | Move | Design-time vs runtime guidance |
| `mode_actor_pattern.md` | Move | Pattern reference |
| `professor_docs_analysis.md` | Move | Analysis reference |
| `runtime_and_formats.md` | Move | Format comparison |
| `README.md` | Move | Directory index |

### agent_coordination/ → knowledge/agent_coordination/

| File | Action | Rationale |
|------|--------|-----------|
| `HANDOFF_PROTOCOLS.md` | Move | Reference doc for handoff patterns |
| `MULTI_AGENT_PATTERNS.md` | Move | Multi-agent reference |
| `SCOPE_VS_DELEGATION.md` | Move | Scope design reference |
| `0INDEX.md` | Move | Directory index |

### context_loading/ → knowledge/context_loading/

| File | Action | Rationale |
|------|--------|-----------|
| `HOW_CONTEXT_WORKS.md` | Move | Context loading reference |

### entity_lifecycle/ → knowledge/entity_lifecycle/

| File | Action | Rationale |
|------|--------|-----------|
| `ENTITY_TYPES.md` | Move | Entity type reference |
| `INSTANTIATION_GUIDE.md` | Move | Entity creation reference (also used by /entity-creation skill) |
| `MAINTENANCE_GUIDE.md` | Move | Entity maintenance reference |

### layer_stage_system/ → knowledge/layer_stage_system/

| File | Action | Rationale |
|------|--------|-----------|
| `OVERVIEW.md` | Move | System overview |
| `LAYERS_EXPLAINED.md` | Move | Layer reference |
| `STAGES_EXPLAINED.md` | Move | Stage reference |
| `SUB_LAYERS_AS_ENTRY_POINTS.md` | **Review** | May need rewriting since sub-layers are being dissolved |
| `SUB_STAGES_EXPLAINED.md` | Move | Sub-stage reference |
| `NESTED_DEPTH_NAMING.md` | Move | Naming convention reference |
| `0INDEX.md` | Move | Directory index |

### naming_conventions/ → knowledge/naming_conventions/

| File | Action | Rationale |
|------|--------|-----------|
| `HIERARCHY_NAMING_CONVENTION.md` | Move | Naming reference |

### navigation_patterns/ → knowledge/navigation_patterns/

| File | Action | Rationale |
|------|--------|-----------|
| `TRAVERSAL_GUIDE.md` | Move | Navigation reference |

### principles/ → knowledge/principles/

| File | Action | Rationale |
|------|--------|-----------|
| `README.md` | Move | Principles overview |
| Short critical principles | **Also extract** to `rules/static/principles.md` | Core principles should be auto-loaded |

### software_engineering_knowledge_system/ → knowledge/software_engineering/

| File | Action | Rationale |
|------|--------|-----------|
| `README.md` | Move | Overview |
| `0_instruction_docs/MASTER_KNOWLEDGE_MAP.md` | Move | Knowledge map |
| `0_instruction_docs/checklists/ic-path.md` | Move | Checklist reference |
| `0_instruction_docs/diagrams/knowledge-map-overview.mermaid` | Move | Diagram |

---

## sub_layer_0_02_rules/ → .0agnostic/rules/

### 0_every_api_request/ → rules/static/

These are rules that must be followed in EVERY session. They belong in `rules/static/` and get synced to `.claude/rules/` for auto-loading.

| File | Action | Rationale |
|------|--------|-----------|
| `AI_CONTEXT_COMMIT_PUSH_RULE.md` | Move to `rules/static/` | Universal rule, always needed |
| `AI_CONTEXT_MODIFICATION_PROTOCOL.md` | Move to `rules/static/` | Universal rule, always needed |
| `CONTEXT_TRAVERSAL_RULE.md` | Move to `rules/static/` | Universal rule, always needed |
| `README.md` | Dissolve | Not needed — rules are self-describing |

### 1_scenario_based/ → rules/dynamic/

These are rules that apply in specific situations. They belong in `rules/dynamic/` with YAML frontmatter for path-scoping.

| File | Action | New paths: frontmatter |
|------|--------|----------------------|
| `AI_DOCUMENTATION_PROTOCOL.md` | Move to `rules/dynamic/` | `paths: **/*.md` or always-loaded |
| `CONTEXT_FILE_PATTERN.md` | Move to `rules/dynamic/` | `paths: **/CLAUDE.md, **/0AGNOSTIC.md` |
| `CROSS_OS_COMPATIBILITY_RULES.md` | Move to `rules/dynamic/` | `paths: sub_layer_0_05_*/**` → `knowledge/setup/**` |
| `LAYER_CONTEXT_HEADER_PROTOCOL.md` | Move to `rules/dynamic/` | Evaluate scope |
| `LOCATION_RULE_APPLICATION_PROTOCOL.md` | Move to `rules/dynamic/` | Evaluate scope |
| `OUTPUT_FIRST_PROTOCOL.md` | Move to `rules/dynamic/` | All directories |
| `safety_governance.md` | Move to `rules/dynamic/` | Security-related paths |
| `sequential_development_methodology.md` | Move to `rules/dynamic/` | Development paths |
| `README.md` | Dissolve | Not needed |

### Root-level rule files

| File | Action | Rationale |
|------|--------|-----------|
| `FILE_PATH_LINKING_RULE.md` | Move to `rules/static/` | Universal rule |
| `AI_CONTEXT_PROPOSAL_REQUIREMENTS.md` | Move to `rules/static/` | Universal rule |
| `context_priority_rules.md` | Move to `rules/static/` | Universal rule |
| `context_scope_boundaries.md` | Move to `rules/static/` | Universal rule |
| `README.md` | Dissolve | Not needed |

### 0_instruction_docs/ → knowledge/instruction_docs/

These are NOT rules — they are reference documentation that currently lives inside the rules directory. They should be knowledge.

| Content | Action | Rationale |
|---------|--------|-----------|
| `MASTER_DOCUMENTATION.md` | Move to `knowledge/instruction_docs/` | Reference doc |
| `MASTER_TERMINAL_EXECUTION_REFERENCE.md` | Move to `knowledge/instruction_docs/` | Reference doc |
| `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md` | Move to `knowledge/instruction_docs/` | Reference doc |
| `UNIVERSAL_DOCUMENTATION_SYSTEM.md` | Move to `knowledge/instruction_docs/` | Reference doc |
| All other instruction docs | Move to `knowledge/instruction_docs/` | Reference docs |
| `agent-patterns/` | Move to `knowledge/instruction_docs/agent-patterns/` | Reference |
| `initialization/` | Move to `knowledge/instruction_docs/initialization/` | Reference |
| `integrated_from_projects/` | Move to `knowledge/instruction_docs/integrated/` | Reference |

### 1_status_progress_docs/ → Evaluate

| File | Action | Rationale |
|------|--------|-----------|
| `SESSION_SUMMARY_NOV_11_2025_*.md` | Move to `episodic_memory/` or archive | Session record, not a rule |

### 3_archive_docs/ → Archive or delete

| Content | Action | Rationale |
|---------|--------|-----------|
| `20251023_*.md` resolution docs | Archive | Historical, not active |
| `CURSOR_*.md` | Archive or `.1merge/.1cursor_merge/` | Cursor-specific historical |
| `TERMINAL_*.md` | Archive | Historical solutions |

### sub_layer_0_04_99_stages/ → Evaluate per stage

The rules sub-layer has its own stage hierarchy. This needs case-by-case evaluation:

| Stage | Content | Action |
|-------|---------|--------|
| `stage_0_01_request_gathering/outputs/tree_of_needs/` | Extensive needs analysis (30+ files) | Move to `knowledge/rule_development/tree_of_needs/` |
| `stage_0_02_research/outputs/` | Research findings | Move to `knowledge/rule_development/research/` |
| `stage_0_03-11_*` | Empty stages | Delete (only CLAUDE.md files) |
| `status.json` | Stage progress tracking | Evaluate if still needed |

---

## sub_layer_0_03_protocols/ → .0agnostic/protocols/

| File | Action | Rationale |
|------|--------|-----------|
| `context_loading_protocol.md` | Move to `protocols/` | Workflow procedure |
| `context_quality_checklist.md` | Move to `protocols/` | Quality checklist |
| `features_init_prompt.md` | Move to `protocols/` | Feature initialization procedure |
| `universal_init_prompt.md` | Move to `protocols/` | Universal init procedure |
| `what_to_do_next.md` | Move to `protocols/` | Decision procedure |
| `HIERARCHY_ADOPTION_CHECKLIST.md` | Move to `protocols/` | Adoption procedure |
| `HIERARCHY_QUICK_START.md` | Move to `protocols/` | Quick start procedure |
| `MIGRATION_GUIDE.md` | Move to `protocols/` | Migration procedure |
| `README.md` | Dissolve | Not needed |

**Sync behavior:** Each protocol file is transformed into a `.claude/skills/*/SKILL.md` by `agnostic-sync.sh`. The protocol name becomes the skill name. WHEN/WHEN NOT conditions are extracted or added during sync.

---

## sub_layer_0_04+_setup_dependant/ → Split

Setup-dependent content splits between knowledge and .1merge/:

| Content | New Location | Rationale |
|---------|-------------|-----------|
| `_shared/` docs | `knowledge/setup/shared/` | Cross-platform reference |
| `sub_layer_0_05_linux_ubuntu/` | `.1merge/` or `knowledge/setup/linux/` | OS-specific |
| `sub_layer_0_05_macos/` | `.1merge/` or `knowledge/setup/macos/` | OS-specific |
| `sub_layer_0_05_windows/` | `.1merge/` or `knowledge/setup/windows/` | OS-specific |
| `sub_layer_0_05_wsl/` | `.1merge/` or `knowledge/setup/wsl/` | OS-specific |
| Firebase docs | `knowledge/setup/shared/firebase/` | Deployment reference |
| GitHub SSO docs | `knowledge/setup/shared/github/` | Auth reference |
| VSCode docs | `knowledge/setup/shared/vscode/` | Editor reference |
| Deployment docs | `knowledge/setup/shared/deployment/` | Deployment reference |

---

## Sync Conflict Files

Multiple `.sync-conflict-*` files exist in the sub-layers (from Syncthing). During migration:

1. Compare each sync-conflict file with its original
2. Keep the newer/correct version
3. Delete all sync-conflict copies
4. This is a cleanup opportunity

---

## Migration Sequence

### Phase 1: Create Target Structure
1. Create subdirectories inside `layer_0/.0agnostic/`: `knowledge/`, `knowledge/principles/`, `rules/static/`, `rules/dynamic/`, `protocols/`
2. The rest of the `.0agnostic/` structure already exists

### Phase 2: Move Knowledge Files
1. Move all `sub_layer_0_01_knowledge_system/` subdirectories to `.0agnostic/knowledge/`
2. Clean up sync-conflict files
3. Update any @import references in CLAUDE.md files

### Phase 3: Move Rules
1. Move `0_every_api_request/` files to `.0agnostic/rules/static/`
2. Move `1_scenario_based/` files to `.0agnostic/rules/dynamic/` (add YAML frontmatter)
3. Move root-level rule files to `.0agnostic/rules/static/`
4. Move `0_instruction_docs/` to `.0agnostic/knowledge/instruction_docs/`
5. Archive `3_archive_docs/`
6. Move stage content to `knowledge/rule_development/`

### Phase 4: Move Protocols
1. Move all protocol files to `.0agnostic/protocols/`
2. Clean up sync-conflict files

### Phase 5: Handle Setup-Dependent
1. Move `_shared/` to `.0agnostic/knowledge/setup/shared/`
2. Move OS-specific content to `.0agnostic/knowledge/setup/{os}/` or `.1merge/`

### Phase 6: Update References
1. Update all CLAUDE.md @import paths
2. Update skill references to new locations
3. Update `~/.claude/CLAUDE.md` scenario-based rule paths
4. Run `agnostic-sync.sh` to regenerate tool files

### Phase 7: Clean Up
1. Delete empty `layer_0_04_sub_layers/` directory
2. Remove the `layer_0_00_sub_layer_registry/` (no longer needed)
3. Update 0INDEX.md files

---

## File Count Summary

| Category | File Count | New Location |
|----------|-----------|-------------|
| Knowledge docs | ~38 | `.0agnostic/knowledge/` |
| Static rules | ~8 | `.0agnostic/rules/static/` |
| Dynamic rules | ~9 | `.0agnostic/rules/dynamic/` |
| Instruction docs (reclassified from rules) | ~30+ | `.0agnostic/knowledge/instruction_docs/` |
| Archive docs | ~10 | Archive or delete |
| Stage content | ~40+ | `.0agnostic/knowledge/rule_development/` |
| Protocols | ~10 | `.0agnostic/protocols/` |
| Setup-dependent | ~100+ | `.0agnostic/knowledge/setup/` + `.1merge/` |
| Registry | ~15 | Delete (no longer needed) |

---

*Migration map for sub-layer dissolution into .0agnostic/*
*Created: 2026-02-16*
