---
resource_id: "e9f0a1b2-c3d4-4e5f-6a7b-8c9d0e1f2a3b"
resource_type: "output"
resource_name: "operations_and_interface_design"
---
# Operations & Interface Design

> **Date**: 2026-03-07
> **Purpose**: Inventory of all system operations, categorized by automation level, with agent-friendly interface design for each

<!-- section_id: "f0a1b2c3-d4e5-4f6a-7b8c-9d0e1f2a3b4c" -->
## 1. Automation Decision Framework

Every operation falls into one of three categories:

| Category | When to Use | Agent Involvement | Mechanism |
|----------|-------------|-------------------|-----------|
| **A: Fully Automated** | Deterministic, no judgment needed, triggered by events | None — runs without agent | Shell scripts, git hooks, file watchers |
| **B: Agent-Assisted** | Requires search, discovery, context understanding, or creative decisions | Agent performs the operation | Flat files (TSV), structured files (JSON), documentation |
| **C: Hybrid** | Automated trigger, but agent needs to see or act on results | Agent receives results passively | Hooks inject context; agent decides whether to act |

**Decision criteria**:
- Can the operation produce a correct result 100% of the time without judgment? → **Category A**
- Does the operation require understanding context, making choices, or interpreting results? → **Category B**
- Is there an automated trigger point, but the agent still needs to be aware? → **Category C**

<!-- section_id: "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d" -->
## 2. Complete Operations Inventory

### Category A: Fully Automated (No Agent)

| # | Operation | Trigger | Mechanism | Status |
|---|-----------|---------|-----------|--------|
| A1 | Rebuild UUID index (.uuid-index.json) | `pointer-sync.sh --rebuild-index` | Scan all files for resource_id/entity_id headers | Implemented |
| A2 | Rebuild entity lookup TSV | Part of A1 | Generated from UUID index data | Implemented |
| A3 | Validate all pointers | `pointer-sync.sh --validate` | Check each pointer's target exists, exit 0/1 | Implemented |
| A4 | Validate pointers after agnostic-sync | End of agnostic-sync.sh run | Inline call to pointer-sync.sh --validate | Implemented |
| A5 | Resolve {{resolve:UUID}} placeholders | agnostic-sync.sh generation | String replacement during CLAUDE.md generation | Implemented (runtime mode) |
| A6 | Assign UUIDs to new files | assign-file-uuids.sh | Scan for missing resource_id, add UUID4 header | Implemented |
| A7 | Assign UUIDs to new entities | assign-entity-uuids.sh | Scan for missing entity_id, add UUID4 | Implemented |
| A8 | Generate per-entity resource indexes | create-resource-indexes.sh | Scan entity .0agnostic/, write resource_index.json | Implemented |
| A9 | Detect renames/moves on git operations | post-checkout / post-merge hooks | Compare old vs new paths in git diff | Not yet |
| A10 | Auto-rebuild index on git operations | post-checkout / post-merge hooks | Run pointer-sync.sh --rebuild-index | Not yet |
| A11 | Pre-commit pointer validation | pre-commit hook | pointer-sync.sh --validate, block if exit 1 | Not yet (hook exists but optional) |
| A12 | Incremental index rebuild | pointer-sync.sh (future flag) | Rebuild only entries for changed files | Not yet |

### Category B: Agent-Assisted (Agent Does It, System Provides Interface)

| # | Operation | Agent's Tool | Interface | Token Cost | Status |
|---|-----------|-------------|-----------|------------|--------|
| B1 | Find entities by name/keyword | Grep | `.entity-lookup.tsv` | ~80-530 tokens | Implemented |
| B2 | Resolve UUID to current path | Grep or Read | `.entity-lookup.tsv` or `.uuid-index.json` | ~80-530 or ~2000+ tokens | Implemented |
| B3 | Navigate parent/child hierarchy | Grep | `.entity-lookup.tsv` (4th column = parent_UUID) | ~80-530 tokens | Implemented |
| B4 | Create new pointer files | Write | Frontmatter template (documented in REQ-01) | ~200 tokens | Implemented |
| B5 | Edit existing pointer files | Edit | Direct file editing | ~100 tokens | Implemented |
| B6 | Look up resource metadata | Read | Per-entity `resource_index.json` | ~200-1000 tokens | Implemented |
| B7 | Query entities by type/filter | Grep | `.entity-lookup.tsv` with regex patterns | ~80-530 tokens | Partial |
| B8 | Find all children of an entity | Grep | `.entity-lookup.tsv` (grep parent_UUID column) | ~80-530 tokens | Implemented |
| B9 | Trace full parent chain to root | Grep (repeated) | `.entity-lookup.tsv` (follow parent_UUID up) | ~400-2000 tokens | Implemented |

### Category C: Hybrid (Automated Trigger, Agent Sees Results)

