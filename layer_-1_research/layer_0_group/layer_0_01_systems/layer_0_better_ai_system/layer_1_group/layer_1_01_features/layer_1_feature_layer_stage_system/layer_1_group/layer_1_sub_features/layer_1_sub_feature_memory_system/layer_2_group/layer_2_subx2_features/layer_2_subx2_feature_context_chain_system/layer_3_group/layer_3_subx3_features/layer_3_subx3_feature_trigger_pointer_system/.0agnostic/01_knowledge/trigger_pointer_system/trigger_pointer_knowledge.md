---
resource_id: "89891764-41a7-4708-81ed-cc72e3b094ac"
resource_type: "knowledge"
resource_name: "trigger_pointer_knowledge"
---
# Trigger Pointer System — Knowledge

<!-- section_id: "3d687dc2-20f8-4c8e-b6ba-be937a875b8e" -->
## Overview

The trigger pointer system automates the maintenance of pointer files across the layer-stage hierarchy. Pointer files are lightweight markdown files that reference a canonical location elsewhere in the tree, avoiding content duplication while maintaining navigability.

<!-- section_id: "e55f7215-68ee-4782-9459-77ee62b39a8f" -->
## Architecture

<!-- section_id: "8517f107-8724-407b-89d3-5495e842a490" -->
### Components

| Component | Purpose | Location |
|-----------|---------|----------|
| pointer-sync.sh | Main sync script — finds, resolves, updates pointers | Root `.0agnostic/03_protocols/pointer_sync_protocol/tools/pointer-sync.sh` |
| entity-find.sh | Fast entity lookup by name (~5ms, no Python) | Root `.0agnostic/03_protocols/pointer_sync_protocol/tools/entity-find.sh` |
| .entity-lookup.tsv | Flat entity index (name/uuid/path), generated | Root `.entity-lookup.tsv` |
| pointer_sync_protocol.md | Pointer file format, creation guide, resolution algorithm | Root `.0agnostic/03_protocols/` |
| pointer_sync_rule.md | Always-apply rule for pointer file conventions | Root `.0agnostic/02_rules/static/` |
| pointer-edit-guard.sh | Claude Code PostToolUse hook — reminds agents to validate | Root `.0agnostic/06_.../08_hooks/scripts/` |
| agnostic-sync integration | Validation runs at end of every `agnostic-sync.sh` run | Root `.0agnostic/03_protocols/agnostic_sync_protocol/tools/agnostic-sync.sh` |

<!-- section_id: "1bac227b-3dab-4316-8cc4-cccc83f797fe" -->
### How Pointers Work

1. **Identification**: Pointer files have YAML frontmatter with `pointer_to:` and `canonical_entity:` fields
2. **Resolution**: The sync script searches for the canonical entity directory by name using `find`, not by stored path
3. **Path computation**: Relative paths are computed from the pointer file's directory to the canonical target using `python3 -c "import os.path; print(os.path.relpath(...))`
4. **Update**: The `> **Canonical location**:` line in the pointer body is rewritten with the new computed path

<!-- section_id: "191d6ceb-8c0e-4f31-a951-fe09caf58853" -->
### Why Entity-Relative Resolution

Pointers survive intermediate directory renames because the script searches for the entity by name, not by the old path. Only the leaf entity directory name must remain stable. This means reorganizing parent directories (a common operation) never breaks pointers.

<!-- section_id: "c1c8308d-aa3e-4b4f-9480-c0342116aaaa" -->
### Trigger Mechanisms

| Trigger | When | What Happens |
|---------|------|-------------|
| Claude Code PostToolUse hook | After Edit/Write on `.md` files | Checks for pointer frontmatter, reminds agent to validate |
| agnostic-sync.sh integration | After every sync run | Runs `pointer-sync.sh --validate` automatically |
| Manual invocation | Developer runs script directly | Full sync or validate-only mode |

<!-- section_id: "3a813505-25fb-4a20-9bd0-39b705073fc3" -->
### Relationship to Context Chain System

This system is a child of the context chain system. It addresses **Avenue A4 (parent chain)** reliability by ensuring that pointer files — which form navigation links across the hierarchy — stay valid even as the directory tree evolves.

<!-- section_id: "efde5424-16f1-478d-aa8a-ff0ecdb43968" -->
## Design Decisions

1. **YAML frontmatter, not external registry**: Pointer metadata lives in the file itself, making it portable and self-describing
2. **Entity-name search, not path storage**: Resolution by name tolerates directory reorganization
3. **Non-blocking hooks**: Hooks remind but don't block — agents and developers can proceed even if sync hasn't run
4. **Integrated validation**: Running validation after every agnostic-sync ensures pointers are checked frequently without manual effort
