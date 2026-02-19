# Rules System Problems

**Date**: 2026-01-25
**Source**: AI System Audit

---

## Problem Summary

The rules and protocols system lacks organization, has conflicting versions, and no priority mechanism for conflict resolution.

---

## Major Problems

### 1. Conflicting Terminal Protocols
**Severity**: MAJOR

Multiple terminal execution protocols exist with no clear priority:

| File | Location |
|------|----------|
| `terminal_execution_protocol.md` | sub_layer_0_04_rules/ |
| `UNIVERSAL_TERMINAL_EXECUTION.md` | sub_layer_0_04_rules/ |
| `MASTER_TERMINAL_EXECUTION_REFERENCE.md` | sub_layer_0_04_rules/0_instruction_docs/ |
| `terminal-quick-reference.md` | sub_layer_0_04_rules/0_instruction_docs/ |

**Impact**: Agents don't know which protocol to follow.

---

### 2. No Rule Priority System
**Severity**: MAJOR (escalating)

**Current State**:
- `sub_layer_0_04_rules/` contains many rules
- No meta-rule defining priority
- No conflict resolution guidance
- No versioning system

**Missing**:
- Rule precedence definition
- Scope labeling (universal, OS, tool)
- Version numbers
- Deprecation markers

---

### 3. Archive Docs Not Clearly Archived
**Severity**: MINOR

**Location**: `sub_layer_0_04_rules/3_archive_docs/`

**Problems**:
- Contains old resolutions (YYYYMMDD format)
- Some may still be relevant
- No indication of what supersedes them
- No clear "superseded by" links

**Files**:
- `20251023_CompleteDocumentationOrganization_Resolution_v1.0.md`
- `20251023_SubdirectoryNumbering_Resolution_v1.0.md`
- `CURSOR_AGENT_TERMINAL_HANGING_SOLUTION.md`
- etc.

---

### 4. Mixed Instruction Types in Same Folder
**Severity**: MINOR

**Location**: `sub_layer_0_04_rules/0_instruction_docs/`

**Contains**:
- Agent guides (`AGENT_DISCOVERY_GUIDE.md`)
- Terminal protocols
- Quick references
- Tool-specific instructions (`supabase_javascript_quick_reference.md`, `canvas_submission_protocol.md`)

**Problem**: No clear organization principle.

---

### 5. Rule Scope Unclear
**Severity**: MINOR

Rules exist with unclear scope:
- Some are universal
- Some are OS-specific (`CROSS_OS_COMPATIBILITY_RULES.md`)
- Some are tool-specific
- No labeling system

---

## Missing Rules Infrastructure

1. **No rule registry** - can't enumerate all rules
2. **No rule inheritance** - child layers can't override parent rules
3. **No rule validation** - conflicting rules not detected
4. **No rule search** - hard to find applicable rules

---

## Recommendations

1. **Create rule categories** - organize by type/scope
2. **Add priority levels** - explicit precedence
3. **Version all rules** - v1.0, v1.1, etc.
4. **Create deprecation markers** - "superseded by X"
5. **Build rule registry** - enumerate and search

---

## Related

- `ai_context_system` - rules as context
- `ai_automation_system` - rule validation
- `ai_documentation_system` - rule documentation
