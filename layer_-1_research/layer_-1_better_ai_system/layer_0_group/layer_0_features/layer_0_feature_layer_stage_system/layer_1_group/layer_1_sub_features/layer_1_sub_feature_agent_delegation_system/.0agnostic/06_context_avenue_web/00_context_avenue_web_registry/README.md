# Context Avenue Web Registry

## Ordering Principle

Avenues are ordered from **most comprehensive** (can include everything) to **most fragmented** (scoped to specific events/paths).

## Avenues

| # | Avenue | Scope | What It Contains |
|---|--------|-------|------------------|
| 01 | `01_aalang/` | Full agent graphs | Complete `.gab.jsonld` orchestrators and agents — modes, actors, personas, constraints, transitions |
| 02 | `02_aalang_markdown_integration/` | Markdown summaries | `.integration.md` files — human-readable summaries of AALang graphs |
| 03 | `03_@import_references/` | Reference collections | `@imports/` reference files — curated content collections for context loading |
| 04 | `04_skills/` | Action-oriented | `SKILL.md` files — specific capabilities with WHEN/WHEN NOT conditions |
| 05 | `05_agents/` | Lightweight stubs | `.agent.jsonld` files — purpose-specific agent definitions |
| 06 | `06_path_specific_rules/` | Directory-scoped | Rules that apply to specific paths/directories |
| 07 | `07_hooks/` | Event-triggered | Hook scripts triggered by tool events (pre/post commit, file changes, etc.) |

## How to Use

- Read avenues in order when building a new entity's context web
- Each avenue is independent — not all entities need all avenues
- The registry tracks which avenues are populated for this entity
- To add a new avenue, insert it at the appropriate comprehensiveness level

## Current Population

| Avenue | Populated? | Notes |
|--------|-----------|-------|
| 01_aalang | No | Entity-level AALang lives in `AALang_jsonld_agents/` at entity root |
| 02_aalang_markdown_integration | No | Integration MDs not yet created for this entity |
| 03_@import_references | No | No @imports defined yet |
| 04_skills | No | No entity-specific skills yet |
| 05_agents | No | Agent stubs in `AALang_jsonld_agents/` at entity root |
| 06_path_specific_rules | No | No path-specific rules yet |
| 07_hooks | No | No hooks defined yet |
