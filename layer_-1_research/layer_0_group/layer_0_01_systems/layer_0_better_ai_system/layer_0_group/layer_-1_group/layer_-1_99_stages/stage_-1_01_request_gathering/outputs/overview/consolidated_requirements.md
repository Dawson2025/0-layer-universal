# Consolidated Requirements

**Project**: Better AI System
**Date**: 2026-01-26
**Total Requirements**: 45 Functional, 24 Non-Functional (includes REQ-04-F00 through REQ-04-F00d as CRITICAL)

---

## Core Wants and Needs

These are the five fundamental goals that ALL requirements derive from:

| Need | Description | Key Question |
|------|-------------|--------------|
| **NEED-01: Persistent Knowledge** | AI "knows" the project without loading everything | "How does AI remember without context bloat?" |
| **NEED-02: Cross-Tool Freedom** | Not locked to one AI app | "Can I use Claude Code today, Codex CLI tomorrow?" |
| **NEED-03: Session Continuity** | Pick up where you left off | "What if I run out of tokens or switch tools?" |
| **NEED-04: Scalable Context** | Works for small and large projects | "Does this still work when the project grows 10x?" |
| **NEED-05: Self-Navigating System** | AI finds what it needs | "Can AI understand the system by exploring it?" |

### How Needs Map to Request Areas

| Need | Primary Requests |
|------|-----------------|
| NEED-01: Persistent Knowledge | REQ-04 (Memory), REQ-06 (Context) |
| NEED-02: Cross-Tool Freedom | REQ-04 (Agnostic Architecture) |
| NEED-03: Session Continuity | REQ-04 (Continuity), REQ-03 (Handoffs) |
| NEED-04: Scalable Context | REQ-03 (Delegation), REQ-04 (Progressive Disclosure) |
| NEED-05: Self-Navigating | REQ-01 (Layer-Stage), REQ-05 (Documentation) |

---

## Critical Architectural Pattern

> **Persistent Memory Without Context Bloat**

This is the foundational pattern that addresses the core needs.

### The Problem
AI agents have limited context windows. Loading all project knowledge into every conversation:
- Consumes tokens rapidly
- Slows response times
- Loses focus on the actual task
- Doesn't scale as projects grow

### The Solution: Distributed Knowledge via System Prompts + Delegation

Instead of one agent holding everything in context, use:

1. **Hierarchical System Prompts (CLAUDE.md)**
   - Each layer/stage/component has its own CLAUDE.md
   - Loaded automatically when working in that context
   - Contains only what's needed for that scope
   - Agents inherit context from their location in the hierarchy

2. **Agent-Manager Hierarchy with Delegation**
   - Manager agents don't do everything themselves
   - They delegate to specialized agents who have focused system prompts
   - Each agent loads only the context relevant to its specialty
   - Handoffs transfer minimal state, not full context

3. **Just-in-Time Context Loading (.claude infrastructure)**
   - Skills load references only when needed
   - Agents have role-specific knowledge
   - Progressive disclosure: SKILL.md → references → deep docs
   - Read on demand, not upfront

4. **System Prompt Extension via Referenced Resources**
   - System prompts have size limits - can't inline everything
   - Config folders (`.claude/`, `.agnostic/`) hold extended resources
   - Resources: skills, agents, rules, references, hooks, commands, etc.
   - Prompt references resources → loaded when invoked
   - Agnostic definitions sync to AI app-specific formats

5. **Cross-Tool Session Continuity**
   - Can switch AI apps mid-task (Claude Code → Codex CLI → Gemini CLI, etc.)
   - System is self-describing - any AI can understand current state
   - Handoff documents capture session state for continuation
   - Layer-stage hierarchy enables quick navigation to current work
   - "Tell AI the project, it finds where to pick up"

### How This Maps to Requirements

| Pattern | Implementation | Requests |
|---------|---------------|----------|
| Hierarchical prompts | CLAUDE.md at every level | REQ-05, REQ-06 |
| Agent delegation | Manager → Worker handoffs | REQ-03 |
| Just-in-time loading | Skills with references | REQ-04, REQ-06 |
| Referenced resources | Config folders with skills/agents/rules | REQ-04-F00c |
| Cross-tool continuity | Self-describing system + handoffs | REQ-04-F00d |
| Minimal handoffs | Handoff protocol | REQ-03-F04 |

### Key Metrics
- **Context per task**: Only what's needed (not everything)
- **Token efficiency**: Delegation reduces total usage
- **Scalability**: System grows without context growth

### Existing Implementation

This pattern is already implemented throughout the system:

