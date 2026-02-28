---
description: Show current status of request_gathering stage with detailed metrics
argument-hint: [--verbose] [--request XX]
---

# /01_request_gathering-status

Check the current status of the request_gathering stage.

## Status Checks

### Request Inventory
Check `outputs/requests/` for:
- Total request folders (expected: 8)
- Completeness of each request (request.md, requirements.md, specs.md)
- Any missing or incomplete files

### Overview Documents
Check `outputs/overview/` for:
- README.md - Request index
- system_vision.md - Vision document
- consolidated_requirements.md - All requirements
- implementation_roadmap.md - Phased plan
- dependencies.md - Request relationships

### Metrics to Report

| Metric | Expected | Actual |
|--------|----------|--------|
| Total Requests | 8 | ? |
| Functional Requirements | 40 | ? |
| Non-Functional Requirements | 24 | ? |
| Acceptance Criteria | 40 | ? |

### Request Status Table

| ID | Name | Priority | Complete |
|----|------|----------|----------|
| 01 | Better Layer-Stage System | HIGH | ? |
| 02 | Better Setup System | MEDIUM | ? |
| 03 | AI Manager Hierarchy System | HIGH | ? |
| 04 | AI Dynamic Memory System | LOW | ? |
| 05 | AI Documentation System | MEDIUM | ? |
| 06 | AI Context System | MEDIUM | ? |
| 07 | AI Rules System | LOW | ? |
| 08 | AI Automation System | MEDIUM | ? |

## Output Format

```
## Request Gathering Status

**Stage**: stage_-1_01_request_gathering
**Project**: better_ai_system

### Summary
- Requests: X/8 complete
- Requirements: X functional, X non-functional
- Overview docs: X/5 complete

### Issues
- [List any missing or incomplete items]

### Next Actions
- [List recommended next steps]
```

## Flags
- `--verbose`: Show detailed file-by-file status
- `--request XX`: Show status for specific request only
