---
resource_id: "efdf87af-51e6-4d1a-8146-51d89b483aaf"
resource_type: "output"
resource_name: "QUICK_REFERENCE"
---
# AI Manager Hierarchy - Quick Reference Guide

**Purpose**: Fast lookup for common tasks and locations
**Audience**: AI agents and developers working with the hierarchy

---

<!-- section_id: "84f10fce-a190-4295-b54b-fc555ddc9ef0" -->
## Quick Start (5 Minutes)

1. **Read**: `HIERARCHY_QUICK_START.md` in `sub_layer_0_01_basic_prompts_throughout/`
2. **Understand**: Layers (L0-L3), Stages (9-step pipeline), Handoffs (JSON communication)
3. **Find your OS context**: `layer_N/.../os/{wsl|linux_ubuntu}/CLAUDE.md`
4. **Check adoption checklist**: `HIERARCHY_ADOPTION_CHECKLIST.md`

---

<!-- section_id: "ece7e3f0-10a2-484e-bf7a-4e51eb797ae0" -->
## Common Tasks

<!-- section_id: "aa9cc549-0484-4985-b7bc-f38f1c7586db" -->
### "I need to spawn a worker agent"
1. Read CLI recursion syntax: `sub_layer_0_13_universal_protocols/cli_recursion/`
2. Check your OS context: `layer_N/.../os/{your_os}/AGENTS.md`
3. Create handoff document using schema: `handoff_schema.md`
4. Use CLI pattern from syntax guide

<!-- section_id: "868ce0ca-d316-4453-8fff-506c50d7e698" -->
### "I need to integrate a framework (LangGraph, AutoGen, etc.)"
1. Read framework orchestration: `sub_layer_0_13_universal_protocols/framework_orchestration/`
2. Check when to use frameworks vs. handoffs
3. Follow integration patterns in guide
4. Reference normative spec: `framework_orchestration.md` in ideal hierarchy

<!-- section_id: "e7bd5a82-5e7b-4e20-9850-aeca3a72e43f" -->
### "I need to log/monitor my work"
1. Read observability protocol: `sub_layer_0_13_universal_protocols/observability/`
2. Follow structured logging format (JSON)
3. Place logs in: `layer_N/stage_N.XX_.../ai_agent_system/logs/`
4. Include trace_id for distributed tracing

<!-- section_id: "1f93a9b0-2678-44e3-9798-db7526d74f7e" -->
### "I need to check my permissions"
1. Read safety/governance: `sub_layer_0_04_universal_rules/safety_governance.md`
2. Find your layer's permission level
3. Check approval gate requirements
4. Verify budget limits

<!-- section_id: "81224016-dced-4081-b380-7948f634efc8" -->
### "I need to deploy to production"
1. Read deployment overview: `sub_layer_0_05_os_setup/.../deployment/AI_MANAGER_HIERARCHY_DEPLOYMENT.md`
2. Choose architecture (single-machine, distributed, production scale)
3. Configure environment (dev/staging/prod)
4. Follow deployment pipeline

<!-- section_id: "6b07043f-f8eb-46a4-9aca-2430eb1dc052" -->
### "I need to adopt this in my project"
1. Read rollout plan: `/home/dawson/.cursor/plans/ai_manager_hierarchy_rollout_plan.md`
2. Follow adoption checklist: `HIERARCHY_ADOPTION_CHECKLIST.md`
3. Use migration guide if existing project: `MIGRATION_GUIDE.md`
4. Start with pilot feature/component

---

<!-- section_id: "812baa3c-212d-4851-9c0f-282bb0bbdab7" -->
## File Locations Cheat Sheet

<!-- section_id: "febf7b89-d32c-401f-87bb-8e0cead573a6" -->
### Entry Points
```
SYSTEM_OVERVIEW.md                          → High-level overview
USAGE_GUIDE.md                              → How to use hierarchy
HIERARCHY_QUICK_START.md                    → 5-10 min onboarding
```

