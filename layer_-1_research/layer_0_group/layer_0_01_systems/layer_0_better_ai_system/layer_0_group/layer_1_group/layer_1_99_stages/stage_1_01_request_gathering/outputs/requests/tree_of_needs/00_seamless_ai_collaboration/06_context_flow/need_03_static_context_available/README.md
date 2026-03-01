# Need: Static Context Available

## Parent Branch
`06_context_flow`

---

## Problem Statement

Static context (rules, principles, knowledge, structure) rarely changes but agents need reliable access to it. Currently:
- Agent might not know where rules live
- Knowledge is scattered and hard to find
- Principles exist but aren't loaded
- Structure/patterns aren't documented

---

## What We Need

**Static context** should be:
1. **Organized** - Clear locations for each type
2. **Discoverable** - Entry points tell agent where to find it
3. **Stable** - Rarely changes, can be cached/memorized
4. **Layered** - Universal rules vs project-specific rules

---

## Static Context Types

| Type | What It Is | Location Pattern | Changes |
|------|------------|------------------|---------|
| **Rules** | Must-follow constraints | `sub_layer_0_04_rules/` | Rarely |
| **Principles** | Guiding philosophy | `sub_layer_0_03_principles/` | Rarely |
| **Knowledge** | Domain information | `sub_layer_0_02_knowledge/` | Occasionally |
| **Structure** | How things are organized | `CLAUDE.md`, `index.jsonld` | Occasionally |
| **Skills** | Reusable capabilities | `.claude/skills/` | Occasionally |

---

## Solution: Static Context Hierarchy

```
Universal Static (Layer 0)
├── Rules that apply to ALL work
├── Principles that guide ALL decisions
└── Knowledge that's always relevant

Project Static (Layer 1+)
├── Project-specific rules
├── Project-specific knowledge
└── Project structure
```

### Access Pattern

```json
// In index.jsonld
"nav:staticContext": {
  "rules": {
    "universal": "../../../layer_0/sub_layer_0_04_rules/",
    "local": "./rules/"
  },
  "knowledge": {
    "universal": "../../../layer_0/sub_layer_0_02_knowledge/",
    "local": "./knowledge/"
  },
  "principles": "../../../layer_0/sub_layer_0_03_principles/"
}
```

---

## Success Criteria

- [ ] Agent can find universal rules within 2 navigation steps
- [ ] Agent knows difference between universal and local rules
- [ ] Knowledge is organized by topic, not by when it was added
- [ ] Agent doesn't re-read static files unnecessarily

---

## Related Needs

- `need_04_dynamic_context_available` - Counterpart: changing context
- `01_capable/need_01_persistent_knowledge` - Knowledge persistence

---

## Status

- **Priority**: Medium
- **Complexity**: Medium
- **Current State**: Sub-layer structure exists, needs better navigation
