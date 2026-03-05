---
resource_id: "35aa04d0-c7ae-40f7-a247-58f8981e41ca"
resource_type: "document"
resource_name: "UPDATE"
---
# Codex CLI - Update Instructions (Linux Ubuntu)

**Last Updated:** 2025-01-26  
**Current Version:** 0.80.0  
**OS:** Linux Ubuntu  
**Environment:** Local  
**Coding App:** Cursor

<!-- section_id: "03970796-1d55-412f-8ad8-30be10bf4c95" -->
## Overview

This document describes how to update Codex CLI to the latest version on Linux Ubuntu. For cross-platform documentation, see the [shared update guide](../../../../../../_shared/0.06_environments/_shared/0.07_coding_apps/_shared/0.09_ai_apps/codex_cli/setup/UPDATE.md).

<!-- section_id: "427c2798-00cc-4cf3-98ff-a186ef5da72a" -->
## Linux Ubuntu-Specific Considerations

<!-- section_id: "b0c4c0ab-4cfc-444d-a5fd-78053c4fe75e" -->
### Installation Method on Linux

Codex CLI is installed via npm on Linux. Ensure you have Node.js and npm installed, preferably via nvm to avoid permission issues.

<!-- section_id: "4212b3c3-a805-4200-9283-b189c95f893b" -->
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

<!-- section_id: "8c6c4ab1-b619-41dc-ba9a-d89272e3a8a8" -->
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

<!-- section_id: "a4e0013d-399b-4fd3-89e7-52147330bf26" -->
## Update Method

<!-- section_id: "f6aaba1d-34fc-48d5-b4b6-23b84f14562a" -->
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

<!-- section_id: "6d8d33ae-c606-48fd-b97c-232115ba6056" -->
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

<!-- section_id: "5bb2efa8-c952-45b4-a1b4-71bd6283c274" -->
## Linux-Specific Troubleshooting

<!-- section_id: "d9983c1e-5d56-49aa-a165-bc9a8188dcb4" -->
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

<!-- section_id: "10f7b906-dde5-47eb-858b-428992733f09" -->
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

<!-- section_id: "0ad1bfb2-73ab-4b4a-94f6-b40226a38d7b" -->
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

<!-- section_id: "9fd30fbd-702b-4a14-b47b-1746f8aebb5a" -->
## Update History

<!-- section_id: "2ef73476-4232-47a0-9eb8-49930e603881" -->
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

<!-- section_id: "fc28b2c4-851f-4316-bb2f-c74c5674cf46" -->
## Platform Support

- ✅ **Linux Ubuntu**: Fully supported (this platform)
- ✅ **macOS**: Fully supported
- ⚠️ **Windows**: Experimental (recommended to use WSL)

<!-- section_id: "fab50f1f-41bc-4429-a400-fb89f3af7db8" -->
## References

- **Shared Update Guide:** `../../../../../../_shared/0.06_environments/_shared/0.07_coding_apps/_shared/0.09_ai_apps/codex_cli/setup/UPDATE.md`
- **Official Documentation:** https://developers.openai.com/codex/cli
- **npm Package:** https://www.npmjs.com/package/@openai/codex

<!-- section_id: "506a1b26-1882-428e-b6b5-feec25e8c2a8" -->
## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **AI Apps Setup:** `../../../../../../_shared/0.06_environments/_shared/0.07_coding_apps/_shared/0.09_ai_apps/_shared/` (universal context)