<!-- section_id: "74359794-babf-45e6-807e-67a695444893" -->
### Manager/Worker Patterns
```
layer_0_group/0.00_ai_manager_system/   → L0 manager patterns
layer_2_project/1.00_ai_manager_system/     → L1 manager patterns
layer_2_features/2.00_ai_manager_system/    → L2 manager patterns
layer_4_components/3.00_ai_manager_system/  → L3 manager patterns
```

<!-- section_id: "d399cf7c-299b-474f-b1e7-c4516969e801" -->
### Handoff Schema
```
layer_0_group/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md
```

<!-- section_id: "d3895daf-5376-4693-aaec-c4a509a22bbf" -->
### OS Context (replace N with layer number, OS with wsl/linux_ubuntu)
```
layer_N/.../stage_N.01_instructions/ai_agent_system/os/{OS}/CLAUDE.md
layer_N/.../stage_N.01_instructions/ai_agent_system/os/{OS}/AGENTS.md
layer_N/.../stage_N.01_instructions/ai_agent_system/os/{OS}/GEMINI.md
```

<!-- section_id: "fa9cf770-5970-4e0c-8c46-9f55a18c2448" -->
### Operational Protocols
```
sub_layer_0_13_universal_protocols/framework_orchestration/
sub_layer_0_13_universal_protocols/cli_recursion/
sub_layer_0_13_universal_protocols/observability/
```

<!-- section_id: "fe256a4b-9e06-45f6-b6f2-fe20225b1e9f" -->
### Rules & Governance
```
sub_layer_0_04_universal_rules/safety_governance.md
```

<!-- section_id: "e509abae-1e5a-4bb1-bf23-8b175678b922" -->
### Deployment
```
sub_layer_0_05_os_setup/.../deployment/AI_MANAGER_HIERARCHY_DEPLOYMENT.md
```

<!-- section_id: "d7966dcc-ba09-4b03-b1c7-5710aeba862a" -->
### Adoption Resources
```
HIERARCHY_ADOPTION_CHECKLIST.md             → New project onboarding
MIGRATION_GUIDE.md                          → Existing project migration
implementation_lessons_learned.md            → Feedback template
```

---

<!-- section_id: "2497e9b6-36c2-4e6d-8a55-06d4afd75a7c" -->
## Layer Quick Reference

| Layer | Purpose | Manager Tool | Worker Tool | Example |
|-------|---------|--------------|-------------|---------|
| L0 | Universal rules, tools, standards | Claude Code / Gemini | Claude Code | Security policies, coding standards |
| L1 | Project-specific constraints | Claude Code / Gemini | Claude Code / Codex | Project architecture, tech stack |
| L2 | Individual features | Claude Code | Codex CLI | Auth system, payment processing |
| L3 | Concrete components | Claude Code | Codex CLI | LoginForm, PaymentGateway |
| L4+ | Sub-components (optional) | Codex CLI | Codex CLI | FormUI, Validation, APIHandler |

---

<!-- section_id: "8d1f0f9f-23cd-46ac-95f8-3c4be96a690d" -->
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

<!-- section_id: "b2c3e154-e58e-4354-9ac4-4e7f791f2f55" -->
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

<!-- section_id: "c46530fb-f4ec-4ba8-89f4-9fc67aa36dfd" -->
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

<!-- section_id: "09b00375-95a1-4051-a02e-f28a772b78b2" -->
## Tool Specialization

<!-- section_id: "236a145d-9110-4844-9cc9-124be8cc0fe7" -->
### Claude Code (Managers, Complex Work)
- Roles: L0-L2 managers, criticism, complex multi-file work
- Strengths: Deep reasoning, broad context, cascading instructions
- Use for: Decomposition, aggregation, architectural decisions

<!-- section_id: "f1322b12-0c35-42c1-a361-71b0e0dbbe00" -->
### Codex CLI (Workers, Atomic Tasks)
- Roles: L2-L4 workers, testing, bounded implementation
- Strengths: Fast, focused, short sessions, atomic operations
- Use for: Single-file changes, test writing, bounded execution

<!-- section_id: "53ee91c9-ec22-4a8a-945c-965533f52ad0" -->
### Gemini CLI (Planning, Research)
- Roles: Request, instructions, planning stages, research
- Strengths: Long dialogues, research-heavy, exploration
- Use for: Requirements gathering, planning, documentation research

