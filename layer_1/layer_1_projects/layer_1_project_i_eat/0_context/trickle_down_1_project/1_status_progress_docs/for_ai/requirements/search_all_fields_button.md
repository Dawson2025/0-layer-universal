---
resource_id: "4ea0c059-6dad-4817-bd5e-22fad20f60c7"
resource_type: "document"
resource_name: "search_all_fields_button"
---
# All Fields Search Reliability

- **Source Prompt**: `docs/prompts.txt/search_bar/all_fields_search_button_not_working_too_well.md`

<!-- section_id: "e79059da-401c-4d7c-96d8-5e0b80ddad2a" -->
## Goal
Restore the expected behavior of the “All Fields” search so that users can discover words by matching across every searchable attribute in the View All Words page.

<!-- section_id: "16f9f0c1-e50e-47d0-96b3-fc712d83b9ae" -->
## Functional Requirements
- Ensure the all-fields search action scans every relevant word property (e.g., new language word, English translations, phoneme data, metadata) instead of delegating to the narrower field-specific queries.
- Provide consistent query execution feedback (loading indicators, empty-state messaging) aligned with other search buttons on the page.
- Guard against regressions by adding automated coverage that exercises the all-fields pathway.

<!-- section_id: "e264de2c-09b5-4fa3-a33e-e0c1e2321f7a" -->
## Acceptance Criteria
- Triggering the all-fields search returns matching records where any searchable field satisfies the query; previously working field-specific buttons remain unaffected.
- Entering a term that does not match any fields produces the expected “no results” UI state.
- The automated test suite exercises at least one positive and one negative all-fields search scenario.

<!-- section_id: "a828b541-76c4-4e85-9206-6cca4388ee4a" -->
## Notes
- Validate that server- and client-side filters stay in sync; discrepancies between SQL, Firestore, and in-memory filters are the common root cause.
- Consider exposing telemetry or logging around the all-fields path to ease future debugging.
