# Branch: Principles

## Purpose

Core design principles governing the context chain system. These principles guide all architecture and implementation decisions.

## Topics

| File | Principle | Type |
|------|-----------|------|
| `lean_static_context.md` | Keep static context minimal, push detail to dynamic | Efficiency |
| `chain_continuity.md` | Every entity must maintain unbroken parent chain to root | Structural Integrity |
| `avenue_redundancy.md` | Critical context reachable through 3+ independent avenues | Reliability |
| `single_source_of_truth.md` | 0AGNOSTIC.md is canonical; tool files are derived | Consistency |
| `graceful_degradation.md` | System continues functioning when avenues fail | Resilience |

## Principle Relationships

- Avenue redundancy enables graceful degradation
- Chain continuity depends on single source of truth (0AGNOSTIC.md is the chain link)
- Lean static context is implemented via the static/dynamic split
- All principles reinforce each other -- no principle works in isolation
