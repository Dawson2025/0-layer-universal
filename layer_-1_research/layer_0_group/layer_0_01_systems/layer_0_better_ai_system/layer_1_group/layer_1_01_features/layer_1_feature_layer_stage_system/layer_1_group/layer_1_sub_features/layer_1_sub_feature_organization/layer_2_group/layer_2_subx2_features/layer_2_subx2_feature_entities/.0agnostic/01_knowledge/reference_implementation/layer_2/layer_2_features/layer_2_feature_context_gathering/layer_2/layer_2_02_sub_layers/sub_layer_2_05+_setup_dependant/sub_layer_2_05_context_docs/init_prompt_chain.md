---
resource_id: "7bccb494-0096-465d-b689-043efc0a236f"
resource_type: "knowledge"
resource_name: "init_prompt_chain"
---
# Init Prompt Chain

<!-- section_id: "faa2be5f-7b84-480c-98a4-a69d2341e8f0" -->
## Overview
Init prompts form a chain from Layer 0 down to the current entity, providing cumulative context and rules.

<!-- section_id: "d5a64134-d2e5-447f-8239-93968da2852c" -->
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

<!-- section_id: "f243b94e-1884-488a-b3d2-1a4136d4d747" -->
## Inheritance Model

Each level inherits from above and can:
1. **Extend** - Add new rules
2. **Specialize** - Narrow general rules
3. **Override** - Replace rules (use sparingly)

<!-- section_id: "235e9995-f6ba-42b2-8494-591a2928ee8c" -->
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

<!-- section_id: "7b63e743-452d-4301-90f8-6d66aa19ef6b" -->
## Application Order

1. Load Layer 0 init_prompt (base rules)
2. Apply Layer 1 init_prompt (project type rules)
3. Apply Layer 2 init_prompt (feature rules)
4. Apply Layer N init_prompt (current entity rules)

Later rules take precedence where conflicts exist.

<!-- section_id: "7d34b731-5067-4658-bd1c-0f91579938cf" -->
## Example Chain

<!-- section_id: "9090436d-311a-4a4b-bd9f-0b424476b1b5" -->
### Layer 0: Universal Framework
```markdown
# Universal Init Prompt
- Follow Layer-Stage conventions
- Use semantic versioning
- Document all public interfaces
```

<!-- section_id: "4e0c2b0e-6886-4c83-8769-5cf56675c216" -->
### Layer 1: Python Project
```markdown
# Python Project Init Prompt
- Follow PEP 8 style guide
- Use type hints
- Prefer dataclasses for data structures
```

<!-- section_id: "4733fc04-f527-4063-9bf2-235a0078f60d" -->
### Layer 2: Auth Feature
```markdown
# Auth Feature Init Prompt
- Never log credentials
- Use bcrypt for password hashing
- Tokens expire after 24 hours
```

<!-- section_id: "64d272aa-6618-4e9e-ad08-ccdf7d0845f2" -->
### Layer 3: Login Component
```markdown
# Login Component Init Prompt
- Rate limit: 5 attempts per minute
- Lock account after 10 failures
- Send notification on suspicious activity
```

<!-- section_id: "1166e36b-fa5e-46d2-83b7-172f585ed2cd" -->
## Combined Context
The AI agent operating on the Login Component receives ALL of the above, with the most specific rules taking precedence.

<!-- section_id: "1ed212f6-de66-4a76-ac1c-b27b72e467d2" -->
## Best Practices

<!-- section_id: "5b9ebbce-a9fa-49ce-bcab-fa56c95dc0ce" -->
### DO:
- Keep each level focused on its scope
- Reference parent rules when extending
- Document overrides explicitly
- Use clear, specific language

<!-- section_id: "e59be3c0-3325-4095-b952-a033102e23f2" -->
### DON'T:
- Repeat parent rules unnecessarily
- Create conflicting rules without clear override
- Make rules too specific at high levels
- Assume context from other branches

<!-- section_id: "c1c40aa9-3419-4219-9dae-ea0a81fb68ab" -->
## Finding Init Prompts

Standard locations:
1. `layer_N/layer_N_00_ai_manager_system/agnostic/init_prompt.md`
2. `layer_N/layer_N_00_ai_manager_system/{platform}/init_prompt.md`
3. `CLAUDE.md` (may contain or reference init prompt)

<!-- section_id: "e6dcc985-24a5-4d74-a112-79cc97ce7c41" -->
## Platform-Specific Chains

For platform-specific contexts:
```
Universal init_prompt.md
    └── Project agnostic init_prompt.md
        └── Feature agnostic init_prompt.md
            └── Feature {platform} init_prompt.md
```

Platform-specific init prompts extend agnostic ones, not replace them.
