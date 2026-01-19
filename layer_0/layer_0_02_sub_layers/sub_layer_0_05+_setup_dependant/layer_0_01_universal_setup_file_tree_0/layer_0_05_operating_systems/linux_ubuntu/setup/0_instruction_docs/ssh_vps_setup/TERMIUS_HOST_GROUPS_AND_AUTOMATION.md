# Termius Host Groups and Automation Setup

**Status**: PARTIALLY WORKING
**Last Updated**: 2026-01-18 (session 2)

---

## Overview

This document covers the Termius host groups structure and automation attempts for managing SSH connections across multiple devices.

---

## Host Groups Strategy

### Naming Convention
- All lowercase
- Underscores for spaces
- Format: `for_<starting_device>` (group) and `for_<starting_device>_<target>` (host)

### Groups Structure

| Group Name | Purpose | Hosts |
|------------|---------|-------|
| `for_iphone` | Hosts to connect to from iPhone | vps, linux, windows (optional) |
| `for_laptop_linux` | Hosts to connect to from Linux laptop | vps, windows (optional) |
| `for_laptop_windows` | Hosts to connect to from Windows laptop | vps, linux |
| `for_vps` | Hosts to connect to from VPS | linux, windows (optional) |

### Host Naming Examples

| Host Label | In Group | Target |
|------------|----------|--------|
| `for_iphone_vps` | for_iphone | VPS (46.224.184.10) |
| `for_iphone_linux` | for_iphone | Linux laptop (100.73.84.89) |
| `for_laptop_linux_vps` | for_laptop_linux | VPS (46.224.184.10) |
| `for_laptop_windows_vps` | for_laptop_windows | VPS (46.224.184.10) |
| `for_laptop_windows_linux` | for_laptop_windows | Linux laptop |
| `for_vps_linux` | for_vps | Linux laptop |

---

## Connection Details

### VPS (Hetzner)
- **Public IP**: 46.224.184.10
- **Tailscale IP**: 100.93.148.5
- **User**: root
- **Auth**: SSH key

### Linux Laptop (Ubuntu)
- **Tailscale IP**: 100.73.84.89
- **Local IP**: varies (check with `ip addr`)
- **User**: dawson
- **Auth**: SSH key

### iPhone
- **Tailscale IP**: 100.75.210.27
- **Role**: Client only (no incoming SSH)

### Windows (Optional)
- **Local IP**: varies
- **User**: dawson
- **Auth**: SSH key (requires OpenSSH Server enabled)

---

## What Works

### Manual Termius App Configuration
- Creating hosts manually in Termius app
- Creating groups manually
- Termius account sync across devices
- SSH key import/export

### Account Sync
- Sign in with same Termius account on all devices
- Hosts and groups sync automatically
- Works on Windows, Linux, iPhone, Android

### SSH Config Integration
- Termius can import from `~/.ssh/config`
- Keys stored in `~/.ssh/` are accessible

---

## What Doesn't Work

### Termius CLI Automation
**Problem**: Termius CLI uses newer encryption algorithms incompatible with the vault

**Error observed**:
```
Error: Unsupported cipher: chacha20-poly1305
```

**Explanation**:
- Termius stores credentials in an encrypted vault
- Newer versions use chacha20-poly1305 encryption
- The CLI tool (especially older versions or certain builds) can't decrypt this
- This prevents scripted automation of host creation

**Attempted workarounds**:
1. Using .deb instead of snap (no improvement)
2. Exporting/importing JSON configs (requires manual vault access)
3. Using pass password manager as credential store (partial success)

### Scripted Host Creation
Cannot automate via scripts due to CLI limitations above.

---

## Pass Password Manager Setup

As a workaround for storing credentials securely on Linux:

### Installation
```bash
sudo apt install pass
```

### GPG Key Setup
```bash
# Generate GPG key
gpg --full-generate-key
# Select: RSA and RSA, 4096 bits, no expiration

# Initialize pass with your GPG key ID
pass init "YOUR_GPG_KEY_ID"
```

### Storing Credentials
```bash
# Store Termius password
pass insert termius/password

# Store SSH passphrases
pass insert ssh/vps_key_passphrase
```

### Retrieving Credentials
```bash
# Get password (copies to clipboard for 45 seconds)
pass -c termius/password

# Get and display
pass termius/password
```

---

## Current Implementation Status

| Task | Status | Notes |
|------|--------|-------|
| Create group structure in Termius | Pending | Use NEW HOST dropdown → New Group |
| VPS host configured | ✅ Done | 46.224.184.10, user: root, created via Quick Connect |
| Linux host configured | Pending | Need to add via Tailscale IP 100.73.84.89 |
| iPhone app installed | Pending | User to download, hosts will sync |
| Windows SSH server | Optional | For incoming connections |
| CLI automation | ❌ Blocked | Python 3.12 incompatibility (getargspec) |
| xdotool GUI automation | ✅ Working | Use --window flag to target specific windows |
| Pass password manager | ✅ Done | On Linux laptop |

---

## Recommended Workflow

Since CLI automation doesn't work:

1. **Set up hosts manually in Termius app** on any device
2. **Sign in to Termius account** on all devices
3. **Hosts sync automatically** via Termius cloud

### Manual Setup Steps

