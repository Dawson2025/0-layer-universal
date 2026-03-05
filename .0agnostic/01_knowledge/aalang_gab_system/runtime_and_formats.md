---
resource_id: "ae107012-a9cf-46ab-9ee2-1c484b47601a"
resource_type: "knowledge"
resource_name: "runtime_and_formats"
---
# Runtime Behaviors & Format Specifications

## Overview

The runtime and format specs define how AALang agents behave during execution and how they format their output. These are defined in two separate files that all personas reference.

**Sources**:
- `layer_0/layer_0_01_ai_manager_system/professor/gab-runtime.jsonld`
- `layer_0/layer_0_01_ai_manager_system/professor/gab-formats.jsonld`

---

## Runtime Behaviors (gab-runtime.jsonld)

The runtime defines cross-persona behaviors — patterns that every persona in the agent follows consistently.

### DebugModeCheck

Every persona checks the DebugModeStateActor before producing output:
- **Debug ON**: Include internal reasoning, decision rationale, state transitions
- **Debug OFF**: Clean user-facing output only

This is checked at the start of every persona's execution turn.

### UserQuestionHandling

When the user asks a question mid-execution:
- Pause current mode work
- Address the question
- Resume mode work
- Do NOT reset mode progress

This prevents user questions from disrupting the execution flow.

### DecisionLoggingPattern

Every significant decision is logged to the DecisionLogStateActor:
- What decision was made
- Why (rationale)
- What alternatives were considered
- Confidence level

This creates an audit trail in `build-log.md` format.

### ProductNameIdentification

Early in execution, identify and lock the product name:
- Extract from user description
- Confirm with user
- Store in ProductNameStateActor
- Use consistently in all output

### GenerationDebugFileCheck

Before entering Generation mode:
- Check if debug files should be produced
- Prepare file structure for output
- Validate that all prerequisite information is available

### GenerationReadinessCheck

Gate check before Generation mode begins:
- All required state actors populated?
- Spec from Formalization mode complete?
- User has approved the approach?
- Quality prerequisites met?

### ModeTransitionValidation

When transitioning between modes:
- Verify exit conditions of current mode are met
- Verify entry conditions of next mode are met
- Log the transition in DecisionLog
- Update state actors with transition metadata

### CommonErrorHandling

When errors occur during execution:
- Log the error with context
- Attempt recovery within the current mode
- If unrecoverable, communicate to user with clear explanation
- Do NOT silently fail or skip steps

---

## Format Specifications (gab-formats.jsonld)

The format specs define what output looks like in different contexts.

### Debug Logging Format

When debug mode is ON, output includes:

```
[DEBUG] Mode: <current_mode>
[DEBUG] Actor: <current_actor> (<persona>)
[DEBUG] State: <relevant_state_summary>
[DEBUG] Decision: <what_was_decided>
[DEBUG] Rationale: <why>
```

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

## Practical Implications

1. **Debug mode is a first-class feature**: Not an afterthought — it's baked into every persona's execution
2. **Decisions are auditable**: The DecisionLog creates a complete history of why the agent did what it did
3. **Error handling is consistent**: Every persona follows the same error pattern
4. **User questions don't break flow**: The runtime defines how to handle interruptions gracefully

---

*Knowledge area: aalang_gab_system/runtime_and_formats*
*Last updated: 2026-02-07*
