---
resource_id: "9a0b7c8f-3358-4e63-b26f-046d84c8f862"
resource_type: "agnostic_document"
resource_name: "0AGNOSTIC"
---
# Layer -1 - Research Context

<!-- section_id: "29781dce-1404-499f-b7cb-cdaf8b5a769b" -->
## Identity

entity_id: "08fe74b8-89f1-4aaa-82f2-03130df055fe"

You are an AI agent working within the layer_-1 (research) context. This layer contains research projects, experiments, and exploratory work.

<!-- section_id: "e1525dde-e056-4d29-b4ad-9cc8ff375278" -->
## Navigation
- **Detailed resources**: `.0agnostic/` folder
- **Universal rules**: Inherit from `../.0agnostic/rules/`
- **Layer_-1 metadata**: In `layer_-1_group/layer_-1_00_layer_registry/`
- **Layer_-1 workflow stages**: In `layer_-1_group/layer_-1_99_stages/`
- **Layer_0 research group**: In `layer_0_group/` (researching layer_0 structures)
- **Layer_0 systems**: In `layer_0_group/layer_0_01_systems/` (foundational architectural systems)
  - Each system (e.g., `layer_0_better_ai_system/`) has its own `layer_0_group/layer_0_99_stages/`
- **Layer_0 projects**: In `layer_0_group/layer_0_02_projects/` (specific applications/initiatives)
  - Each project (e.g., `layer_0_langtrak_dev_agent_system/`) has its own `layer_0_group/layer_0_99_stages/`
- **Layer_0 registry**: In `layer_0_group/layer_0_00_layer_registry/` (metadata only, no stages)
- **Active research**: See Active Research Projects section below

<!-- section_id: "62cbc1ed-60c3-4fea-8f2d-f9818da83458" -->
## Key Behaviors

<!-- section_id: "69ebbd95-b1f8-4341-bcab-55554992e8e2" -->
### Agent Context Loading
Each directory may have a `.gab.jsonld` agent definition with a matching `.integration.md` summary (same base name):
- e.g., `agent_orchestrator.gab.jsonld` → `agent_orchestrator.integration.md`
- Read the `.integration.md` for a quick summary; query the `.gab.jsonld` via jq for precise mode constraints
- `.integration.md` files are auto-generated — do not edit directly

<!-- section_id: "628b34ee-57c7-432d-a842-21fdbfd48bff" -->
### Context Discovery
Before starting any task:
1. Read this file (0AGNOSTIC.md)
2. Check `../.0agnostic/02_rules/` for universal rules
3. Read project-specific context in research directories
4. Find the `.gab.jsonld` for your role and read its matching `.integration.md`
5. Read episodic memory if resuming work

<!-- section_id: "c75155bc-91a5-4c9d-a141-c9da3d44beaf" -->
### Episodic Memory
Record your work in `.0agnostic/episodic_memory/`:
- Create session files for significant work
- Update divergence.log when changing outputs
- Enable next session to continue seamlessly
- **Quick review**: Check `memory/episodic.md` (auto-memory topic file) for recent session history across all layers
- **After updating**: Run `.0agnostic/01_knowledge/layer_stage_system/resources/tools/episodic-sync.sh` to sync episodic memory to auto-memory

<!-- section_id: "843eb030-860e-4aa0-b685-affc085ee351" -->
### Research Protocol
Research projects follow stages 01-11 (see Stage Navigation below).

<!-- section_id: "d0abe0ca-aecb-4ddb-b23b-14d62459103e" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Need universal rules | Load `../.0agnostic/rules/` |
| Starting research | Navigate to project's stage_-1_02_research |
| Designing solutions | Navigate to project's stage_-1_04_design |
| Starting new session | Read `.0agnostic/episodic_memory/index.md` |

<!-- section_id: "a8f23451-018b-47e4-b902-6e30a640a48b" -->
## Active Research Projects

Layer_0 research is organized into two categories:

<!-- section_id: "ba4feeaf-7a9a-43b7-abba-df694519960c" -->
### Layer_0 Systems
Foundational, reusable architectural constructs in `layer_0_group/layer_0_systems/`:

- **layer_-1_better_ai_system**: SHIMI concepts, agent memory, multi-agent sync
- **layer_-1_learning_simulation_system**: Learning simulation frameworks and patterns

<!-- section_id: "51445d73-4e6d-4308-bbac-49c99a268cb9" -->
### Layer_0 Projects
Specific applications/initiatives in `layer_0_group/layer_0_projects/`:

- **layer_-1_langtrak_dev_agent_system**: Development of language tracking agent system

<!-- section_id: "0d091d91-d203-403c-8e89-123b86b79172" -->
## Quick Reference

- **Layer**: -1 (research - experimental work)
- **Inherits**: layer_0 universal rules
- **Stages**: 01-11 (research workflow)
- **Memory**: Episodic (sessions preserve context)

<!-- section_id: "212f5b39-9ac7-42d5-82b0-48ac6c9ff82e" -->
## Stage Navigation

Stages are numbered 01-11 and represent workflow phases:

| Stage | Name | Purpose |
|-------|------|---------|
| 01 | Request Gathering | Clarify requirements |
| 02 | Research | Explore, gather info |
| 03 | Instructions | Define constraints |
| 04 | Design | Architecture |
| 05 | Planning | Break into subtasks |
| 06 | Development | Implementation |
| 07 | Testing | Verification |
| 08 | Criticism | Review |
| 09 | Fixing | Corrections |
| 10 | Current Product | Deliverable |
| 11 | Archives | History |

**To identify current stage**: Check your working directory path for `stage_*_NN_*` pattern.

**To find stage content**: Use `0INDEX.md` at `layer_-1_group/layer_-1_99_stages/` directory, or within each project's own stages directory.

---

*This is a tool-agnostic context file. See `.0agnostic/` for detailed resources.*

