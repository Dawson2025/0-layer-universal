# Protocol: Avenue Audit

**Purpose**: Verify that all 8 context delivery avenues are functional for a given entity.

---

## When to Use

- After creating a new entity
- After populating `.0agnostic/` content
- When avenue coverage seems incomplete
- Periodic health check on established entities

## Steps

### Step 1: Check Avenue 1 — System Prompt (CLAUDE.md)

```bash
test -f CLAUDE.md && grep -q "## Identity" CLAUDE.md && echo "A1: PASS" || echo "A1: FAIL"
```

Verify it was generated (has auto-generated footer), not hand-edited.

### Step 2: Check Avenue 2 — Path Rules

```bash
count=$(find .claude/rules/ -name "*.md" -not -name ".gitkeep" | wc -l)
[ "$count" -gt 0 ] && echo "A2: PASS ($count rules)" || echo "A2: SCAFFOLDED"
```

### Step 3: Check Avenue 3 — Skills

```bash
count=$(find .0agnostic/skills/ -name "SKILL.md" | wc -l)
# Also check .claude/skills/ if it exists
[ "$count" -gt 0 ] && echo "A3: PASS ($count skills)" || echo "A3: SCAFFOLDED"
```

### Step 4: Check Avenue 4 — Parent References

```bash
grep -q "Parent" 0AGNOSTIC.md && echo "A4: PASS" || echo "A4: FAIL"
```

Then validate the parent path resolves (see Chain Validation Protocol).

### Step 5: Check Avenue 5 — JSON-LD Agent Definitions

```bash
gab=$(find . -maxdepth 1 -name "*.gab.jsonld" | head -1)
if [ -n "$gab" ]; then
  jq empty "$gab" 2>/dev/null && echo "A5: PASS" || echo "A5: FAIL (invalid JSON)"
else
  echo "A5: SCAFFOLDED"
fi
```

### Step 6: Check Avenue 6 — Integration Summaries

```bash
integ=$(find . -maxdepth 1 -name "*.integration.md" | head -1)
[ -n "$integ" ] && [ "$(wc -l < "$integ")" -gt 5 ] && echo "A6: PASS" || echo "A6: SCAFFOLDED"
```

### Step 7: Check Avenue 7 — Episodic Memory

```bash
sessions=$(find .0agnostic/episodic_memory/sessions/ -name "*.md" -not -name ".gitkeep" | wc -l)
[ "$sessions" -gt 0 ] && echo "A7: PASS ($sessions sessions)" || echo "A7: SCAFFOLDED (expected for new entities)"
```

### Step 8: Check Avenue 8 — Agnostic System

```bash
rules=$(find .0agnostic/rules/ -name "*.md" -not -name ".gitkeep" | wc -l)
knowledge=$(find .0agnostic/knowledge/ -name "*.md" -not -name ".gitkeep" | wc -l)
[ "$rules" -gt 0 ] && [ "$knowledge" -gt 0 ] && echo "A8: PASS ($rules rules, $knowledge knowledge)" || echo "A8: SCAFFOLDED"
```

### Step 9: Report Summary

```
Avenue Coverage Report for: [entity-name]
──────────────────────────────────────────
A1 System Prompt:     PASS
A2 Path Rules:        PASS (1 rule)
A3 Skills:            PASS (2 skills)
A4 Parent References: PASS (7-level chain)
A5 JSON-LD:           PASS (valid, 38 @graph entries)
A6 Integration:       PASS (38 lines)
A7 Episodic Memory:   SCAFFOLDED (new entity)
A8 Agnostic System:   PASS (7 rules, 9 knowledge)
──────────────────────────────────────────
Result: 7/8 PASS, 1 SCAFFOLDED, 0 FAIL
```

## Success Criteria

- 6+ avenues PASS for an established entity
- 5+ avenues PASS for a newly created entity
- A7 (Episodic) may be SCAFFOLDED on new entities
- Zero FAIL on avenues A1, A4, A5 (critical path)
