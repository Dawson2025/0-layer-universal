---
resource_id: "64e713fc-d40f-4dac-bd20-1bd05252356e"
resource_type: "knowledge"
resource_name: "03_improvement_proposals"
---
# Improvement Proposals for Layer-Stage System

## Date: 2026-01-25
## Source: Inconsistency Analysis

---

## Proposal 1: Standardize Naming Convention

### Problem
Mixed dot notation (`layer_1.02`) and underscore notation (`layer_1_02`)

### Proposed Solution
**Adopt underscore notation universally**

```
# Standard Pattern
layer_N_XX_name

# Examples
layer_0_00_layer_registry
layer_1_02_sub_layers
sub_layer_0_05_setup_dependant
```

### Migration Steps
1. Create migration script to rename all files/folders
2. Update all documentation references
3. Update all CLAUDE.md files
4. Update all status.json path references
5. Test glob patterns still work

### Breaking Changes
- All hardcoded paths need updating
- Git history will show renames

---

## Proposal 2: Finalize Stage Numbering (v3.0)

### Problem
Multiple numbering schemes (00-10 vs 00-11)

### Proposed Solution
**Adopt v3.0 numbering with registry at 00**

| Position | Stage | Purpose |
|----------|-------|---------|
| 00 | stage_registry | Centralized stage metadata |
| 01 | request_gathering | Initial requirements |
| 02 | research | Problem exploration |
| 03 | instructions | Task definition |
| 04 | planning | Implementation planning |
| 05 | design | Solution architecture |
| 06 | development | Implementation |
| 07 | testing | Verification |
| 08 | criticism | Review and critique |
| 09 | fixing | Issue resolution |
| 10 | current_product | Working version |
| 11 | archives | Historical records |

### Migration Steps
1. Add `stage_0_00_stage_registry/` to all entities
2. Renumber existing stages (+1)
3. Update all stage documentation
4. Update handoff references
5. Update automation scripts

---

## Proposal 3: Standardize Layer Components

### Problem
Inconsistent internal component positions

### Proposed Solution
**Standardize component positions with registry**

| Position | Component | Purpose |
|----------|-----------|---------|
| 00 | layer_registry | Layer metadata, child index |
| 01 | ai_manager_system | Agent configurations |
| 02 | manager_handoff_documents | Inter-layer communication |
| 03 | sub_layers | Content slots |
| 99 | stages | Workflow stages |

### Registry Schema
```json
{
  "layer_number": 0,
  "entity_type": "feature",
  "entity_name": "better_layer_stage_system",
  "parent_layer": -1,
  "children": {
    "features": [],
    "components": [],
    "sub_projects": []
  },
  "created_at": "2026-01-25",
  "last_updated": "2026-01-25"
}
```

---

## Proposal 4: Clarify Relative Layer Numbering

### Problem
L-1 research context creates ambiguity between relative and absolute numbering

### Proposed Solution
**Document both systems explicitly**

#### Absolute Numbering
- Layer 0 = `0_layer_universal/`
- Layer 1 = Direct children of L0
- Layer 2 = Children of L1
- etc.

#### Relative Numbering (Within Context)
- In research projects: L-1 = project, L0 = features, L1 = sub-features
- In regular projects: L0 = project, L1 = features, L2 = sub-features

#### Context Marker
Add `context_type` to status files:
```json
{
  "context_type": "research",  // or "production"
  "relative_layer": 0,
  "absolute_layer": 2
}
```

### Documentation Updates
1. Create `LAYER_NUMBERING_GUIDE.md` with clear examples
2. Add context_type to all status.json files
3. Update context gathering rules for L-1 traversal

---

## Proposal 5: Synchronize Documentation

### Problem
Documentation references outdated patterns

### Proposed Solution
**Create documentation versioning system**

1. **Add version headers to all docs**:
```markdown
---
version: 3.0
last_updated: 2026-01-25
compatible_with: ["2.0", "3.0"]
---
```

2. **Create central VERSION.md**:
```markdown
# Layer-Stage Framework Version History

## v3.0 (Current)
- Stage numbering: 00 = registry, 01-11 = workflow
- Layer components: 00 = registry, 01-03, 99
- Naming: underscore only
- .claude: full structure

## v2.0 (Deprecated)
- Stage numbering: 00-10
- No registries
- Mixed naming
```

3. **Automated doc sync check**:
Create script to verify doc versions match implementation

---

## Proposal 6: Standardize Sub-Layer Slots

### Problem
The `05+` notation is ambiguous

### Proposed Solution
**Use explicit ranges with reserved slots**

