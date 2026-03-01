# Deduplication Pattern: Quick Reference for AI Agents

**MANDATORY RULE:** Apply this pattern to ALL documentation work.

---

## TL;DR (30 seconds)

1. **Check first**: Does documentation already exist at `.0agnostic/`?
2. **If YES**: Use it (don't copy)
3. **If NO**: Create at root if universal, locally if entity-specific
4. **If duplicate found**: Replace with pointer file
5. **Always edit**: The canonical version at root (never edit pointers)

---

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

## Decision Tree

```
Creating documentation?
  ├─ Exists at .0agnostic/? → USE IT (don't copy)
  └─ Doesn't exist?
     ├─ Universal? → Create at .0agnostic/
     └─ Entity-specific? → Create locally
```

---

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

## Red Flags 🚩

| Red Flag | What to Do |
|----------|-----------|
| Same file in root AND research | Convert research to pointer |
| File says "Inherits from X" | Update to use new pointer format |
| Multiple versions of same doc | Consolidate to canonical + pointers |
| Editing a file in research | Check if canonical exists; edit that instead |

---

## Canonical Locations

```
.0agnostic/01_knowledge/    ← Universal knowledge (INSTANTIATION_GUIDE.md, LAYERS_EXPLAINED.md, etc.)
.0agnostic/02_rules/        ← Universal rules (this one!)
.0agnostic/03_protocols/    ← Universal protocols (stage_report_protocol.md, etc.)
```

---

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

## Commit Message

```
[AI Context] Replace duplicate [filename] with canonical pointer
```

---

## When in Doubt

Load full resources:
- `.0agnostic/02_rules/documentation_deduplication_rule.md` (Complete rule)
- `.0agnostic/01_knowledge/deduplication_pattern.md` (Full guide)
- `.0agnostic/01_knowledge/deduplication_onboarding.md` (Team guide)

---

**Status:** MANDATORY | **Last Updated:** 2026-02-28 | **Applies To:** All AI agents, all documentation
