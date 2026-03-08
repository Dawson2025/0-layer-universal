---
resource_id: "38458775-458b-4806-9145-ca66fae2b23d"
resource_type: "readme_output"
resource_name: "README"
---
# Need: Instance Context

**Branch**: [Instantiation Pattern](../README.md)

<!-- section_id: "81582bee-c85c-4f55-9ae9-b42068210dac" -->
## Definition

Each instance MUST carry context specific to its user/situation: profile, knowledge state, goals, and adaptation history.

<!-- section_id: "960568a8-bc35-4b52-9669-6a7e5351e5bd" -->
## Why This Matters

The value of instantiation is personalization. Without rich instance context, instances are just copies of the template. Context enables the AI to adapt — knowing what the student already understands, what they struggle with, and what their goals are.

<!-- section_id: "6ae62161-0ba3-49e1-8425-075252dd0b29" -->
## Acceptance Criteria

- [ ] Instance context includes user profile data
- [ ] Instance context tracks knowledge state (what the user knows/doesn't know)
- [ ] Instance context connects to user goals (career, learning objectives)
- [ ] Context is stored in the instance entity, not in the system template

<!-- section_id: "425edd20-0112-4763-9a08-38d6c2cee3a9" -->
## References

- [Requirements](requirements/)
- [User Stories](user_stories/)
