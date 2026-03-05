---
resource_id: "440464c7-98bf-4b55-8779-b667cb2fdf10"
resource_type: "document"
resource_name: "github_sso_token_setup"
---
# GitHub SSO Token Setup Guide

<!-- section_id: "d9ea0c28-0a34-4b2f-882e-8478ba7868ed" -->
## Overview

This guide documents the complete process for setting up GitHub Personal Access Tokens (PAT) with SAML SSO authorization for organizations that require Single Sign-On authentication.

<!-- section_id: "6e6d58fe-69f5-42f9-a043-e5ac8950d7b1" -->
## Compatibility (OS / Environment)

The **PAT + SSO authorization requirement is GitHub/org-side**, so the concept applies everywhere. What changes by OS/environment is **how you store credentials** and **how you complete the SSO web login**.

- ✅ **WSL (Ubuntu/Debian/etc.)**: Works well; browser-based SSO usually happens in your normal browser via WSLg, or via MCP Playwright/browser tooling.
- ✅ **Native Linux**: Same as WSL (store token via helper or OS keyring; authorize via browser).
- ✅ **macOS**: Same flow; recommend macOS Keychain-based credential manager or a scoped helper.
- ✅ **Windows (Git-for-Windows)**: Same flow; recommend Git Credential Manager (Windows Credential Manager) rather than Unix-path scripts.
- ⚠️ **CI (GitHub Actions, etc.)**: Prefer short-lived auth (`GITHUB_TOKEN`, GitHub App tokens, or injected secrets). Avoid long-lived PAT files.
- ⚠️ **Containers**: Similar to CI; treat as ephemeral and inject secrets at runtime, not baked into images.

<!-- section_id: "c5093871-c5da-4555-ac63-091b36878b5f" -->
## Problem Statement

