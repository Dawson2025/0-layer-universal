---
resource_id: "840a3a99-507a-4844-8cc6-629bc64a0f8d"
resource_type: "knowledge"
resource_name: "lean_static_context"
---
# Principle: Lean Static Context

<!-- section_id: "c1806832-2763-43ef-b9d8-215bf890f852" -->
## Summary

Static context (loaded on every API call) must be kept minimal. Detail belongs in dynamic context (loaded on-demand). This is the most impactful optimization in the context chain system because static context has a multiplicative cost: tokens multiplied by the number of API calls in a session.

CLAUDE.md should contain only identity (3-5 lines), triggers (5-10 lines), and pointers (navigation table). Detailed rules, knowledge, skills content, agent definitions, and session history all belong in .0agnostic/ where they are read only when needed. Target CLAUDE.md at 30-80 lines for entities and 15-30 lines for containers. A healthy entity should have a dynamic-to-static ratio of 5:1 or higher.

The exception: critical safety rules, scope boundaries, and identity must stay static even if verbose, because skipping them on any API call could lead to incorrect behavior.

<!-- section_id: "75c28b93-2549-40bc-9a72-bd7e190236aa" -->
## Key Concepts

- **Multiplicative cost**: Static tokens are paid on every API call in a session
- **Target sizes**: CLAUDE.md 30-80 lines (entity), 15-30 lines (container)
- **What stays static**: Identity, triggers, pointers, critical safety rules
- **What goes dynamic**: Rules, knowledge, skills content, agent defs, episodic memory
- **Healthy ratio**: Dynamic content should be 5-10x the size of static content

<!-- section_id: "79a92abe-b843-4bd8-be1b-e2eedabf8bc6" -->
## Reference Table

| What | Where | Notes |
|------|-------|-------|
| Full principle doc | `.0agnostic/01_knowledge/principles/lean_static_context.md` | Size targets, audit steps, exceptions |
| Optimization strategies | `.0agnostic/01_knowledge/chain_optimization_strategies.md` | 6 strategies including lean CLAUDE.md |
| Static/dynamic dimensions | `.0agnostic/01_knowledge/static_dynamic_context.md` | Full 2x2 matrix and token budget |
