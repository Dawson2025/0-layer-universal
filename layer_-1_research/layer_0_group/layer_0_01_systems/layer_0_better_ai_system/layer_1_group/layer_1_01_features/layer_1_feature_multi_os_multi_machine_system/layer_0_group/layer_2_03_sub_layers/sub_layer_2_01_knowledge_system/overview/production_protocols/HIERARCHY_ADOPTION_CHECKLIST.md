---
resource_id: "dedaba5f-5e2a-4296-9ea6-e6a14cdf1c52"
resource_type: "document"
resource_name: "HIERARCHY_ADOPTION_CHECKLIST"
---
# AI Manager Hierarchy - Adoption Checklist

**Purpose**: Step-by-step checklist for projects adopting the AI Manager Hierarchy System
**Target Audience**: Managers, workers, and supervisors working on new or existing projects
**Estimated Time**: 2-4 hours for initial adoption (varies by project complexity)

---

## Overview

This checklist guides you through adopting the AI Manager Hierarchy System for your project. You can adopt the full hierarchy or selectively implement components based on your needs. The checklist is organized into **must-have** (required for basic adoption) and **nice-to-have** (recommended for full benefits) items.

**When to Use This Checklist**:
- Starting a new project from scratch
- Retrofitting an existing project with hierarchy patterns
- Adding new features to a hierarchy-enabled project
- Onboarding a new agent to the hierarchy system

---

## Pre-Adoption: Understand the Hierarchy

### Read Top-Level Documentation (Must-Have)

**Time**: 30-45 minutes

- [ ] **Read MASTER_DOCUMENTATION_INDEX.md**
  - Location: `/home/dawson/code/0_layer_universal/0_context/MASTER_DOCUMENTATION_INDEX.md`
  - Focus: "AI Manager Hierarchy System" section (lines 77-101)
  - Goal: Understand what the hierarchy is and where docs live

- [ ] **Read SYSTEM_OVERVIEW.md**
  - Location: `/home/dawson/code/0_layer_universal/0_context/SYSTEM_OVERVIEW.md`
  - Focus: "Agent OS Architecture" section (lines 8-44)
  - Goal: Understand core concepts (layers, stages, manager/worker, tool specialization)

- [ ] **Read USAGE_GUIDE.md**
  - Location: `/home/dawson/code/0_layer_universal/0_context/USAGE_GUIDE.md`
  - Focus: "Working with the AI Manager Hierarchy" section (lines 12-111)
  - Goal: Know which docs to read first, which layers to touch, how handoffs work

### Understand Layer/Stage Framework (Must-Have)

**Time**: 20-30 minutes

- [ ] **Read Layer/Stage Framework README**
  - Location: `/home/dawson/code/0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md`
  - Goal: Understand L0-L4+ layers and stage pipeline
  - Note: This framework implements the Ideal AI Manager Hierarchy System

- [ ] **Identify your project's layer**
  - L1 (Project): Entire project (e.g., "web-app", "lang-trak")
  - L2 (Feature): Major feature within a project (e.g., "User Authentication")
  - L3 (Component): Specific component within a feature (e.g., "Login Form")
  - L4+ (Sub-component): Nested components (optional, for complex features)

- [ ] **Identify relevant stages for your work**
  - Common stages: 0.00_request_gathering, 0.01_instructions, 0.02_planning, 0.03_research, 0.04_development, 0.05_testing, 0.06_delivery
  - Note: Not all stages are needed for every project

### Read Layer Manager System READMEs (Must-Have)

**Time**: 30-40 minutes