<!-- section_id: "dfa19fb2-5916-48cf-b608-8455d3a82050" -->
### Cursor IDE (Interactive, Debugging)
- Roles: Human-in-the-loop, interactive debugging
- Strengths: Visual feedback, real-time interaction
- Use for: Debugging complex issues, refactoring with human guidance

---

<!-- section_id: "854736e5-2374-421c-8fde-7e44af06b26f" -->
## Common Commands

<!-- section_id: "d885e400-d371-4085-be58-8bef4d48a890" -->
### Spawn Worker (CLI Recursion)
```bash
# Generic pattern
{claude-code|codex|gemini} --session "{task}" \
  --context "layer_N/stage_N.XX_.../hand_off_documents/incoming.json" \
  --output "layer_N/stage_N.XX_.../hand_off_documents/outgoing.json"
```

<!-- section_id: "7de3a371-01b8-4ab2-bf41-907971c508db" -->
### Check Logs
```bash
# View observability logs
cat layer_N/stage_N.XX_.../ai_agent_system/logs/agent_YYYYMMDD_HHMMSS.json

# Follow live logs (if supported)
tail -f layer_N/stage_N.XX_.../ai_agent_system/logs/current.log
```

<!-- section_id: "50009462-6021-47c3-b73a-03262b0df950" -->
### Validate Handoff
```bash
# Check handoff against schema (if tooling exists)
validate-handoff handoff_schema.md incoming.json
```

---

<!-- section_id: "ca5a2452-a8de-4a4a-800c-2b807ea42b3b" -->
## Troubleshooting

<!-- section_id: "ce643661-1da2-43b9-b397-4b4b91ca06e7" -->
### "I can't find the right OS context"
→ Check: `layer_N/.../stage_N.01_instructions/ai_agent_system/os/{wsl|linux_ubuntu}/`
→ If missing for Windows/macOS, directories exist but files not yet created

<!-- section_id: "433f6659-7c8d-4d14-8a6b-42b4cbeb35de" -->
### "I don't know which layer to work at"
→ L3 for most component work
→ L2 for feature-level changes
→ L1 for project-wide changes
→ L0 only for universal rules/standards

<!-- section_id: "49a1e299-0ede-4855-a09b-572c588f7f65" -->
### "I'm not sure if I need a framework or handoffs"
→ Use handoffs for most work (simpler, more explicit)
→ Use frameworks when you need complex parallelism or specialized orchestration
→ See `framework_orchestration_overview.md` for guidance

<!-- section_id: "36d62488-ed06-47f0-acc9-d52f71aa15e1" -->
### "My budget is being exceeded"
→ Check: `safety_governance.md` for limits
→ Use cheaper models (Haiku for simple tasks)
→ Break work into smaller subtasks
→ Check if you're at the right layer (lower layers = lower budgets)

---

<!-- section_id: "1198aae4-867d-49be-92dc-2c9cb89e7d23" -->
## Help & Resources

<!-- section_id: "a18d5e1b-143d-49a9-b51d-1fae59a07ce4" -->
### For Questions
→ Review normative specs: `-1_research/.../things_learned/ideal_ai_manager_hierarchy_system/`
→ Check implementation docs: `implementation/`
→ Read adoption guides: `HIERARCHY_ADOPTION_CHECKLIST.md`, `MIGRATION_GUIDE.md`

<!-- section_id: "4b195ec2-d758-4a02-b764-654543f7fc3a" -->
### For Issues
→ Document in: `implementation_lessons_learned.md`
→ Check troubleshooting: `implementation/guides/TROUBLESHOOTING.md`
→ Review phase summaries: `implementation/phase_summaries/`

<!-- section_id: "1024bc6b-6874-4556-93d9-b035f2813237" -->
### For Feedback
→ Use lessons learned template
→ Submit via continuous improvement process
→ Weekly/bi-weekly/monthly/quarterly cycles

---

**Last Updated**: 2025-12-24
**Version**: 1.0
**Purpose**: Quick reference for common hierarchy tasks
