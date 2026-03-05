---
resource_id: "273d5d1d-9e9e-411c-8335-42e20fa7160f"
resource_type: "document"
resource_name: "vertical_chain_rules"
---
# Vertical Chain Rules

<!-- section_id: "f849f3ec-2d81-4799-8975-b9075b80365c" -->
## Always Gather
- All ancestor init_prompt.md files (up to Layer 0)
- All descendant status files

<!-- section_id: "6ab471ba-d9d5-4f14-95ff-aec57030ff90" -->
## Ancestor Gathering
| Level | What to Gather |
|-------|----------------|
| Universal (0) | Framework rules, global init prompt |
| Parent (N-1) | Project context, conventions |
| Current (N) | Entity-specific rules |

<!-- section_id: "cb437a5e-2032-48d5-a08e-0762b38d1a30" -->
## Descendant Gathering
| Type | What to Gather |
|------|----------------|
| Sub-projects | Status, blockers |
| Features | Status, dependencies |
| Components | Status if task-relevant |

<!-- section_id: "fae4f038-6515-444c-93a2-506e9b4e7374" -->
## Why Vertical is Always Relevant

<!-- section_id: "307e1fe6-5595-4966-8c06-3ebba1cf61a9" -->
### Ancestors Provide:
1. **Inherited Rules** - Constraints that apply to all descendants
2. **Context Inheritance** - Understanding of where current entity fits
3. **Convention Definitions** - Standards to follow
4. **Global Configuration** - Framework-wide settings

<!-- section_id: "2cfc9b11-de04-4474-a1b4-60624872b910" -->
### Descendants Provide:
1. **Implementation Status** - Progress of sub-components
2. **Blockers** - Issues that affect parent
3. **Dependencies** - What sub-components need
4. **Completion State** - Whether work is done

<!-- section_id: "1b3408ae-5ecd-4830-9b61-5c6499bb0192" -->
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

<!-- section_id: "6a0f95a4-d872-4786-9537-14e4e1452da1" -->
## Priority Order
1. Current entity init_prompt.md (highest)
2. Parent init_prompt.md
3. Grandparent init_prompt.md
4. ... up to Layer 0
5. Direct child status files
6. Deeper descendant status files (lowest)
