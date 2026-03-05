---
resource_id: "f4159f8c-dc0a-4d3a-a8ca-359fd8eb3147"
resource_type: "readme
output"
resource_name: "README"
---
# Need: Version Coexistence

**Branch**: [Research/Production Lifecycle](../README.md)

<!-- section_id: "55038a42-7bb1-45c4-8d67-b98177413f6c" -->
## Definition

Research and production versions MUST coexist within the same system, with production as the default and research as an opt-in mode.

<!-- section_id: "e705a64f-d3d1-49ee-b220-70681aae0415" -->
## Why This Matters

The system isn't "in research" or "in production" — it's always both. Agents default to production context but can switch to research when explicitly asked. This coexistence is permanent, not transitional.

<!-- section_id: "243529e2-7fc0-4812-9532-f2ba8d093877" -->
## Acceptance Criteria

- [ ] Production is the default mode for all agents
- [ ] Agents can opt into research context when directed
- [ ] Both versions share the same structural conventions (entity structure)
- [ ] Mode switching is explicit and traceable

<!-- section_id: "3af2dc72-1280-4329-aa21-43eb217ef25e" -->
## References

- [Requirements](requirements/)
- [User Stories](user_stories/)
