---
resource_id: "83cbdd61-78fc-4337-a82a-0d81069ce7d8"
resource_type: "document"
resource_name: "context_quality_checklist"
---
# Context Quality Checklist

**Purpose**: Systematic verification before an agent begins work.

**When to Use**: After context loading, before task execution.

---

<!-- section_id: "6cffb359-6378-4332-a1e1-c0a639081275" -->
## Pre-Work Checklist

Complete this checklist before starting any task in the layer-stage system.

<!-- section_id: "043580a9-a3b1-4226-99e0-5ee54ceda1b2" -->
### 1. Loading Quality

- [ ] CLAUDE.md chain loaded (from ~ to cwd)
- [ ] .claude/rules/*.md files loaded (if present)
- [ ] CLAUDE.local.md loaded (if present)
- [ ] No critical load errors

<!-- section_id: "872e371e-748b-43eb-bb56-20ef9f805e00" -->
### 2. Position Quality

- [ ] Current layer identified: `layer_____`
- [ ] Current stage identified: `stage_____` (or N/A)
- [ ] Current sub_layer identified: `_____` (or N/A)
- [ ] Depth from 0_layer_universal: `_____`

<!-- section_id: "40f7f0f2-e472-4480-8c5c-f78189e44c8c" -->
### 3. Inheritance Quality

- [ ] Inheritance chain built: `[layer_0] → [layer_1] → ...`
- [ ] Parent layers loaded
- [ ] Override markers detected and recorded
- [ ] Conflicts resolved or escalated

<!-- section_id: "f1deed22-62c7-4130-a03d-2037b363507f" -->
### 4. Rules Quality

- [ ] sub_layer_0_04_rules loaded
- [ ] Universal rules identified
- [ ] Layer-specific rules identified
- [ ] No contradictory rules unresolved

<!-- section_id: "824ff794-f5ed-47de-8192-622267fb8623" -->
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

<!-- section_id: "c464efa9-8f36-46eb-a473-8457e401e364" -->
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

<!-- section_id: "e09eb17c-37aa-4fed-9291-173bf365c27d" -->
## If Checklist Fails

<!-- section_id: "73c61448-17b4-40d0-a09b-08aee1435713" -->
### Confidence < 0.8

1. Identify which factor(s) are low
2. Load missing context
3. Re-calculate confidence
4. If still low, escalate to user

<!-- section_id: "84c9747a-51e7-4c6c-84db-86f449812d03" -->
### Unresolved Conflicts

1. List the conflicts
2. Show which layers conflict
3. Ask user which should take precedence
4. Record decision

<!-- section_id: "de66f1e2-82e2-4aae-847f-8277aec368a1" -->
### Missing Required Context

1. List missing files
2. Attempt to load them
3. If unavailable, warn user
4. Proceed with caution (if non-critical)

---

<!-- section_id: "6bf5bb14-cb96-40a4-b323-ab87c40d9a15" -->
## Checklist Shortcut

For experienced agents, the minimum check:

```
[ ] Layer known
[ ] Rules loaded
[ ] Confidence >= 0.8
[ ] Ready to work
```

---

<!-- section_id: "d30c55f8-c6ed-44d5-b239-a226a077e3c8" -->
## Related

- `context_loading_protocol.md` - Full protocol documentation
- `sub_layer_0_01_ai_system/context_agents/` - Agent definitions
