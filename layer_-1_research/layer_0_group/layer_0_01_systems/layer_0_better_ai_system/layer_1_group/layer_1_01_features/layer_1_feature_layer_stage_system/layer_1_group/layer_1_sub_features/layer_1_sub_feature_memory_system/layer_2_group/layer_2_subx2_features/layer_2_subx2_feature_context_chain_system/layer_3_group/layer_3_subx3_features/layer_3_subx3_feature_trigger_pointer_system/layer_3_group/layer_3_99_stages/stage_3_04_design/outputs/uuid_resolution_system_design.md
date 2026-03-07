---
resource_id: "c9d0e1f2-a3b4-4567-8234-567890123456"
resource_type: "output"
resource_name: "uuid_resolution_system_design"
---
# UUID Resolution System Design

<!-- section_id: "d0e1f2a3-b4c5-4678-9345-678901234567" -->
## Date: 2026-03-07

<!-- section_id: "e1f2a3b4-c5d6-4789-0456-789012345678" -->
## Problem Statement

The UUID identity system assigns stable identifiers to every entity, file, directory, section, and stage (5,300+ entries). But references throughout the codebase still use hardcoded filesystem paths. When anything moves, all path references break and must be manually updated (81+ files during the script protocol migration).

**Root cause**: UUIDs exist as metadata alongside paths, but nothing resolves via UUID at runtime. The path is still the primary reference mechanism everywhere.

**Goal**: Make UUID the primary reference mechanism. Paths become derived artifacts, resolved at the moment of use from the UUID index.

<!-- section_id: "f2a3b4c5-d6e7-4890-1567-890123456789" -->
## Core Design: The resolve-uuid Function

### The Resolution Layer

```bash
resolve-uuid() {
  local uuid="$1"
  local root
  root="$(git rev-parse --show-toplevel 2>/dev/null || echo "$HOME/dawson-workspace/code/0_layer_universal")"
  local index="$root/.uuid-index.json"

  if [[ ! -f "$index" ]]; then
    echo "ERROR: UUID index not found at $index" >&2
    return 1
  fi

  local path
  path=$(jq -r --arg id "$uuid" '.[$id].path // empty' "$index")

  if [[ -z "$path" ]]; then
    echo "ERROR: UUID $uuid not found in index" >&2
    return 1
  fi

  echo "$root/$path"
}
```

### Performance

| Metric | Value |
|--------|-------|
| Index file | `.uuid-index.json` (~2.6 MB, 5,300+ entries) |
| Load time | ~3ms |
| Single lookup | <0.03ms |
| Full resolution (load + lookup) | ~5ms |
| Acceptable for | Every script call, every reference resolution |

### Usage in Scripts

```bash
# Before (hardcoded path — breaks when things move):
bash ".0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh" --validate

# After (UUID reference — survives any move):
bash "$(resolve-uuid 08a4e9bc-8cc1-457e-b966-0a912ae6dff7)" --validate
```

### Usage in Cross-Script Calls

```bash
# Before (relative path from SCRIPT_DIR):
POINTER_SYNC="$SCRIPT_DIR/../../pointer_sync_protocol/tools/pointer-sync.sh"

# After (UUID — doesn't matter where either script lives):
POINTER_SYNC="$(resolve-uuid 08a4e9bc-8cc1-457e-b966-0a912ae6dff7)"
```

<!-- section_id: "a3b4c5d6-e7f8-4901-2678-901234567890" -->
## UUID Reference Syntax in Source Files

### In 0AGNOSTIC.md (Source of Truth)

0AGNOSTIC.md files use a placeholder syntax that `agnostic-sync.sh` can process:

```markdown
| pointer-sync.sh | `{{resolve:08a4e9bc-8cc1-457e-b966-0a912ae6dff7}}` | Sync all pointers |
```

The `{{resolve:UUID}}` placeholder is:
- **Human-scannable**: The UUID is visible, can be looked up manually
- **Machine-resolvable**: `agnostic-sync.sh` replaces it with the current path during generation
- **Stable**: Never needs updating when things move

### In Generated Context Files (CLAUDE.md, AGENTS.md, etc.)

