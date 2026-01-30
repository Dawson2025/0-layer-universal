# Stage 07: Fixing

## Purpose
Address identified issues and defects. This stage implements fixes, improvements, and refinements based on criticism and testing feedback.

## Entry Criteria
- Criticism report received
- Issues prioritized
- Root causes identified
- Fix scope agreed

## Exit Criteria
- All critical issues resolved
- Fixes verified
- Regression testing passed
- Documentation updated
- Ready for deployment or archival

## Typical Tasks
- Fix reported defects
- Implement improvements
- Address technical debt
- Update tests for fixes
- Verify fixes work correctly
- Document changes made

## Handoffs
- **From Previous (06_criticism)**: CRITICISM_REPORT
- **To Next (09_archives)**: FIXED_IMPLEMENTATION ready for archival

## Directory Structure
```
stage_0_09_fixing/
├── CLAUDE.md             # This file
├── ai_agent_system/      # AI tool configs for this stage
└── hand_off_documents/   # Stage handoffs
```

## AI Agent Guidelines
When working in this stage:
- Address root causes, not symptoms
- Verify fixes do not introduce regressions
- Update tests to prevent recurrence
- Document what was fixed and why
- Consider fix impact on other components
- Prioritize critical fixes first
