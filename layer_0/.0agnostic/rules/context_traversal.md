# Context Traversal Rules

## Rule: Always Traverse Before Working

Before starting ANY task:

1. **Read 0AGNOSTIC.md** at current directory (or nearest parent)
2. **Identify layer and stage** (layer_0, layer_1, layer_-1 + stage 01-11)
3. **Check .0agnostic/** for detailed resources if needed
4. **Read episodic memory** (.0agnostic/episodic_memory/index.md) if resuming work

## Why This Matters

- Context informs how work should be done
- Previous sessions contain relevant decisions
- Rules may have been added since last session
- Skipping traversal causes errors and rework

## Traversal Pattern

```
Start at working directory
  ↓
Read 0AGNOSTIC.md (lean context)
  ↓
Need more detail? → Load .0agnostic/[topic]/
  ↓
Resuming work? → Read .0agnostic/episodic_memory/index.md
  ↓
Begin task with full context
```

## Integration with Episodic Memory

When you read episodic/index.md:
- See recent sessions and their summaries
- Understand what was done before
- Avoid repeating work or contradicting decisions
- Continue seamlessly from where previous session left off