When accessing repositories in organizations with SAML SSO enabled (like BYU-Idaho's `byui-math-dept`), Personal Access Tokens must be explicitly authorized for SSO before they can be used for Git operations.

<!-- section_id: "9e88e4fa-24f5-4f86-9052-f783c138c4d0" -->
### Error Symptoms

```bash
remote: The 'byui-math-dept' organization has enabled or enforced SAML SSO.
remote: To access this repository, visit https://github.com/orgs/byui-math-dept/sso?authorization_request=...
fatal: unable to access 'https://github.com/...': The requested URL returned error: 403
```

<!-- section_id: "85d3322a-c0d2-4a88-b9cb-58984913e0af" -->
## Solution: Complete Setup Process

<!-- section_id: "a1afdefb-0032-46e3-85ef-5c80a0d2a086" -->
### Step 1: Create Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token"
3. Set token details:
   - **Note**: Descriptive name (e.g., "Clone pac20026_fall2025 repo")
   - **Expiration**: Pick what your org/policy requires (some orgs allow “No expiration”; shorter expirations are safer)
   - **Scopes**: At minimum select `repo` for repository access
4. Click "Generate token"
5. **IMPORTANT**: Copy the token immediately (it won't be shown again)

<!-- section_id: "ec6c2032-a9f6-43d5-82bb-6e0afe208905" -->
### Step 2: Authorize Token for SSO

**This is the critical step that's often missed!**

#### Method 1: Using Browser Automation (Recommended)

Use MCP browser tools to automate the authorization:

```
1. Navigate to: https://github.com/settings/tokens
2. Find your token in the list
3. Click "Configure SSO" button next to your token
4. Click "Authorize" next to the organization
5. Complete SAML authentication (Duo, etc.)
6. Verify "Authorized" status appears
```

#### Method 2: Using Authorization Request URL

When Git shows an authorization URL:
```
1. Copy the authorization URL from the error message
2. Paste it in browser
3. Click "Continue" to start SSO flow
4. Complete Duo or other 2FA authentication
5. Confirm authorization success
```

<!-- section_id: "7da31f8c-74fc-4bd9-ae89-023ce9786cc8" -->
### Step 3: Store Token Securely

#### Option A (Legacy): `credential.helper store` + `~/.git-credentials`

Configure Git credential storage:

```bash
# Enable credential storage
git config --global credential.helper store

# Store credentials (one-time)
echo "https://USERNAME:TOKEN@github.com" > ~/.git-credentials
chmod 600 ~/.git-credentials
```

#### Option B (Preferred for SSO Orgs): Org-scoped credential helper (no `.git-credentials`)

For `byui-math-dept` repos, a safer pattern is a **custom Git credential helper** that only activates for:

`https://github.com/byui-math-dept/*`

This avoids storing a broad GitHub token in `~/.git-credentials` and prevents accidental reuse for other orgs.

**Where it lives (Linux / WSL / macOS):**
- Helper script: `~/.local/bin/git-credential-github-byui-math-dept`
- Token file: `~/.config/git/pats/byui-math-dept.pat` (permissions: `chmod 600`)
- Git config:
  - `credential.helper=~/.local/bin/git-credential-github-byui-math-dept`
  - `credential.useHttpPath=true` (required so Git includes `byui-math-dept/<repo>.git` in credential requests)

**OS / environment compatibility (this helper approach):**
- ✅ **WSL (Ubuntu/Debian/etc.)**: works inside the distro user environment.
- ✅ **Native Linux**: works per-user.
- ✅ **macOS**: works per-user (same Git credential helper protocol; paths differ but `~/.local/bin` works on most setups).
- ⚠️ **Windows (Git-for-Windows)**: the *approach* works, but the exact helper implementation differs (recommend Git Credential Manager / `manager-core`, or reimplement helper in PowerShell and store token via Windows facilities).
- ⚠️ **CI/containers**: prefer CI secrets + ephemeral tokens (or `GITHUB_TOKEN` in GitHub Actions); avoid long-lived PAT files baked into images.

**Note (permissions gotcha on Linux/WSL):**
- `~/.config` must be traversable (needs execute bit). If you accidentally run `chmod 600 ~/.config`, Git won’t be able to read `~/.config/git/pats/...`.

<!-- section_id: "8c56286f-2e8c-4493-ba71-45bd280b05f3" -->
### Step 4: Configure Git Remote

Ensure remote URL is clean (no embedded token):

```bash
cd /path/to/repository
git remote set-url origin https://github.com/ORG/REPO.git
```

<!-- section_id: "42356826-0a78-43b3-8e64-5ca1d9d72ae3" -->
### Step 5: Verify Setup

Test that everything works:

```bash
git fetch
git status
```

Should complete without errors.

<!-- section_id: "c4096406-3578-443c-9bec-90e431e6a6fc" -->
## Common Issues and Solutions

<!-- section_id: "87081139-c820-4070-b9ec-480fa9ccb8c2" -->
### Issue: Git Config Conflicts

**Symptom**: `gh auth git-credential` errors

**Solution**: Remove conflicting credential helpers:

```bash
# Check current helpers
git config --global --get-all credential.helper

# Remove all helpers
git config --global --unset-all credential.helper

# Set only store helper
git config --global credential.helper store
```

<!-- section_id: "5d02a99b-70f1-4331-ad7e-e42b3c8b42c7" -->
### Issue: Token Not Authorized After Creation

**Symptom**: 403 errors persist even with new token

**Solution**: Creating a token ≠ Authorizing it for SSO. Must complete SSO authorization step separately.

<!-- section_id: "72ffca01-0bfc-4a56-8272-2e74ff65238c" -->
### Issue: Need Multiple Tokens for Different Organizations

**Solution**: Each token can be authorized for multiple organizations. Alternatively, use multiple tokens and store them all in credentials file.

<!-- section_id: "3bf1ca86-a1dc-437e-89b0-b15307acb7db" -->
## Browser Automation Example

Today's successful setup using cursor-browser-extension MCP:

```
1. mcp_cursor-browser-extension_browser_navigate to GitHub tokens page
2. mcp_cursor-browser-extension_browser_click on "Configure SSO" button
3. mcp_cursor-browser-extension_browser_click on organization to authorize
4. User completed Duo authentication on phone
5. Browser remained open and authenticated
6. Git operations immediately worked
```

<!-- section_id: "10ed8c6f-7c1b-4ce7-8be3-79c2bffff426" -->
## Best Practices

<!-- section_id: "1aef6ab5-b616-4251-9eef-10162ae07977" -->
### Token Management

- ✅ Create tokens with descriptive names
- ✅ Set appropriate expiration dates
- ✅ Use minimal required scopes
- ✅ Authorize for SSO immediately after creation
- ✅ Store tokens securely in `~/.git-credentials`
- ❌ Never embed tokens in remote URLs
- ❌ Never commit tokens to repositories

<!-- section_id: "5e29cde5-d897-4a52-9959-df0e04580eeb" -->
### SSO Authorization

- ✅ Authorize token immediately after creation
- ✅ Verify authorization before using token
- ✅ Keep browser session open during setup
- ✅ Test with `git fetch` after authorization
- ❌ Don't assume token works without SSO auth
- ❌ Don't skip the "Configure SSO" step

<!-- section_id: "f3f7a200-649f-464e-9c2e-c6be1ea80d11" -->
### Browser Sessions

- ✅ Use MCP browser tools for automation
- ✅ Keep browser open across sessions
- ✅ Maintain authenticated state
- ❌ Don't close browser prematurely
- ❌ Don't paste tokens into places that will be logged/snapshotted

<!-- section_id: "d335a3f4-7cbf-4b38-8f57-bc61a9a52d27" -->
## Organization-Specific Notes

<!-- section_id: "581d268d-3d49-4152-8c46-e9e786ca318f" -->
### BYU-Idaho (byui-math-dept)

- **SSO Provider**: Church of Jesus Christ authentication
- **2FA**: Duo Security (push notifications)
- **Token Scopes Needed**: `repo` (minimum)
- **Typical Repositories**: Student course portfolios (e.g., `pac20026_fall2025`)

<!-- section_id: "1956d7e6-42ba-49cf-9f75-4e0fcee8a4ce" -->
### Authentication Flow

1. GitHub SSO page
2. Redirect to Church login (id.churchofjesuschrist.org)
3. Duo Security push notification
4. Redirect back to GitHub
5. Authorization complete

<!-- section_id: "d6eab8b7-7cb9-46da-8f63-a302b8bd3b97" -->
## Reference

- **Date Documented**: November 11, 2025
- **Working Example**: `/home/dawson/code/pac20026_fall2025`
- **Token Storage**: Prefer org-scoped helper + `~/.config/git/pats/byui-math-dept.pat` (or an equivalent secure OS-native credential manager)
- **Status**: ✅ Fully functional and tested
- **Related Docs**: 
  - `browser_management_policy.md` - Persistent browser sessions
  - `browser_opening_rule.md` - MCP browser usage
  - `git_commit_rule.md` - Git best practices

---

*This guide ensures reliable GitHub access for SAML SSO-protected repositories across all future sessions.*