- [ ] **Read Layer 0 Manager System README**
  - Location: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.00_ai_manager_system/README.md`
  - Goal: Understand universal manager/worker patterns

- [ ] **Read Layer 1 Manager System README** (if you're working at L1)
  - Location: `/home/dawson/code/0_layer_universal/0_context/layer_1_project/1.00_ai_manager_system/README.md`
  - Goal: Understand project-level manager/worker patterns

- [ ] **Read Layer 2 Manager System README** (if you're working at L2)
  - Location: `/home/dawson/code/0_layer_universal/0_context/layer_2_features/2.00_ai_manager_system/README.md`
  - Goal: Understand feature-level manager/worker patterns

- [ ] **Read Layer 3 Manager System README** (if you're working at L3)
  - Location: `/home/dawson/code/0_layer_universal/0_context/layer_3_components/3.00_ai_manager_system/README.md`
  - Goal: Understand component-level manager/worker patterns

### Review Handoff Schema (Must-Have)

**Time**: 15-20 minutes

- [ ] **Read Handoff Schema Definition**
  - Location: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
  - Goal: Understand handoff structure and required fields
  - Key fields: schemaVersion, id, kind, layer, stage, from, to, task, constraints, artifacts, status

- [ ] **Review Handoff Examples**
  - Vertical handoff: L0 manager → L1 manager
  - Horizontal handoff: Planning stage → Development stage
  - Goal: See how handoffs flow through the hierarchy

---

## Adoption Step 1: OS Variant and Tool Specialization

### Select Appropriate OS Variant (Must-Have)

**Time**: 10-15 minutes

- [ ] **Identify your operating system**
  - Options: wsl, linux_ubuntu, windows, macos
  - Check: `echo $OSTYPE` (Linux/macOS) or `$env:OS` (Windows PowerShell)
  - Current system: `__OS_VARIANT_HERE__` (to be filled in by agent)

- [ ] **Locate OS-specific context for your layer**
  - L0: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.99_stages/stage_0_01_instructions/ai_agent_system/os/<os-id>/`
  - L1: `/home/dawson/code/0_layer_universal/0_context/layer_1_project/1.99_stages/stage_1.01_instructions/ai_agent_system/os/<os-id>/`
  - L2: `/home/dawson/code/0_layer_universal/0_context/layer_2_features/2.99_stages/stage_2.01_instructions/ai_agent_system/os/<os-id>/`
  - L3: `/home/dawson/code/0_layer_universal/0_context/layer_3_components/3.99_stages/stage_3.01_instructions/ai_agent_system/os/<os-id>/`

