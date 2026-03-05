---
resource_id: "70e8e69c-9bf6-4327-b6bb-f4f7e5cbdc84"
resource_type: "knowledge"
resource_name: "graceful_degradation"
---
# Principle: Graceful Degradation

**Type**: Resilience
**Severity**: High
**Date**: 2026-02-17

---

<!-- section_id: "68969cfd-6d32-415d-8976-16161b0cef39" -->
## Statement

**When one or more context delivery avenues fail, the system must continue functioning with reduced but sufficient context. No single avenue failure should render an entity unusable.**

---

<!-- section_id: "b178f9f4-9d79-47dd-941e-bceb555f8475" -->
## Rationale

In practice, context delivery is imperfect:
- An agent launched from a different cwd won't see deep CLAUDE.md files
- A .gab.jsonld with a syntax error can't be parsed
- Episodic memory is empty on first session
- A tool might not support .claude/rules/
- MCP servers might be unavailable

Rather than requiring all 8 avenues to function perfectly, the system should degrade gracefully — losing detail but retaining core capability.

---

<!-- section_id: "9071bf31-d958-48e6-8f3a-748828e3231e" -->
## Degradation Tiers

| Tier | Avenues Available | Agent Capability | Acceptable? |
|------|------------------|------------------|-------------|
| **Full** | All 8 functional | Complete context, optimal behavior | Ideal |
| **Good** | 5-7 functional | Most context available, minor gaps | Yes |
| **Adequate** | 3-4 functional | Core identity + some rules | Yes (with warnings) |
| **Minimal** | 1-2 functional | Identity only, no detailed guidance | Marginal |
| **Failed** | 0 functional | Agent has no entity context | No — escalate |

---

<!-- section_id: "693b9020-d839-40ee-a1f6-a38e6ae478de" -->
## Minimum Viable Context

An agent can function with just these elements:
1. **Identity**: Who am I? (role, scope, layer)
2. **Parent**: Where do I fit in the hierarchy?
3. **One rule source**: What constraints apply?

This minimum is achievable through any single avenue that provides identity:
- A1 (CLAUDE.md) provides identity via the cascade
- A4 (0AGNOSTIC.md) provides identity via the source of truth
- A6 (.integration.md) provides identity via the summary

---

<!-- section_id: "509af032-3631-4ca2-b36d-6388cc35bdcf" -->
## Failure Scenarios and Mitigations

| Scenario | Lost Avenue(s) | Mitigation |
|----------|---------------|-----------|
| Agent launched from wrong cwd | A1 (deep CLAUDE.md), A2 (path rules) | A4 (0AGNOSTIC chain) still works — agent reads it manually |
| .gab.jsonld has JSON error | A5 (JSON-LD) | A6 (.integration.md) provides same info in markdown |
| First session (no history) | A7 (episodic memory) | A1-A6, A8 all function — episodic is additive |
| .0agnostic/ not populated | A8 (agnostic system partially) | A1 (CLAUDE.md) + A5 (.gab.jsonld) provide core context |
| Tool doesn't support path rules | A2 (path rules) | A1 + A4 + A8 cover the same rules content |

---

<!-- section_id: "5e053814-7487-4219-af36-4c9907e9a40c" -->
## Design Implications

<!-- section_id: "59ab61dd-7c39-4a4e-b6f6-504e23c17cef" -->
### Avenue Overlap is Intentional

The 8 avenues intentionally overlap. This is not redundancy waste — it's resilience engineering. Each avenue delivers context through a different mechanism, so a failure in one mechanism doesn't cascade.

<!-- section_id: "b7022478-50bc-4ff6-b5d7-812c1edc389e" -->
### Paired Avenues

Some avenues function as pairs:
- **A5 + A6**: .gab.jsonld (structured) + .integration.md (readable) — same content, two formats
- **A1 + A4**: CLAUDE.md (generated, static) + 0AGNOSTIC.md (source, dynamic) — same identity, two delivery times
- **A2 + A8**: Path rules (auto-loaded) + .0agnostic/rules (manual read) — same rules, two loading mechanisms

If one member of a pair fails, the other provides coverage.

<!-- section_id: "87078d88-ba81-43ca-9f2e-c68247f26be0" -->
### Fail-Open vs Fail-Closed

The context chain system fails **open**: missing context means the agent operates with less guidance, not that it stops working. This is appropriate because:
- Missing rules → agent uses general best practices (acceptable)
- Missing mode constraints → agent operates without GAB structure (acceptable for simple tasks)
- Missing episodic → agent starts fresh (acceptable)

The exception is **identity**: if the agent cannot determine its role and scope, it should escalate to the user rather than guessing.

---

<!-- section_id: "f40996bb-61d1-4841-9e2b-2bc8fb2ade33" -->
## Related Principles

- Avenue Redundancy — redundancy is what enables graceful degradation
- Chain Continuity — the parent chain is the backbone; its failure is the most impactful
- Single Source of Truth — even in degraded mode, 0AGNOSTIC.md remains canonical
