# Outgoing Hand Off Documents

Documents prepared for the next stage.

## Destination

| Field | Value |
|-------|-------|
| **To Stage** | stage_-1_02_research |
| **To Path** | `../stage_-1_02_research/hand_off_documents/incoming/` |
| **Expected Content** | Documented requests, requirements, dependencies, open questions |

## What to Include in Outgoing Handoff

### Required Content

1. **Request Summary**
   - Total count of requests
   - Priority distribution
   - Status of each

2. **Requirements Overview**
   - Functional requirements count
   - Non-functional requirements count
   - Key acceptance criteria

3. **Dependencies**
   - Critical path
   - Recommended research order
   - Blocking relationships

4. **Open Questions**
   - Questions that need research
   - Unclear requirements
   - Technology decisions needed

### Key Documents to Reference

| Document | Location |
|----------|----------|
| Request Index | `outputs/overview/README.md` |
| System Vision | `outputs/overview/system_vision.md` |
| All Requirements | `outputs/overview/consolidated_requirements.md` |
| Dependencies | `outputs/overview/dependencies.md` |
| Roadmap | `outputs/overview/implementation_roadmap.md` |

## Documents

| File | Date | Destination | Description |
|------|------|-------------|-------------|
| (none yet) | - | - | - |

## Template for Outgoing Documents

```markdown
# Request Gathering → Research Handoff

**Date**: YYYY-MM-DD
**From Stage**: stage_-1_01_request_gathering
**To Stage**: stage_-1_02_research
**Prepared By**: [Name/Agent]

## Summary

| Metric | Count |
|--------|-------|
| Total Requests | X |
| Functional Requirements | X |
| Non-Functional Requirements | X |

## Requests Overview

| ID | Name | Priority | Key Focus |
|----|------|----------|-----------|
| 01 | [Name] | HIGH | [Focus areas] |

## Critical Path

[Recommended order for research]

## Open Questions for Research

1. [Question needing investigation]
2. [Technology decision needed]

## Key Documents

- System Vision: `outputs/overview/system_vision.md`
- All Requirements: `outputs/overview/consolidated_requirements.md`
- Dependencies: `outputs/overview/dependencies.md`

## Notes for Research Stage

[Any special considerations]
```

## Handoff Checklist

Before creating outgoing handoff:

- [ ] All requests have complete documentation
- [ ] Requirements are consolidated
- [ ] Dependencies are mapped
- [ ] Open questions are documented
- [ ] Validation checklist passes
- [ ] Overview documents are up to date

## How to Deliver

1. Create handoff document using template above
2. Save as `YYYYMMDD_to_research_handoff.md`
3. Copy to `../stage_-1_02_research/hand_off_documents/incoming/`
4. Update stage status to complete
