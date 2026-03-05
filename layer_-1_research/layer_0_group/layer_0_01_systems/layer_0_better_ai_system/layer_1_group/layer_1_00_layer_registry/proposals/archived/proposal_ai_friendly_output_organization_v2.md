---
resource_id: "bb779700-0e20-448a-856f-7125d56930a1"
resource_type: "document"
resource_name: "proposal_ai_friendly_output_organization_v2"
---
# Proposal v2: AI-Agent-Friendly Organization Using Layer-Stage Hierarchy

**Date**: 2026-02-02
**Version**: 2.0
**Status**: ⚠️ SUPERSEDED by v3
**Superseded By**: `proposal_ai_friendly_output_organization_v3.md`
**Reason**: v3 adds complete agnostic system, three-tier architecture, sync script, tool-specific configs
**Previous Version**: `proposal_ai_friendly_output_organization.md` (v1)

---

> **Note**: This proposal has been superseded. See v3 for the complete architecture including:
> - 0AGNOSTIC.md as source of truth
> - Three-tier folder architecture (.0agnostic/ → .1*_merge/ → native output)
> - Tool-specific configurations (Claude, Cursor, Copilot, Gemini, Aider)
> - Sync system (agnostic-sync.sh)
> - Episodic memory in correct location

---

**Supersedes**: v1 (which organized within stage outputs only)

---

<!-- section_id: "17f37032-2c12-460d-9cca-eb0f9b2ef8d9" -->
## Change from v1

| Aspect | v1 | v2 |
|--------|----|----|
| **Organization** | Nested folders within `stage_-1_02_research/outputs/by_topic/` | Use existing layer-stage hierarchy with features |
| **Location** | All in one place | Distributed to features + cross-cutting at project level |
| **Entry Points** | New CLAUDE.md in each by_topic folder | Leverage existing feature CLAUDE.md files |
| **Dogfooding** | Parallel structure | Uses the system we're designing |

---

<!-- section_id: "b1629056-fdb0-49d4-8900-a026f5346544" -->
## Problem Statement

<!-- section_id: "11ab9fc3-51d5-4a1e-a336-439339fb706d" -->
### Current Issues

1. **Research is lumped together** - All topics in one `by_topic/` folder
2. **Disconnected from features** - Research doesn't live with the feature it informs
3. **Not using our own system** - We're designing a layer-stage system but not using it
4. **AI agents struggle** - No clear entry points, discovery, or contribution guidelines

<!-- section_id: "bac8c91c-1995-44c6-8586-8e4e88dcac34" -->
### What AI Agents Need

| Need | Solution |
|------|----------|
| Know their role | `CLAUDE.md` at each level |
| Discover content | `0INDEX.md` at each level |
| Get overview | `synthesis/` folder at each level |
| Know when to load | Triggers in CLAUDE.md |
| Know where to contribute | Contribution guidelines |
| See relationships | Cross-reference maps |
| Track progress | Status indicators |

---

<!-- section_id: "9a24e92a-9212-496c-8a86-84d3d539a238" -->
## Proposed Solution

<!-- section_id: "3e0c502e-d49a-44b9-910a-eb7f4b6bfb84" -->
### Core Idea

**Organize research into the layer-stage hierarchy using features**, with AI-agent-friendly enhancements at every level.

```
layer_-1_better_ai_system/           # Research project
├── layer_-1_group/                        # Project-level (cross-cutting)
│   └── stages/                      # Project stages
│       └── stage_02_research/       # Cross-feature research
│
└── layer_0_group/                         # Feature level
    └── layer_0_features/
        ├── layer_0_feature_ai_dynamic_memory_system/
        ├── layer_0_feature_ai_context_system/
        ├── layer_0_feature_ai_manager_hierarchy_system/
        ├── layer_0_feature_better_layer_stage_system/
        └── layer_0_feature_ai_automation_system/
```

---

<!-- section_id: "0d120d53-6369-43f7-b24b-b429b26d526a" -->
## AI-Agent-Friendly Enhancements

<!-- section_id: "7cd8fea4-7114-437e-9191-651f2554d2c5" -->
### 1. CLAUDE.md at Every Level

Every folder that an agent might enter gets a `CLAUDE.md`:

