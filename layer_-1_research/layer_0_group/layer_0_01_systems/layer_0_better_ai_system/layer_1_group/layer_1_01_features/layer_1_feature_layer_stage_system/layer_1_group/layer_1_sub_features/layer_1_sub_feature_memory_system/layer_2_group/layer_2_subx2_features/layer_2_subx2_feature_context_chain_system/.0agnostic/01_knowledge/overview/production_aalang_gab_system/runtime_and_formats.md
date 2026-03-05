---
resource_id: "e622c503-2230-41ef-ae65-bf63c0a072f2"
resource_type: "knowledge"
resource_name: "runtime_and_formats"
---
# Runtime Behaviors & Format Specifications

<!-- section_id: "65c600b5-53d8-4cdd-97c2-ed01ed3923d9" -->
## Overview

The runtime and format specs define how AALang agents behave during execution and how they format their output. These are defined in two separate files that all personas reference.

**Sources**:
- `layer_0/layer_0_01_ai_manager_system/professor/gab-runtime.jsonld`
- `layer_0/layer_0_01_ai_manager_system/professor/gab-formats.jsonld`

---

<!-- section_id: "ac0e8766-c1a5-43dd-acec-37e074ae3d85" -->
## Runtime Behaviors (gab-runtime.jsonld)

The runtime defines cross-persona behaviors — patterns that every persona in the agent follows consistently.

<!-- section_id: "aad0cee2-eb53-4cf7-84a5-f08503900b73" -->
### DebugModeCheck

Every persona checks the DebugModeStateActor before producing output:
- **Debug ON**: Include internal reasoning, decision rationale, state transitions
- **Debug OFF**: Clean user-facing output only

This is checked at the start of every persona's execution turn.

<!-- section_id: "880df15a-2eab-433c-b7fe-62c7c37d90f2" -->
### UserQuestionHandling

When the user asks a question mid-execution:
- Pause current mode work
- Address the question
- Resume mode work
- Do NOT reset mode progress

This prevents user questions from disrupting the execution flow.

<!-- section_id: "e91c67b4-dacb-494b-b8a5-0d07ba9a2eab" -->
### DecisionLoggingPattern

Every significant decision is logged to the DecisionLogStateActor:
- What decision was made
- Why (rationale)
- What alternatives were considered
- Confidence level

This creates an audit trail in `build-log.md` format.

<!-- section_id: "ecca3051-c70b-41f0-951a-d07a548a9812" -->
### ProductNameIdentification

Early in execution, identify and lock the product name:
- Extract from user description
- Confirm with user
- Store in ProductNameStateActor
- Use consistently in all output

<!-- section_id: "eb543129-e831-4a55-b026-872f6f6d5df2" -->
### GenerationDebugFileCheck

Before entering Generation mode:
- Check if debug files should be produced
- Prepare file structure for output
- Validate that all prerequisite information is available

<!-- section_id: "e86d14dc-af0a-4ca2-8ef8-759acebd53e4" -->
### GenerationReadinessCheck

Gate check before Generation mode begins:
- All required state actors populated?
- Spec from Formalization mode complete?
- User has approved the approach?
- Quality prerequisites met?

<!-- section_id: "467f29ac-733e-4b29-9d08-a0f4d8430ca2" -->
### ModeTransitionValidation

When transitioning between modes:
- Verify exit conditions of current mode are met
- Verify entry conditions of next mode are met
- Log the transition in DecisionLog
- Update state actors with transition metadata

<!-- section_id: "664c92cb-e531-437c-9a4a-ad3870cd6316" -->
### CommonErrorHandling

When errors occur during execution:
- Log the error with context
- Attempt recovery within the current mode
- If unrecoverable, communicate to user with clear explanation
- Do NOT silently fail or skip steps

---

<!-- section_id: "70741cad-5694-41f1-b5a2-c73bc79d9e94" -->
## Format Specifications (gab-formats.jsonld)

The format specs define what output looks like in different contexts.

<!-- section_id: "6bdf6782-ba55-41d9-8d19-c372b4ff5df3" -->
### Debug Logging Format

When debug mode is ON, output includes:

```
[DEBUG] Mode: <current_mode>
[DEBUG] Actor: <current_actor> (<persona>)
[DEBUG] State: <relevant_state_summary>
[DEBUG] Decision: <what_was_decided>
[DEBUG] Rationale: <why>
```

<!-- section_id: "581ea58b-8e37-446f-9558-5d4a7a295556" -->
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

<!-- section_id: "40e16632-71e5-48fe-93e1-445f1c9011cf" -->
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

<!-- section_id: "a84fdad5-8ebc-42af-a405-30d5a50919da" -->
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

<!-- section_id: "878ef03d-de1b-4372-8b24-ce230a8f4553" -->
## Practical Implications

1. **Debug mode is a first-class feature**: Not an afterthought — it's baked into every persona's execution
2. **Decisions are auditable**: The DecisionLog creates a complete history of why the agent did what it did
3. **Error handling is consistent**: Every persona follows the same error pattern
4. **User questions don't break flow**: The runtime defines how to handle interruptions gracefully

---

*Knowledge area: aalang_gab_system/runtime_and_formats*
*Last updated: 2026-02-07*
