---
resource_id: "ee838447-f113-4ba4-abed-5a7e04449f36"
resource_type: "rule"
resource_name: "FILE_PATH_LINKING_RULE"
---
# [CRITICAL] File Path Linking Rule

## Rule (MANDATORY)

When creating or updating files, ALWAYS include the full clickable file path in the response so the user can easily navigate to it in the IDE.

## Format

After any file creation or modification, include:

**Single file**:
```
**File**: `/full/path/to/file.md`
```

**Multiple files**:
```
**Files created/updated**:
- `/full/path/to/file1.md`
- `/full/path/to/file2.md`
```

## Applies To

- All file Write operations
- All file Edit operations
- Any operation that creates or modifies files
- ALL layers, ALL stages, ALL entities

## Rationale

Users working in IDEs can click on full file paths to navigate directly to the file. This improves workflow efficiency and reduces friction.

## Propagation

This rule MUST be included in:
- All 0AGNOSTIC.md files (in Behaviors section)
- All generated CLAUDE.md files
- All tool-specific context files (AGENTS.md, GEMINI.md, etc.)

---

*Critical Universal Rule - Layer 0*
