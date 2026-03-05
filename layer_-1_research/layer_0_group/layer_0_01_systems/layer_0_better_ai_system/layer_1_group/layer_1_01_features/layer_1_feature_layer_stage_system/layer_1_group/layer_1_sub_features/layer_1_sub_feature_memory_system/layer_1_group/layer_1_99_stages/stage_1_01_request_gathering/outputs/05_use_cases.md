---
resource_id: "f7ee6e1b-d8f8-4a6d-b7e6-171b81b4534d"
resource_type: "output"
resource_name: "05_use_cases"
---
# Use Cases: How the Memory System Will Be Used

<!-- section_id: "0a7036ec-3943-413a-9b8f-d068f489b367" -->
## Overview

Concrete scenarios that the memory system must support, organized by the three child sub-features (context chain, dynamic memory, navigation) plus cross-cutting concerns.

---

<!-- section_id: "930a9c90-b330-4073-8706-930b1516c7a4" -->
## Context Chain Use Cases

<!-- section_id: "9463b7b6-bb9e-474e-930a-3d6b52ee88b4" -->
### UC-CC1: Session Start Context Loading
**Actor**: AI agent starting a new session
**Trigger**: User launches Claude Code (or any tool) in a project directory
**Flow**:
1. Agent reads CLAUDE.md chain from root to cwd (existing behavior)
2. Agent reads entity's status.json to know current stage
3. Agent reads recent episodic memory to understand what happened last session
4. Agent loads relevant entity-scoped memories for current task
5. Agent is ready to work with full context

**Current gap**: Steps 3-4 are manual or missing

<!-- section_id: "3eee5289-6446-4b03-9327-bf30835301d4" -->
### UC-CC2: Cross-Entity Context Discovery
**Actor**: AI agent working on a sub-feature
**Trigger**: Agent needs context from a sibling entity (e.g., working on `dynamic_memory` but needs info from `context_chain_system`)
**Flow**:
1. Agent recognizes it needs related context
2. Agent discovers sibling entities through parent's children list
3. Agent reads relevant sibling's memory/outputs
4. Agent integrates cross-entity context without losing current scope

**Current gap**: No mechanism for sibling discovery beyond manual navigation

<!-- section_id: "bce0503b-bf99-4f80-b754-fbec79349bf0" -->
### UC-CC3: Relevance-Based Context Filtering
**Actor**: AI agent with deep hierarchy path
**Trigger**: Loading full CLAUDE.md chain would consume too many tokens
**Flow**:
1. Agent assesses current task requirements
2. Agent loads minimal mandatory context (identity, critical rules)
3. Agent defers loading of non-essential ancestor context
4. Agent loads specific context on-demand as task requires it

**Current gap**: No relevance assessment — everything in path is loaded

---

<!-- section_id: "2413d6fe-e64c-49ab-b056-e6d9904cb4bf" -->
## Dynamic Memory Use Cases

<!-- section_id: "ffbb1c0e-2721-4768-b253-ecfc4bf50ab1" -->
### UC-DM1: Automatic Session Recording
**Actor**: AI agent completing significant work
**Trigger**: End of session or significant milestone within session
**Flow**:
1. Agent detects significant work was done (files created/edited, decisions made)
2. Agent generates session summary (date, what was done, files changed, decisions, open questions)
3. Agent stores summary in entity's episodic memory location
4. Agent updates entity's status.json if stage progress changed

**Current gap**: This is entirely manual today

<!-- section_id: "769f7a84-de0d-4d7b-8745-e783b181f151" -->
### UC-DM2: Resume Previous Work
**Actor**: AI agent starting a session on previously-worked-on entity
**Trigger**: User says "continue where we left off" or similar
**Flow**:
1. Agent reads entity's episodic memory index
2. Agent finds most recent session record
3. Agent loads session context: what was done, what's pending, what decisions were made
4. Agent resumes work from that point without user re-explaining

**Current gap**: Episodic memory is empty, so there's nothing to resume from

<!-- section_id: "da93df70-19f6-46b2-8bb1-8fccdb194935" -->
### UC-DM3: Learning Capture and Propagation
**Actor**: AI agent that discovers a reusable insight
**Trigger**: Agent encounters a gotcha, best practice, or pattern worth remembering
**Flow**:
1. Agent recognizes the insight is reusable (not just task-specific)
2. Agent stores insight in entity-scoped memory
3. If insight is universal, agent promotes it to layer 0 memory
4. Future sessions in any related entity can access the insight

**Current gap**: Insights are lost between sessions or siloed in auto-memory

