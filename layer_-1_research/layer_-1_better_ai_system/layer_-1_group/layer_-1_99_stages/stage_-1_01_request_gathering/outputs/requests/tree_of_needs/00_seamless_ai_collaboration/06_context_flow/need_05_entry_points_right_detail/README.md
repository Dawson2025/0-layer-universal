# Need: Entry Points Have Right Detail

## Parent Branch
`06_context_flow`

---

## Problem Statement

Entry point files (CLAUDE.md, index.jsonld) are the first thing an agent reads. They need to contain **just enough** information to:
1. Establish identity and role
2. Communicate critical rules
3. Direct to more detailed resources

**The Goldilocks Problem:**
- **Too sparse**: Agent doesn't know what to do or where to go
- **Too verbose**: Context window overflow, agent overwhelmed, key info buried
- **Just right**: Agent knows identity, critical rules, and how to find more

---

## What We Need

Entry points should be **minimal but complete** - containing:

| Must Include | Why |
|--------------|-----|
| Identity | Who am I? What's my role? |
| Critical Rules | What must I always do? (2-5 rules max) |
| Triggers | When should I load what? |
| Pointers | Where do I go for more detail? |

| Should NOT Include | Why |
|--------------------|-----|
| Full rule text | Point to rules/, let agent read when needed |
| Complete knowledge | Point to knowledge/, load on-demand |
| Detailed procedures | Point to skills/, invoke when relevant |
| Historical information | Point to episodic/, read if needed |

---

## Target Metrics

| Metric | Target | Rationale |
|--------|--------|-----------|
| Token count | < 500 tokens | Fits easily in context |
| Rules listed | 2-5 critical only | More = read rules/ |
| Navigation links | 5-10 pointers | Cover main destinations |
| Load time (cognitive) | < 10 seconds | Agent understands quickly |

---

## Solution: Entry Point Template

### CLAUDE.md (Human-Readable)
```markdown
# Entity Name

## Identity
You are [role] at [layer/location].
- **Scope**: [what you handle]
- **Parent**: [link]
- **Children**: [links]

## Critical Rules (ALWAYS FOLLOW)
1. [Most important rule - 1 line]
2. [Second most important - 1 line]
3. [Third - 1 line]

Full rules: `path/to/rules/`

## Triggers
| When | Load |
|------|------|
| Session start | status.json, episodic/index.md |
| Stage work | .claude/skills/{stage}-workflow/ |
| Creating entity | .claude/skills/entity-creation/ |

## Navigation
| Need | Location |
|------|----------|
| Rules | sub_layer_0_04_rules/ |
| Knowledge | sub_layer_0_02_knowledge/ |
| Skills | .claude/skills/ |
| Current state | status.json |
```

### index.jsonld (Machine-Readable)
```json
{
  "@id": "entity_name",
  "@type": "Feature",
  "name": "...",
  "layer": 0,

  "nav:parent": {"@id": "../"},
  "nav:children": [...],
  "nav:rules": {"@id": "rules/"},
  "nav:knowledge": {"@id": "knowledge/"},
  "nav:skills": {"@id": ".claude/skills/"},
  "nav:status": {"@id": "status.json"},

  "trigger:onSessionStart": [...],
  "trigger:onStageWork": {...}
}
```

---

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| Embedding full rules | Bloats entry point | Summarize + link |
| Listing every file | Overwhelming | Group by purpose |
| No navigation | Agent lost | Add nav: links |
| Prose descriptions | Hard to parse | Use tables/JSON |
| Duplicate info | Inconsistency risk | Single source of truth |

---

## Success Criteria

- [ ] Entry point fits in 500 tokens
- [ ] Agent can identify its role in < 5 seconds
- [ ] Agent knows where to find more detail
- [ ] Critical rules are visible without scrolling
- [ ] Navigation covers all main destinations

---

## Related Needs

- `need_02_context_propagation_works` - How context flows from entry point
- `need_06_navigation_to_deeper_details` - What happens after entry point

---

## Status

- **Priority**: High
- **Complexity**: Medium
- **Current State**: CLAUDE.md files exist but vary in detail level
