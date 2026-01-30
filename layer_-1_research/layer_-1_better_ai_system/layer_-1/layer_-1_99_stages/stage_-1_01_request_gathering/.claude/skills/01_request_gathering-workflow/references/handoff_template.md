# Handoff Document Template

Use this template when preparing to transition from request_gathering to the research stage.

## Outgoing Handoff Template

```markdown
# Request Gathering → Research Handoff

**Date**: YYYY-MM-DD
**From Stage**: 01_request_gathering
**To Stage**: 02_research
**Prepared By**: [Name/Agent]

## Summary

Total requests documented: X
Total functional requirements: X
Total non-functional requirements: X

## Requests Overview

| ID | Name | Priority | Key Focus Areas |
|----|------|----------|-----------------|
| 01 | [Name] | HIGH | [2-3 key points] |
| 02 | [Name] | MEDIUM | [2-3 key points] |

## Critical Path

The following requests should be researched first due to dependencies:

1. **REQ-XX**: [Name] - Foundation for others
2. **REQ-XX**: [Name] - Blocks X other requests

## Open Questions for Research

Questions that need investigation:

1. [Question about approach/technology]
2. [Question about feasibility]
3. [Question about integration]

## Recommended Research Order

Based on dependencies (see outputs/overview/dependencies.md):

### Phase 1 (No dependencies)
- REQ-01: [Name]

### Phase 2 (Depends on Phase 1)
- REQ-05, REQ-06, REQ-07

### Phase 3 (Depends on Phase 2)
- REQ-08

### Phase 4+ (Later phases)
- REQ-02, REQ-03, REQ-04

## Key Documents to Review

| Document | Location | Purpose |
|----------|----------|---------|
| System Vision | `outputs/overview/system_vision.md` | High-level goals |
| All Requirements | `outputs/overview/consolidated_requirements.md` | Full requirement list |
| Dependencies | `outputs/overview/dependencies.md` | Request relationships |
| Roadmap | `outputs/overview/implementation_roadmap.md` | Phased plan |

## Notes for Research Stage

[Any special considerations, constraints, or context that the research stage should know]
```

## Incoming Handoff Template

```markdown
# [Previous Stage] → Request Gathering Handoff

**Date**: YYYY-MM-DD
**From Stage**: [Stage name]
**Received By**: [Name/Agent]

## Context Received

[Summary of what was passed from previous stage]

## Initial Requests Identified

[List of requests that need to be documented]

## Stakeholder Input

[Any stakeholder feedback or priorities]

## Constraints

[Any constraints or limitations identified]
```
