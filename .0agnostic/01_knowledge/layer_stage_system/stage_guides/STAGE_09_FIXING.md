---
resource_id: "738bd48f-bbb6-4ef3-a87b-ad6fab43ce9b"
resource_type: "knowledge"
resource_name: "STAGE_09_FIXING"
---
# Stage 09: Fixing — Universal Guide

<!-- section_id: "b4bb31da-ae4b-4bb7-bfce-26b3465fc465" -->
## Purpose

Address issues identified in testing (stage 07) and criticism (stage 08). This is the **correction stage** — resolve problems, close gaps, and bring work up to quality.

<!-- section_id: "ad9009af-1dfa-4adf-b48d-f569dfb89246" -->
## What This Stage IS

The fixing agent:
- Reads issues from stage 08 (critique) and failures from stage 07 (testing)
- Prioritizes fixes by severity (critical first, then major, then minor)
- Implements fixes to artifacts, code, documentation, or structure
- Documents what was fixed and how
- Triggers re-testing (loop back to stage 07) after fixes

<!-- section_id: "47acd635-01fd-4e7e-81bc-8e59c53232fa" -->
## What This Stage IS NOT

The fixing agent does NOT:
- **Identify issues** — that's stage 07 (testing) and stage 08 (criticism) — fixing only resolves known issues
- **Redesign architecture** — that's stage 04 (if fixes require design changes, hand off back)
- **Add new features** — that's stage 01→06 (fixing corrects existing work, not extends it)
- **Critique quality** — that's stage 08 (fixing implements, not evaluates)

The agent **resolves identified problems**, not **finds new ones**.

<!-- section_id: "da67b3e8-c479-4210-8248-f690bbca29d5" -->
## Methodology

```
outputs/
├── fixes_log.md                <- What was fixed, why, and how
└── stage_report.md
```

<!-- section_id: "9e6ccae4-2ab9-4aa1-a2e5-437831da4e81" -->
### Fixes Log Format

Each fix entry documents:
- **Issue reference**: Link to the critique/test that identified it
- **Severity**: Critical / Major / Minor
- **What was changed**: Files modified, specific changes
- **Verification**: How to confirm the fix works (feeds back to stage 07)

<!-- section_id: "eaedb5b7-e004-4572-80cb-9d755eb40c77" -->
### Fix Workflow

1. Read stage 08 critique and stage 07 test failures
2. Sort by severity (critical → major → minor)
3. For each issue:
   a. Understand the root cause
   b. Implement the fix
   c. Note what was changed in fixes_log.md
4. After all fixes, trigger re-testing (stage 07)

<!-- section_id: "3514b188-9bed-43b4-b0d8-e9c8d06e869b" -->
## Inputs

- **Stage 08 outputs** — critique with categorized issues
- **Stage 07 outputs** — test failures with details
- **Stage 06 outputs** — artifacts to modify
- **Stage 04 outputs** — design specs (to ensure fixes stay within design)

<!-- section_id: "fea19f58-8bb5-49f7-907c-d39c89c71f58" -->
## Outputs

| Output | Location | Format |
|--------|----------|--------|
| Fixes log | `outputs/fixes_log.md` | Documented fixes with references to issues |
| Modified artifacts | Entity itself | Fixed code, scripts, docs, etc. |
| Stage report | `outputs/stage_report.md` | Standard stage report format |

<!-- section_id: "5e42d965-e484-4ed8-a917-db8ec1d8ab1b" -->
## Success Criteria

This stage is complete when:
1. All critical issues are resolved
2. All major issues are resolved (or explicitly deferred with rationale)
3. Minor issues are resolved or documented as known limitations
4. Fixes log documents all changes
5. Work is ready for re-testing (stage 07)

<!-- section_id: "7b137364-e43c-414c-b4db-055c4b7b43ed" -->
## Exit Protocol

1. Update `outputs/stage_report.md` with current status
2. If handing off to **stage 07** (testing): list what was fixed and which tests to re-run
3. If handing off to **stage 04** (design): note issues that require design changes beyond simple fixes
4. If handing off to **stage 01** (request_gathering): note requirements that need revision

<!-- section_id: "4fc0f0c1-789e-4972-8a98-081cf7d5778b" -->
## Common Patterns

- **Loop: 08 → 09 → 07 → 08**: The quality loop — critique, fix, re-test, re-critique
- **Severity-first**: Always fix critical issues before major, major before minor
- **Minimal changes**: Fix the issue, don't refactor the surrounding code
- **Root cause**: Fix the cause, not the symptom

<!-- section_id: "3f2b4daf-630c-469a-a2a3-3ad590ecbafc" -->
## Anti-Patterns

- Fixing without understanding root cause (creates new issues)
- Scope creep: adding features while fixing (keep fixes focused)
- Not documenting fixes (makes re-testing impossible to target)
- Fixing minor issues while critical ones remain (wrong priority order)
