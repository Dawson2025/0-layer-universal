# Documentation System Problems

**Date**: 2026-01-25
**Source**: AI System Audit

---

## Problem Summary

Documentation across the AI system has drifted from implementation, contains broken path references, and lacks validation mechanisms.

---

## Critical Problems

### 1. Broken Path References
**Severity**: CRITICAL

| File | Broken Reference | Status |
|------|------------------|--------|
| `layer_0_01_ai_manager_system/README.md` | `sub_layer_0_13_universal_protocols/` | Path doesn't exist |
| `sub_layer_0_04_rules/safety_governance.md` | `../sub_layer_0_13_universal_protocols/observability/` | Path doesn't exist |
| `handoff_schema.md` | `/code/0_layer_universal/0_context/` | Folder doesn't exist |

**Root Cause**: Structure changed but documentation not updated.

---

### 2. Init Prompt Chain Confusion
**Severity**: MAJOR

**Documentation Claims**:
```
layer_0_group/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/0_basic_prompts_throughout/universal_init_prompt.md
```

**Actual Location**:
```
layer_0_group/layer_0_03_sub_layers/sub_layer_0_01_prompts/universal_init_prompt.md
```

**Impact**: Agents following documentation cannot find the init prompt.

---

### 3. Documentation Describes Wrong Structure
**Severity**: MAJOR

**SYSTEM_OVERVIEW.md describes**:
- Slots at layer level: `layer_N/slots/`
- Numbered slot pattern: `0.01`, `0.02`, etc.

**Implementation has**:
- Sub-layers only: `layer_N/layer_N_03_sub_layers/sub_layer_N_XX/`
- Different numbering: `layer_0_03_sub_layers`

---

## Major Problems

### 4. Dots vs Underscores in Paths
**Severity**: MAJOR

| Context | Uses |
|---------|------|
| Documentation | `stage_0_00_`, `layer_0_02_` |
| Actual directories | `stage_0_01_`, `layer_0_03_` |

**Files Affected**: SYSTEM_OVERVIEW.md, multiple READMEs

---

### 5. Old Trickle-Down References
**Severity**: MAJOR

Some documentation still references:
```
0_context/trickle_down_*/
```

System has moved to:
```
layer_N/layer_N_XX_*/
```

---

### 6. Multiple Entry Points
**Severity**: MINOR

Multiple CLAUDE.md files with different scopes:
- `/CLAUDE.md` (root)
- `layer_0_group/CLAUDE.md` (if exists)
- `layer_1/.../CLAUDE.md` (features)

No clear guidance on which is primary or reading order.

---

## Missing Documentation Infrastructure

1. **No link validation** - broken links not detected
2. **No path checking** - path changes don't trigger doc updates
3. **No README standards** - README content varies widely
4. **No documentation index** - hard to find relevant docs

---

## Recommendations

1. **Create path validation script** - check all path references
2. **Standardize naming convention** - pick dots OR underscores
3. **Create documentation update triggers** - when structure changes
4. **Define CLAUDE.md hierarchy** - clear reading order
5. **Create documentation templates** - consistent README format

---

## Related

- `ai_automation_system` - validation tooling
- `better_layer_stage_system` - naming conventions
