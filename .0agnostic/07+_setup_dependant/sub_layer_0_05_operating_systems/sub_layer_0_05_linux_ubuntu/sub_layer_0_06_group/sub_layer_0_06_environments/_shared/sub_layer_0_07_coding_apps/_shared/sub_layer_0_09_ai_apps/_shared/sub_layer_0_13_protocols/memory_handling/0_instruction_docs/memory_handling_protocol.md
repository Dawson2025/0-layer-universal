---
resource_id: "2e9bc90e-e4dc-40dd-988a-81cbc19c008a"
resource_type: "document"
resource_name: "memory_handling_protocol"
---
# Memory Handling Protocol

<!-- section_id: "8789b025-6725-4591-970b-c976a1628223" -->
## Applicability
**When to use:** Whenever the user explicitly asks the agent to "remember" something (e.g., "Remember that I like...", "Remember this rule...").
**Scope:** Universal (applies to all interactions).
**Goal:** To ensure long-term memories are recorded accurately, located precisely, and confirmed to the user with evidence.

<!-- section_id: "49cc7222-d936-4854-a7db-55792c0bc066" -->
## Protocol Steps

1.  **Record the Memory:** Update the appropriate context file (e.g., `universal_init_prompt.md`, a feature `README.md`, or a specific rule file).
2.  **Confirm with Exactness:** In your response to the user, you MUST explicitly provide the following in this specific order:
    *   **Where recorded:** Describe the location in natural language (e.g., "I've added this to the feature-level tools documentation...").
    *   **Exact Directory Location:** Provide the **full, absolute, or root-relative path** to the file(s) you modified. Do not just say "in the project folder." Show the path starting from `0_layer_universal` or the project root.
    *   **How context was updated:** Briefly explain the edit (e.g., "I appended a new 'Submission Safety Rule' section...").
    *   **Thing Remembered/Emphasis on the Code:** Explicitly point out the area/section where the memory was coded/written.

<!-- section_id: "5a86ab3a-53e4-4973-997f-cec05090619e" -->
## Example Response

> "I have remembered that rule.
>
> **Where recorded:** I added it to the Feature Tools documentation for the Applied Programming workflow.
> **Exact Location:** `code/1_layer_school/lang-trak-in-progress/0_context/layer_2_features/layer_2_feature_.../sub_layer_2.11_feature_tools/README.md`
> **How context was updated:** I created a new section titled `## Feature-Specific Rules` and added the 'Submission Safety Rule' there.
> **Thing Remembered/Emphasis on the Code:** I explicitly wrote: 'The AI agent is authorized to fill out forms... but FORBIDDEN from clicking the final Submit button.'"