```markdown
# CLAUDE.md - [Entity Name]

## Identity
You are a [role] agent working on [scope].

## Scope
- Topic 1
- Topic 2

## Triggers: When to Load This Context
- When user asks about [keywords]
- When working on [related tasks]

## On Entry
1. Read `0INDEX.md` to see current state
2. Read `synthesis/` for overview
3. Check status of sub-entities

## Where to Contribute
| Type of Work | Location |
|--------------|----------|
| [work type] | [location] |

## Navigation
- **Parent**: [link]
- **Children**: [links]
- **Related**: [links to related features]
```

<!-- section_id: "2b0a909a-2391-44e3-bc6b-68014dcef771" -->
### 2. 0INDEX.md at Every Level

Every folder gets a `0INDEX.md` for discovery:

```markdown
# Index: [Entity Name]

## Contents

| Item | Type | Status | Description |
|------|------|--------|-------------|
| `item` | file/folder | ✅/⚠️/🔄/❌ | Description |

## Status Legend
- ✅ Complete - Ready for next stage
- ⚠️ Partial - Has content, needs work
- 🔄 In Progress - Actively being worked on
- ❌ Empty - Placeholder only

## Cross-References

| This Topic | Relates To | Why |
|------------|------------|-----|
| [topic] | [related] | [reason] |

## Open Questions
- [ ] Question 1

## Stage Progress
| Stage | Status |
|-------|--------|
| 01 Request Gathering | ✅ |
| 02 Research | 🔄 |
| 03 Instructions | ❌ |
| ... | ... |

## Last Updated
[Date] by [session/agent]
```

<!-- section_id: "b717885a-470c-4017-9889-d1b070735415" -->
### 3. synthesis/ Folder at Every Level

Every significant folder gets a `synthesis/` subfolder:

```
feature/
├── synthesis/
│   └── feature_synthesis.md
├── layer_0_group/
│   └── layer_0_99_stages/
│       └── stage_0_02_research/
│           ├── synthesis/
│           │   └── research_synthesis.md
│           └── outputs/
│               └── synthesis/
│                   └── outputs_synthesis.md
```

<!-- section_id: "59b6ae8f-68d1-4125-96dc-1b475eaad126" -->
### 4. Cross-Reference Maps

At project level and feature level:

```markdown
# Cross-Reference Map

## Feature Relationships

| Feature | Depends On | Feeds Into |
|---------|------------|------------|
| Memory System | - | Context System |
| Context System | Memory | Automation |
| Manager Hierarchy | - | Context System |
| Layer-Stage System | - | All features |
| Automation | Context, Layer-Stage | - |

## Research Topic → Feature Mapping

| Research Topic | Primary Feature | Related Features |
|----------------|-----------------|------------------|
| Agent amnesia | Context System | Memory System |
| Tool configs | Context System | Automation |
| Multi-agent sync | Manager Hierarchy | Memory System |
```

<!-- section_id: "9a132749-ea22-4bfe-963f-0f779cfc6518" -->
### 5. Contribution Templates

At project level, templates for new research:

```markdown
# Research: [Topic]

**Date**: YYYY-MM-DD
**Feature**: [which feature this belongs to]
**Status**: Draft | In Progress | Complete
**Related**: [links to related files]

---

## Question
What we're trying to answer.

## Findings
What we learned.

## Sources
- [Source](url)

## Implications for [Feature]
How this affects the feature design.

## Open Questions
- Question 1
```

---

<!-- section_id: "8af08e93-25b3-4ae8-aa38-d7d179682916" -->
## Full Proposed Structure

