---
resource_id: "c26fe8b5-f6b5-4557-9481-4f7deb542c85"
resource_type: "readme
knowledge"
resource_name: "README"
---
# Branch: Principles

<!-- section_id: "a909b0cc-0e49-45e5-9f47-77b64df50c67" -->
## Purpose

Core design principles governing the context chain system. These principles guide all architecture and implementation decisions.

<!-- section_id: "88791ee6-2d3c-49e3-8470-3b7b35881b98" -->
## Topics

| File | Principle | Type |
|------|-----------|------|
| `lean_static_context.md` | Keep static context minimal, push detail to dynamic | Efficiency |
| `chain_continuity.md` | Every entity must maintain unbroken parent chain to root | Structural Integrity |
| `avenue_redundancy.md` | Critical context reachable through 3+ independent avenues | Reliability |
| `single_source_of_truth.md` | 0AGNOSTIC.md is canonical; tool files are derived | Consistency |
| `graceful_degradation.md` | System continues functioning when avenues fail | Resilience |

<!-- section_id: "2522f933-460d-4ef5-9ce9-6ff9368d8f7e" -->
## Principle Relationships

- Avenue redundancy enables graceful degradation
- Chain continuity depends on single source of truth (0AGNOSTIC.md is the chain link)
- Lean static context is implemented via the static/dynamic split
- All principles reinforce each other -- no principle works in isolation