| Position | Slot | Purpose |
|----------|------|---------|
| 01 | prompts | Visual notes, diagrams |
| 02 | knowledge_system | Documentation |
| 03 | principles | Guiding principles |
| 04 | rules | Constraints |
| 05 | setup_os | OS-specific content |
| 06 | setup_env | Environment-specific |
| 07 | setup_tools | Tool-specific |
| 08-98 | custom | Entity-specific slots |

### Benefits
- Clear, explicit positions
- No ambiguous `+` notation
- Room for custom slots

---

## Proposal 7: Unify Handoff Naming

### Problem
Inconsistent: `hand_off_documents` vs `manager_handoff_documents`

### Proposed Solution
**Standardize to `handoff_documents`** (no underscore in "handoff")

```
# Stage handoffs
stage_N_XX_name/
└── handoff_documents/
    ├── from_previous.json
    └── to_next.json

# Layer handoffs
layer_N/
└── layer_N_02_handoff_documents/
    ├── to_parent.json
    └── to_children.json
```

### Handoff Schema
```json
{
  "handoff_type": "stage|layer",
  "source": "stage_02_research",
  "target": "stage_03_instructions",
  "summary": "Research complete",
  "artifacts": ["outputs/findings.md"],
  "open_questions": [],
  "created_at": "2026-01-25"
}
```

---

## Proposal 8: Define Registry Standards

### Problem
Inconsistent registry implementation

### Proposed Solution
**Create registry schemas**

#### Layer Registry Schema
```json
{
  "schema_version": "1.0",
  "layer_number": 0,
  "entity_type": "feature",
  "entity_name": "better_layer_stage_system",
  "description": "Research feature for Layer-Stage improvements",
  "parent": {
    "path": "../..",
    "layer": -1
  },
  "children": {
    "features": [],
    "components": [],
    "sub_projects": []
  },
  "metadata": {
    "created_at": "2026-01-25",
    "created_by": "claude",
    "last_updated": "2026-01-25"
  }
}
```

#### Stage Registry Schema
```json
{
  "schema_version": "1.0",
  "stages": [
    {"number": 1, "name": "request_gathering", "status": "completed"},
    {"number": 2, "name": "research", "status": "in_progress"},
    ...
  ],
  "current_stage": 2,
  "workflow_type": "linear|iterative",
  "last_updated": "2026-01-25"
}
```

---

## Proposal 9: Standardize Status Schema

### Problem
Multiple status.json formats

### Proposed Solution
**Single standard schema**

```json
{
  "schema_version": "1.0",
  "entity": {
    "type": "feature",
    "name": "better_layer_stage_system",
    "layer": 0
  },
  "context": {
    "type": "research",
    "parent_project": "better_ai_system"
  },
  "progress": {
    "current_stage": "02_research",
    "percent_complete": 25,
    "last_activity": "2026-01-25"
  },
  "stages": [
    {"stage": "01_request_gathering", "status": "completed", "completed_at": "2026-01-25"},
    {"stage": "02_research", "status": "in_progress", "started_at": "2026-01-25"}
  ],
  "notes": "Analyzing reference implementation"
}
```

---

## Proposal 10: .claude Folder Standard

### Problem
Varying completeness of .claude structures

### Proposed Solution
**Define minimum viable .claude structure**

```
.claude/
├── settings.json          # REQUIRED: permissions, context
├── agents/                 # OPTIONAL: custom agents
│   └── {stage}-agent.md
├── commands/              # OPTIONAL: slash commands
│   └── {stage}-status.md
├── skills/                # OPTIONAL: workflow skills
│   └── {stage}-workflow/
│       ├── SKILL.md
│       └── references/
├── hooks/                 # OPTIONAL: automation
│   ├── hooks.json
│   └── scripts/
└── scripts/               # OPTIONAL: utilities
```

### Minimum Required (`settings.json`):
```json
{
  "context": {
    "include": ["CLAUDE.md", "../CLAUDE.md"],
    "exclude": ["**/node_modules/**"]
  },
  "permissions": {
    "allowedTools": ["Read", "Glob", "Grep"]
  }
}
```

---

## Implementation Priority

| Proposal | Priority | Effort | Impact |
|----------|----------|--------|--------|
| P2: Stage Numbering | High | Medium | High |
| P3: Layer Components | High | Low | High |
| P4: Relative Numbering | High | Medium | High |
| P9: Status Schema | High | Medium | High |
| P1: Naming Convention | Medium | High | Medium |
| P5: Doc Sync | Medium | Medium | Medium |
| P8: Registry Standards | Medium | Medium | Medium |
| P7: Handoff Naming | Low | Low | Low |
| P6: Sub-Layer Slots | Low | Low | Low |
| P10: .claude Standard | Low | Low | Medium |

---

## Next Steps

1. Review proposals with stakeholders
2. Prioritize based on current pain points
3. Create migration scripts for high-priority items
4. Implement incrementally with backward compatibility
5. Update all documentation to match
