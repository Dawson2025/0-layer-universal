---
resource_id: "27c72375-d6d8-4f31-81f6-3993873215ca"
resource_type: "document"
resource_name: "GITHUB_TOKEN_STORAGE_LOCATIONS"
---
# GitHub Token Storage Locations

<!-- section_id: "7ff9dc6f-f553-4778-8e1d-c56745df3dca" -->
## Overview

This document tracks where GitHub Personal Access Tokens are stored for the pac20026_fall2025 repository and provides quick reference for future access.

<!-- section_id: "b4e76334-1af7-4c1d-98f6-a5eff84e34ee" -->
## Primary Storage Location (Preferred)

<!-- section_id: "0895549b-28cf-4ee8-957b-bf0f048fec19" -->
### Org-scoped credential helper + local PAT file

**Goal**: Store a PAT for a single SSO-protected org (e.g., `byui-math-dept`) without using `~/.git-credentials` and without embedding tokens in remotes.

**Token file** (local only; never commit):
- `~/.config/git/pats/byui-math-dept.pat` (permissions: `chmod 600`)

**Credential helper** (local only):
- `~/.local/bin/git-credential-github-byui-math-dept`

**Critical git config** (enables org-scoped matching):
```bash
git config --global credential.useHttpPath true
```

<!-- section_id: "cf4331cd-ddc8-4edc-86e0-2337af913e79" -->
## Secondary Documentation Location

<!-- section_id: "9738f73b-45d0-406e-ae20-b19604cb788d" -->
### Repository Reference File

**Location**: `/home/dawson/code/pac20026_fall2025/GITHUB_TOKEN_INFO.md`

**Purpose**: 
- Human-readable reference
- Token details and expiration
- Setup instructions
- Troubleshooting guide

**Security**:
- Added to `.gitignore` to prevent accidental commits
- Local file only (never committed to repository)

<!-- section_id: "403cc603-ecb1-4538-9d2b-218597792d85" -->
## GitHub Web Interface (Token Management)

**Token Management**: https://github.com/settings/tokens  
**Token ID / Value**: Do not store token IDs or token values in committed docs.

<!-- section_id: "9fd7c30c-cf8e-4f1f-893b-1459c37f72bd" -->
### Token Details (example fields to track locally)
- **Scopes**: `repo` (minimum for private repo access)
- **Expires**: `<date>` or `No expiration` (per org policy)
- **SSO Authorized**: ✅ (must be explicitly authorized)
- **Status**: Active

<!-- section_id: "2d1e578b-ad33-415d-9811-d0fdf7f01752" -->
## Universal Documentation (Source of Truth)

**Complete Setup Guide**: 
```
/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_06_environment_setup/trickle_down_0.5_setup/0_instruction_docs/github/github_sso_token_setup.md
```

Contains:
- Step-by-step token creation
- SSO authorization process
- Troubleshooting guide
- Browser automation examples
- BYU-Idaho specific notes

<!-- section_id: "265a9b45-6182-40fa-ae5f-08651883924e" -->
## Quick Reference Commands

<!-- section_id: "b5d6d2a8-849f-4008-a50c-144b0b0ee225" -->
### Check Token File Permissions
```bash
ls -la ~/.config/git/pats/byui-math-dept.pat
```

<!-- section_id: "5d448b69-c8ac-4f67-8d42-00af5bfe6edd" -->
### Test Repository Access
```bash
cd /home/dawson/code/pac20026_fall2025
git status
git pull
```

<!-- section_id: "44339c36-6ebb-4e94-a7b5-a22ba239517a" -->
### View Git Configuration
```bash
git config --global --get-all credential.helper
git config --global credential.useHttpPath
```

<!-- section_id: "5a3d0908-c48b-4bde-9a2a-bf94415f08f2" -->
## Repository Configuration

<!-- section_id: "9bc114f0-096b-45bd-90cb-785878f02563" -->
### pac20026_fall2025

- **Local Path**: `/home/dawson/code/pac20026_fall2025`
- **Remote URL**: `https://github.com/byui-math-dept/pac20026_fall2025.git`
- **Branch**: main
- **Organization**: byui-math-dept (SSO-protected)
- **Status**: ✅ Fully accessible

<!-- section_id: "a0441676-2bfc-4fa8-bb2a-65fd77ec5dff" -->
## Browser Session

**MCP Browser**: cursor-browser-extension  
**Status**: Open and authenticated  
**Location**: https://github.com/settings/tokens  
**Session**: Persistent across AI chat sessions

<!-- section_id: "3453a581-0ba8-42f8-9197-e7f0ddaa3f74" -->
## Security Best Practices

<!-- section_id: "fa7c1c23-e502-4231-91a5-e46ea18bfbe7" -->
### ✅ Do:
- Keep token in a local file with `600` permissions (or an OS-native credential manager)
- Add token documentation to `.gitignore`
- Use an org-scoped helper (or OS-native credential manager) for automatic authentication
- Authorize token for SSO immediately after creation
- Document token expiration date

<!-- section_id: "a3b877bf-a442-4d4a-b918-b5cbc7b9b9c7" -->
### ❌ Don't:
- Commit token to any repository
- Share token publicly
- Embed token in Git remote URLs
- Store token in unprotected files
- Forget to authorize for SSO

<!-- section_id: "bdfdac3d-6121-4ed0-86e2-22749624583f" -->
## Token Renewal Process

When token expires (December 11, 2025):

1. Go to https://github.com/settings/tokens
2. Generate new token with same scopes
3. Configure SSO authorization for byui-math-dept
4. Update `~/.git-credentials` with new token:
   ```bash
   echo "https://dawson:NEW_TOKEN@github.com" > ~/.git-credentials
   chmod 600 ~/.git-credentials
   ```
5. Test with `git fetch`

<!-- section_id: "9a62bf90-6bb8-4e20-a912-2b285e2c532f" -->
## Verification Checklist

✅ Token stored in `~/.git-credentials`  
✅ File permissions set to 600  
✅ Git configured to use credential store  
✅ Remote URL clean (no embedded token)  
✅ SSO authorized for organization  
✅ Repository access working (`git pull` successful)  
✅ Documentation file created and ignored  
✅ Browser session authenticated and persistent

<!-- section_id: "17282c5d-d857-49d2-ae60-45fd8153c1ef" -->
## Status

- **Setup Date**: November 11, 2025
- **Last Verified**: November 11, 2025
- **Status**: ✅ Fully Operational
- **Git Operations**: All working (pull, push, fetch, clone)
- **Browser Session**: Authenticated and persistent

---

**Note**: This document is in the universal 0_ai_context directory so it can be referenced across all future AI sessions.
