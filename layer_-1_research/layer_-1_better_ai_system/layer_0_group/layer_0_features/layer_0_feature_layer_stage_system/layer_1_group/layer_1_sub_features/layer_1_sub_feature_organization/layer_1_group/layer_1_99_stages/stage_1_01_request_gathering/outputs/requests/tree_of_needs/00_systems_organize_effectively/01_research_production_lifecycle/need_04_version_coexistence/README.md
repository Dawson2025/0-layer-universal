# Need: Version Coexistence

**Branch**: [Research/Production Lifecycle](../README.md)

## Definition

Research and production versions MUST coexist within the same system, with production as the default and research as an opt-in mode.

## Why This Matters

The system isn't "in research" or "in production" — it's always both. Agents default to production context but can switch to research when explicitly asked. This coexistence is permanent, not transitional.

## Acceptance Criteria

- [ ] Production is the default mode for all agents
- [ ] Agents can opt into research context when directed
- [ ] Both versions share the same structural conventions (entity structure)
- [ ] Mode switching is explicit and traceable

## References

- [Requirements](requirements/)
- [User Stories](user_stories/)
