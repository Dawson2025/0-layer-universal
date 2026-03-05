---
resource_id: "0e83aa33-c218-4db2-b824-b7c563b65773"
resource_type: "document"
resource_name: "UPDATE"
---
# Codex CLI - Update Instructions

**Last Updated:** 2025-01-26  
**Current Version:** 0.80.0

<!-- section_id: "e51a2459-5e7f-4467-9ab9-f621854d398d" -->
## Overview

This document describes how to update Codex CLI to the latest version. Codex CLI is distributed via npm and can be updated using standard npm commands.

<!-- section_id: "c50bda21-ecde-4574-80f2-9bb6e03630ec" -->
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

<!-- section_id: "403ac12e-c7bd-43d2-ae5e-f84ba3be7f9d" -->
## Update Method

<!-- section_id: "c6d93be6-40c9-42f8-b896-acca9ccd7ce2" -->
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

<!-- section_id: "c8e37164-b606-4240-a3d4-be6f302484b7" -->
### Alternative: npm update

You can also use the `npm update` command:

```bash
npm update -g @openai/codex
```

**Note:** `npm update` may not always install the latest version if your current version satisfies the semver range. Using `npm install -g @openai/codex@latest` ensures you get the absolute latest version.

<!-- section_id: "a0131f85-84b1-4e21-8354-279cf58a8f25" -->
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

<!-- section_id: "cc2f6953-726d-4b6d-9004-73ae65b8481c" -->
## Troubleshooting

<!-- section_id: "0e45e7e8-3af5-4b7b-aa37-6f05d3f88efc" -->
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

<!-- section_id: "c0976ad9-c949-4e00-8635-04ceede791c7" -->
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

<!-- section_id: "e102e45d-657e-4e15-a449-4914817583f4" -->
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

<!-- section_id: "82d0b161-c4f5-40a8-9a52-b7e98b3408f0" -->
## Update History

<!-- section_id: "8bb9591e-4f98-4089-975f-09b3044cfff3" -->
### 2025-01-26: Updated to v0.80.0
- **Previous version:** 0.79.0
- **Method used:** `npm install -g @openai/codex@latest`
- **Notes:** 
  - Update completed successfully
  - No configuration changes required
  - All functionality verified after update

<!-- section_id: "f393fd42-3269-4dfc-a8db-12b9ff9c271a" -->
## Platform Support

- ✅ **macOS**: Fully supported
- ✅ **Linux**: Fully supported
- ⚠️ **Windows**: Experimental (recommended to use WSL)

<!-- section_id: "09a33b3d-dd61-462e-b5b1-e7c7f6edd1ac" -->
## References

- **Official Documentation:** https://developers.openai.com/codex/cli
- **npm Package:** https://www.npmjs.com/package/@openai/codex

<!-- section_id: "9ddd5484-d30c-4a87-b019-1c05e20ff611" -->
## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **AI Apps Setup:** `../../sub_layer_0_09_ai_apps_tools_setup/` (universal context)
