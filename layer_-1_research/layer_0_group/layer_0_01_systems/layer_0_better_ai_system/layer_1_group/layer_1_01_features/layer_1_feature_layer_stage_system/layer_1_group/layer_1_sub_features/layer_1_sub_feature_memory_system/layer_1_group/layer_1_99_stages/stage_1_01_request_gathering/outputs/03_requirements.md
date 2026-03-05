---
resource_id: "1f373fd2-184d-4761-96c3-9c5516edf43e"
resource_type: "output"
resource_name: "03_requirements"
---
# Requirements: What the Memory System Must Do

<!-- section_id: "934b577a-39b9-4133-97ba-757f6c59b9de" -->
## Requirement Categories

Requirements organized by priority: MUST (non-negotiable), SHOULD (important), COULD (nice-to-have).

---

<!-- section_id: "127fd4c5-846b-4a89-b6f7-09faa592fcf2" -->
## MUST Requirements

<!-- section_id: "73581a09-9d6b-4713-b5ce-267a78ca9438" -->
### M1: Tool-Agnostic Memory Storage
The memory system MUST store memories in formats readable by ANY AI tool — not just Claude Code. The agnostic system (`0AGNOSTIC.md`, `.0agnostic/`) already establishes this principle. Memory must follow it.

**Rationale**: The layer-stage framework is used across Claude Code, Cursor, Gemini, and potentially more tools. Tool-specific memory (like `~/.claude/` auto-memory) creates silos.

**Acceptance criteria**:
- Memory files use universal formats (Markdown, JSON, JSON-LD)
- No dependency on any single tool's native memory API
- Any AI tool can read and contribute to the shared memory

<!-- section_id: "3446bf9c-b25e-4b6b-98c4-0029947b35e7" -->
### M2: Hierarchical Memory Aligned with Layer-Stage Structure
Memory MUST respect the existing hierarchy: layers (0, 1, -1), stages (01-11), entities, sub-features. Memory scoped to an entity should be accessible from that entity and its descendants.

**Rationale**: The framework IS hierarchical. Memory that ignores this structure creates confusion about where to store and find things.

**Acceptance criteria**:
- Memory can be scoped to any level (universal, project, feature, sub-feature, stage)
- Child entities inherit parent memory
- Entity-scoped memory is discoverable through normal navigation

<!-- section_id: "f2ddfd0e-83a6-4f09-b599-467f77220cf3" -->
### M3: Cross-Session Persistence
Memory MUST persist across sessions. Key learnings, decisions, and context from one session must be available in the next.

**Rationale**: This is the fundamental point — without persistence, every session starts cold.

**Acceptance criteria**:
- Memories survive session boundaries
- Git-tracked for version history and sync
- Retrievable without knowing the exact session that created them

<!-- section_id: "53d0689b-7aef-4535-9256-a68ca767599b" -->
### M4: Automated Episodic Recording
The system MUST automatically capture significant session events without requiring manual discipline.

**Rationale**: The current episodic memory structure exists but is empty because it relies on manual creation. If it's not automatic, it won't happen.

**Acceptance criteria**:
- Significant work triggers automatic session recording
- Records include: date, what was done, files changed, decisions made
- Stored in the entity's episodic memory location

<!-- section_id: "37957f71-245a-4b7f-99c3-d6b0fafe80e6" -->
### M5: Efficient Context Loading
Memory retrieval MUST NOT overload the context window. The system must be selective about what it loads.

**Rationale**: Current CLAUDE.md chain loads everything in the ancestor path regardless of relevance. With deep hierarchies, this wastes significant tokens.

