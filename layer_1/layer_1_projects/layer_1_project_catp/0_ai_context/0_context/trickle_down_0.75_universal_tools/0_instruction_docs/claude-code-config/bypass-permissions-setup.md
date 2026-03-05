---
resource_id: "ad695678-2ce4-4660-bb87-6696689e5761"
resource_type: "document"
resource_name: "bypass-permissions-setup"
---
# Claude Code Bypass Permissions Setup Guide
*Universal Configuration for Trusted Development Environments*

<!-- section_id: "748300c5-1a89-424f-8037-60ce1dda812b" -->
## Overview

Bypass permissions mode allows Claude Code to operate without permission prompts, enabling autonomous development in trusted environments. This guide covers configuration, implementation, and security considerations.

<!-- section_id: "0f006fd0-be47-4508-ac27-c629107e2da5" -->
## ⚠️ Security Warning

**Use bypass permissions mode ONLY in:**
- Personal development projects
- Trusted local environments
- Isolated development containers
- Educational/learning projects

**NEVER use bypass mode for:**
- Shared team repositories
- Client projects with sensitive data
- Production environments
- Codebases with proprietary information
- Systems with regulatory compliance requirements

<!-- section_id: "08b3fb0f-97e6-4334-beaf-802ee372746b" -->
## Configuration Methods

<!-- section_id: "ab517edb-f796-42e5-ae1c-02873a516294" -->
### Method 1: Project-Level Configuration (Recommended)

This method enables bypass mode for a specific project while maintaining security for other projects.

#### Step 1: Create Project Settings Directory

```bash
mkdir -p .claude
```

#### Step 2: Create Settings File

Create `.claude/settings.json` in your project root:

```json
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
```

**⚠️ IMPORTANT NOTE**: The `disableBypassPermissionsMode` field does NOT work as documented. The schema only accepts `"disable"` as a value, not `false`. The correct way to enable bypass permissions mode is using `defaultMode: "bypassPermissions"` as shown above.

#### Step 3: Add to Version Control (Optional)

If this is a personal project, you can commit this file:

```bash
git add .claude/settings.json
git commit -m "Enable Claude Code bypass permissions for development"
```

**Important**: Only commit this for personal projects. For shared repositories, use `.claude/settings.local.json` instead and add it to `.gitignore`.

#### Configuration Values

| Field | Value | Behavior |
|-------|-------|----------|
| `defaultMode` | `"bypassPermissions"` | **RECOMMENDED**: Enables bypass mode and shows Shift+Tab toggle |
| `defaultMode` | `"default"` | Normal permissions mode (prompts for approval) |
| `defaultMode` | `"acceptEdits"` | Auto-accept edit operations only |
| `defaultMode` | `"plan"` | Start in planning mode |
| `disableBypassPermissionsMode` | `"disable"` | Prevents bypass mode from being activated |
| `disableBypassPermissionsMode` | Not set | Allows bypass mode but doesn't auto-enable it |

**Note**: Despite old documentation suggesting `disableBypassPermissionsMode: false`, this is **invalid**. Use `defaultMode: "bypassPermissions"` instead.

<!-- section_id: "ef5dabee-66d1-483d-8263-b907a54e847b" -->
### Method 2: Command-Line Flag

Enable bypass mode for a single session without modifying configuration files:

```bash
claude --dangerously-skip-permissions
```

**Use cases:**
- One-off autonomous tasks
- Testing without modifying config
- Temporary permission bypass

**Limitations:**
- Only affects current session
- Cannot be overridden by enterprise policies
- No persistent configuration

<!-- section_id: "84346163-d158-40e4-97d0-27b9840d9d05" -->
### Method 3: User-Level Default

Set bypass mode as default for all your projects:

#### Step 1: Create User Settings Directory

```bash
mkdir -p ~/.claude
```

#### Step 2: Create User Settings File

Create `~/.claude/settings.json`:

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

**Note**: Project-level settings can still override this.

<!-- section_id: "7a310f91-d441-4243-b30f-53482581cba6" -->
### Method 4: Local Development Override

