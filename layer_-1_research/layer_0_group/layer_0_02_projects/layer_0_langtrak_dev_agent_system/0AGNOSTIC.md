---
resource_id: "85a52c9c-d16a-425d-b2c0-e5b7f3fad5b9"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

<!-- section_id: "86c585e2-e3a9-4b38-9514-5721edc6ac9b" -->
## Identity

entity_id: "e3f7291d-0aab-4b9b-ad65-879000ed236e"

**Role**: LangTrak Dev Agent System Research Manager
**Scope**: Research and design how AI agents should work together to develop LangTrak — agent roles, delegation patterns, context organization, workflow stages, and MCP tool integration specific to LangTrak's architecture
**Layer**: 0 (Dev Agent System), researched at Layer -1 (Research)
**Parent**: `../../0AGNOSTIC.md` (layer_-1_research)
**Children**: (none yet — features will be added as research topics emerge)

<!-- section_id: "d010bab2-1d93-491c-9989-72350c38afa6" -->
## Key Behaviors

<!-- section_id: "f9ec21cd-97ef-401a-ace7-6b0e0c923a64" -->
### What This System Covers

This research project investigates how to create a development agent system specifically for LangTrak. Unlike the generic agent_delegation_system (which defines universal delegation patterns), this project:

1. **Maps LangTrak's 10-layer feature hierarchy to agent roles** — which agents exist, what each one knows, how they communicate
2. **Designs context chains for LangTrak development** — what context each layer agent needs (STATIC vs on-demand), how universal context cascades
3. **Defines development workflows** — how agents move through stages (design, development, testing) for each LangTrak feature
4. **Integrates MCP tools** — which tools (Mermaid, Playwright, Perplexity, etc.) each agent needs and when
5. **Creates agent definitions** — GAB/AALang agent files for LangTrak-specific roles

<!-- section_id: "3323cd79-9d03-4a78-b08d-9e2a6d0994ce" -->
### Relationship to Agent Delegation System

The ADS entity (`layer_-1_better_ai_system/.../agent_delegation_system/`) defines **universal** delegation patterns. This project **applies** those patterns to LangTrak specifically:

- ADS defines Principle 8 (scope boundaries) → this project defines which boundaries exist in LangTrak
- ADS defines the minimal context model → this project specifies what "minimal" means for each LangTrak layer
- ADS defines stage reports → this project designs what reports each LangTrak stage produces
- ADS defines relay patterns → this project maps relay chains through LangTrak's L2-L11 hierarchy

<!-- section_id: "4c160017-e00f-47fb-9443-5a501d5be479" -->
### Context Discovery

Before starting any task:
1. Read this file
2. Check `../../.0agnostic/02_rules/` for universal rules
3. Check `.0agnostic/` for project-specific resources
4. Read episodic memory if resuming work: `.0agnostic/04_episodic_memory/sessions/`

<!-- section_id: "e1855af1-7e4d-4451-b121-55e7bb3112ba" -->
## Methodology

1. **Research** (stage 02): Study LangTrak's codebase, feature modules, and existing architecture
2. **Design** (stage 04): Design agent roles, context chains, delegation patterns for LangTrak
3. **Development** (stage 06): Create agent definitions (GAB/AALang files), context templates, workflow scripts
4. **Testing** (stage 07): Validate agent definitions against real LangTrak development tasks

<!-- section_id: "80f9a527-c3c1-4e7f-823c-06634fec69aa" -->
## Inputs

| Source | What | Location |
|--------|------|----------|
| LangTrak architecture | Feature hierarchy, codebase structure | `../../../layer_1/layer_1_projects/layer_1_project_lang_trak/` |
| LangTrak design docs | Layer hierarchy, context model | `.../stage_1_04_design/outputs/design_decisions/` |
| Universal delegation patterns | Principles, rules, stage guides | `../../../.0agnostic/01_knowledge/principles/` |
| ADS research | Delegation patterns, scope boundaries | `../layer_0_01_systems/layer_0_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_agent_delegation_system/` |

<!-- section_id: "f8b6d66e-da22-4d48-aacb-0da297d51b41" -->
## Outputs

| Output | Location | Purpose |
|--------|----------|---------|
| Agent role definitions | `outputs/by_topic/` per stage | What each LangTrak dev agent does |
| Context chain specs | `outputs/by_topic/` | What context flows where |
| Agent GAB/AALang files | Stage 06 outputs | Actual agent definition files |
| Development workflow guides | Stage 06 outputs | How agents work through LangTrak stages |

<!-- section_id: "196a5a1f-6cec-4139-a718-703addd100b4" -->
## Triggers

Load this context when:
- User mentions: LangTrak agents, LangTrak dev system, LangTrak development agent
- Working on: How AI agents should develop LangTrak features
- Keywords: LangTrak layer agents, feature agent roles, LangTrak context chains
- Entering: `/layer_-1_research/layer_0_group/layer_0_02_projects/layer_0_langtrak_dev_agent_system/`

# ── Current Status ──

<!-- section_id: "e84fed83-4b37-45ef-939d-9be5c97f5751" -->
## Current Status

**Phase**: Active — Agent Hierarchy Structure Experiment designed, ready for trial execution
**Active stages**: Stage 02 (research) — experiment framework created
**Active experiment**: `stage_-1_02_research/outputs/experiments/agent_hierarchy_structure_experiment.md`
**Trials defined**: A (per-layer), B (domain clusters), C (per-stage), D (hybrid), E (flat team)
**Test tasks**: 7 real LangTrak issues (debug, feature, architecture) across 8 evaluation metrics
**Key questions to investigate**:
1. What agent roles map to LangTrak's 10-layer hierarchy (L2 Infrastructure through L11 Orchestration)?
2. How do cross-cutting layers (L9 Enhancements, L10 Admin, L11 Orchestration) affect agent delegation?
3. What MCP tools does each layer agent need?
4. How should context cascade through LangTrak's dependency chain vs. be loaded on-demand?
5. What does a concrete LangTrak development workflow look like (end to end)?

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

<!-- section_id: "b36d2039-0afa-433c-937d-09fcd6bdbf66" -->
## Open Items

- Initial research topics need to be defined in stage 02
- LangTrak architecture diagrams exist at: `.../stage_1_04_design/outputs/design_decisions/feature_hierarchy/diagrams/`
- Feature layer hierarchy design doc exists at: `.../feature_layer_hierarchy_design.md` (DRAFT)

# ── References ──

<!-- section_id: "83018c91-b83f-47a8-a0fa-117234d832cd" -->
## Navigation

| Direction | Path |
|-----------|------|
| Parent | `../0AGNOSTIC.md` |
| Stages | `layer_-1_group/layer_-1_99_stages/` |
| LangTrak project | `../../layer_1/layer_1_projects/layer_1_project_lang_trak/` |
| LangTrak design | `.../stage_1_04_design/outputs/design_decisions/feature_hierarchy/` |
| ADS entity | `../layer_-1_better_ai_system/.../agent_delegation_system/` |
| Universal principles | `../../.0agnostic/01_knowledge/principles/` |

<!-- section_id: "618c47a6-193a-4591-bf93-e991223fea09" -->
## Where to Contribute

| Work Type | Location |
|-----------|----------|
| Research findings | `layer_-1_group/layer_-1_99_stages/stage_-1_02_research/outputs/` |
| Design decisions | `layer_-1_group/layer_-1_99_stages/stage_-1_04_design/outputs/` |
| Agent definitions | `layer_-1_group/layer_-1_99_stages/stage_-1_06_development/outputs/` |
| Session notes | `.0agnostic/04_episodic_memory/sessions/` |
