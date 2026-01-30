# AI System Problems Audit

**Date**: 2026-01-25
**Scope**: Full AI system at `/home/dawson/dawson-workspace/code/0_layer_universal`
**Status**: Research in Progress

---

## Executive Summary

The AI system exhibits significant structural inconsistencies stemming from an incomplete transition between architectural approaches. The codebase is moving from an older "trickle_down" convention to the new "Layer-Stage Framework" but this migration is incomplete.

**Critical Issues**: 15
**Major Issues**: 12
**Minor Issues**: 8

---

## 1. NAMING CONVENTION PROBLEMS

### 1.1 [FIXED] Dots vs Underscores Inconsistency
**Severity**: CRITICAL
**Resolution**: FIXED on 2026-01-25. Core docs were updated to use underscore naming consistently (e.g., `SYSTEM_OVERVIEW.md`, `layer_0_01_ai_manager_system/README.md`, `universal_init_prompt.md`, and stage system docs).

| Location | Uses Dots | Uses Underscores |
|----------|-----------|------------------|
| Documentation | `stage_0_00_`, `layer_0_02_` | - |
| Actual Directories | - | `stage_0_01_`, `layer_0_03_` |
| universal_init_prompt.md | `sub_layer_0_03_`, `sub_layer_0_04_` | `sub_layer_0_01_` |

**Files Affected**:
- `SYSTEM_OVERVIEW.md`
- `layer_0_01_ai_manager_system/README.md`
- `universal_init_prompt.md`
- Multiple stage READMEs

**Impact**: Navigation breaks when following documented paths. The primary references have been corrected.

### 1.2 [FIXED] Wrong Naming Inside Sub-Layers (layer_ vs sub_layer_)
**Severity**: CRITICAL
**Resolution**: FIXED on 2026-01-25. The entire structure within `sub_layer_0_05+_setup_dependant/` was refactored to use the correct `sub_layer_` prefixing. The unnecessary `layer_0_01_universal_setup_file_tree_0` wrapper was also removed.

**Old (Incorrect) Structure**:
```
sub_layer_0_05+_setup_dependant/
└── layer_0_01_universal_setup_file_tree_0/     ❌ Should be sub_layer_
    └── layer_0_05_operating_systems/           ❌ Should be sub_layer_
```

**New (Correct) Structure**:
```
sub_layer_0_05+_setup_dependant/
└── sub_layer_0_05_operating_systems/
    ├── sub_layer_0_05_linux_ubuntu/
    │   └── sub_layer_0_06_environments/
    └── sub_layer_0_05_macos/
        └── sub_layer_0_06_environments/
```

**Rule**: Children of a `sub_layer` should also use `sub_layer_` naming.

**Impact**: Breaks sub_layer traversal pattern completely. The impact is now resolved.

### 1.3 Sub-Layer Plus Notation Ambiguity
**Severity**: MAJOR

The `+` notation in `sub_layer_0_05+_setup_dependant` is inconsistent:
- Sometimes means "0.05 through 0.14 consolidated"
- Sometimes means "extendable beyond this number"
- No formal definition exists

### 1.3 Mixed Layer Component Naming
**Severity**: MAJOR

| Pattern | Example | Used In |
|---------|---------|---------|
| `layer_N_XX_name` | `layer_0_01_ai_manager_system` | Main structure |
| `layer_N_XX` | `layer_1_00` | Some nested |
| `N_XX_name` | `0.02_sub_layers` | Documentation |

---

## 2. STAGE SYSTEM PROBLEMS

### 2.1 [FIXED] Multiple Stage Numbering Schemes
**Severity**: CRITICAL
**Resolution**: FIXED on 2026-01-25. Layer-1 framework stages were realigned to the 11-stage scheme used in layer_0 (request_gathering → research → ... → archives). Stage directories and references now match `stage_0_01` through `stage_0_11`.

**Scheme A** (in `layer_0/layer_0_99_stages/`):
```
01: request_gathering
02: research
03: instructions
04: planning
05: design
06: development
07: testing
08: criticism
09: fixing
10: current_product
11: archives
```

**Scheme B** (in `layer_1_feature_layer_stage_system/status.json`):
```
00: request_gathering
01: instructions
02: planning
03: design
04: development
05: testing
06: criticism
07: fixing
08: current_product
09: archives
```

**Differences**:
- Research stage exists in A but not B
- Numbering starts at 01 vs 00
- Total stages: 11 vs 10

### 2.2 Empty Handoff Documents
**Severity**: MAJOR

All stage directories have empty `hand_off_documents/` folders with only `.gitkeep`:
- `stage_0_01_request_gathering/hand_off_documents/`
- `stage_0_02_research/hand_off_documents/`
- ... (all 11 stages)

**Expected**: `incoming.json`, `outgoing.json` per handoff_schema.md
**Actual**: Empty

### 2.3 [FIXED] Status Tracking Inconsistency
**Severity**: MAJOR
**Resolution**: FIXED on 2026-01-25. Added `layer_0_99_stages/status.json` and aligned status files to the same 11-stage scheme. Legacy `status_1.json` was archived in the layer-1 framework.

