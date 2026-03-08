---
resource_id: "250bd5b4-233e-44e6-a0dc-211e5eda0207"
resource_type: "readme_document"
resource_name: "README"
---
# Stage Documentation

This directory contains detailed documentation for each of the 11 workflow stages (00-10) in the Layer-Stage Framework.

<!-- section_id: "29305c18-0bd4-4a71-b686-301c059c93fc" -->
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

<!-- section_id: "950881f7-1c97-4a4a-a936-379d3aaa3f14" -->
## Usage

Each stage document follows a consistent template:
- **Purpose**: What the stage accomplishes
- **Entry Criteria**: Prerequisites for entering
- **Exit Criteria**: Requirements for completion
- **Typical Tasks**: Common activities
- **Handoffs**: Input/output artifacts
- **Directory Structure**: Expected file organization

<!-- section_id: "ae7926b6-6b44-42ca-a769-91e3088b38c5" -->
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

<!-- section_id: "bc68bf57-586f-42dc-9ef7-e904d9616b70" -->
## Stage Structure

Each stage directory contains:
```
stage_N_XX_name/
├── ai_agent_system/       # Agent configuration
├── hand_off_documents/    # Concise handoff notes
└── outputs/               # Stage artifacts (referenced by handoffs)
```

The `outputs/` folder allows handoff documents to remain concise by referencing artifacts rather than duplicating content inline.
