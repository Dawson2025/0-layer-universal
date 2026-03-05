---
resource_id: "e9567741-99ab-4f16-9859-b87da7082c94"
resource_type: "document"
resource_name: "memory_handling_protocol"
---
# Memory Handling Protocol

<!-- section_id: "344160fc-751d-4cbc-85c3-971a0115978e" -->
## Applicability
**When to use:** Whenever the user explicitly asks the agent to "remember" something (e.g., "Remember that I like...", "Remember this rule...").
**Scope:** Universal (applies to all interactions).
**Goal:** To ensure long-term memories are recorded accurately, located precisely, and confirmed to the user with evidence.

<!-- section_id: "18417630-dc0c-4a8f-bf72-1fd0b5a4969d" -->
## Protocol Steps

1.  **Record the Memory:** Update the appropriate context file (e.g., `universal_init_prompt.md`, a feature `README.md`, or a specific rule file).
2.  **Confirm with Exactness:** In your response to the user, you MUST explicitly provide the following in this specific order:
    *   **Where recorded:** Describe the location in natural language (e.g., "I've added this to the feature-level tools documentation...").
    *   **Exact Directory Location:** Provide the **full, absolute, or root-relative path** to the file(s) you modified. Do not just say "in the project folder." Show the path starting from `0_layer_universal` or the project root.
    *   **How context was updated:** Briefly explain the edit (e.g., "I appended a new 'Submission Safety Rule' section...").
    *   **Thing Remembered/Emphasis on the Code:** Explicitly point out the area/section where the memory was coded/written.

<!-- section_id: "2d57c987-0ea0-4c8a-9a3b-4ce76ec48e25" -->
## Example Response

> "I have remembered that rule.
>
> **Where recorded:** I added it to the Feature Tools documentation for the Applied Programming workflow.
> **Exact Location:** `code/1_layer_school/lang-trak-in-progress/0_context/layer_2_features/layer_2_feature_.../sub_layer_2.11_feature_tools/README.md`
> **How context was updated:** I created a new section titled `## Feature-Specific Rules` and added the 'Submission Safety Rule' there.
> **Thing Remembered/Emphasis on the Code:** I explicitly wrote: 'The AI agent is authorized to fill out forms... but FORBIDDEN from clicking the final Submit button.'"