---
resource_id: "4eaf8b0c-8080-45e8-a5b4-2fdbe5259b98"
resource_type: "document"
resource_name: "UPDATE"
---
# Codex CLI - Update Instructions

**Last Updated:** 2025-01-26  
**Current Version:** 0.80.0

## Overview

This document describes how to update Codex CLI to the latest version. Codex CLI is distributed via npm and can be updated using standard npm commands.

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

## Update Method

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

### Alternative: npm update

You can also use the `npm update` command:

```bash
npm update -g @openai/codex
```

**Note:** `npm update` may not always install the latest version if your current version satisfies the semver range. Using `npm install -g @openai/codex@latest` ensures you get the absolute latest version.

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

## Troubleshooting

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

## Update History

### 2025-01-26: Updated to v0.80.0
- **Previous version:** 0.79.0
- **Method used:** `npm install -g @openai/codex@latest`
- **Notes:** 
  - Update completed successfully
  - No configuration changes required
  - All functionality verified after update

## Platform Support

- ✅ **macOS**: Fully supported
- ✅ **Linux**: Fully supported
- ⚠️ **Windows**: Experimental (recommended to use WSL)

## References

- **Official Documentation:** https://developers.openai.com/codex/cli
- **npm Package:** https://www.npmjs.com/package/@openai/codex

## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **AI Apps Setup:** `../../sub_layer_0_09_ai_apps_tools_setup/` (universal context)
