---
resource_id: "c6d7e8f9-a0b1-4c2d-3e4f-5a6b7c8d9e0f"
resource_type: "output"
resource_name: "agent_friendly_interface_design"
---
# Agent-Friendly Interface Design

> **Date**: 2026-03-07
> **Scope**: How to design UUID/entity interfaces that AI agents actually use
> **Principle**: Work WITH agent preferences, not against them

<!-- section_id: "d7e8f9a0-b1c2-4d3e-4f5a-6b7c8d9e0f1a" -->
## 1. Design Philosophy

**The core insight**: AI agents have built-in tool preferences enforced by their system prompt. These preferences are:
1. Hardcoded at the system prompt level (highest priority)
2. Consistent across models (Opus, Sonnet, Haiku all prefer native tools)
3. Resistant to override (MANDATORY/MUST language in user instructions doesn't reliably override system prompt)

**Design principle**: Make the agent's preferred tool also the correct tool. Don't create a better hammer and ask the agent to stop using the existing one — put the nails where the existing hammer can reach them.

<!-- section_id: "e8f9a0b1-c2d3-4e4f-5a6b-7c8d9e0f1a2b" -->
## 2. Interface Preference Ladder

Five tiers of interface design, ranked by agent compliance:

| Tier | Interface | Agent Tool | Compliance | Token Cost | Agent Effort |
|------|-----------|-----------|------------|------------|-------------|
| **T1** | `.entity-lookup.tsv` | Grep | ~97% | 1 call, <500 tokens | Zero — uses preferred tool |
| **T2** | `.uuid-index.json` | Read + jq mental parsing | ~85% | 1-2 calls, 500-2000 tokens | Low — familiar JSON |
| **T3** | PostToolUse hooks | Auto-injected | Passive (~40% follow-through) | 0 calls (injected) | Zero — but optional |
| **T4** | PreToolUse hooks | Forced redirect | ~95% (forced) | 0 calls (blocked) | Zero — but disruptive |
| **T5** | Bash scripts (entity-find.sh) | Bash | ~20% | 1+ calls, variable | High — unfamiliar tool |

### Why Each Tier Works (or Doesn't)

**T1 — Grep on TSV**: Agent already prefers Grep over grep. A flat TSV file is the simplest possible Grep target. One line per entity, tab-separated columns. The agent sees it as "just another Grep search" — zero cognitive overhead.

**T2 — Read JSON**: Agent knows how to Read files and parse JSON mentally. Useful for detailed lookups (parent chains, metadata). More data than TSV but requires the agent to find the right key.

**T3 — PostToolUse hooks**: Fire after the agent already did its search. Inject a tip like "TIP: For entity discovery, Grep .entity-lookup.tsv". The agent MAY follow the tip on its next search. Low compliance because the agent already has results.

**T4 — PreToolUse hooks**: Fire BEFORE the agent's search. Can block with `permissionDecision: "deny"` and provide redirect context. High compliance because the agent is forced to try something else. Risk: may block legitimate searches.

**T5 — Bash scripts**: Directly conflicts with system prompt's "use Grep instead of grep, use Glob instead of find" directives. Agent will choose Glob/Grep over entity-find.sh every time. Only works if explicitly instructed AND no alternative exists.

<!-- section_id: "f9a0b1c2-d3e4-4f5a-6b7c-8d9e0f1a2b3c" -->
## 3. The "Filesystem as Database" Model

### 3.1 Core Analogy

| Database Concept | Filesystem Equivalent | File |
|-----------------|----------------------|------|
| **Primary key** | UUID (`resource_id`, `entity_id`) | Embedded in file headers |
| **Flat table (index)** | `.entity-lookup.tsv` | Tab-separated: name, UUID, path, parent_UUID |
| **Full record store** | `.uuid-index.json` | JSON with 5,313 entries, full metadata |
| **Foreign key** | `parent_UUID` column in TSV | Links child → parent |
| **Query interface** | Grep (flat) / Read+jq (structured) | Native agent tools |
| **Index rebuild** | `pointer-sync.sh --rebuild-index` | Regenerates TSV + JSON from source files |
| **Schema** | YAML frontmatter (`resource_id:`, `resource_type:`) | In every file header |

### 3.2 Query Patterns (Agent-Friendly)

| Query | SQL Equivalent | Agent Command |
|-------|---------------|---------------|
| Find entity by name | `SELECT * FROM entities WHERE name LIKE '%memory%'` | `Grep pattern="memory" path=".entity-lookup.tsv"` |
| Get entity UUID | `SELECT uuid FROM entities WHERE name = 'memory_system'` | `Grep pattern="memory_system" path=".entity-lookup.tsv"` (2nd column) |
| Get entity path | `SELECT path FROM entities WHERE name LIKE '%pointer%'` | `Grep pattern="pointer" path=".entity-lookup.tsv"` (3rd column) |
| Find children | `SELECT * FROM entities WHERE parent_uuid = 'X'` | `Grep pattern="X" path=".entity-lookup.tsv"` (4th column match) |
| Resolve UUID to path | `SELECT path FROM uuids WHERE uuid = 'X'` | `Read .uuid-index.json` → find `.uuids["X"].path` |
| Full metadata | `SELECT * FROM uuids WHERE uuid = 'X'` | `Read .uuid-index.json` → find `.uuids["X"]` |

### 3.3 Why TSV Over JSON for Primary Queries

| Factor | TSV (`.entity-lookup.tsv`) | JSON (`.uuid-index.json`) |
|--------|---------------------------|--------------------------|
| Grep-compatible | Yes — one match per line | No — multi-line entries |
| Token cost per query | ~30 tokens (Grep call) + ~50-500 tokens (results) | ~30 tokens (Read call) + 2000+ tokens (file content) |
| Human readable | Yes — tab-separated columns | Partially — nested structure |
| Partial matches | Natural — Grep supports regex | Requires jq or mental parsing |
| Column access | Positional (1st=name, 2nd=UUID, 3rd=path, 4th=parent) | Key-based (`.uuids["X"].path`) |
| File size | ~30 KB (382 entities) | ~2.6 MB (5,313 entries with metadata) |

<!-- section_id: "a0b1c2d3-e4f5-4a6b-7c8d-9e0f1a2b3c4d" -->
## 4. Rename/Move Resilience

### 4.1 The Problem

Traditional path-based references break when files or directories move:
```
# Reference in doc A:
See: .0agnostic/pointer-sync.sh

# File moves to:
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh

# Result: Doc A now has a broken reference
# Fix: Find and update all 65+ files that reference the old path
```

### 4.2 The UUID Solution

```
# Reference in doc A (UUID-based):
pointer-sync.sh (resource_id: 08a4e9bc-8cc1-457e-b966-0a912ae6dff7)

# File moves to new location
# Run: pointer-sync.sh --rebuild-index

# Result:
# - .uuid-index.json updated: UUID now resolves to new path
# - .entity-lookup.tsv updated: new path in 3rd column
# - Doc A's UUID reference still works — resolve UUID → get new path
# - ZERO documentation changes needed
```

### 4.3 Resilience Flow

```
File/directory moves
        ↓
pointer-sync.sh --rebuild-index
        ↓
Scans all files for resource_id/entity_id headers
        ↓
Rebuilds .uuid-index.json (UUID → new path)
        ↓
Rebuilds .entity-lookup.tsv (name, UUID, new path, parent_UUID)
        ↓
All Grep queries on .entity-lookup.tsv return new paths
        ↓
All UUID lookups in .uuid-index.json return new paths
        ↓
Zero documentation updates needed
```

### 4.4 What Survives What

| Event | Path-Based References | UUID-Based References |
|-------|----------------------|----------------------|
| File renamed | All break | All survive (after rebuild) |
| Directory moved | All break | All survive (after rebuild) |
| Entity restructured | All break | All survive (after rebuild) |
| Content edited | Survive | Survive |
| File deleted | Both break | UUID resolves to empty (detectable) |
| New file created | N/A | Assign UUID, add to index |

<!-- section_id: "b1c2d3e4-f5a6-4b7c-8d9e-0f1a2b3c4d5e" -->
## 5. Token Efficiency Analysis

### 5.1 Approach Comparison

| Approach | Tool Calls | Input Tokens | Output Tokens | Total Cost |
|----------|-----------|-------------|---------------|------------|
| **Grep on TSV** | 1 | ~30 | ~50-500 | ~80-530 |
| **Read .uuid-index.json** | 1 | ~30 | ~2000-5000 | ~2030-5030 |
| **Bash entity-find.sh** | 1 | ~50 | ~200-1000 | ~250-1050 |
| **Manual Glob + Read chain** | 3-5 | ~150-250 | ~2000-5000 | ~2150-5250 |
| **Task subagent search** | 1 (spawns agent) | ~200 | variable | ~5000-20000 |

### 5.2 Token Budget Impact

With ~100 instructions available (after system prompt uses ~50):
- Our CLAUDE.md chain uses ~15-20 instructions
- Critical Rule #5 (Entity Lookup) uses ~3 instructions
- .claude/rules/uuid-identity-system.md uses ~5 instructions
- Total entity lookup overhead: ~8 instructions = ~5% of budget

This is lean enough to not crowd out other instructions.

<!-- section_id: "c2d3e4f5-a6b7-4c8d-9e0f-1a2b3c4d5e6f" -->
## 6. Interface Design Recommendations

### 6.1 Primary Interface: Grep on .entity-lookup.tsv

- **Format**: Tab-separated, one entity per line
- **Columns**: name, UUID, path, parent_UUID
- **Access**: `Grep pattern="<search>" path=".entity-lookup.tsv"`
- **Regeneration**: `pointer-sync.sh --rebuild-index`
- **Size**: ~30 KB for 382 entities (grows linearly)

### 6.2 Secondary Interface: Read .uuid-index.json

- **Format**: JSON with `.uuids` top-level key
- **Access**: `Read .uuid-index.json` then mentally parse, or `jq '.uuids["UUID"].path'`
- **Use when**: Need full metadata (resource_type, children, parent chain)
- **Size**: ~2.6 MB for 5,313 entries

### 6.3 Instruction Format: Tool Use Example

Rather than verbose explanations, use a single example (proven +18 point accuracy improvement):

```
For entity discovery, use the Grep tool on .entity-lookup.tsv:
Grep pattern="memory" path=".entity-lookup.tsv"
Each line: name<TAB>UUID<TAB>path<TAB>parent_UUID
```

This is 3 lines, ~30 tokens, and more effective than a 20-line explanation.

### 6.4 Hook Strategy

- **PostToolUse on Glob|Grep**: Suggest .entity-lookup.tsv when entity-discovery patterns detected
- **Future**: PreToolUse to intercept entity searches and redirect to TSV before the agent wastes a tool call on Glob

### 6.5 Subagent Strategy

Since subagents don't get .claude/rules/:
1. CLAUDE.md chain includes Critical Rule #5 — subagents read this
2. PostToolUse hooks fire for subagents (same process)
3. For high-priority subagents: include instruction in Task prompt string
