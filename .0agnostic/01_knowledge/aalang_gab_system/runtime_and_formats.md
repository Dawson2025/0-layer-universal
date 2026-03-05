---
resource_id: "ae107012-a9cf-46ab-9ee2-1c484b47601a"
resource_type: "knowledge"
resource_name: "runtime_and_formats"
---
# Runtime Behaviors & Format Specifications

<!-- section_id: "f2ef8d4b-0c6c-4ccf-b256-c9a26bdcc3bd" -->
## Overview

The runtime and format specs define how AALang agents behave during execution and how they format their output. These are defined in two separate files that all personas reference.

**Sources**:
- `layer_0/layer_0_01_ai_manager_system/professor/gab-runtime.jsonld`
- `layer_0/layer_0_01_ai_manager_system/professor/gab-formats.jsonld`

---

<!-- section_id: "6ee2b344-7c55-4187-a4d8-089dc05ed842" -->
## Runtime Behaviors (gab-runtime.jsonld)

The runtime defines cross-persona behaviors — patterns that every persona in the agent follows consistently.

<!-- section_id: "9339a55b-4411-4bae-be00-c47266ffb945" -->
### DebugModeCheck

Every persona checks the DebugModeStateActor before producing output:
- **Debug ON**: Include internal reasoning, decision rationale, state transitions
- **Debug OFF**: Clean user-facing output only

This is checked at the start of every persona's execution turn.

<!-- section_id: "ea7c14d6-978c-4627-a5da-c7d48ee937af" -->
### UserQuestionHandling

When the user asks a question mid-execution:
- Pause current mode work
- Address the question
- Resume mode work
- Do NOT reset mode progress

This prevents user questions from disrupting the execution flow.

<!-- section_id: "4c43568b-4586-4d0b-95a4-ea923376f64d" -->
### DecisionLoggingPattern

Every significant decision is logged to the DecisionLogStateActor:
- What decision was made
- Why (rationale)
- What alternatives were considered
- Confidence level

This creates an audit trail in `build-log.md` format.

<!-- section_id: "c56fa63f-c6ab-425c-910f-3e98634b67e1" -->
### ProductNameIdentification

Early in execution, identify and lock the product name:
- Extract from user description
- Confirm with user
- Store in ProductNameStateActor
- Use consistently in all output

<!-- section_id: "25fea269-c277-4eaa-a07e-1bec98845013" -->
### GenerationDebugFileCheck

Before entering Generation mode:
- Check if debug files should be produced
- Prepare file structure for output
- Validate that all prerequisite information is available

<!-- section_id: "1972d711-935d-43a4-94bc-82ece9fb0197" -->
### GenerationReadinessCheck

Gate check before Generation mode begins:
- All required state actors populated?
- Spec from Formalization mode complete?
- User has approved the approach?
- Quality prerequisites met?

<!-- section_id: "3bd37998-a4a9-4860-ac5c-334d49ffdbb8" -->
### ModeTransitionValidation

When transitioning between modes:
- Verify exit conditions of current mode are met
- Verify entry conditions of next mode are met
- Log the transition in DecisionLog
- Update state actors with transition metadata

<!-- section_id: "a7987add-65f7-4654-81ca-b554f274cb49" -->
### CommonErrorHandling

When errors occur during execution:
- Log the error with context
- Attempt recovery within the current mode
- If unrecoverable, communicate to user with clear explanation
- Do NOT silently fail or skip steps

---

<!-- section_id: "5ab79173-e5d2-4435-a9ff-fbe130e7e214" -->
## Format Specifications (gab-formats.jsonld)

The format specs define what output looks like in different contexts.

<!-- section_id: "dd32c6c5-3c84-413e-b252-576cc7749be5" -->
### Debug Logging Format

When debug mode is ON, output includes:

```
[DEBUG] Mode: <current_mode>
[DEBUG] Actor: <current_actor> (<persona>)
[DEBUG] State: <relevant_state_summary>
[DEBUG] Decision: <what_was_decided>
[DEBUG] Rationale: <why>
```

<!-- section_id: "019e08da-bf52-4d02-8843-69ca215fc574" -->
### Decision Logging Format (build-log.md)

Decisions are logged in a structured format:

```markdown
## Decision: <title>
- **Mode**: <which_mode>
- **Actor**: <which_actor>
- **Options Considered**: <list>
- **Chosen**: <option>
- **Rationale**: <why>
- **Confidence**: <0.0-1.0>
```

<!-- section_id: "3e7e4da4-9321-4ce3-a9e6-d5533ec4899d" -->
### Output Format Rules

**Debug Mode ON**:
- Show all internal reasoning
- Include state actor values
- Show confidence calculations
- Display mode transition gates

**Debug Mode OFF**:
- Clean, user-facing output only
- Hide internal reasoning
- Show only final results and questions
- Professional, concise formatting

---

<!-- section_id: "186865a8-5e7f-4ace-b3f3-b0125cf743e5" -->
## How Runtime & Formats Are Referenced

Every persona definition in an AALang agent includes a reference to the runtime:

```json
{
  "references": ["gab-runtime.jsonld"],
  "behaviors": ["DebugModeCheck", "DecisionLoggingPattern", ...]
}
```

This means all personas in the agent share the same runtime behaviors — consistency is enforced by the runtime spec, not by individual persona definitions.

---

<!-- section_id: "a7abaace-d8cd-4d85-a7cf-db7a1eb19c42" -->
## Practical Implications

1. **Debug mode is a first-class feature**: Not an afterthought — it's baked into every persona's execution
2. **Decisions are auditable**: The DecisionLog creates a complete history of why the agent did what it did
3. **Error handling is consistent**: Every persona follows the same error pattern
4. **User questions don't break flow**: The runtime defines how to handle interruptions gracefully

---

*Knowledge area: aalang_gab_system/runtime_and_formats*
*Last updated: 2026-02-07*
