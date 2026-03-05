---
resource_id: "4eaf8b0c-8080-45e8-a5b4-2fdbe5259b98"
resource_type: "document"
resource_name: "UPDATE"
---
# Codex CLI - Update Instructions

**Last Updated:** 2025-01-26  
**Current Version:** 0.80.0

<!-- section_id: "668d66e1-9e01-46dc-bb92-655e9251f932" -->
## Overview

This document describes how to update Codex CLI to the latest version. Codex CLI is distributed via npm and can be updated using standard npm commands.

<!-- section_id: "8494ea0b-ba6c-4f7c-a446-f3a3c2a9b757" -->
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

<!-- section_id: "161f5612-5ca5-4f9d-b816-36a532f497d4" -->
## Update Method

<!-- section_id: "5acf4135-2b81-48cf-9053-f1702365b3d7" -->
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

<!-- section_id: "fe3f43e2-abf9-4b6b-b115-4fa07290177c" -->
### Alternative: npm update

You can also use the `npm update` command:

```bash
npm update -g @openai/codex
```

**Note:** `npm update` may not always install the latest version if your current version satisfies the semver range. Using `npm install -g @openai/codex@latest` ensures you get the absolute latest version.

<!-- section_id: "0d2c2134-048f-4c5c-a8b7-3e2a08bc5d8e" -->
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

<!-- section_id: "ab44f315-42a8-4978-b71d-84f914bf443b" -->
## Troubleshooting

<!-- section_id: "19a8de99-3594-4783-a78b-30c2317c14da" -->
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

<!-- section_id: "20897ec1-5e4f-453d-90bd-4618d630f586" -->
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

<!-- section_id: "885f81cc-d32c-4b24-864b-00b5e436a06c" -->
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

<!-- section_id: "70603614-d6e8-4516-b490-3e2c54917041" -->
## Update History

<!-- section_id: "1b6db0cb-0d1c-44d9-a009-f063a24a194c" -->
### 2025-01-26: Updated to v0.80.0
- **Previous version:** 0.79.0
- **Method used:** `npm install -g @openai/codex@latest`
- **Notes:** 
  - Update completed successfully
  - No configuration changes required
  - All functionality verified after update

<!-- section_id: "4977cd4f-d167-42b4-ac97-e6bf6aa4b354" -->
## Platform Support

- ✅ **macOS**: Fully supported
- ✅ **Linux**: Fully supported
- ⚠️ **Windows**: Experimental (recommended to use WSL)

<!-- section_id: "e88c9429-50b4-4fa6-810c-67d9064659de" -->
## References

- **Official Documentation:** https://developers.openai.com/codex/cli
- **npm Package:** https://www.npmjs.com/package/@openai/codex

<!-- section_id: "dfcd0ee5-7663-4321-92fc-fb491b9ec536" -->
## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **AI Apps Setup:** `../../sub_layer_0_09_ai_apps_tools_setup/` (universal context)