Since all major AI apps can run bash (see `ai_app_bash_capability_research.md`), generated files include both the UUID and a resolve instruction:

```markdown
## Script References

To resolve any script path, use:
`resolve-uuid <UUID>` or `jq -r --arg id "<UUID>" '.[$id].path' .uuid-index.json`

| Script | UUID | Resolve |
|--------|------|---------|
| pointer-sync.sh | `08a4e9bc-8cc1-457e-b966-0a912ae6dff7` | `$(resolve-uuid 08a4e9bc)` |
| entity-find.sh | `f4a2b3c5-d6e7-4f89-a0b1-c2d3e4f5a6b7` | `$(resolve-uuid f4a2b3c5)` |
```

### Fallback for Apps Without Bash (Theoretical)

If a future AI app cannot run bash, `agnostic-sync.sh` generates a version with pre-resolved paths:

```markdown
| pointer-sync.sh | `.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh` |
```

This is the current behavior. The resolved path is a generated convenience — correct at generation time but potentially stale after moves.

<!-- section_id: "b4c5d6e7-f8a9-4012-3789-012345678901" -->
## Self-Healing References

### The Key Insight

When an AI app reads a CLAUDE.md that contains UUID + resolve-uuid instructions, it resolves the reference **at the moment of use**. This means:

1. Something moves at time T
2. `pointer-sync.sh --rebuild-index` runs at time T+1 (updates UUID → path mapping)
3. AI app reads CLAUDE.md at time T+5 — the UUID reference is still there, unchanged
4. AI app runs `resolve-uuid` — gets the **current** path from the rebuilt index
5. Reference works correctly, even though CLAUDE.md was never regenerated

**No stale window.** Compare with the current path-based approach:

1. Something moves at time T
2. CLAUDE.md still has the old path — **broken** until someone runs `agnostic-sync.sh`
3. AI app reads CLAUDE.md, tries the old path — **fails**

### Self-Healing Requirement

For self-healing to work, only one thing must be updated after a move: the UUID index. This is already handled by `pointer-sync.sh --rebuild-index`, which scans the filesystem and regenerates `.uuid-index.json`.

<!-- section_id: "c5d6e7f8-a9b0-4123-4890-123456789012" -->
## Move Workflow (Target State)

After implementing the UUID resolution system, the complete workflow for moving any file, directory, or entity:

```
1. mv old/path new/path                          # Physical move
2. pointer-sync.sh --rebuild-index               # Update UUID → path mapping (~3s)
3. (optional) agnostic-sync.sh                   # Regenerate pre-resolved paths for non-bash apps
4. git add && git commit && git push             # Commit
```

**What you do NOT need to do:**
- Grep across 81+ files for path references
- Manually update documentation
- Fix script-to-script calls
- Update hook paths
- Re-check every context file

<!-- section_id: "d6e7f8a9-b0c1-4234-5901-234567890123" -->
## Integration Points

### 1. resolve-uuid Shell Function

**Location**: Sourced by all scripts (e.g., in a shared `_common.sh` or defined inline)

**Distribution**: Two options:
- **Option A**: Standalone script at a well-known location (e.g., `.0agnostic/03_protocols/pointer_sync_protocol/tools/resolve-uuid.sh`) — bootstrapping problem: how do you find the resolver without a path?
- **Option B** (recommended): Inline function in each script's preamble, or sourced from `$ROOT/.0agnostic/resolve-uuid.sh` using `git rev-parse --show-toplevel` to find ROOT — no UUID needed to find the resolver itself.

### 2. agnostic-sync.sh Enhancement

Current behavior: Copies 0AGNOSTIC.md content into CLAUDE.md with tool-specific additions.

New behavior: Also resolves `{{resolve:UUID}}` placeholders in 0AGNOSTIC.md to current paths (for human readability) while emitting UUID references + resolve instructions (for AI app use).

### 3. Git Hooks

Current: Hooks reference scripts by hardcoded path.
New: Hooks use `resolve-uuid` to find scripts. The hook file itself is at a well-known git path (`.git/hooks/pre-commit`), so no UUID needed for the hook — but the scripts it calls are resolved by UUID.

