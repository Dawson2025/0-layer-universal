# Need: Instance Context

**Branch**: [Instantiation Pattern](../README.md)

## Definition

Each instance MUST carry context specific to its user/situation: profile, knowledge state, goals, and adaptation history.

## Why This Matters

The value of instantiation is personalization. Without rich instance context, instances are just copies of the template. Context enables the AI to adapt — knowing what the student already understands, what they struggle with, and what their goals are.

## Acceptance Criteria

- [ ] Instance context includes user profile data
- [ ] Instance context tracks knowledge state (what the user knows/doesn't know)
- [ ] Instance context connects to user goals (career, learning objectives)
- [ ] Context is stored in the instance entity, not in the system template

## References

- [Requirements](requirements/)
- [User Stories](user_stories/)
