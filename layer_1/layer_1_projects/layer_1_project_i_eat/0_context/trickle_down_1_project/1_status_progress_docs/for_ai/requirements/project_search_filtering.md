---
resource_id: "999322eb-fe5c-42b0-a78b-27e3a74336a3"
resource_type: "document"
resource_name: "project_search_filtering"
---
# My Projects Search

- **Source Prompt**: Conversation request – add searchable My Projects list (2025-??-??)

<!-- section_id: "a35af74d-373c-4d1d-9b06-78f9d90fccf6" -->
## Goal
Allow users to quickly locate a project by name from the My Projects dashboard, even when many projects are listed.

<!-- section_id: "5fd86643-4645-4800-9690-41324d2f6805" -->
## Functional Requirements
- Provide a search control within the My Projects page that filters visible project cards as the user types.
- Match project group names and any sub-project names so related branches surface together.
- Ensure the search operates on the client without requiring a page reload and falls back gracefully when the query is cleared.

<!-- section_id: "acfbcf45-6dd7-44b1-a1a0-adbc24268e49" -->
## Acceptance Criteria
- Typing a partial string narrows the list to only cards containing that text in the project or sub-project titles.
- Clearing the search field restores the full project list in its prior order.
- When no items match, the UI communicates that there are no results instead of showing an empty area.

<!-- section_id: "11b96cdf-e92b-4f87-ae67-39b4bcd1a390" -->
## Notes
- Keep the existing visual styling consistent with the My Projects layout; avoid introducing disruptive elements that push controls off-screen on smaller viewports.
- Consider future expansion for filtering by storage type or variant counts by leaving room near the search input.
