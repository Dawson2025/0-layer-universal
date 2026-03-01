# Chain Optimization Strategies

**Layer**: layer_2 (Research Sub-Feature)
**Stage**: 05_design
**Date**: 2026-02-17
**Topic**: Practical strategies for keeping context chains efficient

---

## Overview

Context chains have a direct cost: every static token is sent on every API call. A 7-level deep chain with verbose CLAUDE.md files at each level could consume thousands of tokens per call. This document captures strategies for keeping chains efficient while maintaining full functionality.

---

## Strategy 1: Lean CLAUDE.md, Rich .0agnostic/

The most impactful optimization. CLAUDE.md is static (always loaded). .0agnostic/ is dynamic (loaded on-demand).

| Content Type | Put in CLAUDE.md | Put in .0agnostic/ |
|-------------|-----------------|-------------------|
| Identity (role, scope, parent) | Yes | No (redundant) |
| Triggers (when to activate) | Yes | No (needed for matching) |
| Pointers (where to find more) | Yes | No (needed for navigation) |
| Detailed rules | No | Yes (rules/) |
| Knowledge documents | No | Yes (knowledge/) |
| Skills | Listing only | Yes (skills/SKILL.md) |
| Agent definitions | No | Agent reads .gab.jsonld |
| Session history | No | Yes (episodic_memory/) |

**Target**: CLAUDE.md should be 30-80 lines. Everything else goes to .0agnostic/.

---

## Strategy 2: Pointer-Based Navigation

Instead of embedding content, embed **pointers** to content:

```markdown
## Pointers
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_4_group/layer_4_subx4_features/` for sub-features

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../../0AGNOSTIC.md` |
| Stages | `layer_3_group/layer_3_99_stages/` |
| Children | `layer_4_group/layer_4_subx4_features/` |
```

This costs ~10 tokens in CLAUDE.md vs ~500+ tokens for inline content.

---

## Strategy 3: Agnostic-Sync Section Extraction

`agnostic-sync.sh` extracts only specific h2 sections from 0AGNOSTIC.md into CLAUDE.md:
- Identity (required)
- Navigation (optional, extracted if present)
- Critical Rules (optional)
- Key Behaviors (optional)
- Triggers (optional)

Sections NOT in this list are **not** copied to CLAUDE.md. Use this to keep research notes, design discussions, and detailed documentation in 0AGNOSTIC.md without inflating the static context.

---

## Strategy 4: Container Node Minimalism

Container nodes (layer_N_group/, layer_N_features/) should have the absolute minimum context:

```markdown
# 0AGNOSTIC.md - layer_0_group

## Identity
Internal structure container for the better_ai_system project.
- **Parent**: `../0AGNOSTIC.md` (layer_-1_better_ai_system)

## Triggers
Load this context when:
- Navigating the internal structure of better_ai_system
- Entering: `layer_0_group/`
```

**Target**: Container 0AGNOSTIC.md should be 10-20 lines. They exist for chain continuity, not content.

---

## Strategy 5: Dynamic Chain Walking

Rather than pre-loading the full chain, walk it on-demand:

| Approach | Token Cost | When to Use |
|----------|-----------|-------------|
| Full pre-load | High (sum of all levels) | Debugging, validation |
| Walk-to-depth-N | Medium (first N levels) | Normal work (N=2-3) |
| Current + parent only | Low (2 levels) | Focused tasks |
| Current only | Minimal (1 level) | Quick edits |

Most work only needs the current entity + its immediate parent. Deep chain walks should be reserved for scope validation and cross-entity coordination.

---

## Strategy 6: Integration Summaries as Cache

`.integration.md` files serve as a **cached summary** of `.gab.jsonld`:
- .gab.jsonld: ~800 lines, ~2000 tokens, requires jq parsing
- .integration.md: ~40 lines, ~200 tokens, plain markdown

For most tasks, reading the integration summary is sufficient. Only query the full .gab.jsonld when you need precise mode constraints or actor definitions.

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It's Bad | Alternative |
|-------------|-------------|-------------|
| Inline documentation in CLAUDE.md | Inflates static cost | Move to .0agnostic/knowledge/ |
| Duplicating parent context in child | Double token cost | Use Parent: reference |
| Loading full chain on every task | Wastes tokens | Walk only needed depth |
| Verbose container 0AGNOSTIC.md | Containers route, don't inform | Keep to ~15 lines |
| Skipping agnostic-sync after edits | Stale CLAUDE.md | Always sync after changes |

---

## Measurement

Track optimization effectiveness with:

```bash
# Count static tokens per entity
wc -w CLAUDE.md  # rough token estimate (words ≈ 1.3x tokens)

# Count chain total
for f in $(chain-walk 0AGNOSTIC.md); do wc -w "$f"; done | awk '{s+=$1} END {print s}'

# Compare static vs dynamic ratio
static=$(wc -w CLAUDE.md | awk '{print $1}')
dynamic=$(find .0agnostic/ -name "*.md" -exec wc -w {} + | tail -1 | awk '{print $1}')
echo "Static: $static, Dynamic: $dynamic, Ratio: $(echo "scale=1; $dynamic/$static" | bc):1"
```

**Target ratio**: Dynamic content should be 5-10x the size of static content. If static ≥ dynamic, the chain is not using on-demand loading effectively.

---

## Related Documents

- Static vs dynamic context: `./static_dynamic_context.md`
- Context chain architecture: `./context_chain_architecture.md`
- How context works: `sub_layer_3_01_knowledge_system/overview/production_context_system/HOW_CONTEXT_WORKS.md`
