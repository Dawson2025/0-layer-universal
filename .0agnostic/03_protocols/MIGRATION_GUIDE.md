---
resource_id: "41035de6-dc2a-4706-abc4-0db2727e63d4"
resource_type: "protocol"
resource_name: "MIGRATION_GUIDE"
---
# AI Manager Hierarchy - Migration Guide

**Purpose**: Guide for retrofitting existing projects with AI Manager Hierarchy patterns
**Target Audience**: Project managers and agents working on established codebases
**Approach**: Incremental adoption - you can adopt pieces at a time

---

<!-- section_id: "a54baebe-3f46-4189-90f1-302b94e5a21b" -->
## Overview

This guide helps you migrate existing projects to the AI Manager Hierarchy System **without disrupting ongoing work**. The key principle is **incremental adoption**: start with high-value pieces, gradually expand, and always maintain working code.

**When to Use This Guide**:
- You have an existing project with code, features, and components
- You want to adopt hierarchy patterns without rewriting everything
- You want to improve agent coordination on an active project
- You need to retrofit handoff documents for past work

**What You'll Learn**:
- How to assess your current project structure
- How to map existing work to layers/stages
- How to create manager/worker boundaries
- How to retrofit handoff documents
- Common migration patterns
- Incremental migration strategies

---

<!-- section_id: "3426f058-9294-4bd0-92c5-6d122db5a86b" -->
## Migration Philosophy

<!-- section_id: "d882201e-eda1-4a35-ab49-3afc413c4ab6" -->
### Core Principles

1. **Working Code First**: Never break existing functionality to adopt the hierarchy
2. **Incremental Adoption**: Start small, prove value, expand gradually
3. **No Rewriting**: Map existing structure to hierarchy, don't rebuild from scratch
4. **Documentation-Heavy**: Create handoff documents and context, not new code
5. **Opt-In**: Teams can choose which pieces of the hierarchy to adopt

<!-- section_id: "b5490f13-6212-4e5e-ac99-6bbda34c5e60" -->
### Migration Levels

You can adopt the hierarchy at three levels of depth:

**Level 1: Documentation Only** (1-2 hours)
- Create L1 project context
- Document existing features and components
- No code changes, minimal process changes
- Value: Better agent orientation, clearer project structure

**Level 2: Handoff Documents** (3-4 hours)
- Add handoff documents for new work
- Map existing work to layers/stages (retroactively)
- Archive past handoffs for reference
- Value: Better coordination, clearer task boundaries

**Level 3: Full Hierarchy** (6-8 hours)
- Implement manager/worker separation
- Add observability logging
- Configure safety/governance
- Use CLI recursion or framework orchestration
- Value: Full benefits of hierarchy (coordination, safety, observability)

**Recommendation**: Start with Level 1, move to Level 2 for new features, adopt Level 3 only if project complexity warrants it.

---

<!-- section_id: "f4bc0160-84e1-4c4e-8e34-9346859c3d5e" -->
## Step 1: Assess Current Project Structure

<!-- section_id: "ad19154d-dbdb-4eea-ad79-b1f913a49111" -->
### 1.1 Inventory Your Project

**Time**: 30-45 minutes

**Questions to Answer**:

1. **What is the project?**
   - [ ] Name: `____________________`
   - [ ] Description: One-sentence summary
   - [ ] Repository: Path or URL
   - [ ] Status: Active, maintenance, deprecated?

2. **What are the major features?**
   - [ ] List 3-5 main features (e.g., "User Authentication", "Data Export", "Admin Dashboard")
   - [ ] For each feature, estimate: Lines of code, complexity (low/medium/high), active development?

3. **What are the components within features?**
   - [ ] For each feature, list 3-5 components (e.g., "Login Form", "Session Manager", "Password Reset")
   - [ ] For each component, estimate: Files involved, dependencies, complexity

4. **What is the current agent workflow?**
   - [ ] How do agents get tasks? (verbal, ticket system, handoff docs, other)
   - [ ] How do agents coordinate? (ad-hoc, meetings, documents, other)
   - [ ] How are results delivered? (code commits, reports, demos, other)

<!-- section_id: "092fbeea-7076-4172-a3fd-e14b88fa6698" -->
### 1.2 Create Project Assessment Document

**Location**: `<project-root>/.ai_context/project_assessment.md`

**Template**:

