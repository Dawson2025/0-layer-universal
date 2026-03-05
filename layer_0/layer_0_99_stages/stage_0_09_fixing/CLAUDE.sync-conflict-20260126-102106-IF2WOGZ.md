---
resource_id: "4d586148-b69b-46f3-8417-121dc103924e"
resource_type: "document"
resource_name: "CLAUDE.sync-conflict-20260126-102106-IF2WOGZ"
---
# Stage 07: Fixing

<!-- section_id: "008a4b7f-11d4-4f46-b90d-e09d78928701" -->
## Purpose
Address identified issues and defects. This stage implements fixes, improvements, and refinements based on criticism and testing feedback.

<!-- section_id: "06631705-a097-4b92-8076-10147ca3d910" -->
## Entry Criteria
- Criticism report received
- Issues prioritized
- Root causes identified
- Fix scope agreed

<!-- section_id: "8ec3d7d4-37f8-4e97-930f-081cb33726f1" -->
## Exit Criteria
- All critical issues resolved
- Fixes verified
- Regression testing passed
- Documentation updated
- Ready for deployment or archival

<!-- section_id: "6e5ad4f8-8c34-4cb7-b79a-c1798483894f" -->
## Typical Tasks
- Fix reported defects
- Implement improvements
- Address technical debt
- Update tests for fixes
- Verify fixes work correctly
- Document changes made

<!-- section_id: "596f4aa8-82a2-48bb-8326-17b6551a68bc" -->
## Handoffs
- **From Previous (06_criticism)**: CRITICISM_REPORT
- **To Next (09_archives)**: FIXED_IMPLEMENTATION ready for archival

<!-- section_id: "87f35c99-65f5-4d68-9287-835587b37b76" -->
## Directory Structure
```
stage_0_09_fixing/
├── CLAUDE.md             # This file
├── ai_agent_system/      # AI tool configs for this stage
└── hand_off_documents/   # Stage handoffs
```

<!-- section_id: "5bb6ba0f-0d64-4703-9158-a9272a463763" -->
## AI Agent Guidelines
When working in this stage:
- Address root causes, not symptoms
- Verify fixes do not introduce regressions
- Update tests to prevent recurrence
- Document what was fixed and why
- Consider fix impact on other components
- Prioritize critical fixes first
