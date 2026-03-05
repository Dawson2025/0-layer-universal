---
resource_id: "daa53f69-023e-4882-961a-00a068764d3e"
resource_type: "knowledge"
resource_name: "AI_CONTEXT_COMMIT_PUSH_RULE"
---
# AI Context Commit and Push Rule

<!-- section_id: "96a42c60-afe3-46b1-a8b7-e24af143dfc6" -->
## Rule

After any approved changes are made to the AI context system, the AI MUST:

1. **Stage the changed files** with `git add`
2. **Commit** with a descriptive message
3. **Push** to the remote repository

<!-- section_id: "214bd992-6beb-451a-9812-cdc61cab84c1" -->
## Scope

This rule applies to all modifications within:

| Path Pattern | Description |
|--------------|-------------|
| `0_layer_universal/` | Entire AI context system |
| `layer_*/` | All layer directories |
| `sub_layer_*/` | All sublayer directories |
| `stage_*/` | All stage directories |
| `CLAUDE.md` | Claude context files |
| `status.json` | Status tracking files |

<!-- section_id: "0ccce084-6efe-44b5-a6ef-60ef58829056" -->
## Commit Message Format

```
[AI Context] <brief description>

- File 1: <change type>
- File 2: <change type>
...

Co-Authored-By: Claude <noreply@anthropic.com>
```

<!-- section_id: "b5dcd07d-7ece-4f29-a59f-1da76edac8e9" -->
## Rationale

- **Preservation**: Changes are saved and not lost
- **Sync**: Enables synchronization across devices (Windows/Linux dual boot)
- **History**: Creates version history of AI context evolution
- **Collaboration**: Changes are visible to user on all devices

<!-- section_id: "0977955a-1354-4444-9cb7-0edc776edf45" -->
## Workflow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   User      │     │   AI Shows  │     │   User      │     │  AI Commits │
│   Request   │ ──▶ │   Diagram   │ ──▶ │   Approves  │ ──▶ │  and Pushes │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

<!-- section_id: "ccfd182e-4749-42d8-b12b-b23f0210d034" -->
## Date Added
2026-01-26

<!-- section_id: "1c51e817-5066-468b-b6bb-bf2cdecfa081" -->
## Related Rules
- AI_CONTEXT_MODIFICATION_PROTOCOL.md - Show diagram before modifying
