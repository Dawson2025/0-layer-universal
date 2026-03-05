---
resource_id: "7869e7bc-9d7c-4e87-8d59-0ee538eedeb6"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-035816-IF2WOGZ"
---
# Stage 06: Criticism

<!-- section_id: "0fe76bf3-13f8-44e1-b96c-faa014416577" -->
## Purpose
Critically evaluate the work product. This stage provides objective assessment, identifies improvements, and validates quality standards are met.

<!-- section_id: "0fe3cb5c-cf42-4d22-b48c-f13928e65d5b" -->
## Entry Criteria
- Test results received
- Implementation available for review
- Quality criteria defined

<!-- section_id: "cb0b77d5-be54-4d1d-8f6c-01eceec91ab0" -->
## Exit Criteria
- Critical review completed
- Issues prioritized
- Improvement recommendations documented
- Go/no-go decision made
- Handoff prepared for Fixing

<!-- section_id: "fb02fa4d-d663-4887-a13c-9f90e61a2c3b" -->
## Typical Tasks
- Review code quality
- Assess architecture decisions
- Evaluate test coverage
- Check documentation completeness
- Identify technical debt
- Provide actionable feedback

<!-- section_id: "85184d2f-504e-4dc6-b032-cb4bf9718c22" -->
## Handoffs
- **From Previous (05_testing)**: TEST_RESULTS
- **To Next (07_fixing)**: CRITICISM_REPORT with issues and recommendations

<!-- section_id: "bdf0a2cd-1236-46a7-bb01-dca15528a1e4" -->
## Directory Structure
```
stage_0_08_criticism/
├── CLAUDE.md             # This file
├── ai_agent_system/      # AI tool configs for this stage
└── hand_off_documents/   # Stage handoffs
```

<!-- section_id: "b4e76f13-b258-4df5-8361-8b351e5b65e9" -->
## AI Agent Guidelines
When working in this stage:
- Be objective and constructive
- Prioritize issues by impact
- Provide specific, actionable feedback
- Consider both short and long-term impacts
- Document rationale for recommendations
- Distinguish critical from nice-to-have issues
