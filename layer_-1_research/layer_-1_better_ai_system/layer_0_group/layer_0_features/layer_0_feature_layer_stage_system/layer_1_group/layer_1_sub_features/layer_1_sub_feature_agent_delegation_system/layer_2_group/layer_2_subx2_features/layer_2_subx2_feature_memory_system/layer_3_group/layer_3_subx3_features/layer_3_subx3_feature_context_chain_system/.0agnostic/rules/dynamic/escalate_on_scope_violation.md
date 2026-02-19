# Rule: Escalate on Scope Violation

**Status**: MANDATORY
**Applies**: When an agent detects it is working outside its declared scope

---

## When This Rule Activates

- Agent's current task doesn't match the Identity scope in its nearest `0AGNOSTIC.md`
- Agent is asked to modify files in a sibling or ancestor entity without explicit instruction
- Agent cannot determine its role from any available avenue (identity failure)
- Agent encounters conflicting rules from different chain levels

## Rule

When scope is unclear or violated, escalate rather than guess:

1. **Detect the violation**:
   - Current task scope doesn't match `0AGNOSTIC.md` Identity → Scope
   - No `0AGNOSTIC.md` reachable (identity failure)
   - Multiple conflicting Identity definitions found

2. **Stop work** on the out-of-scope task

3. **Escalate to the user** with:
   - What you were asked to do
   - What your declared scope is (quote the Identity section)
   - Why you think this is out of scope
   - Suggested alternatives (delegate to correct entity, expand scope, or proceed with acknowledgment)

4. **Do not guess** — an agent with wrong scope produces wrong output

## Why Dynamic

Scope violations are rare. Most tasks fall within the agent's declared scope. Checking scope on every micro-task would add unnecessary overhead. This rule fires only when the agent notices a mismatch.

## Fail-Open Exception

If the agent cannot determine its scope (no `0AGNOSTIC.md` reachable through any avenue), it should:
1. Notify the user that identity context is missing
2. Operate with general best practices
3. Flag its output as "produced without entity context"

## Related

- Principle: `knowledge/principles/graceful_degradation.md`
- Knowledge: `knowledge/context_chain_architecture.md`
