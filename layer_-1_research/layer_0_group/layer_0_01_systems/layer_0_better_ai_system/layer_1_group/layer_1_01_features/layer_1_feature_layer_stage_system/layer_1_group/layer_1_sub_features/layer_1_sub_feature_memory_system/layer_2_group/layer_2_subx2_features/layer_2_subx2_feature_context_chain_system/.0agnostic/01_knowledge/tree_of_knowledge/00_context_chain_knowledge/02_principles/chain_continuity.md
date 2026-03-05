---
resource_id: "b4051837-bb3e-4b77-a453-61deb1a549ad"
resource_type: "knowledge"
resource_name: "chain_continuity"
---
# Principle: Chain Continuity

<!-- section_id: "807578d8-01d1-479f-a003-59e5430d4091" -->
## Summary

Every entity in the layer-stage system must maintain an unbroken parent reference chain from itself to the system root. A broken chain means an entity is orphaned -- it cannot inherit context, rules, or knowledge from its ancestors, and agents cannot traverse upward for escalation or scope validation.

The parent chain is the backbone of context inheritance. When an agent arrives at an entity, it reads 0AGNOSTIC.md for local identity, follows the Parent reference for broader scope, and continues upward to understand the full hierarchy. If any link is broken, the agent works with incomplete context, leading to missing inherited rules, incorrect scope assumptions, and failed escalation paths.

Container directories (groups, feature registries) must have 0AGNOSTIC.md even if minimal. Never delete an 0AGNOSTIC.md that is referenced as a parent. Never create an entity without establishing its parent reference. Recovery from a chain break involves creating a minimum viable 0AGNOSTIC.md with Identity + Parent, running agnostic-sync.sh, and re-testing.

<!-- section_id: "b86a2554-0ab8-42c3-9045-901180865096" -->
## Key Concepts

- **Every entity needs a Parent line** (except the root)
- **Parent paths must resolve** to existing 0AGNOSTIC.md files with Identity sections
- **Containers need 0AGNOSTIC.md too** -- even if minimal, they maintain the chain
- **Never delete** a 0AGNOSTIC.md that is referenced as a parent by any child
- **Tested by**: `test_context_chain_traversal.sh` -- walks full chain, verifies each link

<!-- section_id: "6ec08e7c-2366-417a-a43d-e00e67687de0" -->
## Reference Table

| What | Where | Notes |
|------|-------|-------|
| Full principle doc | `.0agnostic/01_knowledge/principles/chain_continuity.md` | Requirements, verification, recovery steps |
| Chain architecture | `.0agnostic/01_knowledge/context_chain_architecture.md` | How chains are constructed |
| Chain traversal test | `layer_2_99_stages/stage_2_07_testing/outputs/test_context_chain_traversal.sh` | Automated chain validation |
