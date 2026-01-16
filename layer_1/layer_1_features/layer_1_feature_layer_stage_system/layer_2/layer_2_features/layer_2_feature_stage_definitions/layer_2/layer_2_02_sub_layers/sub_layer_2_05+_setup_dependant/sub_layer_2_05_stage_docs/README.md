# Stage Documentation

This directory contains detailed documentation for each of the 10 workflow stages (00-09) in the Layer-Stage Framework.

## Stage Files

| File | Stage | Description |
|------|-------|-------------|
| `stage_00_request_gathering.md` | Request Gathering | Initial requirement collection |
| `stage_01_instructions.md` | Instructions | Task definition |
| `stage_02_planning.md` | Planning | Implementation planning |
| `stage_03_design.md` | Design | Solution architecture |
| `stage_04_development.md` | Development | Implementation |
| `stage_05_testing.md` | Testing | Verification |
| `stage_06_criticism.md` | Criticism | Review and critique |
| `stage_07_fixing.md` | Fixing | Issue resolution |
| `stage_08_current_product.md` | Current Product | Working version |
| `stage_09_archives.md` | Archives | Historical records |

## Usage

Each stage document follows a consistent template:
- **Purpose**: What the stage accomplishes
- **Entry Criteria**: Prerequisites for entering
- **Exit Criteria**: Requirements for completion
- **Typical Tasks**: Common activities
- **Handoffs**: Input/output artifacts
- **Directory Structure**: Expected file organization

## Workflow Pattern

```
00 -> 01 -> 02 -> 03 -> 04 -> 05 -> 06 -> 07 -> 08
 ^                                          |
 |                                          v
 +------------------------------------------+
                (iteration loop)

08 -> 09 (archival)
```

Stages support both linear progression and iterative loops based on feedback from criticism and testing stages.