```
layer_-1_better_ai_system/
├── CLAUDE.md                              # Project entry point (enhanced)
├── 0INDEX.md                              # Project discovery (NEW)
├── _crossref.md                           # Feature relationships (NEW)
├── _templates/                            # Contribution templates (NEW)
│   ├── research_template.md
│   ├── feature_template.md
│   └── component_template.md
│
├── layer_-1_group/                              # PROJECT-LEVEL
│   ├── CLAUDE.md                          # Layer entry (enhanced)
│   ├── 0INDEX.md                          # Layer discovery (NEW)
│   └── layer_-1_99_stages/
│       ├── CLAUDE.md                      # Stages manager (enhanced)
│       ├── 0INDEX.md                      # Stages discovery (NEW)
│       │
│       └── stage_-1_02_research/
│           ├── CLAUDE.md                  # Stage entry (enhanced)
│           ├── 0INDEX.md                  # Stage discovery (NEW)
│           └── outputs/
│               ├── CLAUDE.md              # Outputs entry (NEW)
│               ├── 0INDEX.md              # Outputs discovery (NEW)
│               ├── synthesis/
│               │   └── project_research_synthesis.md
│               │
│               ├── cross_cutting/         # Research spanning features
│               │   ├── CLAUDE.md
│               │   ├── 0INDEX.md
│               │   ├── synthesis/
│               │   │   └── cross_cutting_synthesis.md
│               │   │
│               │   └── external_frameworks/
│               │       ├── CLAUDE.md
│               │       ├── 0INDEX.md
│               │       ├── synthesis/
│               │       ├── existing_solutions.md
│               │       ├── shimi_framework_research.md
│               │       ├── shimi_sync_mechanisms_explained.md
│               │       ├── system_comparison_and_recommendations.md
│               │       ├── why_not_use_existing_frameworks.md
│               │       └── can_custom_system_outperform_frameworks.md
│               │
│               ├── proposals/             # Proposals (like this one)
│               │   ├── CLAUDE.md
│               │   ├── 0INDEX.md
│               │   └── [proposal files]
│               │
│               └── episodic/              # Session tracking
│                   ├── index.md
│                   ├── sessions/
│                   └── changes/
│
└── layer_0_group/
    ├── CLAUDE.md                          # Layer 0 entry (enhanced)
    ├── 0INDEX.md                          # Layer 0 discovery (NEW)
    │
    └── layer_0_features/
        ├── CLAUDE.md                      # Features manager (enhanced)
        ├── 0INDEX.md                      # Features discovery (NEW)
        ├── _crossref.md                   # Feature relationships (NEW)
        │
        │
        ├── layer_0_feature_ai_dynamic_memory_system/
        │   ├── CLAUDE.md                  # ENHANCED with triggers
        │   ├── 0INDEX.md                  # NEW
        │   ├── synthesis/
        │   │   └── memory_system_synthesis.md
        │   └── layer_0_group/
        │       └── layer_0_99_stages/
        │           └── stage_0_02_research/
        │               ├── CLAUDE.md
        │               ├── 0INDEX.md
        │               └── outputs/
        │                   ├── CLAUDE.md
        │                   ├── 0INDEX.md
        │                   ├── synthesis/
        │                   │   └── memory_research_synthesis.md
        │                   ├── agnostic_memory_system_research.md
        │                   ├── memory_systems.md
        │                   ├── claude_code_memory_gap_analysis.md
        │                   ├── why_claude_code_lacks_memory_research.md
        │                   ├── anthropic_memory_tool_api_research.md
        │                   └── memory_system_recommendation.md
        │
        │
        ├── layer_0_feature_ai_context_system/
        │   ├── CLAUDE.md                  # ENHANCED
        │   ├── 0INDEX.md                  # NEW
        │   ├── synthesis/
        │   │   └── context_system_synthesis.md
        │   └── layer_0_group/
        │       └── layer_0_99_stages/
        │           └── stage_0_02_research/
        │               ├── CLAUDE.md
        │               ├── 0INDEX.md
        │               └── outputs/
        │                   ├── CLAUDE.md
        │                   ├── 0INDEX.md
        │                   ├── synthesis/
        │                   │   └── context_research_synthesis.md
        │                   ├── agent_amnesia_and_context_systems.md
        │                   ├── tool_context_systems.md
        │                   ├── tool_rankings.md
        │                   ├── ai_context_filesystem_locations.md
        │                   ├── agnostic_sync_system_design.md
        │                   ├── agnostic_mapping.md
        │                   └── system_prompt_architecture.md  # APPROVED
        │
        │
        ├── layer_0_feature_ai_manager_hierarchy_system/
        │   ├── CLAUDE.md                  # ENHANCED
        │   ├── 0INDEX.md                  # NEW
        │   ├── synthesis/
        │   │   └── manager_system_synthesis.md
        │   └── layer_0_group/
        │       └── layer_0_99_stages/
        │           └── stage_0_02_research/
        │               ├── CLAUDE.md
        │               ├── 0INDEX.md
        │               └── outputs/
        │                   ├── CLAUDE.md
        │                   ├── 0INDEX.md
        │                   ├── synthesis/
        │                   │   └── manager_research_synthesis.md
        │                   ├── is_your_system_multi_agent.md
        │                   ├── multi_agent_parallel_execution_insight.md
        │                   └── updated_understanding_system_scale.md
        │
        │
        ├── layer_0_feature_better_layer_stage_system/
        │   ├── CLAUDE.md                  # ENHANCED
        │   ├── 0INDEX.md                  # NEW
        │   ├── synthesis/
        │   │   └── layer_stage_synthesis.md
        │   └── layer_0_group/
        │       └── layer_0_99_stages/
        │           └── stage_0_02_research/
        │               ├── CLAUDE.md
        │               ├── 0INDEX.md
        │               └── outputs/
        │                   ├── CLAUDE.md
        │                   ├── 0INDEX.md
        │                   ├── synthesis/
        │                   │   └── layer_stage_research_synthesis.md
        │                   ├── layer_stage_instantiation.md
        │                   ├── system_context_hierarchy_research.md
        │                   ├── hierarchical_needs_tree_patterns.md
        │                   └── rule_propagation_problem.md
        │
        │
        └── layer_0_feature_ai_automation_system/
            ├── CLAUDE.md                  # ENHANCED
            ├── 0INDEX.md                  # NEW
            ├── synthesis/
            │   └── automation_synthesis.md
            └── layer_0_group/
                └── layer_0_99_stages/
                    └── stage_0_02_research/
                        ├── CLAUDE.md
                        ├── 0INDEX.md
                        └── outputs/
                            ├── CLAUDE.md
                            ├── 0INDEX.md
                            ├── synthesis/
                            │   └── automation_research_synthesis.md
                            └── automated_traversal_for_your_system.md
```

