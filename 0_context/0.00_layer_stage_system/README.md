# Layer & Stage System Management

This directory contains documentation and workflows for **managing the layering and staging system itself** - the meta-level work of maintaining and extending the framework.

**Last Updated:** 2026-01-15

---

## Structure

```
0.00_layer_stage_system/
├── README.md                    ← You are here
└── stages/
    ├── status.json              # Current stage tracking
    ├── stage_0.00_request_gathering/
    ├── stage_0.01_instructions/
    ├── stage_0.02_planning/
    │   └── hand_off_documents/
    │       └── MCP_DOCUMENTATION_PLAN.md
    ├── stage_0.03_design/
    ├── stage_0.04_development/
    ├── stage_0.05_testing/
    ├── stage_0.06_criticism/
    ├── stage_0.07_fixing/
    ├── stage_0.08_current_product/   ← CURRENT DELIVERABLES
    │   ├── changes/                   # Change protocols
    │   └── setup/                     # Entity creation guides
    └── stage_0.09_archives/
```

---

## Quick Access to Current Deliverables

| Content | Location |
|---------|----------|
| **Change protocols** | `stages/stage_0.08_current_product/changes/` |
| **Setup guides** | `stages/stage_0.08_current_product/setup/` |
| **Planning docs** | `stages/stage_0.02_planning/hand_off_documents/` |
| **Current status** | `stages/status.json` |

### Key Documents

| Document | Path |
|----------|------|
| Restructuring Protocol | `stages/stage_0.08_current_product/changes/restructuring_migration_protocol.md` |
| Traversal Protocol | `stages/stage_0.08_current_product/changes/traversal_update_protocol.md` |
| Path Verification | `stages/stage_0.08_current_product/changes/verify_paths.sh` |
| Instantiation Guide | `stages/stage_0.08_current_product/setup/instantiation_guide.md` |
| Project Checklist | `stages/stage_0.08_current_product/setup/project_creation_checklist.md` |

---

## Important: Making Changes

When making structural changes to the framework:

1. **Content migration** - Migrate actual content, not just create empty structures
2. **Traversal updates** - Update ALL navigation docs so agents can find new paths

**See:**
- `stages/stage_0.08_current_product/changes/restructuring_migration_protocol.md`
- `stages/stage_0.08_current_product/changes/traversal_update_protocol.md`

---

## Distinction from `0.01_layer_stage_framework/`

| This folder (`0.00_`) | Framework folder (`0.01_`) |
|----------------------|---------------------------|
| **Meta**: How to manage the system | **Content**: Templates & guides for using the system |
| Change protocols, setup guides | Layer templates, feature guides |
| System administration | System usage |

---

## Structural Change Checklist

When making structural changes (renaming directories, adding stages/layers):

| Priority | File | What to Update |
|----------|------|----------------|
| 1 | `universal_init_prompt.md` | Directory paths & structure diagrams |
| 2 | `MASTER_DOCUMENTATION_INDEX.md` | Document links |
| 3 | `SYSTEM_OVERVIEW.md` | Architecture description |
| 4 | `0.01_layer_stage_framework/README.md` | Framework structure |
| 5 | All `*.md` files with hardcoded paths | Use `grep` + `sed` for bulk updates |

**Verify:** Run `stages/stage_0.08_current_product/changes/verify_paths.sh`

---

## Recent Structural Changes

| Date | Change |
|------|--------|
| 2026-01-15 | Integrated folders into stages structure |
| 2026-01-15 | Added `stages/` folder for system management workflow |
| 2026-01-15 | Added `traversal_update_protocol.md` and `verify_paths.sh` |
| 2026-01-15 | Added stage N.08 `current_product` (renumbered archives to N.09) |
| 2026-01-15 | Renamed top-level folders to `<N>_layer_<name>/` format |
| 2026-01-13 | Renamed `0.06_mcp_servers` → `0.06_mcp_servers_and_apis_and_secrets` |

---

## Related

- `0.01_layer_stage_framework/` - Templates and guides for using the framework
- `layer_0_universal/` - Universal layer implementation
