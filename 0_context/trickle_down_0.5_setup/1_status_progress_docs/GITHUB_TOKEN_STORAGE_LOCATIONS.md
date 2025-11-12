# GitHub Token Storage Locations

## Overview

This document tracks where GitHub Personal Access Tokens are stored for the pac20026_fall2025 repository and provides quick reference for future access.

## Primary Storage Location

### Git Credentials File (Secure Storage)

**Location**: `~/.git-credentials`  
**Full Path**: `/home/dawson/.git-credentials`

**Contents**:
```
https://dawson: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@github.com
```

**Security**:
- Permissions: `600` (read/write for owner only)
- Protected by file system permissions
- Used automatically by Git for authentication

**Configuration**:
```bash
git config --global credential.helper store
```

## Secondary Documentation Location

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

## GitHub Web Interface

**Token Management**: https://github.com/settings/tokens  
**Token ID**: 2803295200  
**Token Name**: "Clone pac20026_fall2025 repo"

### Token Details:
- **Scopes**: `repo` (full repository access)
- **Expires**: December 11, 2025
- **SSO Authorized**: ✅ byui-math-dept organization
- **Status**: Active and working

## Universal Documentation

**Complete Setup Guide**: 
```
/home/dawson/code/0_ai_context/0_context/trickle_down_0.5_setup/0_instruction_docs/github_sso_token_setup.md
```

Contains:
- Step-by-step token creation
- SSO authorization process
- Troubleshooting guide
- Browser automation examples
- BYU-Idaho specific notes

## Quick Reference Commands

### View Stored Token
```bash
cat ~/.git-credentials
```

### Check Token Permissions
```bash
ls -la ~/.git-credentials
```

### Test Repository Access
```bash
cd /home/dawson/code/pac20026_fall2025
git status
git pull
```

### View Git Configuration
```bash
git config --global credential.helper
```

## Repository Configuration

### pac20026_fall2025

- **Local Path**: `/home/dawson/code/pac20026_fall2025`
- **Remote URL**: `https://github.com/byui-math-dept/pac20026_fall2025.git`
- **Branch**: main
- **Organization**: byui-math-dept (SSO-protected)
- **Status**: ✅ Fully accessible

## Browser Session

**MCP Browser**: cursor-browser-extension  
**Status**: Open and authenticated  
**Location**: https://github.com/settings/tokens  
**Session**: Persistent across AI chat sessions

## Security Best Practices

### ✅ Do:
- Keep token in `~/.git-credentials` with 600 permissions
- Add token documentation to `.gitignore`
- Use `credential.helper = store` for automatic authentication
- Authorize token for SSO immediately after creation
- Document token expiration date

### ❌ Don't:
- Commit token to any repository
- Share token publicly
- Embed token in Git remote URLs
- Store token in unprotected files
- Forget to authorize for SSO

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

## Verification Checklist

✅ Token stored in `~/.git-credentials`  
✅ File permissions set to 600  
✅ Git configured to use credential store  
✅ Remote URL clean (no embedded token)  
✅ SSO authorized for organization  
✅ Repository access working (`git pull` successful)  
✅ Documentation file created and ignored  
✅ Browser session authenticated and persistent

## Status

- **Setup Date**: November 11, 2025
- **Last Verified**: November 11, 2025
- **Status**: ✅ Fully Operational
- **Git Operations**: All working (pull, push, fetch, clone)
- **Browser Session**: Authenticated and persistent

---

**Note**: This document is in the universal 0_ai_context directory so it can be referenced across all future AI sessions.

