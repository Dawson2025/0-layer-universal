# Need: Reference Format Standard — User Stories

---

### US-1: Agent follows reference to source
**As an** agent reading a knowledge file that claims "vectors can't capture typed relationships",
**I want** a standardized reference pointing to the exact source file and section,
**So that** I can load the full explanation in one targeted read.

**Acceptance**: Reference is parseable, path is valid, section exists.

---

### US-2: Script validates all references
**As a** validation script,
**I want** to parse all references in all knowledge files,
**So that** I can report broken links (moved files, renamed sections).

**Acceptance**: Script finds and validates every reference. Reports broken ones.

---

### US-3: Developer creates new knowledge file
**As the** developer writing a new knowledge file,
**I want** a clear reference format to follow,
**So that** my references are consistent with all other knowledge files.

**Acceptance**: Format is documented with copy-pasteable examples.
