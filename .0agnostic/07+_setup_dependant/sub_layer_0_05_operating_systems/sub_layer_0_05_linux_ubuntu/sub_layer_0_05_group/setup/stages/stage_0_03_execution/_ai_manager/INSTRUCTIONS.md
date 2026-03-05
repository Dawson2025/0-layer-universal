---
resource_id: "27381823-1888-4480-bd16-d6a268e45d84"
resource_type: "document"
resource_name: "INSTRUCTIONS"
---
# AI Manager: Stage 0.03 - Execution

## Your Role
Execute the plan, track progress, generate outputs, handle blockers.

## On Entry
1. Read `../HANDOFF.md` first
2. Read `../../stage_0_02_planning/output/PLAN_*.md`
3. Check `../output/PROGRESS_*.md` for current state

## Your Tasks
- [ ] Execute steps from plan in order
- [ ] Track progress in PROGRESS_*.md
- [ ] Generate required outputs (scripts, configs, etc.)
- [ ] Handle blockers - document and escalate if needed
- [ ] Update `../HANDOFF.md` frequently

## Expected Outputs
```
output/
├── PROGRESS_[project_name].md    # Status tracking
└── [generated files]             # Scripts, configs, docs
```

## Rules
- Follow the plan unless blocked
- Document everything you do
- Update HANDOFF.md before stopping
- Follow `CROSS_OS_COMPATIBILITY_RULES.md` for all file creation
- Test outputs when possible

## Blockers Protocol
1. Document blocker in PROGRESS_*.md
2. Update HANDOFF.md with blocker status
3. List what's needed to unblock
4. Continue with non-blocked items if possible

## Completion Checklist
- [ ] All plan steps executed or documented as blocked
- [ ] Outputs generated and stored in output/
- [ ] PROGRESS_*.md up to date
- [ ] HANDOFF.md reflects final status
- [ ] User informed of completion/blockers

## Hand Off
Update `../HANDOFF.md` with final status. If complete, note "Ready for verification". If blocked, clearly state what's needed.
