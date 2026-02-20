# Context Avenue Web Registry

## Ordering Principle

Avenues are ordered from **most comprehensive** (can include everything) to **most fragmented** (scoped to specific events/paths).

## Avenues

| # | Avenue | Scope | What It Contains |
|---|--------|-------|------------------|
| 01 | `01_aalang/` | Full agent graphs | Complete `.gab.jsonld` orchestrators and agents — modes, actors, personas, constraints, transitions |
| 02 | `02_aalang_markdown_integration/` | Markdown summaries | `.integration.md` files — human-readable summaries of AALang graphs |
| 03 | `03_auto_memory/` | Persistent memory | Auto-memory files — operational learnings, patterns, gotchas that persist across sessions |
| 04 | `04_@import_references/` | Reference collections | `@imports/` reference files — curated content collections for context loading |
| 05 | `05_skills/` | Action-oriented | `SKILL.md` files — specific capabilities with WHEN/WHEN NOT conditions |
| 06 | `06_agents/` | Lightweight stubs | `.agent.jsonld` files — purpose-specific agent definitions |
| 07 | `07_path_specific_rules/` | Directory-scoped | Rules that apply to specific paths/directories |
| 08 | `08_hooks/` | Event-triggered | Hook scripts triggered by tool events (pre/post commit, file changes, etc.) |

## How to Use

- Read avenues in order when building a new entity's context web
- Each avenue is independent — not all entities need all avenues
- The registry tracks which avenues are populated for this entity
- To add a new avenue, insert it at the appropriate comprehensiveness level

## Current Population

| Avenue | Populated? | Notes |
|--------|-----------|-------|
| 01_aalang | **Yes** | 3 entity-level files (orchestrator, agent, stub). Stage AALang files live in each stage's own `.0agnostic/06_context_avenue_web/01_aalang/` |
| 02_aalang_markdown_integration | No | Integration MDs not yet created for this entity |
| 03_auto_memory | No | No entity-specific auto-memory yet |
| 04_@import_references | No | No @imports defined yet |
| 05_skills | No | No entity-specific skills yet |
| 06_agents | No | Agent stubs in `AALang_jsonld_agents/` at entity root |
| 07_path_specific_rules | No | No path-specific rules yet |
| 08_hooks | No | No hooks defined yet |
