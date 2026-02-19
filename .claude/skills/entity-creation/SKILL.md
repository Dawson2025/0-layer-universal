---
name: entity-creation
description: "Create new layers, sub-layers, stages, features, projects, or components with proper structure. Use when the user needs a new project, feature, or structural entity in the layer-stage system. Enforces the Stage Completeness Rule (all 12 stages) and canonical entity structure."
---

# Entity Creation Skill

## WHEN to Use
- Creating a new project (`layer_1_project_*`)
- Creating a new feature (`layer_2_feature_*`)
- Creating a new component (`layer_3_component_*`)
- Creating a new research project (`layer_-1_*`)
- Creating stages for an entity
- When the user says "create a new project/feature/component"

## WHEN NOT to Use
- Modifying an existing entity (use normal file editing)
- Creating individual files within an existing entity
- Renaming or reorganizing existing structure

## References (MUST READ BEFORE EXECUTING)

| Reference | Path | Why |
|-----------|------|-----|
| **Canonical structure** | `@imports/entity_structure.md` | **Full directory tree, stage structure, naming conventions, mkdir templates** |
| Instantiation guide | `layer_0/.../entity_lifecycle/INSTANTIATION_GUIDE.md` | Templates for 0AGNOSTIC.md, 0INDEX.md |
| Entity types | `layer_0/.../entity_lifecycle/ENTITY_TYPES.md` | Type-specific details |
| Stages | `layer_0/.../layer_stage_system/STAGES_EXPLAINED.md` | **Stage Completeness Rule** |
| Layers | `layer_0/.../layer_stage_system/LAYERS_EXPLAINED.md` | Layer structure |
| Sub-layers | `layer_0/.../layer_stage_system/SUB_LAYERS_EXPLAINED.md` | Sub-layer types |
| Nested depth | `layer_0/.../layer_stage_system/NESTED_DEPTH_NAMING.md` | subxN naming |

**Full paths**:
- `@imports/` = `0_layer_universal/@imports/`
- `layer_stage_system/` = `layer_0/.0agnostic/01_knowledge/layer_stage_system/`
- `entity_lifecycle/` = `layer_0/.0agnostic/01_knowledge/entity_lifecycle/`

## Protocol

### Step 1: Determine Entity Type and Layer

| Creating a... | Location | Layer N |
|---------------|----------|---------|
| Project | `layer_1/layer_1_projects/` | 1 |
| Feature | `<project>/layer_2_group/layer_2_features/` | 2 |
| Component | `<feature>/layer_3_group/layer_3_components/` | 3 |
| Research project | `layer_-1_research/` | -1 |
| Research feature | `<research>/layer_0_group/layer_0_features/` | 0 |

### Step 2: Create Entity Root Directories

Use the mkdir templates from `@imports/entity_structure.md`. Every entity needs ALL of these at root:

| Directory | Contents | Purpose |
|---|---|---|
| `.0agnostic/` | `01_knowledge/`, `02_rules/{static,dynamic}`, `03_protocols/`, `04_agents/`, `05_skills/`, `06_hooks/scripts/`, `07_episodic_memory/{sessions,changes}`, `08+_setup_dependant/` | On-demand AI resources (numbered subdirs) |
| `.1merge/` | 6 tools × 3 tiers each (18 subdirectories total) | Tool-specific overrides |
| `.claude/` | `rules/`, `episodic_memory/{sessions,changes}/` | Claude Code config |
| `.cursor/` | `rules/`, `episodic_memory/{sessions,changes}/` | Cursor config |
| `.gemini/` | `episodic_memory/{sessions,changes}/` | Gemini config |
| `.codex/` | `episodic_memory/{sessions,changes}/` | Codex config |
| `.github/` | `instructions/` | GitHub config |
| `layer_N_group/` | Full internal structure (see Step 3) | Entity internals (**MUST use _group suffix**) |
| `layer_N+1_group/` | Children container (if applicable) | Child entities (**MUST use _group suffix**) |
| `outputs/` | `episodic_memory/{sessions,changes}/` | Entity-level outputs |
| `synthesis/` | (empty initially) | Cross-cutting summaries |

