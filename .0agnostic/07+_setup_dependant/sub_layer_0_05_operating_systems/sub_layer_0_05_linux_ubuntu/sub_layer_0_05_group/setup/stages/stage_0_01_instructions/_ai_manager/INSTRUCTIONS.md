---
resource_id: "ff9f12cf-0f49-4761-8e9f-af62ba848168"
resource_type: "document"
resource_name: "INSTRUCTIONS"
---
# AI Manager: Stage 0.01 - Instructions/Specifications

## Your Role
Create technical specifications based on requirements. Define interfaces, data structures, and technical approach.

## On Entry
1. Read `../HANDOFF.md` first
2. Read `../../stage_0_00_request_gathering/output/REQUEST_*.md`
3. Understand the requirements fully

## Your Tasks
- [ ] Define technical approach
- [ ] Specify interfaces/APIs
- [ ] Document data structures
- [ ] List dependencies
- [ ] Note technical constraints
- [ ] Update `HANDOFF.md` with status

## Expected Outputs
```
output/
└── SPEC_[project_name].md
```

## Rules
- Reference requirements, don't repeat them
- Be specific and unambiguous
- Consider cross-OS compatibility (see `CROSS_OS_COMPATIBILITY_RULES.md`)
- Don't implement yet - just specify

## Completion Checklist
- [ ] Technical spec documented
- [ ] All requirements addressed
- [ ] Dependencies identified
- [ ] HANDOFF.md updated
- [ ] Ready for stage_0_02

## Hand Off
When complete, update `../HANDOFF.md` status to COMPLETE and note that stage_0_02 is ready.
