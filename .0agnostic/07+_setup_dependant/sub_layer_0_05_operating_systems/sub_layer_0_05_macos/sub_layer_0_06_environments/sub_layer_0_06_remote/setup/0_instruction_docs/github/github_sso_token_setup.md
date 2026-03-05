---
resource_id: "f018ab2c-9804-4868-a7f9-e09e3eed57af"
resource_type: "document"
resource_name: "github_sso_token_setup"
---
# GitHub SSO Token Setup Guide

<!-- section_id: "a0382f91-e8b8-43a6-b0cd-a596797189d6" -->
## Overview

This guide documents the complete process for setting up GitHub Personal Access Tokens (PAT) with SAML SSO authorization for organizations that require Single Sign-On authentication.

<!-- section_id: "faf620b5-56e0-4567-aa7d-44ff1df90e62" -->
## Compatibility (OS / Environment)

The **PAT + SSO authorization requirement is GitHub/org-side**, so the concept applies everywhere. What changes by OS/environment is **how you store credentials** and **how you complete the SSO web login**.

- ✅ **WSL (Ubuntu/Debian/etc.)**: Works well; browser-based SSO usually happens in your normal browser via WSLg, or via MCP Playwright/browser tooling.
- ✅ **Native Linux**: Same as WSL (store token via helper or OS keyring; authorize via browser).
- ✅ **macOS**: Same flow; recommend macOS Keychain-based credential manager or a scoped helper.
- ✅ **Windows (Git-for-Windows)**: Same flow; recommend Git Credential Manager (Windows Credential Manager) rather than Unix-path scripts.
- ⚠️ **CI (GitHub Actions, etc.)**: Prefer short-lived auth (`GITHUB_TOKEN`, GitHub App tokens, or injected secrets). Avoid long-lived PAT files.
- ⚠️ **Containers**: Similar to CI; treat as ephemeral and inject secrets at runtime, not baked into images.

<!-- section_id: "3f21714f-4eed-48b7-891a-e4d100050dc8" -->
## Problem Statement

When accessing repositories in organizations with SAML SSO enabled (like BYU-Idaho's `byui-math-dept`), Personal Access Tokens must be explicitly authorized for SSO before they can be used for Git operations.

<!-- section_id: "38febd1c-626c-44fe-9b99-9c406a9c26bc" -->
### Error Symptoms

```bash
remote: The 'byui-math-dept' organization has enabled or enforced SAML SSO.
remote: To access this repository, visit https://github.com/orgs/byui-math-dept/sso?authorization_request=...
fatal: unable to access 'https://github.com/...': The requested URL returned error: 403
```

<!-- section_id: "8db2a461-2f2b-493e-8cf2-7caf1304af10" -->
## Solution: Complete Setup Process

<!-- section_id: "5266655f-1746-4214-a283-799e6f0d2370" -->
### Step 1: Create Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token"
3. Set token details:
   - **Note**: Descriptive name (e.g., "Clone pac20026_fall2025 repo")
   - **Expiration**: Pick what your org/policy requires (some orgs allow “No expiration”; shorter expirations are safer)
   - **Scopes**: At minimum select `repo` for repository access
4. Click "Generate token"
5. **IMPORTANT**: Copy the token immediately (it won't be shown again)

<!-- section_id: "a77a0b36-1e0e-4ef9-91b3-f31910b5916e" -->
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

<!-- section_id: "eb94efb8-1461-4473-ab96-44e92328fa34" -->
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

<!-- section_id: "ffe13e99-77ca-4fc7-8d1b-8357cd92cb0b" -->
### Step 4: Configure Git Remote

Ensure remote URL is clean (no embedded token):

```bash
cd /path/to/repository
git remote set-url origin https://github.com/ORG/REPO.git
```

<!-- section_id: "0fd095b7-60db-42bb-93e7-de946980f36c" -->
### Step 5: Verify Setup

Test that everything works:

```bash
git fetch
git status
```

Should complete without errors.

<!-- section_id: "856260e8-b5a7-4158-9f3a-b954defe6ac5" -->
## Common Issues and Solutions

<!-- section_id: "3c5d41c9-57d2-47c5-ba84-939e93b920bd" -->
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

<!-- section_id: "c1b13fc0-2f16-4bb5-ada3-54809d85f308" -->
### Issue: Token Not Authorized After Creation

**Symptom**: 403 errors persist even with new token

**Solution**: Creating a token ≠ Authorizing it for SSO. Must complete SSO authorization step separately.

<!-- section_id: "079c26b4-dc5d-4e8f-8f35-9343eaa88a53" -->
### Issue: Need Multiple Tokens for Different Organizations

**Solution**: Each token can be authorized for multiple organizations. Alternatively, use multiple tokens and store them all in credentials file.

<!-- section_id: "c2227a93-bb72-4414-b03e-051f1f215dba" -->
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

<!-- section_id: "271e8b1d-963a-43df-9e4b-492821c68357" -->
## Best Practices

<!-- section_id: "114cf01d-188c-49a4-9688-ce6e28afbb1c" -->
### Token Management

- ✅ Create tokens with descriptive names
- ✅ Set appropriate expiration dates
- ✅ Use minimal required scopes
- ✅ Authorize for SSO immediately after creation
- ✅ Store tokens securely in `~/.git-credentials`
- ❌ Never embed tokens in remote URLs
- ❌ Never commit tokens to repositories

<!-- section_id: "f2d14296-ed47-4b70-89fd-0948683e2dd9" -->
### SSO Authorization

- ✅ Authorize token immediately after creation
- ✅ Verify authorization before using token
- ✅ Keep browser session open during setup
- ✅ Test with `git fetch` after authorization
- ❌ Don't assume token works without SSO auth
- ❌ Don't skip the "Configure SSO" step

<!-- section_id: "bb92ad72-0f2e-4617-82e5-09a78f582a9a" -->
### Browser Sessions

- ✅ Use MCP browser tools for automation
- ✅ Keep browser open across sessions
- ✅ Maintain authenticated state
- ❌ Don't close browser prematurely
- ❌ Don't paste tokens into places that will be logged/snapshotted

<!-- section_id: "735563b0-4240-4a97-84c6-d08fb397d909" -->
## Organization-Specific Notes

<!-- section_id: "a9a4e617-5e94-4c76-92ab-c51336d8a333" -->
### BYU-Idaho (byui-math-dept)

- **SSO Provider**: Church of Jesus Christ authentication
- **2FA**: Duo Security (push notifications)
- **Token Scopes Needed**: `repo` (minimum)
- **Typical Repositories**: Student course portfolios (e.g., `pac20026_fall2025`)

<!-- section_id: "e68d76a7-cc49-4382-b6b1-5d1c8118a321" -->
### Authentication Flow

1. GitHub SSO page
2. Redirect to Church login (id.churchofjesuschrist.org)
3. Duo Security push notification
4. Redirect back to GitHub
5. Authorization complete

<!-- section_id: "183ec6a8-34d5-49b8-a214-73b22302cc74" -->
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
