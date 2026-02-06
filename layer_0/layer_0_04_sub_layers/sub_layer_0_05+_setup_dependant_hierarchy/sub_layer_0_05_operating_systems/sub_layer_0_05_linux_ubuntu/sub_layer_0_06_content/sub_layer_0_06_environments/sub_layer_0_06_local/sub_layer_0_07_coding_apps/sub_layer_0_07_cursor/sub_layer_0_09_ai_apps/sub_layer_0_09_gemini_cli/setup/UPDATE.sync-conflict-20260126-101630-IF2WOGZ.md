# Gemini CLI - Update Instructions (Linux Ubuntu)

**Last Updated:** 2025-01-26  
**Current Version:** 0.23.0  
**OS:** Linux Ubuntu  
**Environment:** Local  
**Coding App:** Cursor

## Overview

This document describes how to update Gemini CLI to the latest version on Linux Ubuntu. For cross-platform documentation, see the [shared update guide](../../../../../../_shared/0.06_environments/_shared/0.07_coding_apps/_shared/0.09_ai_apps/gemini_cli/setup/UPDATE.md).

## Linux Ubuntu-Specific Considerations

### Installation Method on Linux

Gemini CLI is installed via npm on Linux. Ensure you have Node.js and npm installed, preferably via nvm to avoid permission issues.

### PATH Configuration

On Linux Ubuntu, ensure your PATH includes the npm global bin directory:

**If using nvm:**
```bash
# Add to ~/.bashrc or ~/.zshrc
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

**If using system npm:**
```bash
# Check npm global prefix
npm config get prefix
# Add that path/bin to your PATH
export PATH="$(npm config get prefix)/bin:$PATH"
```

## Checking Current Version

Before updating, check your current version:

```bash
gemini --version
```

**Example output:**
```
0.23.0
```

Check installation location:
```bash
which gemini
# Example: /home/dawson/.nvm/versions/node/v22.21.1/bin/gemini
```

Check npm package version:
```bash
npm list -g @google/gemini-cli
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

**Note:** If using nvm, ensure nvm is loaded:
```bash
source ~/.nvm/nvm.sh
# Or ensure it's in your ~/.bashrc
```

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

## Linux-Specific Troubleshooting

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
   # Or add to ~/.bashrc:
   echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.bashrc
   echo '[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. Verify npm global bin directory is in PATH:
   ```bash
   npm config get prefix
   # Add that path/bin to your PATH if not already there
   export PATH="$(npm config get prefix)/bin:$PATH"
   ```

### Issue: Permission errors during update

**Solution:**
1. **Recommended:** Use nvm to manage Node.js and npm (avoids permission issues):
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

### 2025-01-26: Verified/Updated to v0.23.0 on Linux Ubuntu
- **Previous version:** 0.23.0 (already at latest)
- **Method used:** `npm install -g @google/gemini-cli@latest`
- **OS:** Linux Ubuntu
- **Environment:** Local
- **Coding App:** Cursor
- **Notes:** 
  - Update completed successfully
  - No version change (already at latest)
  - All functionality verified
  - Deprecation warning noted but harmless
  - Update process worked smoothly on Linux Ubuntu

## Platform Support

- ✅ **Linux Ubuntu**: Fully supported (this platform)
- ✅ **macOS**: Fully supported
- ✅ **Windows**: Supported (via npm)

## References

- **Shared Update Guide:** `../../../../../../_shared/0.06_environments/_shared/0.07_coding_apps/_shared/0.09_ai_apps/gemini_cli/setup/UPDATE.md`
- **Official Documentation:** https://ai.google.dev/docs
- **npm Package:** https://www.npmjs.com/package/@google/gemini-cli
- **Update Guide:** https://milvus.io/ai-quick-reference/how-do-i-update-gemini-cli

## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **AI Apps Setup:** `../../../../../../_shared/0.06_environments/_shared/0.07_coding_apps/_shared/0.09_ai_apps/_shared/` (universal context)
