# Overview Document Templates

Templates for the documents in `outputs/overview/`.

---

## README.md Template

```markdown
# Request Gathering Overview

**Project**: [Project Name]
**Stage**: 01 - Request Gathering
**Last Updated**: YYYY-MM-DD

## Summary

| Metric | Count |
|--------|-------|
| Total Requests | X |
| Functional Requirements | X |
| Non-Functional Requirements | X |
| Acceptance Criteria | X |

## Requests

| ID | Name | Priority | Status |
|----|------|----------|--------|
| 01 | [Name] | HIGH | Active |
| 02 | [Name] | MEDIUM | Active |

## Quick Links

- [System Vision](system_vision.md)
- [All Requirements](consolidated_requirements.md)
- [Dependencies](dependencies.md)
- [Implementation Roadmap](implementation_roadmap.md)

## Request Details

### Request 01: [Name]
- **Problem**: [One-line summary]
- **Location**: `../requests/request_01_[name]/`

### Request 02: [Name]
- **Problem**: [One-line summary]
- **Location**: `../requests/request_02_[name]/`
```

---

## system_vision.md Template

```markdown
# System Vision

**Project**: [Project Name]
**Date**: YYYY-MM-DD

## Vision Statement

[2-3 sentences describing the ideal end state]

## Goals

1. **[Goal 1]**: [Description]
2. **[Goal 2]**: [Description]
3. **[Goal 3]**: [Description]

## Guiding Principles

| Principle | Description |
|-----------|-------------|
| [Principle 1] | [How it guides decisions] |
| [Principle 2] | [How it guides decisions] |

## Success Criteria

The project is successful when:

1. [Measurable outcome 1]
2. [Measurable outcome 2]
3. [Measurable outcome 3]

## Out of Scope

The following are explicitly NOT part of this project:

- [Item 1]
- [Item 2]

## Stakeholders

| Stakeholder | Interest | Impact |
|-------------|----------|--------|
| [Who] | [What they care about] | [How affected] |
```

---

## consolidated_requirements.md Template

```markdown
# Consolidated Requirements

**Project**: [Project Name]
**Last Updated**: YYYY-MM-DD

## Summary

| Category | Count |
|----------|-------|
| Functional Requirements | X |
| Non-Functional Requirements | X |
| Total | X |

## Functional Requirements by Request

### Request 01: [Name]

| ID | Requirement | Priority |
|----|-------------|----------|
| REQ-01-F01 | [Description] | HIGH |
| REQ-01-F02 | [Description] | MEDIUM |

### Request 02: [Name]

| ID | Requirement | Priority |
|----|-------------|----------|
| REQ-02-F01 | [Description] | HIGH |

## Non-Functional Requirements by Request

### Request 01: [Name]

| ID | Requirement | Category |
|----|-------------|----------|
| REQ-01-NF01 | [Description] | Performance |
| REQ-01-NF02 | [Description] | Usability |

## Cross-Cutting Requirements

Requirements that span multiple requests:

| ID | Requirement | Applies To |
|----|-------------|------------|
| [ID] | [Description] | REQ-01, REQ-03 |
```

---

## dependencies.md Template

```markdown
# Request Dependencies

**Project**: [Project Name]
**Last Updated**: YYYY-MM-DD

## Dependency Graph

\`\`\`
        ┌─────────┐
        │ REQ-01  │ (Foundation)
        └────┬────┘
             │
    ┌────────┼────────┐
    ▼        ▼        ▼
┌───────┐ ┌───────┐ ┌───────┐
│REQ-02 │ │REQ-03 │ │REQ-04 │
└───────┘ └───┬───┘ └───────┘
              │
              ▼
          ┌───────┐
          │REQ-05 │
          └───────┘
\`\`\`

## Dependency Matrix

| Request | Depends On | Blocks |
|---------|------------|--------|
| 01 | (none) | 02, 03, 04 |
| 02 | 01 | - |
| 03 | 01 | 05 |

## Critical Path

\`\`\`
REQ-01 → REQ-03 → REQ-05
\`\`\`

## Implementation Order

1. **Phase 1**: REQ-01 (no dependencies)
2. **Phase 2**: REQ-02, REQ-03, REQ-04 (depend on Phase 1)
3. **Phase 3**: REQ-05 (depends on Phase 2)
```

---

## implementation_roadmap.md Template

```markdown
# Implementation Roadmap

**Project**: [Project Name]
**Last Updated**: YYYY-MM-DD

## Overview

[Brief description of the implementation approach]

## Phases

### Phase 1: Foundation
**Requests**: REQ-01
**Focus**: [What this phase establishes]

**Deliverables**:
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

**Success Criteria**:
- [Measurable criterion]

---

### Phase 2: Core Features
**Requests**: REQ-02, REQ-03
**Depends On**: Phase 1
**Focus**: [What this phase builds]

**Deliverables**:
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

**Success Criteria**:
- [Measurable criterion]

---

### Phase 3: Integration
**Requests**: REQ-04, REQ-05
**Depends On**: Phase 2
**Focus**: [What this phase connects]

## Risk Considerations

| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk 1] | HIGH | [How to address] |
| [Risk 2] | MEDIUM | [How to address] |

## Parallel Opportunities

These can be worked simultaneously:
- Phase 2a: REQ-02
- Phase 2b: REQ-03
```
