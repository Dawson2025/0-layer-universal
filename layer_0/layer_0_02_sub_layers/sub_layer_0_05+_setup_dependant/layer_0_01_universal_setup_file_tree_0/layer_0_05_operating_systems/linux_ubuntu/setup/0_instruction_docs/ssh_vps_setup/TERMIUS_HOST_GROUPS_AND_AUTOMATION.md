# Termius Host Groups and Automation Setup

**Status**: PARTIALLY WORKING
**Last Updated**: 2026-01-18 (session 3)

---

## Overview

This document covers the Termius host groups structure and automation attempts for managing SSH connections across multiple devices.

---

## SSH Key Strategy

**IMPORTANT: Each device uses its OWN SSH key for outbound connections.**

This means:
- When connecting FROM iPhone → use iPhone's key
- When connecting FROM Linux laptop → use Linux laptop's key
- When connecting FROM Windows laptop → use Windows laptop's key
- When connecting FROM VPS → use VPS's key

### Key Configuration Per Group

| Group | Key to Use | Purpose |
|-------|-----------|---------|
| for_iphone | iPhone key (generated in Termius app) | iPhone connects OUT to other hosts |
| for_laptop_linux | Linux laptop key (~/.ssh/id_ed25519) | Linux connects OUT to other hosts |
| for_laptop_windows | Windows laptop key | Windows connects OUT to other hosts |
| for_vps | VPS key (/root/.ssh/id_ed25519) | VPS connects OUT to other hosts |

### Termius Keychain Setup

Each device's private key needs to be imported into Termius Keychain:

1. **iPhone key**: Generated directly in Termius iOS app → Settings → Keychain → Generate Key
2. **Linux laptop key**: Import `~/.ssh/id_ed25519` into Termius → Keychain → Import
3. **Windows laptop key**: Import from Windows SSH directory
4. **VPS key**: Import `/root/.ssh/id_ed25519`

### Host Configuration

When creating hosts in each group, assign the appropriate key:
- Hosts in `for_laptop_linux` → use the imported Linux key
- Hosts in `for_iphone` → use the iPhone-generated key
- etc.

### Public Keys (authorized_keys)

Each target machine's `~/.ssh/authorized_keys` must contain the PUBLIC keys of all devices that should be able to connect to it.

Current known public keys:
- **VPS**: `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICRiRcYM71J8iBgoPG6qzc220hzGJcSKiaT346zIWu4w root@ubuntu-4gb-nbg1-1`
- **Linux laptop**: `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOsafGsGzpQ+h/kQx5DE16EJXj3FwlPdDwE0Gf8LBUSF dawson@github`
- **iPhone (Termius)**: Check Termius app → Keychain → export public key

---

## Manual Steps Required

Due to GUI automation limitations with multi-line content (private keys), the following must be done manually:

### 1. Import Linux Laptop Key to Termius Keychain

1. Open Termius → Click "Vaults" tab
2. Click on the Key icon (🔑) in the left sidebar
3. Click "KEY" dropdown → Select to add new key
4. Fill in:
   - **Label**: `linux-laptop-key`
   - **Private key**: Copy entire content from `~/.ssh/id_ed25519`:
     ```
     -----BEGIN OPENSSH PRIVATE KEY-----
     [key content here]
     -----END OPENSSH PRIVATE KEY-----
     ```
   - Public key will auto-populate after valid private key is entered
5. Save the key

### 2. Assign Keys to Hosts

For each host in `for_laptop_linux` group:
1. Click on the host to edit
2. Scroll down to find "Key" field
3. Select `linux-laptop-key` from dropdown
4. Save

### 3. Add Linux Laptop Host to Groups

The Linux laptop (Tailscale IP: 100.73.84.89) needs to be added to:
- `for_vps` group (so VPS can connect to Linux laptop)
- `for_iphone` group (so iPhone can connect to Linux laptop)

For each:
1. NEW HOST → Enter details:
   - Address: `100.73.84.89`
   - Label: `for_vps_linux` or `for_iphone_linux`
   - Username: `dawson`
   - Parent Group: Select appropriate group
   - Key: Select appropriate key (VPS key for for_vps, iPhone key for for_iphone)
2. Save

