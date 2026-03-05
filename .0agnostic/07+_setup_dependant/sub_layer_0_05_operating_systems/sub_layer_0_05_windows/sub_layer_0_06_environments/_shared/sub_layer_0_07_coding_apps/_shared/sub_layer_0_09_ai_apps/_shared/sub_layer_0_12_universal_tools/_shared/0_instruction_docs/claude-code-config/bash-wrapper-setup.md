---
resource_id: "3da3680b-97d1-40f4-b9c7-8163044e97ea"
resource_type: "document"
resource_name: "bash-wrapper-setup"
---
# Claude Code Bash Wrapper Setup Guide
*Advanced Configuration: Conditional Bypass Permissions via Shell Wrapper*

<!-- section_id: "5b7fcdaa-92cf-4190-beca-285e10909711" -->
## Overview

This guide documents how to create a bash wrapper function that conditionally enables bypass permissions based on your current directory or environment variables. This approach provides more flexibility than configuration files alone.

<!-- section_id: "d45de391-4ccb-429c-9d31-2b69bc24d206" -->
## Why Use a Bash Wrapper?

<!-- section_id: "390b254e-ecd2-490e-95c9-069f91de52b5" -->
### Advantages

✅ **Context-Aware Bypass**
- Enable bypass only in specific directories
- Control via environment variables
- Different behavior per project

✅ **No Configuration File Changes**
- Works without modifying `.claude/settings.json`
- Doesn't affect version-controlled settings
- Easy to enable/disable globally

✅ **Granular Control**
- Per-directory automation
- Per-session control via environment variables
- Preserves help/version commands

<!-- section_id: "bd700feb-c0bb-4bf1-bc2a-0997478bd938" -->
### Disadvantages

❌ **Shell-Specific**
- Only works in bash/zsh
- Doesn't affect Claude Code launched from GUI
- Must configure each shell environment

❌ **Less Discoverable**
- Hidden in shell config files
- Team members won't automatically get it
- Harder to audit than configuration files

<!-- section_id: "7765977a-fc78-4efd-811e-04fad5034835" -->
## Implementation

<!-- section_id: "4f0de6c8-10be-4a36-8d67-0a40b68f1dd9" -->
### Method 1: Project Directory-Based Bypass

This wrapper enables bypass permissions automatically when you're in a specific project directory.

#### Step 1: Find Claude Binary Path

```bash
which claude
# Output example: /home/username/.nvm/versions/node/v22.20.0/bin/claude
```

Store this path - you'll need it for the wrapper.

#### Step 2: Add Wrapper to ~/.bashrc

Open your `~/.bashrc` (or `~/.zshrc` for zsh):

```bash
nano ~/.bashrc
```

Add this function at the end:

```bash
# >>> CLAUDE_WRAPPER_CONDITIONAL_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when in project directory
    if [[ "$PWD" == "/home/username/code/my-project"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_CONDITIONAL_END
```

**Important**: Replace:
- `/home/username/.nvm/versions/node/v22.20.0/bin/claude` with your actual path from step 1
- `/home/username/code/my-project` with your project path

#### Step 3: Reload Shell Configuration

```bash
source ~/.bashrc
```

#### Step 4: Verify Wrapper

```bash
# Check the wrapper function exists
typeset -f claude

# Test inside your project directory
cd /home/username/code/my-project
claude -p "echo 'testing bypass'"
# Should run without permission prompts

# Test outside your project directory
cd /tmp
claude -p "echo 'testing normal'"
# Should run with normal permission behavior
```

<!-- section_id: "592418df-c6a4-4064-a5c1-89afd927fe4c" -->
### Method 2: Environment Variable-Based Bypass

Enable bypass permissions on-demand with an environment variable.

```bash
# >>> CLAUDE_WRAPPER_ENV_VAR_START
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_ENV_VAR_END
```

**Usage:**

```bash
# Normal mode (with permissions)
claude

# Bypass mode (for this session)
CLAUDE_UNSAFE=1 claude

# Or set for entire session
export CLAUDE_UNSAFE=1
claude
# ... work without prompts ...
unset CLAUDE_UNSAFE  # Back to normal
```

