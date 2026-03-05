---
resource_id: "196fac7b-d39e-40e2-b00f-ed8a22eb4bb3"
resource_type: "document"
resource_name: "ui_mobile_word_creation_flow"
---
# Mobile Word Creation Flow

- **Source Prompt**: `docs/prompts.txt/UI/ui_flow.md`

<!-- section_id: "244d96db-fb9f-4a04-97c1-03a49824c5ef" -->
## Goal
Deliver a clear, top-to-bottom workflow for creating words on mobile screens, ensuring users know which word is selected and what actions to take next.

<!-- section_id: "3f65b5c5-8666-47fc-8e33-33307ceb500d" -->
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

<!-- section_id: "db298952-bf82-4b79-9d55-89bccc91b97b" -->
## Acceptance Criteria
- On mobile screens, scrolling from top to bottom follows the exact hierarchy above without horizontal jumps or hidden sections.
- Selecting syllable sounds reveals inputs for spelling and media upload immediately before the Create Word button.
- Layout adjustments do not regress the desktop experience.

<!-- section_id: "ae3f68a6-bc2b-4ec4-9cbc-0d48fa6c41e7" -->
## Notes
- Ensure the Selected Word header remains visible on mobile to reinforce context before users edit additional fields.
- Break down the UI structure into reusable components where possible so that future sections can be inserted without disrupting the mobile order.
