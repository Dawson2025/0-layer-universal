---
resource_id: "8f29de62-bfc8-44a9-a6f7-857e4d813197"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-102106-IF2WOGZ"
---
# Stage 06: Criticism

## Purpose
Critically evaluate the work product. This stage provides objective assessment, identifies improvements, and validates quality standards are met.

## Entry Criteria
- Test results received
- Implementation available for review
- Quality criteria defined

## Exit Criteria
- Critical review completed
- Issues prioritized
- Improvement recommendations documented
- Go/no-go decision made
- Handoff prepared for Fixing

## Typical Tasks
- Review code quality
- Assess architecture decisions
- Evaluate test coverage
- Check documentation completeness
- Identify technical debt
- Provide actionable feedback

## Handoffs
- **From Previous (05_testing)**: TEST_RESULTS
- **To Next (07_fixing)**: CRITICISM_REPORT with issues and recommendations

## Directory Structure
```
stage_0_08_criticism/
├── CLAUDE.md             # This file
├── ai_agent_system/      # AI tool configs for this stage
└── hand_off_documents/   # Stage handoffs
```

## AI Agent Guidelines
When working in this stage:
- Be objective and constructive
- Prioritize issues by impact
- Provide specific, actionable feedback
- Consider both short and long-term impacts
- Document rationale for recommendations
- Distinguish critical from nice-to-have issues
