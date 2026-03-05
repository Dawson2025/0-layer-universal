---
resource_id: "9511ff97-15cf-4f82-9515-800f3d547660"
resource_type: "document"
resource_name: "ui_mobile_word_creation_flow"
---
# Mobile Word Creation Flow

- **Source Prompt**: `docs/prompts.txt/UI/ui_flow.md`

<!-- section_id: "14130de2-63cb-4102-b647-0306ae15c7e9" -->
## Goal
Deliver a clear, top-to-bottom workflow for creating words on mobile screens, ensuring users know which word is selected and what actions to take next.

<!-- section_id: "589a0658-7719-400a-b947-8b4298d28e80" -->
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

<!-- section_id: "3eff9216-aa93-4d82-a865-edbb799c30d0" -->
## Acceptance Criteria
- On mobile screens, scrolling from top to bottom follows the exact hierarchy above without horizontal jumps or hidden sections.
- Selecting syllable sounds reveals inputs for spelling and media upload immediately before the Create Word button.
- Layout adjustments do not regress the desktop experience.

<!-- section_id: "c2db48df-f757-4d93-a8c4-3841b77b46db" -->
## Notes
- Ensure the Selected Word header remains visible on mobile to reinforce context before users edit additional fields.
- Break down the UI structure into reusable components where possible so that future sections can be inserted without disrupting the mobile order.
