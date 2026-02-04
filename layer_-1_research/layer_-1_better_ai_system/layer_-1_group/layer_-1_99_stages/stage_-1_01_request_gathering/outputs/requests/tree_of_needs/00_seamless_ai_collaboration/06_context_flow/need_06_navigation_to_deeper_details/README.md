# Need: Navigation to Deeper Details

## Parent Branch
`06_context_flow`

---

## Problem Statement

After reading the entry point, agents need to find deeper details. Currently:
- Links may be broken or outdated
- Navigation paths aren't clear
- Agent doesn't know which file has what
- Folder structures are complex and hard to traverse

**Result**: Agent either:
- Reads too much (wasting context)
- Reads too little (missing critical info)
- Gets lost in folder structures

---

## What We Need

Clear **navigation paths** from entry point to any needed resource:

```
Entry Point
    │
    ├──→ Rules (which rule file?)
    │        └──→ Specific rule (modification protocol)
    │
    ├──→ Knowledge (which topic?)
    │        └──→ Specific knowledge (domain X)
    │
    ├──→ Skills (which skill?)
    │        └──→ Skill details (how to use)
    │
    └──→ State (what's current?)
             └──→ History (what happened before?)
```

---

## Solution: Multi-Level Navigation

### Level 1: Category Navigation (Entry Point)
```json
"nav:categories": {
  "rules": {"@id": "sub_layer_0_04_rules/", "index": "0INDEX.md"},
  "knowledge": {"@id": "sub_layer_0_02_knowledge/", "index": "0INDEX.md"},
  "skills": {"@id": ".claude/skills/", "index": "index.jsonld"},
  "stages": {"@id": "layer_0_99_stages/", "index": "index.jsonld"}
}
```

### Level 2: Index Files (Per Category)
Each category has an index that lists contents:

```markdown
<!-- sub_layer_0_04_rules/0INDEX.md -->
# Rules Index

| Rule | Purpose | When to Read |
|------|---------|--------------|
| AI_CONTEXT_MODIFICATION_PROTOCOL.md | How to modify context files | Before any context changes |
| safety_governance.md | Security principles | Security decisions |
| FILE_PATH_LINKING_RULE.md | Include file paths | After creating files |
```

### Level 3: Individual Resources
Each resource is self-contained with:
- Purpose at top
- Full content
- Related resources linked

---

## Navigation Patterns

### Pattern 1: Drill-Down
```
Need: Find the rule for modifying CLAUDE.md

Entry Point
  → nav:rules → sub_layer_0_04_rules/
    → 0INDEX.md → Find "modification"
      → AI_CONTEXT_MODIFICATION_PROTOCOL.md
```

### Pattern 2: Trigger-Based
```
Trigger: Entering stage_01_request_gathering

Entry Point
  → trigger:onStageWork → pattern match
    → .claude/skills/01_request_gathering-workflow/
      → SKILL.md (workflow details)
```

### Pattern 3: Search (via JSON-LD)
```
Query: Find all skills

Entry Point (index.jsonld)
  → nav:skills → .claude/skills/index.jsonld
    → skills[] → list of all skills with descriptions
```

---

## Index File Requirements

Every navigable folder should have an index:

| Folder Type | Index File | Contents |
|-------------|------------|----------|
| Rules | `0INDEX.md` | Rule list with purposes |
| Knowledge | `0INDEX.md` | Topic list with summaries |
| Skills | `index.jsonld` | Skill list with triggers |
| Stages | `index.jsonld` | Stage list with workflows |
| Episodic | `index.md` | Recent sessions, decisions |

---

## JSON-LD Navigation Advantages

```json
// Agent can programmatically traverse
{
  "nav:children": [
    {"@id": "child1/", "@type": "Feature", "name": "Child 1"},
    {"@id": "child2/", "@type": "Stage", "name": "Child 2"}
  ]
}

// vs. parsing markdown:
// "Children: child1/, child2/"
```

Benefits:
- Links are explicit `@id` references
- Types help agent understand what it's navigating to
- Can build navigation graph programmatically

---

## Success Criteria

- [ ] Every folder has an index file
- [ ] Agent can reach any resource in ≤ 3 navigation steps
- [ ] Links in index files are validated (no broken links)
- [ ] Navigation is consistent across all entities
- [ ] Agent can explain its navigation path

---

## Related Needs

- `need_05_entry_points_right_detail` - Starting point for navigation
- `need_02_context_propagation_works` - Overall context flow

---

## Status

- **Priority**: Medium
- **Complexity**: Medium
- **Prototype**: JSON-LD index files demonstrate this pattern
