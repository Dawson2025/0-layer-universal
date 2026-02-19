# Stage Report Protocol

**Scope**: agent_delegation_system — applies to all stage agents within this entity
**Inherits from**: `layer_0/.0agnostic/03_protocols/stage_report_protocol.md`

## Purpose

Every stage agent writes a `stage_report.md` in its `outputs/` directory before exiting. The entity manager reads these reports to maintain status without loading stage-level details.

## When to Write

- After completing any significant work in a stage
- Before handing off to another stage
- When the manager requests a status update

## Format

See universal protocol at `layer_0/.0agnostic/03_protocols/stage_report_protocol.md` for the required format.

## Entity-Specific Notes

For agent_delegation_system stages:
- Stage reports should note which **child entity** (memory_system or multi_agent_system) is affected by stage outputs
- Stage reports should reference **universal artifacts** if the stage work produced artifacts that were promoted to `layer_0/.0agnostic/`
- Stage reports should note overlap with context_chain_system's own stage work where applicable