### 4. Verify authorized_keys on Linux Laptop

Ensure `/home/dawson/.ssh/authorized_keys` contains public keys from:
- VPS: `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICRiRcYM71J8iBgoPG6qzc220hzGJcSKiaT346zIWu4w root@ubuntu-4gb-nbg1-1`
- iPhone (from Termius app)

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

## Termius Account Credentials

### Storage Location

Termius account credentials are stored in the `pass` password manager:

```bash
pass termius/email     # Termius account email
pass termius/password  # Termius account password
```

### Termius Encryption Password

When you enable Termius Vault sync, you may set an encryption password. This is:
- **Separate from** your Termius account password
- Used to encrypt your vault locally before syncing
- Required when signing in on new devices

If you set an encryption password, document it:
```bash
pass insert termius/encryption_password
```

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
| Create group structure in Termius | ✅ Done | All 4 groups created: for_iphone, for_laptop_linux, for_laptop_windows, for_vps |
| VPS host configured | ✅ Done | 46.224.184.10, user: root (via Quick Connect) |
| for_iphone group created | ✅ Done | Contains VPS host (needs key assigned) |
| for_laptop_linux group created | ✅ Done | Contains VPS host (for_laptop_linux_vps, needs key assigned) |
| for_laptop_windows group created | ✅ Done | Contains VPS host (for_laptop_windows_vps, needs key assigned) |
| for_vps group created | ✅ Done | Needs: Linux laptop host + key assignment |
| Linux host configured | ⏳ Pending | Need to add via Tailscale IP 100.73.84.89 to for_iphone, for_vps |
| **Import Linux key to Keychain** | 📋 Manual | Manual - see steps above |
| **Import VPS key to Keychain** | ⏳ Pending | Import VPS `/root/.ssh/id_ed25519` → Termius Keychain |
| **Configure host keys per group** | 📋 Manual | Manual - see steps above |
| Add Linux host to for_vps group | ⏳ Pending | Manual step required |
| Add Linux host to for_iphone group | ⏳ Pending | Manual step required |
| iPhone app installed | ⏳ Pending | User to download, hosts will sync |
| Windows SSH server | Optional | For incoming connections |
| CLI automation | ❌ Blocked | Python 3.12 incompatibility (getargspec) |
| xdotool GUI automation | ✅ Working | Use --window flag to target specific windows |
| Pass password manager | ✅ Done | On Linux laptop |

### Next Steps (Priority Order)

1. **Import Linux laptop SSH key into Termius Keychain**
   - In Termius: Keychain → Import → select `~/.ssh/id_ed25519`
   - This key is used for `for_laptop_linux` group hosts

2. **Assign keys to existing hosts**
   - Edit each host → select appropriate key from Keychain
   - `for_laptop_linux_vps` → Linux key
   - `for_laptop_windows_vps` → Windows key (when available)
   - etc.

3. **Add Linux laptop host** to `for_iphone` and `for_vps` groups
   - Address: 100.73.84.89 (Tailscale)
   - User: dawson

4. **Generate/import iPhone key**
   - In Termius iOS: Settings → Keychain → Generate Key
   - Add public key to Linux laptop's `~/.ssh/authorized_keys`
   - Add public key to VPS's `/root/.ssh/authorized_keys`

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

#### Adding Hosts to Groups

**Method: Use the Parent Group dropdown in Host Details panel**

1. Click on a host in the host list to open the Host Details panel (right side)
2. In the Host Details panel, click on the "Parent Group" field
3. A dropdown appears listing all available groups
4. Select the desired group (e.g., "for_iphone")
5. The change auto-saves immediately

**Important Notes:**
- If Termius account encryption is enabled, you may be prompted for your encryption password when syncing changes
- **Drag-and-drop does NOT work**: In testing, dragging a host to a group did not successfully assign it. Always use the Parent Group dropdown method instead.

**Host Details Panel UI Coordinates (relative to Termius window):**
| Element | Approximate Coordinates | Notes |
|---------|------------------------|-------|
| Host card in list | x=430, y=700 | Click to select and open details panel |
| Parent Group field | y=679 (in right panel) | Click to show group dropdown |
| Group dropdown options | Below Parent Group field | Appears after clicking Parent Group |

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
