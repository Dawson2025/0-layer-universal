# Request Gathering Validation Checklist

Use this checklist to verify completeness before transitioning to research stage.

## Per-Request Validation

Run this for each request in `outputs/requests/request_XX_*/`:

### request.md
- [ ] Has Request ID
- [ ] Has Date
- [ ] Has Priority (HIGH/MEDIUM/LOW)
- [ ] Has Status (Active/Complete/On Hold)
- [ ] Problem Statement is clear and specific
- [ ] At least 2 Key Issues identified
- [ ] Stakeholder identified
- [ ] Desired Outcome defined

### requirements.md
- [ ] Has Request ID matching request.md
- [ ] Has Last Updated date
- [ ] At least 1 Functional Requirement (REQ-XX-FYY)
- [ ] At least 1 Non-Functional Requirement (REQ-XX-NFYY)
- [ ] All requirements use correct ID format
- [ ] All requirements are specific and testable
- [ ] Acceptance Criteria defined (at least 2)

### specs.md
- [ ] Has Request ID matching request.md
- [ ] Has Last Updated date
- [ ] Technical specifications are concrete
- [ ] Includes schemas/formats where applicable
- [ ] Includes directory structures where applicable
- [ ] Includes examples

## Overview Documents Validation

### outputs/overview/README.md
- [ ] Lists all requests with correct count
- [ ] Summary statistics are accurate
- [ ] Links to all request folders work

### outputs/overview/system_vision.md
- [ ] Vision statement is clear
- [ ] Goals align with requests
- [ ] Principles are defined

### outputs/overview/consolidated_requirements.md
- [ ] Total count matches sum of all requirements
- [ ] All requests are represented
- [ ] Functional and non-functional separated
- [ ] No duplicate requirement IDs

### outputs/overview/dependencies.md
- [ ] All requests appear in dependency graph
- [ ] Dependencies are accurate
- [ ] Critical path is identified
- [ ] Implementation order is defined

### outputs/overview/implementation_roadmap.md
- [ ] Phases are defined
- [ ] Phase order respects dependencies
- [ ] Success criteria per phase
- [ ] Timeline considerations (if any)

## Cross-Validation

- [ ] Request count in CLAUDE.md matches actual
- [ ] Requirement counts in CLAUDE.md match actual
- [ ] All request IDs are unique
- [ ] All requirement IDs are unique
- [ ] No orphaned requests (missing from overview)

## Handoff Readiness

- [ ] All per-request validations pass
- [ ] All overview validations pass
- [ ] Cross-validation passes
- [ ] Handoff document prepared (`hand_off_documents/outgoing.md`)
- [ ] Open questions documented for research stage

## Quick Validation Commands

```bash
# Count requests
ls -d outputs/requests/request_*/ | wc -l

# Count functional requirements
grep -r "^### REQ-.*-F" outputs/requests/*/requirements.md | wc -l

# Count non-functional requirements
grep -r "^### REQ-.*-NF" outputs/requests/*/requirements.md | wc -l

# Check for missing files
for dir in outputs/requests/request_*/; do
  for file in request.md requirements.md specs.md; do
    [ -f "$dir/$file" ] || echo "MISSING: $dir$file"
  done
done
```
