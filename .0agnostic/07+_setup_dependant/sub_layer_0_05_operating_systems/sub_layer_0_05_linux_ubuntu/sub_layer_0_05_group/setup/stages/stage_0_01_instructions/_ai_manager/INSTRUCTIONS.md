---
resource_id: "ff9f12cf-0f49-4761-8e9f-af62ba848168"
resource_type: "document"
resource_name: "INSTRUCTIONS"
---
# AI Manager: Stage 0.01 - Instructions/Specifications

<!-- section_id: "ccdd1612-072d-46c5-ba48-20c042d6e2d8" -->
## Your Role
Create technical specifications based on requirements. Define interfaces, data structures, and technical approach.

<!-- section_id: "4a3be2c0-3179-4792-bd9e-d9005d396c99" -->
## On Entry
1. Read `../HANDOFF.md` first
2. Read `../../stage_0_00_request_gathering/output/REQUEST_*.md`
3. Understand the requirements fully

<!-- section_id: "68151e20-18d4-44c2-92e4-ff9b148d21c9" -->
## Your Tasks
- [ ] Define technical approach
- [ ] Specify interfaces/APIs
- [ ] Document data structures
- [ ] List dependencies
- [ ] Note technical constraints
- [ ] Update `HANDOFF.md` with status

<!-- section_id: "1e722588-13b5-43ba-ac60-d1a6239caf5a" -->
## Expected Outputs
```
output/
└── SPEC_[project_name].md
```

<!-- section_id: "e7e2f386-d254-4135-a9c5-d6af05fdca90" -->
## Rules
- Reference requirements, don't repeat them
- Be specific and unambiguous
- Consider cross-OS compatibility (see `CROSS_OS_COMPATIBILITY_RULES.md`)
- Don't implement yet - just specify

<!-- section_id: "9d8beb0b-6cf4-4035-9d92-5982a82c5ae2" -->
## Completion Checklist
- [ ] Technical spec documented
- [ ] All requirements addressed
- [ ] Dependencies identified
- [ ] HANDOFF.md updated
- [ ] Ready for stage_0_02

<!-- section_id: "48e35ae5-2628-402e-ab4d-943f42fcd477" -->
## Hand Off
When complete, update `../HANDOFF.md` status to COMPLETE and note that stage_0_02 is ready.