| Location | Purpose |
|----------|---------|
| `layer_0_group/layer_0_01_ai_manager_system/` | Core manager system with README.md defining roles |
| `layer_0_feature_ai_manager_hierarchy_system/` | Research feature with 57% implementation |
| `ai_agent_system/` directories | Present in every stage for agent configurations |
| `.claude/` folders | Skills, agents, commands, scripts per component |

**Key Research Documents** (in `layer_0_feature_ai_manager_hierarchy_system/`):
- `architecture.md` - Layers, stages, managers, workers, handoffs
- `tools_and_context_systems.md` - How CLAUDE.md, AGENTS.md work as context
- `supervisor_patterns.md` - Orchestration and parallel execution
- `parallel_execution.md` - Scaling via independent workers

**The Core Insight**: Claude Code's CLAUDE.md files are **true system prompts** that:
- Are re-injected every API call
- **Automatically walk up the directory tree** and load ALL parent CLAUDE.md files
- Merge into one unified prompt (general rules from top + specific context from current level)
- Give you "filesystem-as-config" for context
- Enable hierarchical delegation without context explosion

**Contrast with OpenCode**: agents.md only loads from current directory (no cascade).
Achieving hierarchy requires manually spawning separate instances in different directories.

### Multi-Tool Agnostic Architecture

The memory system MUST work across different AI tools, not just Claude Code:

| Tool | Context File | Cascade Behavior |
|------|--------------|------------------|
| Claude Code | CLAUDE.md | Auto-cascade from parents |
| Gemini CLI | GEMINI.md | Manual composition required |
| Codex CLI | AGENTS.md | Single file, no cascade |
| OpenCode CLI | agents.md | Single file, no cascade |

**Key Requirements**:
1. **Source of Truth**: Single agnostic source that syncs to all tools
2. **Tool-Specific Derivations**: Each tool gets its own optimized file
3. **AI App-Specific Overrides**: Each tool file can have tool-specific content preserved during sync
4. **Sync Mechanism**: Changes in source propagate to all tool files

**See Research**: `../../../stage_-1_02_research/outputs/agnostic_memory_system_research.md` for proposed architecture, naming conventions, and implementation approaches.

---

## By Priority

### Critical (Must Have)

| ID | Requirement | Source |
|----|-------------|--------|
| REQ-04-F00 | System Prompt Architecture (CLAUDE.md hierarchy) | Request 04 |
| REQ-04-F00a | Multi-Tool Agnostic Architecture (source of truth + sync) | Request 04 |
| REQ-04-F00b | AI App-Specific Overrides (Claude/Codex/Gemini/OpenCode sections) | Request 04 |
| REQ-04-F00c | System Prompt Extension via Referenced Resources | Request 04 |
| REQ-04-F00d | Cross-Tool Session Continuity | Request 04 |
| REQ-01-F01 | Unified naming convention | Request 01 |
| REQ-01-F02 | Standardized stage numbering | Request 01 |
| REQ-01-F03 | Complete registry system | Request 01 |
| REQ-01-F04 | Consistent status tracking | Request 01 |
| REQ-03-F01 | Agent role definitions | Request 03 |
| REQ-03-F04 | Handoff protocol | Request 03 |
| REQ-05-F01 | Path validation | Request 05 |
| REQ-06-F01 | Unified context rules | Request 06 |
| REQ-08-F01 | Validation suite | Request 08 |

### High (Should Have)

| ID | Requirement | Source |
|----|-------------|--------|
| REQ-02-F01 | Unified configuration manifest | Request 02 |
| REQ-02-F02 | OS abstraction layer | Request 02 |
| REQ-03-F02 | Delegation decision matrix | Request 03 |
| REQ-03-F03 | Agent persona library | Request 03 |
| REQ-05-F02 | Single source of truth | Request 05 |
| REQ-05-F04 | Structure-documentation sync | Request 05 |
| REQ-06-F02 | Agnostic/specific clarity | Request 06 |
| REQ-06-F03 | Entry point chain | Request 06 |
| REQ-07-F01 | Rule hierarchy | Request 07 |
| REQ-08-F03 | Entity scaffolding | Request 08 |
| REQ-08-F04 | CI/CD integration | Request 08 |

### Medium (Nice to Have)

| ID | Requirement | Source |
|----|-------------|--------|
| REQ-02-F03 | Workspace bootstrapping | Request 02 |
| REQ-02-F04 | Synchronization strategy | Request 02 |
| REQ-03-F05 | Session continuity | Request 03 |
| REQ-04-F01 | Session memory persistence | Request 04 |
| REQ-04-F02 | Memory retrieval | Request 04 |
| REQ-05-F05 | Documentation index | Request 05 |
| REQ-06-F04 | Smart context selection | Request 06 |
| REQ-07-F02 | Conflict resolution | Request 07 |
| REQ-07-F03 | Rule registry | Request 07 |
| REQ-08-F02 | Migration automation | Request 08 |
| REQ-08-F05 | Documentation generation | Request 08 |

