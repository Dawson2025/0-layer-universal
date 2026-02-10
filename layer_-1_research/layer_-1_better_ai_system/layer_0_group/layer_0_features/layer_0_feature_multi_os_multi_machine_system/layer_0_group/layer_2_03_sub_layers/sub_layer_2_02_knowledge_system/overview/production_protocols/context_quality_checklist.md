# Context Quality Checklist

**Purpose**: Systematic verification before an agent begins work.

**When to Use**: After context loading, before task execution.

---

## Pre-Work Checklist

Complete this checklist before starting any task in the layer-stage system.

### 1. Loading Quality

- [ ] CLAUDE.md chain loaded (from ~ to cwd)
- [ ] .claude/rules/*.md files loaded (if present)
- [ ] CLAUDE.local.md loaded (if present)
- [ ] No critical load errors

### 2. Position Quality

- [ ] Current layer identified: `layer_____`
- [ ] Current stage identified: `stage_____` (or N/A)
- [ ] Current sub_layer identified: `_____` (or N/A)
- [ ] Depth from 0_layer_universal: `_____`

### 3. Inheritance Quality

- [ ] Inheritance chain built: `[layer_0] → [layer_1] → ...`
- [ ] Parent layers loaded
- [ ] Override markers detected and recorded
- [ ] Conflicts resolved or escalated

### 4. Rules Quality

- [ ] sub_layer_0_04_rules loaded
- [ ] Universal rules identified
- [ ] Layer-specific rules identified
- [ ] No contradictory rules unresolved

### 5. Confidence Quality

| Factor | Score | Threshold |
|--------|-------|-----------|
| Layer Identified | ___/1.0 | >= 0.8 |
| Stage Identified | ___/1.0 | >= 0.8 (or N/A) |
| Rules Awareness | ___/1.0 | >= 0.8 |
| Inheritance Resolved | ___/1.0 | >= 0.8 |
| Required Context Loaded | ___/1.0 | >= 0.8 |
| **Overall** | ___/1.0 | **>= 0.8** |

---

## Quick Self-Check

Before starting work, agent should be able to answer:

1. **Where am I?**
   - Layer: _____
   - Stage: _____
   - Path: _____

2. **What do I inherit?**
   - From: _____
   - Key rules: _____

3. **What can I override?**
   - Layers I can override: _____
   - Any overrides active: _____

4. **What rules apply?**
   - Universal rules: _____
   - Layer-specific: _____
   - Any conflicts: _____

5. **Am I ready?**
   - Overall confidence: _____
   - Missing context: _____

---

## If Checklist Fails

### Confidence < 0.8

1. Identify which factor(s) are low
2. Load missing context
3. Re-calculate confidence
4. If still low, escalate to user

### Unresolved Conflicts

1. List the conflicts
2. Show which layers conflict
3. Ask user which should take precedence
4. Record decision

### Missing Required Context

1. List missing files
2. Attempt to load them
3. If unavailable, warn user
4. Proceed with caution (if non-critical)

---

## Checklist Shortcut

For experienced agents, the minimum check:

```
[ ] Layer known
[ ] Rules loaded
[ ] Confidence >= 0.8
[ ] Ready to work
```

---

## Related

- `context_loading_protocol.md` - Full protocol documentation
- `sub_layer_0_01_ai_system/context_agents/` - Agent definitions
