---
resource_id: "64e713fc-d40f-4dac-bd20-1bd05252356e"
resource_type: "knowledge"
resource_name: "03_improvement_proposals"
---
# Improvement Proposals for Layer-Stage System

<!-- section_id: "364c4746-9c90-45ec-9ff7-55eab292e734" -->
## Date: 2026-01-25
<!-- section_id: "9011abca-ecc1-4ac4-bb65-fc11d6466382" -->
## Source: Inconsistency Analysis

---

<!-- section_id: "76488928-72bd-4403-894a-23d2fec4c9b2" -->
## Proposal 1: Standardize Naming Convention

<!-- section_id: "0abc289a-0fe6-4dd3-9114-37464376ebc0" -->
### Problem
Mixed dot notation (`layer_1.02`) and underscore notation (`layer_1_02`)

<!-- section_id: "169ea11d-bd5c-46bf-9f2d-58d0b5398e64" -->
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

<!-- section_id: "cbd02e32-938f-4dd7-9fde-a5606df69ed8" -->
### Migration Steps
1. Create migration script to rename all files/folders
2. Update all documentation references
3. Update all CLAUDE.md files
4. Update all status.json path references
5. Test glob patterns still work

<!-- section_id: "259bedc7-c31e-42b6-bd11-4de0f3547350" -->
### Breaking Changes
- All hardcoded paths need updating
- Git history will show renames

---

<!-- section_id: "dc84285f-e973-4466-ab5d-610294183694" -->
## Proposal 2: Finalize Stage Numbering (v3.0)

<!-- section_id: "a8095c78-dc61-4b3e-be93-bb8beff90feb" -->
### Problem
Multiple numbering schemes (00-10 vs 00-11)

<!-- section_id: "45925faa-8d67-479c-9fed-e2da629578c6" -->
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

<!-- section_id: "0895fc42-99e2-478d-8289-c6261de9a944" -->
### Migration Steps
1. Add `stage_0_00_stage_registry/` to all entities
2. Renumber existing stages (+1)
3. Update all stage documentation
4. Update handoff references
5. Update automation scripts

---

<!-- section_id: "9799144a-6561-4e45-b34f-d8bae246f1b4" -->
## Proposal 3: Standardize Layer Components

<!-- section_id: "eb9dba32-fedb-4853-ac93-6b586f248d88" -->
### Problem
Inconsistent internal component positions

<!-- section_id: "95fd25b1-19da-44d9-b8bd-a398494c867a" -->
### Proposed Solution
**Standardize component positions with registry**

| Position | Component | Purpose |
|----------|-----------|---------|
| 00 | layer_registry | Layer metadata, child index |
| 01 | ai_manager_system | Agent configurations |
| 02 | manager_handoff_documents | Inter-layer communication |
| 03 | sub_layers | Content slots |
| 99 | stages | Workflow stages |

<!-- section_id: "2af7555b-763e-4b3c-b1b7-ff1f4657ccea" -->
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

<!-- section_id: "1f11fc3d-740a-41cc-858d-c1bd01101135" -->
## Proposal 4: Clarify Relative Layer Numbering

<!-- section_id: "3f67c6d2-f15d-4874-8f38-76793dec431a" -->
### Problem
L-1 research context creates ambiguity between relative and absolute numbering

<!-- section_id: "471ff0f1-c31d-4c44-b6b7-c9c35ec27fe4" -->
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

<!-- section_id: "e29bf2ac-398a-4ddb-9ed8-a8e92c59fee6" -->
### Documentation Updates
1. Create `LAYER_NUMBERING_GUIDE.md` with clear examples
2. Add context_type to all status.json files
3. Update context gathering rules for L-1 traversal

---

<!-- section_id: "d3322dfd-a808-461d-8ce2-4acf94c1ac96" -->
## Proposal 5: Synchronize Documentation

<!-- section_id: "0d10e30c-6d05-417d-9e24-4d21457ceac1" -->
### Problem
Documentation references outdated patterns

<!-- section_id: "b32fc540-e6ca-4069-ab78-dae7f0889fb8" -->
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

<!-- section_id: "db2d5970-2cdd-4ee2-bf74-abf1d5a9d033" -->
## Proposal 6: Standardize Sub-Layer Slots

<!-- section_id: "889da186-c80f-4622-9e44-7021cb842bf3" -->
### Problem
The `05+` notation is ambiguous

<!-- section_id: "e96942f2-cb0f-49b7-82df-c03f4c85d2a9" -->
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

<!-- section_id: "bbbc9969-e358-4b5a-b433-0d5fdd401b1d" -->
### Benefits
- Clear, explicit positions
- No ambiguous `+` notation
- Room for custom slots

---

<!-- section_id: "2dafdbdf-9587-457a-bb1c-f2ac3ae600fe" -->
## Proposal 7: Unify Handoff Naming

<!-- section_id: "972a5f32-2c20-4f81-bf7b-7e62b22a04cd" -->
### Problem
Inconsistent: `hand_off_documents` vs `manager_handoff_documents`

<!-- section_id: "e19f4b74-3ba1-4b86-8982-95dcc19adee1" -->
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

<!-- section_id: "14dd1a01-fe42-46ec-8c74-a4fde57481ba" -->
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

<!-- section_id: "86c6e60f-189e-4e94-be61-7b918ea27211" -->
## Proposal 8: Define Registry Standards

<!-- section_id: "319f2197-402d-45e6-8ca6-81bc19f2ca9a" -->
### Problem
Inconsistent registry implementation

<!-- section_id: "d15e5e78-7cb5-4ddd-a4da-3b5b00da871c" -->
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

<!-- section_id: "00f8ae15-d58f-47b9-b2d5-a20746a40bfe" -->
## Proposal 9: Standardize Status Schema

<!-- section_id: "6aebfd5a-5237-401e-8783-54e9358b4605" -->
### Problem
Multiple status.json formats

<!-- section_id: "38841153-919e-43b8-aa2e-3831ee43a114" -->
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

<!-- section_id: "a7553839-f59d-4a33-aa6a-7670b90bd35b" -->
## Proposal 10: .claude Folder Standard

<!-- section_id: "b75f394d-3a8f-4b47-a52d-03fa48e9cdf3" -->
### Problem
Varying completeness of .claude structures

<!-- section_id: "587934f7-4a3f-4d07-8df7-03ad384db2ae" -->
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

<!-- section_id: "027fcccc-9a51-4a02-9c1a-d113841270fb" -->
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

<!-- section_id: "23d55013-0e96-4dae-a1f5-2214d8df54b2" -->
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

<!-- section_id: "3debb531-5bda-4f73-b1b9-21c453ea6c2b" -->
## Next Steps

1. Review proposals with stakeholders
2. Prioritize based on current pain points
3. Create migration scripts for high-priority items
4. Implement incrementally with backward compatibility
5. Update all documentation to match