- [ ] **Review OS-specific context files**
  - CLAUDE.md: Manager context (if you're a manager or implementation agent)
  - AGENTS.md: Worker execution context (if you're a short-lived worker)
  - GEMINI.md: Planning context (if you're doing research or long reasoning)

### Choose Tool Specialization Strategy (Nice-to-Have)

**Time**: 10-15 minutes

- [ ] **Decide on tool usage for your project**
  - Claude Code: Managers, deep analysis, complex implementation
  - Codex CLI / Worker Agents: Atomic tasks, code generation
  - Gemini CLI: Research, planning, architecture decisions
  - Mixed: Combine tools based on task complexity

- [ ] **Document tool policy for your project** (optional)
  - Which tool for which tasks?
  - Cost thresholds for tool escalation?
  - Example: Codex for simple tasks (< $0.10), Claude for complex (< $1.00), escalate beyond

---

## Adoption Step 2: Observability and Safety

### Implement Observability Logging (Must-Have)

**Time**: 20-30 minutes

- [ ] **Read Observability Protocol**
  - Location: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/observability/README.md`
  - Goal: Understand log levels, structured logging, log locations

- [ ] **Set up log directory for your project**
  - Recommended: `<project-root>/.ai_context/logs/`
  - Create subdirectories: `managers/`, `workers/`, `handoffs/`

- [ ] **Configure structured logging**
  - Use JSON format for logs
  - Include required fields: timestamp, level, layer, stage, agent_id, message
  - Optional fields: trace_id, span_id, cost, duration

- [ ] **Log key events**
  - Manager spawning workers
  - Handoff creation and acceptance
  - Worker completion and results
  - Errors and warnings

### Configure Safety/Governance Boundaries (Must-Have)

**Time**: 15-20 minutes

- [ ] **Read Safety and Governance Rules**
  - Location: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
  - Goal: Understand permission levels, approval gates, budget limits

- [ ] **Identify your permission level**
  - L0 Manager: System Manager (Level 4) - Full access with approval gates
  - L1 Manager: Project Manager (Level 3) - Project-level access
  - L2 Agent: Standard Agent (Level 2) - Feature-level access
  - L3 Agent: Sandboxed Write (Level 1) - Component directory only

- [ ] **Set budget limits for your project**
  - Recommended: $10-15 per layer (L0: $15, L1: $10, L2: $5, L3: $2)
  - Task limits: L1 tasks max $3, L2 tasks max $1, L3 tasks max $0.25

- [ ] **Define approval gates**
  - What actions require human approval? (delete files, install packages, deploy, budget increases)
  - Who approves? (project owner, supervisor)
  - How? (Slack, email, GitHub comment, CLI prompt)

---

## Adoption Step 3: Deployment Architecture

### Plan Deployment Architecture (Nice-to-Have)

**Time**: 20-30 minutes

- [ ] **Read Deployment Guide**
  - Location: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/deployment/AI_MANAGER_HIERARCHY_DEPLOYMENT.md`
  - Goal: Understand deployment patterns (dev, staging, production)

- [ ] **Select deployment pattern for your project**
  - Pattern 1: Single-Machine Development (local, file-based, SQLite)
  - Pattern 2: Distributed Staging (supervisor cluster, Redis/RabbitMQ, S3)
  - Pattern 3: Production at Scale (5+ supervisors, 10-100+ workers, full observability)

- [ ] **Map layers to services** (if using distributed deployment)
  - L0 Supervisor: API gateway, task queue, manager orchestration
  - L1-L3 Managers: Separate processes/containers
  - L3+ Workers: Auto-scaled worker pool

- [ ] **Define environment-specific configuration**
  - Development: Local setup, minimal logging, no approval gates
  - Staging: Distributed setup, full logging, optional approval gates
  - Production: Full deployment, strict safety rules, mandatory approval gates

---

## Adoption Step 4: Create First Handoff Documents

### Create Project-Level Handoff (Must-Have for L1)

**Time**: 15-25 minutes

- [ ] **Create handoff document directory**
  - Location: `<project-root>/.ai_context/handoffs/`
  - Subdirectories: `incoming/`, `outgoing/`, `archive/`

- [ ] **Create first handoff document** (from L0 to L1, or L1 to L2)
  - Use handoff schema: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
  - Include all required fields: schemaVersion, id, kind, layer, stage, from, to, task, constraints, artifacts, status
  - Example filename: `handoff_L0_to_L1_<project-name>_<timestamp>.json`

- [ ] **Validate handoff document**
  - All required fields present?
  - Task description clear and actionable?
  - Constraints well-defined (budget, time, scope)?
  - Artifacts specified (deliverables, outputs)?

### Set Up Handoff Workflow (Nice-to-Have)

**Time**: 10-15 minutes

- [ ] **Define handoff acceptance criteria**
  - What makes a handoff "accepted"? (manager reads and acknowledges)
  - What triggers "in_progress"? (manager starts work)
  - What triggers "completed"? (artifacts delivered, tests pass)

- [ ] **Create handoff templates** for common flows
  - L0 → L1: Project initialization
  - L1 → L2: Feature request
  - L2 → L3: Component implementation
  - Stage-to-stage: Planning → Development, Development → Testing

---

## Adoption Step 5: Test with Pilot Feature

### Select Pilot Feature (Must-Have for Full Adoption)

**Time**: 5-10 minutes

- [ ] **Choose one feature to implement with hierarchy**
  - Should be: Small enough to complete in 1-2 days, representative of typical work, has clear success criteria
  - Examples: User authentication, CRUD API endpoint, data validation component

- [ ] **Define success criteria for pilot**
  - Feature fully implemented and tested?
  - Handoff documents complete and accurate?
  - Observability logs capture all key events?
  - Safety rules followed (no violations)?
  - Cost within budget?

### Implement Pilot Feature with Hierarchy (Must-Have)

**Time**: 4-8 hours (varies by feature complexity)

- [ ] **Create L1 → L2 handoff** (if implementing a feature)
  - Manager: L1 project manager
  - Worker: L2 feature manager
  - Task: Implement [feature name]

- [ ] **Create L2 → L3 handoffs** (if breaking feature into components)
  - Manager: L2 feature manager
  - Workers: L3 component workers
  - Tasks: Implement individual components

- [ ] **Log all interactions**
  - Manager spawning workers
  - Worker accepting handoffs
  - Worker reporting progress
  - Worker completing tasks

- [ ] **Verify observability**
  - Check logs in `.ai_context/logs/`
  - Verify structured format (JSON)
  - Verify required fields present

- [ ] **Verify safety compliance**
  - No permission violations?
  - All approvals logged?
  - Costs tracked accurately?
  - Budget limits respected?

### Evaluate Pilot Results (Must-Have)

**Time**: 30-45 minutes

- [ ] **Check success criteria**
  - Feature complete? ✓ / ✗
  - Handoffs complete? ✓ / ✗
  - Logs comprehensive? ✓ / ✗
  - Safety compliant? ✓ / ✗
  - Within budget? ✓ / ✗

- [ ] **Document what worked**
  - Which parts of hierarchy were most useful?
  - Which docs were easy to find?
  - Which patterns felt natural?

- [ ] **Document what didn't work**
  - Which parts were confusing?
  - Which docs were hard to find?
  - Which patterns felt awkward or cumbersome?

- [ ] **Identify improvements**
  - Template adjustments needed?
  - Documentation gaps?
  - Process bottlenecks?

---

## Adoption Step 6: Orchestration and CLI Recursion (Nice-to-Have)

### Review Orchestration Options (Nice-to-Have)

**Time**: 15-20 minutes

- [ ] **Read Framework Orchestration Overview** (if using frameworks)
  - Location: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md`
  - Goal: Understand when to use LangGraph, AutoGen, CrewAI, MetaGPT

- [ ] **Decide if framework orchestration is needed**
  - Simple projects: Handoff-based coordination is sufficient
  - Complex projects: Consider LangGraph (deterministic), AutoGen (dialogue), CrewAI (roles)

### Review CLI Recursion Patterns (Nice-to-Have)

**Time**: 15-20 minutes

- [ ] **Read CLI Recursion Syntax** (if implementing deep hierarchies)
  - Location: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md`
  - Goal: Understand how managers spawn workers via CLI

- [ ] **Decide if CLI recursion is needed**
  - Flat projects (L1 only): Not needed
  - Nested projects (L1 → L2 → L3): Consider CLI recursion for manager spawning

- [ ] **Choose recursion approach** (if applicable)
  - Claude Code `--allowed` flags: Good for Claude-to-Claude recursion
  - Handoff-based scripts: Good for mixed tools (Claude → Codex → Gemini)
  - Framework-based: Good for complex parallel orchestration

---

## Post-Adoption: Continuous Improvement

### Contribute Lessons Learned (Nice-to-Have)

**Time**: 15-20 minutes

- [ ] **Document your experience**
  - Location: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/implementation_lessons_learned.md`
  - What worked well?
  - What didn't work as expected?
  - Recommended improvements?

- [ ] **Share patterns you developed**
  - Handoff templates
  - Manager scripts
  - Worker coordination patterns
  - Cost optimization techniques

### Maintain Documentation (Nice-to-Have)

**Time**: Ongoing (5-10 minutes/week)

- [ ] **Keep handoff documents current**
  - Archive completed handoffs
  - Update in-progress handoffs
  - Clean up stale handoffs

- [ ] **Update observability logs**
  - Rotate logs regularly (weekly or monthly)
  - Analyze logs for insights (cost patterns, bottlenecks)
  - Archive old logs

- [ ] **Review and adjust safety rules**
  - Budget limits still appropriate?
  - Approval gates working smoothly?
  - Permission boundaries correct?

---

## Quick Reference: Must-Have vs. Nice-to-Have

### Must-Have (Minimum Viable Adoption)

**Time**: 2-3 hours

1. ✅ Read top-level docs (MASTER_INDEX, SYSTEM_OVERVIEW, USAGE_GUIDE)
2. ✅ Understand layer/stage framework
3. ✅ Read layer manager system README for your layer
4. ✅ Review handoff schema
5. ✅ Select OS variant
6. ✅ Set up observability logging (basic)
7. ✅ Configure safety boundaries (basic)
8. ✅ Create first handoff document
9. ✅ Test with pilot feature

### Nice-to-Have (Full-Featured Adoption)

**Time**: +2-3 hours (4-6 hours total)

1. ✅ Choose tool specialization strategy
2. ✅ Plan deployment architecture
3. ✅ Set up handoff workflow
4. ✅ Review orchestration options
5. ✅ Review CLI recursion patterns
6. ✅ Contribute lessons learned
7. ✅ Maintain documentation over time

---

## Troubleshooting

### Common Issues

**Issue**: "I can't find the right documentation"
- **Solution**: Start with MASTER_DOCUMENTATION_INDEX.md, use search for keywords

**Issue**: "Handoff documents feel too heavy"
- **Solution**: Start with minimal handoffs (just task, from, to, status), add fields as needed

**Issue**: "Observability logging is too verbose"
- **Solution**: Start with INFO level, filter to WARNING+ as project matures

**Issue**: "Safety rules are slowing me down"
- **Solution**: Request permission level increase (L3 → L2, etc.), or use approval gate bypass (dev only)

**Issue**: "I don't know which layer/stage I'm in"
- **Solution**: Ask: "Am I working on entire project (L1), a feature (L2), or a component (L3)?"

**Issue**: "CLI recursion isn't working"
- **Solution**: Check OS-specific examples, verify tool commands are correct, try handoff-based approach instead

---

## Appendix: Checklist for Different Project Types

### Greenfield Project (New from Scratch)

**Focus**: Start with full hierarchy from day 1

- [x] Must-Have items 1-9 (above)
- [x] Create L1 project context
- [x] Set up directory structure (`.ai_context/`, `logs/`, `handoffs/`)
- [x] Define all features as L2 from the start
- [x] Break features into L3 components
- [ ] Optional: Set up CI/CD with hierarchy logging

**Estimated Time**: 3-4 hours initial setup

### Retrofit Existing Project

**Focus**: Map existing work to hierarchy incrementally

- [x] Must-Have items 1-9 (above)
- [x] Assess current project structure
- [x] Map existing features to L2
- [x] Map existing components to L3
- [x] Create handoff documents for past work (optional, archive immediately)
- [x] Start using hierarchy for new work only
- [ ] Gradually migrate existing work to hierarchy patterns

**Estimated Time**: 4-6 hours initial setup + ongoing migration

### Small/Simple Project (< 5 features)

**Focus**: Use L0-L1 without deep nesting

- [x] Must-Have items 1-5 (read docs, select OS)
- [x] Create L1 project context
- [x] Skip L2-L3 (implement features directly at L1)
- [x] Use horizontal handoffs only (stage-to-stage)
- [x] Minimal observability (logs optional)
- [ ] Optional: Upgrade to full hierarchy if project grows

**Estimated Time**: 1-2 hours initial setup

### Large/Complex Project (10+ features)

**Focus**: Full hierarchy with deep nesting

- [x] All Must-Have items 1-9
- [x] All Nice-to-Have items
- [x] Use L0 → L1 → L2 → L3 → L4+ (if needed)
- [x] Implement CLI recursion for manager spawning
- [x] Consider framework orchestration (LangGraph, AutoGen)
- [x] Full observability (distributed tracing, metrics, alerts)
- [x] Strict safety rules (approval gates, budget limits, audit trails)

**Estimated Time**: 6-8 hours initial setup

---

## Next Steps After Adoption

1. **Start Using the Hierarchy**
   - Create handoffs for new work
   - Log all manager/worker interactions
   - Respect safety boundaries

2. **Iterate and Improve**
   - Review logs regularly (weekly)
   - Adjust templates based on experience
   - Contribute lessons learned

3. **Scale Up**
   - Add more features with hierarchy patterns
   - Onboard other agents
   - Refine deployment architecture

4. **Contribute Back**
   - Share patterns and templates
   - Improve documentation
   - Help others adopt the hierarchy

---

## Related Documentation

**Top-Level Docs**:
- MASTER_DOCUMENTATION_INDEX.md: `/home/dawson/code/0_layer_universal/0_context/MASTER_DOCUMENTATION_INDEX.md`
- SYSTEM_OVERVIEW.md: `/home/dawson/code/0_layer_universal/0_context/SYSTEM_OVERVIEW.md`
- USAGE_GUIDE.md: `/home/dawson/code/0_layer_universal/0_context/USAGE_GUIDE.md`

**Framework and Manager Docs**:
- Layer/Stage Framework: `/home/dawson/code/0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md`
- L0 Manager: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.00_ai_manager_system/README.md`
- L1 Manager: `/home/dawson/code/0_layer_universal/0_context/layer_1_project/1.00_ai_manager_system/README.md`
- L2 Manager: `/home/dawson/code/0_layer_universal/0_context/layer_2_features/2.00_ai_manager_system/README.md`
- L3 Manager: `/home/dawson/code/0_layer_universal/0_context/layer_3_components/3.00_ai_manager_system/README.md`

**Handoff and Operational Docs**:
- Handoff Schema: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- Observability: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/observability/README.md`
- Safety Rules: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- Deployment: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/deployment/AI_MANAGER_HIERARCHY_DEPLOYMENT.md`

**Orchestration Docs**:
- Framework Orchestration: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/framework_orchestration/0_instruction_docs/framework_orchestration_overview.md`
- CLI Recursion: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/cli_recursion/0_instruction_docs/cli_recursion_syntax.md`

**Rollout Plan**:
- Rollout Plan: `/home/dawson/.cursor/plans/ai_manager_hierarchy_rollout_plan.md`
- Migration Guide: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/MIGRATION_GUIDE.md` (to be created)
- Quick Start: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/HIERARCHY_QUICK_START.md` (to be created)

---

**Document Status**: Active
**Version**: 1.0
**Last Updated**: 2025-12-24
**Related**: MIGRATION_GUIDE.md, HIERARCHY_QUICK_START.md, ai_manager_hierarchy_rollout_plan.md
