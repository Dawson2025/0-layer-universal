# Research Synthesis: Better AI System

**Layer**: -1 (Research)
**Stage**: 02_research
**Date**: 2026-02-02
**Status**: In Progress

---

## Executive Summary

This synthesis consolidates all research from the `better_ai_system` project. The research addresses a core problem: **how to build an AI context system that survives session boundaries, works across multiple tools, and scales with project complexity**.

### Key Findings

1. **Agent Amnesia is Real**: 41.8% of AI agent failures are context-related. The solution requires explicit architectural structure, not just better prompts.

2. **Three-Layer Memory Architecture**: Industry standard is Immediate (session) → Episodic (cross-session) → Semantic (global knowledge).

3. **AGNOSTIC System Design**: Dual `0AGNOSTIC.md` + `.0agnostic/` system provides tool portability with single source of truth.

4. **Claude Code's Memory Gap**: Claude Code stores extensive session data but doesn't use it for memory. The lack of automatic memory is **by design** (transparency, privacy, technical challenges).

5. **Your System is 80% There**: The remaining 20% is automation (hooks, traversal), not architecture.

6. **You Already Have Multi-Agent**: CLI tools can spawn sub-agents, filesystem is shared context - this is a TRUE multi-agent system with sync needs.

7. **Tool Rankings Established**: Tier 1: Claude Code + Cursor. Tier 2: Aider + Copilot + Codex. Tier 3: Gemini + OpenCode + Continue.

---

## Quick Reference: When to Read What

| If You Need To... | Read This File | Location |
|-------------------|----------------|----------|
| Understand layer-stage instantiation | `layer_stage_instantiation_understanding.md` | `by_topic/` |
| Learn agent amnesia solutions | `agent_amnesia_and_context_systems_conversation.md` | `by_topic/` |
| Compare external frameworks | `agent_amnesia_external_approaches.md` | `outputs/` root |
| Understand system prompt architecture | `system_prompt_architecture.md` | `02_finished_understanding/by_topic/` |
| Compare tools and choose which to use | Tool Rankings section in `layer_stage_instantiation_understanding.md` | `by_topic/` |
| Design agnostic sync system | `agnostic_sync_system_design.md` | `by_topic/` |
| Understand why Claude Code lacks memory | `why_claude_code_lacks_memory_research.md` | `by_topic/` |
| See recommendations for your system | `memory_system_recommendation.md` | `by_topic/` |
| Compare your system vs SHIMI | `system_comparison_and_recommendations.md` | `by_topic/` |
| Understand multi-agent implications | `multi_agent_parallel_execution_insight.md` | `by_topic/` |

---

## Topic Summaries with Triggers

### 1. Agent Amnesia Problem

**Trigger**: When starting a new session, when context seems lost, when agent forgets previous work

**Key Insight**: 41.8% of AI agent failures are context-related. Agents "wake up" each session with no memory.

**Solution Pattern**: Identity → Triggers → Pointers
- Tell agent WHO it is (identity, scope, constraints)
- Tell agent WHEN to do things (triggers for conditional loading)
- Tell agent WHERE to find things (pointers to resources)

**Source Files**:
- `by_topic/agent_amnesia_and_context_systems_conversation.md` - Full conversation with solutions
- `outputs/agent_amnesia_external_approaches.md` - External framework research (LangGraph, AutoGen, CrewAI, etc.)
- `by_topic/session_2026-01-30_agent_amnesia_research.md` - Session log

---

### 2. System Prompt Architecture

**Trigger**: When designing what goes IN system prompt vs REFERENCED, when structuring CLAUDE.md

**Key Insight**: System prompt = content in EVERY API call. Referenced = loaded on-demand.

**Approved Pattern**: Container-as-Manager
- Folders with CLAUDE.md are managers of their contents
- CLAUDE.md defines identity, scope, navigation, behaviors
- Resources in `.claude/` or `.0agnostic/` loaded on-demand

**What Goes IN System Prompt**:
- Identity and scope
- Critical rules (small, enforced)
- Navigation triggers
- Mandatory protocols

**What Gets REFERENCED**:
- Knowledge files
- Optional rules
- Detailed procedures
- Historical context

**Source Files**:
- `02_finished_understanding/by_topic/system_prompt_architecture.md` - **APPROVED** - Ready for instructions stage
- `by_topic/agent_amnesia_and_context_systems_conversation.md` - Design process

**Status**: APPROVED - Ready to move to instructions stage

---

### 3. Three-Tier Folder Architecture

**Trigger**: When setting up tool portability, when creating new entities, when building for multiple AI tools

**Architecture**:
```
.0agnostic/         # SOURCE - Tool-agnostic (edit here)
.1*_merge/          # BUILD - Tool-specific overrides/additions
.<tool>/            # OUTPUT - What tools actually read (generated)
```

