---
resource_id: "bbc855ae-ddb8-4d6a-9e54-81b6e6455e94"
resource_type: "document"
resource_name: "github_sso_token_setup"
---
# GitHub SSO Token Setup Guide

<!-- section_id: "1afee358-7011-46ca-b30b-4decb8adbbad" -->
## Overview

This guide documents the complete process for setting up GitHub Personal Access Tokens (PAT) with SAML SSO authorization for organizations that require Single Sign-On authentication.

<!-- section_id: "9e84b481-01de-486b-8874-7803d420b774" -->
## Compatibility (OS / Environment)

The **PAT + SSO authorization requirement is GitHub/org-side**, so the concept applies everywhere. What changes by OS/environment is **how you store credentials** and **how you complete the SSO web login**.

- ✅ **WSL (Ubuntu/Debian/etc.)**: Works well; browser-based SSO usually happens in your normal browser via WSLg, or via MCP Playwright/browser tooling.
- ✅ **Native Linux**: Same as WSL (store token via helper or OS keyring; authorize via browser).
- ✅ **macOS**: Same flow; recommend macOS Keychain-based credential manager or a scoped helper.
- ✅ **Windows (Git-for-Windows)**: Same flow; recommend Git Credential Manager (Windows Credential Manager) rather than Unix-path scripts.
- ⚠️ **CI (GitHub Actions, etc.)**: Prefer short-lived auth (`GITHUB_TOKEN`, GitHub App tokens, or injected secrets). Avoid long-lived PAT files.
- ⚠️ **Containers**: Similar to CI; treat as ephemeral and inject secrets at runtime, not baked into images.

<!-- section_id: "e97f9a91-7d2c-4b1d-964d-45a90de410cd" -->
## Problem Statement

When accessing repositories in organizations with SAML SSO enabled (like BYU-Idaho's `byui-math-dept`), Personal Access Tokens must be explicitly authorized for SSO before they can be used for Git operations.

<!-- section_id: "12d8852e-72ed-4d12-a427-8c7a13c8becf" -->
### Error Symptoms

```bash
remote: The 'byui-math-dept' organization has enabled or enforced SAML SSO.
remote: To access this repository, visit https://github.com/orgs/byui-math-dept/sso?authorization_request=...
fatal: unable to access 'https://github.com/...': The requested URL returned error: 403
```

<!-- section_id: "d030e259-f699-44f7-9cd1-f92ea9be09d6" -->
## Solution: Complete Setup Process

<!-- section_id: "11978b14-cfe2-439f-acdd-a8d3477d0b0c" -->
### Step 1: Create Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token"
3. Set token details:
   - **Note**: Descriptive name (e.g., "Clone pac20026_fall2025 repo")
   - **Expiration**: Pick what your org/policy requires (some orgs allow “No expiration”; shorter expirations are safer)
   - **Scopes**: At minimum select `repo` for repository access
4. Click "Generate token"
5. **IMPORTANT**: Copy the token immediately (it won't be shown again)

<!-- section_id: "80e3d565-eb85-451e-9af9-d7b51e8be397" -->
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

<!-- section_id: "9b7cf8eb-ee39-48c8-96fb-1adaa77eabdb" -->
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

<!-- section_id: "828caaa9-e00c-400a-8f23-8e42d2bb4212" -->
### Step 4: Configure Git Remote

Ensure remote URL is clean (no embedded token):

```bash
cd /path/to/repository
git remote set-url origin https://github.com/ORG/REPO.git
```

<!-- section_id: "13d15fa9-eb5d-4ee1-aec1-bd383c9744ee" -->
### Step 5: Verify Setup

Test that everything works:

```bash
git fetch
git status
```

Should complete without errors.

<!-- section_id: "8994e43a-65ff-4d26-abd1-5f40a446cbcc" -->
## Common Issues and Solutions

<!-- section_id: "857a2bcf-1142-4060-85f6-9a3bc53e2cfc" -->
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

<!-- section_id: "b5287700-445e-4a97-94f5-6ac7b65b4b67" -->
### Issue: Token Not Authorized After Creation

**Symptom**: 403 errors persist even with new token

**Solution**: Creating a token ≠ Authorizing it for SSO. Must complete SSO authorization step separately.

<!-- section_id: "668b583e-fd09-43e0-b567-29a6038e00ea" -->
### Issue: Need Multiple Tokens for Different Organizations

**Solution**: Each token can be authorized for multiple organizations. Alternatively, use multiple tokens and store them all in credentials file.

<!-- section_id: "2a009f1e-e8dc-49d2-b7f8-ee75648b277e" -->
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

<!-- section_id: "0fe9bed8-4a73-4d7c-bdeb-dafb7f412d79" -->
## Best Practices

<!-- section_id: "f4b10ee8-28e8-4e01-ba74-4908acb46369" -->
### Token Management

- ✅ Create tokens with descriptive names
- ✅ Set appropriate expiration dates
- ✅ Use minimal required scopes
- ✅ Authorize for SSO immediately after creation
- ✅ Store tokens securely in `~/.git-credentials`
- ❌ Never embed tokens in remote URLs
- ❌ Never commit tokens to repositories

<!-- section_id: "d756ccf1-4fee-421d-b187-38b8c83b6dbe" -->
### SSO Authorization

- ✅ Authorize token immediately after creation
- ✅ Verify authorization before using token
- ✅ Keep browser session open during setup
- ✅ Test with `git fetch` after authorization
- ❌ Don't assume token works without SSO auth
- ❌ Don't skip the "Configure SSO" step

<!-- section_id: "b8889787-f462-40ef-bc79-a7c4eaf38549" -->
### Browser Sessions

- ✅ Use MCP browser tools for automation
- ✅ Keep browser open across sessions
- ✅ Maintain authenticated state
- ❌ Don't close browser prematurely
- ❌ Don't paste tokens into places that will be logged/snapshotted

<!-- section_id: "23506764-0330-4900-9925-f8fbf78cbc1d" -->
## Organization-Specific Notes

<!-- section_id: "a928463c-d3b7-4356-a418-6575e535b14f" -->
### BYU-Idaho (byui-math-dept)

- **SSO Provider**: Church of Jesus Christ authentication
- **2FA**: Duo Security (push notifications)
- **Token Scopes Needed**: `repo` (minimum)
- **Typical Repositories**: Student course portfolios (e.g., `pac20026_fall2025`)

<!-- section_id: "12639ef2-a0f1-4eec-9af3-5cc21025ac8f" -->
### Authentication Flow

1. GitHub SSO page
2. Redirect to Church login (id.churchofjesuschrist.org)
3. Duo Security push notification
4. Redirect back to GitHub
5. Authorization complete

<!-- section_id: "075a583f-a0f9-41f4-8724-6301ce76498f" -->
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
