---
resource_id: "6d1ca636-5f01-46f0-a14f-219aa21fa1cd"
resource_type: "output"
resource_name: "claude_md_audit"
---
# CLAUDE.md Chain Audit — Findings and Recommendations

## Date: 2026-02-07

## Summary

The CLAUDE.md chain is **over budget** (717 lines vs recommended <500) and full of duplication and ceremonial content. 298 CLAUDE.md files exist across the system with 15,363 total lines.

---

## Static Chain Analysis (Always Loaded)

These 5 files load into EVERY Claude Code session when working in `0_layer_universal/`:

| File | Lines | Key Content |
|------|-------|-------------|
| `~/.claude/CLAUDE.md` | **268** | 6 CRITICAL rules (verbose), layer-stage overview, AALang overview, compliance check, scenario table, AALang pseudo-code |
| `~/CLAUDE.md` | **115** | Key locations, **duplicate** CRITICAL rules, **duplicate** scenario table, AALang pseudo-code |
| `~/dawson-workspace/CLAUDE.md` | 54 | Sync awareness, key locations, AALang pseudo-code |
| `~/dawson-workspace/code/CLAUDE.md` | 55 | Code root, key locations, AALang pseudo-code |
| `0_layer_universal/CLAUDE.md` | **225** | Children table, **duplicate** universal rules, navigation tables, ASCII structure tree, session workflow, AALang pseudo-code |
| **TOTAL** | **717** | **Target: <400** |

---

## Bloat Sources Identified

### 1. Duplicate CRITICAL Rules (~100 lines wasted)

The 6 CRITICAL rules appear nearly identically in:
- `~/.claude/CLAUDE.md` (the authoritative location)
- `~/CLAUDE.md` (verbatim duplicate)
- `0_layer_universal/CLAUDE.md` (partial duplicate under "Universal Rules")

**Fix**: Keep rules in `~/.claude/CLAUDE.md` only. Other files inherit — Claude Code loads them in order.

### 2. Ceremonial AALang Pseudo-Code (~5,000-7,000 lines system-wide)

Every CLAUDE.md has a section like:
```markdown
## AALang Integration
@agent ctx:ContextLoadingAgent
### Context Chain Position
- Position: 1 of 5 (User Global)
- Parent: none (top of chain)
...
### On Load
ctx:ContextLoadingStateActor.loadedFiles += ~/.claude/CLAUDE.md
ctx:ContextConfidenceStateActor.rulesAwareness += 0.3
ctx:NavigationStateActor.depth = 0
```

This occupies 15-25 lines per file across 298 files. Claude Code's parser doesn't execute any of it. The `@agent`, `ctx:`, and state actor lines are purely aspirational.

**Fix**: Replace with 3-line references to actual JSON-LD files:
```markdown
## AALang
- **Orchestrator**: `layer_0_01_ai_manager_system/personal/layer_0_orchestrator.gab.jsonld`
- **Context loader**: `layer_0_03_context_agents/context_loading.gab.jsonld`
- **Skills**: `/context-gathering`, `/stage-workflow`
```

### 3. Large ASCII Diagrams (~65 lines in layer_0/CLAUDE.md alone)

`layer_0/CLAUDE.md` (206 lines) contains three ASCII diagrams:
- Session start protocol flowchart (~20 lines)
- Integration flow box diagram (~27 lines)
- Directory structure tree (~18 lines)

These are informative but don't need to be in static context. They should be @imported.

**Fix**: Move to `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/` and reference with @import directive.

### 4. Duplicate Navigation Tables

The stage list (01-11: request_gathering through archives) appears in at least 3 files. The sub-layer reference table appears in 2 files.

**Fix**: Define once in the deepest relevant file, don't repeat in parents.

---

## System-Wide Statistics

| Metric | Value |
|--------|-------|
| Total CLAUDE.md files | 298 |
| Total lines across all CLAUDE.md | 15,363 |
| Static chain files | 5 |
| Static chain lines | 717 |
| Recommended static chain max | ~500 |
| Estimated ceremonial AALang lines | 5,000-7,000 |
| Files with AALang pseudo-code | ~250+ |
| Root-level skills | 4 |
| Custom agents | 3 |
| Custom commands | 4 |
| `.claude/rules/` files | 0 (directory doesn't exist) |

---

## Recommendations

### Immediate (Tier 2 of adoption roadmap)

1. **Slim `~/.claude/CLAUDE.md`** (268 → ~120 lines): Condense CRITICAL rules to 3-5 lines each, move compliance check and scenario table to @imports
2. **Slim `~/CLAUDE.md`** (115 → ~30 lines): Remove ALL duplicate CRITICAL rules
3. **Slim `0_layer_universal/CLAUDE.md`** (225 → ~130 lines): Remove duplicate rules, move ASCII tree to @import
4. **Replace AALang pseudo-code** in all 5 static chain files with 3-line references

### Short-term (Tier 3)

5. **Create `.claude/rules/`** with path-specific rules (research, school, universal, aalang, development)
6. **Move verbose content to @imports** (compliance checklist, scenario rules, ASCII diagrams)

### Medium-term (Tier 4)

7. **Systematically replace AALang pseudo-code** across all 298 files with references to actual JSON-LD
8. **Create .integration.md companions** for key JSON-LD files

---

## Expected Impact

| Before | After |
|--------|-------|
| 717 lines static chain | ~350 lines |
| 15-25 lines AALang pseudo-code per file | 3-5 lines references per file |
| No path-specific rules | 5+ rules auto-loading by directory |
| Duplicate CRITICAL rules in 3 files | Rules defined once, inherited |
| 0 @import targets | 4+ @import files for verbose content |

---

*Audit conducted: 2026-02-07*
*Related: implementation_plan.md, adoption_roadmap.md*
