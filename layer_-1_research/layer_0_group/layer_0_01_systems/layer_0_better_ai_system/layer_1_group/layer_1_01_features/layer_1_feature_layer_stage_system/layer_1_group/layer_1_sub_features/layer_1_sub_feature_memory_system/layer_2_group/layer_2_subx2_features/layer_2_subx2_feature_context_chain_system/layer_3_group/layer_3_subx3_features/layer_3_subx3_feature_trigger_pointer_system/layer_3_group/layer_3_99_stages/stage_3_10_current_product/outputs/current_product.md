---
resource_id: "50e10df8-5daa-4a4d-883e-4fe474502b30"
resource_type: "output"
resource_name: "current_product"
---
# Pointer Sync System — Current Product

> **Canonical location**: `.0agnostic/03_protocols/` (organized by protocol)

The pointer sync system's tools are organized into three protocol directories under `.0agnostic/03_protocols/`. Each script has a stable `resource_id` (UUID) that survives renames and moves. The system is production-ready and integrated into the agnostic-sync workflow.

<!-- section_id: "2187b9e6-ab3e-4583-878f-983b66b5d8ee" -->
## What's Shipped

| Component | Status | Location |
|-----------|--------|----------|
| `pointer-sync.sh` | Production | `.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh` (~1150 lines) |
| `entity-find.sh` | Production | `.0agnostic/03_protocols/pointer_sync_protocol/tools/entity-find.sh` (~55 lines) |
| Entity lookup TSV | Production | `.entity-lookup.tsv` (353 entities, generated) |
| `create-resource-indexes.sh` | Production | `.0agnostic/03_protocols/pointer_sync_protocol/tools/create-resource-indexes.sh` (~345 lines) |
| Root UUID index | Production | `.uuid-index.json` (5,313 entries) |
| Per-entity resource indexes | Production | `<entity>/.0agnostic/resource_index.json` (50 entities) |
| Pointer sync protocol | Production | `.0agnostic/03_protocols/pointer_sync_protocol/pointer_sync_protocol.md` |
| Pointer sync knowledge | Production | `.0agnostic/01_knowledge/pointer_sync/pointer_sync_knowledge.md` |
| Pointer sync rule | Production | `.0agnostic/02_rules/static/pointer_sync_rule/pointer_sync_rule.md` |
| Pointer edit guard hook | Production | `.0agnostic/06_.../08_hooks/scripts/pointer-edit-guard.sh` |
| agnostic-sync integration | Production | `.0agnostic/03_protocols/agnostic_sync_protocol/tools/agnostic-sync.sh` (validation section) |

<!-- section_id: "f51874ea-40be-4ce2-a8ec-9bde37e0778d" -->
## Usage

```bash
# Fast entity lookup (~5ms, no Python)
.0agnostic/03_protocols/pointer_sync_protocol/tools/entity-find.sh memory          # Find entities by name
.0agnostic/03_protocols/pointer_sync_protocol/tools/entity-find.sh --path chain    # Just show paths
.0agnostic/03_protocols/pointer_sync_protocol/tools/entity-find.sh --uuid memory   # Just show UUIDs

# Sync all pointers (fix stale paths)
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh

# Validate only (check without modifying)
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --validate

# Verbose output
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --verbose

# Dry run (show what would change)
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --dry-run

# Rebuild UUID index from source files
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --rebuild-index

# Look up a UUID or entity name
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --lookup <uuid-or-name>

# Navigate parent chain
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --parent <uuid>
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --parent <uuid> --verbose  # full chain to root

# List children of an entity
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --children <uuid>

# Query with flexible filters
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query type=entity name=*research*
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query type=resource resource_type=script
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query has_children=true
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --query parent_id=<uuid>

# Find references to a UUID
.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh --find-references <uuid>

# Generate resource indexes for all entities
.0agnostic/03_protocols/pointer_sync_protocol/tools/create-resource-indexes.sh
.0agnostic/03_protocols/pointer_sync_protocol/tools/create-resource-indexes.sh --entity <path>
.0agnostic/03_protocols/pointer_sync_protocol/tools/create-resource-indexes.sh --dry-run
```

<!-- section_id: "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d" -->
## Agent-Friendly Entity Discovery (2026-03-07)

### Primary Interface: Grep on .entity-lookup.tsv

Testing revealed that AI agents systematically prefer Grep/Glob/Read over Bash scripts due to Claude Code's system prompt directives. The entity discovery interface was redesigned to work WITH agent preferences:

```bash
# Agent uses native Grep tool (preferred):
Grep pattern="memory" path=".entity-lookup.tsv"

# Each line returns: name<TAB>UUID<TAB>path<TAB>parent_UUID
# Example result:
# layer_1_sub_feature_memory_system  f62dcffc-...  layer_-1_research/.../memory_system  8da21493-...
```

**Why this works**: Grep is the agent's 3rd most preferred tool (after Read and Glob). `.entity-lookup.tsv` is a flat file — one entity per line, tab-separated. Zero friction, single tool call, ~400 tokens of output for 77 matches.

**What replaced**: `entity-find.sh` (Bash script) — agents ignored it in 3/3 test runs because the system prompt says "use Grep instead of grep" and "use Glob instead of find". The script still exists as a CLI tool for human use.

### Secondary Interface: .uuid-index.json via Read

For detailed lookups (full metadata, parent chains, resource types):

```bash
# Agent reads and mentally parses JSON:
Read .uuid-index.json
# Then finds: .uuids["UUID-HERE"].path

# Or via jq in Bash (for scripts, not agents):
jq -r '.uuids["UUID-HERE"].path // empty' .uuid-index.json
```

### Hook System: entity-search-redirect.sh

PostToolUse hook fires after Glob/Grep operations. When the search pattern looks like entity discovery (e.g., `*0AGNOSTIC.md`, `*entity_type*`), injects a context tip suggesting Grep on .entity-lookup.tsv.

**Location**: `.0agnostic/06_context_avenue_web/01_file_based/08_hooks/scripts/entity-search-redirect.sh`
**Registered in**: `.claude/settings.json` (PostToolUse matcher: `Glob|Grep`)

### Known Limitation: Subagent Context

Task tool subagents do NOT receive `.claude/rules/` files. Entity lookup instructions reach subagents via:
1. CLAUDE.md chain (Critical Rule #5, line ~71)
2. PostToolUse hooks (fire for subagents — same process)
3. Task prompt string (explicit instructions from parent agent)

<!-- section_id: "c3d5e7f9-a0b2-4c1d-8e3f-6a7b9c0d2e4f" -->
## Index Statistics (2026-03-07)

| Metric | Count |
|--------|-------|
| Total UUID entries | 5,313 |
| Entity entries | 351+ |
| Stage entries | 396 |
| Resource entries | 4,566 |
| Entities with parent links | 122 |
| Entities with children | 34 |
| Entities with resource indexes | 50 |
| Entity lookup TSV entries | 382 |
| Index file size | ~2.6 MB |
| TSV file size | ~30 KB |
| Index load time | ~3ms |
| Single lookup time | <0.03ms |
| Grep on TSV (typical) | 1 tool call, <500 tokens |