For shared repositories where you want bypass mode locally but not for the team:

#### Step 1: Create Local Settings

Create `.claude/settings.local.json`:

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

#### Step 2: Add to .gitignore

Ensure `.claude/settings.local.json` is in your `.gitignore`:

```bash
echo ".claude/settings.local.json" >> .gitignore
```

This allows you to work with bypass mode while team members maintain permission prompts.

<!-- section_id: "4463d118-d7a4-429a-b0b2-6e375283dba3" -->
## Settings Hierarchy

Claude Code reads settings in this precedence order (highest to lowest):

1. **Enterprise Managed Policies** (`managed-settings.json`)
   - Cannot be overridden
   - Deployed by IT/Security teams
   - Enforces organization-wide policies

2. **Command-Line Arguments** (`--dangerously-skip-permissions`)
   - Session-specific
   - Overrides all file-based settings except managed policies

3. **Project Local Settings** (`.claude/settings.local.json`)
   - Developer-specific overrides
   - Not version controlled
   - Highest precedence for file-based settings

4. **Project Settings** (`.claude/settings.json`)
   - Team-shared configuration
   - Version controlled
   - Project-specific defaults

5. **User Settings** (`~/.claude/settings.json`)
   - Personal defaults
   - Applies to all projects
   - Lowest precedence

<!-- section_id: "f434df53-7cdb-442a-9b0c-f2e818fce902" -->
### Example Hierarchy in Action

```
Enterprise Policy:     disableBypassPermissionsMode: "disable"
↓
Result: Bypass mode DISABLED (enterprise policy wins)
```

```
User Settings:         disableBypassPermissionsMode: false
Project Settings:      disableBypassPermissionsMode: "disable"
↓
Result: Bypass mode DISABLED (project settings win)
```

```
Project Settings:      disableBypassPermissionsMode: false
Local Settings:        disableBypassPermissionsMode: "disable"
↓
Result: Bypass mode DISABLED (local settings win)
```

<!-- section_id: "385292a5-299d-4f22-8a81-be8c951a7979" -->
## Implementation Examples

<!-- section_id: "23be7493-5cf5-4273-a65e-fa969bf9edd8" -->
### Example 1: Personal Side Project (CORRECTED)

**Scenario**: Full control, rapid development, no sensitive data

```json
// .claude/settings.json (committed to git)
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
      "Bash(npx:*)",
      "Bash(ls:*)",
      "Bash(cat:*)",
      "Bash(mkdir:*)",
      "Bash(rm:*)",
      "Bash(cp:*)",
      "Bash(mv:*)"
    ],
    "deny": [
      "Bash(rm -rf /)",
      "Bash(sudo rm -rf :*)",
      "Bash(git push --force origin main)",
      "Bash(git push --force origin master)"
    ]
  }
}
```

**Workflow:**
```bash
# Start Claude Code normally - bypass mode is enabled
claude

# You'll see the Shift+Tab toggle indicator showing bypass mode is active
# AI can autonomously perform allowed operations without prompts
# Dangerous operations (in deny list) are still blocked
```

<!-- section_id: "f73fcddf-0783-4ef5-8f5c-53b76c1cf97c" -->
### Example 2: Shared Repository with Local Override

**Scenario**: Team project, you want bypass locally, team wants prompts

```json
// .claude/settings.json (committed - team default)
{
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  },
  "description": "Team project - permissions required by default"
}
```

```json
// .claude/settings.local.json (not committed - your override)
{
  "permissions": {
    "disableBypassPermissionsMode": false
  },
  "description": "Local override - bypass enabled for my development"
}
```

```bash
# Add to .gitignore
echo ".claude/settings.local.json" >> .gitignore
```

<!-- section_id: "ec2cf3e5-7141-4c67-a940-d8346a2b19a4" -->
### Example 3: Hybrid Approach - Selective Bypass

**Scenario**: Want bypass for most operations, but protect sensitive files

