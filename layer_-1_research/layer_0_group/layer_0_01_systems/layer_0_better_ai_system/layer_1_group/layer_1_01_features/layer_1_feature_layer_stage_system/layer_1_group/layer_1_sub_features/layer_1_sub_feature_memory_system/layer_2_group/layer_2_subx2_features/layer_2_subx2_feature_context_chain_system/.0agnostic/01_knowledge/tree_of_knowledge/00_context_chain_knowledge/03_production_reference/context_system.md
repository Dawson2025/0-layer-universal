---
resource_id: "aa44f2fd-346a-43af-9856-34f5097bf593"
resource_type: "knowledge"
resource_name: "context_system"
---
# Production Context System

<!-- section_id: "f7267c21-36d4-4d98-baec-00ca73364846" -->
## Summary

The production context system is built on the agnostic architecture: `0AGNOSTIC.md` is the source of truth for every entity, `agnostic-sync.sh` generates tool-specific files (CLAUDE.md, AGENTS.md, etc.), and `.0agnostic/` holds on-demand resources (rules, knowledge, skills, agents, episodic memory). This three-tier architecture ensures consistent context across all AI tools while keeping static context lean.

Context loading happens through two independent mechanisms. The CLAUDE.md cascade is automatic: Claude Code walks upward from cwd to root, loading every CLAUDE.md it finds (static, every API call). The 0AGNOSTIC parent chain is manual: agents read 0AGNOSTIC.md and follow Parent references upward (dynamic, on-demand). Both produce context inheritance but at different times and costs. Triggers in 0AGNOSTIC.md (keyword, activity, path-based) tell agents when to load specific entity context.

The `.0agnostic/` directory contains numbered subdirectories: `01_knowledge/` (per-topic with principles, docs, resources), `02_rules/` (static always-apply + dynamic scenario-triggered), `03_protocols/`, `04_agents/`, `05_skills/`, `06_hooks/scripts/`, `07_episodic_memory/`, `04+_setup_dependant/`. This structure is replicated at every entity level in the hierarchy.

<!-- section_id: "686c6d15-bb69-4c0f-8f33-291c42108299" -->
## Key Concepts

- **0AGNOSTIC.md**: Source of truth; edit this, not generated files
- **agnostic-sync.sh**: Generates CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md from 0AGNOSTIC.md
- **CLAUDE.md cascade**: Static, automatic, filesystem walk (root to cwd)
- **0AGNOSTIC parent chain**: Dynamic, manual, explicit Parent references (leaf to root)
- **.0agnostic/ numbered dirs**: On-demand resources loaded when needed

<!-- section_id: "fd88f2e1-bb20-4942-8322-6525a0c77969" -->
## Reference Table

| What | Where | Notes |
|------|-------|-------|
| Production agnostic system | `.0agnostic/` | Live .0agnostic/ implementation |
| Root 0AGNOSTIC.md | `0AGNOSTIC.md` (repo root) | Top of the parent chain |
| agnostic-sync.sh | `.0agnostic/03_protocols/agnostic_sync_protocol/tools/agnostic-sync.sh` | The sync script |
| Entity structure template | `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md` | Canonical directory structure |
| HOW_CONTEXT_WORKS (full doc) | `.0agnostic/01_knowledge/overview/production_context_system/HOW_CONTEXT_WORKS.md` | Detailed walkthrough (copy, not canonical) |
