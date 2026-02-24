---
promote: hot
hot_summary: "On every turn with file changes, report all Added/Updated/Moved/Removed files with full absolute paths at end of response. Full rule: .0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING.md"
hot_trigger: "Any turn that modifies files"
---

# File Change Reporting Rule

**Type**: Static (every API turn)
**Importance**: 0 (highest — applies unconditionally on every turn)
**Scope**: All agents at all levels, all AI tools

## Rule

On **every turn** where the agent modifies the filesystem, it MUST report a summary of all file operations at the end of its response. The report uses full absolute system paths.

## Format

```markdown
**Files changed this turn:**
- **Added**: `/full/path/to/new_file.md`
- **Updated**: `/full/path/to/modified_file.md`
- **Moved**: `/full/path/old` → `/full/path/new`
- **Removed**: `/full/path/to/deleted_file.md`
```

## Priority Order

Report files in this order of emphasis (most important first):

1. **Added** — new files created (Write tool)
2. **Updated** — existing files modified (Edit tool)
3. **Moved** — files relocated (git mv, mv)
4. **Removed** — files deleted (rm, git rm)

## Rules

1. Report MUST use full absolute paths (e.g., `/home/dawson/dawson-workspace/code/0_layer_universal/...`)
2. Report MUST appear at the end of the response (after the main content)
3. If no files were changed on this turn, no report is needed
4. When many files are changed (10+), group by operation type and show counts with representative examples
5. For agent-delegated work, the delegating agent reports the summary when the sub-agent returns
6. This rule supersedes the older File Path Linking rule — the inline `**File**: /path` convention is still encouraged for individual file operations, but this end-of-turn summary is mandatory

## Rationale

The user needs a reliable, consistent way to know what was modified on every turn. This enables:
- Quick verification of what changed
- Easy navigation to modified files
- Audit trail for the session
- Catch unintended modifications early

## Related

- **Supersedes**: The `FILE_PATH_LINKING_RULE.md` inline convention (still valid, but this summary is now required in addition)
