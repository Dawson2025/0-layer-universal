---
resource_id: "cfeb337c-ce32-4792-a78b-573fa72644cd"
resource_type: "document"
resource_name: "TERMIUS_LINUX_SETUP"
---
# Termius Setup for Linux

After fixing the login loop, install Termius on Linux to have the same SSH setup across all devices.

---

<!-- section_id: "d64c4616-1163-4339-9d7b-f85f5dc748e1" -->
## Option 1: Snap (Recommended)

```bash
sudo snap install termius-app
```

---

<!-- section_id: "ec176adb-9d6c-482d-8844-49b073b366df" -->
## Option 2: Flatpak

```bash
flatpak install flathub com.termius.Termius
```

---

<!-- section_id: "747b28ee-9f35-4929-a68d-d75c6a06fe99" -->
## Option 3: Download from Website

1. Go to https://termius.com/linux
2. Download the .deb package
3. Install: `sudo dpkg -i termius_*.deb`

---

<!-- section_id: "0eb7f8f6-db9a-450f-a878-97dbef5efcb6" -->
## After Installation

<!-- section_id: "41cb5b19-daa1-4378-b849-3e9b0577f337" -->
### If Using Termius Account (Recommended)
1. Open Termius
2. Sign in with same account as Windows/iPhone
3. VPS host will automatically sync!

<!-- section_id: "8147594b-a9ae-431a-a14d-e04b0f2b4a1a" -->
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

<!-- section_id: "4ad5e52a-18d3-4085-b9ac-a0fca542c706" -->
## Quick Test

After setup, connect to VPS and run:
```bash
menu
```

You should see the VPS Quick Menu.

---

<!-- section_id: "fc601176-ffad-4bfe-a62f-93d2755ef745" -->
## Termius on All Devices

| Device | Status | Notes |
|--------|--------|-------|
| Windows | ✅ Installed | VPS host configured |
| iPhone | Pending | Download from App Store, sign in to sync |
| Linux | Pending | Install after login fix |

All devices will sync hosts if using the same Termius account.