```markdown
# Project Assessment: [Project Name]

**Date**: [YYYY-MM-DD]
**Assessor**: [Your name or agent ID]
**Purpose**: Map existing project to AI Manager Hierarchy

## Project Overview

- **Name**: [Project name]
- **Description**: [One-sentence summary]
- **Repository**: [Path or URL]
- **Status**: [Active/Maintenance/Deprecated]
- **Primary Language**: [e.g., Python, JavaScript, Java]
- **Framework**: [e.g., Flask, React, Spring]

## Current Structure

### Features (Layer 2)

1. **Feature Name**
   - Description: [Brief description]
   - Components: [List of L3 components]
   - LOC: [Estimated lines of code]
   - Complexity: [Low/Medium/High]
   - Active: [Yes/No]

2. **Feature Name**
   - ...

### Components (Layer 3)

1. **Component Name** (within [Feature Name])
   - Files: [List of primary files]
   - Dependencies: [Internal and external dependencies]
   - Complexity: [Low/Medium/High]

### Current Agent Workflow

- **Task Assignment**: [How tasks are assigned]
- **Coordination**: [How agents coordinate]
- **Delivery**: [How work is delivered]
- **Pain Points**: [Current challenges]

## Hierarchy Mapping Recommendations

- **Layer 1 (Project)**: [This entire project]
- **Layer 2 (Features)**: [List features to track as L2]
- **Layer 3 (Components)**: [List components to track as L3]

## Migration Strategy

- **Level**: [1, 2, or 3 - see Migration Levels above]
- **Timeline**: [Estimated timeline]
- **Incremental Plan**: [Which features to migrate first]
```

**Deliverable**: Complete project assessment document

---

<!-- section_id: "979fade1-b2a4-41f5-8d62-53af2697ae7b" -->
## Step 2: Map Existing Work to Layers/Stages

<!-- section_id: "41fb57d3-9cd3-4070-be0a-5cb0321e24ed" -->
### 2.1 Understand Layer Mapping

**Layer Definitions**:

- **L0 (Universal)**: Cross-project patterns, tools, protocols (already exists in 0_ai_context)
- **L1 (Project)**: This entire project, project-level setup and coordination
- **L2 (Feature)**: Major features within the project (e.g., "User Authentication")
- **L3 (Component)**: Specific components within features (e.g., "Login Form")
- **L4+ (Sub-component)**: Nested components (rarely needed, only for very complex features)

**Mapping Your Project**:

| If your project has... | Map to... |
|------------------------|-----------|
| A single executable/app | L1 (the whole project) |
| 3-10 major features | L2 (one feature per L2 context) |
| Components within features | L3 (one component per L3 context) |
| Deeply nested modules | L4+ (optional, only if truly necessary) |

<!-- section_id: "cf79a2ce-0aee-49ba-9fb4-0097585560d7" -->
### 2.2 Create Layer Mapping Document

**Location**: `<project-root>/.ai_context/layer_mapping.md`

**Template**:

```markdown
# Layer Mapping: [Project Name]

## L1 (Project): [Project Name]

**Description**: [One-sentence project description]
**Scope**: Entire project
**Manager**: [Who manages the project? Human or L0 agent]
**Workers**: [L2 feature managers]

## L2 (Features)

### Feature: [Feature Name]

- **Description**: [Brief description]
- **Directory**: [Primary directory, e.g., `src/auth/`]
- **Components (L3)**: [List of L3 components within this feature]
- **Manager**: [Who manages this feature? L1 manager or dedicated L2 agent]
- **Workers**: [L3 component workers]
- **Handoffs**: [Where handoffs live for this feature]

### Feature: [Feature Name]

- ...

## L3 (Components)

### Component: [Component Name] (within [Feature Name])

- **Description**: [Brief description]
- **Files**: [List of files, e.g., `src/auth/login_form.py`]
- **Dependencies**: [Internal and external dependencies]
- **Manager**: [L2 feature manager]
- **Worker**: [L3 worker agent or developer]

### Component: [Component Name]

- ...

## Stage Mapping (if applicable)

**Current Work Stage**: [e.g., 0.04_development, 0.05_testing]
**Past Stages**: [e.g., 0.00_request_gathering, 0.01_instructions, 0.02_planning already complete]
**Future Stages**: [e.g., 0.06_delivery coming soon]

## Handoff Flow

**Vertical Handoffs** (Layer-to-layer):
- L0 → L1: [Initial project request or ongoing supervision]
- L1 → L2: [Feature requests]
- L2 → L3: [Component implementation tasks]

**Horizontal Handoffs** (Stage-to-stage):
- Planning → Development
- Development → Testing
- Testing → Delivery
```

