---
resource_id: "0bf4a29d-db89-4a49-9c31-6e6a72b34f33"
resource_type: "document"
resource_name: "github_sso_token_setup"
---
# GitHub SSO Token Setup Guide

<!-- section_id: "323e2d94-db05-4ef2-8806-79a0a54bc835" -->
## Overview

This guide documents the complete process for setting up GitHub Personal Access Tokens (PAT) with SAML SSO authorization for organizations that require Single Sign-On authentication.

<!-- section_id: "8c165131-2fa4-464f-b885-54c216b3c2f2" -->
## Compatibility (OS / Environment)

The **PAT + SSO authorization requirement is GitHub/org-side**, so the concept applies everywhere. What changes by OS/environment is **how you store credentials** and **how you complete the SSO web login**.

- ✅ **WSL (Ubuntu/Debian/etc.)**: Works well; browser-based SSO usually happens in your normal browser via WSLg, or via MCP Playwright/browser tooling.
- ✅ **Native Linux**: Same as WSL (store token via helper or OS keyring; authorize via browser).
- ✅ **macOS**: Same flow; recommend macOS Keychain-based credential manager or a scoped helper.
- ✅ **Windows (Git-for-Windows)**: Same flow; recommend Git Credential Manager (Windows Credential Manager) rather than Unix-path scripts.
- ⚠️ **CI (GitHub Actions, etc.)**: Prefer short-lived auth (`GITHUB_TOKEN`, GitHub App tokens, or injected secrets). Avoid long-lived PAT files.
- ⚠️ **Containers**: Similar to CI; treat as ephemeral and inject secrets at runtime, not baked into images.

<!-- section_id: "f730e0b2-e0b8-4a9c-8818-1b6f8959e775" -->
## Problem Statement

When accessing repositories in organizations with SAML SSO enabled (like BYU-Idaho's `byui-math-dept`), Personal Access Tokens must be explicitly authorized for SSO before they can be used for Git operations.

<!-- section_id: "6bd25b15-9bc2-41c5-bd26-3ed27e2cf00f" -->
### Error Symptoms

```bash
remote: The 'byui-math-dept' organization has enabled or enforced SAML SSO.
remote: To access this repository, visit https://github.com/orgs/byui-math-dept/sso?authorization_request=...
fatal: unable to access 'https://github.com/...': The requested URL returned error: 403
```

<!-- section_id: "efe4f521-7742-4668-a795-f1d92ccec16a" -->
## Solution: Complete Setup Process

<!-- section_id: "619a9640-4211-4936-9d97-99960458b0b3" -->
### Step 1: Create Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token"
3. Set token details:
   - **Note**: Descriptive name (e.g., "Clone pac20026_fall2025 repo")
   - **Expiration**: Pick what your org/policy requires (some orgs allow “No expiration”; shorter expirations are safer)
   - **Scopes**: At minimum select `repo` for repository access
4. Click "Generate token"
5. **IMPORTANT**: Copy the token immediately (it won't be shown again)

<!-- section_id: "c2d535f5-79b7-4dab-8d71-ec6b85e72e6a" -->
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

<!-- section_id: "f1fa14fd-5b2a-4677-b7d1-e536a75b4d04" -->
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

<!-- section_id: "0f609250-b942-45f5-b91a-e596092556cc" -->
### Step 4: Configure Git Remote

Ensure remote URL is clean (no embedded token):

```bash
cd /path/to/repository
git remote set-url origin https://github.com/ORG/REPO.git
```

<!-- section_id: "841d5fc0-fc24-4298-a6bf-95f51fb2a9ba" -->
### Step 5: Verify Setup

Test that everything works:

```bash
git fetch
git status
```

Should complete without errors.

<!-- section_id: "6f78ddc3-f504-4ef9-b6c6-bcc560cb87ce" -->
## Common Issues and Solutions

<!-- section_id: "fe83f4c2-1f87-4cec-86b8-9005677df25d" -->
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

<!-- section_id: "2d65a408-cce6-4bc3-9a36-12320aaa0dcf" -->
### Issue: Token Not Authorized After Creation

**Symptom**: 403 errors persist even with new token

**Solution**: Creating a token ≠ Authorizing it for SSO. Must complete SSO authorization step separately.

<!-- section_id: "6ace4765-6446-48e4-93dd-75ac51b5e748" -->
### Issue: Need Multiple Tokens for Different Organizations

**Solution**: Each token can be authorized for multiple organizations. Alternatively, use multiple tokens and store them all in credentials file.

<!-- section_id: "feba3c13-a58c-4758-8b39-aac3a2fb99e5" -->
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

<!-- section_id: "56530f74-b11f-4a1a-9f1c-a71a9d61f989" -->
## Best Practices

<!-- section_id: "e2f2d522-5841-4ec3-85c8-042edd53a813" -->
### Token Management

- ✅ Create tokens with descriptive names
- ✅ Set appropriate expiration dates
- ✅ Use minimal required scopes
- ✅ Authorize for SSO immediately after creation
- ✅ Store tokens securely in `~/.git-credentials`
- ❌ Never embed tokens in remote URLs
- ❌ Never commit tokens to repositories

<!-- section_id: "790f45df-91a8-4012-905f-4bfabc3d6b9d" -->
### SSO Authorization

- ✅ Authorize token immediately after creation
- ✅ Verify authorization before using token
- ✅ Keep browser session open during setup
- ✅ Test with `git fetch` after authorization
- ❌ Don't assume token works without SSO auth
- ❌ Don't skip the "Configure SSO" step

<!-- section_id: "b555149d-5cf1-4c59-9018-262e2a8e0df7" -->
### Browser Sessions

- ✅ Use MCP browser tools for automation
- ✅ Keep browser open across sessions
- ✅ Maintain authenticated state
- ❌ Don't close browser prematurely
- ❌ Don't paste tokens into places that will be logged/snapshotted

<!-- section_id: "ce608b4d-3231-42c0-84cc-ffd79635dbfc" -->
## Organization-Specific Notes

<!-- section_id: "041ce91b-2b37-4222-8430-e1e5d00e6927" -->
### BYU-Idaho (byui-math-dept)

- **SSO Provider**: Church of Jesus Christ authentication
- **2FA**: Duo Security (push notifications)
- **Token Scopes Needed**: `repo` (minimum)
- **Typical Repositories**: Student course portfolios (e.g., `pac20026_fall2025`)

<!-- section_id: "90b24b34-96df-4ada-a531-59a8b6e96c7a" -->
### Authentication Flow

1. GitHub SSO page
2. Redirect to Church login (id.churchofjesuschrist.org)
3. Duo Security push notification
4. Redirect back to GitHub
5. Authorization complete

<!-- section_id: "90b4af41-8b0b-4623-b766-5887ac42d827" -->
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
