---
resource_id: "840b0c79-1607-479f-bce9-0758a1c093d2"
resource_type: "rule"
resource_name: "context_traversal"
---
# Context Traversal Rules

<!-- section_id: "96259962-a9ee-4fe9-858e-fe3ff3353048" -->
## Rule: Always Traverse Before Working

Before starting ANY task:

1. **Read 0AGNOSTIC.md** at current directory (or nearest parent)
2. **Identify layer and stage** (layer_0, layer_1, layer_-1 + stage 01-11)
3. **Check .0agnostic/** for detailed resources if needed
4. **Read episodic memory** (.0agnostic/episodic_memory/index.md) if resuming work

<!-- section_id: "b6318c78-42e2-48f3-aeeb-1687808ad84a" -->
## Why This Matters

- Context informs how work should be done
- Previous sessions contain relevant decisions
- Rules may have been added since last session
- Skipping traversal causes errors and rework

<!-- section_id: "ec19653f-32dd-4a2b-b15a-910e3427b08f" -->
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

<!-- section_id: "60bf93be-1fcb-4c3c-9106-16edd164ce11" -->
## Integration with Episodic Memory

When you read episodic/index.md:
- See recent sessions and their summaries
- Understand what was done before
- Avoid repeating work or contradicting decisions
- Continue seamlessly from where previous session left off

