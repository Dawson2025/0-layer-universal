---
resource_id: "d3f8e059-2c3c-4a38-81d1-6d0b42acd677"
resource_type: "document"
resource_name: "group_collaboration"
---
# Group Collaboration System

- **Source Prompt**: Existing implementation analysis (2025-10-15)
- **Related Implementation**: `features/groups/routes.py`, `features/groups/api.py`, `features/groups/templates/`

<!-- section_id: "57ca6f4a-5708-439c-9467-7f477dec8331" -->
## Goal
Enable teams to collaborate on language projects by organizing users into groups, managing memberships, and sharing projects within those groups using secure invitation tokens.

<!-- section_id: "b3c4431c-04b3-4093-928c-8159dc73ddfc" -->
## Functional Requirements
- Allow authenticated users to create named groups with descriptions and designate themselves as group admin.
- Generate unique, shareable invitation tokens for each group that expire after a set period.
- Enable users to join groups by visiting invitation links (e.g., `/groups/join/<token>`).
- Track group memberships with join timestamps and prevent duplicate memberships.
- Display group members and project associations in a dedicated group detail page.
- Allow group admins to regenerate invitation tokens when needed.
- Support sharing projects to groups so all members can access them.
- List all groups a user belongs to on the groups dashboard (`/groups`).

<!-- section_id: "f8976df5-56da-404d-a06a-d790c9e79306" -->
## Acceptance Criteria
- Creating a group via `/groups/create` stores it in the `groups` table with the current user as admin.
- Each group automatically receives a unique invitation token stored in `group_invites` table with expiration timestamp.
- Visiting `/groups/join/<token>` adds the current user to the group if the token is valid and not expired.
- Group detail page (`/groups/<id>`) shows group name, description, member list, and invitation link.
- Admins can regenerate invitation tokens via API endpoint; old tokens are invalidated.
- Projects can be shared to groups, making them visible to all group members.
- Invalid or expired invitation tokens display appropriate error messages.
- Users cannot join the same group twice; duplicate attempts are gracefully rejected.

<!-- section_id: "7c31dc18-c77d-451a-9c14-23d184532844" -->
## Notes
- Group invites use unique tokens to avoid exposing internal group IDs in shareable URLs.
- Consider adding invitation expiration warnings and group role management (admin/member permissions) in future updates.
- Token expiration defaults are set during invite creation; adjust based on security requirements.
- Future work may include group-level project templates and bulk operations.
