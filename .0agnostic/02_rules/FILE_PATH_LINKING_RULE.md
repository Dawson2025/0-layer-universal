---
resource_id: "ee838447-f113-4ba4-abed-5a7e04449f36"
resource_type: "rule"
resource_name: "FILE_PATH_LINKING_RULE"
---
# [CRITICAL] File Path Linking Rule

<!-- section_id: "3eb97d73-3b42-44d6-8538-55416d6748f6" -->
## Rule (MANDATORY)

When creating or updating files, ALWAYS include the full clickable file path in the response so the user can easily navigate to it in the IDE.

<!-- section_id: "0b51e003-46b4-40a8-99ed-a3ea1ed5dd11" -->
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

<!-- section_id: "abc16d24-495e-413c-8502-408fd4f04e11" -->
## Applies To

- All file Write operations
- All file Edit operations
- Any operation that creates or modifies files
- ALL layers, ALL stages, ALL entities

<!-- section_id: "f88c7894-af42-48b1-b5cb-e7a850f7dd93" -->
## Rationale

Users working in IDEs can click on full file paths to navigate directly to the file. This improves workflow efficiency and reduces friction.

<!-- section_id: "ac971d30-3142-44f7-bbc3-6e06d3775c55" -->
## Propagation

This rule MUST be included in:
- All 0AGNOSTIC.md files (in Behaviors section)
- All generated CLAUDE.md files
- All tool-specific context files (AGENTS.md, GEMINI.md, etc.)

---

*Critical Universal Rule - Layer 0*