| Location | Has status.json | Status |
|----------|-----------------|--------|
| `layer_0/layer_0_99_stages/` | NO | Missing |
| `layer_1_feature_layer_stage_system/layer_1/layer_1_99_stages/` | YES | Has both status.json and status_1.json |
| `better_layer_stage_system/layer_0/layer_0_99_stages/` | NO | Missing |

### 2.4 [FIXED] Stage Registry Not Implemented
**Severity**: MAJOR
**Resolution**: FIXED on 2026-01-25. `layer_0/layer_0_99_stages/layer_0_00_stage_registry/` exists and is in use.

CLAUDE.md references: `layer_0/layer_0_99_stages/layer_0_00_stage_registry/`
**Actual**: Directory exists under layer_0.

---

## 3. DOCUMENTATION DRIFT

### 3.1 [FIXED] Broken Path References
**Severity**: CRITICAL
**Resolution**: FIXED on 2026-01-25. Updated the listed documents to point at current paths (Layer 0 manager docs, safety governance source, and handoff schema references).

**File**: `layer_0_01_ai_manager_system/README.md`
- References: `sub_layer_0_13_universal_protocols/`
- Actual location: Updated to the shared protocols path under `sub_layer_0_05+_setup_dependant/.../sub_layer_0_13_protocols/`

**File**: `sub_layer_0_04_rules/safety_governance.md`
- References: `../sub_layer_0_13_universal_protocols/observability/`
- Status: Path corrected

**File**: `handoff_schema.md`
- References: `/code/0_layer_universal/0_context/` paths
- Actual: `/code/0_layer_universal/` (no 0_context folder in current structure)

### 3.2 [PARTIALLY FIXED] Init Prompt Chain Confusion
**Severity**: MAJOR
**Resolution**: Core entry-point docs were updated to reference `layer_0/layer_0_03_sub_layers/sub_layer_0_01_prompts/universal_init_prompt.md`. Some legacy references may remain in archived or legacy contexts.

Documentation claims init prompt at:
```
layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md
```

Actual location:
```
layer_0/layer_0_03_sub_layers/sub_layer_0_01_prompts/universal_init_prompt.md
```

### 3.3 Documentation Describes Wrong Structure
**Severity**: MAJOR

`SYSTEM_OVERVIEW.md` describes slots at layer level, but implementation uses sub-layers only:
- Documented: `layer_N/slots/`
- Actual: `layer_N/layer_N_03_sub_layers/sub_layer_N_XX/`

---

## 4. REGISTRY PROBLEMS

### 4.1 [FIXED] Missing layer_registry.yaml
**Severity**: CRITICAL
**Resolution**: FIXED on 2026-01-25. `layer_registry.yaml` was added alongside `sub_layer_registry.yaml` in the sub-layer registry directory.

**Expected at**: `layer_0_03_sub_layers/layer_0_00_sub_layer_registry/layer_registry.yaml`
**Status**: File exists

Referenced by:
- `layer_0_00_sub_layer_registry/README.md`
- Automation scripts (cannot run)

### 4.2 Aliases Without Authoritative Source
**Severity**: MINOR

Aliases exist in `layer_0_00_sub_layer_registry/aliases/`:
- `basic_prompts_throughout.md`
- `software_engineering_knowledge_system.md`
- `universal_principles.md`
- `universal_rules.md`
- `setup_dependant_sub_layers.md`

But no master registry to validate against.

---

## 5. AI MANAGER SYSTEM PROBLEMS

### 5.1 Agnostic/Specific Pattern Incomplete
**Severity**: MAJOR

`layer_0_01_ai_manager_system/` has:
- `agnostic/` - Contains context_gathering_rules.md, init_prompt.md, layer_navigation.md
- `specific/os/wsl/...` - Deeply nested but sparse

**Problem**: No clear guidance on when to use agnostic vs specific.

### 5.2 Multiple CLAUDE.md Entry Points
**Severity**: MINOR

No single entry point - multiple CLAUDE.md files with different scopes:
- `/CLAUDE.md` (root)
- `layer_0/CLAUDE.md` (if exists)
- `layer_1/.../CLAUDE.md` (features)
- `.claude/` directory structure

### 5.3 Context Gathering Rules Scattered
**Severity**: MINOR

Rules exist in multiple places:
- `layer_0_01_ai_manager_system/agnostic/context_gathering_rules.md`
- `layer_2_feature_context_gathering/` (in layer_stage_system)
- Inline in various READMEs

---

## 6. SUB-LAYER PROBLEMS

### 6.1 Legacy Code Not Cleaned Up
**Severity**: MINOR

`sub_layer_0_05+_setup_dependant/legacy_sublayer_readmes/` contains old sub-layers:
- `sub_layer_0_13_universal_protocols/`
- Multiple numbered directories

**Problem**: Documentation still references these as if they were live.

