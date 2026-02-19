# Stage Boundary Rule

**Type**: Static (always applies)
**Inherits from**: `layer_0/.0agnostic/02_rules/static/STAGE_BOUNDARY_RULE.md`

## Rule

Stage agents MUST NOT perform work that belongs to another stage. When work falls outside scope, the agent stops, documents the out-of-scope work in its stage report, and hands off to the correct stage.

## Common Boundary Violations

| If in... | Do NOT... | Instead... |
|----------|-----------|------------|
| 01 (request gathering) | Design solutions | Document the need, hand off to 04 |
| 02 (research) | Write requirements | Document findings, hand off to 01 |
| 04 (design) | Write code | Document the design, hand off to 06 |
| 06 (development) | Redesign architecture | Flag the design issue, hand off to 04 |
| 07 (testing) | Fix bugs | Document failures, hand off to 09 |

## Escalation

When a stage agent encounters work outside its scope:
1. Document it in `outputs/stage_report.md` under "Open Items"
2. Note which stage should handle it
3. Continue with in-scope work
4. The manager reads the stage report and routes the work appropriately