### Low (Future Consideration)

| ID | Requirement | Source |
|----|-------------|--------|
| REQ-04-F03 | Context compression | Request 04 |
| REQ-04-F04 | Knowledge base building | Request 04 |
| REQ-04-F05 | Memory hierarchy | Request 04 |
| REQ-07-F04 | Active vs archived separation | Request 07 |
| REQ-07-F05 | Rule discovery | Request 07 |

---

## By Request Area

### Request 01: Layer-Stage System (4 functional, 3 non-functional)
- REQ-01-F01: Unified naming convention
- REQ-01-F02: Standardized stage numbering
- REQ-01-F03: Complete registry system
- REQ-01-F04: Consistent status tracking
- REQ-01-NF01: Documentation accuracy
- REQ-01-NF02: Backward compatibility
- REQ-01-NF03: Maintainability

### Request 02: Setup System (5 functional, 3 non-functional)
- REQ-02-F01: Unified configuration manifest
- REQ-02-F02: OS abstraction layer
- REQ-02-F03: Workspace bootstrapping
- REQ-02-F04: Synchronization strategy
- REQ-02-F05: Environment configuration
- REQ-02-NF01: Idempotency
- REQ-02-NF02: Transparency
- REQ-02-NF03: Rollback capability

### Request 03: Manager Hierarchy (5 functional, 3 non-functional)
- REQ-03-F01: Agent role definitions
- REQ-03-F02: Delegation decision matrix
- REQ-03-F03: Agent persona library
- REQ-03-F04: Handoff protocol
- REQ-03-F05: Session continuity
- REQ-03-NF01: Efficiency
- REQ-03-NF02: Clarity
- REQ-03-NF03: Flexibility

### Request 04: Dynamic Memory (8 functional, 3 non-functional)
- REQ-04-F00: System Prompt Architecture **(CRITICAL)**
- REQ-04-F01: Session memory persistence
- REQ-04-F02: Memory retrieval
- REQ-04-F03: Context compression
- REQ-04-F04: Knowledge base building
- REQ-04-F05: Memory hierarchy
- REQ-04-NF01: Storage efficiency
- REQ-04-NF02: Retrieval speed
- REQ-04-NF03: Privacy/security

### Request 05: Documentation System (5 functional, 3 non-functional)
- REQ-05-F01: Path validation
- REQ-05-F02: Single source of truth
- REQ-05-F03: Init prompt clarity
- REQ-05-F04: Structure-documentation sync
- REQ-05-F05: Documentation index
- REQ-05-NF01: Accessibility
- REQ-05-NF02: Maintainability
- REQ-05-NF03: Discoverability

### Request 06: Context System (5 functional, 3 non-functional)
- REQ-06-F01: Unified context rules
- REQ-06-F02: Agnostic/specific clarity
- REQ-06-F03: Entry point chain
- REQ-06-F04: Smart context selection
- REQ-06-F05: Context manifest
- REQ-06-NF01: Efficiency
- REQ-06-NF02: Transparency
- REQ-06-NF03: Flexibility

### Request 07: Rules System (5 functional, 3 non-functional)
- REQ-07-F01: Rule hierarchy
- REQ-07-F02: Conflict resolution
- REQ-07-F03: Rule registry
- REQ-07-F04: Active vs archived separation
- REQ-07-F05: Rule discovery
- REQ-07-NF01: Clarity
- REQ-07-NF02: Maintainability
- REQ-07-NF03: Enforcement

### Request 08: Automation System (5 functional, 3 non-functional)
- REQ-08-F01: Validation suite
- REQ-08-F02: Migration automation
- REQ-08-F03: Entity scaffolding
- REQ-08-F04: CI/CD integration
- REQ-08-F05: Documentation generation
- REQ-08-NF01: Usability
- REQ-08-NF02: Safety
- REQ-08-NF03: Performance

---

## Acceptance Summary

Total acceptance criteria across all requests: 40

| Request | Criteria Count |
|---------|----------------|
| 01 - Layer-Stage | 4 |
| 02 - Setup | 4 |
| 03 - Manager Hierarchy | 5 |
| 04 - Dynamic Memory | 5 |
| 05 - Documentation | 5 |
| 06 - Context | 5 |
| 07 - Rules | 5 |
| 08 - Automation | 5 |
