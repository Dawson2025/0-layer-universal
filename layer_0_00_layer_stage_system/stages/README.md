# System Management Stages

**Purpose:** Track workflow stages for changes to the Layer + Stage system itself.

**Last Updated:** 2026-01-15

---

## Stages

| Stage | Name | Purpose |
|-------|------|---------|
| 0.00 | request_gathering | Gather requirements for system changes |
| 0.01 | instructions | Define constraints and scope |
| 0.02 | planning | Plan implementation approach |
| 0.03 | design | Design structural changes |
| 0.04 | development | Implement changes |
| 0.05 | testing | Verify changes work |
| 0.06 | criticism | Review against standards |
| 0.07 | fixing | Apply corrections |
| 0.08 | current_product | **Current system state** (protocols, guides, scripts) |
| 0.09 | archives | Historical versions of system docs |

---

## Current Status

See `status.json` for current stage tracking.

---

## What Goes Where

### stage_0.08_current_product/
The actual deliverables of system management work:
- Current change protocols
- Current setup guides
- Current verification scripts
- Active system documentation

### stage_0.09_archives/
Previous versions:
- Old protocol versions
- Deprecated guides
- Historical system states

---

## Related

- `../changes/` - Change protocols (restructuring, traversal)
- `../setup/` - Entity creation guides
- `../plans/` - Planning documents
