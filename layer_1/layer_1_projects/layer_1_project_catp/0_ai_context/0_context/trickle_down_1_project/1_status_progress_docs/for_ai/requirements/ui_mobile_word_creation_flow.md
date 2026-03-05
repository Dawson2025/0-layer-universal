---
resource_id: "d30b6e12-adfd-417c-8726-a97aedf980b0"
resource_type: "document"
resource_name: "ui_mobile_word_creation_flow"
---
# Mobile Word Creation Flow

- **Source Prompt**: `docs/prompts.txt/UI/ui_flow.md`

<!-- section_id: "9194cc00-a11b-4840-90a2-24c9cce292cf" -->
## Goal
Deliver a clear, top-to-bottom workflow for creating words on mobile screens, ensuring users know which word is selected and what actions to take next.

<!-- section_id: "4a8575d0-fa73-43bf-84c3-4d24dbc88f75" -->
## Functional Requirements
- When the viewport matches mobile dimensions, present the creation form as a vertical sequence with the following order:
  1. Selected word summary.
  2. Language selector/display.
  3. English word entry.
  4. Syllable Configuration section.
  5. Optimized Word Suggestions section.
  6. Existing English words list (when available).
- After users confirm syllable sounds, prompt for the new language spelling and optional media upload before rendering the Create Word action button.
- Preserve the desktop layout while applying the vertical reflow only to mobile-sized viewports.

<!-- section_id: "d54bbe79-aa66-4c93-b9e3-03edb2caf4a0" -->
## Acceptance Criteria
- On mobile screens, scrolling from top to bottom follows the exact hierarchy above without horizontal jumps or hidden sections.
- Selecting syllable sounds reveals inputs for spelling and media upload immediately before the Create Word button.
- Layout adjustments do not regress the desktop experience.

<!-- section_id: "29df3cc6-34e4-4484-a5c1-81a6f9fe0d21" -->
## Notes
- Ensure the Selected Word header remains visible on mobile to reinforce context before users edit additional fields.
- Break down the UI structure into reusable components where possible so that future sections can be inserted without disrupting the mobile order.
