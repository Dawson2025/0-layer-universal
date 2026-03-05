---
resource_id: "89c786a0-964a-4722-b9ad-fab9d9afc06b"
resource_type: "document"
resource_name: "ui_selected_word_phoneme_feedback"
---
# Selected Word Phoneme Feedback

- **Source Prompt**: `docs/prompts.txt/UI/chosen_word_individual_phoneme_block_display_and_sound_off_display.md`

<!-- section_id: "985b285f-5a97-4729-9662-59d51fa0487c" -->
## Goal
Guarantee that the Selected Word panel always shows interactive phoneme blocks and playback guidance, regardless of how the word was chosen.

<!-- section_id: "b450eae6-3529-49b9-8ee7-6d960b1c04f1" -->
## Functional Requirements
- Display the Selected Word section with individual phoneme blocks whenever a word is highlighted, whether it originated from syllable configuration blocks or the optimized/suggested word list.
- Highlight phoneme blocks in sync with playback and support existing interaction gestures (double-click, shift-click, control/command-click, right-click).
- Surface the instructional text explaining how to trigger phoneme sounds in all selection paths.

<!-- section_id: "a6f45d10-b342-47e6-bfaa-19d828d1e692" -->
## Acceptance Criteria
- Selecting a suggestion produces the same phoneme block rendering, highlighting behavior, and instructional copy as selecting from the syllable configuration area.
- Regression tests confirm the previously working path (selecting directly within syllable configuration) still behaves as expected.
- The Selected Word section never downgrades to plain text-only output.

<!-- section_id: "eb668a71-f08c-4af7-baa2-e30b06daf1e9" -->
## Notes
- Consolidate the rendering logic so both selection sources call a shared component/util, avoiding divergence over time.
- Consider adding automated UI coverage for both selection paths once the testing framework supports end-to-end checks.
