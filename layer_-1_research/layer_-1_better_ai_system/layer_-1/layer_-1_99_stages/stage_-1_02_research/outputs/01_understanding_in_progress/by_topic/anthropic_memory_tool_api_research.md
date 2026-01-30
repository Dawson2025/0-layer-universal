# Anthropic Memory Tool API Research

**Date**: 2026-01-30
**Stage**: stage_-1_02_research
**Topic**: The official Memory Tool API from Anthropic

---

## What Is It?

The Memory Tool is a **beta API feature** (launched Sept 29, 2025) that lets Claude store and retrieve information across conversations through a file-based system.

**Key point**: It's a **client-side tool** - YOU control where/how data is stored. Claude just makes tool calls, your app executes them.

---

## How It Works

```
User Request
    ↓
Claude checks /memories directory (automatic)
    ↓
Claude reads relevant files
    ↓
Claude uses memory to help
    ↓
Claude writes learnings back to /memories
```

Claude automatically:
1. Checks `/memories` directory before starting tasks
2. Creates, reads, updates, deletes files
3. References memories in future conversations

---

## Enabling It

**Beta header required**: `context-management-2025-06-27`

```python
response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=4096,
    messages=[...],
    tools=[
        { "type": "memory_20250818", "name": "memory" },
    ],
    betas=["context-management-2025-06-27"],
)
```

---

## Supported Models

- Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)
- Claude Sonnet 4 (`claude-sonnet-4-20250514`)
- Claude Haiku 4.5 (`claude-haiku-4-5-20251001`)
- Claude Opus 4.5 (`claude-opus-4-5-20251101`)
- Claude Opus 4.1 (`claude-opus-4-1-20250805`)
- Claude Opus 4 (`claude-opus-4-20250514`)

---

## Tool Commands

### view
Shows directory contents or file contents:
```json
{
  "command": "view",
  "path": "/memories",
  "view_range": [1, 10]  // Optional: specific lines
}
```

### create
Create a new file:
```json
{
  "command": "create",
  "path": "/memories/notes.txt",
  "file_text": "Meeting notes:\n- Discussed project timeline"
}
```

### str_replace
Replace text in a file:
```json
{
  "command": "str_replace",
  "path": "/memories/preferences.txt",
  "old_str": "Favorite color: blue",
  "new_str": "Favorite color: green"
}
```

### insert
Insert text at specific line:
```json
{
  "command": "insert",
  "path": "/memories/todo.txt",
  "insert_line": 2,
  "insert_text": "- Review memory tool documentation\n"
}
```

### delete
Delete file or directory:
```json
{
  "command": "delete",
  "path": "/memories/old_file.txt"
}
```

### rename
Rename or move:
```json
{
  "command": "rename",
  "old_path": "/memories/draft.txt",
  "new_path": "/memories/final.txt"
}
```

---

## Auto-Injected System Prompt

When memory tool is enabled, this is automatically added:

```
IMPORTANT: ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE.
MEMORY PROTOCOL:
1. Use the `view` command of your `memory` tool to check for earlier progress.
2. ... (work on the task) ...
   - As you make progress, record status / progress / thoughts etc in your memory.
ASSUME INTERRUPTION: Your context window might be reset at any moment,
so you risk losing any progress that is not recorded in your memory directory.
```

---

## Using with Context Editing

Can combine with **context editing** for long-running workflows:

1. Claude makes many tool calls, context grows
2. Approaches threshold → Claude gets warning
3. Claude saves important info to `/memories`
4. Old tool results cleared automatically
5. Claude continues, referencing memory files

```python
context_management={
    "edits": [
        {
            "type": "clear_tool_uses_20250919",
            "trigger": {
                "type": "input_tokens",
                "value": 100000
            },
            "keep": {
                "type": "tool_uses",
                "value": 3
            },
            "exclude_tools": ["memory"]  # Don't clear memory tool calls
        }
    ]
}
```

---

## Security Considerations

1. **Path traversal protection** - Validate all paths stay within `/memories`
2. **Sensitive information** - Claude usually refuses to write sensitive info
3. **File storage size** - Track sizes, prevent unlimited growth
4. **Memory expiration** - Consider clearing old unused files

---

## Relationship to Claude Code

**Important**: This is an **API feature**, not a Claude Code feature.

| Feature | Where | How |
|---------|-------|-----|
| Memory Tool API | Anthropic API | Beta header + tool definition |
| Claude Code memory | Claude Code CLI | CLAUDE.md + hooks |

Claude Code doesn't use the Memory Tool API. It uses:
- CLAUDE.md files (loaded every session)
- Hooks (SessionEnd, PreCompact)
- Manual file operations

---

## Implications for Our System

### Could We Use This?

The Memory Tool API could theoretically be used to build memory into Claude Code if:
1. Claude Code adopted it internally
2. Or we built a wrapper that uses the API

### Our Current Approach Comparison

| Aspect | Memory Tool API | Our outputs/episodic/ |
|--------|-----------------|----------------------|
| Storage | /memories directory | outputs/episodic/ |
| Auto-check on start | Yes (built-in) | No (needs CLAUDE.md pointer) |
| Format | XML recommended | Markdown |
| Tool calls | view, create, str_replace, etc. | Read, Write, Edit |
| Context editing | Built-in integration | Manual |

### Key Insight

The Memory Tool API does what we're doing manually:
- File-based memory
- Explicit storage (not black-box)
- Claude manages the files

But it's API-only, not in Claude Code CLI yet.

---

## Sources

- [Memory Tool - Claude API Docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
- [Exploring Anthropic's Memory Tool - Leonie Monigatti](https://www.leoniemonigatti.com/blog/claude-memory-tool.html)
- [Managing context - Anthropic](https://www.anthropic.com/news/context-management)
