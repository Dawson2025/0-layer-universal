---
resource_id: "c1f686c1-1201-4a85-8eb6-463a91d7de4f"
resource_type: "rule"
resource_name: "I0_FILE_CHANGE_REPORTING"
---
---
promote: hot
hot_summary: "On every turn with file changes: (1) describe changes INLINE with full absolute paths using path:line format (e.g., /home/dawson/.../file.md:42) for ctrl-click navigation, (2) provide end-of-turn summary of all Added/Updated/Moved/Removed files. All paths start from /home/, NEVER abbreviated. Use path:line for ANY file reference pointing to a specific location. Full rule: .0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING/I0_FILE_CHANGE_REPORTING.md"
hot_trigger: "Any turn that modifies files"
---

# File Change Reporting Rule

**Type**: Static (every API turn)
**Importance**: 0 (highest — applies unconditionally on every turn)
**Scope**: All agents at all levels, all AI tools

<!-- section_id: "1e441487-602f-405d-a12c-bef6572a85eb" -->
## Rule

On **every turn** where the agent modifies the filesystem, it MUST do two things:

1. **Inline references**: When describing a change in the response body, include the full absolute path **right there** with the description of what was changed and why. The reader should never have to cross-reference a separate list to know where a described change happened.

2. **End-of-turn summary**: At the end of the response, provide a consolidated list of ALL file operations. This serves as the audit trail and quick-reference.

Both parts use full absolute paths starting from `/home/`.

<!-- section_id: "51940abd-26be-4109-8096-a04fb52b02f8" -->
## Part 1: Inline References (in response body)

When you describe what you changed, include the path inline so the change and its location are never separated:

```markdown
I updated the stage report protocol at `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/03_protocols/stage_report_protocol.md:15` to add the new canonical handoff location. The testing guide at `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_07_TESTING.md:42` was also updated with the new by_suite structure.
```

**NOT this** (description disconnected from location):

```markdown
I updated the stage report protocol to add the new canonical handoff location. I also updated the testing guide with the new by_suite structure.

**Files changed:**
- Updated: /home/.../stage_report_protocol.md
- Updated: /home/.../STAGE_07_TESTING.md
```

The first version tells you **what changed** and **where** together. The second forces you to mentally reconnect descriptions to paths.

<!-- section_id: "f9c43c21-f3f1-4dfd-abb5-a200e040dcf5" -->
## Part 2: End-of-Turn Summary (after main content)

```markdown
**Files changed this turn:**
- **Added**: `/home/dawson/dawson-workspace/code/0_layer_universal/.../new_file.md`
- **Updated**: `/home/dawson/dawson-workspace/code/0_layer_universal/.../modified_file.md:37`
- **Moved**: `/home/dawson/.../old_name.md` → `/home/dawson/.../new_name.md`
- **Removed**: `/home/dawson/dawson-workspace/code/0_layer_universal/.../deleted_file.md`
```

<!-- section_id: "23f9e19d-ba28-45ba-8249-23cbadc62b4d" -->
### Priority Order

Report files in this order of emphasis (most important first):

1. **Added** — new files created (Write tool)
2. **Updated** — existing files modified (Edit tool)
3. **Moved** — files relocated (git mv, mv)
4. **Removed** — files deleted (rm, git rm)

<!-- section_id: "8c297ded-68c8-49c3-8442-0cf5b9c57ff3" -->
## Rules