---

<!-- section_id: "dd5ca5c6-b74b-4fd1-b6f1-6c6a359fb009" -->
## File Distribution

<!-- section_id: "8bb94166-12b6-457c-aca4-08c66e205b3a" -->
### Research Files → Features

| Current File | → Feature | Location in Feature |
|--------------|-----------|---------------------|
| `agnostic_memory_system_research.md` | `ai_dynamic_memory_system` | `stage_0_02_research/outputs/` |
| `memory_systems.md` | `ai_dynamic_memory_system` | `stage_0_02_research/outputs/` |
| `claude_code_memory_gap_analysis.md` | `ai_dynamic_memory_system` | `stage_0_02_research/outputs/` |
| `why_claude_code_lacks_memory_research.md` | `ai_dynamic_memory_system` | `stage_0_02_research/outputs/` |
| `anthropic_memory_tool_api_research.md` | `ai_dynamic_memory_system` | `stage_0_02_research/outputs/` |
| `memory_system_recommendation.md` | `ai_dynamic_memory_system` | `stage_0_02_research/outputs/` |
| `agent_amnesia_and_context_systems.md` | `ai_context_system` | `stage_0_02_research/outputs/` |
| `ai_context_filesystem_locations.md` | `ai_context_system` | `stage_0_02_research/outputs/` |
| `agnostic_sync_system_design.md` | `ai_context_system` | `stage_0_02_research/outputs/` |
| `system_prompt_architecture.md` | `ai_context_system` | → Move to `stage_0_03_instructions/` |
| `is_your_system_multi_agent.md` | `ai_manager_hierarchy_system` | `stage_0_02_research/outputs/` |
| `multi_agent_parallel_execution_insight.md` | `ai_manager_hierarchy_system` | `stage_0_02_research/outputs/` |
| `updated_understanding_system_scale.md` | `ai_manager_hierarchy_system` | `stage_0_02_research/outputs/` |
| `system_context_hierarchy_research.md` | `better_layer_stage_system` | `stage_0_02_research/outputs/` |
| `hierarchical_needs_tree_patterns.md` | `better_layer_stage_system` | `stage_0_02_research/outputs/` |
| `rule_propagation_problem.md` | `better_layer_stage_system` | `stage_0_02_research/outputs/` |
| `automated_traversal_for_your_system.md` | `ai_automation_system` | `stage_0_02_research/outputs/` |

<!-- section_id: "5b9ab32a-7c89-4168-8731-83e69167fa7f" -->
### Large File Split

`layer_stage_instantiation_understanding.md` (2300+ lines) splits into:

| New File | → Feature | Content |
|----------|-----------|---------|
| `tool_context_systems.md` | `ai_context_system` | Tool configs (~500 lines) |
| `tool_rankings.md` | `ai_context_system` | Rankings (~300 lines) |
| `agnostic_mapping.md` | `ai_context_system` | Mapping (~130 lines) |
| `layer_stage_instantiation.md` | `better_layer_stage_system` | Core patterns (~1400 lines) |