**Generation Flow**:
```
0AGNOSTIC.md + .1claude_merge/overrides → CLAUDE.md
.0agnostic/ + .1claude_merge/ → .claude/
```

**Source Files**:
- `by_topic/layer_stage_instantiation_understanding.md` - Comprehensive architecture
- `by_topic/agnostic_sync_system_design.md` - Sync script design
- `by_topic/agnostic_memory_system_research.md` - Initial research

---

### 4. Tool Context Systems

**Trigger**: When working with specific AI tools, when configuring tool-specific behavior, when migrating between tools

**Tool Quick Reference**:

| Tool | Main File | Config Folder | Dynamic Rules |
|------|-----------|---------------|---------------|
| Claude Code | `CLAUDE.md` | `.claude/` | Globs in frontmatter |
| Cursor | `.cursorrules` | `.cursor/rules/` | Globs in MDC frontmatter |
| Copilot | `copilot-instructions.md` | `.github/` | `applyTo` frontmatter |
| Gemini CLI | `GEMINI.md` | `~/.gemini/` | `@import` syntax |
| Codex CLI | `AGENTS.md` | `~/.codex/` | N/A (global only) |
| Aider | `.aider.conf.yml` | N/A | N/A (config only) |
| OpenCode | Config YAML | `.opencode/` | Agent prompts |
| Continue | `config.yaml` | `.continue/` | Context providers |

**Source Files**:
- `by_topic/layer_stage_instantiation_understanding.md` - Detailed docs for all 8 tools
- `by_topic/ai_context_filesystem_locations.md` - Filesystem locations research

---

### 5. Tool Rankings & Recommendations

**Trigger**: When choosing which tool to use, when setting up workflow, when budgeting

**Tier 1 (Primary)**:
- **Claude Code** ⭐⭐⭐⭐⭐ - Large codebases, refactoring, complex reasoning
- **Cursor** ⭐⭐⭐⭐⭐ - IDE experience, real-time completion

**Tier 2 (Strong Alternatives)**:
- **Aider** ⭐⭐⭐⭐ - Git integration, model flexibility, BYOK
- **GitHub Copilot** ⭐⭐⭐⭐ - Teams, GitHub integration
- **Codex CLI** ⭐⭐⭐⭐ - Autonomous task completion

**Tier 3 (Specialized)**:
- **Gemini CLI** ⭐⭐⭐½ - Free tier, Google ecosystem
- **OpenCode** ⭐⭐⭐½ - Open source, custom agents
- **Continue** ⭐⭐⭐ - IDE integration, OSS

**Recommended Combo for Solo Devs**:
```
Claude Code (complex work) + Cursor (daily coding) + Aider (model flexibility)
```

**Source Files**:
- `by_topic/layer_stage_instantiation_understanding.md` - Tool Rankings section

---

### 6. Memory System Recommendation

**Trigger**: When deciding whether to build custom memory vs use existing, when prioritizing improvements

**Key Recommendation**: Hybrid approach - keep custom system, add automation

**What You Have** (Keep It):
- File-based memory (CLAUDE.md hierarchy)
- Episodic structure (outputs/episodic/)
- Handoff documents
- Layer-stage organization

**What to Add** (Automation):
- SessionStart hooks for auto-traversal
- PreCompact hooks for session summary
- Automated context gathering

**Quote**: "You're 80% there. The remaining 20% is automation, not architecture."

**Source Files**:
- `by_topic/memory_system_recommendation.md` - Full recommendation
- `by_topic/why_claude_code_lacks_memory_research.md` - Why Claude Code is designed this way
- `by_topic/claude_code_memory_gap_analysis.md` - Gap analysis

---

### 7. Multi-Agent System Insights

**Trigger**: When multiple agents work in parallel, when dealing with sync issues, when designing agent coordination

**Key Insight**: Your system IS multi-agent. CLI tools spawn sub-agents, filesystem is shared context.

**Implications**:
- Need file locking (prevent concurrent writes)
- Need change tracking (Git-based hashing)
- Need conflict resolution (CRDT merge rules)
- Need atomic operations (temp files + rename)

**What You Need from SHIMI-adjacent concepts**:
1. File locking (prevent conflicts)
2. Git-based change tracking (detect divergence)
3. CRDT merge rules (resolve conflicts)
4. Atomic operations (ensure consistency)

**What You DON'T Need**:
- Network protocols
- Separate memory trees
- Decentralized consensus

**Source Files**:
- `by_topic/multi_agent_parallel_execution_insight.md` - Full analysis
- `by_topic/system_comparison_and_recommendations.md` - Comparison with SHIMI
- `by_topic/shimi_framework_research.md` - SHIMI research
- `by_topic/shimi_sync_mechanisms_explained.md` - Sync mechanisms