<!-- section_id: "d7ddea0b-a95f-408d-b7c7-8beb4a427d00" -->
### Method 3: Combined Approach (Recommended)

Combine both methods for maximum flexibility:

```bash
# >>> CLAUDE_WRAPPER_COMBINED_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1 OR in project directory
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/my-project"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_COMBINED_END
```

**Behavior:**
- Inside `/home/username/code/my-project`: Bypass enabled automatically
- Outside that directory: Normal permissions
- Anywhere with `CLAUDE_UNSAFE=1`: Bypass enabled
- `--help` and `--version`: Always work normally

<!-- section_id: "1b1993a9-476e-4803-8b91-c1bce2e4d1fa" -->
## Real-World Example

Here's the exact wrapper from the Lang-Trak project:

```bash
# >>> CLAUDE_WRAPPER_CONDITIONAL_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/dawson/.nvm/versions/node/v22.20.0/bin/claude"
if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1 or when in the project directory
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/dawson/code/lang-trak-in-progress"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_CONDITIONAL_END
```

**Testing Results:**
```bash
# Inside project
$ cd /home/dawson/code/lang-trak-in-progress
$ claude -p "echo hello"
hello  # No permission prompt

# Outside project
$ cd /tmp
$ claude -p "echo hello"
# Permission prompt appears (normal behavior)

# Override from outside project
$ cd /tmp
$ CLAUDE_UNSAFE=1 claude -p "echo hello"
hello  # No permission prompt
```

<!-- section_id: "1813648c-c1de-495a-a1c1-293759386e2e" -->
## Advanced Configurations

<!-- section_id: "2987f09a-b57c-4ba0-ad64-39e9fbd2aa6a" -->
### Multiple Project Directories

Enable bypass for multiple projects:

