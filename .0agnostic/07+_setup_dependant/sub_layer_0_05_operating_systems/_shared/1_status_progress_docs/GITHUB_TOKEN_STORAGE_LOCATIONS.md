---
resource_id: "930b39aa-6eca-4af0-98aa-84369b9a989e"
resource_type: "document"
resource_name: "GITHUB_TOKEN_STORAGE_LOCATIONS"
---
# GitHub Token Storage Locations

<!-- section_id: "95bbfce9-be1a-46e4-b61a-ae7a42902a44" -->
## Overview

This document tracks where GitHub Personal Access Tokens are stored for the pac20026_fall2025 repository and provides quick reference for future access.

<!-- section_id: "204e2f1a-fe72-46ba-9d0f-177670c8199a" -->
## Primary Storage Location (Preferred)

<!-- section_id: "c83ef62b-cd40-4b9e-8acf-819e78d61eab" -->
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

<!-- section_id: "52478c40-4190-40e8-8bae-cffa225d23b5" -->
## Secondary Documentation Location

<!-- section_id: "9e9bba04-88f0-42e6-ab1c-2b1e7ee3ac3d" -->
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

<!-- section_id: "94961c16-078d-4e7b-af6c-d1b1609b43d8" -->
## GitHub Web Interface (Token Management)

**Token Management**: https://github.com/settings/tokens  
**Token ID / Value**: Do not store token IDs or token values in committed docs.

<!-- section_id: "02698b85-84ec-453f-b193-8e660c21bedc" -->
### Token Details (example fields to track locally)
- **Scopes**: `repo` (minimum for private repo access)
- **Expires**: `<date>` or `No expiration` (per org policy)
- **SSO Authorized**: ✅ (must be explicitly authorized)
- **Status**: Active

<!-- section_id: "62882787-1f39-4ab2-93dd-ea607284b06d" -->
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

<!-- section_id: "594c6618-3afa-4e45-b18f-30f7dd68ef5c" -->
## Quick Reference Commands

<!-- section_id: "612f9ebb-4d65-46e5-ba68-937c3c603cf3" -->
### Check Token File Permissions
```bash
ls -la ~/.config/git/pats/byui-math-dept.pat
```

<!-- section_id: "2bf15530-64d2-43c0-9ca9-56791d5f93ee" -->
### Test Repository Access
```bash
cd /home/dawson/code/pac20026_fall2025
git status
git pull
```

<!-- section_id: "37bcd679-ebbc-4032-8b36-deaab794cd63" -->
### View Git Configuration
```bash
git config --global --get-all credential.helper
git config --global credential.useHttpPath
```

<!-- section_id: "30e4de37-6fe7-43bc-862c-09efd359c70b" -->
## Repository Configuration

<!-- section_id: "c95b00d5-0119-4f93-84e8-a8aa2f5e2880" -->
### pac20026_fall2025

- **Local Path**: `/home/dawson/code/pac20026_fall2025`
- **Remote URL**: `https://github.com/byui-math-dept/pac20026_fall2025.git`
- **Branch**: main
- **Organization**: byui-math-dept (SSO-protected)
- **Status**: ✅ Fully accessible

<!-- section_id: "0f26f6cf-8fa4-4e97-b33b-c95f06e1f10b" -->
## Browser Session

**MCP Browser**: cursor-browser-extension  
**Status**: Open and authenticated  
**Location**: https://github.com/settings/tokens  
**Session**: Persistent across AI chat sessions

<!-- section_id: "9eeb76b5-6e39-4cff-8db8-ece4d53274c4" -->
## Security Best Practices

<!-- section_id: "3cf7665c-3482-4911-9568-771e985edb12" -->
### ✅ Do:
- Keep token in a local file with `600` permissions (or an OS-native credential manager)
- Add token documentation to `.gitignore`
- Use an org-scoped helper (or OS-native credential manager) for automatic authentication
- Authorize token for SSO immediately after creation
- Document token expiration date

<!-- section_id: "5435e6bd-9445-45f1-a936-100295f99829" -->
### ❌ Don't:
- Commit token to any repository
- Share token publicly
- Embed token in Git remote URLs
- Store token in unprotected files
- Forget to authorize for SSO

<!-- section_id: "b81e4f01-b27f-4f71-9a29-9bef7dea11b2" -->
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

<!-- section_id: "9070a34d-c1cb-4430-a1b7-a0243a486eb5" -->
## Verification Checklist

✅ Token stored in `~/.git-credentials`  
✅ File permissions set to 600  
✅ Git configured to use credential store  
✅ Remote URL clean (no embedded token)  
✅ SSO authorized for organization  
✅ Repository access working (`git pull` successful)  
✅ Documentation file created and ignored  
✅ Browser session authenticated and persistent

<!-- section_id: "39f0cb74-d68a-43c9-90be-6e4520ffaee7" -->
## Status

- **Setup Date**: November 11, 2025
- **Last Verified**: November 11, 2025
- **Status**: ✅ Fully Operational
- **Git Operations**: All working (pull, push, fetch, clone)
- **Browser Session**: Authenticated and persistent

---

**Note**: This document is in the universal 0_ai_context directory so it can be referenced across all future AI sessions.
