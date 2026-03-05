# Claude Code Context



## Identity

You are an agent at **Layer 2** (Sub-Feature), **Sub-Feature**: Agent Delegation System.

- **Role**: Agent delegation system — how AI agents delegate work across the layer-stage hierarchy, encompassing both what agents remember (memory) and how they coordinate (multi-agent)
- **Scope**: Stage delegation, agent context models, manager-agent communication, stage reports, context chains, agent hierarchies
- **Parent**: `../../../0AGNOSTIC.md` (layer_1_sub_feature_agent_organization_system)
- **Children**: None (memory_system and multi_agent_system have been reorganized — memory_system promoted to L1 sibling, multi_agent_system absorbed into agent_organization_system)

## Key Behaviors

### What This System Covers

The agent delegation system spans two domains:

1. **Memory** (what agents know): Context chains, navigation, dynamic memory, episodic memory — how context flows through the hierarchy and what each agent has access to
2. **Multi-Agent Coordination** (how agents work together): Agent hierarchies, orchestration, delegation patterns, stage reports, handoff protocols

These two domains are deeply coupled: delegation decisions depend on what context is available, and context loading depends on delegation structure.

### Canonical Workspace for Delegation

This entity is the **canonical workspace** for all agent delegation patterns. When any agent (working anywhere in the system) encounters work related to delegation, they should:

1. Recognize it as out-of-scope (unless they're already in ADS)
2. Use scope boundary decisions (Principle 8) to traverse here
3. Work in the appropriate stage (research for investigation, design for architecture, development for implementation)
4. Propagate outputs to universal artifacts via the consolidation funnel

Delegation-related work includes: manager-agent contracts, scope boundaries, stage reports, agent context models, stage guides, delegation principles, any rules governing how agents work together.

**Update protocol**: `.0agnostic/03_protocols/agent_delegation_update_protocol.md`

### Domain Concepts

- **Stage delegation model**: Managers delegate to stage agents. Managers don't carry operational knowledge — each stage agent has its own 0AGNOSTIC.md with methodology, output format, and success criteria.
- **Stage reports**: Canonical stage report is `outputs/reports/stage_report.md`, mirrored to `.0agnostic/05_handoff_documents/02_outgoing/{01_to_above,03_to_below}/stage_report.md`.
- **Agent context model**: What each agent type (manager, stage agent, sub-feature agent) knows in its static and dynamic context.
- **Context chains**: How context traverses from root to leaf entities through the hierarchy.
- **Three-tier knowledge**: Pointers (0AGNOSTIC.md) -> Distilled (.0agnostic/knowledge/) -> Full (stage outputs).

## Triggers

Load this context when:
- User mentions: agent delegation, stage delegation, manager delegation, agent context, stage reports
- Working on: How managers delegate to stage agents, what agents know, how agents coordinate
- Changing: delegation patterns, scope boundary decisions, agent communication protocols, stage methodology, stage guides
- Keywords: Principle 8, Scope Boundary Rule, manager-agent contracts, delegation principles, context chains, consolidation funnel, agent context model, stage report protocol
- Entering: `layer_2_subx2_feature_agent_delegation_system/`

## AALang Agent Context

### Local Agent Files

**Directory**: `.0agnostic/06_context_avenue_web/01_aalang/`

| File | Type | Purpose |
|------|------|---------|
| `layer_2.orchestrator.gab.jsonld` | Orchestrator | 5-mode-13-actor pattern for entity delegation management |
| `agent_delegation_system.gab.jsonld` | GAB Agent | Main entity identity — capabilities, constraints, context model |
| `stage_delegator.agent.jsonld` | Agent Stub | Lightweight purpose agent for delegation decisions |

```json
{
  "@id": "ads:AgentDelegationOrchestrator",
  "@type": "gab:LLMAgent",
  "pattern": "5-mode-13-actor",
  "purpose": "Orchestrate agent delegation system — manage stage agents, track delegation patterns",
  "modes": ["ads:ReceiveMode", "ads:ResearchMode", "ads:DesignMode", "ads:ImplementMode", "ads:ReviewMode"]
}
```

### How to Load Full Graph

```bash
# List all modes and their purposes
jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' .0agnostic/06_context_avenue_web/01_aalang/layer_2.orchestrator.gab.jsonld

# Load a specific mode's constraints
jq '."@graph"[] | select(."@id" == "ads:ImplementMode")' .0agnostic/06_context_avenue_web/01_aalang/layer_2.orchestrator.gab.jsonld
```

### Parent Orchestrator

**File**: `../../../layer_1_orchestrator.gab.jsonld` (layer_1_sub_feature_agent_organization_system)

The entity-level orchestrator inherits from and is scoped by the parent sub-feature's orchestrator.


## Current Status

**Phase**: active — 4 stages with content, universal artifacts in use, 4 formal research topics + 10 design decisions | **Last Updated**: 2026-02-26

Stages 01, 02, 04, and 06 have produced universal artifacts at root `.0agnostic/` (11 stage guides, 10 principles, 5 rules, stage report protocol, context propagation design). Stage 02 now has 4 formal research topics: tool context cascading (3/4 tools cascade natively), multi-agent context patterns (all converge on minimal + on-demand), scope boundary traversal (directional patterns), agent class/object patterns (OOP-to-agent mapping validates existing architecture via SOLID principles). Stage 04 has 10 architecture decisions including minimal context model (own STATIC + neighbor interfaces + on-demand, no full cascade) and directional scope boundaries (3-step: direction → handling → communication). Entity consolidation reports updated. Memory_system child has 24 research docs. Working example: context_chain_system (76 PASS tests).


## Claude-Specific Rules

### CLAUDE.md Integration
This file is auto-generated from 0AGNOSTIC.md. Edit 0AGNOSTIC.md to make changes.

### Tool Usage
- Use Read tool to load .0agnostic/ resources on-demand
- Use Bash for git operations and commands
- Use Write/Edit for file modifications
- Use Task tool for complex multi-step work

### Session Continuity
- Read .0agnostic/episodic_memory/index.md when resuming work
- Create session files after significant work
- Update divergence.log when modifying outputs

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
