# REQ-02: Relative Path Computation

## Requirement

The pointer sync system MUST compute relative paths from the pointer file's directory to the resolved canonical target using `python3 os.path.relpath`.

## Specification

- Input: absolute path of pointer file's parent directory, absolute path of canonical target
- Output: relative path string (e.g., `../sibling_entity`, `.`, `../../parent/child`)
- Depends on: python3 being available in PATH
- Edge cases:
  - Same directory → `.`
  - Parent directory → `..`
  - Deeply nested → correct chain of `../` segments
  - Cross-branch (sibling entities) → correct traversal

## Rationale

Relative paths ensure pointers survive repository relocation (the repo can be cloned to any absolute path and pointers still work). Using `os.path.relpath` provides a battle-tested implementation.

## Test Coverage

- Tests 4.1 (sibling), 4.2 (deep to shallow), 4.3 (self-reference) validate relative path computation
