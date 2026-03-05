---
resource_id: "ff8f2be2-63fa-4330-9f6c-2362a0dc1b30"
resource_type: "readme
knowledge"
resource_name: "README"
---
# Stage Documentation

This directory contains detailed documentation for each of the 11 workflow stages (00-10) in the Layer-Stage Framework.

<!-- section_id: "af68754e-fb2b-4617-bf34-f00419f12ea3" -->
## Stage Files

| File | Stage | Description |
|------|-------|-------------|
| `stage_00_request_gathering.md` | Request Gathering | Initial requirement collection |
| `stage_01_research.md` | Research | Explore problem space, gather information |
| `stage_02_instructions.md` | Instructions | Task definition |
| `stage_03_planning.md` | Planning | Implementation planning |
| `stage_04_design.md` | Design | Solution architecture |
| `stage_05_development.md` | Development | Implementation |
| `stage_06_testing.md` | Testing | Verification |
| `stage_07_criticism.md` | Criticism | Review and critique |
| `stage_08_fixing.md` | Fixing | Issue resolution |
| `stage_09_current_product.md` | Current Product | Working version |
| `stage_10_archives.md` | Archives | Historical records |

<!-- section_id: "ba722678-3523-416b-aaf7-9107b67eba10" -->
## Usage

Each stage document follows a consistent template:
- **Purpose**: What the stage accomplishes
- **Entry Criteria**: Prerequisites for entering
- **Exit Criteria**: Requirements for completion
- **Typical Tasks**: Common activities
- **Handoffs**: Input/output artifacts
- **Directory Structure**: Expected file organization

<!-- section_id: "4ae59e2b-20cb-4b7a-b4da-1fe30b9c4bd6" -->
## Workflow Pattern

```
00 -> 01 -> 02 -> 03 -> 04 -> 05 -> 06 -> 07 -> 08 -> 09
 ^                                               |
 |                                               v
 +-----------------------------------------------+
                  (iteration loop)

09 -> 10 (archival)
```

Stages support both linear progression and iterative loops based on feedback from criticism and testing stages.

<!-- section_id: "315f90d9-38ba-42a4-ab2f-c6c021029ff2" -->
## Stage Structure

Each stage directory contains:
```
stage_N_XX_name/
├── ai_agent_system/       # Agent configuration
├── hand_off_documents/    # Concise handoff notes
└── outputs/               # Stage artifacts (referenced by handoffs)
```

The `outputs/` folder allows handoff documents to remain concise by referencing artifacts rather than duplicating content inline.