```json
// .claude/settings.json
{
  "permissions": {
    "disableBypassPermissionsMode": false,
    "deny": [
      "Read(.env)",
      "Read(.env.*)",
      "Edit(.env)",
      "Edit(.env.*)",
      "Read(config/secrets/**)",
      "Edit(config/secrets/**)",
      "Bash(rm -rf *)",
      "Bash(git push --force*)"
    ]
  },
  "description": "Bypass enabled but sensitive operations denied"
}
```

This configuration:
- Enables bypass mode for general operations
- Explicitly denies access to environment files
- Blocks destructive commands
- Provides a safety net for critical operations

<!-- section_id: "58b9bab5-2d5c-4806-8f92-77c3ad3697fd" -->
### Example 4: Temporary Bypass for Specific Task

**Scenario**: Need bypass for one-time refactoring, normally use permissions

```bash
# One-time use without changing configuration
claude --dangerously-skip-permissions

# Run your task
# Bypass mode only active for this session

# Next time you run claude without the flag:
claude
# Normal permission prompts return
```

<!-- section_id: "61b26300-7224-4e3d-b065-2c2aacc63983" -->
## Verification

<!-- section_id: "f6e0e87f-cfc0-4141-bceb-8d19d7734ad0" -->
### Check Current Settings

```bash
# View current permission configuration
claude
```

Then in Claude Code:
```
/permissions
```

This shows:
- Current bypass mode status
- Active allow/deny rules
- Settings hierarchy being applied

<!-- section_id: "516513aa-64d5-47c0-87c6-2285408addc3" -->
### Test Bypass Mode

Create a test file to verify bypass is working:

```bash
# Start Claude Code
claude

# Ask Claude to create a test file
> "Create a test file called test-bypass.txt with the content 'Bypass mode active'"
```

If bypass mode is enabled:
- No permission prompt appears
- File is created immediately
- Operation completes autonomously

If bypass mode is disabled:
- Permission prompt appears
- You must approve the file creation
- Operation waits for confirmation

<!-- section_id: "842f6b8e-c4db-43b8-8e7d-edee82f81cd7" -->
## Disabling Bypass Mode

<!-- section_id: "af56434f-8e76-4a42-9ea0-df240a48c417" -->
### Temporary Disable (Current Session)

Cannot be done - bypass is session-wide if enabled. Restart Claude Code without the flag.

<!-- section_id: "ea652785-93d1-47b3-bf1b-6a9bc04aa694" -->
### Permanent Disable for Project

```json
// .claude/settings.json
{
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  }
}
```

<!-- section_id: "8262a378-34e2-424e-a8d4-a2aac7e5cb97" -->
### Remove All Bypass Configuration

```bash
# Remove project settings
rm .claude/settings.json
rm .claude/settings.local.json

# Remove user settings
rm ~/.claude/settings.json

# Claude Code will revert to default (prompts enabled)
```

<!-- section_id: "df77cf51-44a2-48b1-ab4d-478864e58906" -->
## Enterprise Policy Enforcement

<!-- section_id: "b53a77ce-63c6-4978-a7a0-72c86b1799df" -->
### Scenario: Organization Requires Permissions

If your organization deploys managed policies, bypass mode may be disabled regardless of your configuration.

**Managed Policy Example** (`managed-settings.json`):
```json
{
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  },
  "enforced": true,
  "description": "Corporate security policy - bypass mode prohibited"
}
```

**Result**: You cannot enable bypass mode, even with:
- Project settings
- User settings
- Command-line flags

**What to do:**
1. Contact your IT/Security team
2. Request exception for specific projects
3. Explain business justification
4. Follow your organization's security approval process

<!-- section_id: "92fdbe4a-d84d-4e1c-935a-f7e0e7aed0ca" -->
## Troubleshooting

<!-- section_id: "aa2ad6ab-6e0b-4c41-9156-3eecd3bb28ed" -->
### Shift+Tab Toggle Not Appearing

**Symptom**: Cannot see the bypass permissions mode toggle indicator in the UI

**Root Cause**: The Shift+Tab toggle only appears when `defaultMode: "bypassPermissions"` is set.

