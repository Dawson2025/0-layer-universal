---
resource_id: "d2a23fc6-4dd8-4f37-8781-0634588599e4"
resource_type: "rule"
resource_name: "agent_delegation_workspace_rule"
---
# Agent Delegation Workspace Rule

**Type**: Dynamic (applies when delegation work is identified)
**Scope**: All agents working on delegation-related topics
**Importance**: I1 (High)

## Rule

Work related to agent delegation patterns belongs in the **agent_delegation_system** entity, not in the entity where you currently are. This entity maintains the full propagation chain (stage outputs -> universal artifacts) and working examples. Delegation changes made elsewhere won't propagate correctly.

**Canonical workspace path**: `layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_agent_delegation_system/`

## When This Applies

Triggers:
- Changing how agents delegate to each other
- Modifying scope boundary decisions (Principle 8)
- Updating stage methodology or stage guides
- Changing manager-agent communication protocols
- Adding or removing delegation principles
- Modifying stage report format or protocol
- Changing agent context models (what agents know in STATIC vs DYNAMIC)
- Updating the Scope Boundary Rule

Keywords that indicate delegation work:
- Principle 8, Scope Boundary Rule, stage guides, stage delegation
- Manager-agent contracts, delegation principles, agent context model
- Stage reports, consolidation funnel, context propagation
- Agent hierarchies, multi-agent coordination, instantiation decisions

## What to Do

1. **Recognize** this is out-of-scope for your current entity/stage
2. **Apply Principle 8** (Scope Boundary Decisions) — this is an "up" or "sideways" traversal depending on your position
3. **Traverse** to the agent_delegation_system entity (path above)
4. **Follow** the update protocol at that entity: `.0agnostic/03_protocols/agent_delegation_update_protocol.md`

## Why

The agent_delegation_system entity:
- Maintains 4 active stages (01 requirements, 02 research, 04 design, 06 development) for delegation work
- Produces universal artifacts (11 stage guides, 10 principles, 5 rules, 1 protocol) via the consolidation funnel
- Has working examples (context_chain_system with 76 PASS tests) that validate changes
- Follows the propagation chain: stage outputs -> stage reports -> stages_report -> layer_report -> 0AGNOSTIC.md

Delegation changes made elsewhere:
- Won't have corresponding stage outputs (research, design decisions)
- Won't propagate through the consolidation funnel
- Won't be validated against working examples
- Won't appear in entity reports for future reference

## See Also

- **Principle 8**: `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md`
- **Scope Boundary Rule**: `.0agnostic/02_rules/static/STAGE_BOUNDARY_RULE/STAGE_BOUNDARY_RULE.md`
- **Update Protocol**: At ADS entity `.0agnostic/03_protocols/agent_delegation_update_protocol.md`
