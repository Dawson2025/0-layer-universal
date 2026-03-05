---
resource_id: "0fa5302a-86b1-4124-8a26-5db1a482c448"
resource_type: "document"
resource_name: "github_sso_token_setup"
---
# GitHub SSO Token Setup Guide

<!-- section_id: "2360e440-8561-4088-921e-529bcf9200de" -->
## Overview

This guide documents the complete process for setting up GitHub Personal Access Tokens (PAT) with SAML SSO authorization for organizations that require Single Sign-On authentication.

<!-- section_id: "7180ff12-b006-4e83-a60f-71e6523a7083" -->
## Compatibility (OS / Environment)

The **PAT + SSO authorization requirement is GitHub/org-side**, so the concept applies everywhere. What changes by OS/environment is **how you store credentials** and **how you complete the SSO web login**.

- ✅ **WSL (Ubuntu/Debian/etc.)**: Works well; browser-based SSO usually happens in your normal browser via WSLg, or via MCP Playwright/browser tooling.
- ✅ **Native Linux**: Same as WSL (store token via helper or OS keyring; authorize via browser).
- ✅ **macOS**: Same flow; recommend macOS Keychain-based credential manager or a scoped helper.
- ✅ **Windows (Git-for-Windows)**: Same flow; recommend Git Credential Manager (Windows Credential Manager) rather than Unix-path scripts.
- ⚠️ **CI (GitHub Actions, etc.)**: Prefer short-lived auth (`GITHUB_TOKEN`, GitHub App tokens, or injected secrets). Avoid long-lived PAT files.
- ⚠️ **Containers**: Similar to CI; treat as ephemeral and inject secrets at runtime, not baked into images.

<!-- section_id: "89a0f5a4-7122-4be3-a944-b773466cad83" -->
## Problem Statement

When accessing repositories in organizations with SAML SSO enabled (like BYU-Idaho's `byui-math-dept`), Personal Access Tokens must be explicitly authorized for SSO before they can be used for Git operations.

<!-- section_id: "5fa465f7-d377-4800-aab2-a427e3440098" -->
### Error Symptoms

```bash
remote: The 'byui-math-dept' organization has enabled or enforced SAML SSO.
remote: To access this repository, visit https://github.com/orgs/byui-math-dept/sso?authorization_request=...
fatal: unable to access 'https://github.com/...': The requested URL returned error: 403
```

<!-- section_id: "350a9728-836c-462a-8f06-dfe8b8230b0e" -->
## Solution: Complete Setup Process

<!-- section_id: "649c7a93-a8f6-4a2b-b89e-9b374ee74cd9" -->
### Step 1: Create Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token"
3. Set token details:
   - **Note**: Descriptive name (e.g., "Clone pac20026_fall2025 repo")
   - **Expiration**: Pick what your org/policy requires (some orgs allow “No expiration”; shorter expirations are safer)
   - **Scopes**: At minimum select `repo` for repository access
4. Click "Generate token"
5. **IMPORTANT**: Copy the token immediately (it won't be shown again)

<!-- section_id: "a037650a-a416-4f77-8b8e-5b3b8f6bf16a" -->
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

<!-- section_id: "aee9fb9a-a0c4-4bd8-956c-131c9e92f03a" -->
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

<!-- section_id: "ecc9a15c-d50f-4c64-86ec-41501b23a0e9" -->
### Step 4: Configure Git Remote

Ensure remote URL is clean (no embedded token):

```bash
cd /path/to/repository
git remote set-url origin https://github.com/ORG/REPO.git
```

<!-- section_id: "8bd28263-292e-4864-bf75-dce9f07e6741" -->
### Step 5: Verify Setup

Test that everything works:

```bash
git fetch
git status
```

Should complete without errors.

<!-- section_id: "dfa9e20e-e6a7-4390-a43d-7e7f733c364d" -->
## Common Issues and Solutions

<!-- section_id: "f0415c99-3414-4c02-a92f-56fbe56dd548" -->
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

<!-- section_id: "a2091bbc-e9de-41f0-a373-40c0cd56347b" -->
### Issue: Token Not Authorized After Creation

**Symptom**: 403 errors persist even with new token

**Solution**: Creating a token ≠ Authorizing it for SSO. Must complete SSO authorization step separately.

<!-- section_id: "cc59ce29-e7a2-4cb0-b87b-50cbea68f612" -->
### Issue: Need Multiple Tokens for Different Organizations

**Solution**: Each token can be authorized for multiple organizations. Alternatively, use multiple tokens and store them all in credentials file.

<!-- section_id: "7ac050d2-7054-43cd-86c5-f8aa4ccf9872" -->
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

<!-- section_id: "b5f121db-ca8f-4748-8814-0c7e3da6006b" -->
## Best Practices

<!-- section_id: "155df230-19d7-483f-9808-6345c0cfdcf4" -->
### Token Management

- ✅ Create tokens with descriptive names
- ✅ Set appropriate expiration dates
- ✅ Use minimal required scopes
- ✅ Authorize for SSO immediately after creation
- ✅ Store tokens securely in `~/.git-credentials`
- ❌ Never embed tokens in remote URLs
- ❌ Never commit tokens to repositories

<!-- section_id: "945eaa1f-1f91-4c68-9b03-f05bb6ae2dcf" -->
### SSO Authorization

- ✅ Authorize token immediately after creation
- ✅ Verify authorization before using token
- ✅ Keep browser session open during setup
- ✅ Test with `git fetch` after authorization
- ❌ Don't assume token works without SSO auth
- ❌ Don't skip the "Configure SSO" step

<!-- section_id: "3580de71-d886-4e88-a948-4b348c4f79d8" -->
### Browser Sessions

- ✅ Use MCP browser tools for automation
- ✅ Keep browser open across sessions
- ✅ Maintain authenticated state
- ❌ Don't close browser prematurely
- ❌ Don't paste tokens into places that will be logged/snapshotted

<!-- section_id: "7ba86bfa-1a94-4fba-a3e2-8ac206126403" -->
## Organization-Specific Notes

<!-- section_id: "141c2955-8415-4004-9f0b-72a4f3d316e5" -->
### BYU-Idaho (byui-math-dept)

- **SSO Provider**: Church of Jesus Christ authentication
- **2FA**: Duo Security (push notifications)
- **Token Scopes Needed**: `repo` (minimum)
- **Typical Repositories**: Student course portfolios (e.g., `pac20026_fall2025`)

<!-- section_id: "f56573dc-4eb4-449b-add6-5d9fb30debad" -->
### Authentication Flow

1. GitHub SSO page
2. Redirect to Church login (id.churchofjesuschrist.org)
3. Duo Security push notification
4. Redirect back to GitHub
5. Authorization complete

<!-- section_id: "a5408c38-2a58-42bd-855b-329def223bfc" -->
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