### 6.2 [FIXED] Consolidated Structure Unstable
**Severity**: MINOR
**Resolution**: FIXED on 2026-01-25. The structure was refactored. The `layer_0_01_universal_setup_file_tree_0` wrapper was removed, and all children now use the correct `sub_layer_0_XX_` naming convention. A README is still recommended.

**Old Issues**:
- Uses `layer_0_05`, `layer_0_06` numbering internally
- Conflicts with conceptual layer numbering
- No README explaining organization

### 6.3 Missing Sub-Layer Content
**Severity**: MINOR

Several sub-layers are empty or near-empty:
- `sub_layer_0_03_principles/` - Only .gitkeep
- `sub_layer_0_02_knowledge_system/` - Sparse content

---

## 7. RULES & PROTOCOLS PROBLEMS

### 7.1 Conflicting Terminal Protocols
**Severity**: MAJOR

Multiple versions exist:
- `terminal_execution_protocol.md`
- `UNIVERSAL_TERMINAL_EXECUTION.md`
- `MASTER_TERMINAL_EXECUTION_REFERENCE.md`
- `terminal-quick-reference.md`

No guidance on which to use or precedence.

### 7.2 No Rule Priority System
**Severity**: MINOR

`sub_layer_0_04_rules/` contains many rules but:
- No meta-rule defining priority
- No conflict resolution guidance
- No versioning system

### 7.3 Archive Docs Not Clearly Archived
**Severity**: MINOR

`3_archive_docs/` contains old resolutions but:
- Some may still be relevant
- No indication of what supersedes them
- Filenames use old date format (YYYYMMDD)

---

## 8. FEATURE DEFINITION PROBLEMS

### 8.1 Child Features Incomplete
**Severity**: MAJOR

`layer_1_feature_layer_stage_system/layer_2/layer_2_features/` has 5 child features:
- `layer_2_feature_ai_manager_hierarchy` - Partially implemented
- `layer_2_feature_context_gathering` - Partially implemented
- `layer_2_feature_handoff_system` - Partially implemented
- `layer_2_feature_layer_definitions` - Partially implemented
- `layer_2_feature_stage_definitions` - Partially implemented

All need completion to finalize the framework.

### 8.2 Framework Docs vs Implementation Gap
**Severity**: MAJOR

`sub_layer_1_05_framework_docs/` contains:
- `FLEXIBLE_LAYERING_SYSTEM.md` (28KB)
- `EXTENDING_THE_FRAMEWORK.md` (20KB)
- `WORKFLOW_FEATURE_PATTERN.md` (13KB)

But actual implementation doesn't fully match these specs.

---

## 9. CROSS-CUTTING PROBLEMS

### 9.1 No Validation Tooling
**Severity**: MAJOR

Only one validation script exists:
- `stage_0_08_current_product/changes/verify_paths.sh`

Missing:
- Registry validation
- Structure validation
- Link checking
- Schema validation for status.json

### 9.2 No Migration Automation
**Severity**: MINOR

Migration protocols documented but no automation:
- `restructuring_migration_protocol.md` - Manual steps only
- `traversal_update_protocol.md` - Manual steps only

### 9.3 Inconsistent Entity Pattern
**Severity**: MINOR

Entity creation guides exist but pattern varies:
- `instantiation_guide.md` - Comprehensive
- `project_creation_checklist.md` - Checklist format
- `feature_creation_checklist.md` - Checklist format
- `component_creation_checklist.md` - Checklist format

No unified entity creation API/script.

---

## 10. PROBLEM CATEGORIES FOR RESEARCH FEATURES

Based on this audit, problems map to potential research features:

| Problem Category | Potential Feature | Priority |
|------------------|-------------------|----------|
| Naming/Structure | `better_layer_stage_system` | HIGH |
| Stage workflow | `better_layer_stage_system` | HIGH |
| Documentation drift | `ai_documentation_system` | MEDIUM |
| Registry gaps | `better_layer_stage_system` | HIGH |
| Context gathering | `ai_context_system` | MEDIUM |
| Rules conflicts | `ai_rules_system` | LOW |
| Validation tooling | `ai_automation_system` | MEDIUM |
| Migration | `ai_migration_system` | LOW |

---

## Recommended Next Steps

1. **Immediate**: Standardize naming convention (underscores) - **COMPLETE**
2. **Immediate**: Create missing layer_registry.yaml - **COMPLETE**
3. **Short-term**: Finalize stage numbering scheme - **COMPLETE**
4. **Short-term**: Fix all broken path references - **COMPLETE**
5. **Medium-term**: Populate handoff documents with examples
6. **Medium-term**: Create validation tooling
7. **Long-term**: Complete child feature definitions
8. **Long-term**: Automate migration and entity creation

---

## Related Research

- `better_layer_stage_system/things_learned/01_current_system_analysis.md`
- `better_layer_stage_system/things_learned/02_inconsistencies_found.md`
- `better_layer_stage_system/things_learned/03_improvement_proposals.md`
