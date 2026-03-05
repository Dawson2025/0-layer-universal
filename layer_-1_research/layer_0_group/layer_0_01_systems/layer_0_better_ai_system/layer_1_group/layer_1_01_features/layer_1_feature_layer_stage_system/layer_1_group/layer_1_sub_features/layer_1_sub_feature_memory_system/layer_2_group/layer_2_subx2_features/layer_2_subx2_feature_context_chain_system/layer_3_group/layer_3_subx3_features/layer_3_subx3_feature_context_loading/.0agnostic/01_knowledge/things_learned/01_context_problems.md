---
resource_id: "c3bd69c2-fc7a-44b0-bbcf-fbf4aef99577"
resource_type: "knowledge"
resource_name: "01_context_problems"
---
# Context System Problems

**Date**: 2026-01-25
**Source**: AI System Audit

---

<!-- section_id: "96ba47c6-5921-4258-b883-05ab480a21de" -->
## Problem Summary

Context gathering and management for AI agents is fragmented, with rules scattered across multiple locations and unclear priority/scope definitions.

---

<!-- section_id: "5259f4ad-cdc8-4bf5-85d5-763a4f30f4bd" -->
## Major Problems

<!-- section_id: "21eb06fc-fc45-4bef-a880-e56ee2f3eb8b" -->
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

<!-- section_id: "8cea5a29-7283-439e-9dce-14c127e3139e" -->
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

<!-- section_id: "64fbf43b-ef70-48a6-b559-ef6fc0fc83bc" -->
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

<!-- section_id: "6fac2079-5d70-4074-bdd0-c9815bfc83de" -->
### 4. Context Gathering Skill Issues
**Severity**: MINOR

**Location**: `.claude/skills/context-gathering`

**Problems**:
- References old `0_context` structure
- No bridge documentation to new system
- May not work with current structure

---

<!-- section_id: "277c5c36-9672-4cee-aff9-ea818c668e3c" -->
### 5. Layer Navigation Incomplete
**Severity**: MINOR

**File**: `layer_0_01_ai_manager_system/agnostic/layer_navigation.md`

**Problems**:
- Vertical chain rules defined
- Horizontal (sibling) rules unclear
- Stage-specific navigation not covered

---

<!-- section_id: "e50c3d02-8cd7-40d6-89e4-aae3801d7399" -->
## Missing Context Infrastructure

1. **No context priority system** - which context overrides which?
2. **No context caching** - agents reload same context repeatedly
3. **No scope boundaries** - what context applies where?
4. **No context compression** - full context too large for some agents

---

<!-- section_id: "22313573-8138-48b7-896f-790fa5a6046a" -->
## Recommendations

1. **Consolidate context rules** - single authoritative location
2. **Define agnostic/specific pattern** - clear documentation
3. **Create CLAUDE.md hierarchy** - defined reading order
4. **Add context priority rules** - override mechanism
5. **Create context loading optimization** - cache, compress

---

<!-- section_id: "ffe86045-b9c8-41e8-8232-8e01b9332bef" -->
## Related

- `ai_documentation_system` - documentation as context
- `better_layer_stage_system` - framework structure
- `ai_manager_hierarchy_system` - manager/worker context needs
