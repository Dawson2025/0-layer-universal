---
description: Mark request_gathering stage as complete and prepare handoff to research stage
argument-hint: [--notes "completion notes"]
---

# /01_request_gathering-complete

Complete the request_gathering stage and prepare for the research stage.

## Verification Checklist

### Requests (outputs/requests/)
- [ ] All 8 request folders have complete documentation
- [ ] Each request has: request.md, requirements.md, specs.md
- [ ] Requirements are specific and testable
- [ ] Specs include concrete examples

### Overview (outputs/overview/)
- [ ] README.md lists all requests with accurate status
- [ ] system_vision.md captures high-level goals
- [ ] consolidated_requirements.md has all 40 functional + 24 non-functional
- [ ] implementation_roadmap.md has prioritized phases
- [ ] dependencies.md shows request relationships

### Quality Checks
- [ ] No placeholder text remaining
- [ ] All requirement IDs are unique (REQ-XX-FYY format)
- [ ] Dependencies are complete and accurate
- [ ] Acceptance criteria are testable

## Handoff Preparation

1. Create `hand_off_documents/outgoing.md`:
   - Summary of all requests
   - Key decisions made
   - Open questions for research
   - Recommended research priorities

2. Update project status:
   - Mark stage as complete in status.json
   - Note completion date

3. Prepare for Stage 02 (Research):
   - Identify which requests need exploration
   - Note any ambiguities to resolve
   - Suggest research approaches

## Output
Summary of completion status and handoff document location.
