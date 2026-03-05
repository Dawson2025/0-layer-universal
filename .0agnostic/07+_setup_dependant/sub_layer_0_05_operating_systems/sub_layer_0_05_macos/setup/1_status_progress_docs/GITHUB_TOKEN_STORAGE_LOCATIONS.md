---
resource_id: "19a882e5-8b40-491d-a7ba-0f630d57ae4f"
resource_type: "document"
resource_name: "GITHUB_TOKEN_STORAGE_LOCATIONS"
---
# GitHub Token Storage Locations

<!-- section_id: "f147687f-6036-43fc-9382-41d582ff12cf" -->
## Overview

This document tracks where GitHub Personal Access Tokens are stored for the pac20026_fall2025 repository and provides quick reference for future access.

<!-- section_id: "7b5f9a5c-c3c2-4ad2-b5c5-881935e278ca" -->
## Primary Storage Location (Preferred)

<!-- section_id: "30cd5c02-ccab-4c23-ab94-1087a5eb7a36" -->
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

<!-- section_id: "c168f2d8-836a-463b-b3a3-76457aebe96a" -->
## Secondary Documentation Location

<!-- section_id: "64838756-1740-4448-9e91-9fd4491064ab" -->
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

<!-- section_id: "103c7991-a305-4c95-ac0f-688727f642bf" -->
## GitHub Web Interface (Token Management)

**Token Management**: https://github.com/settings/tokens  
**Token ID / Value**: Do not store token IDs or token values in committed docs.

<!-- section_id: "0cd16333-b6d2-4a0f-a5e0-7ed75167e3d9" -->
### Token Details (example fields to track locally)
- **Scopes**: `repo` (minimum for private repo access)
- **Expires**: `<date>` or `No expiration` (per org policy)
- **SSO Authorized**: ✅ (must be explicitly authorized)
- **Status**: Active

<!-- section_id: "d2d12ec7-858a-4018-8188-0492a790b4d9" -->
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

<!-- section_id: "0806929d-90a3-468e-903b-cfadaa2bc827" -->
## Quick Reference Commands

<!-- section_id: "b8661a8f-7906-442a-af93-654e68ce185a" -->
### Check Token File Permissions
```bash
ls -la ~/.config/git/pats/byui-math-dept.pat
```

<!-- section_id: "3a46a116-ffe0-4e76-8f69-a857d1203ca8" -->
### Test Repository Access
```bash
cd /home/dawson/code/pac20026_fall2025
git status
git pull
```

<!-- section_id: "e72c45c3-83c6-453d-bfd6-859b2591d510" -->
### View Git Configuration
```bash
git config --global --get-all credential.helper
git config --global credential.useHttpPath
```

<!-- section_id: "6c6fd380-ed98-4f43-800e-190f7df26bed" -->
## Repository Configuration

<!-- section_id: "2e29474a-ddb1-4f8e-b7a7-9aa07246f658" -->
### pac20026_fall2025

- **Local Path**: `/home/dawson/code/pac20026_fall2025`
- **Remote URL**: `https://github.com/byui-math-dept/pac20026_fall2025.git`
- **Branch**: main
- **Organization**: byui-math-dept (SSO-protected)
- **Status**: ✅ Fully accessible

<!-- section_id: "3ff75b76-68f8-4896-9436-5cf89673f965" -->
## Browser Session

**MCP Browser**: cursor-browser-extension  
**Status**: Open and authenticated  
**Location**: https://github.com/settings/tokens  
**Session**: Persistent across AI chat sessions

<!-- section_id: "a601a083-bd0e-477a-9526-91c9deded591" -->
## Security Best Practices

<!-- section_id: "66e26f02-622e-41cf-abfb-84ce583dcb6a" -->
### ✅ Do:
- Keep token in a local file with `600` permissions (or an OS-native credential manager)
- Add token documentation to `.gitignore`
- Use an org-scoped helper (or OS-native credential manager) for automatic authentication
- Authorize token for SSO immediately after creation
- Document token expiration date

<!-- section_id: "f3b7c38f-31cd-4097-93f8-c1b69ad2e087" -->
### ❌ Don't:
- Commit token to any repository
- Share token publicly
- Embed token in Git remote URLs
- Store token in unprotected files
- Forget to authorize for SSO

<!-- section_id: "d03697cc-362d-4ef7-ba61-0fdec275912d" -->
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

<!-- section_id: "b1dc94e5-e16c-452c-8367-afc555865af3" -->
## Verification Checklist

✅ Token stored in `~/.git-credentials`  
✅ File permissions set to 600  
✅ Git configured to use credential store  
✅ Remote URL clean (no embedded token)  
✅ SSO authorized for organization  
✅ Repository access working (`git pull` successful)  
✅ Documentation file created and ignored  
✅ Browser session authenticated and persistent

<!-- section_id: "b50b9c1b-8b4d-486e-a4a9-40354fc3d26f" -->
## Status

- **Setup Date**: November 11, 2025
- **Last Verified**: November 11, 2025
- **Status**: ✅ Fully Operational
- **Git Operations**: All working (pull, push, fetch, clone)
- **Browser Session**: Authenticated and persistent

---

**Note**: This document is in the universal 0_ai_context directory so it can be referenced across all future AI sessions.