<!-- section_id: "eb4cb4a6-b149-4c23-a5aa-4e9440f967ae" -->
### Cross-Cutting Research (Stays at Project Level)

| File | Location | Reason |
|------|----------|--------|
| `existing_solutions.md` | `layer_-1_group/.../cross_cutting/external_frameworks/` | Spans all features |
| `shimi_framework_research.md` | `layer_-1_group/.../cross_cutting/external_frameworks/` | Spans all features |
| `shimi_sync_mechanisms_explained.md` | `layer_-1_group/.../cross_cutting/external_frameworks/` | Spans all features |
| `system_comparison_and_recommendations.md` | `layer_-1_group/.../cross_cutting/external_frameworks/` | Spans all features |
| `why_not_use_existing_frameworks.md` | `layer_-1_group/.../cross_cutting/external_frameworks/` | Spans all features |
| `can_custom_system_outperform_frameworks.md` | `layer_-1_group/.../cross_cutting/external_frameworks/` | Spans all features |

<!-- section_id: "281c87b5-89f6-4b82-809f-e36998660d4c" -->
### Proposals (New Location)

| File | Location |
|------|----------|
| `proposal_ai_friendly_output_organization.md` | `layer_-1_group/.../outputs/proposals/` |
| `proposal_ai_friendly_output_organization_v2.md` | `layer_-1_group/.../outputs/proposals/` |

---

<!-- section_id: "c2c89c0e-b440-44e4-b3ea-1b4bfe5ccced" -->
## CLAUDE.md Templates

<!-- section_id: "b842ca8b-0d82-4ac2-9aff-5edae7ddcc02" -->
### Project-Level CLAUDE.md

```markdown
# CLAUDE.md - better_ai_system (Research Project)

## Identity
You are a research agent working on the **better_ai_system** project.
This project researches improvements to AI system architecture.

## Scope
- Memory systems and session continuity
- Context systems and tool portability
- Manager hierarchy and multi-agent coordination
- Layer-stage framework improvements
- Automation and tooling

## Triggers: When to Load This Context
- Starting work on any AI system improvement
- Researching AI coding tool patterns
- Designing agent-friendly structures

## On Entry
1. Read `0INDEX.md` for project overview
2. Check `_crossref.md` for feature relationships
3. Identify which feature your task relates to
4. Navigate to that feature's CLAUDE.md

## Features (Navigate to One)

| Feature | Focus | Entry Point |
|---------|-------|-------------|
| `ai_dynamic_memory_system` | Memory, persistence, episodic | `layer_0_group/layer_0_features/.../CLAUDE.md` |
| `ai_context_system` | Context, tools, agnostic design | `layer_0_group/layer_0_features/.../CLAUDE.md` |
| `ai_manager_hierarchy_system` | Multi-agent, coordination | `layer_0_group/layer_0_features/.../CLAUDE.md` |
| `better_layer_stage_system` | Framework, hierarchy, patterns | `layer_0_group/layer_0_features/.../CLAUDE.md` |
| `ai_automation_system` | Tooling, validation, discovery | `layer_0_group/layer_0_features/.../CLAUDE.md` |

## Cross-Cutting Research
For research spanning multiple features:
`layer_-1_group/layer_-1_99_stages/stage_-1_02_research/outputs/cross_cutting/`

## Where to Contribute

| Type of Work | Location |
|--------------|----------|
| Feature-specific research | That feature's `stage_02_research/outputs/` |
| Cross-feature research | `layer_-1_group/.../cross_cutting/` |
| New proposals | `layer_-1_group/.../proposals/` |
| Session logs | `layer_-1_group/.../episodic/sessions/` |
```

<!-- section_id: "67d686c4-6212-4fd8-a096-0f3f26c7f069" -->
### Feature-Level CLAUDE.md