---

### 8. External Framework Comparison

**Trigger**: When considering whether to adopt external frameworks, when comparing approaches

**Frameworks Researched**:
- LangGraph (state machine + memory)
- AutoGen (multi-agent conversation)
- CrewAI (role-based agents)
- OpenAI Agents SDK
- Anthropic patterns

**Key Finding**: Three-layer memory is industry standard:
1. **Immediate** (in-context) - Current session
2. **Episodic** (short-term) - Recent sessions
3. **Semantic** (long-term) - Persistent knowledge

**Your System vs Frameworks**:
| Requirement | Your System | SHIMI | Result |
|-------------|-------------|-------|--------|
| tool_portable | ✅ Strong | ❌ Weak | You win |
| cross_platform | ✅ Strong | ❌ Weak | You win |
| bounded | ✅ Strong | ❌ Weak | You win |
| auditable | ✅ Strong | ✅ Strong | Tie |
| discoverable | ⚠️ Partial | ✅ Strong | SHIMI wins |
| debuggable | ⚠️ Partial | ✅ Strong | SHIMI wins |

**Recommendation**: Stay with custom system, add discovery/debugging tooling

**Source Files**:
- `outputs/agent_amnesia_external_approaches.md` - Comprehensive external research
- `by_topic/why_not_use_existing_frameworks.md` - Analysis
- `by_topic/can_custom_system_outperform_frameworks.md` - Comparison
- `by_topic/automated_traversal_for_your_system.md` - Discovery tooling ideas

---

### 9. Layer-Stage Instantiation

**Trigger**: When creating new projects/features/components, when understanding system structure

**Core Concepts**:
1. **Layers = Specificity**: Universal (0) → Project (1) → Feature (2) → Component (3)
2. **Rules CASCADE**: Lower layer rules apply to all higher layers
3. **Two-folder structure**: `layer_N/` (internals) + `layer_N+1/` (children)
4. **Design before Planning**: Stage 04 = design, Stage 05 = planning

**Entity Structure**:
```
layer_N_<type>_<name>/
├── 0AGNOSTIC.md          # Source of truth
├── CLAUDE.md             # Generated
├── .0agnostic/           # Agnostic config
├── .claude/              # Tool-specific
├── layer_N/              # Entity internals
│   └── layer_N_99_stages/
└── layer_N+1/            # Children
```

**Source Files**:
- `by_topic/layer_stage_instantiation_understanding.md` - **COMPREHENSIVE** (2300+ lines)

---

## Files by Category

### Finished Understanding (Ready for Instructions)
- `02_finished_understanding/by_topic/system_prompt_architecture.md` ✅

### Large Files (Consider Splitting)
- `by_topic/layer_stage_instantiation_understanding.md` - 2300+ lines
- `by_topic/agent_amnesia_and_context_systems_conversation.md` - 794 lines
- `outputs/agent_amnesia_external_approaches.md` - 672 lines

### Session Tracking
- `episodic/index.md`
- `episodic/sessions/session_2026-01-30_agent_amnesia.md`
- `episodic/sessions/session_2026-02-01_tool_conventions.md`
- `episodic/changes/2026-01-30_changes.md`

---

## Proposals Pending Review

| Proposal | File | Status | Affects |
|----------|------|--------|---------|
| AI-Friendly Output Organization v1 | `../../../../../../layer_-1_00_layer_registry/proposals/proposal_ai_friendly_output_organization.md` | ⚠️ Superseded | - |
| AI-Friendly Output Organization v2 | `../../../../../../layer_-1_00_layer_registry/proposals/proposal_ai_friendly_output_organization_v2.md` | ⚠️ Superseded | - |
| AI-Friendly Output Organization v3 | `../../../../../../layer_-1_00_layer_registry/proposals/proposal_ai_friendly_output_organization_v3.md` | ⚠️ Superseded | - |
| AI-Friendly Output Organization v4 | `../../../../../../layer_-1_00_layer_registry/proposals/proposal_ai_friendly_output_organization_v4.md` | ⚠️ Superseded | - |
| AI-Friendly Output Organization v5 | `../../../../../../layer_-1_00_layer_registry/proposals/proposal_ai_friendly_output_organization_v5.md` | ⚠️ Superseded | - |
| AI-Friendly Output Organization v6 | `../../../../../../layer_-1_00_layer_registry/proposals/proposal_ai_friendly_output_organization_v6.md` | **Pending Review** | Entity registry, stage registry, layer registry |

