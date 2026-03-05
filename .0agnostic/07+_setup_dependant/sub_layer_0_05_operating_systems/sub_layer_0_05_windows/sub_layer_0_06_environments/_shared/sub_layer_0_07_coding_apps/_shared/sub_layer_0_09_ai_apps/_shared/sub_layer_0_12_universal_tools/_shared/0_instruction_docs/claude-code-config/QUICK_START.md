---
resource_id: "9484e8c7-4397-4fca-9d9a-26ebec6b3785"
resource_type: "document"
resource_name: "QUICK_START"
---
# Claude Code Bypass Permissions - Quick Start Guide

<!-- section_id: "3ed2d28c-fd14-4b2d-9e91-8119595df22b" -->
## 5-Minute Setup

<!-- section_id: "83fe21c8-ad8e-43a2-a19d-e10fd588cf3c" -->
### For Personal Projects (Recommended)

1. **Create settings directory:**
   ```bash
   mkdir -p .claude
   ```

2. **Create settings file:**
   ```bash
   cat > .claude/settings.json << 'EOF'
   {
     "permissions": {
       "defaultMode": "bypassPermissions",
       "allow": [
         "WebSearch",
         "WebFetch(domain:*)",
         "Read(/**)",
         "Edit(**)",
         "Write(**)",
         "Bash(git:*)",
         "Bash(npm:*)",
         "Bash(npx:*)"
       ],
       "deny": [
         "Bash(rm -rf /)",
         "Bash(sudo rm -rf :*)",
         "Bash(git push --force origin main)",
         "Bash(git push --force origin master)"
       ]
     }
   }
   EOF
   ```

3. **Done!** Start Claude Code normally:
   ```bash
   claude
   ```

   **You should now see the Shift+Tab bypass mode toggle indicator.**

<!-- section_id: "b5131df9-9615-4903-b613-d2e093b0d848" -->
### For Shared Repositories (Local Override)

1. **Create local settings:**
   ```bash
   mkdir -p .claude
   cat > .claude/settings.local.json << 'EOF'
   {
     "permissions": {
       "defaultMode": "bypassPermissions",
       "allow": [
         "WebSearch",
         "WebFetch(domain:*)",
         "Read(/**)",
         "Edit(**)",
         "Write(**)",
         "Bash(git:*)",
         "Bash(npm:*)",
         "Bash(npx:*)"
       ],
       "deny": [
         "Bash(rm -rf /)",
         "Bash(sudo rm -rf :*)",
         "Bash(git push --force origin main)",
         "Bash(git push --force origin master)"
       ]
     }
   }
   EOF
   ```

2. **Add to .gitignore:**
   ```bash
   echo ".claude/settings.local.json" >> .gitignore
   ```

3. **Done!** Your team won't have bypass mode, but you will.

<!-- section_id: "8b3e3d51-bbc4-4994-87ec-efe67bee3a6c" -->
### One-Time Use (No Configuration)

```bash
claude --dangerously-skip-permissions
```

<!-- section_id: "3d72507e-d554-4a44-bc0d-ea7819995a9d" -->
## Verification

In Claude Code, run:
```
/permissions
```

Look for: "Bypass permissions mode: enabled"

<!-- section_id: "a2418c13-1b5f-40ec-b9ee-b9ecd0d3c024" -->
## Common Configurations

<!-- section_id: "315c1a3f-be0e-4838-88a2-1a475a269b5e" -->
### What Actually Works

**⚠️ IMPORTANT**: The `disableBypassPermissionsMode: false` approach shown in older documentation **does NOT work**. The correct configuration is:

```json
{
  "permissions": {
    "defaultMode": "bypassPermissions",
    "allow": [
      "Read(/**)",
      "Edit(**)",
      "Write(**)",
      "Bash(git:*)",
      "Bash(npm:*)"
    ],
    "deny": [
      "Bash(rm -rf /)",
      "Bash(sudo rm -rf :*)",
      "Bash(git push --force origin main)",
      "Bash(git push --force origin master)",
      "Edit(.env*)"
    ]
  }
}
```

**Key Points:**
- Use `"defaultMode": "bypassPermissions"` to enable bypass mode and show the Shift+Tab toggle
- Include comprehensive `allow` rules for the operations you need
- Add `deny` rules for dangerous operations
- The `disableBypassPermissionsMode` field only accepts `"disable"` as a value (to disable bypass mode)

<!-- section_id: "807d93fe-17da-4db6-9a09-69c2779fb585" -->
### Full Documentation

See [bypass-permissions-setup.md](./bypass-permissions-setup.md) for complete details.

<!-- section_id: "4d3e3c64-4783-47c3-9296-70c37425d0f9" -->
## Need Help?

- **Security concerns?** Read [Security Best Practices](./bypass-permissions-setup.md#security-best-practices)
- **Not working?** See [Troubleshooting](./bypass-permissions-setup.md#troubleshooting)
- **Enterprise environment?** Check [Enterprise Policies](./bypass-permissions-setup.md#enterprise-policy-enforcement)
