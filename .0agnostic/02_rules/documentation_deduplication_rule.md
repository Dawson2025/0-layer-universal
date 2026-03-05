---
resource_id: "a6000fb0-7a5e-45a1-b072-3eeb29f56504"
resource_type: "rule"
resource_name: "documentation_deduplication_rule"
---
# Documentation Deduplication Rule

**Status:** MANDATORY | **Scope:** All AI agents | **Level:** Critical

---

<!-- section_id: "5de0cd55-3173-4b56-be6b-a1ca2fe1e0f7" -->
## Rule: Single-Source-of-Truth for Documentation

When creating, updating, or encountering documentation, AI agents MUST follow the deduplication pattern to prevent duplicate content across the codebase.

<!-- section_id: "04d97644-5dd1-4349-a6ef-c6832a34ae0b" -->
### The Rule

**MUST:**
1. Check if documentation already exists at root `.0agnostic/` before creating new documents
2. If it exists → reference it (don't copy)
3. If it doesn't exist → create at root `.0agnostic/` if universal, locally if entity-specific
4. When finding duplicates → replace with pointer files linking to canonical
5. When editing → always edit the canonical version at root `.0agnostic/`

**MUST NOT:**
1. Create duplicate documentation in multiple locations
2. Edit pointer files (they auto-reference canonical)
3. Copy documentation instead of pointing to it
4. Maintain separate versions of the same documentation

---

<!-- section_id: "1311e52d-926f-4cfb-8cec-ab89db95da34" -->
## Quick Reference

<!-- section_id: "92d399c1-69b9-4a3a-9ce7-9789852df7b3" -->
### Canonical Locations (Edit Here)

All authoritative documentation lives in:
```
.0agnostic/01_knowledge/         ← Universal knowledge
.0agnostic/02_rules/              ← Universal rules
.0agnostic/03_protocols/          ← Universal protocols
```

<!-- section_id: "75c94766-ed88-4277-9bd6-3aeb9c83eaff" -->
### Pointer Format (Use When Duplicates Found)

Replace duplicate content with pointer:
```markdown
# [Title]

This file has been replaced with a pointer to the canonical source.

**[READ CANONICAL [FILENAME].md]([relative_path_to_canonical])**

---

[1-2 sentences explaining what this covers]

This pointer file directs you to the current production definition.
```

<!-- section_id: "dbd1e701-9e74-41a6-8391-39c41a0378ac" -->
### Decision Tree

```
Need to create/update documentation?
  ↓
Does it already exist at root .0agnostic/?
  ├─ YES → Use/reference it (don't copy)
  └─ NO → Is it universal?
         ├─ YES → Create at root .0agnostic/
         └─ NO → Is it entity-specific?
                ├─ YES → Create locally at entity
                └─ NO → Unclear? Create at root
```

<!-- section_id: "cf03da2e-0b3c-41e6-b34e-c6dbcdfc08eb" -->
### When You Find a Duplicate

1. Identify canonical (usually at root)
2. Replace duplicate with pointer file
3. Calculate relative path
4. Test the link
5. Commit: `[AI Context] Replace duplicate [filename] with canonical pointer`

---

<!-- section_id: "966d8454-66cd-4844-a81e-9c06fe74c59d" -->
## Why This Matters

| Problem | Solution | Result |
|---------|----------|--------|
| Same doc in 10 locations | 1 canonical + 9 pointers | Update once = everywhere |
| Manual sync required | Automatic referencing | No drift risk |
| Inconsistency risk | Single source of truth | Guaranteed consistency |
| High maintenance burden | Pointer maintenance (zero work) | 93% burden reduction |

---

<!-- section_id: "fcdc657d-a833-4744-aae0-3568b300a9dc" -->
## Related Resources

- **Full Pattern Guide:** `.0agnostic/01_knowledge/deduplication_pattern.md`
- **Team Onboarding:** `.0agnostic/01_knowledge/deduplication_onboarding.md`
- **Project Summary:** `.0agnostic/01_knowledge/deduplication_project_summary.md`
- **Current Canonicals:** See deduplication_pattern.md section "Current Canonical Documents"

---

<!-- section_id: "e4d1a589-9218-4e95-9162-e87e3b7ff7fd" -->
## Enforcement

This rule is:
- ✅ MANDATORY for all documentation work
- ✅ CHECKED in code review (look for new duplicates)
- ✅ AUTOMATED where possible (pointer validation in CI/CD future enhancement)
- ✅ DOCUMENTED in agent context loading (triggers below)

---

<!-- section_id: "2f3eb896-b405-4952-a42c-df5db7e6c9cd" -->
## For AI Agents: Context Loading

**Load this rule when:**
- Creating new documentation files
- Updating existing documentation
- Finding duplicate content
- Establishing entity-specific knowledge
- Reviewing documentation structure

**Trigger keywords:** deduplication, duplicate, pointer, canonical, single source, documentation pattern

---

*Last Updated: 2026-02-28*
*Applies To: All AI agents, all phases of development*
