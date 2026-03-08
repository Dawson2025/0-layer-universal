---
resource_id: "d3e8ba31-104b-4ed7-8235-d40c2d47c522"
resource_type: "agnostic_document"
resource_name: "0AGNOSTIC"
---
# 0AGNOSTIC.md - layer_1_sub_feature_agent_organization_system

<!-- section_id: "a112c6ca-4f6d-40e7-aca3-e2dd7a885114" -->
## Identity

entity_id: "89b8614b-15da-411a-b046-3f1554e3903d"


You are an agent at **Layer 1** (Sub-Feature), **Sub-Feature**: Agent Organization System.

- **Role**: Agent organization system — how AI agents are organized as teams, hierarchies, and coordinated groups to overcome the fundamental limitation of single-agent context windows
- **Scope**: Agent team structure, hierarchy, coordination patterns, spawning, communication channels, delegation orchestration
- **Parent**: `../../../0AGNOSTIC.md` (layer_1_feature_layer_stage_system)
- **Children**: agent_delegation_system, agent_hierarchy, orchestration

<!-- section_id: "74990a45-5a38-4120-8998-ccef0873b956" -->
## Key Behaviors

<!-- section_id: "aac405a4-1cf8-461a-a50c-470ff7c09314" -->
### The Fundamental Problem

A single AI agent cannot hold everything for a large project:
1. **Context window overflow** — large codebases and projects exceed what one agent can hold
2. **Skill noise** — loading many skills creates noise; trigger conditions and skill listings pollute context when only one specific capability is needed
3. **Finite static context** — system prompts, CLAUDE.md, and instructions have hard ceilings
4. **Finite dynamic context** — conversation history fills up, especially on large codebases

<!-- section_id: "854529a5-14d6-4ce3-9ccf-4ba51ed648be" -->
### The Solution: Organized Multi-Agent Teams

Split work across many coordinated specialized agents, each with focused context:
- Each agent carries only the context relevant to its scope
- Skills are loaded only by the agents that need them
- Agents communicate through structured channels (stage reports, handoff docs, team tools)
- A hierarchy determines who manages whom, who delegates to whom

<!-- section_id: "e5668396-e7b6-4fcc-95ab-a7f2dbf3a990" -->
### Domain Concepts

- **Agent hierarchy**: Parent-child management relationships — who manages whom in the agent tree
- **Spawning patterns**: When and how to create specialized agents (Task tool, teams, subagents)
- **Communication channels**: Stage reports, handoff documents, team tools, episodic memory as inter-agent communication
- **Coordination patterns**: How agents avoid duplication, share findings, and stay aligned
- **Delegation**: Which agents handle which work, how delegation decisions are made (child entity: agent_delegation_system)

<!-- section_id: "f1f6f34b-8572-4c7f-84ed-7f2aa38f279f" -->
## Triggers

Load this context when:
- User mentions: agent organization, agent teams, agent hierarchy, multi-agent coordination, agent communication
- Working on: How agents are structured as organizations, how they overcome context limits through teamwork
- Entering: `layer_1_sub_feature_agent_organization_system/`

<!-- section_id: "009cd90b-b9ae-4505-b4d0-c0809ee226d0" -->
## Pointers

<!-- section_id: "0e4cd2c9-cb9d-4c51-a9c1-47b747ec30d9" -->
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_2_group/layer_2_subx2_features/` for children

<!-- section_id: "91906b3f-d5a9-4aba-a0d3-6270d391f8fc" -->
### Navigation

| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Stages | `layer_1_group/layer_1_99_stages/` |
| Children | `layer_2_group/layer_2_subx2_features/` |

<!-- section_id: "e5e328a8-282e-435e-b87f-8f60a3970592" -->
## Where to Contribute

| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/episodic_memory/` |

# -- References --

<!-- section_id: "1772e6d0-938f-4be3-9a24-a0bd9d65d6e1" -->
## Navigation

<!-- section_id: "8b6b6039-3c5b-4108-a388-341bb87e6681" -->
### Children

| Child | Purpose | Location |
|-------|---------|----------|
| agent_delegation_system | Which agents handle which work, how delegation decisions are made | `layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_agent_delegation_system/` |
| agent_hierarchy | Parent-child management relationships, who manages whom | `layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_agent_hierarchy/` |
| orchestration | Agent spawning, inter-agent communication, runtime coordination | `layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_orchestration/` |

<!-- section_id: "8e45a5b4-5087-4043-9fe5-dcba294ab268" -->
### Key Locations

| Content | Location |
|---------|----------|
| Entity source of truth | `0AGNOSTIC.md` (this file) |
| Dashboard | `0INDEX.md` |
| Stages | `layer_1_group/layer_1_99_stages/` |
| On-demand resources | `.0agnostic/` |
| Children | `layer_2_group/layer_2_subx2_features/` |

<!-- section_id: "e1cfe1a9-a708-41c1-8563-71066fefbc26" -->
## Current Status

**Phase**: active — entity created, all 3 children migrated (agent_delegation_system from L1, agent_hierarchy + orchestration from multi_agent_system) | **Last Updated**: 2026-03-04

<!-- section_id: "19822fd4-7734-4643-afe0-bb36e662902f" -->
## Success Criteria

This entity succeeds when:
- Agents can be organized into effective teams/hierarchies
- Each agent in the team carries only the context relevant to its scope
- Spawning patterns are documented and repeatable
- Communication channels enable async coordination without context overflow
- The hierarchy maps naturally to the layer-stage structure

<!-- section_id: "aa32387c-cf31-440a-b4a2-50168de62343" -->
## On Exit

1. Update `0INDEX.md` with current state
2. If delegating to children, note which child and what work
