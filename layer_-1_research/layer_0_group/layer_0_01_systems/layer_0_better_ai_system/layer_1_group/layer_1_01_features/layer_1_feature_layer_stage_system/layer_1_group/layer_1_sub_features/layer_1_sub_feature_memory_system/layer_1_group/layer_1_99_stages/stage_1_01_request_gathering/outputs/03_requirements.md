---
resource_id: "1f373fd2-184d-4761-96c3-9c5516edf43e"
resource_type: "output"
resource_name: "03_requirements"
---
# Requirements: What the Memory System Must Do

## Requirement Categories

Requirements organized by priority: MUST (non-negotiable), SHOULD (important), COULD (nice-to-have).

---

## MUST Requirements

### M1: Tool-Agnostic Memory Storage
The memory system MUST store memories in formats readable by ANY AI tool — not just Claude Code. The agnostic system (`0AGNOSTIC.md`, `.0agnostic/`) already establishes this principle. Memory must follow it.

**Rationale**: The layer-stage framework is used across Claude Code, Cursor, Gemini, and potentially more tools. Tool-specific memory (like `~/.claude/` auto-memory) creates silos.

**Acceptance criteria**:
- Memory files use universal formats (Markdown, JSON, JSON-LD)
- No dependency on any single tool's native memory API
- Any AI tool can read and contribute to the shared memory

### M2: Hierarchical Memory Aligned with Layer-Stage Structure
Memory MUST respect the existing hierarchy: layers (0, 1, -1), stages (01-11), entities, sub-features. Memory scoped to an entity should be accessible from that entity and its descendants.

**Rationale**: The framework IS hierarchical. Memory that ignores this structure creates confusion about where to store and find things.

**Acceptance criteria**:
- Memory can be scoped to any level (universal, project, feature, sub-feature, stage)
- Child entities inherit parent memory
- Entity-scoped memory is discoverable through normal navigation

### M3: Cross-Session Persistence
Memory MUST persist across sessions. Key learnings, decisions, and context from one session must be available in the next.

**Rationale**: This is the fundamental point — without persistence, every session starts cold.

**Acceptance criteria**:
- Memories survive session boundaries
- Git-tracked for version history and sync
- Retrievable without knowing the exact session that created them

### M4: Automated Episodic Recording
The system MUST automatically capture significant session events without requiring manual discipline.

**Rationale**: The current episodic memory structure exists but is empty because it relies on manual creation. If it's not automatic, it won't happen.

**Acceptance criteria**:
- Significant work triggers automatic session recording
- Records include: date, what was done, files changed, decisions made
- Stored in the entity's episodic memory location

### M5: Efficient Context Loading
Memory retrieval MUST NOT overload the context window. The system must be selective about what it loads.

**Rationale**: Current CLAUDE.md chain loads everything in the ancestor path regardless of relevance. With deep hierarchies, this wastes significant tokens.

**Acceptance criteria**:
- Only task-relevant memory loaded into context
- Context budget respected (memory doesn't crowd out reasoning space)
- Static memory footprint bounded and predictable

### M6: Backward Compatibility
The new memory system MUST NOT break existing mechanisms. CLAUDE.md chain, auto-memory, and agnostic system must continue to work.

**Rationale**: The existing system is functional and relied upon. We're enhancing, not replacing.

**Acceptance criteria**:
- Existing CLAUDE.md chain loading unchanged
- Auto-memory continues to function
- `0AGNOSTIC.md` → `agnostic-sync.sh` workflow preserved
- No existing files need to be restructured

---

## SHOULD Requirements

### S1: Cross-Project Knowledge Transfer
Memory SHOULD enable learnings from one project/entity to benefit others where relevant.

**Rationale**: Currently, learning about debugging in one project doesn't help with debugging in another. Universal learnings should propagate upward.

**Acceptance criteria**:
- Mechanism for promoting entity-specific learnings to universal (layer 0) memory
- Cross-entity search capability
- Clear distinction between entity-specific and universal memories

### S2: Temporal Reasoning
The system SHOULD support time-based queries: "What were we working on last week?", "When did we make this decision?", "What changed since the last session?"

**Rationale**: Temporal context is critical for resuming work, understanding history, and tracking progress.

**Acceptance criteria**:
- All memories timestamped
- Temporal queries supported (date ranges, "most recent", "since last session")
- Session timeline reconstructable

### S3: Memory Consolidation and Decay
The system SHOULD consolidate verbose memories into summaries over time and allow low-value memories to fade.

**Rationale**: Without consolidation, memory grows indefinitely. Without decay, stale information pollutes retrieval.

**Acceptance criteria**:
- Old, detailed memories summarized into compact forms
- Importance-based retention (high-value memories kept, low-value decay)
- Configurable retention policies per scope/type

### S4: Structured + Unstructured Memory
The system SHOULD support both free-form notes AND structured data (entities, relationships, facts).

**Rationale**: Some knowledge is best as prose (reflections, context), other knowledge as structured facts (entity attributes, decision records).

**Acceptance criteria**:
- Support for Markdown prose (human-readable)
- Support for structured JSON/JSON-LD (machine-queryable)
- Both types coexist and complement each other

### S5: Memory Quality Monitoring
The system SHOULD provide visibility into memory health: what's stored, how much, how stale, what's missing.

**Rationale**: Without observability, memory systems silently degrade.

**Acceptance criteria**:
- Memory inventory per scope (count, size, age distribution)
- Staleness detection (memories not accessed or updated recently)
- Contradiction detection (conflicting facts)

### S6: Multi-Agent Memory Coordination
The system SHOULD support multiple agents reading from and writing to shared memory with appropriate access controls.

**Rationale**: Team workflows involve multiple agents (leader + teammates) who need shared context.

**Acceptance criteria**:
- Multiple agents can read shared memory simultaneously
- Write coordination (no silent overwrites)
- Role-based visibility where appropriate

---

## COULD Requirements

### C1: Semantic Search Over Memory
The system COULD support embedding-based semantic search for finding relevant memories by meaning rather than keyword.

**Rationale**: As memory grows, keyword search becomes insufficient. Semantic search finds conceptually related memories.

### C2: Automated Stage Transitions
The system COULD automatically detect when work has progressed beyond the current stage and suggest transitions.

**Rationale**: status.json is often stale because transitions are manual.

### C3: Memory Visualization
The system COULD provide visual representations of the memory state — what's loaded, what's available, how it's connected.

**Rationale**: Debugging memory systems requires understanding what the agent "knows" at any given moment.

### C4: External Memory Integration
The system COULD integrate with external memory platforms (Mem0, vector stores) while maintaining tool-agnostic core.

**Rationale**: Production deployments may need scalability beyond flat files.

### C5: Memory Templates
The system COULD provide templates for common memory types (decision records, session summaries, entity profiles) to ensure consistency.

**Rationale**: Structured templates reduce the cognitive load of recording memories correctly.

---

## Non-Requirements (Explicitly Out of Scope)

### NR1: Real-Time Streaming Memory
We are NOT building a real-time memory sync system. Batch/session-level updates are sufficient.

### NR2: Parametric Memory Modification
We are NOT fine-tuning models or modifying model weights. Our memory is entirely token-level (external).

### NR3: Building a Memory Platform
We are NOT building a standalone memory platform like Mem0 or Zep. We're designing a memory architecture FOR the layer-stage framework.

### NR4: Replacing Claude Code's Native Memory
We are NOT replacing `~/.claude/` auto-memory. We're building a complementary tool-agnostic layer.
