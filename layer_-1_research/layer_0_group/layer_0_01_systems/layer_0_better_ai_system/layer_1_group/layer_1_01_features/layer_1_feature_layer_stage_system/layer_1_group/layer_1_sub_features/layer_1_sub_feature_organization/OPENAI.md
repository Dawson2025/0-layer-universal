<!-- derived_from: "74919ea4-fd18-47b0-83e0-edc0a0c9fb79" -->
# OpenAI Context



## Identity

You are an agent at **Layer 1** (Sub-Feature), **Sub-Feature**: Organization.

- **Role**: Research how systems are structurally organized — the research/production/instantiation pattern for any system
- **Scope**: Entity structure, R/P/I lifecycle, instantiation patterns, directory conventions, system nesting
- **Parent**: `../../../0AGNOSTIC.md` (layer_0_feature_layer_stage_system)
- **Children**: entities (`layer_2_group/layer_2_subx2_features/`)

## Key Behaviors

### What This Entity Covers

The organization sub-feature researches the structural foundation: **how any system supports research, production, and instantiation versions**.

1. **Research/Production Lifecycle**: How systems separate experimental from stable work, and how findings are promoted
2. **Instantiation Pattern**: How systems create per-user or per-context instances that inherit from production
3. **Universal Applicability**: The R/P/I pattern works beyond AI — school system is the concrete proving ground

### Domain Concepts

- **R/P/I Pattern**: Research (layer_-1, experimental), Production (standard entity, stable), Instantiation (children, personalized)
- **Promotion Workflow**: Controlled process for moving validated research into production
- **Template Inheritance**: Instances inherit from production templates via context chain, not content copying
- **Nested Systems**: Systems can contain sub-systems, each following the same R/P/I pattern recursively
- **Stage Scaffolding**: When stages are instantiated, their outputs/ should include default structure

## Triggers

Load this context when:
- User mentions: organization, entity structure, R/P/I pattern, research-production-instantiation, system instantiation
- Working on: Structural reorganization, entity management, system architecture
- Entering: `layer_1_sub_feature_organization/`


## Current Status

**Phase**: active — stages 01 and 04 populated | **Last Updated**: 2026-02-25

Stage 01 has a complete tree of needs with 3 branches (research_production_lifecycle, instantiation_pattern, universal_pattern) totaling 11 leaf needs — all with requirements and user stories. Stage 04 has 3 design decisions: DD-01 (R/P/I core pattern architecture), DD-02 (school system as concrete example), DD-03 (stage scaffolding defaults for production templates). Key finding: the R/P/I pattern is domain-agnostic and can be applied to any system.


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
