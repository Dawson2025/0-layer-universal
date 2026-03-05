---
resource_id: "be434e08-2dc0-485a-8fb7-862bf84b7698"
resource_type: "rule"
resource_name: "escalate_on_scope_violation"
---
# Rule: Escalate on Scope Violation

**Status**: MANDATORY
**Applies**: When an agent detects it is working outside its declared scope

---

<!-- section_id: "7cdafdad-f25a-4f1d-966c-b75dd0fbcbe0" -->
## When This Rule Activates

- Agent's current task doesn't match the Identity scope in its nearest `0AGNOSTIC.md`
- Agent is asked to modify files in a sibling or ancestor entity without explicit instruction
- Agent cannot determine its role from any available avenue (identity failure)
- Agent encounters conflicting rules from different chain levels

<!-- section_id: "f9129b36-0f78-4278-b74c-84138a755dbb" -->
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

<!-- section_id: "0899637a-0aaf-49a0-bff0-d5abe2fd5d97" -->
## Why Dynamic

Scope violations are rare. Most tasks fall within the agent's declared scope. Checking scope on every micro-task would add unnecessary overhead. This rule fires only when the agent notices a mismatch.

<!-- section_id: "3aba0e2e-9a89-407b-a3bf-a75acef01af0" -->
## Fail-Open Exception

If the agent cannot determine its scope (no `0AGNOSTIC.md` reachable through any avenue), it should:
1. Notify the user that identity context is missing
2. Operate with general best practices
3. Flag its output as "produced without entity context"

<!-- section_id: "7a64d592-4a07-4602-b32c-c0a97fef76b4" -->
## Related

- Principle: `knowledge/principles/graceful_degradation.md`
- Knowledge: `knowledge/context_chain_architecture.md`
