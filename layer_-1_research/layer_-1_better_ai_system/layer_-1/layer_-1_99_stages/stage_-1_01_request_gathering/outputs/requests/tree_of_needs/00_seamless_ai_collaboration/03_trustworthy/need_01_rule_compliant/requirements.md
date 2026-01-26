# Need: Rule Compliant

**Branch**: [03_trustworthy](../)
**Question**: "Does AI follow the defined rules?"

---

## Definition

AI consistently follows the rules defined at each level of the hierarchy.
- Rules have clear priority and scope
- Conflicts are resolved predictably
- Rules can be discovered and understood

---

## Why This Matters

- Rules prevent mistakes
- Rules encode project conventions
- Rules must be followed consistently
- Conflicting rules cause confusion

---

## Requirements

### Rule Hierarchy (from request_07)
- MUST define rule priority levels (critical, standard, advisory)
- MUST specify scope (universal, layer, project, stage)
- MUST allow higher scopes to override lower
- SHOULD prevent conflicting rules at same level

### Conflict Resolution (from request_07)
- MUST define how conflicts are resolved
- MUST prefer more specific over general
- MUST prefer newer over older (with version tracking)
- SHOULD alert when conflicts detected

### Rule Registry (from request_07)
- MUST maintain registry of all active rules
- MUST track rule versions
- MUST indicate supersession relationships
- SHOULD support rule deprecation

### Active vs Archived Separation (from request_07)
- MUST clearly separate active from archived
- MUST indicate why rules were archived
- MUST link archived to superseding rules
- SHOULD prevent accidental use of archived

### Rule Discovery (from request_07)
- MUST have single entry point to find rules
- MUST categorize by topic
- MUST support search
- SHOULD auto-generate rule index

---

## Acceptance Criteria

- [ ] Rule hierarchy is defined and documented
- [ ] Priority levels clearly specified (critical/standard/advisory)
- [ ] Scopes clearly specified (universal/layer/project/stage)
- [ ] Conflict resolution algorithm exists and is documented
- [ ] Rule registry lists all active rules with versions
- [ ] Archived rules are clearly separated
- [ ] Single entry point finds all rules
- [ ] Rules include examples and rationale

---

## Integrated From

- request_07: REQ-07-F01, REQ-07-F02, REQ-07-F03, REQ-07-F04, REQ-07-F05, REQ-07-NF01
