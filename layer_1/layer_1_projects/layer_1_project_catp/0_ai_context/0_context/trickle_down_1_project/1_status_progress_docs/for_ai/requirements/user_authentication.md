---
resource_id: "b88d37cf-1052-436d-b5f5-4a069feffdc1"
resource_type: "document"
resource_name: "user_authentication"
---
# User Authentication & Account Management

- **Source Prompt**: Existing implementation analysis (2025-10-15)
- **Related Implementation**: `app.py` routes 3088-3262, `features/auth.py`, `templates/login.html`, `templates/register.html`

<!-- section_id: "00060f40-9776-4555-bf81-a4d591e304cc" -->
## Goal
Provide secure user authentication and account management to enable multi-user collaboration, personalized workspaces, and access control across the language tracking application.

<!-- section_id: "0fbfbfec-892e-4430-93d6-1a2d989bf48c" -->
## Functional Requirements
- Support local username/password authentication with secure password hashing for users who prefer not to use cloud services.
- Integrate Firebase Authentication to allow OAuth-based login via Google and other providers.
- Provide user registration workflow that creates accounts with unique usernames and email addresses.
- Maintain user sessions across requests and provide secure logout functionality.
- Link Firebase user IDs to local user records for hybrid authentication support.
- Store user metadata including creation timestamps and active status flags.
- Protect routes and features based on authentication state (logged-in vs. anonymous).

<!-- section_id: "2246b646-ed8d-4b8f-be42-92c6d2cc4f8c" -->
## Acceptance Criteria
- Users can register new accounts via `/register` with username, email, and password; passwords are hashed before storage.
- Users can log in via `/login` using either local credentials or Firebase OAuth (Google Sign-In).
- Successful authentication creates a server-side session that persists across page loads.
- Firebase-authenticated users are automatically linked to local user records via `firebase_uid` column.
- Logout clears the session and redirects to login page.
- Protected routes redirect unauthenticated users to the login page.
- Duplicate usernames or emails are rejected during registration with clear error messages.
- User info (username, email) is accessible throughout the application via `get_user_info()` helper.

<!-- section_id: "ac7a1483-94a1-4e07-be6c-77c4d19de395" -->
## Notes
- The `users` table stores both locally-registered and Firebase-authenticated users.
- Firebase authentication is optional; the app functions fully with local auth if Firebase is unavailable.
- Session secret key should be rotated regularly in production environments.
- Consider adding email verification and password reset flows in future iterations.