**The 6 .1merge tools**: `.1claude_merge`, `.1cursor_merge`, `.1gemini_merge`, `.1aider_merge`, `.1codex_merge`, `.1copilot_merge`
**Each tool has 3 tiers**: `0_synced/`, `1_overrides/`, `2_additions/`

### Step 3: Create Internal Structure (layer_N_group/)

```
layer_N_group/
├── layer_N_00_layer_registry/proposals/
├── layer_N_01_ai_manager_system/
├── layer_N_02_manager_handoff_documents/
│   ├── incoming/{from_above,from_below}/
│   └── outgoing/{to_above,to_below}/
└── layer_N_99_stages/
```

Note: Entity-scoped resources (knowledge, rules, protocols, etc.) live in `.0agnostic/` with numbered subdirectories, NOT in a separate sub_layers directory.

### Step 4: [CRITICAL] Create ALL 12 Stages (00-11)

**Stage Completeness Rule**: Create ALL 12 stages. **Empty stages are valid. Missing stages are NOT.**

```bash
# Stage 00 (registry)
mkdir -p "layer_N_group/layer_N_99_stages/stage_N_00_stage_registry/outputs"

# Stages 01-11
for i in 01_request_gathering 02_research 03_instructions 04_planning 05_design 06_development 07_testing 08_criticism 09_fixing 10_current_product 11_archives; do
  mkdir -p "layer_N_group/layer_N_99_stages/stage_N_$i/outputs"
done
```

### Step 5: Add Config Directories to EACH Stage

Every stage gets the same config structure as the entity root:

```bash
for stage_dir in layer_N_group/layer_N_99_stages/stage_N_*/; do
  mkdir -p "$stage_dir"/{.0agnostic/{01_knowledge,02_rules,03_protocols,04_agents,05_skills,06_hooks/scripts,07_episodic_memory/{sessions,changes}},.1merge/{.1claude_merge/{0_synced,1_overrides,2_additions},.1cursor_merge/{0_synced,1_overrides,2_additions},.1gemini_merge/{0_synced,1_overrides,2_additions},.1aider_merge/{0_synced,1_overrides,2_additions},.1codex_merge/{0_synced,1_overrides,2_additions},.1copilot_merge/{0_synced,1_overrides,2_additions}},.claude/{rules,episodic_memory/{sessions,changes}},.cursor/{rules,episodic_memory/{sessions,changes}},.gemini/episodic_memory/{sessions,changes},.codex/episodic_memory/{sessions,changes},.github/instructions,synthesis}
done
```

### Step 6: Create Required Files

#### 6a. Entity root files
- `0AGNOSTIC.md` — See INSTANTIATION_GUIDE.md for template
- `0INDEX.md` — See INSTANTIATION_GUIDE.md for template
- `README.md` — Human-readable overview

#### 6b. Internal directory 0AGNOSTIC.md files
Create `0AGNOSTIC.md` in EVERY directory inside `layer_N_group/`:
- Each internal dir (00-03, sub-layers, stages root)
- Each stage directory
- Run `agnostic-sync.sh` on each to generate CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md

#### 6c. Orchestrator files
| File | Location | Purpose |
|---|---|---|
| `layer_N_orchestrator.gab.jsonld` | Entity root | Entity-level orchestrator |
| `layer_N_99_stages_orchestrator.gab.jsonld` | `layer_N_99_stages/` | Stages orchestrator |

Copy from a sibling entity and adapt names/references.

#### 6d. Stage agent stubs
Create `stage_N_XX_name_agent.jsonld` in each stage directory.

#### 6e. Status tracker
Create `status_N.json` in `layer_N_99_stages/`.

### Step 7: Generate Integration Files

**Every `.jsonld` file MUST have a matching `.integration.md`.**

```bash
# Generate for all .jsonld files
for f in $(find <entity> -name "*.jsonld" -type f); do
  bash tools/jsonld-to-md.sh "$f"
  # Fix naming: tool outputs *.jsonld.integration.md, rename to *.integration.md
  base="${f%.jsonld}"
  if [ -f "${f}.integration.md" ]; then
    mv "${f}.integration.md" "${base}.integration.md"
  fi
done
```

