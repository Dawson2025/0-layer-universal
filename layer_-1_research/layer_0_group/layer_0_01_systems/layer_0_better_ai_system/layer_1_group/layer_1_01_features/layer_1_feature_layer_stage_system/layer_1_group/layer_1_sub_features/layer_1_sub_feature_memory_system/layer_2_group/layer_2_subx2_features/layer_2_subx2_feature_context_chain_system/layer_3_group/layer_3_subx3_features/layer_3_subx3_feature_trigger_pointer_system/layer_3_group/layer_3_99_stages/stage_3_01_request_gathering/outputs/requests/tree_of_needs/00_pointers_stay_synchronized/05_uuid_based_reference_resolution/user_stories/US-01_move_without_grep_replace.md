---
resource_id: "0b1c2d3e-4f5a-4b6c-7d8e-9f0a1b2c3d4e"
resource_type: "output"
resource_name: "US-01_move_without_grep_replace"
---
# US-01: Move Without Grep-and-Replace

**Need**: [UUID-Based Reference Resolution](../README.md)

---

**As a** developer who needs to reorganize the directory structure (move scripts, rename entities, restructure layers),
**I want** to simply move the files and rebuild the UUID index,
**So that** all references across the entire codebase automatically resolve to the new locations without me having to grep-and-replace across 80+ files.

<!-- section_id: "1c2d3e4f-5a6b-4c7d-8e9f-0a1b2c3d4e5f" -->
### What Happens

1. Developer moves a file, directory, or entity to a new location (via `mv`, `git mv`, IDE refactor, or file manager)
2. Developer runs `pointer-sync.sh --rebuild-index` (~3 seconds) — scans filesystem, updates UUID → path mapping in `.uuid-index.json`
3. All UUID-based references in scripts, docs, and context files now resolve to the new path
4. Developer commits. Done.

**What does NOT happen:**
- No `grep -rl "old/path" | xargs sed` across the codebase
- No manual editing of 0AGNOSTIC.md resource tables
- No manual editing of knowledge docs, rules, protocols, skills
- No manual editing of stage outputs
- No manual fixing of script-to-script calls
- No manual updating of git hooks
- No risk of missed references or silent breakage

<!-- section_id: "2d3e4f5a-6b7c-4d8e-9f0a-1b2c3d4e5f6a" -->
### Acceptance Criteria

- Moving 12 scripts (like the script protocol migration) requires zero documentation updates — only `mv` + `rebuild-index`
- `pointer-sync.sh --validate` exits 0 after move + rebuild
- All scripts execute correctly from their new locations via UUID resolution
- All AI app context files produce correct paths when resolved
- No manual file edits required beyond the physical move itself
