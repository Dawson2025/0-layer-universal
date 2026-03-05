---
resource_id: "7ac11a1a-e680-4996-9d43-b01933d468a3"
resource_type: "document"
resource_name: "ui_selected_word_phoneme_feedback"
---
# Selected Word Phoneme Feedback

- **Source Prompt**: `docs/prompts.txt/UI/chosen_word_individual_phoneme_block_display_and_sound_off_display.md`

<!-- section_id: "381239e5-2fcc-46a4-9e4a-1a98f8f3f39f" -->
## Goal
Guarantee that the Selected Word panel always shows interactive phoneme blocks and playback guidance, regardless of how the word was chosen.

<!-- section_id: "9f452ead-d684-470c-8292-7180ecf931e5" -->
## Functional Requirements
- Display the Selected Word section with individual phoneme blocks whenever a word is highlighted, whether it originated from syllable configuration blocks or the optimized/suggested word list.
- Highlight phoneme blocks in sync with playback and support existing interaction gestures (double-click, shift-click, control/command-click, right-click).
- Surface the instructional text explaining how to trigger phoneme sounds in all selection paths.

<!-- section_id: "506905f6-301e-4a50-9f71-ab20e55114de" -->
## Acceptance Criteria
- Selecting a suggestion produces the same phoneme block rendering, highlighting behavior, and instructional copy as selecting from the syllable configuration area.
- Regression tests confirm the previously working path (selecting directly within syllable configuration) still behaves as expected.
- The Selected Word section never downgrades to plain text-only output.

<!-- section_id: "d5edbbd3-ec2d-4486-85f8-32cf9c9442d4" -->
## Notes
- Consolidate the rendering logic so both selection sources call a shared component/util, avoiding divergence over time.
- Consider adding automated UI coverage for both selection paths once the testing framework supports end-to-end checks.
