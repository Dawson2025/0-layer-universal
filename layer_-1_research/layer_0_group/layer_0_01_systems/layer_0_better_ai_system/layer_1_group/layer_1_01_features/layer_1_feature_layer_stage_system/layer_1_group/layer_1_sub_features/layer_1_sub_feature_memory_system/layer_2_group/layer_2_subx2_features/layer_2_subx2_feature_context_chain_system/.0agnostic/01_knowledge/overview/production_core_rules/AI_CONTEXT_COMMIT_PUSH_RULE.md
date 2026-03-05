---
resource_id: "daa53f69-023e-4882-961a-00a068764d3e"
resource_type: "knowledge"
resource_name: "AI_CONTEXT_COMMIT_PUSH_RULE"
---
# AI Context Commit and Push Rule

## Rule

After any approved changes are made to the AI context system, the AI MUST:

1. **Stage the changed files** with `git add`
2. **Commit** with a descriptive message
3. **Push** to the remote repository

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

## Commit Message Format

```
[AI Context] <brief description>

- File 1: <change type>
- File 2: <change type>
...

Co-Authored-By: Claude <noreply@anthropic.com>
```

## Rationale

- **Preservation**: Changes are saved and not lost
- **Sync**: Enables synchronization across devices (Windows/Linux dual boot)
- **History**: Creates version history of AI context evolution
- **Collaboration**: Changes are visible to user on all devices

## Workflow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   User      │     │   AI Shows  │     │   User      │     │  AI Commits │
│   Request   │ ──▶ │   Diagram   │ ──▶ │   Approves  │ ──▶ │  and Pushes │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

## Date Added
2026-01-26

## Related Rules
- AI_CONTEXT_MODIFICATION_PROTOCOL.md - Show diagram before modifying
