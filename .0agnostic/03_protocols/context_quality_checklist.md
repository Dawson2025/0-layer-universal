---
resource_id: "3bc2be2a-578f-4a06-abae-f1acf0fac2d8"
resource_type: "protocol"
resource_name: "context_quality_checklist"
---
# Context Quality Checklist

**Purpose**: Systematic verification before an agent begins work.

**When to Use**: After context loading, before task execution.

---

<!-- section_id: "a9c6907f-d0cb-4d35-a678-96d7158ff58d" -->
## Pre-Work Checklist

Complete this checklist before starting any task in the layer-stage system.

<!-- section_id: "bed86a0b-88c0-461c-8976-54656ca6ae0b" -->
### 1. Loading Quality

- [ ] CLAUDE.md chain loaded (from ~ to cwd)
- [ ] .claude/rules/*.md files loaded (if present)
- [ ] CLAUDE.local.md loaded (if present)
- [ ] No critical load errors

<!-- section_id: "9198099a-9a86-409c-bf55-25d13ba53999" -->
### 2. Position Quality

- [ ] Current layer identified: `layer_____`
- [ ] Current stage identified: `stage_____` (or N/A)
- [ ] Current sub_layer identified: `_____` (or N/A)
- [ ] Depth from 0_layer_universal: `_____`

<!-- section_id: "adc60267-d07b-4f2c-ac79-a1ca531be080" -->
### 3. Inheritance Quality

- [ ] Inheritance chain built: `[layer_0] → [layer_1] → ...`
- [ ] Parent layers loaded
- [ ] Override markers detected and recorded
- [ ] Conflicts resolved or escalated

<!-- section_id: "52b30b43-593a-4f49-ae56-0c20e856adb9" -->
### 4. Rules Quality

- [ ] sub_layer_0_02_rules loaded
- [ ] Universal rules identified
- [ ] Layer-specific rules identified
- [ ] No contradictory rules unresolved

<!-- section_id: "4ae0bc8a-494a-49b6-b781-c6ac049716dd" -->
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

<!-- section_id: "150bfe2b-23d4-42f2-9f86-4348575d8b62" -->
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

<!-- section_id: "214dbe5a-e9a1-4e6a-830f-cbb2b73733d5" -->
## If Checklist Fails

<!-- section_id: "62643f96-c271-4459-8ba8-a892071eb3a9" -->
### Confidence < 0.8

1. Identify which factor(s) are low
2. Load missing context
3. Re-calculate confidence
4. If still low, escalate to user

<!-- section_id: "93bd20ba-a1bf-487b-87e0-43f1ef4d5fb2" -->
### Unresolved Conflicts

1. List the conflicts
2. Show which layers conflict
3. Ask user which should take precedence
4. Record decision

<!-- section_id: "9ad55da9-5af9-4b74-8b37-f4a3a93dcad7" -->
### Missing Required Context

1. List missing files
2. Attempt to load them
3. If unavailable, warn user
4. Proceed with caution (if non-critical)

---

<!-- section_id: "b87c7bb9-8d97-493c-a54b-b8ba6323abdc" -->
## Checklist Shortcut

For experienced agents, the minimum check:

```
[ ] Layer known
[ ] Rules loaded
[ ] Confidence >= 0.8
[ ] Ready to work
```

---

<!-- section_id: "ff499850-c1a4-4859-97f9-e12eb45acc40" -->
## Related

- `context_loading_protocol.md` - Full protocol documentation
- `sub_layer_0_01_ai_system/context_agents/` - Agent definitions
