---
resource_id: "8a76e99e-88fc-4aca-8ff2-07f852b5f501"
resource_type: "document"
resource_name: "GITHUB_TOKEN_STORAGE_LOCATIONS"
---
# GitHub Token Storage Locations

<!-- section_id: "1393f8c8-98d1-43a5-a8a2-591478cbae00" -->
## Overview

This document tracks where GitHub Personal Access Tokens are stored for the pac20026_fall2025 repository and provides quick reference for future access.

<!-- section_id: "c13b1b74-570a-49e6-b901-4c473f3e8069" -->
## Primary Storage Location (Preferred)

<!-- section_id: "7d4d156b-05b6-481f-a616-3388bcf354d1" -->
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

<!-- section_id: "3470cf5a-061f-448a-9777-7a2fa692b288" -->
## Secondary Documentation Location

<!-- section_id: "1a04667c-b77f-4b41-8c3c-5522cdf3e8fa" -->
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

<!-- section_id: "6a84cb6b-6c40-4123-8814-86f283007795" -->
## GitHub Web Interface (Token Management)

**Token Management**: https://github.com/settings/tokens  
**Token ID / Value**: Do not store token IDs or token values in committed docs.

<!-- section_id: "5fecd3b2-c3b5-45ba-ab6f-0e8964ad6546" -->
### Token Details (example fields to track locally)
- **Scopes**: `repo` (minimum for private repo access)
- **Expires**: `<date>` or `No expiration` (per org policy)
- **SSO Authorized**: ✅ (must be explicitly authorized)
- **Status**: Active

<!-- section_id: "5e41dd01-e0a2-4345-ab07-f9ebe2fa4028" -->
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

<!-- section_id: "87711f06-299c-43d0-948e-822396f74aeb" -->
## Quick Reference Commands

<!-- section_id: "5fe2f8b9-4067-4edb-baf9-74cd118da01f" -->
### Check Token File Permissions
```bash
ls -la ~/.config/git/pats/byui-math-dept.pat
```

<!-- section_id: "84c25f6e-9c42-4c42-a1c7-141d0bd0b558" -->
### Test Repository Access
```bash
cd /home/dawson/code/pac20026_fall2025
git status
git pull
```

<!-- section_id: "c5168372-0537-4480-a79d-ec114315bf72" -->
### View Git Configuration
```bash
git config --global --get-all credential.helper
git config --global credential.useHttpPath
```

<!-- section_id: "df035172-9d95-4c09-979c-e23aec57f56b" -->
## Repository Configuration

<!-- section_id: "9e9ad84b-0a30-4d9d-8d68-b8fe9a983a42" -->
### pac20026_fall2025

- **Local Path**: `/home/dawson/code/pac20026_fall2025`
- **Remote URL**: `https://github.com/byui-math-dept/pac20026_fall2025.git`
- **Branch**: main
- **Organization**: byui-math-dept (SSO-protected)
- **Status**: ✅ Fully accessible

<!-- section_id: "a2f5c427-967c-44b5-97b2-c065154e94d5" -->
## Browser Session

**MCP Browser**: cursor-browser-extension  
**Status**: Open and authenticated  
**Location**: https://github.com/settings/tokens  
**Session**: Persistent across AI chat sessions

<!-- section_id: "9b26b588-9ef2-4c6d-b422-ce0c19501240" -->
## Security Best Practices

<!-- section_id: "01d6f097-be94-47c0-a8ce-fe601f52d4b0" -->
### ✅ Do:
- Keep token in a local file with `600` permissions (or an OS-native credential manager)
- Add token documentation to `.gitignore`
- Use an org-scoped helper (or OS-native credential manager) for automatic authentication
- Authorize token for SSO immediately after creation
- Document token expiration date

<!-- section_id: "2f0f1452-0cba-435e-82e3-af165b8728c3" -->
### ❌ Don't:
- Commit token to any repository
- Share token publicly
- Embed token in Git remote URLs
- Store token in unprotected files
- Forget to authorize for SSO

<!-- section_id: "ff9782d4-e384-4a68-bb10-8be2f4ed9984" -->
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

<!-- section_id: "14595752-c683-478f-a531-59eff3e6652f" -->
## Verification Checklist

✅ Token stored in `~/.git-credentials`  
✅ File permissions set to 600  
✅ Git configured to use credential store  
✅ Remote URL clean (no embedded token)  
✅ SSO authorized for organization  
✅ Repository access working (`git pull` successful)  
✅ Documentation file created and ignored  
✅ Browser session authenticated and persistent

<!-- section_id: "80780d09-b70d-4509-979e-84eabda136e9" -->
## Status

- **Setup Date**: November 11, 2025
- **Last Verified**: November 11, 2025
- **Status**: ✅ Fully Operational
- **Git Operations**: All working (pull, push, fetch, clone)
- **Browser Session**: Authenticated and persistent

---

**Note**: This document is in the universal 0_ai_context directory so it can be referenced across all future AI sessions.
