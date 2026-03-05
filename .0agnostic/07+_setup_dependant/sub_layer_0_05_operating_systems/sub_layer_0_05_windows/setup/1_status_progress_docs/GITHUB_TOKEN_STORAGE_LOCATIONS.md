---
resource_id: "1ffa7aea-a7bb-4523-b1a6-923f784d4240"
resource_type: "document"
resource_name: "GITHUB_TOKEN_STORAGE_LOCATIONS"
---
# GitHub Token Storage Locations

<!-- section_id: "2ab348a2-c82b-496f-a2a8-7924a10f32a5" -->
## Overview

This document tracks where GitHub Personal Access Tokens are stored for the pac20026_fall2025 repository and provides quick reference for future access.

<!-- section_id: "97f8b427-45e1-4aca-8fe9-64c79c5b2dd2" -->
## Primary Storage Location (Preferred)

<!-- section_id: "ad1a5ff2-e642-45b8-92c3-7d4e0d93d39b" -->
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

<!-- section_id: "26e34c7c-011c-48b1-ac2d-4e32b9f491c5" -->
## Secondary Documentation Location

<!-- section_id: "92998f53-25f6-4bdd-9fcb-f99d7cb47863" -->
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

<!-- section_id: "ca622530-f47e-42f0-a251-e7098cef803b" -->
## GitHub Web Interface (Token Management)

**Token Management**: https://github.com/settings/tokens  
**Token ID / Value**: Do not store token IDs or token values in committed docs.

<!-- section_id: "974bfb4b-3fff-403a-847c-93d5fa0ec8ac" -->
### Token Details (example fields to track locally)
- **Scopes**: `repo` (minimum for private repo access)
- **Expires**: `<date>` or `No expiration` (per org policy)
- **SSO Authorized**: ✅ (must be explicitly authorized)
- **Status**: Active

<!-- section_id: "f0d3e682-bee0-49d0-aec3-9081bddd30d4" -->
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

<!-- section_id: "69a6e16b-bec9-4179-a03e-540cf3a0a564" -->
## Quick Reference Commands

<!-- section_id: "efc4d7cd-9f56-4683-b57c-2fa7564a8156" -->
### Check Token File Permissions
```bash
ls -la ~/.config/git/pats/byui-math-dept.pat
```

<!-- section_id: "b8d5dbcf-1812-4008-b16f-8b17a6b7061e" -->
### Test Repository Access
```bash
cd /home/dawson/code/pac20026_fall2025
git status
git pull
```

<!-- section_id: "3babf666-b534-459b-ac2f-2f6e1c672f2c" -->
### View Git Configuration
```bash
git config --global --get-all credential.helper
git config --global credential.useHttpPath
```

<!-- section_id: "a16b3a9e-5b98-43bc-a565-0fc7f44e119c" -->
## Repository Configuration

<!-- section_id: "d0854497-407e-4ddd-8c42-b5c516269585" -->
### pac20026_fall2025

- **Local Path**: `/home/dawson/code/pac20026_fall2025`
- **Remote URL**: `https://github.com/byui-math-dept/pac20026_fall2025.git`
- **Branch**: main
- **Organization**: byui-math-dept (SSO-protected)
- **Status**: ✅ Fully accessible

<!-- section_id: "df82811d-755e-46cc-9254-01913def7bb1" -->
## Browser Session

**MCP Browser**: cursor-browser-extension  
**Status**: Open and authenticated  
**Location**: https://github.com/settings/tokens  
**Session**: Persistent across AI chat sessions

<!-- section_id: "4ff7709a-2da5-481b-8843-8cdd1f948e3f" -->
## Security Best Practices

<!-- section_id: "0d1cddff-4920-4c23-a2fc-c9ea5fb7dd2e" -->
### ✅ Do:
- Keep token in a local file with `600` permissions (or an OS-native credential manager)
- Add token documentation to `.gitignore`
- Use an org-scoped helper (or OS-native credential manager) for automatic authentication
- Authorize token for SSO immediately after creation
- Document token expiration date

<!-- section_id: "b2364a77-91da-40c7-963c-d80297fe2021" -->
### ❌ Don't:
- Commit token to any repository
- Share token publicly
- Embed token in Git remote URLs
- Store token in unprotected files
- Forget to authorize for SSO

<!-- section_id: "ac00c9f6-2775-4692-89d8-7b942fc3347d" -->
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

<!-- section_id: "f0694d6f-b8fb-4847-a9dc-33a472142715" -->
## Verification Checklist

✅ Token stored in `~/.git-credentials`  
✅ File permissions set to 600  
✅ Git configured to use credential store  
✅ Remote URL clean (no embedded token)  
✅ SSO authorized for organization  
✅ Repository access working (`git pull` successful)  
✅ Documentation file created and ignored  
✅ Browser session authenticated and persistent

<!-- section_id: "4074a218-4f0e-4569-9b55-e6232eae3901" -->
## Status

- **Setup Date**: November 11, 2025
- **Last Verified**: November 11, 2025
- **Status**: ✅ Fully Operational
- **Git Operations**: All working (pull, push, fetch, clone)
- **Browser Session**: Authenticated and persistent

---

**Note**: This document is in the universal 0_ai_context directory so it can be referenced across all future AI sessions.
