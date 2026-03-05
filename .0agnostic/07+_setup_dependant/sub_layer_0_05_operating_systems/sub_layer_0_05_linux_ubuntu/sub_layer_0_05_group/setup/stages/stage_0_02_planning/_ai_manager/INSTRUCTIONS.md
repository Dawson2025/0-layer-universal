---
resource_id: "7894f1f5-3cef-4586-af9b-1fd67799a6e1"
resource_type: "document"
resource_name: "INSTRUCTIONS"
---
# AI Manager: Stage 0.02 - Planning

<!-- section_id: "e7f46fa8-a55c-4fb4-99d7-3f6f7e69af15" -->
## Your Role
Create detailed execution plans based on technical specifications.

<!-- section_id: "a52f1054-0b1e-4379-9306-24100b853e46" -->
## On Entry
1. Read `../HANDOFF.md` first
2. Read `../../stage_0_01_instructions/output/SPEC_*.md`
3. Understand the technical approach

<!-- section_id: "3da86f5d-0522-46eb-9585-ef0bbe9f5b1a" -->
## Your Tasks
- [ ] Break work into phases/steps
- [ ] Identify dependencies between steps
- [ ] Estimate effort/complexity
- [ ] Create rollback/contingency plans
- [ ] Update `../HANDOFF.md` with status

<!-- section_id: "a1c32205-c775-443c-bca7-c78402128b15" -->
## Expected Outputs
```
output/
└── PLAN_[project_name].md
```

<!-- section_id: "902f56e4-7830-4c70-ac05-1b65d2ad84b0" -->
## Rules
- Reference specs, don't repeat them
- Make steps actionable and clear
- Consider failure scenarios
- Follow `CROSS_OS_COMPATIBILITY_RULES.md`

<!-- section_id: "6a30cecd-13de-41ae-95d5-a44daecd8e39" -->
## Completion Checklist
- [ ] Plan documented with clear phases
- [ ] Dependencies mapped
- [ ] Rollback plan included
- [ ] HANDOFF.md updated
- [ ] Ready for stage_0_03

<!-- section_id: "886e3902-4a57-4536-b56f-35b68f599b83" -->
## Hand Off
Update `../HANDOFF.md` status to COMPLETE. Note: "Ready for stage_0_03 execution"
