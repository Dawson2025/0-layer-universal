---
resource_id: "542ab8dd-15ee-46d1-8ad2-2c62ae0a3cc7"
resource_type: "knowledge"
resource_name: "FILE_PATH_LINKING_RULE"
---
# [CRITICAL] File Path Linking Rule

<!-- section_id: "64452de3-002f-4804-b99c-1b20b028631c" -->
## Rule (MANDATORY)

When creating or updating files, ALWAYS include the full clickable file path in the response so the user can easily navigate to it in the IDE.

<!-- section_id: "f0c319aa-5016-4a23-bbb1-8884c269090f" -->
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

<!-- section_id: "31759763-4a41-4b30-a8cc-edf4cc289314" -->
## Applies To

- All file Write operations
- All file Edit operations
- Any operation that creates or modifies files
- ALL layers, ALL stages, ALL entities

<!-- section_id: "88ff17ab-a9eb-4732-919f-72bd06bb4a7c" -->
## Rationale

Users working in IDEs can click on full file paths to navigate directly to the file. This improves workflow efficiency and reduces friction.

<!-- section_id: "6e1c84e5-d805-4b99-a75f-29ea2c798b5d" -->
## Propagation

This rule MUST be included in:
- All 0AGNOSTIC.md files (in Behaviors section)
- All generated CLAUDE.md files
- All tool-specific context files (AGENTS.md, GEMINI.md, etc.)

---

*Critical Universal Rule - Layer 0*
