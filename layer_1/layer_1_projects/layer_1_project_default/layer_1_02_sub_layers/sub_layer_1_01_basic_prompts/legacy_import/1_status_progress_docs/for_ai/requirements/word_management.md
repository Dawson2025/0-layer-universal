---
resource_id: "7031b39c-9bd3-4a5e-907f-acd29c3d9fe2"
resource_type: "document"
resource_name: "word_management"
---
# Word Management & Editing

- **Source Prompt**: Existing implementation analysis (2025-10-15)
- **Related Implementation**: `app.py` routes 1066-1405, `templates/word_lookup.html`, `templates/word_edit.html`, `templates/words_display.html`

<!-- section_id: "faccf14f-98df-4452-9db8-10fc6d783bf7" -->
## Goal
Provide comprehensive word management capabilities including search, lookup, editing, and deletion to maintain and refine the constructed language vocabulary over time.

<!-- section_id: "7b0d1cfa-b597-44c9-9da5-8032375ece53" -->
## Functional Requirements
- Enable users to search and look up existing words by English translation, new language word, or phoneme content.
- Display word details including English meaning, constructed word, phonemes, language, and attached media.
- Provide a dedicated edit interface for modifying word attributes without recreating the word.
- Support updating word fields: English translation, new language spelling, phonemes, language assignment.
- Support composing multi-syllable words by adding ordered syllable blocks with onset, nucleus, and coda selections for each syllable.
- Provide inline audio preview controls for individual syllables and the assembled word during creation so users can hear the structure as they build it.
- Allow adding or removing video attachments to/from existing words.
- Surface associated video playback whenever a word detail page is viewed, including from modal or list contexts.
- Enable bulk viewing of all words in the current project with filtering options.
- Provide word deletion functionality with proper cleanup of associated media files.
- Track which user created each word for ownership and access control.

<!-- section_id: "0c98601f-791b-4a7b-a17f-1978a203074d" -->
## Acceptance Criteria
- Word lookup page (`/words/lookup`) accepts search queries and returns matching results from the current project.
- API endpoint `/api/lookup-word` searches across word fields and returns JSON results with word details.
- Word edit page (`/words/edit/<id>`) pre-populates form with current word data for modification.
- Updating a word via `/api/update-word/<id>` persists changes and updates phoneme frequency counts.
- Word creation form allows adding, reordering, and removing syllable blocks; submitted words persist the multi-syllable structure in the database.
- Selected Word panel exposes play controls for each syllable and whole-word playback that invoke TTS endpoints before saving.
- Removing a video via `/api/remove-video/<id>` deletes the file from storage and clears the database reference.
- Word detail and lookup views embed playable video components whenever a word has an attached clip, with clear affordances to add or replace media from that context.
- Deleting a word via `/api/delete-word/<id>` removes the database entry, decrements phoneme usage, and deletes associated media.
- Word display page (`/words/display`) renders all project words with search filtering and pagination.
- Search operates across multiple fields (English, new language, phonemes) and highlights matches.

<!-- section_id: "f0a5f893-ed0e-4b36-bcf3-32e5a8de79ca" -->
## Notes
- Word edits should validate phoneme selections against the project's available phoneme set.
- Media deletion must handle both local file system and cloud storage paths.
- Consider adding edit history or version tracking for collaborative editing scenarios.
- Bulk operations (delete multiple words, export word list) may be added in future iterations.
- Search could be enhanced with fuzzy matching or regex support for advanced queries.
