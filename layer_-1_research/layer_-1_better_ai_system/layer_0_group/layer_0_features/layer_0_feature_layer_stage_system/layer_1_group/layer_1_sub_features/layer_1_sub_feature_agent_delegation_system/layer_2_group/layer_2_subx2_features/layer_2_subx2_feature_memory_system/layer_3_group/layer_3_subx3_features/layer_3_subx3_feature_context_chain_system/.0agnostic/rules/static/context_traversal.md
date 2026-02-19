# Context Traversal Rules (Context Chain System)

## Rule: Always Traverse the Full 0AGNOSTIC Parent Chain

Before starting ANY task within the context_chain_system, traverse the complete 0AGNOSTIC.md parent chain (7 levels deep). Each level may override or extend context from its parent.

## Parent Chain Path

```
context_chain_system          (you are here)
  → memory_system             (parent — memory system context)
  → layer_stage_system        (grandparent — layer-stage framework)
  → layer_0_features          (feature registry context)
  → layer_0_group             (group-level context)
  → better_ai_system          (research project context)
  → layer_-1_research         (research root — terminal node)
```

## Why This Matters

- Parent entities define rules that apply to all children
- A rule at `better_ai_system` level applies here unless explicitly overridden
- Skipping levels risks missing constraints, naming conventions, or active protocols
- The chain establishes the full scope of applicable context

## Traversal Pattern

```
current_dir = context_chain_system/
while current_dir has 0AGNOSTIC.md:
    read 0AGNOSTIC.md → extract Identity, Rules, Triggers
    extract Parent path from 0AGNOSTIC.md
    if no Parent line → reached root, stop
    current_dir = resolve(Parent path)
    continue
```

## Quick Check

If you cannot read all 7 levels, at minimum read:
1. **Current** (context_chain_system) — immediate scope
2. **memory_system** — parent feature context
3. **layer_-1_research** — root-level constraints

## Integration with Episodic Memory

After traversal, check `.0agnostic/episodic_memory/index.md` at the current level to pick up session history before beginning work.