<!-- section_id: "503b20ac-88fd-49e0-b5b9-4c16618df388" -->
### UC-DM4: Decision Recording
**Actor**: AI agent or user making an architectural/design decision
**Trigger**: A choice is made between alternatives with lasting implications
**Flow**:
1. Decision is identified (what was decided, what alternatives existed, why this choice)
2. Decision recorded with context, rationale, and date
3. Decision linked to the entity/stage where it applies
4. Future work can reference the decision without re-debating

**Current gap**: Decisions are sometimes captured in outputs but not systematically

<!-- section_id: "a0bb79c8-43bd-4187-8e94-1730b7496160" -->
### UC-DM5: Memory Consolidation
**Actor**: System (automated or manually triggered)
**Trigger**: Entity's memory has grown large, or periodic maintenance
**Flow**:
1. Review accumulated session records and learnings
2. Consolidate redundant entries (merge duplicates)
3. Summarize detailed records into compact forms
4. Archive or decay low-value memories
5. Update memory index

**Current gap**: No consolidation mechanism exists

---

<!-- section_id: "1c66d60c-081c-409a-93c8-79722e44001e" -->
## Navigation Use Cases

<!-- section_id: "e980daca-55c8-4408-bb22-e51ca3e77b2f" -->
### UC-NAV1: "Where Am I?" Context Orientation
**Actor**: AI agent entering a new directory
**Trigger**: User navigates to unfamiliar part of the hierarchy
**Flow**:
1. Agent reads local 0AGNOSTIC.md / CLAUDE.md
2. Agent identifies: layer, entity type, current stage, parent, children
3. Agent presents orientation summary to user
4. Agent loads appropriate context for this location

**Current behavior**: Context traversal rule handles this, but agent doesn't always proactively orient

<!-- section_id: "6a477e3d-9b94-4112-9b91-defe4db39915" -->
### UC-NAV2: "What Else Is Related?" Exploration
**Actor**: User or agent wanting to understand scope
**Trigger**: Exploring what exists in the framework
**Flow**:
1. Agent reads parent entity's children list
2. Agent summarizes sibling entities and their purposes
3. Agent identifies which entities are most relevant to current task
4. Agent can navigate to any entity and load its context

**Current gap**: No systematic exploration capability

<!-- section_id: "e64dfa72-81d0-4d72-8227-92788cf532ee" -->
### UC-NAV3: "What Have We Done?" History Query
**Actor**: User wanting to understand project history
**Trigger**: "What did we work on last week?" or "What's the status of feature X?"
**Flow**:
1. Agent queries episodic memory across relevant entities
2. Agent filters by time range
3. Agent synthesizes timeline of recent work
4. Agent identifies current status and pending items

**Current gap**: Episodic memory is empty; no temporal query capability

---

<!-- section_id: "dfc87c4e-59db-4e72-8d53-db79bd6e4f5f" -->
## Cross-Cutting Use Cases

<!-- section_id: "685d1764-279e-4eb7-bcbe-d8e7ee165e94" -->
### UC-XC1: Multi-Tool Memory Access
**Actor**: User switching between AI tools (Claude Code → Cursor → Gemini)
**Trigger**: User works on same entity with different tools
**Flow**:
1. Tool A writes memories in agnostic format
2. User switches to Tool B
3. Tool B reads same agnostic memory files
4. Tool B has access to everything Tool A learned
5. Tool B can contribute its own learnings back

**Current gap**: Only `0AGNOSTIC.md` is truly tool-agnostic; memory files are tool-specific

<!-- section_id: "c66d3697-17db-458e-b777-4ad9a3b8939d" -->
### UC-XC2: Multi-Agent Collaboration
**Actor**: Team of AI agents working on related tasks
**Trigger**: User launches parallel agents (Claude Code team workflows)
**Flow**:
1. Leader creates shared task list
2. Each agent accesses shared entity memory
3. Agents record their work to shared memory
4. Agents can read each other's contributions
5. No conflicts from simultaneous access

**Current gap**: No shared memory protocol for multi-agent scenarios

<!-- section_id: "8b904080-27be-43e3-b6d5-2ad659d1e090" -->
### UC-XC3: Memory Health Check
**Actor**: User or automated maintenance
**Trigger**: Periodic or on-demand review
**Flow**:
1. Scan all entity memory locations
2. Report: total memories, staleness, gaps (empty episodic dirs), contradictions
3. Recommend: consolidation targets, empty spots to fill, stale entries to update
4. Execute approved maintenance actions

**Current gap**: No health monitoring exists
