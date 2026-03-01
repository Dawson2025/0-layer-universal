# Need: Bounded

**Branch**: [03_trustworthy](../)
**Question**: "Does AI stay within its scope?"

---

## Definition

AI operates within defined boundaries and doesn't exceed its authority.
- Scope limits are respected
- Permissions are clear
- Actions are appropriate to context

---

## Why This Matters

- Unconstrained AI can cause damage
- Different contexts have different permissions
- Need to limit blast radius
- Trust requires boundaries

---

## Requirements

### Scope Boundaries
- MUST define what each agent/level is allowed to do
- MUST define what is out of scope
- MUST not exceed defined scope
- SHOULD ask for permission when scope is unclear

### Permission Model
- MUST have clear permission levels
- MUST inherit permissions from hierarchy appropriately
- MUST allow scope-specific overrides
- SHOULD warn before taking high-impact actions

### Containment
- MUST not affect files/areas outside scope
- MUST not leak context between unrelated tasks
- MUST not make changes without appropriate authorization
- SHOULD operate with minimal necessary permissions

### Agent Role Boundaries (from request_03)
- MUST define Manager agent responsibilities and limits
- MUST define Worker agent responsibilities and limits
- MUST specify when each role is appropriate
- SHOULD include criteria for when to delegate vs execute directly

---

## Acceptance Criteria

- [ ] Scope boundaries are defined for each level
- [ ] Agent roles have clear limits
- [ ] AI respects scope boundaries
- [ ] High-impact actions require confirmation
- [ ] No changes made outside defined scope
- [ ] Permissions are documented and enforced
- [ ] Minimal necessary permissions are used

---

## Integrated From

- request_03: REQ-03-F01 (role definitions and scope)
- request_07: (implied from rule enforcement)
