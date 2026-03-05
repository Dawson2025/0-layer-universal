---
resource_id: "2e640f60-6a66-47e1-8828-ebde0966ae22"
resource_type: "document"
resource_name: "ui_selected_word_phoneme_feedback"
---
# Selected Word Phoneme Feedback

- **Source Prompt**: `docs/prompts.txt/UI/chosen_word_individual_phoneme_block_display_and_sound_off_display.md`

<!-- section_id: "7f87b115-cb61-47b9-883a-8f702b3c1e80" -->
## Goal
Guarantee that the Selected Word panel always shows interactive phoneme blocks and playback guidance, regardless of how the word was chosen.

<!-- section_id: "ef61cf28-8bb4-4da2-9e19-db556c75fb23" -->
## Functional Requirements
- Display the Selected Word section with individual phoneme blocks whenever a word is highlighted, whether it originated from syllable configuration blocks or the optimized/suggested word list.
- Highlight phoneme blocks in sync with playback and support existing interaction gestures (double-click, shift-click, control/command-click, right-click).
- Surface the instructional text explaining how to trigger phoneme sounds in all selection paths.

<!-- section_id: "da998c88-4db1-4fb1-b7a4-6aa964c10209" -->
## Acceptance Criteria
- Selecting a suggestion produces the same phoneme block rendering, highlighting behavior, and instructional copy as selecting from the syllable configuration area.
- Regression tests confirm the previously working path (selecting directly within syllable configuration) still behaves as expected.
- The Selected Word section never downgrades to plain text-only output.

<!-- section_id: "83c36b4e-ec86-4122-804a-1adc08e1c408" -->
## Notes
- Consolidate the rendering logic so both selection sources call a shared component/util, avoiding divergence over time.
- Consider adding automated UI coverage for both selection paths once the testing framework supports end-to-end checks.