**Acceptance criteria**:
- Only task-relevant memory loaded into context
- Context budget respected (memory doesn't crowd out reasoning space)
- Static memory footprint bounded and predictable

<!-- section_id: "c7924e3f-c4a2-4c9c-9946-2ae99cbe0c61" -->
### M6: Backward Compatibility
The new memory system MUST NOT break existing mechanisms. CLAUDE.md chain, auto-memory, and agnostic system must continue to work.

**Rationale**: The existing system is functional and relied upon. We're enhancing, not replacing.

**Acceptance criteria**:
- Existing CLAUDE.md chain loading unchanged
- Auto-memory continues to function
- `0AGNOSTIC.md` → `agnostic-sync.sh` workflow preserved
- No existing files need to be restructured

---

<!-- section_id: "2971abc3-782a-4d95-8479-07b85be2506b" -->
## SHOULD Requirements

<!-- section_id: "4987e40f-ff9c-4dc6-8eb6-4ec2bee98a36" -->
### S1: Cross-Project Knowledge Transfer
Memory SHOULD enable learnings from one project/entity to benefit others where relevant.

**Rationale**: Currently, learning about debugging in one project doesn't help with debugging in another. Universal learnings should propagate upward.

**Acceptance criteria**:
- Mechanism for promoting entity-specific learnings to universal (layer 0) memory
- Cross-entity search capability
- Clear distinction between entity-specific and universal memories

<!-- section_id: "8b31e665-b43a-4d81-982d-325f8cc2106e" -->
### S2: Temporal Reasoning
The system SHOULD support time-based queries: "What were we working on last week?", "When did we make this decision?", "What changed since the last session?"

**Rationale**: Temporal context is critical for resuming work, understanding history, and tracking progress.

**Acceptance criteria**:
- All memories timestamped
- Temporal queries supported (date ranges, "most recent", "since last session")
- Session timeline reconstructable

<!-- section_id: "b490cb4f-d217-4d40-8824-e0964b745710" -->
### S3: Memory Consolidation and Decay
The system SHOULD consolidate verbose memories into summaries over time and allow low-value memories to fade.

**Rationale**: Without consolidation, memory grows indefinitely. Without decay, stale information pollutes retrieval.

**Acceptance criteria**:
- Old, detailed memories summarized into compact forms
- Importance-based retention (high-value memories kept, low-value decay)
- Configurable retention policies per scope/type

<!-- section_id: "f8ee1064-6075-41bd-85e9-a7fd0ead57e8" -->
### S4: Structured + Unstructured Memory
The system SHOULD support both free-form notes AND structured data (entities, relationships, facts).

**Rationale**: Some knowledge is best as prose (reflections, context), other knowledge as structured facts (entity attributes, decision records).

**Acceptance criteria**:
- Support for Markdown prose (human-readable)
- Support for structured JSON/JSON-LD (machine-queryable)
- Both types coexist and complement each other

<!-- section_id: "ee6e3f43-8277-4802-9c44-9b1d821361b7" -->
### S5: Memory Quality Monitoring
The system SHOULD provide visibility into memory health: what's stored, how much, how stale, what's missing.

**Rationale**: Without observability, memory systems silently degrade.

**Acceptance criteria**:
- Memory inventory per scope (count, size, age distribution)
- Staleness detection (memories not accessed or updated recently)
- Contradiction detection (conflicting facts)

<!-- section_id: "ec37d345-8be5-4911-b11a-11ffe0770cf9" -->
### S6: Multi-Agent Memory Coordination
The system SHOULD support multiple agents reading from and writing to shared memory with appropriate access controls.

**Rationale**: Team workflows involve multiple agents (leader + teammates) who need shared context.

**Acceptance criteria**:
- Multiple agents can read shared memory simultaneously
- Write coordination (no silent overwrites)
- Role-based visibility where appropriate

---

<!-- section_id: "f7277c53-799a-4003-b512-30dc00435626" -->
## COULD Requirements

<!-- section_id: "beed855e-81e3-4a2f-a8dd-cb9c4d160b62" -->
### C1: Semantic Search Over Memory
The system COULD support embedding-based semantic search for finding relevant memories by meaning rather than keyword.

**Rationale**: As memory grows, keyword search becomes insufficient. Semantic search finds conceptually related memories.

<!-- section_id: "53c49196-3d14-4e82-b75d-8113b4535d6f" -->
### C2: Automated Stage Transitions
The system COULD automatically detect when work has progressed beyond the current stage and suggest transitions.

**Rationale**: status.json is often stale because transitions are manual.

<!-- section_id: "50382094-542c-42ca-8b93-d1c41511439a" -->
### C3: Memory Visualization
The system COULD provide visual representations of the memory state — what's loaded, what's available, how it's connected.

**Rationale**: Debugging memory systems requires understanding what the agent "knows" at any given moment.

<!-- section_id: "0f03bbb4-0605-4aca-bb16-ea1c28ec7b06" -->
### C4: External Memory Integration
The system COULD integrate with external memory platforms (Mem0, vector stores) while maintaining tool-agnostic core.

**Rationale**: Production deployments may need scalability beyond flat files.

<!-- section_id: "280489db-5b7c-4c31-b8a7-70e2867263d3" -->
### C5: Memory Templates
The system COULD provide templates for common memory types (decision records, session summaries, entity profiles) to ensure consistency.

**Rationale**: Structured templates reduce the cognitive load of recording memories correctly.

---

<!-- section_id: "18f0ce9f-c42a-42cb-b5c2-4840be787c9a" -->
## Non-Requirements (Explicitly Out of Scope)

<!-- section_id: "4cc8bdc9-440d-414a-8660-9e2c2dd3eaf3" -->
### NR1: Real-Time Streaming Memory
We are NOT building a real-time memory sync system. Batch/session-level updates are sufficient.

<!-- section_id: "9fe0c7ff-9c76-4512-80ef-4e75d9ef65bc" -->
### NR2: Parametric Memory Modification
We are NOT fine-tuning models or modifying model weights. Our memory is entirely token-level (external).

<!-- section_id: "77cf6e97-fe00-423c-8361-be0a6f57d4f3" -->
### NR3: Building a Memory Platform
We are NOT building a standalone memory platform like Mem0 or Zep. We're designing a memory architecture FOR the layer-stage framework.

<!-- section_id: "a2826f8c-87d1-4777-9add-26a169d27b7a" -->
### NR4: Replacing Claude Code's Native Memory
We are NOT replacing `~/.claude/` auto-memory. We're building a complementary tool-agnostic layer.
