---
resource_id: "c0f0f907-2843-460d-8f1f-95095114d75c"
resource_type: "knowledge"
resource_name: "01_rules_problems"
---
# Rules System Problems

**Date**: 2026-01-25
**Source**: AI System Audit

---

<!-- section_id: "cab582ef-8346-4cc4-9859-e0a7c5cbbe43" -->
## Problem Summary

The rules and protocols system lacks organization, has conflicting versions, and no priority mechanism for conflict resolution.

---

<!-- section_id: "7e1e5f80-bccd-4c9e-ad61-85ba7b7eb21d" -->
## Major Problems

<!-- section_id: "304badce-1c18-4e9d-86ca-0c1e8fb32230" -->
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

<!-- section_id: "d5fa1cac-6f51-406a-91b9-184f5567abd2" -->
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

<!-- section_id: "6fb1e5cb-0589-41c5-8d3f-f2a2da4ca62c" -->
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

<!-- section_id: "1d5074d2-eca6-4f93-bca1-1644a8527b40" -->
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

<!-- section_id: "f6d3444c-28fa-434d-8210-f796f063ed8e" -->
### 5. Rule Scope Unclear
**Severity**: MINOR

Rules exist with unclear scope:
- Some are universal
- Some are OS-specific (`CROSS_OS_COMPATIBILITY_RULES.md`)
- Some are tool-specific
- No labeling system

---

<!-- section_id: "cc064029-3ae4-427e-ade1-054afb62104a" -->
## Missing Rules Infrastructure

1. **No rule registry** - can't enumerate all rules
2. **No rule inheritance** - child layers can't override parent rules
3. **No rule validation** - conflicting rules not detected
4. **No rule search** - hard to find applicable rules

---

<!-- section_id: "584bb93c-dc99-4fa1-a71f-988d5da33ee1" -->
## Recommendations

1. **Create rule categories** - organize by type/scope
2. **Add priority levels** - explicit precedence
3. **Version all rules** - v1.0, v1.1, etc.
4. **Create deprecation markers** - "superseded by X"
5. **Build rule registry** - enumerate and search

---

<!-- section_id: "01d6dc12-f151-40e1-af77-3a17d76fdb5d" -->
## Related

- `ai_context_system` - rules as context
- `ai_automation_system` - rule validation
- `ai_documentation_system` - rule documentation
