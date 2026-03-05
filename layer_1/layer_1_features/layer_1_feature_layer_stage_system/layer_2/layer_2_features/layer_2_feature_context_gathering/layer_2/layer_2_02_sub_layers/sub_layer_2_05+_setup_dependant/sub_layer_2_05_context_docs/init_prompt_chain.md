---
resource_id: "be6f53ee-9f24-4c46-ad4a-72f4d46faac3"
resource_type: "document"
resource_name: "init_prompt_chain"
---
# Init Prompt Chain

<!-- section_id: "d13dd35b-309b-48e5-a342-9d1b72f282d4" -->
## Overview
Init prompts form a chain from Layer 0 down to the current entity, providing cumulative context and rules.

<!-- section_id: "0f2f8270-1fd0-4ac0-9354-4ffe44d03400" -->
## Chain Structure

```
Layer 0 (Universal)
    └── init_prompt.md (Framework rules)
        └── Layer 1 (Project Type)
            └── init_prompt.md (Type conventions)
                └── Layer 2 (Feature)
                    └── init_prompt.md (Feature specifics)
                        └── Layer 3 (Component)
                            └── init_prompt.md (Component details)
```

<!-- section_id: "6c6b96b1-9c48-4b58-932a-8765fc3a5bd7" -->
## Inheritance Model

Each level inherits from above and can:
1. **Extend** - Add new rules
2. **Specialize** - Narrow general rules
3. **Override** - Replace rules (use sparingly)

<!-- section_id: "88922c65-c040-47a4-b6a1-e798ef8a8de4" -->
## Chain Resolution

When gathering context, traverse UP then apply DOWN:

```
build_init_prompt_chain(entity):
    chain = []

    # Traverse up to root
    current = entity
    while current exists:
        chain.prepend(current.init_prompt)
        current = current.parent

    # chain[0] = Layer 0 (most general)
    # chain[n] = Current (most specific)

    return chain
```

<!-- section_id: "c3a22fa9-1267-42b7-bbf7-017036991241" -->
## Application Order

1. Load Layer 0 init_prompt (base rules)
2. Apply Layer 1 init_prompt (project type rules)
3. Apply Layer 2 init_prompt (feature rules)
4. Apply Layer N init_prompt (current entity rules)

Later rules take precedence where conflicts exist.

<!-- section_id: "588aeb2b-b611-45ce-a1fe-338e9f49f212" -->
## Example Chain

<!-- section_id: "1a8600f3-f3cb-4cf5-a0ff-fe7edb1809a0" -->
### Layer 0: Universal Framework
```markdown
# Universal Init Prompt
- Follow Layer-Stage conventions
- Use semantic versioning
- Document all public interfaces
```

<!-- section_id: "3039b8d9-232c-414a-b52b-a242858968d3" -->
### Layer 1: Python Project
```markdown
# Python Project Init Prompt
- Follow PEP 8 style guide
- Use type hints
- Prefer dataclasses for data structures
```

<!-- section_id: "85c27a8d-ac11-47d1-bf5f-65b218f42fa8" -->
### Layer 2: Auth Feature
```markdown
# Auth Feature Init Prompt
- Never log credentials
- Use bcrypt for password hashing
- Tokens expire after 24 hours
```

<!-- section_id: "d60266fe-30c2-47c6-aeec-8ae05684388b" -->
### Layer 3: Login Component
```markdown
# Login Component Init Prompt
- Rate limit: 5 attempts per minute
- Lock account after 10 failures
- Send notification on suspicious activity
```

<!-- section_id: "bd38f676-fdcc-4086-911f-540c32c6ab7e" -->
## Combined Context
The AI agent operating on the Login Component receives ALL of the above, with the most specific rules taking precedence.

<!-- section_id: "09d1bb46-62eb-4211-a29f-d7c0053d0807" -->
## Best Practices

<!-- section_id: "1f1daaea-76e3-4d35-81d0-8354b3193036" -->
### DO:
- Keep each level focused on its scope
- Reference parent rules when extending
- Document overrides explicitly
- Use clear, specific language

<!-- section_id: "15ed95b1-fa9e-451f-8e9a-01dc47e2f097" -->
### DON'T:
- Repeat parent rules unnecessarily
- Create conflicting rules without clear override
- Make rules too specific at high levels
- Assume context from other branches

<!-- section_id: "0639cce8-599b-4a82-8ec5-5a7f5aaf8e38" -->
## Finding Init Prompts

Standard locations:
1. `layer_N/layer_N_00_ai_manager_system/agnostic/init_prompt.md`
2. `layer_N/layer_N_00_ai_manager_system/{platform}/init_prompt.md`
3. `CLAUDE.md` (may contain or reference init prompt)

<!-- section_id: "4ba57f4d-ed81-400b-b421-fd00deb67366" -->
## Platform-Specific Chains

For platform-specific contexts:
```
Universal init_prompt.md
    └── Project agnostic init_prompt.md
        └── Feature agnostic init_prompt.md
            └── Feature {platform} init_prompt.md
```

Platform-specific init prompts extend agnostic ones, not replace them.
