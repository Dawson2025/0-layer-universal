---
resource_id: "f78b8704-87f3-4067-9762-07642cbb1e36"
resource_type: "knowledge"
resource_name: "lean_static_context"
---
# Principle: Lean Static Context

**Type**: Efficiency
**Severity**: High
**Date**: 2026-02-17

---

## Statement

**Static context (loaded on every API call) must be kept minimal. Push detail into dynamic context (loaded on-demand) to reduce per-call token cost.**

---

## Rationale

Claude Code's context architecture has a critical asymmetry:

- **Static context** (CLAUDE.md chain, MCP schemas, skill listings, auto memory) is included in **every single API message**. A 1,000-token CLAUDE.md costs 1,000 tokens per call, whether the content is relevant to that call or not.

- **Dynamic context** (tool results, skill content, .0agnostic/ reads) only enters context when the agent explicitly invokes it. A 5,000-token knowledge document costs 0 tokens unless the agent reads it.

This means static context has a **multiplicative cost** (tokens × number of API calls), while dynamic context has a **one-time cost** (tokens × 1 per read).

---

## The Rule

| Content | Static (CLAUDE.md) | Dynamic (.0agnostic/) |
|---------|--------------------|-----------------------|
| Identity (who am I) | Yes — 3-5 lines | No |
| Triggers (when to activate) | Yes — 5-10 lines | No |
| Pointers (where to find more) | Yes — table of paths | No |
| Detailed rules | No | Yes (rules/) |
| Knowledge documents | No | Yes (knowledge/) |
| Skill content | Listing only (name + when) | Yes (SKILL.md) |
| Agent constraints | No | Yes (.gab.jsonld) |
| Session history | No | Yes (episodic_memory/) |

### Target Sizes

| File | Target | Acceptable | Too Large |
|------|--------|-----------|-----------|
| CLAUDE.md (entity) | 30-80 lines | 80-150 lines | >150 lines |
| CLAUDE.md (container) | 15-30 lines | 30-50 lines | >50 lines |
| 0AGNOSTIC.md | 20-50 lines | 50-100 lines | >100 lines |
| Auto memory (MEMORY.md) | 50-100 lines | 100-200 lines | >200 lines (truncated) |

---

## How to Apply

### Step 1: Audit current CLAUDE.md

```bash
wc -l CLAUDE.md  # should be <80 for entities, <30 for containers
```

### Step 2: Identify bloat

Look for sections that should be dynamic:
- Detailed instructions (→ .0agnostic/rules/)
- Reference documentation (→ .0agnostic/knowledge/)
- Examples and code snippets (→ .0agnostic/knowledge/)
- Historical context (→ .0agnostic/episodic_memory/)

### Step 3: Move to dynamic

1. Create the appropriate .0agnostic/ file
2. Replace inline content with a pointer in 0AGNOSTIC.md
3. Run `agnostic-sync.sh` to regenerate CLAUDE.md

### Step 4: Verify

```bash
# Check reduction
wc -l CLAUDE.md
# Verify pointer resolves
cat .0agnostic/[target-file]
```

---

## Dynamic-to-Static Ratio

A healthy entity should have a dynamic-to-static ratio of **5:1 or higher**:

```
Dynamic content (.0agnostic/):  ~2,000 lines
Static content (CLAUDE.md):     ~50 lines
Ratio:                          40:1 ✓
```

If the ratio is below 3:1, the entity is likely including too much in static context.

---

## Exceptions

Some content must stay static even if it's verbose:
- **Critical safety rules** that must be visible on every call
- **Scope boundaries** that prevent out-of-scope work
- **Identity** that establishes the agent's role

When in doubt: if skipping the content on one API call could lead to incorrect behavior, keep it static.

---

## Related Principles

- Chain Optimization Strategies — practical techniques for applying this principle
- Avenue Redundancy — dynamic content should still be reachable via multiple avenues
