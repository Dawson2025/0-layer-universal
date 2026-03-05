---
resource_id: "cfeb337c-ce32-4792-a78b-573fa72644cd"
resource_type: "document"
resource_name: "TERMIUS_LINUX_SETUP"
---
# Termius Setup for Linux

After fixing the login loop, install Termius on Linux to have the same SSH setup across all devices.

---

## Option 1: Snap (Recommended)

```bash
sudo snap install termius-app
```

---

## Option 2: Flatpak

```bash
flatpak install flathub com.termius.Termius
```

---

## Option 3: Download from Website

1. Go to https://termius.com/linux
2. Download the .deb package
3. Install: `sudo dpkg -i termius_*.deb`

---

## After Installation

### If Using Termius Account (Recommended)
1. Open Termius
2. Sign in with same account as Windows/iPhone
3. VPS host will automatically sync!

### If Not Using Account
Import from SSH config (already configured):

```bash
# The SSH config already has VPS configured
cat ~/.ssh/config
```

Or manually add:
- **Host**: VPS
- **Address**: 46.224.184.10
- **Username**: root
- **Key**: ~/.ssh/id_ed25519

---

## Quick Test

After setup, connect to VPS and run:
```bash
menu
```

You should see the VPS Quick Menu.

---

## Termius on All Devices

| Device | Status | Notes |
|--------|--------|-------|
| Windows | ✅ Installed | VPS host configured |
| iPhone | Pending | Download from App Store, sign in to sync |
| Linux | Pending | Install after login fix |

All devices will sync hosts if using the same Termius account.
