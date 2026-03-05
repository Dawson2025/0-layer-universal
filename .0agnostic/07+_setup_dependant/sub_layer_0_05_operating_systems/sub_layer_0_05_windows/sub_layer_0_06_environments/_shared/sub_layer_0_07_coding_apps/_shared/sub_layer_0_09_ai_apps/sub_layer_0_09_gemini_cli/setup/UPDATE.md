---
resource_id: "a7b3c993-8419-4d02-aca8-8da37d77f819"
resource_type: "document"
resource_name: "UPDATE"
---
# Gemini CLI - Update Instructions

**Last Updated:** 2025-01-26  
**Current Version:** 0.23.0

## Overview

This document describes how to update Gemini CLI to the latest version. Gemini CLI is distributed via npm and can be updated using standard npm commands.

## Checking Current Version

Before updating, check your current version:

```bash
gemini --version
```

**Example output:**
```
0.23.0
```

You can also check the npm package version:

```bash
npm list -g @google/gemini-cli
```

**Example output:**
```
/home/dawson/.nvm/versions/node/v22.21.1/lib
└── @google/gemini-cli@0.23.0
```

## Update Method

### npm Update (Standard Method)

Gemini CLI is managed through npm. To update to the latest version:

```bash
npm install -g @google/gemini-cli@latest
```

**What this does:**
- Downloads and installs the latest version of `@google/gemini-cli`
- Replaces the previous global installation
- Updates the `gemini` command to the new version

**Example output:**
```
npm warn deprecated node-domexception@1.0.0: Use your platform's native DOMException instead

changed 583 packages in 19s

155 packages are looking for funding
  run `npm fund` for details
```

**Note:** The deprecation warning about `node-domexception` is harmless and comes from a dependency. It does not affect functionality.

### Alternative: npm update

You can also use the `npm update` command:

```bash
npm update -g @google/gemini-cli
```

**Note:** `npm update` may not always install the latest version if your current version satisfies the semver range. Using `npm install -g @google/gemini-cli@latest` ensures you get the absolute latest version.

### Alternative: Using npx (No Global Installation)

If you prefer not to install globally, you can use `npx` which automatically fetches and runs the latest version:

```bash
npx @google/gemini-cli
```

**Benefits:**
- Always uses the latest version
- No global installation needed
- No manual updates required

**Drawbacks:**
- Slightly slower startup (downloads on first run)
- Requires internet connection

## Verification After Update

After updating, verify the installation:

```bash
# Check version
gemini --version

# Check installation location
which gemini

# Check npm package version
npm list -g @google/gemini-cli

# Test basic functionality
gemini --help
```

## Troubleshooting

### Issue: "Command not found" after update

**Solution:**
1. Check if the binary is in your PATH:
   ```bash
   which gemini
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
   npm install -g @google/gemini-cli@latest --force
   ```

2. Clear npm cache and reinstall:
   ```bash
   npm cache clean --force
   npm install -g @google/gemini-cli@latest
   ```

3. Verify you're using the correct Node.js version:
   ```bash
   node --version
   npm --version
   ```

### Issue: Deprecation warnings

**Solution:**
- The `node-domexception@1.0.0` deprecation warning is harmless
- It comes from a dependency and does not affect Gemini CLI functionality
- The warning will be resolved when the dependency is updated by the maintainers

## Update History

### 2025-01-26: Verified/Updated to v0.23.0
- **Previous version:** 0.23.0 (already at latest)
- **Method used:** `npm install -g @google/gemini-cli@latest`
- **Notes:** 
  - Update completed successfully
  - No version change (already at latest)
  - All functionality verified
  - Deprecation warning noted but harmless

## Platform Support

- ✅ **macOS**: Fully supported
- ✅ **Linux**: Fully supported
- ✅ **Windows**: Supported (via npm)

## References

- **Official Documentation:** https://ai.google.dev/docs
- **npm Package:** https://www.npmjs.com/package/@google/gemini-cli
- **Update Guide:** https://milvus.io/ai-quick-reference/how-do-i-update-gemini-cli

## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **AI Apps Setup:** `../../sub_layer_0_09_ai_apps_tools_setup/` (universal context)
