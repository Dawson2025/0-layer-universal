---
name: 01_request_gathering-workflow
description: Workflow skill for collecting and documenting requirements for the better_ai_system project.
version: 1.0.0
---

# Request Gathering Workflow Skill

## When to Use
- When entering the request_gathering stage
- When adding or modifying requests
- When reviewing requirement completeness
- When preparing handoff to research stage

## Project Context
- **Project**: better_ai_system
- **Purpose**: Improve AI system architecture
- **Current Requests**: 8 documented
- **Requirements**: 40 functional, 24 non-functional

## Workflow Steps

### 1. Initialize
```
1. Read outputs/overview/README.md for current state
2. Check hand_off_documents/ for incoming context
3. Review outputs/overview/dependencies.md for relationships
```

### 2. Review Existing Requests
```
For each request in outputs/requests/request_XX_*/:
  - Read request.md for problem statement
  - Read requirements.md for requirements
  - Read specs.md for technical details
  - Note gaps or ambiguities
```

### 3. Add New Request (if needed)
```
1. Create outputs/requests/request_XX_name/
2. Create request.md:
   - Request ID, Date, Priority, Status
   - Problem Statement
   - Key Issues Identified
   - Stakeholder
   - Desired Outcome

3. Create requirements.md:
   - Functional Requirements (REQ-XX-FYY)
   - Non-Functional Requirements (REQ-XX-NFYY)
   - Acceptance Criteria

4. Create specs.md:
   - Technical specifications
   - Schemas and formats
   - Directory structures
   - Examples

5. Update overview documents
```

### 4. Update Overviews
```
After any request changes:
- Update outputs/overview/README.md
- Update outputs/overview/consolidated_requirements.md
- Update outputs/overview/dependencies.md if needed
- Update outputs/overview/implementation_roadmap.md if needed
```

### 5. Prepare Handoff
```
When stage is complete:
- Verify all requests are complete
- Create hand_off_documents/outgoing.md
- Summarize for research stage
```

## Key Files

| File | Purpose |
|------|---------|
| `outputs/overview/README.md` | Request index and summary |
| `outputs/overview/system_vision.md` | High-level vision |
| `outputs/overview/consolidated_requirements.md` | All requirements |
| `outputs/overview/implementation_roadmap.md` | Phased plan |
| `outputs/overview/dependencies.md` | Request relationships |

## Best Practices
- Use consistent requirement ID format: REQ-XX-FYY
- Include acceptance criteria for all requirements
- Document dependencies explicitly
- Keep specs concrete with examples
- Update overviews after every change

## References

This skill includes supporting documents in the `references/` folder:

| File | Purpose | When to Use |
|------|---------|-------------|
| `references/README.md` | Templates + request index | Creating new requests |
| `references/handoff_template.md` | Handoff document templates | Preparing stage transitions |
| `references/validation_checklist.md` | Completeness checklist | Before handoff |
| `references/example_request.md` | Complete REQ-01 example | Format reference |
| `references/overview_templates.md` | Overview doc templates | Creating overview files |
| `references/dependency_diagram.md` | Dependency visualizations | Updating dependencies |

When creating new requests, read `references/README.md` for templates.
When preparing handoff, read `references/handoff_template.md` and `references/validation_checklist.md`.