**Solution:**
1. ✅ Add `"defaultMode": "bypassPermissions"` to your settings file
2. ✅ Include comprehensive `allow` rules (see working example below)
3. ✅ Restart Claude Code

**Working Configuration:**
```json
{
  "permissions": {
    "defaultMode": "bypassPermissions",
    "allow": [
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
      "Bash(git push --force origin main)"
    ]
  }
}
```

**What DOESN'T Work:**
```json
{
  "permissions": {
    "disableBypassPermissionsMode": false  // ❌ INVALID - does not show toggle
  }
}
```

The `disableBypassPermissionsMode` field only accepts `"disable"` as a value (to prevent bypass mode). Setting it to `false` is invalid according to the schema.

<!-- section_id: "054bf2c4-7b4d-4501-a769-4a8fafdb76f2" -->
### Bypass Mode Not Working

**Symptom**: Still seeing permission prompts despite configuration

**Checklist:**
1. ✅ Verify you're using `"defaultMode": "bypassPermissions"` (not `disableBypassPermissionsMode: false`)
2. ✅ Include comprehensive `allow` rules in your configuration
3. ✅ Check for enterprise managed policies
4. ✅ Ensure JSON syntax is valid
5. ✅ Verify file is in correct location (`.claude/settings.json` or `.claude/settings.local.json`)
6. ✅ Restart Claude Code after changing settings
7. ✅ Check settings precedence - higher level may override

**Diagnostic:**
```bash
# Check if settings file is valid JSON
cat .claude/settings.json | python3 -m json.tool

# Review settings hierarchy
claude
# Then: /permissions
```

<!-- section_id: "13dcf9a8-bf75-4ce6-a3fe-d490687c8819" -->
### Bypass Mode Active When It Shouldn't Be

**Symptom**: No permission prompts when you expected them

**Checklist:**
1. ✅ Check for `--dangerously-skip-permissions` flag in launch command
2. ✅ Look for `.claude/settings.local.json` override
3. ✅ Review user-level settings (`~/.claude/settings.json`)
4. ✅ Verify project settings don't enable bypass

**Fix:**
```bash
# Find all settings files
find ~ -name "settings.json" -o -name "settings.local.json" 2>/dev/null

# Review each for bypass configuration
```

<!-- section_id: "62367a23-2bdc-4b70-90a3-972fc0567004" -->
### Specific Operations Still Require Permissions

**Symptom**: Bypass mode enabled, but some operations still prompt

**Explanation**: Deny rules override bypass mode

**Example:**
```json
{
  "permissions": {
    "disableBypassPermissionsMode": false,
    "deny": [
      "Bash(rm *)"
    ]
  }
}
```

Even with bypass enabled, `rm` commands will be denied.

**Solution**: Remove deny rules if you want full bypass, or keep them for safety.

<!-- section_id: "14aa5f53-ec14-4328-af6c-109feff71d75" -->
## Security Best Practices

<!-- section_id: "ed8b2026-a645-4f9b-97ab-8ad09bbaba5c" -->
### 1. Scope Bypass to Specific Projects

❌ **Don't do this:**
```json
// ~/.claude/settings.json (applies to ALL projects)
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

✅ **Do this instead:**
```json
// .claude/settings.json (specific project only)
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

<!-- section_id: "4b030b56-590b-48f2-825b-f57316f8c56e" -->
### 2. Document Why Bypass is Enabled

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false
  },
  "description": "Personal learning project - bypass enabled for rapid experimentation",
  "project": "python-automation-tools",
  "owner": "personal",
  "risk_level": "low"
}
```

<!-- section_id: "77f66237-e5c7-4c68-b5a1-d8df931a166c" -->
### 3. Use Deny Rules for Critical Operations

Even with bypass mode, protect destructive operations:

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false,
    "deny": [
      "Bash(rm -rf /)",
      "Bash(sudo rm *)",
      "Bash(git push --force*)",
      "Bash(DROP TABLE*)",
      "Edit(.git/config)",
      "Bash(curl * | bash)"
    ]
  }
}
```

