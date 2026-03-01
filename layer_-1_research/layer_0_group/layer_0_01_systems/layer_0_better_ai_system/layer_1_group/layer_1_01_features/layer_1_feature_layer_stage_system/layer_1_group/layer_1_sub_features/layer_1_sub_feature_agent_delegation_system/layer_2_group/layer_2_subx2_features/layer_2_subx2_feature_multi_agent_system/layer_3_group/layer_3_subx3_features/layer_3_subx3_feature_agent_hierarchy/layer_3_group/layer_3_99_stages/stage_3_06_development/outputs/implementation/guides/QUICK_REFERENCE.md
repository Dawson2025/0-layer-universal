# AI Manager Hierarchy - Quick Reference Guide

**Purpose**: Fast lookup for common tasks and locations
**Audience**: AI agents and developers working with the hierarchy

---

## Quick Start (5 Minutes)

1. **Read**: `HIERARCHY_QUICK_START.md` in `sub_layer_0_01_basic_prompts_throughout/`
2. **Understand**: Layers (L0-L3), Stages (9-step pipeline), Handoffs (JSON communication)
3. **Find your OS context**: `layer_N/.../os/{wsl|linux_ubuntu}/CLAUDE.md`
4. **Check adoption checklist**: `HIERARCHY_ADOPTION_CHECKLIST.md`

---

## Common Tasks

### "I need to spawn a worker agent"
1. Read CLI recursion syntax: `sub_layer_0_13_universal_protocols/cli_recursion/`
2. Check your OS context: `layer_N/.../os/{your_os}/AGENTS.md`
3. Create handoff document using schema: `handoff_schema.md`
4. Use CLI pattern from syntax guide

### "I need to integrate a framework (LangGraph, AutoGen, etc.)"
1. Read framework orchestration: `sub_layer_0_13_universal_protocols/framework_orchestration/`
2. Check when to use frameworks vs. handoffs
3. Follow integration patterns in guide
4. Reference normative spec: `framework_orchestration.md` in ideal hierarchy

### "I need to log/monitor my work"
1. Read observability protocol: `sub_layer_0_13_universal_protocols/observability/`
2. Follow structured logging format (JSON)
3. Place logs in: `layer_N/stage_N.XX_.../ai_agent_system/logs/`
4. Include trace_id for distributed tracing

### "I need to check my permissions"
1. Read safety/governance: `sub_layer_0_04_universal_rules/safety_governance.md`
2. Find your layer's permission level
3. Check approval gate requirements
4. Verify budget limits

### "I need to deploy to production"
1. Read deployment overview: `sub_layer_0_05_os_setup/.../deployment/AI_MANAGER_HIERARCHY_DEPLOYMENT.md`
2. Choose architecture (single-machine, distributed, production scale)
3. Configure environment (dev/staging/prod)
4. Follow deployment pipeline

### "I need to adopt this in my project"
1. Read rollout plan: `/home/dawson/.cursor/plans/ai_manager_hierarchy_rollout_plan.md`
2. Follow adoption checklist: `HIERARCHY_ADOPTION_CHECKLIST.md`
3. Use migration guide if existing project: `MIGRATION_GUIDE.md`
4. Start with pilot feature/component

---

## File Locations Cheat Sheet

### Entry Points
```
SYSTEM_OVERVIEW.md                          → High-level overview
USAGE_GUIDE.md                              → How to use hierarchy
HIERARCHY_QUICK_START.md                    → 5-10 min onboarding
```

### Manager/Worker Patterns
```
layer_0_group/0.00_ai_manager_system/   → L0 manager patterns
layer_2_project/1.00_ai_manager_system/     → L1 manager patterns
layer_3_features/2.00_ai_manager_system/    → L2 manager patterns
layer_4_components/3.00_ai_manager_system/  → L3 manager patterns
```

### Handoff Schema
```
layer_0_group/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md
```

### OS Context (replace N with layer number, OS with wsl/linux_ubuntu)
```
layer_N/.../stage_N.01_instructions/ai_agent_system/os/{OS}/CLAUDE.md
layer_N/.../stage_N.01_instructions/ai_agent_system/os/{OS}/AGENTS.md
layer_N/.../stage_N.01_instructions/ai_agent_system/os/{OS}/GEMINI.md
```

### Operational Protocols
```
sub_layer_0_13_universal_protocols/framework_orchestration/
sub_layer_0_13_universal_protocols/cli_recursion/
sub_layer_0_13_universal_protocols/observability/
```

### Rules & Governance
```
sub_layer_0_04_universal_rules/safety_governance.md
```

### Deployment
```
sub_layer_0_05_os_setup/.../deployment/AI_MANAGER_HIERARCHY_DEPLOYMENT.md
```

### Adoption Resources
```
HIERARCHY_ADOPTION_CHECKLIST.md             → New project onboarding
MIGRATION_GUIDE.md                          → Existing project migration
implementation_lessons_learned.md            → Feedback template
```

---

## Layer Quick Reference

| Layer | Purpose | Manager Tool | Worker Tool | Example |
|-------|---------|--------------|-------------|---------|
| L0 | Universal rules, tools, standards | Claude Code / Gemini | Claude Code | Security policies, coding standards |
| L1 | Project-specific constraints | Claude Code / Gemini | Claude Code / Codex | Project architecture, tech stack |
| L2 | Individual features | Claude Code | Codex CLI | Auth system, payment processing |
| L3 | Concrete components | Claude Code | Codex CLI | LoginForm, PaymentGateway |
| L4+ | Sub-components (optional) | Codex CLI | Codex CLI | FormUI, Validation, APIHandler |

