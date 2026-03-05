---
resource_id: "8f29de62-bfc8-44a9-a6f7-857e4d813197"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-102106-IF2WOGZ"
---
# Stage 06: Criticism

<!-- section_id: "2668e1ac-3020-46e9-b210-278756c067b3" -->
## Purpose
Critically evaluate the work product. This stage provides objective assessment, identifies improvements, and validates quality standards are met.

<!-- section_id: "d6de7d7a-638c-4452-9f2a-f0c147c09b5e" -->
## Entry Criteria
- Test results received
- Implementation available for review
- Quality criteria defined

<!-- section_id: "a09d5b4a-665d-4c12-bb0a-d2cc427a2058" -->
## Exit Criteria
- Critical review completed
- Issues prioritized
- Improvement recommendations documented
- Go/no-go decision made
- Handoff prepared for Fixing

<!-- section_id: "d1c13803-f195-4ce2-8b85-1afeedb65870" -->
## Typical Tasks
- Review code quality
- Assess architecture decisions
- Evaluate test coverage
- Check documentation completeness
- Identify technical debt
- Provide actionable feedback

<!-- section_id: "565e138e-2bac-4e86-8d29-6bc53393249e" -->
## Handoffs
- **From Previous (05_testing)**: TEST_RESULTS
- **To Next (07_fixing)**: CRITICISM_REPORT with issues and recommendations

<!-- section_id: "40018d39-ca0a-4c43-848e-9eea391de0c2" -->
## Directory Structure
```
stage_0_08_criticism/
├── CLAUDE.md             # This file
├── ai_agent_system/      # AI tool configs for this stage
└── hand_off_documents/   # Stage handoffs
```

<!-- section_id: "84b27abf-c8be-4b9b-ae35-55ecd3f0cd10" -->
## AI Agent Guidelines
When working in this stage:
- Be objective and constructive
- Prioritize issues by impact
- Provide specific, actionable feedback
- Consider both short and long-term impacts
- Document rationale for recommendations
- Distinguish critical from nice-to-have issues
