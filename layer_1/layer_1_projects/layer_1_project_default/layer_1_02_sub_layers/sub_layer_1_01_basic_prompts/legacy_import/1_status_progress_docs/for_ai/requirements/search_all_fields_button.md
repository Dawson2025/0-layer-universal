---
resource_id: "19ec920b-1b47-4cdc-8937-bf58d3a5ea3b"
resource_type: "document"
resource_name: "search_all_fields_button"
---
# All Fields Search Reliability

- **Source Prompt**: `docs/prompts.txt/search_bar/all_fields_search_button_not_working_too_well.md`

<!-- section_id: "93c5ac9d-3d3c-4be4-8b09-cdfb404449c1" -->
## Goal
Restore the expected behavior of the “All Fields” search so that users can discover words by matching across every searchable attribute in the View All Words page.

<!-- section_id: "28a9cb1d-40c1-4e68-9a3f-3efde64e762b" -->
## Functional Requirements
- Ensure the all-fields search action scans every relevant word property (e.g., new language word, English translations, phoneme data, metadata) instead of delegating to the narrower field-specific queries.
- Provide consistent query execution feedback (loading indicators, empty-state messaging) aligned with other search buttons on the page.
- Guard against regressions by adding automated coverage that exercises the all-fields pathway.

<!-- section_id: "103cc004-64b6-4908-81f4-a45afe275efd" -->
## Acceptance Criteria
- Triggering the all-fields search returns matching records where any searchable field satisfies the query; previously working field-specific buttons remain unaffected.
- Entering a term that does not match any fields produces the expected “no results” UI state.
- The automated test suite exercises at least one positive and one negative all-fields search scenario.

<!-- section_id: "438362bc-2171-4512-bbbe-eef1aaae8b9e" -->
## Notes
- Validate that server- and client-side filters stay in sync; discrepancies between SQL, Firestore, and in-memory filters are the common root cause.
- Consider exposing telemetry or logging around the all-fields path to ease future debugging.
