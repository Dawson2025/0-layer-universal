# OpenAI Context



## Identity

You are an agent at **Layer 1** (Sub-Feature), **Sub-Feature**: Agent Delegation System.

- **Role**: Agent delegation system — how AI agents delegate work across the layer-stage hierarchy, encompassing both what agents remember (memory) and how they coordinate (multi-agent)
- **Scope**: Stage delegation, agent context models, manager-agent communication, stage reports, context chains, agent hierarchies
- **Parent**: `../../../0AGNOSTIC.md` (layer_0_feature_layer_stage_system)
- **Children**: memory_system, multi_agent_system (in `layer_2_group/layer_2_subx2_features/`)

## Key Behaviors

### What This System Covers

The agent delegation system spans two domains:

1. **Memory** (what agents know): Context chains, navigation, dynamic memory, episodic memory — how context flows through the hierarchy and what each agent has access to
2. **Multi-Agent Coordination** (how agents work together): Agent hierarchies, orchestration, delegation patterns, stage reports, handoff protocols

These two domains are deeply coupled: delegation decisions depend on what context is available, and context loading depends on delegation structure.

### Domain Concepts

- **Stage delegation model**: Managers delegate to stage agents. Managers don't carry operational knowledge — each stage agent has its own 0AGNOSTIC.md with methodology, output format, and success criteria.
- **Stage reports**: Stage agents write `outputs/reports/stage_report.md` before exiting. Managers read these for async status without loading stage details.
- **Agent context model**: What each agent type (manager, stage agent, sub-feature agent) knows in its static and dynamic context.
- **Context chains**: How context traverses from root to leaf entities through the hierarchy.
- **Three-tier knowledge**: Pointers (0AGNOSTIC.md) -> Distilled (.0agnostic/knowledge/) -> Full (stage outputs).

## Triggers

Load this context when:
- User mentions: agent delegation, stage delegation, manager delegation, agent context, stage reports
- Working on: How managers delegate to stage agents, what agents know, how agents coordinate
- Entering: `layer_1_sub_feature_agent_delegation_system/`

## AALang Agent Context

### Local Agent Files

**Directory**: `.0agnostic/06_context_avenue_web/01_aalang/`

| File | Type | Purpose |
|------|------|---------|
| `layer_1.orchestrator.gab.jsonld` | Orchestrator | 5-mode-13-actor pattern for entity delegation management |
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
jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' .0agnostic/06_context_avenue_web/01_aalang/layer_1.orchestrator.gab.jsonld

# Load a specific mode's constraints
jq '."@graph"[] | select(."@id" == "ads:ImplementMode")' .0agnostic/06_context_avenue_web/01_aalang/layer_1.orchestrator.gab.jsonld
```

### Parent Orchestrator

**File**: `../../../../layer_0_orchestrator.gab.jsonld` (layer_0_feature_layer_stage_system)

The entity-level orchestrator inherits from and is scoped by the parent feature's orchestrator.


## Current Status

**Phase**: active (stage 01 populated, universal artifacts produced, working example established) | **Last Updated**: 2026-02-20

This entity has progressed through stages 01, 02, 04, and 06, producing universal artifacts at `.0agnostic/` (11 stage guides, 10 principles, 3 static rules, 2 dynamic rules, stage report protocol). Working example: context_chain_system (76 PASS tests).


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
