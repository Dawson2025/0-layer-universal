# Stage Manager Workflow References

Reference documents for stage management operations.

## Reference Index

| File | Purpose |
|------|---------|
| [README.md](README.md) | This index |
| [reorder_procedure.md](reorder_procedure.md) | Step-by-step stage reorder guide |
| [stage_schema.md](stage_schema.md) | Stage directory structure template |

## Quick Reference: Stage Order

| # | Name | Purpose |
|---|------|---------|
| 00 | stage_manager | Meta: manages stages |
| 01 | request_gathering | Collect requirements |
| 02 | research | Explore problem space |
| 03 | instructions | Define constraints |
| 04 | planning | Break into subtasks |
| 05 | design | Architecture decisions |
| 06 | development | Implementation |
| 07 | testing | Verification |
| 08 | criticism | Review |
| 09 | fixing | Corrections |
| 10 | current_product | Deliverable |
| 11 | archives | Historical |

## Quick Reference: Stage Directory Pattern

```
stage_-1_XX_name/
├── CLAUDE.md
├── .claude/
│   ├── agents/
│   ├── commands/
│   ├── hooks/
│   ├── scripts/
│   ├── settings.json
│   └── skills/
├── hand_off_documents/
│   ├── incoming/
│   └── outgoing/
└── outputs/
```