**Deliverable**: Complete layer mapping document

---

<!-- section_id: "6c114595-7aba-4b07-b722-8a45eed0acc0" -->
## Step 3: Create Manager/Worker Boundaries

<!-- section_id: "135a7460-9c43-47ea-85bc-c2dce4de3248" -->
### 3.1 Identify Manager and Worker Roles

**Current State**: Likely flat structure (all agents are peers)
**Target State**: Hierarchical structure (managers delegate to workers)

**Manager Characteristics**:
- Reads incoming handoffs
- Plans and delegates work
- Spawns worker agents
- Aggregates worker results
- Writes outgoing handoffs
- Typically long-lived (stays active across multiple tasks)

**Worker Characteristics**:
- Reads incoming handoffs
- Executes specific tasks
- Reports results to manager
- Does not spawn sub-workers (or only L3 → L4 workers)
- Typically short-lived (spawned, executes, exits)

<!-- section_id: "0a773cd0-f429-4dcb-af6a-9beeb5d8428c" -->
### 3.2 Define Boundaries for Your Project

**Questions to Answer**:

1. **Who is the L1 Manager?**
   - [ ] Human project owner
   - [ ] L0 supervisor agent
   - [ ] Dedicated L1 project manager agent
   - [ ] Mixed (human delegates to L1 manager)