<!-- section_id: "5cc14bab-beaa-4922-ac39-55965514a143" -->
### 4. Regular Security Reviews

Periodically review and audit your bypass configurations:

```bash
# Find all bypass configurations
find ~ -name "settings*.json" -exec grep -l "disableBypassPermissionsMode.*false" {} \;

# Review each one
# Remove bypass from projects that no longer need it
```

<!-- section_id: "39f40cd9-81ab-4cc2-9d0b-7f6709995317" -->
### 5. Use Version Control Wisely

```gitignore
# .gitignore
.claude/settings.local.json   # Personal overrides
.claude/managed-settings.json # Enterprise policies
.env*                          # Secrets
```

```bash
# What TO commit
git add .claude/settings.json  # Only if personal project
```

<!-- section_id: "fdfc756b-219f-4b7a-bcda-549a53ab6346" -->
## Alternative: Fine-Grained Permissions

Instead of bypassing all permissions, consider allowing specific operations:

```json
{
  "permissions": {
    "allow": [
      "Read(**)",
      "Bash(npm *)",
      "Bash(git status)",
      "Bash(git diff)",
      "Edit(src/**)",
      "Edit(tests/**)",
      "Write(docs/**)"
    ]
  }
}
```

**Benefits:**
- No permission prompts for allowed operations
- Maintains security for non-allowed operations
- More granular control than bypass mode
- Better for shared repositories

**See**: [fine-grained-permissions.md](./fine-grained-permissions.md)

<!-- section_id: "3a9b030c-c6b3-43ad-8904-636072d275c5" -->
## Frequently Asked Questions

<!-- section_id: "82f2eabc-d20a-446c-b4db-e5453529beca" -->
### Q: Is bypass mode safe for personal projects?

**A**: Yes, if:
- You fully control the repository
- No sensitive data is present
- Not connected to production systems
- You understand the implications

<!-- section_id: "3f9b6171-ab5b-41e8-855f-843c14852ceb" -->
### Q: Can I use bypass mode in a Docker container?

**A**: Yes, containers provide additional isolation:
```dockerfile
# Dockerfile
FROM python:3.11
WORKDIR /app
COPY .claude/settings.json .claude/
# Bypass mode contained within container
```

<!-- section_id: "0c00f64b-b62a-4fca-8609-4b12ee40edd5" -->
### Q: What happens if I forget bypass mode is enabled?

**A**: Claude Code will operate autonomously without prompts. You may experience:
- Unexpected file modifications
- Commands executed without confirmation
- Potential data loss if destructive operations occur

**Mitigation**: Use deny rules for critical operations.

<!-- section_id: "eb26f765-53e5-4f4a-a65c-b3cc1b78b670" -->
### Q: Can enterprise policies be bypassed?

**A**: No. Managed policies have highest precedence and cannot be overridden.

<!-- section_id: "d8c257ce-2c82-4d3b-a35f-4365bf1a7057" -->
### Q: Does bypass mode affect MCP servers?

**A**: Historically yes (Issue #5307), though this may be fixed in newer versions. Test your specific version.

<!-- section_id: "0a2a569c-e787-432d-be7d-88c6e8df6093" -->
## Related Documentation

- [Fine-Grained Permissions](./fine-grained-permissions.md)
- [Enterprise Security Policies](./enterprise-policies.md)
- [Project Settings Setup](./project-settings.md)
- [Settings Hierarchy](./settings-hierarchy.md)

<!-- section_id: "113e1211-0741-47f1-be4b-4d5fcd2d5652" -->
## External References

- [Official Claude Code Settings Docs](https://docs.claude.com/en/docs/claude-code/settings)
- [IAM Documentation](https://docs.claude.com/en/docs/claude-code/iam)
- [Security Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)

<!-- section_id: "62d41041-3f91-485f-8264-8bc30d1181b7" -->
## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0   | 2025-10-24 | Initial documentation created |

---
*This guide is part of the Universal Tools (Level 0.75) and provides implementation patterns for any Claude Code project.*
