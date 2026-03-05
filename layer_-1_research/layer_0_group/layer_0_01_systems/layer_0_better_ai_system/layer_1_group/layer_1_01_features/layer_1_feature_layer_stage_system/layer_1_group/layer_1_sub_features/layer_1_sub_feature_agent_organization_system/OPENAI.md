# OpenAI Context


## Identity

You are an agent at **Layer 1** (Sub-Feature), **Sub-Feature**: Agent Organization System.

- **Role**: Agent organization system — how AI agents are organized as teams, hierarchies, and coordinated groups to overcome the fundamental limitation of single-agent context windows
- **Scope**: Agent team structure, hierarchy, coordination patterns, spawning, communication channels, delegation orchestration
- **Parent**: `../../../0AGNOSTIC.md` (layer_1_feature_layer_stage_system)
- **Children**: agent_delegation_system, agent_hierarchy, orchestration

## Key Behaviors

### The Fundamental Problem

A single AI agent cannot hold everything for a large project:
1. **Context window overflow** — large codebases and projects exceed what one agent can hold
2. **Skill noise** — loading many skills creates noise; trigger conditions and skill listings pollute context when only one specific capability is needed
3. **Finite static context** — system prompts, CLAUDE.md, and instructions have hard ceilings
4. **Finite dynamic context** — conversation history fills up, especially on large codebases

### The Solution: Organized Multi-Agent Teams

Split work across many coordinated specialized agents, each with focused context:
- Each agent carries only the context relevant to its scope
- Skills are loaded only by the agents that need them
- Agents communicate through structured channels (stage reports, handoff docs, team tools)
- A hierarchy determines who manages whom, who delegates to whom

### Domain Concepts

- **Agent hierarchy**: Parent-child management relationships — who manages whom in the agent tree
- **Spawning patterns**: When and how to create specialized agents (Task tool, teams, subagents)
- **Communication channels**: Stage reports, handoff documents, team tools, episodic memory as inter-agent communication
- **Coordination patterns**: How agents avoid duplication, share findings, and stay aligned
- **Delegation**: Which agents handle which work, how delegation decisions are made (child entity: agent_delegation_system)

## Triggers

Load this context when:
- User mentions: agent organization, agent teams, agent hierarchy, multi-agent coordination, agent communication
- Working on: How agents are structured as organizations, how they overcome context limits through teamwork
- Entering: `layer_1_sub_feature_agent_organization_system/`

## Pointers

### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_2_group/layer_2_subx2_features/` for children

### Navigation

| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Stages | `layer_1_group/layer_1_99_stages/` |
| Children | `layer_2_group/layer_2_subx2_features/` |

## Where to Contribute

| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/episodic_memory/` |

# -- References --

## Navigation

### Children

| Child | Purpose | Location |
|-------|---------|----------|
| agent_delegation_system | Which agents handle which work, how delegation decisions are made | `layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_agent_delegation_system/` |
| agent_hierarchy | Parent-child management relationships, who manages whom | `layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_agent_hierarchy/` |
| orchestration | Agent spawning, inter-agent communication, runtime coordination | `layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_orchestration/` |

### Key Locations

| Content | Location |
|---------|----------|
| Entity source of truth | `0AGNOSTIC.md` (this file) |
| Dashboard | `0INDEX.md` |
| Stages | `layer_1_group/layer_1_99_stages/` |
| On-demand resources | `.0agnostic/` |
| Children | `layer_2_group/layer_2_subx2_features/` |

## Current Status

**Phase**: active — entity created, all 3 children migrated (agent_delegation_system from L1, agent_hierarchy + orchestration from multi_agent_system) | **Last Updated**: 2026-03-04

## Success Criteria

This entity succeeds when:
- Agents can be organized into effective teams/hierarchies
- Each agent in the team carries only the context relevant to its scope
- Spawning patterns are documented and repeatable
- Communication channels enable async coordination without context overflow
- The hierarchy maps naturally to the layer-stage structure

## On Exit

1. Update `0INDEX.md` with current state
2. If delegating to children, note which child and what work

## OpenAI-Specific Notes

### Function Calling
When using OpenAI function calling:
- Read .0agnostic/ resources for detailed instructions
- Check episodic memory for context
- Follow multi-agent sync rules for shared files

### Context Window Management
- 0AGNOSTIC.md is lean (<400 tokens)
- Load .0agnostic/ resources on-demand
- Avoid loading everything upfront

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
