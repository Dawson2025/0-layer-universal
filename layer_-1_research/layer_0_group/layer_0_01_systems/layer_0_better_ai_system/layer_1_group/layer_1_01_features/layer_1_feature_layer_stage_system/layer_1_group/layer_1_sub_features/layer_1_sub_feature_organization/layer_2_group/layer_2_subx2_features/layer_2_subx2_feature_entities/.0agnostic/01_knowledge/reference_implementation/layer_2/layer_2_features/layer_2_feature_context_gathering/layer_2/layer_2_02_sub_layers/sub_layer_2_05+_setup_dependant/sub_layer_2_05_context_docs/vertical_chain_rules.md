---
resource_id: "069c3fdd-819d-4333-9842-527bd761315e"
resource_type: "knowledge"
resource_name: "vertical_chain_rules"
---
# Vertical Chain Rules

## Always Gather
- All ancestor init_prompt.md files (up to Layer 0)
- All descendant status files

## Ancestor Gathering
| Level | What to Gather |
|-------|----------------|
| Universal (0) | Framework rules, global init prompt |
| Parent (N-1) | Project context, conventions |
| Current (N) | Entity-specific rules |

## Descendant Gathering
| Type | What to Gather |
|------|----------------|
| Sub-projects | Status, blockers |
| Features | Status, dependencies |
| Components | Status if task-relevant |

## Why Vertical is Always Relevant

### Ancestors Provide:
1. **Inherited Rules** - Constraints that apply to all descendants
2. **Context Inheritance** - Understanding of where current entity fits
3. **Convention Definitions** - Standards to follow
4. **Global Configuration** - Framework-wide settings

### Descendants Provide:
1. **Implementation Status** - Progress of sub-components
2. **Blockers** - Issues that affect parent
3. **Dependencies** - What sub-components need
4. **Completion State** - Whether work is done

## Traversal Algorithm

```
gather_vertical_context(entity):
    context = []

    # Gather ancestors (up)
    current = entity.parent
    while current exists:
        context.append(current.init_prompt)
        current = current.parent

    # Gather descendants (down)
    for child in entity.children:
        context.append(child.status)
        context.extend(gather_descendant_status(child))

    return context
```

## Priority Order
1. Current entity init_prompt.md (highest)
2. Parent init_prompt.md
3. Grandparent init_prompt.md
4. ... up to Layer 0
5. Direct child status files
6. Deeper descendant status files (lowest)
