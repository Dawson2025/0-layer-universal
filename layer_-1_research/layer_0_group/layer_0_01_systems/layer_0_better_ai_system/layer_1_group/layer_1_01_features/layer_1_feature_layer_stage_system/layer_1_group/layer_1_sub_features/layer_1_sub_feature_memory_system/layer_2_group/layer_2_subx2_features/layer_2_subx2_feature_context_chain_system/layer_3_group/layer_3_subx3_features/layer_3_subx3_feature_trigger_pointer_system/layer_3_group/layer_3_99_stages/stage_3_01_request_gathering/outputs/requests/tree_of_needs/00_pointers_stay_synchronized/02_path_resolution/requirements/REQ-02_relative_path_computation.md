---
resource_id: "5bd5efb7-9db9-4f6c-b656-3643738d584a"
resource_type: "output"
resource_name: "REQ-02_relative_path_computation"
---
# REQ-02: Relative Path Computation

<!-- section_id: "b7b5638e-dfde-4329-abb7-24e21c3f06de" -->
## Requirement

The pointer sync system MUST compute correct relative paths from the pointer file's directory to the resolved canonical target.

<!-- section_id: "c493bcbc-49e4-498b-a578-d2812537de9c" -->
## Specification

- Input: location of pointer file, location of canonical target
- Output: relative path string (e.g., `../sibling_entity`, `.`, `../../parent/child`)
- Edge cases MUST be handled:
  - Same directory → `.`
  - Parent directory → `..`
  - Deeply nested → correct chain of `../` segments
  - Cross-branch (sibling entities) → correct traversal

<!-- section_id: "6d9b2ef7-e3d2-4f58-a923-9f3cabc39b49" -->
## Rationale

Relative paths ensure pointers survive repository relocation (the repo can be cloned to any absolute path and pointers still work).

> **Design note**: Implementation details (specific tools, languages, libraries) are documented in stage 04 design outputs.

<!-- section_id: "51e049d3-c126-4125-8f3b-6e52b492a371" -->
## Test Coverage

- Tests 4.1 (sibling), 4.2 (deep to shallow), 4.3 (self-reference) validate relative path computation