### 4. UUID Index as the Single Source of Path Truth

The `.uuid-index.json` becomes the authoritative UUID → path mapping:
- **Generated by**: `pointer-sync.sh --rebuild-index`
- **Read by**: `resolve-uuid`, `agnostic-sync.sh`, AI agents
- **Updated**: After any file/directory move
- **Size**: ~2.6 MB for 5,300+ entries
- **Speed**: ~3ms load, <0.03ms per lookup

<!-- section_id: "e7f8a9b0-c1d2-4345-6012-345678901234" -->
## Implementation Phases

### Phase 1: Create resolve-uuid Function
- Write the function (simple jq lookup on .uuid-index.json)
- Test with known UUIDs
- Document usage

### Phase 2: Update Scripts to Use resolve-uuid
- Replace hardcoded cross-script paths with `resolve-uuid` calls
- Keep `SCRIPT_DIR`-based relative paths for same-directory scripts (already UUID-independent)
- Update git hooks to use `resolve-uuid`

### Phase 3: Add {{resolve:UUID}} Syntax to 0AGNOSTIC.md
- Define the placeholder syntax
- Update `agnostic-sync.sh` to resolve placeholders during generation
- Convert key path references in 0AGNOSTIC.md files to use placeholders

### Phase 4: Update agnostic-sync.sh Output
- Emit UUID references + resolve-uuid instructions in CLAUDE.md, AGENTS.md
- Emit resolved paths in .cursorrules, copilot-instructions.md, GEMINI.md, OPENAI.md (fallback)
- Or emit UUID references in all files (since all apps can run bash)

### Phase 5: Validation
- Move a script, rebuild index, verify all UUID references resolve correctly
- Move an entity directory, rebuild index, verify
- Run all scripts to confirm nothing breaks

<!-- section_id: "f8a9b0c1-d2e3-4456-7123-456789012345" -->
## AI App Capability Summary

Research confirms all major AI coding apps can run bash (see `ai_app_bash_capability_research.md`). This means UUID references with resolve-uuid instructions can go in **all** ported context files:

| Context File | App(s) | Can Bash? | Reference Type |
|-------------|--------|-----------|---------------|
| CLAUDE.md | Claude Code | Yes | UUID + resolve-uuid |
| AGENTS.md | Codex CLI | Yes | UUID + resolve-uuid |
| GEMINI.md | Gemini CLI | Yes | UUID + resolve-uuid |
| OPENAI.md | OpenAI apps | Yes | UUID + resolve-uuid |
| .cursorrules | Cursor agent | Yes | UUID + resolve-uuid |
| copilot-instructions.md | Copilot (VS Code + CLI) | Yes | UUID + resolve-uuid |

No app currently requires pre-resolved paths as its primary mechanism.

<!-- section_id: "a9b0c1d2-e3f4-4567-8234-567890123456" -->
## Bootstrapping Problem

One challenge: How does `resolve-uuid` find itself? It needs a path to load the UUID index.

**Solution**: Use `git rev-parse --show-toplevel` to find the repo root. This is a git primitive that works regardless of where scripts live. From root, the index is always at `.uuid-index.json`.

```bash
ROOT="$(git rev-parse --show-toplevel)"
INDEX="$ROOT/.uuid-index.json"
```

This is the one hardcoded path in the entire system — the index location relative to repo root. Everything else resolves through it.

<!-- section_id: "b0c1d2e3-f4a5-4678-9345-678901234567" -->
## Why This Solves the Problem

**Before UUID resolution**: Moving a script requires:
1. Move the file
2. Find all 65+ references across the codebase (`grep -rl`)
3. Update each one manually
4. Hope you didn't miss any
5. Repeat every time something moves

**After UUID resolution**: Moving a script requires:
1. Move the file
2. Run `pointer-sync.sh --rebuild-index` (~3 seconds)
3. Done — all UUID-based references resolve automatically

The UUIDs are no longer just metadata. They are the **primary reference mechanism**. The path is a derived value, resolved on demand, always current.