2. **Who are the L2 Managers?** (one per feature)
   - [ ] L1 manager handles all features (no L2 separation)
   - [ ] Dedicated L2 agent per feature
   - [ ] Mixed (some features have L2 managers, some don't)

3. **Who are the L3 Workers?** (one per component)
   - [ ] L2 managers handle all components (no L3 separation)
   - [ ] Dedicated L3 worker per component (spawned on-demand)
   - [ ] Mixed (some components use L3 workers, some don't)

4. **What triggers worker spawning?**
   - [ ] Handoff document creation (manager reads handoff, spawns worker)
   - [ ] CLI command (manager runs `claude-code --allowed ...` or `codex run ...`)
   - [ ] Framework orchestration (LangGraph, AutoGen, etc.)

<!-- section_id: "a94ff599-6ac0-4aff-ac7e-774afccceb21" -->
### 3.3 Document Manager/Worker Boundaries

**Location**: `<project-root>/.ai_context/manager_worker_boundaries.md`

**Template**:

```markdown
# Manager/Worker Boundaries: [Project Name]

## L1 (Project) Manager

**Role**: [Human, L0 agent, L1 agent, or mixed]
**Responsibilities**:
- Read L0 → L1 handoffs
- Delegate to L2 feature managers
- Aggregate L2 results
- Write L1 → L0 handoffs (project status)

**Spawning Method**: [Handoff-based, CLI, framework, or manual]

## L2 (Feature) Managers

**Per Feature**: [Yes/No - one manager per feature, or L1 handles all]

**Example: [Feature Name] Manager**
- **Role**: [L1 agent, dedicated L2 agent, or human]
- **Responsibilities**:
  - Read L1 → L2 handoffs for this feature
  - Delegate to L3 component workers
  - Aggregate L3 results
  - Write L2 → L1 handoffs (feature status)
- **Spawning Method**: [Handoff-based, CLI, framework, or manual]

## L3 (Component) Workers

**Per Component**: [Yes/No - one worker per component, or L2 handles all]

**Example: [Component Name] Worker**
- **Role**: [Codex worker, Claude worker, Gemini worker, or human]
- **Responsibilities**:
  - Read L2 → L3 handoffs for this component
  - Implement component
  - Write L3 → L2 handoffs (component completion)
- **Spawning Method**: [CLI command, framework, or manual]
- **Lifecycle**: [Short-lived: spawned, executes, exits]

## Boundary Enforcement

**How are boundaries enforced?**
- [ ] Permission levels (L0 > L1 > L2 > L3 in safety_governance.md)
- [ ] Directory restrictions (L3 workers can only write to component directory)
- [ ] Handoff schema (workers must follow handoff format)
- [ ] Observability logging (all spawning and completion logged)
```

**Deliverable**: Complete manager/worker boundaries document

---

<!-- section_id: "7da4f118-dda9-4ad1-943d-4dd2d3a97d40" -->
## Step 4: Retrofit Handoff Documents

<!-- section_id: "fcc9c373-ae76-49d6-bc3e-59eba8fcf7a8" -->
### 4.1 Understand Handoff Retrofitting

**Purpose**: Create handoff documents for **past work** (already completed) to establish history and context

**When to Retrofit**:
- ✅ When onboarding new agents (they need context on past decisions)
- ✅ When documenting architecture decisions (ADRs)
- ✅ When creating audit trail for compliance
- ❌ When past work is simple and context is obvious
- ❌ When retrofitting overhead exceeds value

**Retrofitting Approach**:
1. Create handoff documents for **major milestones** (initial project, feature launches)
2. Archive handoffs immediately (status: "completed", "archived")
3. Focus on **why** decisions were made, not **what** was done (code is the record of "what")

<!-- section_id: "4ad29d07-639b-4030-afb0-cdb1eee258c8" -->
### 4.2 Create Retrospective Handoffs

**Location**: `<project-root>/.ai_context/handoffs/archive/`

**Template**: Use standard handoff schema with "archived" status

**Example: Retrospective L0 → L1 Handoff** (Initial project request)

```json
{
  "schemaVersion": "1.0",
  "id": "handoff_L0_to_L1_web-app_2024-01-15T10:00:00Z",
  "kind": "vertical",
  "layer": {
    "from": 0,
    "to": 1
  },
  "stage": {
    "from": "0.00_request_gathering",
    "to": "0.01_instructions"
  },
  "from": {
    "agent_id": "human_instructor",
    "role": "project_owner"
  },
  "to": {
    "agent_id": "L1_web-app_manager",
    "role": "project_manager"
  },
  "task": {
    "description": "Create a minimal Flask web application with SQLite database for school project",
    "objectives": [
      "Implement basic CRUD operations",
      "Add user authentication",
      "Deploy to local development server"
    ]
  },
  "constraints": {
    "budget": "$15.00",
    "deadline": "2024-02-01",
    "scope": "Bare minimum functionality for course requirement"
  },
  "artifacts": {
    "deliverables": [
      "Working Flask app (app.py)",
      "SQLite database (data/database.db)",
      "HTML templates (templates/)",
      "Development server script (start_dev.sh)"
    ]
  },
  "status": "completed",
  "archived": true,
  "archived_date": "2024-02-01T14:30:00Z",
  "retrospective": true,
  "notes": "Created retrospectively on 2025-12-24 for migration to AI Manager Hierarchy. Original work completed without hierarchy patterns."
}
```

**Deliverable**: 3-5 retrospective handoff documents for major milestones

<!-- section_id: "7330e0c4-efd4-442a-bfdc-4dca8037f67e" -->
### 4.3 Create Handoff Templates for Future Work

**Location**: `<project-root>/.ai_context/handoffs/templates/`

**Templates to Create**:

1. **L1 → L2 Feature Request Template**
   - Use for new feature requests going forward

2. **L2 → L3 Component Implementation Template**
   - Use for component tasks going forward

3. **Stage-to-Stage Handoff Template**
   - Use for planning → development, development → testing, etc.

**Template Example**: See handoff schema at `/home/dawson/code/0_layer_universal/0_context/layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`

**Deliverable**: 3-5 handoff templates for common workflows

---

<!-- section_id: "c076ea82-6bf1-4a2f-a7b5-0f3a3986a219" -->
## Step 5: Incremental Migration Strategies

<!-- section_id: "cbdb6535-e190-4762-849f-899dcbbe7257" -->
### Strategy 1: New Work First (Recommended)

**Approach**: Keep existing code as-is, use hierarchy for all new work

**Steps**:
1. Create L1 project context (documentation only)
2. Map existing features to L2 (documentation only)
3. **Going forward**: All new features use L2 handoffs and L3 workers
4. **Existing features**: No changes unless refactoring is needed

**Pros**:
- ✅ Zero risk to existing functionality
- ✅ Immediate value for new work
- ✅ Gradual learning curve

**Cons**:
- ❌ Mixed approach (old code without hierarchy, new code with hierarchy)
- ❌ Existing features don't benefit until refactored

**Timeline**: 2-3 hours initial setup, ongoing adoption for new work

---

<!-- section_id: "918334f7-e0a3-4317-8f10-d799eff78906" -->
### Strategy 2: Feature-by-Feature Migration

**Approach**: Migrate one feature at a time to full hierarchy

**Steps**:
1. Select one feature for migration (preferably active development)
2. Create L2 context for that feature
3. Create L3 contexts for components within the feature
4. Retrofit handoff documents for the feature
5. Use hierarchy for all work on that feature going forward
6. Repeat for next feature

**Pros**:
- ✅ Deep adoption for migrated features
- ✅ Focused effort (one feature at a time)
- ✅ Clear success criteria (feature fully migrated)

**Cons**:
- ❌ More effort upfront
- ❌ Mixed approach across features (some migrated, some not)

**Timeline**: 4-6 hours per feature, 2-4 weeks for 3-5 features

---

<!-- section_id: "f8063647-af2e-42f0-95d9-7cc429c64f37" -->
### Strategy 3: Observability and Safety Only

**Approach**: Add observability and safety without full hierarchy

**Steps**:
1. Create L1 project context (minimal)
2. Set up observability logging (`.ai_context/logs/`)
3. Configure safety/governance boundaries
4. Log all agent actions going forward
5. **Optional**: Add handoff documents later

**Pros**:
- ✅ Immediate observability and safety benefits
- ✅ Low adoption overhead
- ✅ Can add handoffs later without rework

**Cons**:
- ❌ Missing coordination benefits (handoffs, manager/worker)
- ❌ Logs are useful but not actionable without hierarchy

**Timeline**: 2-3 hours initial setup

---

<!-- section_id: "fe2e0134-933d-490b-acaf-4c326982df04" -->
### Strategy 4: Documentation-Heavy Migration

**Approach**: Create comprehensive documentation, minimal code/process changes

**Steps**:
1. Create L1 project context (comprehensive)
2. Map all features to L2 (documentation only)
3. Map all components to L3 (documentation only)
4. Retrofit handoff documents for major milestones (archived)
5. **Optional**: Use hierarchy for coordination later

**Pros**:
- ✅ Excellent project orientation for new agents
- ✅ Minimal process disruption
- ✅ Foundation for deeper adoption later

**Cons**:
- ❌ Documentation overhead with limited immediate value
- ❌ Risk of documentation drift if not maintained

**Timeline**: 6-8 hours upfront, low ongoing effort

---

<!-- section_id: "654e0f51-2197-4dfe-8d72-ce9b510f208d" -->
### Strategy 5: Hybrid Adoption

**Approach**: Mix and match hierarchy components based on value

**Steps**:
1. Create L1 project context (always)
2. Use L2 handoffs for complex features (selective)
3. Use L3 workers for well-defined components (selective)
4. Add observability logging (always)
5. Configure safety rules (always)
6. Skip manager/worker separation (optional)
7. Skip CLI recursion or framework orchestration (optional)

**Pros**:
- ✅ Maximum flexibility
- ✅ Adopt only high-value pieces
- ✅ Minimal overhead

**Cons**:
- ❌ Inconsistent patterns (harder to onboard new agents)
- ❌ May miss synergies from full adoption

**Timeline**: 3-5 hours initial setup, ongoing selective adoption

---

<!-- section_id: "ca69909b-1aa7-4494-873f-e7ddff6bff9b" -->
## Common Migration Patterns

<!-- section_id: "216b6b69-0fe2-4149-b1d7-990569fc503d" -->
### Pattern 1: Flat to Hierarchical (L1 → L1+L2+L3)

**Before**:
- All agents work at the same level
- No manager/worker distinction
- Ad-hoc coordination

**After**:
- L1 manager coordinates feature work
- L2 managers coordinate component work
- L3 workers implement components
- Handoffs define task boundaries

**Migration Path**:
1. Designate L1 manager (human or agent)
2. Create L2 contexts for features
3. Start using L2 handoffs for new features
4. Gradually add L3 workers for components

---

<!-- section_id: "0f54bcaa-6a82-4b59-868a-c9524f17b3a3" -->
### Pattern 2: Monolithic to Modular (Single file → L2+L3 breakdown)

**Before**:
- One large file with multiple features
- No clear boundaries between features/components

**After**:
- Features separated into modules (L2)
- Components separated into files (L3)
- Handoffs define module interfaces

**Migration Path**:
1. Identify features in monolithic code
2. Create L2 contexts for each feature
3. Refactor code into modules (feature by feature)
4. Create L3 contexts for components within modules

---

<!-- section_id: "4cced3f2-c854-45cc-aecb-8feb403ae273" -->
### Pattern 3: Siloed to Coordinated (Isolated agents → Manager/Worker coordination)

**Before**:
- Agents work in isolation
- Duplicate work or conflicting changes
- Poor visibility into who's doing what

**After**:
- Managers coordinate agents
- Handoffs define task ownership
- Observability logs show all activity

**Migration Path**:
1. Designate managers for each layer
2. Require handoff documents for all tasks
3. Log all manager/worker interactions
4. Review logs regularly to optimize coordination

---

<!-- section_id: "22b9182b-d040-48a7-9554-284f48f715e7" -->
## Migration Checklist

<!-- section_id: "ca72fa60-fa0d-493f-bb78-80fce63b2c6d" -->
### Pre-Migration

- [ ] Read this migration guide completely
- [ ] Review HIERARCHY_ADOPTION_CHECKLIST.md
- [ ] Choose migration strategy (1-5 above)
- [ ] Get stakeholder buy-in (if applicable)

<!-- section_id: "f6da591d-73b8-4e81-81c5-41837bf39ba4" -->
### Phase 1: Assessment (Day 1)

- [ ] Create project assessment document
- [ ] Create layer mapping document
- [ ] Create manager/worker boundaries document
- [ ] Review with team (if applicable)

<!-- section_id: "cb64ca57-0ca2-46c5-9cde-881aee0f66b2" -->
### Phase 2: Setup (Day 2-3)

- [ ] Create `.ai_context/` directory structure
  - [ ] `logs/` (observability)
  - [ ] `handoffs/incoming/`, `handoffs/outgoing/`, `handoffs/archive/`
  - [ ] `templates/` (handoff templates)
- [ ] Create L1 project context
- [ ] Set up observability logging (basic)
- [ ] Configure safety/governance boundaries
- [ ] Create handoff templates

<!-- section_id: "5a040f9f-7252-4d15-9155-c2e1e9fe2c36" -->
### Phase 3: Retrospective Documentation (Day 4-5, optional)

- [ ] Create 3-5 retrospective handoff documents for major milestones
- [ ] Archive retrospective handoffs
- [ ] Document architecture decisions (if applicable)

<!-- section_id: "a12c2c48-c178-4a94-b2e1-0b23204b2545" -->
### Phase 4: New Work Adoption (Ongoing)

- [ ] Use handoff documents for all new features
- [ ] Log all manager/worker interactions
- [ ] Review logs weekly
- [ ] Iterate on templates based on experience

<!-- section_id: "d921f18d-c31b-4822-8cfc-f0b9835d59fb" -->
### Phase 5: Gradual Expansion (Weeks 2-4)

- [ ] Migrate one existing feature to hierarchy (if using Strategy 2)
- [ ] Add L3 workers for complex components
- [ ] Refine manager/worker boundaries
- [ ] Contribute lessons learned

---

<!-- section_id: "382577b3-4174-4b0d-b2e2-45ffeb3e6221" -->
## Troubleshooting Migration Issues

<!-- section_id: "a64db70e-be75-40d8-b6d0-9f6af2ff185d" -->
### Issue: "Too much documentation overhead"

**Symptoms**: Handoff creation takes longer than actual work
**Solutions**:
- Start with minimal handoffs (just task, from, to, status)
- Use templates to reduce repetition
- Only create handoffs for complex tasks (skip trivial tasks)
- Consider Strategy 3 (observability only) or Strategy 5 (hybrid)

---

<!-- section_id: "861794d0-6ead-4d5a-9abf-629f17ba8c64" -->
### Issue: "Existing code doesn't fit layer model"

**Symptoms**: Features and components don't map cleanly to L2/L3
**Solutions**:
- Use L1 only (skip L2/L3 if project is simple)
- Group related code into logical features (even if files are mixed)
- Accept imperfect mapping (documentation is approximate, not exact)
- Refactor incrementally (one feature at a time)

---

<!-- section_id: "f37d75d8-7d8f-4c50-81f8-a9acb65d91e8" -->
### Issue: "Agents aren't using hierarchy patterns"

**Symptoms**: Handoffs not created, logs not written, boundaries not respected
**Solutions**:
- Make hierarchy patterns explicit in task instructions
- Link to HIERARCHY_ADOPTION_CHECKLIST.md in task descriptions
- Review and approve handoffs before work starts
- Use observability logs to identify non-compliance
- Provide training and examples

---

<!-- section_id: "cd85d3f3-1867-49fd-9f5a-68b21cbb48fa" -->
### Issue: "Migration stalled after initial setup"

**Symptoms**: L1 context created, but no ongoing adoption
**Solutions**:
- Choose simpler strategy (e.g., Strategy 1 instead of Strategy 2)
- Focus on one high-value piece (e.g., just observability)
- Set weekly review cadence to reinforce adoption
- Celebrate small wins (first handoff, first migrated feature)

---

<!-- section_id: "90744216-642d-4a21-a57b-eb17de5fb90c" -->
### Issue: "Hierarchy feels too rigid for our workflow"

**Symptoms**: Handoffs slow down fast-moving work
**Solutions**:
- Use Strategy 5 (hybrid adoption) - adopt only useful pieces
- Simplify handoff templates (remove non-essential fields)
- Use horizontal handoffs only (stage-to-stage, skip layer-to-layer)
- Accept that hierarchy may not fit all projects (opt-out is OK)

---

<!-- section_id: "9f4858bf-9b3b-4a46-b343-24044ef104fc" -->
## Success Metrics for Migration

| Metric | Measurement | Target |
|--------|-------------|--------|
| **Setup Time** | Hours to complete Phase 1-2 | < 8 hours |
| **Handoff Adoption** | % of new features using handoffs | > 70% |
| **Observability** | % of agent actions logged | > 80% |
| **Safety Compliance** | Permission violations | 0 |
| **Agent Satisfaction** | Survey or subjective rating | ≥ 6/10 |
| **Documentation Drift** | Weeks since last update | < 2 weeks |

---

<!-- section_id: "f1a9420f-4974-4e3e-a682-3b932d2a9e97" -->
## Next Steps After Migration

1. **Use the hierarchy** for all new work
2. **Review logs** weekly to identify patterns and improvements
3. **Iterate on templates** based on real usage
4. **Contribute lessons learned** to `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/implementation_lessons_learned.md`
5. **Onboard new agents** using HIERARCHY_ADOPTION_CHECKLIST.md
6. **Expand adoption** to more features or deeper layers (L3, L4+)

---

<!-- section_id: "e50a5cfc-aa28-46ff-aa23-6567459a1255" -->
## Related Documentation

**Adoption and Rollout**:
- Rollout Plan: `/home/dawson/.cursor/plans/ai_manager_hierarchy_rollout_plan.md`
- Adoption Checklist: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/HIERARCHY_ADOPTION_CHECKLIST.md`
- Quick Start: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/HIERARCHY_QUICK_START.md` (to be created)

**Core Hierarchy Docs**:
- MASTER_DOCUMENTATION_INDEX: `/home/dawson/code/0_layer_universal/0_context/MASTER_DOCUMENTATION_INDEX.md`
- SYSTEM_OVERVIEW: `/home/dawson/code/0_layer_universal/0_context/SYSTEM_OVERVIEW.md`
- USAGE_GUIDE: `/home/dawson/code/0_layer_universal/0_context/USAGE_GUIDE.md`
- Layer/Stage Framework: `/home/dawson/code/0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md`

**Handoff and Manager Docs**:
- Handoff Schema: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.01_manager_handoff_documents/0.00_to_universal/handoff_schema.md`
- L0 Manager: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.00_ai_manager_system/README.md`
- L1 Manager: `/home/dawson/code/0_layer_universal/0_context/layer_1_project/1.00_ai_manager_system/README.md`
- L2 Manager: `/home/dawson/code/0_layer_universal/0_context/layer_2_features/2.00_ai_manager_system/README.md`
- L3 Manager: `/home/dawson/code/0_layer_universal/0_context/layer_3_components/3.00_ai_manager_system/README.md`

**Operational Docs**:
- Observability: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_13_universal_protocols/observability/README.md`
- Safety Rules: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_04_universal_rules/safety_governance.md`
- Deployment: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/deployment/AI_MANAGER_HIERARCHY_DEPLOYMENT.md`

---

**Document Status**: Active
**Version**: 1.0
**Last Updated**: 2025-12-24
**Related**: HIERARCHY_ADOPTION_CHECKLIST.md, HIERARCHY_QUICK_START.md, ai_manager_hierarchy_rollout_plan.md
