# System Management Stages

**Purpose:** Track workflow stages for changes to the Layer + Stage system itself.

**Last Updated:** 2026-01-15

---

## Stages

| Stage | Name | Purpose |
|-------|------|---------|
| 0.01 | request_gathering | Gather requirements for system changes |
| 0.02 | research | Explore options and gather context |
| 0.03 | instructions | Define constraints and scope |
| 0.04 | planning | Plan implementation approach |
| 0.05 | design | Design structural changes |
| 0.06 | development | Implement changes |
| 0.07 | testing | Verify changes work |
| 0.08 | criticism | Review against standards |
| 0.09 | fixing | Apply corrections |
| 0.10 | current_product | **Current system state** (protocols, guides, scripts) |
| 0.11 | archives | Historical versions of system docs |

---

## Current Status

See `status.json` for current stage tracking.

---

## What Goes Where

### stage_0_10_current_product/
The actual deliverables of system management work:
- Current change protocols
- Current setup guides
- Current verification scripts
- Active system documentation

### stage_0_11_archives/
Previous versions:
- Old protocol versions
- Deprecated guides
- Historical system states

---

## Related

- `../changes/` - Change protocols (restructuring, traversal)
- `../setup/` - Entity creation guides
- `../plans/` - Planning documents
