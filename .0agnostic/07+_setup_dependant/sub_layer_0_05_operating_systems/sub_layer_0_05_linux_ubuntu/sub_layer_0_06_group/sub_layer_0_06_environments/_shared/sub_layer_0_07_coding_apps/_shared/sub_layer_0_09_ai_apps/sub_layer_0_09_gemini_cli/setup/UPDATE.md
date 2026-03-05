---
resource_id: "bce76fdd-1e7f-4fe3-9646-f730f76527b3"
resource_type: "document"
resource_name: "UPDATE"
---
# Gemini CLI - Update Instructions

**Last Updated:** 2025-01-26  
**Current Version:** 0.23.0

<!-- section_id: "db134b25-455a-4893-87dd-85f2e0be2ade" -->
## Overview

This document describes how to update Gemini CLI to the latest version. Gemini CLI is distributed via npm and can be updated using standard npm commands.

<!-- section_id: "c7acb7bd-1642-49f7-b8ec-396913edd5a2" -->
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

<!-- section_id: "2d0e054e-65b9-43ce-be08-4c03e2c6a04f" -->
## Update Method

<!-- section_id: "0b37276f-1dd1-4b9b-be6d-fffd8b48af28" -->
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

<!-- section_id: "0b498512-8047-4fbd-abe2-c58398988424" -->
### Alternative: npm update

You can also use the `npm update` command:

```bash
npm update -g @google/gemini-cli
```

**Note:** `npm update` may not always install the latest version if your current version satisfies the semver range. Using `npm install -g @google/gemini-cli@latest` ensures you get the absolute latest version.

<!-- section_id: "843a2365-b8af-4f64-b3c6-5474752847bf" -->
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

<!-- section_id: "b365d543-554d-4341-bcb3-29c44cf556db" -->
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

<!-- section_id: "c3e673f8-2dc2-436d-b2af-d21f8ac628d7" -->
## Troubleshooting

<!-- section_id: "81bec4f8-3d68-4a0c-8761-5157ccdb6016" -->
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

<!-- section_id: "a2c23e61-f842-4980-89d2-e18fca71a6bc" -->
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

<!-- section_id: "7c4dd69d-483e-43df-8f2a-e149590d3029" -->
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

<!-- section_id: "e4018096-a379-4363-8c6a-aef05d57f34a" -->
### Issue: Deprecation warnings

**Solution:**
- The `node-domexception@1.0.0` deprecation warning is harmless
- It comes from a dependency and does not affect Gemini CLI functionality
- The warning will be resolved when the dependency is updated by the maintainers

<!-- section_id: "8d5d657f-219f-4c7b-a063-99b120e9f395" -->
## Update History

<!-- section_id: "c7f1df23-8c6a-44f6-aef9-a0c43b449aa5" -->
### 2025-01-26: Verified/Updated to v0.23.0
- **Previous version:** 0.23.0 (already at latest)
- **Method used:** `npm install -g @google/gemini-cli@latest`
- **Notes:** 
  - Update completed successfully
  - No version change (already at latest)
  - All functionality verified
  - Deprecation warning noted but harmless

<!-- section_id: "646c92c3-433f-45ac-a090-9a7ba56cf5f2" -->
## Platform Support

- ✅ **macOS**: Fully supported
- ✅ **Linux**: Fully supported
- ✅ **Windows**: Supported (via npm)

<!-- section_id: "b625838c-d0c2-4fcd-9096-8841437dc0f7" -->
## References

- **Official Documentation:** https://ai.google.dev/docs
- **npm Package:** https://www.npmjs.com/package/@google/gemini-cli
- **Update Guide:** https://milvus.io/ai-quick-reference/how-do-i-update-gemini-cli

<!-- section_id: "f9fc985b-e511-4124-87ab-a6f10d4e5af7" -->
## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **AI Apps Setup:** `../../sub_layer_0_09_ai_apps_tools_setup/` (universal context)
