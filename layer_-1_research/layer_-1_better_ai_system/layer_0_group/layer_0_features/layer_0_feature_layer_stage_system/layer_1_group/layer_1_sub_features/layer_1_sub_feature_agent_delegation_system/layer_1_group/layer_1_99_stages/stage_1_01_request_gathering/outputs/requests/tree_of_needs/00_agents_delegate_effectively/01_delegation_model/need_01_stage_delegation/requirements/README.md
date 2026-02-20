# Stage Delegation -- Requirements Index

**Need**: [Stage Delegation](../README.md)

## Overview

These requirements define how managers hand off work to stage agents without carrying operational knowledge. They establish that every stage must have a self-contained `0AGNOSTIC.md` with identity, methodology, and success criteria — so the manager only provides a task and a pointer, never the methodology itself. The boundary between manager responsibility (coordination, priority) and stage agent responsibility (methodology, outputs) is made explicit and enforceable.

## Key Themes

- **Stage Agent Self-Sufficiency**: Every stage agent must find everything it needs in its own `0AGNOSTIC.md` — role, methodology, output format, success criteria, and parent pointers for domain context
- **Manager Delegation Protocol**: Managers delegate with a task description and directory pointer only; they never carry or transmit operational methodology
- **Clear Boundaries**: What stays with the manager (status overview, cross-stage decisions, priority) vs what stays with the stage agent (methodology, detailed outputs, procedures) is explicitly defined with escalation paths

---

| REQ# | Name | Description | File |
|------|------|-------------|------|
| REQ-01 | Stage Agent Identity | Identity, methodology, scope in every stage 0AGNOSTIC.md | [REQ-01_stage_agent_identity.md](./REQ-01_stage_agent_identity.md) |
| REQ-02 | Manager Delegation Protocol | How managers delegate without carrying operational knowledge | [REQ-02_manager_delegation_protocol.md](./REQ-02_manager_delegation_protocol.md) |
| REQ-03 | Boundary Rules | What stays with the manager vs the stage agent | [REQ-03_boundary_rules.md](./REQ-03_boundary_rules.md) |
