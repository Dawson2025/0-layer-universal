# Codex CLI - Update Instructions (Linux Ubuntu)

**Last Updated:** 2025-01-26  
**Current Version:** 0.80.0  
**OS:** Linux Ubuntu  
**Environment:** Local  
**Coding App:** Cursor

## Overview

This document describes how to update Codex CLI to the latest version on Linux Ubuntu. For cross-platform documentation, see the [shared update guide](../../../../../../_shared/0.03_environments/_shared/0.04_coding_apps/_shared/0.05_ai_apps/codex_cli/setup/UPDATE.md).

## Linux Ubuntu-Specific Considerations

### Installation Method on Linux

Codex CLI is installed via npm on Linux. Ensure you have Node.js and npm installed, preferably via nvm to avoid permission issues.

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
codex --version
```

**Example output:**
```
codex-cli 0.80.0
```

Check installation location:
```bash
which codex
# Example: /home/dawson/.nvm/versions/node/v22.21.1/bin/codex
```

Check npm package version:
```bash
npm list -g @openai/codex
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

**Note:** If using nvm, ensure nvm is loaded:
```bash
source ~/.nvm/nvm.sh
# Or ensure it's in your ~/.bashrc
```

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

## Linux-Specific Troubleshooting

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

### 2025-01-26: Updated to v0.80.0 on Linux Ubuntu
- **Previous version:** 0.79.0
- **Method used:** `npm install -g @openai/codex@latest`
- **OS:** Linux Ubuntu
- **Environment:** Local
- **Coding App:** Cursor
- **Notes:** 
  - Update completed successfully
  - No configuration changes required
  - All functionality verified after update
  - Update process worked smoothly on Linux Ubuntu

## Platform Support

- ✅ **Linux Ubuntu**: Fully supported (this platform)
- ✅ **macOS**: Fully supported
- ⚠️ **Windows**: Experimental (recommended to use WSL)

## References

- **Shared Update Guide:** `../../../../../../_shared/0.03_environments/_shared/0.04_coding_apps/_shared/0.05_ai_apps/codex_cli/setup/UPDATE.md`
- **Official Documentation:** https://developers.openai.com/codex/cli
- **npm Package:** https://www.npmjs.com/package/@openai/codex

## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **AI Apps Setup:** `../../../../../../_shared/0.03_environments/_shared/0.04_coding_apps/_shared/0.05_ai_apps/_shared/` (universal context)
