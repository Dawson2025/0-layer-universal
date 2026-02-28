# Request Gathering Workflow References

Reference documents and templates for the request_gathering stage.

## Reference Index

| File | Purpose |
|------|---------|
| [README.md](README.md) | This index + basic templates |
| [handoff_template.md](handoff_template.md) | Templates for incoming/outgoing handoffs |
| [validation_checklist.md](validation_checklist.md) | Completeness verification checklist |
| [example_request.md](example_request.md) | Complete example based on REQ-01 |
| [overview_templates.md](overview_templates.md) | Templates for overview documents |
| [dependency_diagram.md](dependency_diagram.md) | Visual dependency diagrams |

---

## Quick Reference Templates

### Request Template (request.md)
```markdown
# Request: [Name]

**Request ID**: XX
**Date**: YYYY-MM-DD
**Priority**: HIGH | MEDIUM | LOW
**Status**: Active | Complete | On Hold

## Problem Statement
[Describe the problem this request addresses]

## Key Issues Identified
1. [Issue 1]
2. [Issue 2]
3. [Issue 3]

## Stakeholder
- [Who benefits from this being solved]

## Desired Outcome
[What success looks like]
```

### Requirements Template (requirements.md)
```markdown
# Requirements: [Name]

**Request ID**: XX
**Last Updated**: YYYY-MM-DD

## Functional Requirements

### REQ-XX-F01: [Name]
- [Specific, testable requirement]

### REQ-XX-F02: [Name]
- [Specific, testable requirement]

## Non-Functional Requirements

### REQ-XX-NF01: [Name]
- [Quality attribute requirement]

## Acceptance Criteria
- [ ] [Testable criterion 1]
- [ ] [Testable criterion 2]
```

### Specs Template (specs.md)
```markdown
# Specifications: [Name]

**Request ID**: XX
**Last Updated**: YYYY-MM-DD

## [Component] Specification

### Schema/Format
\`\`\`yaml
# Example schema
\`\`\`

### Directory Structure
\`\`\`
path/
├── file1
└── file2
\`\`\`

### Examples
[Concrete examples of the specification in use]
```

---

## Current Requests Reference

| ID | Name | Location |
|----|------|----------|
| 01 | Better Layer-Stage System | `outputs/requests/request_01_better_layer_stage_system/` |
| 02 | Better Setup System | `outputs/requests/request_02_better_setup_system/` |
| 03 | AI Manager Hierarchy System | `outputs/requests/request_03_ai_manager_hierarchy_system/` |
| 04 | AI Dynamic Memory System | `outputs/requests/request_04_ai_dynamic_memory_system/` |
| 05 | AI Documentation System | `outputs/requests/request_05_ai_documentation_system/` |
| 06 | AI Context System | `outputs/requests/request_06_ai_context_system/` |
| 07 | AI Rules System | `outputs/requests/request_07_ai_rules_system/` |
| 08 | AI Automation System | `outputs/requests/request_08_ai_automation_system/` |

---

## Requirement ID Format

```
REQ-XX-FYY  = Functional requirement
REQ-XX-NFYY = Non-functional requirement

Where:
  XX = Request number (01-99)
  YY = Requirement number within request (01-99)
```

---

## When to Use Each Reference

| Task | Reference |
|------|-----------|
| Creating a new request | This README (templates) |
| Checking format conventions | This README or example_request.md |
| Preparing stage handoff | handoff_template.md |
| Verifying completeness | validation_checklist.md |
| Creating overview docs | overview_templates.md |
| Updating dependencies | dependency_diagram.md |