### Step 8: Run agnostic-sync.sh

Generate tool files for ALL 0AGNOSTIC.md files:

```bash
SYNC="layer_0/.0agnostic/agnostic-sync.sh"
for f in $(find <entity> -name "0AGNOSTIC.md" -type f); do
  dir=$(dirname "$f")
  bash "$SYNC" "$dir"
done
```

### Step 9: Update Parent

- Update parent's `0INDEX.md` to include new entity
- Update parent's registry if applicable

### Step 10: Validate

Run `tools/validate-entity.sh <entity-path>` to verify completeness.

## Naming Conventions

| Convention | Rule | Example |
|---|---|---|
| Entity naming | `layer_{N}_{type}_{name}` | `layer_2_feature_assignments` |
| Internal dir | **MUST** use `_group` suffix | `layer_7_group/` (NOT `layer_7/`) |
| Children dir | **MUST** use `_group` suffix | `layer_8_group/` (NOT `layer_8/`) |
| Episodic memory | **MUST** be `episodic_memory` | NOT `episodic/` |
| Agent files | Dot-separation | `name.gab.jsonld` (NOT `name_gab.jsonld`) |

Children are always layer N+1 of their parent.

## Checklist

Before completing, verify ALL of these:

### Structure
- [ ] `.0agnostic/` with numbered subdirs (01_knowledge, 02_rules/{static,dynamic}, 03_protocols, 04_agents, 05_skills, 06_hooks/scripts, 07_episodic_memory/{sessions,changes}, 08+_setup_dependant)
- [ ] `.1merge/` with all 6 tools × 3 tiers = 18 subdirectories
- [ ] `.claude/` with `rules/` AND `episodic_memory/{sessions,changes}/`
- [ ] `.cursor/` with `rules/` AND `episodic_memory/{sessions,changes}/`
- [ ] `.gemini/` with `episodic_memory/{sessions,changes}/`
- [ ] `.codex/` with `episodic_memory/{sessions,changes}/`
- [ ] `.github/instructions/`
- [ ] `layer_N_group/` with _group suffix (NOT bare `layer_N/`)
- [ ] `layer_N+1_group/` with _group suffix (if entity has children)
- [ ] `outputs/episodic_memory/{sessions,changes}/`
- [ ] `synthesis/`

### Stages
- [ ] ALL 12 stages created (00-11) inside `layer_N_group/layer_N_99_stages/`
- [ ] Each stage has config directories (.0agnostic, .1merge, .claude, .cursor, .gemini, .codex, .github, synthesis)
- [ ] Each stage has `0AGNOSTIC.md` + auto-generated tool files
- [ ] Each stage has `stage_N_XX_name_agent.jsonld`
- [ ] Each stage has `stage_N_XX_name_agent.integration.md`

### Files
- [ ] `0AGNOSTIC.md` at entity root with correct identity
- [ ] `0INDEX.md` at entity root
- [ ] `README.md` at entity root
- [ ] `agnostic-sync.sh` run on ALL 0AGNOSTIC.md files (generates CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md)
- [ ] `layer_N_orchestrator.gab.jsonld` at entity root
- [ ] `layer_N_orchestrator.integration.md` at entity root (auto-generated)
- [ ] `layer_N_99_stages_orchestrator.gab.jsonld` in stages dir
- [ ] `layer_N_99_stages_orchestrator.integration.md` in stages dir (auto-generated)
- [ ] `status_N.json` in stages dir
- [ ] Parent's 0INDEX.md updated
- [ ] Parent's registry updated (if applicable)

### Validation
- [ ] Run `tools/validate-entity.sh <entity-path>` — all checks pass

## AALang Reference

Entity creation follows the GAB format defined in:
`layer_0/layer_0_01_ai_manager_system/professor/gab-formats.jsonld`

---

*This skill enforces both the Stage Completeness Rule and the canonical entity structure from `@imports/entity_structure.md`*
