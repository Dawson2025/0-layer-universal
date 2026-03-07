---
resource_id: "b2c3d4e5-f6a7-4890-1bcd-ef0123456790"
resource_type: "output"
resource_name: "script_protocol_migration_design"
---
# Script Protocol Migration Design

<!-- section_id: "c3d4e5f6-a7b8-4901-2cde-f01234567891" -->
## Date: 2026-03-07

<!-- section_id: "d4e5f6a7-b8c9-4012-3def-012345678902" -->
## Problem Statement

12 shell scripts sat loose at `.0agnostic/` root, violating two principles:

1. **Organizational rule**: Nothing should live at `.0agnostic/` root — everything belongs in numbered subdirectories (01_knowledge, 02_rules, 03_protocols, etc.)
2. **Reference brittleness**: All 65+ documentation files referenced scripts by hardcoded path (`.0agnostic/pointer-sync.sh`). Moving anything required updating every reference — the exact "bajillion file changes" problem that the UUID system was built to solve.

<!-- section_id: "e5f6a7b8-c9d0-4123-4ef0-123456789013" -->
## Core Insight: UUID-Based References

The UUID identity system already assigns a stable `resource_id` to every script. When we move a script, its UUID stays the same — only the filesystem path changes. The `.uuid-index.json` maps UUID → current path.

**Principle**: The path is convenience, the UUID is truth.

After this migration, all documentation includes both:
```markdown
| pointer-sync.sh | `.../pointer_sync_protocol/tools/` | resource_id: `08a4e9bc-...` |
```

Future moves only require:
1. Physically move the file
2. Rebuild the UUID index (`pointer-sync.sh --rebuild-index`)
3. All UUID-based lookups automatically resolve to the new path

No documentation changes needed for future moves. This is the design intent of the UUID system being applied to its own tooling.

<!-- section_id: "f6a7b8c9-d0e1-4234-5f01-234567890124" -->
## Script Grouping Design

Scripts group naturally by the protocol they implement:

| Protocol | Scripts | Rationale |
|----------|---------|-----------|
| **pointer_sync_protocol** | pointer-sync.sh, entity-find.sh, create-resource-indexes.sh, migrate-pointers.sh | All pointer/entity resolution tools |
| **uuid_assignment_protocol** | assign-entity-uuids.sh, assign-file-uuids.sh, assign-dir-uuids.sh, assign-section-uuids.sh, create-stage-indexes.sh | All UUID assignment tools |
| **agnostic_sync_protocol** | agnostic-sync.sh, agnostic-diagram-generator.sh, user-level-sync.sh | All tool-agnostic context generation tools |

<!-- section_id: "a7b8c9d0-e1f2-4345-6012-345678901235" -->
## Target Directory Structure

```
.0agnostic/03_protocols/
├── pointer_sync_protocol/
│   ├── pointer_sync_protocol.md     (protocol doc)
│   └── tools/
│       ├── pointer-sync.sh          (resource_id: 08a4e9bc-...)
│       ├── entity-find.sh           (resource_id: f4a2b3c5-...)
│       ├── create-resource-indexes.sh (resource_id: 9f294247-...)
│       └── migrate-pointers.sh      (resource_id: 7505b140-...)
├── uuid_assignment_protocol/
│   ├── uuid_assignment_protocol.md  (protocol doc)
│   └── tools/
│       ├── assign-entity-uuids.sh   (resource_id: 92ab3def-...)
│       ├── assign-file-uuids.sh     (resource_id: 68c9cfcc-...)
│       ├── assign-dir-uuids.sh      (resource_id: c7d8e9f0-...)
│       ├── assign-section-uuids.sh  (resource_id: d8e9f0a1-...)
│       └── create-stage-indexes.sh  (resource_id: bcac347f-...)
└── agnostic_sync_protocol/
    ├── agnostic_sync_protocol.md    (protocol doc)
    └── tools/
        ├── agnostic-sync.sh         (resource_id: 781698fa-...)
        ├── agnostic-diagram-generator.sh (resource_id: 44f8f145-...)
        └── user-level-sync.sh       (resource_id: 5e3e7995-...)
```

<!-- section_id: "b8c9d0e1-f2a3-4456-7123-456789012346" -->
## Internal Path Resolution Design

Scripts use `SCRIPT_DIR` + relative traversal to find the repo root:

```bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
# 4 levels up: tools/ → protocol/ → 03_protocols/ → .0agnostic/ → ROOT
```

### Script-to-Script References

**Same protocol** (scripts in same `tools/` directory):
```bash
bash "$SCRIPT_DIR/pointer-sync.sh" --rebuild-index
```

**Cross-protocol** (e.g., agnostic-sync.sh calling pointer-sync.sh):
```bash
_SYNC_SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
POINTER_SYNC="$_SYNC_SCRIPT_DIR/../../pointer_sync_protocol/tools/pointer-sync.sh"
```

**Git rev-parse scripts** (assign-file-uuids.sh, migrate-pointers.sh, agnostic-diagram-generator.sh):
These use `git rev-parse --show-toplevel` to find root — no path fix needed.

<!-- section_id: "c9d0e1f2-a3b4-4567-8234-567890123457" -->
## Reference Update Strategy

### Batch Updates (81+ files)

Path references were updated via `grep -rl` + `xargs sed`:
- `.0agnostic/pointer-sync.sh` → `.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh`
- `.0agnostic/entity-find.sh` → `.0agnostic/03_protocols/pointer_sync_protocol/tools/entity-find.sh`
- etc. for all 12 scripts

### Manual Updates (key files)

- Root `0AGNOSTIC.md` — UUID section commands, triggers table, resources table
- `.0agnostic/01_knowledge/pointer_sync/pointer_sync_knowledge.md` — components table with UUID column
- `.0agnostic/06_.../05_skills/uuid-query/SKILL.md` — all command paths
- `.claude/rules/uuid-identity-system.md` — quick reference commands
- `.0agnostic/06_.../05_skills/entity-creation/SKILL.md` — sync and validation commands
- Git hooks (pre-commit, post-merge) — script paths
- pointer-edit-guard.sh — hook message with new path + resource_id

### Auto-Generated Files (regenerated by agnostic-sync.sh)

CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules, copilot-instructions.md — all regenerated from updated 0AGNOSTIC.md source files.

<!-- section_id: "d0e1f2a3-b4c5-4678-9345-678901234568" -->
## Why This Matters for the Future

This migration demonstrates the UUID system's value proposition:

**Before UUID system**: Moving a script requires:
1. Move the file
2. Find all 65+ references across the codebase
3. Update each one manually
4. Hope you didn't miss any
5. Repeat every time something moves

**After UUID system**: Moving a script requires:
1. Move the file
2. Run `pointer-sync.sh --rebuild-index`
3. Done — all UUID-based lookups resolve automatically

The remaining path-based references in documentation are for human readability only. The UUID is the stable reference that survives renames, moves, and reorganizations.