**v6 Proposal Summary**: Complete AI system architecture (final corrections):
- **Group folder naming**: `layer_N_group/` and `layer_N+1_group/` suffix for clarity
- **Sub^n naming conventions**: Full depth patterns (sub_, sub_sub_, sub^n)
- **Explicit merge flow**: 0AGNOSTIC.md → .1*_merge/ → CLAUDE.md/GEMINI.md/AGENTS.md
- **All system prompts in stages**: CLAUDE.md, GEMINI.md, AGENTS.md, .cursorrules
- **Proposals subdirectories**: `outputs/proposals/` in each stage
- **Context flow diagrams**: AI agent entry → triggers → pointers → resources
- **Setup-dependent sub-layers**: sub_layer_N_05+ in hierarchy
- **9-phase implementation plan**: Cleanup → Proposals → Rename Groups → Agnostic → Entity Structure → Features → Distribution → Sync → Registries

---

## Actionable Next Steps

### Immediate (Instructions Stage Ready)
1. Move `system_prompt_architecture.md` to Stage 03 (instructions)
2. Create formal specification for Container-as-Manager pattern
3. Define AGNOSTIC.md template and validation rules
4. **Review and approve** `proposal_ai_friendly_output_organization.md`

### Short-term (Automation Needed)
1. Build `agnostic-sync.sh` script for tool generation
2. Create SessionStart hook for auto-traversal
3. Add PreCompact hook for session summary

### Medium-term (Architecture Improvements)
1. Implement file locking for multi-agent coordination
2. Add Git-based change tracking between sessions
3. Build discovery tooling for automated context gathering

### Future (If Needed)
1. Consider Bloom filters if change detection is slow
2. Evaluate CRDT merge rules for conflict resolution
3. Build debugging visibility tools

---

## Source Files Index

### By Topic (In Progress)
| File | Lines | Topic |
|------|-------|-------|
| `layer_stage_instantiation_understanding.md` | 2300+ | Comprehensive instantiation guide + tool context + rankings |
| `agent_amnesia_and_context_systems_conversation.md` | 794 | Agent amnesia solutions, AGNOSTIC design |
| `agnostic_memory_system_research.md` | 161 | Initial memory system research |
| `agnostic_sync_system_design.md` | 140 | Sync script design |
| `claude_code_memory_gap_analysis.md` | 127 | Gap analysis |
| `why_claude_code_lacks_memory_research.md` | 181 | Why Claude Code is designed stateless |
| `memory_system_recommendation.md` | 190 | Hybrid approach recommendation |
| `system_comparison_and_recommendations.md` | 258 | Your system vs SHIMI |
| `multi_agent_parallel_execution_insight.md` | 265 | Multi-agent implications |
| `shimi_framework_research.md` | ~200 | SHIMI framework details |
| `automated_traversal_for_your_system.md` | ~150 | Discovery tooling |
| `existing_solutions.md` | ~100 | Existing solution survey |
| `proposal_ai_friendly_output_organization.md` | ~430 | PROPOSAL v1 - ⚠️ Superseded |
| `proposal_ai_friendly_output_organization_v2.md` | ~755 | PROPOSAL v2 - ⚠️ Superseded |
| `proposal_ai_friendly_output_organization_v3.md` | ~900+ | PROPOSAL v3 - ⚠️ Superseded |
| `proposal_ai_friendly_output_organization_v4.md` | ~600+ | **PROPOSAL v4** - Complete architecture with inventory, diagrams, 8-phase plan |

### Finished Understanding
| File | Lines | Topic |
|------|-------|-------|
| `system_prompt_architecture.md` | 1086 | **APPROVED** - System prompt design |

### Root Outputs
| File | Lines | Topic |
|------|-------|-------|
| `agent_amnesia_external_approaches.md` | 672 | External framework research |

---

## Pointers to Key Decisions

| Decision | Location | Status |
|----------|----------|--------|
| Container-as-Manager pattern | `system_prompt_architecture.md` | APPROVED |
| Identity/Triggers/Pointers format | `agent_amnesia_and_context_systems_conversation.md` | Proposed |
| Three-tier folder architecture | `layer_stage_instantiation_understanding.md` | Proposed |
| Tool rankings | `layer_stage_instantiation_understanding.md` | Documented |
| Hybrid memory approach | `memory_system_recommendation.md` | Recommended |

---

## Session Continuity

When starting a new session on this research:

1. **Read this synthesis first** - Get the overview
2. **Check episodic/index.md** - See what happened in recent sessions
3. **Identify your focus area** - Use triggers table above
4. **Read relevant source files** - Deep dive as needed
5. **Update this synthesis** - Add new findings

---

*Last updated: 2026-02-02*
*Total research files: 31*
*Ready for instructions: 1 (system_prompt_architecture.md)*
