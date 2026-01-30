# Context System Problems

**Date**: 2026-01-25
**Source**: AI System Audit

---

## Problem Summary

Context gathering and management for AI agents is fragmented, with rules scattered across multiple locations and unclear priority/scope definitions.

---

## Major Problems

### 1. Context Gathering Rules Scattered
**Severity**: MAJOR

Context gathering rules exist in multiple places:

| Location | Content |
|----------|---------|
| `layer_0_01_ai_manager_system/agnostic/context_gathering_rules.md` | Main rules |
| `layer_2_feature_context_gathering/` (in layer_stage_system) | Feature definition |
| Various READMEs | Inline context guidance |

**Impact**: No single authoritative source for context rules.

---

### 2. Agnostic/Specific Pattern Incomplete
**Severity**: MAJOR

**Structure**:
```
layer_0_01_ai_manager_system/
├── agnostic/
│   ├── context_gathering_rules.md
│   ├── init_prompt.md
│   └── layer_navigation.md
└── specific/
    └── os/wsl/... (deeply nested, sparse)
```

**Problems**:
- No clear guidance on when to use agnostic vs specific
- Specific is deeply nested but has little content
- Pattern not documented

---

### 3. Multiple CLAUDE.md Entry Points
**Severity**: MINOR

**CLAUDE.md files exist at**:
- Root level
- Layer_0 level
- Each feature
- `.claude/` directory structure

**Problems**:
- Agents don't know which to read first
- No defined chain for context loading
- Potential for conflicting guidance

---

### 4. Context Gathering Skill Issues
**Severity**: MINOR

**Location**: `.claude/skills/context-gathering`

**Problems**:
- References old `0_context` structure
- No bridge documentation to new system
- May not work with current structure

---

### 5. Layer Navigation Incomplete
**Severity**: MINOR

**File**: `layer_0_01_ai_manager_system/agnostic/layer_navigation.md`

**Problems**:
- Vertical chain rules defined
- Horizontal (sibling) rules unclear
- Stage-specific navigation not covered

---

## Missing Context Infrastructure

1. **No context priority system** - which context overrides which?
2. **No context caching** - agents reload same context repeatedly
3. **No scope boundaries** - what context applies where?
4. **No context compression** - full context too large for some agents

---

## Recommendations

1. **Consolidate context rules** - single authoritative location
2. **Define agnostic/specific pattern** - clear documentation
3. **Create CLAUDE.md hierarchy** - defined reading order
4. **Add context priority rules** - override mechanism
5. **Create context loading optimization** - cache, compress

---

## Related

- `ai_documentation_system` - documentation as context
- `better_layer_stage_system` - framework structure
- `ai_manager_hierarchy_system` - manager/worker context needs