1. Open Termius app
2. Create groups: `for_iphone`, `for_laptop_linux`, `for_laptop_windows`, `for_vps`
3. Add hosts to each group with appropriate naming
4. Configure each host with:
   - Address (IP)
   - Username
   - SSH key (import from file or paste)
5. Sign in on other devices - everything syncs

---

## Files Related to This Setup

| File | Location | Purpose |
|------|----------|---------|
| `TERMIUS_CROSS_DEVICE_SETUP.md` | ssh_vps_setup/ | Connection matrix |
| `TERMIUS_LINUX_SETUP.md` | ssh_vps_setup/ | Linux installation |
| `IPHONE_QUICK_GUIDE.md` | ssh_vps_setup/ | iPhone setup steps |
| `FULL_MESH_SSH_PLAN.md` | ssh_vps_setup/ | Full connectivity plan |
| `~/.password-store/` | Linux home | Pass credentials |

---

## xdotool GUI Automation (Working Method)

Since the Termius CLI is broken, you can automate the GUI using `xdotool` on X11.

### Key Technique: Target Specific Windows

```bash
# Get the Termius window ID
TERMIUS_WIN=$(xdotool search --name "Termius" | head -1)

# Activate the window (bring to front and focus)
xdotool windowactivate --sync $TERMIUS_WIN

# Send keys to that specific window
xdotool key --window $TERMIUS_WIN ctrl+k

# Type in that window
xdotool type --window $TERMIUS_WIN "text to type"

# Click at coordinates (requires window to be focused)
xdotool mousemove 176 88 && xdotool click 1
```

### Coordinates and Visual Information

**Window identification:**
```bash
# Find Termius window ID
xdotool search --name "Termius" | head -1
```

**Key UI element coordinates (relative to window):**
| Element | Approximate Coordinates | Notes |
|---------|------------------------|-------|
| NEW HOST dropdown arrow | x=380, y=250 | Click this to reveal dropdown menu (not the button itself) |
| "New Group" option in dropdown | x=505, y=340 | Appears after clicking dropdown arrow |

**Host list entry visual:**
- Each host entry shows IP address and details like "ssh, telnet, root"
- Host entries are clickable to open connection
- Right-click for context menu options

### Creating Groups via Dropdown

To create a new host group:

1. Navigate to Hosts page (Ctrl+1 or click "Hosts" in sidebar)
2. Click the **downward arrow** next to "NEW HOST" button (not the button itself)
3. Dropdown menu appears with options:
   - New Group
   - Import
   - AWS Integration
   - DigitalOcean Integration
   - Azure Integration
4. Click "New Group" to create a new host group
5. Enter group name following naming convention (e.g., `for_iphone`)

**xdotool automation for creating a group:**
```bash
TERMIUS_WIN=$(xdotool search --name "Termius" | head -1)
xdotool windowactivate --sync $TERMIUS_WIN
sleep 0.5

# Click dropdown arrow (adjust coordinates as needed)
xdotool mousemove --window $TERMIUS_WIN 380 250
xdotool click 1
sleep 0.3

# Click "New Group" option
xdotool mousemove --window $TERMIUS_WIN 505 340
xdotool click 1
```

### Termius UI Navigation

**To access the NEW HOST dropdown menu:**
1. Go to Hosts page (click "Hosts" in sidebar or use Ctrl+1)
2. Click the **downward arrow** next to "NEW HOST" button
3. Dropdown shows:
   - New Group
   - Import
   - AWS Integration
   - DigitalOcean Integration
   - Azure Integration

**To create a host via Quick Connect (easiest method):**
1. Type IP in the search bar at top: `46.224.184.10`
2. Press Enter → "Choose protocol" dialog appears
3. Select SSH, click Continue
4. Enter username (e.g., `root`)
5. Click "Continue & Save" → Host is saved!
6. Choose authentication (Password or Public Key)

**To create a host via form:**
- Click "NEW HOST" button directly (not the arrow)
- Or use the "Create host" form in the main area

**To import from SSH config:**
- Click dropdown arrow → Import
- Select SSH config file

### Useful Tools

| Tool | Purpose | Install |
|------|---------|---------|
| `xdotool` | X11 GUI automation | `apt install xdotool` |
| `wmctrl` | Window management | `apt install wmctrl` |
| `scrot` | Screenshots | `apt install scrot` |

### Example: List Windows
```bash
wmctrl -l  # List all windows with IDs
xdotool search --name "Termius"  # Get Termius window ID
```

---

## Future Improvements

1. **Wait for Termius CLI fix**: Future versions may support newer encryption
2. **Use Termius export/import**: JSON backup can transfer configs between installs
3. **SSH config as source of truth**: Maintain `~/.ssh/config` and import to Termius
4. **Ansible for SSH config**: Automate SSH config file generation across machines

---

## Quick Reference

### Tailscale IPs (use these for cross-network access)
```
VPS:     100.93.148.5
Linux:   100.73.84.89
iPhone:  100.75.210.27
```

### SSH Commands (without Termius)
```bash
# To VPS
ssh root@100.93.148.5

# To Linux (from VPS or other)
ssh dawson@100.73.84.89
```

### Check Connectivity
```bash
# On any Tailscale device
tailscale status
tailscale ping 100.73.84.89
```