1. **Both parts are mandatory** — inline references in the body AND the end-of-turn summary. They are complementary, not alternatives.
2. All paths MUST be **full absolute paths starting from `/home/`** — no relative paths, no basename-only references, no abbreviated tails like `stage_1_04_design/outputs/file.md`.
3. **NEVER abbreviate paths** by showing only the last few segments. Always start from the filesystem root. Deep paths in the layer-stage hierarchy can be long — that is expected and required.
4. The end-of-turn summary MUST appear at the end of the response (after the main content).
5. If no files were changed on this turn, neither part is needed.
6. When many files are changed (10+), group by operation type and show counts with representative examples — but each example MUST still use full absolute paths.
7. For agent-delegated work, the delegating agent reports the summary when the sub-agent returns.
8. When referencing a specific location in a file (a function, section, config block), ALWAYS use `path:line` format (e.g., `/home/dawson/.../file.md:42`). This applies to both file change reports AND general file references in conversation.
9. The `:line` suffix is for **runtime output** only (what agents show users). For stored references in pointer files, use `section_id` which is more durable across edits.

<!-- section_id: "7a3b4c5d-e6f7-4890-ab12-cd34ef56a789" -->
## Clickable File References (path:line format)

All file references — whether reporting changes or pointing to code for the user — MUST use the `path:line` format when referencing a specific location:

**Format**: `path/to/file.ext:LINE` or `path/to/file.ext:LINE:COLUMN`

This makes every reference ctrl-clickable in IDE terminals (VS Code, Cursor, JetBrains). This is the de facto universal standard used by gcc, grep, ESLint, TypeScript, and all major CLI tools.

<!-- section_id: "8b4c5d6e-f7a8-4901-bc23-de45fa67b890" -->
### When to Use :line

| Situation | Format | Example |
|-----------|--------|---------|
| Edited a specific section | `path:line` | `/home/dawson/.../rule.md:42` |
| Pointing user to code to review | `path:line` | `/home/dawson/.../design.md:150` |
| End-of-turn summary (updated files) | `path:line` (line of primary change) | `**Updated**: /home/.../file.md:37` |
| New file created | `path` (no line needed) | `**Added**: /home/.../new_file.md` |
| Deleted file | `path` (no line needed) | `**Removed**: /home/.../old_file.md` |
| Referencing a config line | `path:line` | `/home/dawson/.codex/config.toml:16` |

<!-- section_id: "9c5d6e7f-a8b9-4012-cd34-ef56ab78c901" -->
### Why This Matters

- **Ctrl-click navigation**: VS Code, Cursor, and JetBrains terminals auto-detect `path:line` and make it clickable
- **Zero overhead**: Adding `:42` to a path costs nothing but saves the user from manually finding the line
- **Industry standard**: Every compiler, linter, and test runner uses this format — LLMs are pretrained on it

<!-- section_id: "0f1c8203-b31d-45b0-b071-7edd7bd81bbd" -->
### Bad Examples (DO NOT do this)

**Disconnected description and path:**
```markdown
I updated the stage report protocol with the new location.

**Files changed:**
- **Updated**: `/home/dawson/.../stage_report_protocol.md`
```

**Abbreviated paths:**
```markdown
- **Updated**: `stages_manager_pattern.md`
- **Updated**: `.../stage_1_04_design/outputs/design_decisions/stages_manager_pattern.md`
```

<!-- section_id: "86aebf3b-f871-49e2-b98b-4835099b6171" -->
### Good Example

**Inline + summary working together (with :line for ctrl-click navigation):**
```markdown
I updated the stage report protocol at `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/03_protocols/stage_report_protocol.md:15` to add the new canonical handoff location (both to_above and to_below).

**Files changed this turn:**
- **Updated**: `/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/03_protocols/stage_report_protocol.md:15`
```

<!-- section_id: "dae8a603-7125-43de-90b4-cf77b2ea3ce8" -->
## Rationale

The user needs to understand what was modified, where, and why — all together. Separating "what changed" from "where it changed" forces mental cross-referencing. The inline reference connects change descriptions to their locations. The end-of-turn summary provides the consolidated audit trail. Together, they give full traceability without forcing the reader to jump between sections.

<!-- section_id: "a2ac1ae9-4ef7-4e54-a57c-cf6baa71b4ec" -->
## Related

- **Supersedes**: The `FILE_PATH_LINKING_RULE.md` inline convention — both inline and summary are now mandatory
