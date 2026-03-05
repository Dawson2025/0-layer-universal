---
resource_id: "1d881dce-1613-435d-a43e-0bbee8f3bb5c"
resource_type: "rule"
resource_name: "deduplication_quick_reference"
---
# Deduplication Pattern: Quick Reference for AI Agents

**MANDATORY RULE:** Apply this pattern to ALL documentation work.

---

<!-- section_id: "34c14ed2-29f4-4db9-99b8-1518b8c387ca" -->
## TL;DR (30 seconds)

1. **Check first**: Does documentation already exist at `.0agnostic/`?
2. **If YES**: Use it (don't copy)
3. **If NO**: Create at root if universal, locally if entity-specific
4. **If duplicate found**: Replace with pointer file
5. **Always edit**: The canonical version at root (never edit pointers)

---

<!-- section_id: "1b989ea6-ed67-4ccb-aaf3-41ad9ff07c21" -->
## The Pattern

```
Canonical (root)
    ↓
    ├── Authoritative, full content
    ├── Edit here only
    └── Live at .0agnostic/

Pointer (research)
    ↓
    ├── Redirect to canonical
    ├── Never edit
    └── 7-10 lines only
```

---

<!-- section_id: "ada3fbfa-8b7f-423e-af1e-ab136203ee5a" -->
## Decision Tree

```
Creating documentation?
  ├─ Exists at .0agnostic/? → USE IT (don't copy)
  └─ Doesn't exist?
     ├─ Universal? → Create at .0agnostic/
     └─ Entity-specific? → Create locally
```

---

<!-- section_id: "591b6573-b296-4218-9f3f-2b11234b38ae" -->
## Pointer Template (Copy & Paste)

```markdown
# [Title]

This file has been replaced with a pointer to the canonical source.

**[READ CANONICAL [FILENAME].md]([RELATIVE_PATH_TO_CANONICAL])**

---

[1-2 sentences about this documentation]

This pointer file directs you to the current production definition.
```

---

<!-- section_id: "c507d50a-c1a1-409d-b10d-2a43d2715b63" -->
## Red Flags 🚩

| Red Flag | What to Do |
|----------|-----------|
| Same file in root AND research | Convert research to pointer |
| File says "Inherits from X" | Update to use new pointer format |
| Multiple versions of same doc | Consolidate to canonical + pointers |
| Editing a file in research | Check if canonical exists; edit that instead |

---

<!-- section_id: "0b48cbe9-4b34-4cfa-bf5f-7404cf81ec03" -->
## Canonical Locations

```
.0agnostic/01_knowledge/    ← Universal knowledge (INSTANTIATION_GUIDE.md, LAYERS_EXPLAINED.md, etc.)
.0agnostic/02_rules/        ← Universal rules (this one!)
.0agnostic/03_protocols/    ← Universal protocols (stage_report_protocol.md, etc.)
```

---

<!-- section_id: "e6ca3fae-2454-43f9-b7d0-8a9cddb3a40f" -->
## Key Rules

✅ **DO:**
- Check `.0agnostic/` first
- Edit canonical (root) only
- Create pointers for duplicates
- Keep pointers under 15 lines

❌ **DON'T:**
- Copy documentation
- Edit pointer files
- Create duplicates
- Edit research versions

---

<!-- section_id: "9339c56e-660a-444c-acbf-7dde7adcefac" -->
## Commit Message

```
[AI Context] Replace duplicate [filename] with canonical pointer
```

---

<!-- section_id: "9503bd45-7ae8-419d-8e0b-8570b78682a3" -->
## When in Doubt

Load full resources:
- `.0agnostic/02_rules/documentation_deduplication_rule.md` (Complete rule)
- `.0agnostic/01_knowledge/deduplication_pattern.md` (Full guide)
- `.0agnostic/01_knowledge/deduplication_onboarding.md` (Team guide)

---

**Status:** MANDATORY | **Last Updated:** 2026-02-28 | **Applies To:** All AI agents, all documentation
