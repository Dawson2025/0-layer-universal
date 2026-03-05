---
resource_id: "14c65d9e-ffef-4a90-b39c-e886d9240880"
resource_type: "document"
resource_name: "project_search_filtering"
---
# My Projects Search

- **Source Prompt**: Conversation request – add searchable My Projects list (2025-??-??)

<!-- section_id: "1771d238-5570-40b2-a105-03e18254677f" -->
## Goal
Allow users to quickly locate a project by name from the My Projects dashboard, even when many projects are listed.

<!-- section_id: "d1357351-6c06-4695-aab4-0874a21f5ca3" -->
## Functional Requirements
- Provide a search control within the My Projects page that filters visible project cards as the user types.
- Match project group names and any sub-project names so related branches surface together.
- Ensure the search operates on the client without requiring a page reload and falls back gracefully when the query is cleared.

<!-- section_id: "24fa3849-6753-43ab-b9e0-a35b5b00a552" -->
## Acceptance Criteria
- Typing a partial string narrows the list to only cards containing that text in the project or sub-project titles.
- Clearing the search field restores the full project list in its prior order.
- When no items match, the UI communicates that there are no results instead of showing an empty area.

<!-- section_id: "8b60c445-9187-4fed-85c0-8a1ef6f3ceed" -->
## Notes
- Keep the existing visual styling consistent with the My Projects layout; avoid introducing disruptive elements that push controls off-screen on smaller viewports.
- Consider future expansion for filtering by storage type or variant counts by leaving room near the search input.
