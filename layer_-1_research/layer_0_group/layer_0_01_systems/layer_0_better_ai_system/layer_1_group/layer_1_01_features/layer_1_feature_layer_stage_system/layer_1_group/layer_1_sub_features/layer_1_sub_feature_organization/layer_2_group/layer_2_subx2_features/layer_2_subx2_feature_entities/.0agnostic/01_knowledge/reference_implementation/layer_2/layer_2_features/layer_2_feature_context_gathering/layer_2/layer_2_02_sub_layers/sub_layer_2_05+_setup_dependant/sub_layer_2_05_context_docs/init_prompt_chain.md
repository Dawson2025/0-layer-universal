---
resource_id: "7bccb494-0096-465d-b689-043efc0a236f"
resource_type: "knowledge"
resource_name: "init_prompt_chain"
---
# Init Prompt Chain

## Overview
Init prompts form a chain from Layer 0 down to the current entity, providing cumulative context and rules.

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

## Inheritance Model

Each level inherits from above and can:
1. **Extend** - Add new rules
2. **Specialize** - Narrow general rules
3. **Override** - Replace rules (use sparingly)

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

## Application Order

1. Load Layer 0 init_prompt (base rules)
2. Apply Layer 1 init_prompt (project type rules)
3. Apply Layer 2 init_prompt (feature rules)
4. Apply Layer N init_prompt (current entity rules)

Later rules take precedence where conflicts exist.

## Example Chain

### Layer 0: Universal Framework
```markdown
# Universal Init Prompt
- Follow Layer-Stage conventions
- Use semantic versioning
- Document all public interfaces
```

### Layer 1: Python Project
```markdown
# Python Project Init Prompt
- Follow PEP 8 style guide
- Use type hints
- Prefer dataclasses for data structures
```

### Layer 2: Auth Feature
```markdown
# Auth Feature Init Prompt
- Never log credentials
- Use bcrypt for password hashing
- Tokens expire after 24 hours
```

### Layer 3: Login Component
```markdown
# Login Component Init Prompt
- Rate limit: 5 attempts per minute
- Lock account after 10 failures
- Send notification on suspicious activity
```

## Combined Context
The AI agent operating on the Login Component receives ALL of the above, with the most specific rules taking precedence.

## Best Practices

### DO:
- Keep each level focused on its scope
- Reference parent rules when extending
- Document overrides explicitly
- Use clear, specific language

### DON'T:
- Repeat parent rules unnecessarily
- Create conflicting rules without clear override
- Make rules too specific at high levels
- Assume context from other branches

## Finding Init Prompts

Standard locations:
1. `layer_N/layer_N_00_ai_manager_system/agnostic/init_prompt.md`
2. `layer_N/layer_N_00_ai_manager_system/{platform}/init_prompt.md`
3. `CLAUDE.md` (may contain or reference init prompt)

## Platform-Specific Chains

For platform-specific contexts:
```
Universal init_prompt.md
    └── Project agnostic init_prompt.md
        └── Feature agnostic init_prompt.md
            └── Feature {platform} init_prompt.md
```

Platform-specific init prompts extend agnostic ones, not replace them.