```bash
claude() {
  # ... help/version handling ...

  # List of trusted project directories
  local trusted_dirs=(
    "/home/username/code/personal-project"
    "/home/username/code/side-project"
    "/home/username/experiments"
  )

  # Check if current directory starts with any trusted path
  local bypass=0
  for dir in "${trusted_dirs[@]}"; do
    if [[ "$PWD" == "$dir"* ]]; then
      bypass=1
      break
    fi
  done

  # Enable bypass if in trusted directory or CLAUDE_UNSAFE=1
  if [ "$bypass" = "1" ] || [ "${CLAUDE_UNSAFE:-0}" = "1" ]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "f79994c2-5e84-4d8f-a22a-d63219418c01" -->
### Time-Based Bypass

Automatically disable bypass during certain hours (e.g., working hours for client projects):

```bash
claude() {
  # ... help/version handling ...

  # Get current hour (0-23)
  local hour=$(date +%H)

  # Disable bypass during working hours (9 AM - 5 PM)
  if [ "$hour" -ge 9 ] && [ "$hour" -lt 17 ]; then
    # Normal mode during work hours
    command "$_claude_real" "$@"
  else
    # Bypass enabled outside work hours
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/personal"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  fi
}
```

<!-- section_id: "628b62aa-730b-44e4-928f-707e76f6a638" -->
### Git Repository Detection

Enable bypass only in git repositories you own:

```bash
claude() {
  # ... help/version handling ...

  # Check if in a git repo
  if git rev-parse --git-dir > /dev/null 2>&1; then
    # Get git user email
    local git_email=$(git config user.email)

    # Enable bypass if it's your personal email
    if [[ "$git_email" == "personal@example.com" ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  else
    # Not in a git repo - normal mode
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "61ee1bc4-d3a1-4708-a77f-b8616d065048" -->
## Debugging

<!-- section_id: "72245fce-fd56-404c-b7f3-502a5d9cca82" -->
### Check if Wrapper is Active

```bash
# View the current wrapper function
typeset -f claude

# Check which claude command is being used
type claude
# Should output: claude is a function
```

<!-- section_id: "3e67fbcb-5438-4d5c-8e61-8ac79255118d" -->
### Test Without Wrapper

To temporarily bypass the wrapper and use the real binary:

```bash
# Use full path
/home/username/.nvm/versions/node/v22.20.0/bin/claude

# Or use command builtin
command /path/to/real/claude
```

<!-- section_id: "5c670d7f-cf4f-48c7-8803-a5c3e75be072" -->
### Enable Debug Output

Add debugging to your wrapper:

```bash
claude() {
  # Debug mode
  if [ "${CLAUDE_DEBUG:-0}" = "1" ]; then
    echo "[DEBUG] PWD: $PWD"
    echo "[DEBUG] CLAUDE_UNSAFE: ${CLAUDE_UNSAFE:-0}"
    echo "[DEBUG] Will use bypass: $([ condition ] && echo yes || echo no)"
  fi

  # ... rest of wrapper ...
}
```

Usage:
```bash
CLAUDE_DEBUG=1 claude -p "echo test"
```

<!-- section_id: "3c8313ff-b392-4e25-9436-0291525099ee" -->
## Removing the Wrapper

<!-- section_id: "31050a37-9212-4fa3-b13e-3d5f5507e41f" -->
### Temporary Removal (Current Session)

```bash
unset -f claude
```

<!-- section_id: "a4cde5d4-fb1f-4b3a-a9b0-29f3dff5c380" -->
### Permanent Removal

1. Edit `~/.bashrc`:
   ```bash
   nano ~/.bashrc
   ```

2. Remove the wrapper block (between the comment markers)

3. Reload shell:
   ```bash
   source ~/.bashrc
   ```

4. Verify:
   ```bash
   type claude
   # Should output the path to the binary, not "claude is a function"
   ```

<!-- section_id: "858c74c2-9f0f-4d31-b958-0b3140ac9424" -->
## Security Considerations

<!-- section_id: "e5cd74b3-8627-46a7-8f68-4cf1732cd3a8" -->
### Risks

⚠️ **Directory-Based Bypass**
- Anyone with access to the directory gets bypass mode
- Symbolic links could potentially exploit path matching
- Subdirectories inherit bypass behavior

⚠️ **Environment Variable Bypass**
- Environment variables can be set by scripts
- Child processes inherit `CLAUDE_UNSAFE=1`
- Easy to forget it's enabled

⚠️ **Shell Configuration Files**
- `~/.bashrc` is executable code
- Errors can break your shell
- Hard for others to discover the bypass is active

<!-- section_id: "c2c05b2e-cc27-4feb-bbc1-62e075effda5" -->
### Mitigations

✅ **Add Visual Indicators**

```bash
claude() {
  # ... condition checks ...

  if [ "$using_bypass" = "1" ]; then
    echo "⚠️  BYPASS MODE ACTIVE" >&2
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

✅ **Log Bypass Usage**

```bash
claude() {
  # ... condition checks ...

  if [ "$using_bypass" = "1" ]; then
    echo "$(date): Bypass enabled in $PWD" >> ~/.claude/bypass.log
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

✅ **Restrict by Ownership**

```bash
claude() {
  # Only enable bypass if you own the directory
  if [ -O "$PWD" ] && [[ "$PWD" == "/home/username/code"* ]]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "8e6f35d1-5f8f-4a5f-a2e9-3aaf9cba3d6a" -->
## Integration with Configuration Files

The bash wrapper approach **works alongside** `.claude/settings.json` configurations:

<!-- section_id: "df84f41f-dee9-4196-89de-7f68211fd1de" -->
### Precedence

1. **Bash Wrapper** (highest)
   - If wrapper adds `--dangerously-skip-permissions`, that takes effect

2. **Command-Line Flags**
   - Flags passed to the wrapper are forwarded

3. **Configuration Files**
   - `.claude/settings.json` and `.claude/settings.local.json`
   - Still respected when wrapper doesn't add bypass flag

<!-- section_id: "fcf3b724-0d50-44c6-b9f9-bd89a53d5f71" -->
### Example: Hybrid Approach

```bash
# ~/.bashrc - Project directory gets wrapper bypass
claude() {
  if [[ "$PWD" == "/home/username/code/personal"* ]]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

```json
// /home/username/code/work-project/.claude/settings.local.json
// Work project uses fine-grained permissions
{
  "permissions": {
    "allow": [
      "Read(src/**)",
      "Edit(src/**)",
      "Bash(npm test)"
    ]
  }
}
```

**Result:**
- Personal projects: Full bypass via wrapper
- Work projects: Fine-grained permissions via config files
- Other directories: Default Claude Code behavior

<!-- section_id: "9d4ab946-5625-49e5-b604-99e7f0c8721b" -->
## Frequently Asked Questions

<!-- section_id: "440e6b57-a15d-4d7d-b728-42bfe1f68dbe" -->
### Q: Does this work with VS Code?

**A**: Only if you launch Claude Code from the terminal. If you launch VS Code from a GUI, it won't inherit your shell configuration.

**Workaround**: Set environment variables in VS Code settings:
```json
{
  "terminal.integrated.env.linux": {
    "CLAUDE_UNSAFE": "1"
  }
}
```

<!-- section_id: "b40f7198-441e-4a1a-98f0-7b8883354fca" -->
### Q: Can I use this with zsh?

**A**: Yes, the syntax is compatible. Just add the wrapper to `~/.zshrc` instead of `~/.bashrc`.

<!-- section_id: "1cc419e8-43db-403a-95c2-b41dde8ec679" -->
### Q: What about fish shell?

**A**: Fish uses different syntax. Here's the equivalent:

```fish
# ~/.config/fish/functions/claude.fish
function claude
    set -l claude_real /home/username/.nvm/versions/node/v22.20.0/bin/claude

    # Check for help/version
    for arg in $argv
        switch $arg
            case --help -h --version -v
                command $claude_real $argv
                return
        end
    end

    # Enable bypass in project directory
    if string match -q "/home/username/code/my-project*" $PWD
        command $claude_real --dangerously-skip-permissions $argv
    else
        command $claude_real $argv
    end
end
```

<!-- section_id: "e8e500e4-7a8e-4d80-b3ff-3f806ab59cac" -->
### Q: Can I check if bypass is active before running a command?

**A**: Yes, add a helper function:

```bash
claude-bypass-check() {
  if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/trusted"* ]]; then
    echo "✅ Bypass ACTIVE"
  else
    echo "❌ Bypass INACTIVE (normal permissions)"
  fi
}
```

Usage:
```bash
$ claude-bypass-check
✅ Bypass ACTIVE
```

<!-- section_id: "0d909763-0165-4556-8133-d9411bae475c" -->
### Q: How do I share this with my team?

**A**: Document it in your project's README and provide a setup script:

```bash
#!/bin/bash
# scripts/setup-claude-wrapper.sh

CLAUDE_PATH=$(which claude)
PROJECT_PATH=$(pwd)

cat >> ~/.bashrc << EOF

# Auto-generated Claude wrapper for $(basename "$PROJECT_PATH")
_claude_real="$CLAUDE_PATH"
if [ -x "\$_claude_real" ]; then
  claude() {
    for arg in "\$@"; do
      case "\$arg" in
        --help|-h|--version|-v)
          command "\$_claude_real" "\$@"
          return \$?
          ;;
      esac
    done

    if [[ "\$PWD" == "$PROJECT_PATH"* ]]; then
      command "\$_claude_real" --dangerously-skip-permissions "\$@"
    else
      command "\$_claude_real" "\$@"
    fi
  }
fi
EOF

echo "✅ Claude wrapper added to ~/.bashrc"
echo "Run: source ~/.bashrc"
```

<!-- section_id: "3139a031-10a4-43de-86a2-dfb0a6c1cf88" -->
## Related Documentation

- [Bypass Permissions Setup](./bypass-permissions-setup.md) - Configuration file approach
- [Fine-Grained Permissions](./fine-grained-permissions.md) - Alternative to bypass mode
- [Settings Hierarchy](./settings-hierarchy.md) - How settings interact

<!-- section_id: "d9e06536-b23c-4eb1-892e-48336086ada0" -->
## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0   | 2025-10-24 | Initial documentation created |

---
*This guide is part of the Universal Tools (Level 0.75) and provides advanced implementation patterns for Claude Code bypass permissions.*
