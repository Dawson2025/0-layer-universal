# Context Framework Onboarding

**Purpose**: Help agents and users understand how context flows through the system.

---

## Quick Start: Read These Diagrams

### Core Diagrams

| Question | Diagram | Path |
|----------|---------|------|
| What context exists? | Context Architecture | `../layer_1_sub_feature_context_visualization/diagrams/current/context_architecture.md` |
| When does context load? | Context Flow | `../layer_1_sub_feature_context_visualization/diagrams/current/context_flow.md` |
| How does context propagate? | Context Propagation | `../layer_1_sub_feature_context_visualization/diagrams/current/context_propagation.md` |
| What do agents start with? | Agent Instantiation Chain | `../layer_1_sub_feature_context_visualization/diagrams/current/agent_instantiation_chain.md` |
| What's the exact loading order? | Context Loading Sequence | `../layer_1_sub_feature_context_visualization/diagrams/current/context_loading_sequence.md` |

### Specific Operation Flows

| Operation | Diagram | Path |
|-----------|---------|------|
| Creating entities | Entity Creation Flow | `../layer_1_sub_feature_context_visualization/diagrams/current/specific_flows/entity_creation_flow.md` |
| Git commits | Git Commit Flow | `../layer_1_sub_feature_context_visualization/diagrams/current/specific_flows/git_commit_flow.md` |
| Entering stages | Stage Workflow Flow | `../layer_1_sub_feature_context_visualization/diagrams/current/specific_flows/stage_workflow_flow.md` |

---

## Key Concepts

### 1. Context Tiers (What Agents Start With)

When an agent is instantiated, context loads in tiers:

```
TIER 0: System Prompt (immutable - from Anthropic)
   ↓
TIER 1: Tools + MCP Servers (from Claude Code)
   ↓
TIER 2: Global CLAUDE.md (~/.claude/CLAUDE.md)
   ↓
TIER 3: Path-based CLAUDE.md files (~ to working directory)
   ↓
TIER 4: Directory-level files (agent reads index.jsonld, discovers .claude/)
   ↓
TIER 5: Instruction-triggered files (chains: md → jsonld → md → ...)
   ↓
TIER 6: Agent decisions (navigate, spawn sub-agent, load on-demand)
```

**See**: Agent Instantiation Chain diagram for details

### 2. Working Directory Matters

Your working directory determines what CLAUDE.md files load automatically:

| Working Directory | CLAUDE.md Files Loaded |
|-------------------|------------------------|
| `~/` | 2 files |
| `~/dawson-workspace/` | 3 files |
| `.../0_layer_universal/` | 5 files |
| `.../layer_-1_better_ai_system/` | 7 files |

**See**: Agent Instantiation Chain diagram for exact chains

### 3. File Format Roles

| File | Auto-loaded? | Purpose |
|------|--------------|---------|
| `CLAUDE.md` | ✅ Yes | Identity, rules, instructions |
| `index.jsonld` | ❌ No | Navigation, conventions, triggers |
| `SKILL.md` | ❌ No | Detailed task procedures |
| `schema.jsonld` | ❌ No | Type definitions, patterns |

**Chain**: CLAUDE.md → index.jsonld → SKILL.md → schema.jsonld

### 4. Navigation Properties

In `index.jsonld` files:

- `nav:parent` - Link to parent entity
- `nav:children` - Links to child entities
- `nav:siblings` - Links to sibling entities
- `conventions.childNaming` - How to name children
- `trigger:onEntityCreation` - Skill to load when creating entities

---

## Common Tasks

### "I need to understand the current context architecture"

Read: `context_architecture.md`

### "I need to understand when context loads"

Read: `context_flow.md`

### "I need to create a new entity (feature, sub-feature, component)"

1. Read `index.jsonld` of the parent
2. Check `conventions.childNaming` for naming pattern
3. Follow `trigger:onEntityCreation` to load skill
4. Use the skill's checklist

### "I need to understand why an agent didn't get the right context"

1. Check what working directory the agent was in
2. Trace the CLAUDE.md chain (context_flow.md)
3. Check if required files were in a loaded path
4. Check if agent needed to read index.jsonld

### "I want to propose a change to context flow"

1. Create a `diagrams/proposed/{proposal_name}/` directory
2. Create `before.md` showing current state
3. Create `after.md` showing proposed state
4. Reference these in your proposal document

---

## Sub-Features of Context Framework

| Sub-Feature | Purpose |
|-------------|---------|
| `layer_1_sub_feature_context_system` | Core context loading and management |
| `layer_1_sub_feature_dynamic_memory` | Session memory and state persistence |
| `layer_1_sub_feature_navigation_system` | JSON-LD navigation, links, triggers |
| `layer_1_sub_feature_context_visualization` | Diagrams and visual tools |

---

## Next Steps

1. **Start with diagrams**: Read the 4 current state diagrams
2. **Trace a real example**: Pick a working directory and trace what loads
3. **Try entity creation**: Create a test entity and see how conventions flow
4. **Propose improvements**: Use before/after diagrams for any changes

---

*Last updated: 2026-02-05*