---

## Stage Quick Reference

| # | Stage | Purpose | Typical Tool |
|---|-------|---------|--------------|
| 0 | request | Clarify what needs to be done | Gemini CLI |
| 1 | instructions | Define explicit requirements | Gemini CLI |
| 2 | planning | Break work into subtasks | Gemini CLI / Claude Code |
| 3 | design | Choose architectures, interfaces | Claude Code |
| 4 | implementation | Write code | Claude Code / Codex CLI |
| 5 | testing | Verify functionality | Codex CLI |
| 6 | criticism | Review against standards | Claude Code |
| 7 | fixing | Apply corrections | Codex CLI |
| 8 | archiving | Document and close | Any tool |

---

## Handoff JSON Template

```json
{
  "schemaVersion": "1.0.0",
  "id": "handoff-lN-feature-stage-YYYYMMDD-hash",
  "kind": "implementation",
  "layer": N,
  "stage": "stage_N.04_development",
  "from": "layer_N/feature-name/planning",
  "to": "layer_N/feature-name/implementation",
  "createdAt": "2025-12-24T12:00:00Z",
  "task": "Implement feature X",
  "constraints": ["TypeScript", "React", "Accessible"],
  "artifacts": {
    "files": ["src/components/Feature.tsx"]
  },
  "status": "pending"
}
```

---

## Permission Levels Quick Reference

| Level | Layer | What You Can Do |
|-------|-------|-----------------|
| 4 | L0 | Everything (with approval gates) |
| 3 | L1 | Project-level changes (project directory + deps) |
| 2 | L2 | Feature directory + tests, no global changes |
| 1 | L3/L4 | Component directory only |

**Budget Limits**:
- Daily total: $50
- L0 manager: $20/task
- L1 manager: $10/task
- L2 agent: $5/task
- L3 worker: $1/task

---

## Tool Specialization

### Claude Code (Managers, Complex Work)
- Roles: L0-L2 managers, criticism, complex multi-file work
- Strengths: Deep reasoning, broad context, cascading instructions
- Use for: Decomposition, aggregation, architectural decisions

### Codex CLI (Workers, Atomic Tasks)
- Roles: L2-L4 workers, testing, bounded implementation
- Strengths: Fast, focused, short sessions, atomic operations
- Use for: Single-file changes, test writing, bounded execution

### Gemini CLI (Planning, Research)
- Roles: Request, instructions, planning stages, research
- Strengths: Long dialogues, research-heavy, exploration
- Use for: Requirements gathering, planning, documentation research

### Cursor IDE (Interactive, Debugging)
- Roles: Human-in-the-loop, interactive debugging
- Strengths: Visual feedback, real-time interaction
- Use for: Debugging complex issues, refactoring with human guidance

---

## Common Commands

### Spawn Worker (CLI Recursion)
```bash
# Generic pattern
{claude-code|codex|gemini} --session "{task}" \
  --context "layer_N/stage_N.XX_.../hand_off_documents/incoming.json" \
  --output "layer_N/stage_N.XX_.../hand_off_documents/outgoing.json"
```

### Check Logs
```bash
# View observability logs
cat layer_N/stage_N.XX_.../ai_agent_system/logs/agent_YYYYMMDD_HHMMSS.json

# Follow live logs (if supported)
tail -f layer_N/stage_N.XX_.../ai_agent_system/logs/current.log
```

### Validate Handoff
```bash
# Check handoff against schema (if tooling exists)
validate-handoff handoff_schema.md incoming.json
```

---

## Troubleshooting

### "I can't find the right OS context"
→ Check: `layer_N/.../stage_N.01_instructions/ai_agent_system/os/{wsl|linux_ubuntu}/`
→ If missing for Windows/macOS, directories exist but files not yet created

### "I don't know which layer to work at"
→ L3 for most component work
→ L2 for feature-level changes
→ L1 for project-wide changes
→ L0 only for universal rules/standards

### "I'm not sure if I need a framework or handoffs"
→ Use handoffs for most work (simpler, more explicit)
→ Use frameworks when you need complex parallelism or specialized orchestration
→ See `framework_orchestration_overview.md` for guidance

### "My budget is being exceeded"
→ Check: `safety_governance.md` for limits
→ Use cheaper models (Haiku for simple tasks)
→ Break work into smaller subtasks
→ Check if you're at the right layer (lower layers = lower budgets)

---

## Help & Resources

### For Questions
→ Review normative specs: `-1_research/.../things_learned/ideal_ai_manager_hierarchy_system/`
→ Check implementation docs: `implementation/`
→ Read adoption guides: `HIERARCHY_ADOPTION_CHECKLIST.md`, `MIGRATION_GUIDE.md`

### For Issues
→ Document in: `implementation_lessons_learned.md`
→ Check troubleshooting: `implementation/guides/TROUBLESHOOTING.md`
→ Review phase summaries: `implementation/phase_summaries/`

### For Feedback
→ Use lessons learned template
→ Submit via continuous improvement process
→ Weekly/bi-weekly/monthly/quarterly cycles

---

**Last Updated**: 2025-12-24
**Version**: 1.0
**Purpose**: Quick reference for common hierarchy tasks
