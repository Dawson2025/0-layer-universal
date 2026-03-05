---
resource_id: "128aad3a-d241-4d13-b938-6b138b54bd98"
resource_type: "document"
resource_name: "UPDATE"
---
# Codex CLI - Update Instructions

**Last Updated:** 2025-01-26  
**Current Version:** 0.80.0

<!-- section_id: "85fa3254-4826-476d-8ef5-1e472efd249b" -->
## Overview

This document describes how to update Codex CLI to the latest version. Codex CLI is distributed via npm and can be updated using standard npm commands.

<!-- section_id: "5e429960-710d-4553-b1d4-e6a6edebe585" -->
## Checking Current Version

Before updating, check your current version:

```bash
codex --version
```

**Example output:**
```
codex-cli 0.80.0
```

You can also check the npm package version:

```bash
npm list -g @openai/codex
```

**Example output:**
```
/home/dawson/.nvm/versions/node/v22.21.1/lib
└── @openai/codex@0.80.0
```

<!-- section_id: "2878a0b0-426e-4b1f-94aa-6c8cf203cdea" -->
## Update Method

<!-- section_id: "c24e1cfa-0a03-4624-81b2-e39def3b1748" -->
### npm Update (Standard Method)

Codex CLI is managed through npm. To update to the latest version:

```bash
npm install -g @openai/codex@latest
```

**What this does:**
- Downloads and installs the latest version of `@openai/codex`
- Replaces the previous global installation
- Updates the `codex` command to the new version

**Example output:**
```
changed 1 package in 8s
```

<!-- section_id: "27236283-909d-4beb-96ac-76b300ec08cf" -->
### Alternative: npm update

You can also use the `npm update` command:

```bash
npm update -g @openai/codex
```

**Note:** `npm update` may not always install the latest version if your current version satisfies the semver range. Using `npm install -g @openai/codex@latest` ensures you get the absolute latest version.

<!-- section_id: "35fe6d43-40e4-4b80-9d87-213fba7f7b61" -->
## Verification After Update

After updating, verify the installation:

```bash
# Check version
codex --version

# Check installation location
which codex

# Check npm package version
npm list -g @openai/codex

# Test basic functionality
codex --help
```

<!-- section_id: "ce5c3448-d2e5-4ed3-ab43-9cae3e614ac1" -->
## Troubleshooting

<!-- section_id: "af84a1c7-d331-43cd-9180-4c77ee1046ca" -->
### Issue: "Command not found" after update

**Solution:**
1. Check if the binary is in your PATH:
   ```bash
   which codex
   echo $PATH
   ```

2. If using nvm, ensure nvm is loaded:
   ```bash
   source ~/.nvm/nvm.sh
   # Or add to ~/.bashrc or ~/.zshrc
   ```

3. Verify npm global bin directory is in PATH:
   ```bash
   npm config get prefix
   # Add that path/bin to your PATH if not already there
   ```

<!-- section_id: "71f43058-7598-4119-b5d1-13e1db4e16ab" -->
### Issue: Permission errors during update

**Solution:**
1. **Recommended:** Use nvm to manage Node.js and npm (avoids permission issues)
   ```bash
   # Install nvm if not already installed
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
   
   # Use nvm to install Node.js
   nvm install node
   nvm use node
   ```

2. **Alternative:** Configure npm to use a different directory (not recommended):
   ```bash
   mkdir ~/.npm-global
   npm config set prefix '~/.npm-global'
   export PATH=~/.npm-global/bin:$PATH
   # Add to ~/.bashrc or ~/.zshrc
   ```

3. **Not recommended:** Using `sudo` can cause permission issues and is not recommended

<!-- section_id: "f1fd5e42-58ec-4fe8-97a5-ef2cdb5af80e" -->
### Issue: Version not updating

**Solution:**
1. Force reinstall:
   ```bash
   npm install -g @openai/codex@latest --force
   ```

2. Clear npm cache and reinstall:
   ```bash
   npm cache clean --force
   npm install -g @openai/codex@latest
   ```

3. Verify you're using the correct Node.js version:
   ```bash
   node --version
   npm --version
   ```

<!-- section_id: "a6fcb0bf-3f14-4fd3-a472-9fd17a0ed620" -->
## Update History

<!-- section_id: "fb5a5fd8-64e0-4395-a37d-a2c3e8542307" -->
### 2025-01-26: Updated to v0.80.0
- **Previous version:** 0.79.0
- **Method used:** `npm install -g @openai/codex@latest`
- **Notes:** 
  - Update completed successfully
  - No configuration changes required
  - All functionality verified after update

<!-- section_id: "fb9478a8-d0f2-413b-9bfc-ecaea079de68" -->
## Platform Support

- ✅ **macOS**: Fully supported
- ✅ **Linux**: Fully supported
- ⚠️ **Windows**: Experimental (recommended to use WSL)

<!-- section_id: "aa6b7559-9ff5-41e9-bd73-e832c0e8739d" -->
## References

- **Official Documentation:** https://developers.openai.com/codex/cli
- **npm Package:** https://www.npmjs.com/package/@openai/codex

<!-- section_id: "c23d150d-dc88-4a99-a3c2-3d4ac4aa880d" -->
## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **AI Apps Setup:** `../../sub_layer_0_09_ai_apps_tools_setup/` (universal context)
