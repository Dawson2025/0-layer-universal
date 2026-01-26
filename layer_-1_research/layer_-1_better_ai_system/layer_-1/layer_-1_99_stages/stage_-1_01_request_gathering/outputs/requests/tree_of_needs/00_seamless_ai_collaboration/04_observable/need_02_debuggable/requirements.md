# Need: Debuggable

**Branch**: [04_observable](../)
**Question**: "Can I figure out what went wrong?"

---

## Definition

When things go wrong, the cause can be identified and fixed.
- Errors are clear and actionable
- Issues can be traced to source
- Fixes can be verified

---

## Why This Matters

- Things will break
- Need to find root cause
- Need to fix without breaking more
- Need to verify the fix worked

---

## Requirements

### Validation Suite (from request_08)
- MUST validate naming conventions
- MUST validate registry completeness
- MUST validate directory structure
- MUST validate status.json schema
- MUST validate documentation paths
- SHOULD provide clear error messages

### Error Diagnosis
- Errors MUST indicate what went wrong
- Errors MUST indicate where the problem is
- Errors SHOULD suggest fixes
- SHOULD support verbose/debug modes

### Traceability
- MUST be able to trace error to source
- MUST log significant operations
- SHOULD track state changes
- SHOULD support step-by-step replay

### Fix Verification
- MUST have way to verify fixes
- MUST have validation that can be re-run
- SHOULD auto-fix simple issues
- SHOULD prevent reintroduction of fixed issues

---

## Acceptance Criteria

- [ ] Validation suite covers all conventions
- [ ] Validation errors are clear and actionable
- [ ] Errors can be traced to source file/line
- [ ] Error messages suggest fixes
- [ ] Validation can be re-run to verify fixes
- [ ] Auto-fix available for simple issues
- [ ] Debug/verbose mode exists for deep diagnosis

---

## Integrated From

- request_08: REQ-08-F01, REQ-08-NF01