| # | Operation | Trigger | Automated Part | Agent Sees |
|---|-----------|---------|---------------|------------|
| C1 | Entity search hint | Glob/Grep matching entity patterns | PostToolUse hook fires | "TIP: Grep .entity-lookup.tsv for UUIDs" |
| C2 | Pointer edit reminder | Edit/Write on pointer files | PostToolUse hook fires | "Remember to validate pointers" |
| C3 | Stale pointer report | pointer-sync.sh --validate | Script identifies broken pointers | List of broken pointers with fix suggestions |
| C4 | Move impact summary | After git merge/checkout (future) | Script detects moved entities | "N entities moved, index rebuilt" |

<!-- section_id: "b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e" -->
## 3. Agent Interface Design Principles

Based on research (see `stage_3_02_research/outputs/agent_tool_preferences_research.md`):

### Principle 1: Match the Agent's Preferred Tools

Agents prefer (in order): Read > Glob > Grep > Edit > Write > Bash.
Design interfaces using the top 3 tools. Never require Bash as the primary interface.

### Principle 2: Flat Files for Queries, Structured Files for Detail

- **Queries** (search, filter, find): Use TSV — one result per line, Grep-compatible
- **Detail lookups** (full metadata, parent chains): Use JSON — Read tool, parse mentally
- **Never**: Require the agent to run a script and parse stdout

### Principle 3: One Tool Call = One Complete Answer

The agent should get everything it needs in a single Grep or Read call. No multi-step workflows that require the agent to chain 3-4 tool calls to get a simple answer.

### Principle 4: Passive Guidance Over Active Blocking

Use PostToolUse hooks to suggest better approaches (low friction, agent can ignore).
Reserve PreToolUse blocking for critical safety checks only (e.g., preventing writes to generated files).

### Principle 5: Token Efficiency

Every interface has a token budget. Prefer TSV (~80-530 tokens per query) over JSON (~2000+ tokens for full file read). Keep instruction overhead under 10 instructions (~5% of the 150-instruction budget).

<!-- section_id: "c3d4e5f6-a7b8-4c9d-0e1f-2a3b4c5d6e7f" -->
## 4. Interface Mapping

| Agent Need | Recommended Interface | Tool | Example |
|------------|----------------------|------|---------|
| "Where is the memory system?" | `.entity-lookup.tsv` | Grep | `Grep pattern="memory_system" path=".entity-lookup.tsv"` |
| "What's the UUID of pointer_system?" | `.entity-lookup.tsv` | Grep | `Grep pattern="pointer_system" path=".entity-lookup.tsv"` (2nd column) |
| "What does UUID abc123 point to?" | `.entity-lookup.tsv` | Grep | `Grep pattern="abc123" path=".entity-lookup.tsv"` (3rd column) |
| "What are the children of entity X?" | `.entity-lookup.tsv` | Grep | `Grep pattern="<parent_UUID>" path=".entity-lookup.tsv"` (4th column matches) |
| "What resources does entity X have?" | `resource_index.json` | Read | `Read <entity>/.0agnostic/resource_index.json` |
| "Full metadata for UUID abc123" | `.uuid-index.json` | Read | `Read .uuid-index.json` then find `.uuids["abc123"]` |
| "Create a pointer to entity Y" | Frontmatter template | Write | Agent writes file with `pointer_to:` frontmatter |
| "Is my pointer valid?" | N/A (automated) | — | PostToolUse hook reminds; agent runs `pointer-sync.sh --validate` via Bash |

<!-- section_id: "d4e5f6a7-b8c9-4d0e-1f2a-3b4c5d6e7f8a" -->
## 5. Open Operations — Recommended Approach

| Operation | Recommended Category | Rationale |
|-----------|---------------------|-----------|
| Detect renames on git operations (A9) | **A: Fully Automated** | Git hooks are deterministic; compare old/new paths from git diff |
| Auto-rebuild on git operations (A10) | **A: Fully Automated** | No judgment needed; always rebuild after structural changes |
| Pre-commit validation (A11) | **A: Fully Automated** | Binary pass/fail; block commit if broken |
| Incremental index rebuild (A12) | **A: Fully Automated** | Optimization of A1; only scan changed files |
| Fuzzy/short-name entity search | **B: Agent-Assisted** | Agent already uses Grep with regex; partial matching is natural |
| Auto-UUID on entity creation | **A: Fully Automated** | Entity creation skill can call assign-entity-uuids.sh automatically |
| Move impact notification (C4) | **C: Hybrid** | Automated detection, but agent should know what changed |

<!-- section_id: "e5f6a7b8-c9d0-4e1f-2a3b-4c5d6e7f8a9b" -->
## 6. Relationship to Tree of Needs

| Tree Branch | Primary Operations | Category |
|-------------|-------------------|----------|
| 01: Pointer Format | B4 (create), B5 (edit) | B: Agent-Assisted |
| 02: Path Resolution | B1 (find), A1/A2 (rebuild index), B2 (resolve UUID) | Mixed A+B |
| 03: Trigger Automation | C1/C2 (hooks), A3/A4 (validation), A9/A10 (git hooks) | Mixed A+C |
| 04: UUID Graph Traversal | B3 (hierarchy), B8/B9 (parent/child), B6 (metadata) | B: Agent-Assisted |
| 05: UUID Reference Resolution | A5 (resolve placeholders), A1 (rebuild index), B2 (UUID lookup) | Mixed A+B |
