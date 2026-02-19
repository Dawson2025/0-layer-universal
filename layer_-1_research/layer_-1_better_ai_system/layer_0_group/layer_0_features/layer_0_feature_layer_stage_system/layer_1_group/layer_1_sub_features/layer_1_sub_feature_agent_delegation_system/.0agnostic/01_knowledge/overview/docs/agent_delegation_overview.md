# Agent Delegation Overview

## What Agent Delegation Is

Agent delegation is how AI agents divide work across the layer-stage hierarchy. It spans two coupled domains:

1. **Memory** (what agents know): Context chains, navigation, dynamic memory, episodic memory — how context flows through the hierarchy and what each agent has access to
2. **Multi-Agent Coordination** (how agents work together): Agent hierarchies, orchestration, delegation patterns, stage reports, handoff protocols

These are coupled: delegation decisions depend on available context, and context loading depends on delegation structure.

## Core Model

**Managers delegate, agents operate.** Entity managers maintain the big picture and read stage reports to decide what to delegate. Stage agents do the actual work — each has its own `0AGNOSTIC.md` with identity, methodology, output format, and success criteria.

### What Managers Know (static context)
- Entity identity and scope (from 0AGNOSTIC.md)
- Stage status overview (from 0INDEX.md and stage reports)
- Children and their purposes
- Cross-stage coordination rules

### What Managers Do NOT Know
- Stage-level methodology (that's in each stage's 0AGNOSTIC.md)
- Operational procedures (that's in stage outputs)
- Domain-specific details (that's in `.0agnostic/01_knowledge/`)

### What Stage Agents Know (loaded on entry)
- Their own identity and methodology (from their 0AGNOSTIC.md)
- Parent entity domain context (from parent's `.0agnostic/01_knowledge/`)
- Current state of their stage (from outputs/ and stage_report.md)

## Three-Tier Knowledge

Knowledge flows through three tiers:
1. **Pointers** (0AGNOSTIC.md): What this entity IS, where things are — loaded as static context
2. **Distilled** (`.0agnostic/01_knowledge/`): Condensed domain knowledge, principles, architecture docs — loaded on demand
3. **Full** (stage outputs): Complete research, design specs, test results — loaded only when working in that stage

Managers work at the pointer tier. Stage agents load distilled knowledge on demand. Full detail stays within stages.

## Communication Channels

| Channel | Direction | When |
|---------|-----------|------|
| Stage reports | Stage agent → Manager | Before exiting a stage (async status) |
| Handoff documents | Agent → Agent | At session/agent transitions |
| Team tools (SendMessage) | Any → Any | Real-time coordination during team work |
| Task tools (TaskCreate) | Any → Any | Work tracking and assignment |
| Episodic memory | Session → Session | Async session-to-session continuity |

## Working Example

The **context_chain_system** (at `layer_2_group/.../layer_3_subx3_feature_context_chain_system/`) is the primary working example of this delegation model:
- All 11 stage 0AGNOSTIC.md files populated
- Manager delegates to stage agents via Task tool
- Stage reports used for async status
- Entity `.0agnostic/` fully populated with 50+ knowledge/rules/protocol files
- 76 PASS tests validating the implementation

## Universal Artifacts

The work on agent delegation produced universal artifacts now at `layer_0/.0agnostic/`:

| Artifact | Location | Count |
|----------|----------|-------|
| Stage guides | `01_knowledge/layer_stage_system/stage_guides/` | 11 + template |
| Delegation principles | `01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` | 7 principles |
| Static rules | `02_rules/static/` | 3 (boundary, report, delegation) |
| Dynamic rules | `02_rules/dynamic/` | 2 (loops, parallel) |
| Stage report protocol | `03_protocols/stage_report_protocol.md` | 1 |
