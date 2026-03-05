---
resource_id: "eaa44e50-e76a-41fa-a391-bcd5fa479bdb"
resource_type: "document"
resource_name: "user_authentication"
---
# User Authentication & Account Management

- **Source Prompt**: Existing implementation analysis (2025-10-15)
- **Related Implementation**: `app.py` routes 3088-3262, `features/auth.py`, `templates/login.html`, `templates/register.html`

<!-- section_id: "4d3176d8-027b-4b86-8b4e-3c0a71475242" -->
## Goal
Provide secure user authentication and account management to enable multi-user collaboration, personalized workspaces, and access control across the language tracking application.

<!-- section_id: "07fbafed-c231-4722-9e38-4c87c014d93d" -->
## Functional Requirements
- Support local username/password authentication with secure password hashing for users who prefer not to use cloud services.
- Integrate Firebase Authentication to allow OAuth-based login via Google and other providers.
- Provide user registration workflow that creates accounts with unique usernames and email addresses.
- Maintain user sessions across requests and provide secure logout functionality.
- Link Firebase user IDs to local user records for hybrid authentication support.
- Store user metadata including creation timestamps and active status flags.
- Protect routes and features based on authentication state (logged-in vs. anonymous).

<!-- section_id: "6baa09b6-927d-4856-905b-b0f9e25aa91f" -->
## Acceptance Criteria
- Users can register new accounts via `/register` with username, email, and password; passwords are hashed before storage.
- Users can log in via `/login` using either local credentials or Firebase OAuth (Google Sign-In).
- Successful authentication creates a server-side session that persists across page loads.
- Firebase-authenticated users are automatically linked to local user records via `firebase_uid` column.
- Logout clears the session and redirects to login page.
- Protected routes redirect unauthenticated users to the login page.
- Duplicate usernames or emails are rejected during registration with clear error messages.
- User info (username, email) is accessible throughout the application via `get_user_info()` helper.

<!-- section_id: "d5ce7b6d-6486-4769-891e-14570f5a6ae1" -->
## Notes
- The `users` table stores both locally-registered and Firebase-authenticated users.
- Firebase authentication is optional; the app functions fully with local auth if Firebase is unavailable.
- Session secret key should be rotated regularly in production environments.
- Consider adding email verification and password reset flows in future iterations.
