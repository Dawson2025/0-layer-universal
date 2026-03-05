---
resource_id: "738bd48f-bbb6-4ef3-a87b-ad6fab43ce9b"
resource_type: "knowledge"
resource_name: "STAGE_09_FIXING"
---
# Stage 09: Fixing — Universal Guide

## Purpose

Address issues identified in testing (stage 07) and criticism (stage 08). This is the **correction stage** — resolve problems, close gaps, and bring work up to quality.

## What This Stage IS

The fixing agent:
- Reads issues from stage 08 (critique) and failures from stage 07 (testing)
- Prioritizes fixes by severity (critical first, then major, then minor)
- Implements fixes to artifacts, code, documentation, or structure
- Documents what was fixed and how
- Triggers re-testing (loop back to stage 07) after fixes

## What This Stage IS NOT

The fixing agent does NOT:
- **Identify issues** — that's stage 07 (testing) and stage 08 (criticism) — fixing only resolves known issues
- **Redesign architecture** — that's stage 04 (if fixes require design changes, hand off back)
- **Add new features** — that's stage 01→06 (fixing corrects existing work, not extends it)
- **Critique quality** — that's stage 08 (fixing implements, not evaluates)

The agent **resolves identified problems**, not **finds new ones**.

## Methodology

```
outputs/
├── fixes_log.md                <- What was fixed, why, and how
└── stage_report.md
```

### Fixes Log Format

Each fix entry documents:
- **Issue reference**: Link to the critique/test that identified it
- **Severity**: Critical / Major / Minor
- **What was changed**: Files modified, specific changes
- **Verification**: How to confirm the fix works (feeds back to stage 07)

### Fix Workflow

1. Read stage 08 critique and stage 07 test failures
2. Sort by severity (critical → major → minor)
3. For each issue:
   a. Understand the root cause
   b. Implement the fix
   c. Note what was changed in fixes_log.md
4. After all fixes, trigger re-testing (stage 07)

## Inputs

- **Stage 08 outputs** — critique with categorized issues
- **Stage 07 outputs** — test failures with details
- **Stage 06 outputs** — artifacts to modify
- **Stage 04 outputs** — design specs (to ensure fixes stay within design)

## Outputs

| Output | Location | Format |
|--------|----------|--------|
| Fixes log | `outputs/fixes_log.md` | Documented fixes with references to issues |
| Modified artifacts | Entity itself | Fixed code, scripts, docs, etc. |
| Stage report | `outputs/stage_report.md` | Standard stage report format |

## Success Criteria

This stage is complete when:
1. All critical issues are resolved
2. All major issues are resolved (or explicitly deferred with rationale)
3. Minor issues are resolved or documented as known limitations
4. Fixes log documents all changes
5. Work is ready for re-testing (stage 07)

## Exit Protocol

1. Update `outputs/stage_report.md` with current status
2. If handing off to **stage 07** (testing): list what was fixed and which tests to re-run
3. If handing off to **stage 04** (design): note issues that require design changes beyond simple fixes
4. If handing off to **stage 01** (request_gathering): note requirements that need revision

## Common Patterns

- **Loop: 08 → 09 → 07 → 08**: The quality loop — critique, fix, re-test, re-critique
- **Severity-first**: Always fix critical issues before major, major before minor
- **Minimal changes**: Fix the issue, don't refactor the surrounding code
- **Root cause**: Fix the cause, not the symptom

## Anti-Patterns

- Fixing without understanding root cause (creates new issues)
- Scope creep: adding features while fixing (keep fixes focused)
- Not documenting fixes (makes re-testing impossible to target)
- Fixing minor issues while critical ones remain (wrong priority order)
