# Stage Report Protocol

**Scope**: agent_delegation_system — applies to all stage agents within this entity
**Inherits from**: `.0agnostic/03_protocols/stage_report_protocol.md`

## Purpose

Every stage agent writes a canonical `stage_report.md` in `outputs/reports/` before exiting and mirrors it into `.0agnostic/05_handoff_documents/02_outgoing/` for propagation. The entity manager reads these reports to maintain status without loading stage-level details.

## When to Write

- After completing any significant work in a stage
- Before handing off to another stage
- When the manager requests a status update

## Format

See universal protocol at `.0agnostic/03_protocols/stage_report_protocol.md` for the required format.

## Canonical Locations

- Canonical: `outputs/reports/stage_report.md`
- Handoff (to manager): `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md`
- Handoff (to below): `.0agnostic/05_handoff_documents/02_outgoing/03_to_below/stage_report.md`
- Legacy compatibility (temporary): `outputs/stage_report.md`

## Entity-Specific Notes

For agent_delegation_system stages:
- Stage reports should note which **child entity** (memory_system or multi_agent_system) is affected by stage outputs
- Stage reports should reference **universal artifacts** if the stage work produced artifacts that were promoted to `.0agnostic/`
- Stage reports should note overlap with context_chain_system's own stage work where applicable
- Keep canonical and handoff copies synchronized
