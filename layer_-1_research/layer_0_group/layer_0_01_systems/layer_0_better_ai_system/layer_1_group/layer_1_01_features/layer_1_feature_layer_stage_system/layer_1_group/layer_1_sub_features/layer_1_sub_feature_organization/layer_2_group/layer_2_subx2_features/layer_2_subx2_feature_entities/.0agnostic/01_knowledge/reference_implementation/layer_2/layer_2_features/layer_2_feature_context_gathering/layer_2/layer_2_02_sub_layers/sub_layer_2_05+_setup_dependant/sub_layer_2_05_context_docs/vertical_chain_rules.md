---
resource_id: "069c3fdd-819d-4333-9842-527bd761315e"
resource_type: "knowledge"
resource_name: "vertical_chain_rules"
---
# Vertical Chain Rules

<!-- section_id: "813957b1-09f5-40c6-b9f1-bde1c71bad27" -->
## Always Gather
- All ancestor init_prompt.md files (up to Layer 0)
- All descendant status files

<!-- section_id: "dfe610bf-2104-4a45-90b5-ef6c730ef1f8" -->
## Ancestor Gathering
| Level | What to Gather |
|-------|----------------|
| Universal (0) | Framework rules, global init prompt |
| Parent (N-1) | Project context, conventions |
| Current (N) | Entity-specific rules |

<!-- section_id: "e0f08b7d-d480-42f2-baea-062c4858287c" -->
## Descendant Gathering
| Type | What to Gather |
|------|----------------|
| Sub-projects | Status, blockers |
| Features | Status, dependencies |
| Components | Status if task-relevant |

<!-- section_id: "e293f809-c939-4262-88fc-d754e386a0cb" -->
## Why Vertical is Always Relevant

<!-- section_id: "02765b04-eac3-403a-aaeb-c070ea3dc7c7" -->
### Ancestors Provide:
1. **Inherited Rules** - Constraints that apply to all descendants
2. **Context Inheritance** - Understanding of where current entity fits
3. **Convention Definitions** - Standards to follow
4. **Global Configuration** - Framework-wide settings

<!-- section_id: "9a856893-dc45-40e2-b61c-78b999be8208" -->
### Descendants Provide:
1. **Implementation Status** - Progress of sub-components
2. **Blockers** - Issues that affect parent
3. **Dependencies** - What sub-components need
4. **Completion State** - Whether work is done

<!-- section_id: "1ccd252a-b2b7-4382-b54e-85c3b000b9fc" -->
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

<!-- section_id: "acf323e9-6fb9-4c5b-b8a7-97d9dc17eae3" -->
## Priority Order
1. Current entity init_prompt.md (highest)
2. Parent init_prompt.md
3. Grandparent init_prompt.md
4. ... up to Layer 0
5. Direct child status files
6. Deeper descendant status files (lowest)
