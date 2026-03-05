---
resource_id: "56f017db-679d-4852-9c7f-7593074ea192"
resource_type: "document"
resource_name: "search_all_fields_button"
---
# All Fields Search Reliability

- **Source Prompt**: `docs/prompts.txt/search_bar/all_fields_search_button_not_working_too_well.md`

<!-- section_id: "be6444dc-adb9-4631-8158-59342db799dd" -->
## Goal
Restore the expected behavior of the “All Fields” search so that users can discover words by matching across every searchable attribute in the View All Words page.

<!-- section_id: "776698cb-485e-47b6-a701-5dc6647e5999" -->
## Functional Requirements
- Ensure the all-fields search action scans every relevant word property (e.g., new language word, English translations, phoneme data, metadata) instead of delegating to the narrower field-specific queries.
- Provide consistent query execution feedback (loading indicators, empty-state messaging) aligned with other search buttons on the page.
- Guard against regressions by adding automated coverage that exercises the all-fields pathway.

<!-- section_id: "3249faf2-b80e-4b98-9f3d-581bb1a5f863" -->
## Acceptance Criteria
- Triggering the all-fields search returns matching records where any searchable field satisfies the query; previously working field-specific buttons remain unaffected.
- Entering a term that does not match any fields produces the expected “no results” UI state.
- The automated test suite exercises at least one positive and one negative all-fields search scenario.

<!-- section_id: "9ecd5021-6407-4e08-85ac-76e5ad4f0f58" -->
## Notes
- Validate that server- and client-side filters stay in sync; discrepancies between SQL, Firestore, and in-memory filters are the common root cause.
- Consider exposing telemetry or logging around the all-fields path to ease future debugging.
