# layer_0_feature_ai_documentation_system

## Overview
Research feature focused on improving documentation systems across the AI development environment. Addresses documentation drift, path references, and documentation organization patterns.

## Status
**Progress**: ~5% (Research)
**Current Stage**: 02_research

## Purpose
Research and design improvements to documentation:
- Prevent documentation drift from implementation
- Standardize path references
- Create documentation validation
- Define documentation update protocols

## Problems Being Addressed

### From AI System Audit

#### Critical Issues
1. **Broken Path References** (CRITICAL)
   - `layer_0_01_ai_manager_system/README.md` references `sub_layer_0_13_universal_protocols/` which doesn't exist
   - `sub_layer_0_04_rules/safety_governance.md` references non-existent paths
   - `handoff_schema.md` references `/code/0_layer_universal/0_context/` but folder doesn't exist

2. **Init Prompt Chain Confusion** (MAJOR)
   - Documentation claims init prompt at one path, actual location differs
   - Documented: `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/...`
   - Actual: `layer_0/layer_0_03_sub_layers/sub_layer_0_01_prompts/universal_init_prompt.md`

3. **Documentation Describes Wrong Structure** (MAJOR)
   - SYSTEM_OVERVIEW.md describes slots at layer level
   - Implementation uses sub-layers only

#### Major Issues
4. **Dots vs Underscores in Paths** (in documentation)
   - Documentation uses: `0.00_`, `0.01_`, `0.02_`
   - Actual directories: `layer_0_00_`, `layer_0_01_`, `layer_0_02_`

5. **Old Trickle-Down References**
   - Some docs still reference `0_context/trickle_down_*/` structure
   - System has moved to `layer_N/layer_N_XX_*` structure

6. **Multiple CLAUDE.md Entry Points**
   - No clear guidance on which CLAUDE.md is primary
   - Root, layer_0, features all have different CLAUDE.md files

### Specific Documentation Problems
1. No link validation tooling
2. No automated path checking
3. No documentation update triggers on structural changes
4. README files in many directories are stubs or missing

## Research Areas
1. **Path Reference System**
   - Canonical path format
   - Relative vs absolute path rules
   - Path alias system

2. **Documentation Validation**
   - Link checking scripts
   - Path existence validation
   - Cross-reference validation

3. **Update Protocols**
   - When to update which docs
   - Traversal update automation
   - Documentation change tracking

4. **Entry Point Clarity**
   - Single source of truth for navigation
   - Clear hierarchy of documentation
   - Context-aware documentation loading

## Structure
```
layer_0_feature_ai_documentation_system/
├── CLAUDE.md
├── layer_0/
│   ├── layer_0_03_sub_layers/
│   │   └── sub_layer_0_02_knowledge_system/
│   │       ├── overview/
│   │       └── things_learned/
│   └── layer_0_99_stages/
│       └── stage_0_02_research/
│           └── outputs/
└── layer_1/
    └── layer_1_features/
```

## Related Features
- `better_layer_stage_system` - Framework structure (naming conventions)
- `ai_automation_system` - Validation tooling
