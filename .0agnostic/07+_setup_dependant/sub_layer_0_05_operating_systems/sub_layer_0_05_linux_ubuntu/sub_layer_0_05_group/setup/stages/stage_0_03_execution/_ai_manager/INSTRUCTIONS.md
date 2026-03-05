---
resource_id: "27381823-1888-4480-bd16-d6a268e45d84"
resource_type: "document"
resource_name: "INSTRUCTIONS"
---
# AI Manager: Stage 0.03 - Execution

<!-- section_id: "26168cc1-12b9-4824-9527-baaea62288ed" -->
## Your Role
Execute the plan, track progress, generate outputs, handle blockers.

<!-- section_id: "bfe051d9-0089-46ac-87b0-ec821b63b1f8" -->
## On Entry
1. Read `../HANDOFF.md` first
2. Read `../../stage_0_02_planning/output/PLAN_*.md`
3. Check `../output/PROGRESS_*.md` for current state

<!-- section_id: "06b0b1bf-6be9-456c-9d4f-c7d22179ecf3" -->
## Your Tasks
- [ ] Execute steps from plan in order
- [ ] Track progress in PROGRESS_*.md
- [ ] Generate required outputs (scripts, configs, etc.)
- [ ] Handle blockers - document and escalate if needed
- [ ] Update `../HANDOFF.md` frequently

<!-- section_id: "33c10f51-6f4f-46e1-badd-2a7a631da347" -->
## Expected Outputs
```
output/
├── PROGRESS_[project_name].md    # Status tracking
└── [generated files]             # Scripts, configs, docs
```

<!-- section_id: "e1e3ee6e-7857-4751-b3c3-7d657ef0824d" -->
## Rules
- Follow the plan unless blocked
- Document everything you do
- Update HANDOFF.md before stopping
- Follow `CROSS_OS_COMPATIBILITY_RULES.md` for all file creation
- Test outputs when possible

<!-- section_id: "3d0f94f3-eaf0-4135-a250-2229d758c706" -->
## Blockers Protocol
1. Document blocker in PROGRESS_*.md
2. Update HANDOFF.md with blocker status
3. List what's needed to unblock
4. Continue with non-blocked items if possible

<!-- section_id: "221b7056-2d0d-4d0f-9835-fd47d5a150c5" -->
## Completion Checklist
- [ ] All plan steps executed or documented as blocked
- [ ] Outputs generated and stored in output/
- [ ] PROGRESS_*.md up to date
- [ ] HANDOFF.md reflects final status
- [ ] User informed of completion/blockers

<!-- section_id: "0e9f25e8-62ba-4dc2-a1f6-f946ccfc45ad" -->
## Hand Off
Update `../HANDOFF.md` with final status. If complete, note "Ready for verification". If blocked, clearly state what's needed.
