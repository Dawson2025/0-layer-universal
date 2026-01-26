# 0.04_universal_rules

This sub-layer contains universal rules that apply across all layers, stages, OS, and tool contexts.

## Directory Structure

```
0.04_universal_rules/
├── README.md                          # This file
├── LAYER_CONTEXT_HEADER_PROTOCOL.md   # File header requirements
├── safety_governance.md               # Safety and governance rules (NEW)
└── trickle_down_0_universal/          # Legacy universal rules
    └── 0_instruction_docs/
        └── git_commit_rule.md         # Git commit requirements
```

## Core Universal Rules

### Safety, Permissions, and Governance
**Location**: `safety_governance.md`
**Status**: Active (Mandatory)
**Purpose**: Security boundaries, permission models, and governance policies for the AI Manager Hierarchy

**Key Features**:
- Permission levels by layer (L0-L4+)
- Filesystem, network, and command execution boundaries
- Human-in-the-loop approval gates
- Budget governance and resource quotas
- Audit trail and compliance requirements
- Integration with existing git commit and layer context rules

**Reference**: See normative spec in `-1_research/.../ideal_ai_manager_hierarchy_system/safety_and_governance.md`

### Layer Context Header Protocol
**Location**: `LAYER_CONTEXT_HEADER_PROTOCOL.md`
**Status**: Active (Mandatory)
**Purpose**: Standardized file headers for layer/component identification

### Git Commit and Sync Rule
**Location**: `trickle_down_0_universal/0_instruction_docs/git_commit_rule.md`
**Status**: Active (Mandatory)
**Purpose**: Git workflow requirements for all AI sessions

**Requirements**:
- At minimum: `git pull` before work, `git add/commit` after work
- Stronger default: also `git push` after every turn
- Extended for hierarchy: Commit format includes layer, stage, handoff-id, cost

## Notes

- All rules in this directory are **mandatory** unless explicitly marked as optional
- Safety and governance rules take precedence over other rules in case of conflict
- See observability protocol for logging requirements: `../sub_layer_0_13_universal_protocols/observability/`
