# layer_0_feature_ai_rules_system

## Overview
Research feature focused on improving the rules and protocols system for AI agents. Addresses conflicting rules, protocol organization, and rule priority.

## Status
**Progress**: ~5% (Research)
**Current Stage**: 02_research

## Purpose
Research and design improvements to rules systems:
- Rule conflict resolution
- Protocol organization
- Rule versioning
- Rule priority system

## Problems Being Addressed

### From AI System Audit

#### Major Issues
1. **Conflicting Terminal Protocols** (MAJOR)
   - Multiple versions exist with no clear priority:
     - `terminal_execution_protocol.md`
     - `UNIVERSAL_TERMINAL_EXECUTION.md`
     - `MASTER_TERMINAL_EXECUTION_REFERENCE.md`
     - `terminal-quick-reference.md`
   - No guidance on which to use

2. **No Rule Priority System** (MINOR becoming MAJOR)
   - `sub_layer_0_04_rules/` contains many rules
   - No meta-rule defining priority
   - No conflict resolution guidance
   - No versioning system

3. **Archive Docs Not Clearly Archived** (MINOR)
   - `3_archive_docs/` contains old resolutions
   - Some may still be relevant
   - No indication of what supersedes them
   - Filenames use old date format (YYYYMMDD)

#### Specific Rule Files with Issues
4. **Mixed instruction types in same folder**
   - `0_instruction_docs/` contains:
     - Agent guides
     - Terminal protocols
     - Quick references
     - Specific tool instructions (supabase, canvas)
   - No clear organization principle

5. **Rule scope unclear**
   - Some rules are universal
   - Some are OS-specific
   - Some are tool-specific
   - No clear labeling

### Specific Rules Problems
1. Rules scattered across multiple sub-layers
2. No rule inheritance from parent layers
3. No rule override mechanism
4. No rule validation

## Research Areas
1. **Rule Organization**
   - Category system for rules
   - Scope labeling (universal, OS, tool)
   - Priority levels

2. **Conflict Resolution**
   - When rules conflict, which wins?
   - Explicit override syntax
   - Conflict detection

3. **Rule Versioning**
   - How to deprecate rules
   - How to update rules
   - How to archive rules

4. **Rule Discovery**
   - How agents find applicable rules
   - Rule registry
   - Rule search/filter

## Structure
```
layer_0_feature_ai_rules_system/
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
- `better_layer_stage_system` - Framework structure
- `ai_context_system` - Rules as context
- `ai_documentation_system` - Rule documentation
