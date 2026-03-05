---
resource_id: "3355b0b4-2856-4243-8de9-bee3e587e2d9"
resource_type: "output"
resource_name: "04_constraints"
---
# Constraints: What Limits Our Design

<!-- section_id: "71cd1018-cc40-4479-8739-41e676456151" -->
## Hard Constraints (Cannot Be Changed)

<!-- section_id: "90e62871-a90c-4eb5-9bbd-0bc297d1150f" -->
### HC1: Context Window Limits
Every AI tool has a finite context window. Memory injected into context directly competes with the agent's reasoning space.

| Tool | Context Window | Implication |
|------|---------------|-------------|
| Claude Code (Opus) | ~200K tokens | Generous but still bounded; deep hierarchies can consume significant share |
| Claude Sonnet | ~200K tokens | Same model family limits |
| Gemini | ~1M tokens | More headroom but still finite |
| Cursor | Varies by model | Often smaller (128K or less) |

**Design impact**: Memory must be selective. Cannot dump everything into context. Need budgeting.

<!-- section_id: "e84881e2-41ed-473a-b766-72735d99155b" -->
### HC2: Token Cost
Every token loaded costs money. Memory that's always in context (static) costs more than memory loaded on-demand (dynamic).

**Design impact**: Prefer dynamic loading over static where possible. Keep static context lean (CLAUDE.md). Push detail into on-demand resources (.0agnostic/, episodic files).

<!-- section_id: "20314f9e-2803-491a-9b2e-4e1133c68ebd" -->
### HC3: Tool-Agnostic Requirement
The layer-stage framework serves multiple AI tools. Memory cannot depend on any single tool's native features.

**Design impact**:
- Cannot rely solely on `~/.claude/` auto-memory (Claude-specific)
- Cannot use tool-specific APIs for memory management
- Must use universal formats (Markdown, JSON, file system)
- CAN use tool-specific adapters that translate FROM the universal format

<!-- section_id: "93950199-b597-476a-9f68-766bb5ade024" -->
### HC4: Git-Based Persistence
The framework uses git for versioning and syncing. Memory must be git-friendly.

**Design impact**:
- Text-based formats preferred (Markdown, JSON) — not binary
- Files should be diffable and mergeable
- No large binary blobs (vector embeddings don't belong in git)
- Commit history IS a form of memory (when did what change)

<!-- section_id: "c9498702-7c43-4ad7-9009-eedf45829b63" -->
### HC5: Existing Infrastructure
The following exist and must be preserved:
- `0AGNOSTIC.md` → `agnostic-sync.sh` → `CLAUDE.md` pipeline
- `.0agnostic/` directory structure at each entity
- `layer_N_group/layer_N_99_stages/` stage structure
- Status.json stage tracking
- CLAUDE.md context chain loading

**Design impact**: Build ON TOP of these, don't replace them.

<!-- section_id: "0f4a5f27-3b1f-4297-97be-0d7e090385be" -->
### HC6: Human Readability
The primary user (Dawson) must be able to read, understand, and edit any memory file directly.

**Design impact**: No opaque formats. No encoded embeddings as primary storage. Markdown is the lingua franca.

---

<!-- section_id: "31c529f3-ba0a-4b51-b18d-3e5311048e46" -->
## Soft Constraints (Can Be Negotiated)

<!-- section_id: "a09ba584-a77d-44dd-8fd7-b8fc2a0e918f" -->
### SC1: Automation Level
How much memory management should be automatic vs. manual?

| Extreme | Pro | Con |
|---------|-----|-----|
| Fully manual | Full control, no surprises | Won't happen consistently |
| Fully automatic | Always works | May store wrong things, hard to debug |
| **Hybrid** (recommended) | **Best of both** | **Requires good defaults** |

<!-- section_id: "1eb0300f-ef48-48c3-bf9d-3f23c5c02114" -->
### SC2: Memory Granularity
How fine-grained should memories be?

| Level | Example | Trade-off |
|-------|---------|-----------|
| Per-message | Every agent message stored | High fidelity, high volume |
| Per-turn | Each user-agent exchange | Moderate, captures interaction |
| Per-session | Session summary | Compact, loses detail |
| Per-milestone | Only significant events | Very compact, may miss important context |

<!-- section_id: "41f87e62-943e-4d74-981e-fca4f986ee9b" -->
### SC3: Storage Location
Where does memory live in the file system?

| Option | Location | Pro | Con |
|--------|----------|-----|-----|
| In-entity | `<entity>/.0agnostic/memory/` | Hierarchical, scoped | Scattered |
| In-stage | `<stage>/outputs/memory/` | Stage-aligned | Deep paths |
| Centralized | `.0agnostic/memory/` | One place to look | Loses hierarchy |
| **Hybrid** | Entity-level + universal rollup | Both scoped and discoverable | Sync needed |

<!-- section_id: "d9c57f40-5d9b-4d75-b083-099f833ce527" -->
### SC4: Sync Frequency
How often should tool-specific memory sync with the agnostic layer?

| Frequency | Mechanism | Pro | Con |
|-----------|-----------|-----|-----|
| Real-time | Hooks/watchers | Always current | Complexity, performance |
| Per-session | End-of-session script | Predictable | Delays |
| Manual | Run sync command | Full control | Often forgotten |
| **Per-commit** | Git hook triggered | Natural cadence | Tied to git workflow |

---

<!-- section_id: "dfad5605-c36c-40df-9f3f-5e923d5240f0" -->
## Architectural Constraints from Research

From our stage 02 research, key lessons that constrain design:

<!-- section_id: "3eca18f0-9ea5-4a79-bcdf-8c0137d9f189" -->
### The Filesystem Baseline Lesson
Letta's benchmark showed a simple filesystem + good LLM scored 74% on LoCoMo, beating several specialized memory systems. **Implication**: Don't over-engineer. File-based memory with good retrieval may be sufficient.

<!-- section_id: "ec716f8d-7a71-495c-ad1d-c04a1eaa566c" -->
### The Context Window Growth Lesson
Gemini already has 1M tokens. Context windows are growing. **Implication**: Some "memory problems" may be solved by larger windows. Don't build complex retrieval for data that will fit in context soon.

<!-- section_id: "4c3b8266-f8cc-41bf-b482-6ad68893db6b" -->
### The Extraction Error Lesson
LLM-based extraction of facts/entities introduces errors that compound over time. **Implication**: Prefer human-readable, human-verifiable memory over opaque automated extraction. If automating, make it auditable.

<!-- section_id: "f8c83f23-b680-48ce-babd-3b358282f4b0" -->
### The Tool-Specific Trap Lesson
Every framework (LangChain, CrewAI, etc.) built memory their own way. Many are now deprecated or restructured. **Implication**: Build on universal primitives (files, git), not on any framework's memory API.
