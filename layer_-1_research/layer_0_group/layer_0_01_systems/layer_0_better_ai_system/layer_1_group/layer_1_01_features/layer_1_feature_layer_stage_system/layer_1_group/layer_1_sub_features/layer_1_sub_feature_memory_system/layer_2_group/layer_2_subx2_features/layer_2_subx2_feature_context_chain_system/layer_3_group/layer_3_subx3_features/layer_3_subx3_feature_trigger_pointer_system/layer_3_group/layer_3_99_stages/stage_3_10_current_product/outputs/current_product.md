---
resource_id: "50e10df8-5daa-4a4d-883e-4fe474502b30"
resource_type: "output"
resource_name: "current_product"
---
# Pointer Sync System — Current Product

> **Canonical location**: Root `.0agnostic/pointer-sync.sh`

The current working product is the `pointer-sync.sh` script at the root `.0agnostic/` level. It is production-ready and integrated into the agnostic-sync workflow.

## What's Shipped

| Component | Status | Location |
|-----------|--------|----------|
| `pointer-sync.sh` | Production | `.0agnostic/pointer-sync.sh` |
| Pointer sync protocol | Production | `.0agnostic/03_protocols/pointer_sync_protocol.md` |
| Pointer sync knowledge | Production | `.0agnostic/01_knowledge/pointer_sync/pointer_sync_knowledge.md` |
| Pointer sync rule | Production | `.0agnostic/02_rules/static/pointer_sync_rule/pointer_sync_rule.md` |
| Pointer edit guard hook | Production | `.0agnostic/06_.../08_hooks/scripts/pointer-edit-guard.sh` |
| agnostic-sync integration | Production | `.0agnostic/agnostic-sync.sh` (validation section) |

## Usage

```bash
# Sync all pointers (fix stale paths)
.0agnostic/pointer-sync.sh

# Validate only (check without modifying)
.0agnostic/pointer-sync.sh --validate

# Verbose output
.0agnostic/pointer-sync.sh --verbose

# Dry run (show what would change)
.0agnostic/pointer-sync.sh --dry-run
```