```markdown
# CLAUDE.md - AI Context System Feature

## Identity
You are a research/development agent working on the **AI Context System** feature.

## Scope
- Agent amnesia problem and solutions
- Tool context configurations (Claude, Cursor, Copilot, etc.)
- AGNOSTIC.md design and sync system
- System prompt architecture
- Tool rankings and recommendations

## Triggers: When to Load This Context
- User mentions "context", "CLAUDE.md", "agnostic"
- Working on tool portability
- Designing system prompts
- Comparing AI coding tools

## On Entry
1. Read `0INDEX.md` for feature status
2. Read `synthesis/context_system_synthesis.md` for overview
3. Check current stage progress
4. Navigate to relevant stage

## Stage Status

| Stage | Status | Notes |
|-------|--------|-------|
| 01 Request Gathering | ✅ Complete | Requirements defined |
| 02 Research | 🔄 In Progress | Active research |
| 03 Instructions | ⚠️ Partial | `system_prompt_architecture.md` ready |
| 04 Design | ❌ Not Started | - |
| 05+ | ❌ Not Started | - |

## Key Research Files
- `agent_amnesia_and_context_systems.md` - Core problem/solution
- `tool_context_systems.md` - Tool configurations
- `system_prompt_architecture.md` - **APPROVED** - Ready for Stage 03

## Where to Contribute

| Type of Work | Location |
|--------------|----------|
| New research | `layer_0_group/layer_0_99_stages/stage_0_02_research/outputs/` |
| Instructions | `layer_0_group/layer_0_99_stages/stage_0_03_instructions/` |
| Designs | `layer_0_group/layer_0_99_stages/stage_0_04_design/` |

## Related Features
- `ai_dynamic_memory_system` - Memory solves part of context problem
- `ai_automation_system` - Automated context gathering
- `better_layer_stage_system` - Framework for context hierarchy
```

---

<!-- section_id: "20aa5fc8-0812-4b8e-bf4d-9b85adab7848" -->
## 0INDEX.md Templates

<!-- section_id: "84846756-8d3e-47a4-9e32-f5ea113046de" -->
### Project-Level 0INDEX.md

```markdown
# Index: better_ai_system Research Project

## Project Overview
Research project exploring improvements to AI system architecture.

## Contents

| Item | Type | Status | Description |
|------|------|--------|-------------|
| `layer_-1_group/` | folder | 🔄 Active | Project-level stages |
| `layer_0_group/` | folder | 🔄 Active | Features and components |
| `CLAUDE.md` | file | ✅ | Project entry point |
| `_crossref.md` | file | ✅ | Feature relationships |
| `_templates/` | folder | ✅ | Contribution templates |

## Features Status

| Feature | Research | Instructions | Design | Development |
|---------|----------|--------------|--------|-------------|
| `ai_dynamic_memory_system` | 🔄 80% | ❌ | ❌ | ❌ |
| `ai_context_system` | 🔄 70% | ⚠️ 10% | ❌ | ❌ |
| `ai_manager_hierarchy_system` | 🔄 60% | ❌ | ❌ | ❌ |
| `better_layer_stage_system` | 🔄 50% | ❌ | ❌ | ❌ |
| `ai_automation_system` | ⚠️ 20% | ❌ | ❌ | ❌ |

## Pending Decisions
- [ ] Approve `proposal_ai_friendly_output_organization_v2.md`
- [ ] Move `system_prompt_architecture.md` to Stage 03

## Last Updated
2026-02-02 by synthesis session
```

---

<!-- section_id: "fc4c7c31-20f9-4ec2-b355-98aab645392c" -->
## Registry Updates Required

<!-- section_id: "6baf433a-0f39-445d-87bb-343bd37cddf6" -->
### 1. Stage Registry Updates

Add to stage patterns for ALL stages:

```yaml
stage_patterns:
  ai_agent_friendly:
    required_at_stage_root:
      - "CLAUDE.md"    # Stage agent entry point
      - "0INDEX.md"    # Stage discovery
    required_in_outputs:
      - "CLAUDE.md"    # Outputs agent entry
      - "0INDEX.md"    # Outputs discovery
      - "synthesis/"   # Synthesis folder
    optional:
      - "_crossref.md" # If cross-references needed
```

<!-- section_id: "cb137e9b-8034-4b85-b8ff-af2b214f395a" -->
### 2. Layer Registry Updates

Add to layer conventions:

```yaml
layer_conventions:
  ai_agent_friendly:
    required_at_layer_root:
      - "CLAUDE.md"    # Layer agent entry
      - "0INDEX.md"    # Layer discovery
    required_at_features_root:
      - "CLAUDE.md"    # Features manager entry
      - "0INDEX.md"    # Features discovery
      - "_crossref.md" # Feature relationships
    required_per_feature:
      - "CLAUDE.md"    # Feature entry
      - "0INDEX.md"    # Feature discovery
      - "synthesis/"   # Feature synthesis
```

<!-- section_id: "3186a950-768f-4b31-87c9-0f8a4f52e6c2" -->
### 3. Feature Registry Updates

