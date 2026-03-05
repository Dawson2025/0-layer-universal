---
resource_id: "01bef924-c1f2-4fa1-9fa9-c36b18fff02b"
resource_type: "document"
resource_name: "project_search_filtering"
---
# My Projects Search

- **Source Prompt**: Conversation request – add searchable My Projects list (2025-??-??)

<!-- section_id: "143122f6-e49d-4ce8-b166-78bd54effe22" -->
## Goal
Allow users to quickly locate a project by name from the My Projects dashboard, even when many projects are listed.

<!-- section_id: "0876dc5e-7fc2-495e-97fc-bb091f792e31" -->
## Functional Requirements
- Provide a search control within the My Projects page that filters visible project cards as the user types.
- Match project group names and any sub-project names so related branches surface together.
- Ensure the search operates on the client without requiring a page reload and falls back gracefully when the query is cleared.

<!-- section_id: "6356c5e1-efb4-49b5-9c6b-5e8b8801da36" -->
## Acceptance Criteria
- Typing a partial string narrows the list to only cards containing that text in the project or sub-project titles.
- Clearing the search field restores the full project list in its prior order.
- When no items match, the UI communicates that there are no results instead of showing an empty area.

<!-- section_id: "3631707a-29ec-4ecd-92d8-1eaf551cc4e1" -->
## Notes
- Keep the existing visual styling consistent with the My Projects layout; avoid introducing disruptive elements that push controls off-screen on smaller viewports.
- Consider future expansion for filtering by storage type or variant counts by leaving room near the search input.