Add to feature patterns:

```yaml
feature_patterns:
  ai_agent_friendly:
    required:
      - "CLAUDE.md"        # With triggers section
      - "0INDEX.md"        # With status tracking
      - "synthesis/"       # Feature-level synthesis
    claude_md_sections:
      - "Identity"
      - "Scope"
      - "Triggers"
      - "On Entry"
      - "Stage Status"
      - "Where to Contribute"
      - "Related Features"
```

---

<!-- section_id: "628aab1d-1edb-4802-ae15-f400065c2c5c" -->
## Implementation Steps

<!-- section_id: "15c25315-7496-4bef-8746-8c376e6da314" -->
### Phase 1: Structure Setup
1. Create `0INDEX.md` at project root
2. Create `_crossref.md` at project root
3. Create `_templates/` folder with templates
4. Update project `CLAUDE.md` with triggers/navigation

<!-- section_id: "55850a14-56fe-43da-a231-50ef317063ed" -->
### Phase 2: Feature Enhancement
For each feature:
1. Create/update `CLAUDE.md` with full template
2. Create `0INDEX.md`
3. Create `synthesis/` folder
4. Ensure stage structure exists

<!-- section_id: "eb0db715-d429-43b7-896c-83c7b388e258" -->
### Phase 3: Research Distribution
1. Move research files to appropriate features
2. Split `layer_stage_instantiation_understanding.md`
3. Move cross-cutting research to project level
4. Move proposals to `proposals/` folder

<!-- section_id: "d89234e6-3318-4c71-a673-06174937d864" -->
### Phase 4: Synthesis Creation
1. Create feature-level synthesis files
2. Create stage-level synthesis files
3. Update project synthesis to point to features
4. Create cross-cutting synthesis

<!-- section_id: "10f0ea4d-7f44-42c0-a0cc-1ae41a4a9596" -->
### Phase 5: Registry Updates
1. Update `stage_registry.yaml`
2. Update `layer_registry.yaml`
3. Create/update `feature_registry.yaml`

<!-- section_id: "bc3681b8-1800-4181-b198-6a5629efdd7b" -->
### Phase 6: Validation
1. Verify all CLAUDE.md files exist
2. Verify all 0INDEX.md files exist
3. Verify all synthesis folders exist
4. Test agent navigation

---

<!-- section_id: "bf6e1946-f4cd-4321-a81b-33231f926b88" -->
## Benefits Summary

| Benefit | How Achieved |
|---------|--------------|
| **Uses our own system** | Research organized into layer-stage-feature hierarchy |
| **Clear entry points** | CLAUDE.md at every level with triggers |
| **Easy discovery** | 0INDEX.md at every level with status |
| **Quick overviews** | synthesis/ folder at every level |
| **Focused loading** | Agent loads one feature, not all research |
| **Clear contribution** | Guidelines in every CLAUDE.md |
| **Progress tracking** | Stage status in 0INDEX.md |
| **Relationship mapping** | _crossref.md shows feature connections |

---

<!-- section_id: "f0004864-32a1-4e39-957b-60fb3c32c76e" -->
## Metrics

| Metric | Count |
|--------|-------|
| Features to enhance | 5 |
| CLAUDE.md files to create/update | ~25 |
| 0INDEX.md files to create | ~25 |
| Synthesis files to create | ~15 |
| Research files to move | 24 |
| Files to split | 1 (into 4) |
| Registry files to update | 3 |

---

<!-- section_id: "639012b3-54c6-4e17-9db9-718a02d54f8c" -->
## Open Questions

1. Should session-specific files (`session_2026-01-30_*.md`) stay in `episodic/` or move to features?
2. Should `episodic/` be at project level only, or per-feature?
3. How to handle research that's 80% one feature, 20% another?
4. Should proposals have their own stage, or stay in outputs?

---

<!-- section_id: "53032f34-3797-4d62-98bd-39eb3e5d9652" -->
## Decision Needed

- [ ] Approve v2 proposal
- [ ] Approve with modifications (specify)
- [ ] Reject, keep v1 approach
- [ ] Reject both, propose alternative

---

<!-- section_id: "a72c5407-c563-49d3-806c-c21269bcfdcc" -->
## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-02-02 | Nested folders within stage outputs |
| v2 | 2026-02-02 | Use layer-stage hierarchy with features + all AI-friendly enhancements |
